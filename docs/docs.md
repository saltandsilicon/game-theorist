# Docs

`docs/` holds structured working documents that support project work. It is not a second home for current state, raw captures or shipped output.

## Plans

`plans/` contains executable sequences for a phase, feature or change. A plan records scope, order, dependencies and verification criteria. Update it when any of those change.

## Specifications

`specs/` contains observable behaviour, boundaries and acceptance criteria. A specification is the reference for what the project must do, not a record of an implementation session.

Review an existing plan, specification or requirements document with
`ce-doc-review` when the request is to improve the document. Keep
`write-our-docs` as the prose standard, not the reviewer.


## Research

`research/` contains source-backed investigation, notes and analysis. Preserve source details and provenance. Research informs a decision; it does not silently become current project state.

## Audits

`audits/` contains findings, evidence and checks about the project. An audit is evidence for a decision or correction, not the canonical owner of the fact it reports.

## Decisions

`decisions/` contains accepted, rejected or replaced choices, including Architecture Decision Records (ADRs). Each record names the context, decision, reasons and consequences.

## Maintenance classes

The governing maintenance classes are defined by the scaffold contract at `<control-repository>/docs/scaffold-contract.md`:

- **Living**: rewrite when its source, decision or owning system changes.
- **Append-only**: append entries; never silently rewrite history.
- **Curated**: modify after validation or a confirmed fact.
- **Template**: preserve structure, explicit placeholders and the absence of invented values.
- **Generated**: regenerate from the declared source rather than editing the output.
- **Raw**: preserve the source and its provenance; do not rewrite it.
- **Archive**: preserve a superseded artefact and link to its replacement when one exists.

## Decision trail

A plan, specification or ADR must include a `## Decision trail` section whenever execution depends on a prior arbitration. Prior arbitration includes a resolved choice between competing options, an ownership boundary, a rejected route or an approved exception.

When required, use this structure and replace every placeholder with observed information:

```markdown
## Decision trail

- **Question**: <question that required arbitration>
- **Options considered**: <options>
- **Decision**: <accepted route>
- **Authority**: <decision source>
- **Evidence**: <evidence supporting the decision>
```

When execution does not depend on a prior arbitration, omit the section rather than leaving an empty one.

## Specialist routes

| Surface or signal | Owner |
|---|---|
| `CLAUDE.md`, `AGENTS.md`, `.claude.md`, `.claude.local.md`, structural `rules/` issues | `agent-md-improver` |
| `AGENT.md`, agent manifest, evals or adapters | `write-an-agent` |
| Existing plan, specification or requirements document | `ce-doc-review` |
| Release notes, changelog or post-ship documentation | `document-release` |
| Commit, pull request, push or GitHub publication handoff | `gitmo` |

`AGENTS.md` is a repository instruction document. `AGENT.md` is a persistent
agent definition. They do not share an owner.

