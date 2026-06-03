#!/usr/bin/env python3
"""Validate the game-theorist skill and plugin manifests before publishing.

Checks:
  1. SKILL.md has a parseable YAML frontmatter with name + description.
  2. plugin.json and marketplace.json are valid JSON.
  3. plugin.json version matches marketplace.json version.

Run locally:  python3 scripts/validate.py
Runs in CI on every pull request and push to main (.github/workflows/validate.yml).

Evals are NOT run here. They are metered and run manually (see tests/RUNNING-EVALS.md).
"""

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []


def load_json(rel):
    path = ROOT / rel
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"{rel}: file not found")
    except json.JSONDecodeError as exc:
        errors.append(f"{rel}: invalid JSON: {exc}")
    return None


# 1. SKILL.md frontmatter
skill = ROOT / "skills/game-theorist/SKILL.md"
text = skill.read_text(encoding="utf-8") if skill.exists() else ""
frontmatter = None
if not text.startswith("---"):
    errors.append("SKILL.md: missing YAML frontmatter (must start with ---)")
else:
    parts = text.split("---", 2)
    if len(parts) < 3:
        errors.append("SKILL.md: frontmatter not closed with ---")
    else:
        try:
            import yaml

            frontmatter = yaml.safe_load(parts[1])
        except ImportError:
            errors.append("pyyaml not installed (pip install pyyaml)")
        except yaml.YAMLError as exc:
            errors.append(f"SKILL.md: frontmatter is not valid YAML: {exc}")

if isinstance(frontmatter, dict):
    for key in ("name", "description"):
        if not frontmatter.get(key):
            errors.append(f"SKILL.md: frontmatter missing '{key}'")

# 2 + 3. Manifests valid and versions aligned
plugin = load_json(".claude-plugin/plugin.json")
market = load_json(".claude-plugin/marketplace.json")

plugin_version = plugin.get("version") if isinstance(plugin, dict) else None

market_version = None
if isinstance(market, dict):
    plugins = market.get("plugins") or []
    if plugins and isinstance(plugins[0], dict):
        market_version = plugins[0].get("version")

if plugin_version and market_version and plugin_version != market_version:
    errors.append(
        f"version mismatch: plugin.json={plugin_version} "
        f"marketplace.json={market_version}"
    )

if errors:
    print("VALIDATION FAILED:")
    for err in errors:
        print(f"  - {err}")
    sys.exit(1)

print(f"OK: frontmatter valid, manifests valid, version {plugin_version}")
