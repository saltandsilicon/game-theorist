#!/usr/bin/env python3
"""Check project documents without network access, writes, secrets, or LLMs."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections.abc import Iterable
from pathlib import Path
from typing import Any

MARKDOWN_SUFFIXES = {".md", ".markdown"}
RAW_SUFFIXES = {
    ".bin", ".csv", ".gif", ".gz", ".jpeg", ".jpg", ".json", ".jsonl",
    ".pdf", ".png", ".tar", ".tsv", ".xml", ".yaml", ".yml", ".zip",
}
SECRET_NAMES = {".env", ".env.local", ".env.production", "credentials", "secrets"}
LOCAL_LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
HEADING = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")
PLACEHOLDER = re.compile(r"<[^>\n]+>|\[[^\]\n]+\]|\bNot yet recorded\b", re.IGNORECASE)
DATE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
CODE_SPAN = re.compile(r"`[^`\n]*`")
FENCED_BLOCK = re.compile(r"(?ms)^ *`{3,}.*?(?:^ *`{3,}[^\n]*\n?|\Z)")


def _link_body(text: str) -> str:
    # Code spans and fenced blocks document syntax, not live links.
    return CODE_SPAN.sub("", FENCED_BLOCK.sub("", text))
CACHE_DIRS = {".pytest_cache", "__pycache__", ".mypy_cache", ".ruff_cache", "node_modules", ".venv"}


def _in_cache_dir(relative_path: Path) -> bool:
    # Root-relative parts only: a parent directory named like a cache must not swallow the project.
    return bool(CACHE_DIRS & set(relative_path.parts))

REQUIRED_FIELDS = ("type", "title", "owner", "visibility", "status")
SECTIONS_BY_TYPE = {
    "state": ("Current state", "Blockers", "Next action"),
    "roadmap": ("Now", "Next", "Later", "Parked"),
    "scope": ("In scope", "Out of scope", "Extension criteria", "Non-goals"),
    "stack": (
        "Languages", "Tools", "Dependencies", "Services and APIs", "Accounts",
        "Commands", "Directory tree",
    ),
    "design": (
        "Identity", "Tone", "Typography", "Colours", "Layout", "Motion",
        "Assets", "Sources", "Checks",
    ),
    "log": ("Append-only rule", "Entry format", "Promotion rule", "Promotion gate"),
    "lesson": ("Maintenance rule", "Promotion gate", "Entry format"),
    "guide": (),
    "template": (),
}
MAINTENANCE = {
    "living": "rewrite-on-source-change",
    "append-only": "append-only",
    "curated": "modify-after-validation",
    "template": "verify-structure-placeholders",
    "generated": "regenerate-from-source",
    "raw": "immutable",
    "archive": "preserve-with-replacement-link",
}
SERVICE_FILES = {
    "00-inbox/AGENTS.md", "00-inbox/README.md", "archive/archive.md",
    "docs/docs.md", "handovers/README.md", "tools/prompts/README.md",
    "AGENTS.md", "CLAUDE.md",
}


def relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def violation(code: str, reason: str, **extra: str) -> dict[str, str]:
    result = {"code": code, "reason": reason}
    result.update(extra)
    return result


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str, bool]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, False
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return {}, text, True
    fields: dict[str, Any] = {}
    current_list: str | None = None
    for line in lines[1:end]:
        match = re.match(r"^\s*([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        list_match = re.match(r"^\s*-\s*(.*)$", line)
        if list_match and current_list:
            container = fields.setdefault(current_list, [])
            if isinstance(container, list):
                container.append(_yaml_mapping(list_match.group(1)))
            continue
        if match and current_list and line[:1] in (" ", "\t"):
            # Indented keys belong to the open container: a mapping-valued field
            # (generated:) or the last mapping of a list field (sources:).
            key, raw = match.groups()
            container = fields[current_list]
            if isinstance(container, dict):
                container[key] = _yaml_scalar(raw)
            elif not container:
                fields[current_list] = {key: _yaml_scalar(raw)}
            elif isinstance(container[-1], dict):
                container[-1][key] = _yaml_scalar(raw)
            continue
        if not match:
            continue
        key, raw = match.groups()
        if raw == "":
            fields[key] = []
            current_list = key
        else:
            fields[key] = _yaml_scalar(raw)
            current_list = None
    return fields, "\n".join(lines[end + 1 :]), True


def _yaml_scalar(raw: str) -> Any:
    raw = raw.strip().strip("\"'")
    if raw.lower() in {"true", "false"}:
        return raw.lower() == "true"
    if raw.lower() in {"null", "~"}:
        return None
    if raw.startswith("[") and raw.endswith("]"):
        return [_yaml_scalar(part) for part in raw[1:-1].split(",") if part.strip()]
    return raw


def _yaml_mapping(raw: str) -> Any:
    match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", raw.strip())
    if match:
        key, value = match.groups()
        return {key: _yaml_scalar(value)}
    return _yaml_scalar(raw)


def source_values(fields: dict[str, Any]) -> list[str]:
    raw = fields.get("sources", [])
    if isinstance(raw, list):
        values: list[str] = []
        for item in raw:
            if isinstance(item, str):
                values.append(item)
            elif isinstance(item, dict):
                for key in ("path", "source", "uri", "url", "resource"):
                    if key in item and isinstance(item[key], str):
                        values.append(item[key])
        return values
    return [raw] if isinstance(raw, str) and raw else []


def is_secret_or_excluded(path: Path, item: str) -> bool:
    return path.name in SECRET_NAMES or path.suffix.lower() in RAW_SUFFIXES or any(
        part in {"assets", "raw", "exports", "transcripts"} for part in Path(item).parts
    )


def document_class(item: str, path: Path, fields: dict[str, Any]) -> str:
    if is_secret_or_excluded(path, item):
        return "raw"
    if item.startswith("archive/") or item == "archive/archive.md":
        return "archive"
    generated = fields.get("generated")
    if generated is True or generated == "true" or isinstance(generated, dict):
        return "generated"
    doc_type = str(fields.get("type", "")).lower()
    if doc_type == "log" or item.endswith("WTF.md"):
        return "append-only"
    if fields.get("template") is True or fields.get("template") == "true":
        return "template"
    if doc_type in {"lesson", "decision"}:
        return "curated"
    if path.suffix.lower() in MARKDOWN_SUFFIXES:
        return "living"
    return "raw"


def headings(body: str) -> set[str]:
    return {match.group(1).strip() for line in body.splitlines() if (match := HEADING.match(line))}


def resolve_reference(root: Path, item: str, reference: str) -> Path | None:
    reference = reference.strip().split("#", 1)[0].split("?", 1)[0]
    if not reference or reference.startswith(("http://", "https://", "mailto:", "<")):
        return None
    if reference.startswith("/"):
        candidate = Path(reference)
    else:
        # Markdown semantics: relative links resolve from the document's folder.
        # Frontmatter sources (item == "") stay root-relative.
        base = (root / item).parent if item else root
        candidate = (base / reference).resolve()
    try:
        candidate.relative_to(root)
    except ValueError:
        return None
    if candidate.suffix == "" and not candidate.exists():
        candidate = candidate.with_suffix(".md")
    return candidate


def inspect_document(root: Path, path: Path, *, strict: bool = True, changed_items: set[str] | None = None) -> dict[str, Any]:
    item = relative(root, path)
    fields: dict[str, Any] = {}
    body = ""
    violations: list[dict[str, str]] = []
    source = str(path)
    if not path.exists():
        violations.append(violation("missing-path", "the inspected path does not exist"))
        return row(item, "invalid", source, "missing path", "living", MAINTENANCE["living"], violations)
    if is_secret_or_excluded(path, item):
        cls = "raw"
        return row(item, "valid", source, "excluded raw, binary or secret path", cls, MAINTENANCE[cls], [])
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        violations.append(violation("unreadable", f"cannot read document: {error}"))
        return row(item, "invalid", source, "unreadable document", "living", MAINTENANCE["living"], violations)

    fields, body, had_frontmatter = parse_frontmatter(text)
    cls = document_class(item, path, fields)
    policy = MAINTENANCE[cls]
    if strict and path.suffix.lower() in MARKDOWN_SUFFIXES and item not in SERVICE_FILES and cls != "archive":
        if not had_frontmatter:
            violations.append(violation("missing-frontmatter", "maintained Markdown requires YAML frontmatter"))
        elif text.startswith("---") and "\n---" not in text[4:]:
            violations.append(violation("invalid-frontmatter", "frontmatter has no closing delimiter"))
        for field in REQUIRED_FIELDS:
            if field not in fields:
                violations.append(violation("missing-frontmatter-field", f"frontmatter is missing {field!r}", field=field))
        if fields.get("template") is True or fields.get("template") == "true":
            if not PLACEHOLDER.search(text):
                violations.append(violation("template-placeholder", "template has no explicit placeholder"))
            if cls == "template" and (DATE.search(text) or re.search(r"https?://[^ <]+", text)):
                violations.append(violation("plausible-invented-value", "template contains a concrete date or URL"))
    if strict:
        doc_type = str(fields.get("type", "")).lower()
        for section in SECTIONS_BY_TYPE.get(doc_type, ()):
            if section not in headings(body):
                violations.append(violation("missing-section", f"required section {section!r} is absent", section=section))
    for match in LOCAL_LINK.finditer(_link_body(body)):
        ref = match.group(1).strip()
        target = resolve_reference(root, item, ref)
        if target is not None and not target.exists() and not PLACEHOLDER.search(ref):
            violations.append(violation("missing-link", f"local link target does not exist: {ref}", target=ref))
    for ref in source_values(fields):
        target = resolve_reference(root, "", ref)
        if target is not None and not target.exists() and not PLACEHOLDER.search(ref):
            violations.append(violation("missing-source", f"declared source does not exist: {ref}", target=ref))
    if cls == "generated":
        sources = source_values(fields)
        if not sources:
            violations.append(violation("generation-ownership", "generated document must declare sources"))
        if changed_items and item in changed_items and not any(_reference_item(root, ref) in changed_items for ref in sources):
            violations.append(violation("generated-output-modified", "generated output changed without a changed declared source"))
    return row(item, "invalid" if violations else "valid", source, "document inspected", cls, policy, violations)


def _reference_item(root: Path, reference: str) -> str:
    target = resolve_reference(root, "", reference)
    return relative(root, target) if target is not None and target.exists() else reference.strip().split("#", 1)[0]


def row(item: str, status: str, source: str, reason: str, cls: str, policy: str, violations: list[dict[str, str]]) -> dict[str, Any]:
    return {
        "item": item,
        "status": status,
        "source": source,
        "reason": reason,
        "document_class": cls,
        "maintenance_policy": policy,
        "violations": violations,
    }


def _repository_row(root: Path) -> dict[str, Any] | None:
    if (root / ".git").exists():
        return row(".repository", "valid", str(root / ".git"), "Git repository detected", "living", MAINTENANCE["living"], [])
    return row(".repository", "invalid", str(root), "Git repository not detected", "living", MAINTENANCE["living"], [violation("repo-without-git", "project has no Git repository")])


def all_candidates(root: Path) -> list[Path]:
    result = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        item = relative(root, path)
        if _in_cache_dir(Path(item)):
            continue
        if path.suffix.lower() in MARKDOWN_SUFFIXES or is_secret_or_excluded(path, item):
            result.append(path)
    return sorted(result, key=lambda candidate: relative(root, candidate))


def changed_from_git(root: Path) -> list[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), "status", "--porcelain", "--untracked-files=all"],
            check=True, capture_output=True, text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return []
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if len(line) < 4:
            continue
        value = line[3:]
        if " -> " in value:
            value = value.split(" -> ", 1)[1]
        paths.append(value)
    return paths


def inspect(root: Path | str, changed: Iterable[str] | None = None, *, include_repository: bool = True) -> list[dict[str, Any]]:
    root = Path(root).resolve()
    requested = None if changed is None else {str(value) for value in changed}
    paths = all_candidates(root) if requested is None else []
    if requested is not None:
        normalised: set[str] = set()
        for value in requested:
            candidate = Path(value)
            if candidate.is_absolute():
                try:
                    normalised.add(relative(root, candidate.resolve()))
                except ValueError:
                    normalised.add(value)
            else:
                normalised.add(Path(value).as_posix())
        changed_items = normalised
        # Rows are limited to document candidates; changed_items stays whole so a
        # changed non-document source still pulls in its generated consumers.
        paths = [
            root / item for item in sorted(normalised)
            if not _in_cache_dir(Path(item))
            and (Path(item).suffix.lower() in MARKDOWN_SUFFIXES or is_secret_or_excluded(root / item, item))
        ]
        all_rows = [(path, inspect_document(root, path, changed_items=changed_items)) for path in paths]
        # A generated consumer is inspected only when its declared source is one of the changed paths.
        for candidate in all_candidates(root):
            if candidate in paths:
                continue
            try:
                text = candidate.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            fields, _, _ = parse_frontmatter(text)
            if any(_reference_item(root, ref) in changed_items for ref in source_values(fields)):
                all_rows.append((candidate, inspect_document(root, candidate, changed_items=changed_items)))
        rows = [item[1] for item in sorted(all_rows, key=lambda pair: pair[1]["item"])]
    else:
        rows = [inspect_document(root, path) for path in paths]
    if include_repository and requested is None:
        repository = _repository_row(root)
        if repository is not None:
            rows.append(repository)
    return rows


def hook_rows(root: Path, mode: str) -> list[dict[str, Any]]:
    changed = changed_from_git(root)
    return inspect(root, changed=changed, include_repository=False) if mode == "changed" else inspect(root, include_repository=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--changed", nargs="+", metavar="PATH")
    parser.add_argument("--changed-from-git", action="store_true")
    parser.add_argument("--claude-stop-hook", action="store_true")
    parser.add_argument("--codex-session-end-hook", action="store_true")
    args = parser.parse_args()
    try:
        if args.claude_stop_hook or args.codex_session_end_hook:
            payload = json.loads(sys.stdin.read() or "{}")
            if args.claude_stop_hook and payload.get("stop_hook_active"):
                return 0
            rows = hook_rows(args.root.resolve(), "changed")
            invalid = [item for item in rows if item["status"] == "invalid"]
            if invalid and args.claude_stop_hook:
                print(json.dumps({"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": "Document checks found an invalid or stale changed document. Run the portable verifier for details."}}))
            elif invalid and args.codex_session_end_hook:
                print("Document checks found an invalid or stale changed document. Run the portable verifier for details.")
            return 0
        changed = changed_from_git(args.root) if args.changed_from_git else args.changed
        json.dump(inspect(args.root, changed=changed), sys.stdout, indent=2)
        sys.stdout.write("\n")
        return 0
    except Exception:
        # Hooks are advisory and must never block closure or reveal document content.
        if args.claude_stop_hook or args.codex_session_end_hook:
            return 0
        raise


if __name__ == "__main__":
    raise SystemExit(main())
