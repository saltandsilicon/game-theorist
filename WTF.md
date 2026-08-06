---
type: log
title: Corrections and failures log
owner: null
visibility: internal
status: draft
template: true
language: en-GB
---

# WTF log

> Raw record of corrections, failures and observed errors. This document is append-only.

**Update trigger**: Append an entry when a correction, failure, error or other material observed event occurs. Owning role: <owning role>.

**Writing route**: Use `write-our-docs` for agent-facing wording. Keep raw observations factual and unpolished enough to preserve evidence. Use `gitmo` only for commit, pull request or GitHub publication handoff.


## Append-only rule

Append new entries without rewriting, reordering or silently deleting earlier entries. Keep the original observation factual. Do not promote an entry implicitly.

## Entry format

The block below is a format only. It is not a log entry. Copy it, replace every placeholder with observed facts, and append the completed entry.

```markdown
## <YYYY-MM-DD> | <short description>

- Context: Not yet recorded. Owner: <owning role>.
- Observation: Not yet recorded. Owner: <owning role>.
- Correction or failure: Not yet recorded. Owner: <owning role>.
- Impact: Not yet recorded. Owner: <owning role>.
- Evidence: Not yet recorded. Owner: <owning role>.
- Immediate action: Not yet recorded. Owner: <owning role>.
- Follow-up: Not yet recorded. Owner: <owning role>.
```

## Promotion rule

Promote an entry to `LESSONS.md` only after the promotion gate is met. The gate requires either a repeatable pattern validated from one or more entries in this log, or a proven incident with evidence. Record the source, evidence, scope and owning role in `LESSONS.md`.

Keep the original entry here unchanged after promotion. A single unverified observation remains in this log and is not a lesson.

## Promotion gate

- [ ] <WTF entry reference or proven incident reference>
- [ ] Pattern or incident validated with evidence by <owning role>
- [ ] Scope and repeatable rule recorded by <owning role>
- [ ] Curated entry added to `LESSONS.md`
