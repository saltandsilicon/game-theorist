# Contributing

## Single source of truth

All behaviour lives in `skills/game-theorist/SKILL.md`. Never edit the auto-generated copies in
`.cursor/`, `.windsurf/`, or `plugins/`. The GitHub Actions workflow syncs them on every push to
main.

## Adding frameworks

The skill's framework table maps situation types to analytical approaches. To add a framework:

1. Edit `skills/game-theorist/SKILL.md` — add a row to the Framework Reference table and, if the
   framework requires its own phase logic, add a section under Phase 3 or Phase 4.
2. Document it in `docs/frameworks.md` with the same structure as existing entries: when to use, the
   structure, key insight, business examples, what to do.
3. Add a worked example to `docs/examples.md` if you have one.

## Adding resources

Edit `docs/resources.md` directly. Keep the existing structure (Books / Papers / Courses). One
paragraph per resource — what it covers and why it matters. No affiliate links.

## Adding examples

Edit `docs/examples.md`. Follow the existing format: situation description, then all six phases
applied. Use realistic but anonymised business situations.

## Style

- British English throughout (colour, behaviour, modelling, organisation)
- No em dashes — use commas, colons, or full stops
- Phase headers match the skill exactly (Phase 1: Deconstruction, etc.)
- Concrete over abstract — name the framework, the move, the condition

## Pull requests

Open a PR against `main`. Describe what you changed and why. If you are adding a framework, include
at least one example of it applied to a real situation type.
