# Prompt index

This package ships no prompts yet. This file lists only prompts that are physically shipped under `tools/prompts/` in the instantiated project.

## Future listing format

When a prompt is added, list it here in the same change:

| Path | Purpose | Inputs | Output | Maintenance trigger |
|---|---|---|---|---|
| `<prompt path>` | `<what the prompt produces>` | `<required inputs>` | `<expected output>` | `<when the entry must be reviewed>` |

Do not list prompts that exist only in the control repository, a user environment or another project. Remove an entry when its shipped prompt is removed or renamed.
