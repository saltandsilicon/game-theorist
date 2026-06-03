# Contributing

Feedback is useful here. Open an issue or PR if you find a weak framework, a bad recommendation, a
broken install path, a missing edge case, or a better example. The skill should get sharper from
real strategic situations, not from theory alone.

## Single source of truth

The main skill lives in `skills/game-theorist/SKILL.md`.

Edit that file when you want to change how the skill behaves. Do not edit the generated copies in
`.cursor/` or `.windsurf/`, they are synced from the main skill by GitHub Actions.

## Adding frameworks

The skill's framework table maps situation types to analytical approaches. To add a framework:

1. Edit `skills/game-theorist/SKILL.md`: add a row to the Framework Reference table and, if the
   framework requires its own phase logic, add a section under Phase 3 or Phase 4.
2. Document it in `docs/frameworks.md` with the same structure as existing entries: when to use, the
   structure, key insight, business examples, what to do.
3. Add a worked example to `examples/worked-examples.md` if you have one.

## Adding resources

Edit `docs/resources.md` directly. Keep the existing structure (Books / Papers / Courses). One
paragraph per resource: what it covers and why it matters. No affiliate links.

## Adding examples

Edit `examples/worked-examples.md`. Follow the existing condensed format in that file: situation,
stakes, each side's position, the power balance, and the play. Use realistic but anonymised business
situations.

## Before you open a PR

Test the skill in at least one assistant with a real situation. The phases should fire in order, one
at a time. If the assistant returns all six phases at once, the SKILL.md is broken.

## Pull requests

Open a PR against `main`. Describe what you changed and why. If you are adding a framework, include
at least one example of it applied to a real situation type.
