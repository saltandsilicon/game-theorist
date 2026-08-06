# Archive

The archive retains closed or superseded artefacts so that their provenance and lessons remain available.

## Rule

- Archive an artefact only when it is no longer the active owner of current work.
- Preserve the original content and its provenance.
- Never delete an artefact merely because it has been superseded.
- Keep an item in its active owner while it is paused, under review or awaiting a decision.
- Use the archive descriptor at `archive/archive.md`. Do not create a competing `archive/README.md`.

Add this header to an archived artefact:

```markdown
> Archived on <date>. Reason: <reason>. Provenance: <source path>.
```

## Replacement links

When an archived artefact has a replacement, add a relative Markdown link in the archived file and in any index that names it:

```markdown
Replaced by: [<replacement title>](<replacement path>)
```

The replacement link must point to the current owner. If the replacement is not yet known, leave the placeholder explicit and do not invent a destination.
