# game-theorist: workspace context

## Skill overview

**game-theorist** is a six-phase game theory analysis skill for AI coding agents. It models strategic
situations (negotiations, pricing wars, market entry, partnerships, fundraising) and walks through:
Deconstruction → Incentive Mapping → Strategy Space → Equilibrium → Recommendation → Dynamic
Adaptation. One phase at a time, dialogue-driven.

### When to activate / redirect

**Use game-theorist when:** user asks "what's their incentive?", "how will they respond?",
"should I raise prices?", "how to negotiate?": any situation where another party's **strategic
response** is part of the problem. Slash: `/game-theorist`.

**Do NOT use for:** NPV/IRR calculations, email drafting, generic negotiation tips, pure educational
"what does X mean?" questions, descriptive root-cause analysis ("why is churn high?"), PRD writing.

**Exception:** "Should I take this job offer?" → NOT game-theorist (simple yes/no). But
"I'm getting competing offers from two companies" → IS game-theorist (independent actors with
their own incentives).

---

## What this project is

A skill-only repo for AI coding agents. Packages `game-theorist` and ships it to multiple platforms
(Claude Code, Codex, Gemini CLI, Cursor, Windsurf, Cline). No build step, no runtime. The "codebase"
is Markdown only. Public repo: `https://github.com/saltandsilicon/game-theorist`.

## Code structure

```
skills/game-theorist/SKILL.md              ← SINGLE SOURCE OF TRUTH. Never edit copies.
skills/game-theorist/references/
  frameworks.md                            Eleven game theory frameworks
  edge-cases.md                            Eight failure-mode diagnostics
  worked-examples.md                       Real-world case studies
  artefact-template.html                   HTML artefact template (filled by agent at Phase 6)
skills/game-theorist/tests/
  evals.json                               Evaluation test cases
  rubric.md                                Scoring rubric
docs/
  frameworks.md                            Framework reference
  resources.md                             Books, papers, courses
examples/
  worked-examples.md                       Case studies
  edge-cases.md                            Failure-mode diagnostics
  analysis-example.html                    Example HTML artefact (OpenAI board crisis)
demos/
  salary-negotiation-transcript.md         Full six-phase conversation demo
  wrong-call-correction-transcript.md      Demo: correcting a bad initial call
assets/
  game-theorist-knight.webp                Branding
  screenshots/                             Screenshot PNGs for README
.claude-plugin/                            Claude Code marketplace + plugin manifests
.github/workflows/sync-skill.yml           Auto-syncs SKILL.md to .cursor/ and .windsurf/
.cursor/rules/game-theorist.mdc            Cursor rule file
.mcp.json / AGENTS.md / GEMINI.md / .clinerules  Per-agent reference docs
```

**Key convention:** `docs/` and `examples/` mirror the corresponding files in
`skills/game-theorist/references/`. Edit the `skills/` version; push to main and the GitHub Action
syncs to Cursor/Windsurf. Public `docs/` and `examples/` should be updated when SKILL.md changes.

## Common commands

No runnable commands. There is no build step.

The HTML artefact is produced by the agent filling
`skills/game-theorist/references/artefact-template.html` at the end of a six-phase session.
No CLI invocation needed.

## Coding patterns & conventions

- **British English**: `colour`, `behaviour`, `modelling`, `organisation`, `program`.
- **No em dashes.** Use commas, colons, or full stops.
- **No filler**: clean of patterns like "actually", "leverage", "Additionally", "Moreover", "As such".
- **Concrete > abstract**: name the framework, the move, the condition.
- **No "it depends"**: end every analysis with a concrete move + explicit conditions.
- **Phase headers must read `Phase N: Name`** exactly.

## Test strategy

**No automated tests.** Minimum verification:

1. Read SKILL.md → verify six phase headers exist in order.
2. Run the skill in one agent with a real situation.
3. Phases fire in order, one at a time. If all six dump at once, the SKILL.md procedure is broken.

## Active workflows

- **Improve skill** → edit `skills/game-theorist/SKILL.md`, commit, push. Sync handles the rest.
- **Add framework** → edit SKILL.md + `skills/game-theorist/references/frameworks.md` + `docs/frameworks.md`.
- **Generate HTML artefact** → agent fills `skills/game-theorist/references/artefact-template.html` at Phase 6. No script to run.

## Available skills

| Skill | Location | Activation hints |
|-------|----------|-----------------|
| game-theorist | `skills/game-theorist/SKILL.md` | `/game-theorist`, "game theory", "what's their incentive", "how will they respond" |
| game-theorist (Cursor) | `.cursor/skills/game-theorist/SKILL.md` (synced) | Same |
| game-theorist (Windsurf) | `.windsurf/skills/game-theorist/SKILL.md` (synced) | Same |

## Recurring patterns

- **Phase-by-phase dialogue**: one phase at a time, wait for user input. Core contract.
- **BATNA-first**: map every player's outside option before enumerating strategies.
- **Dominance elimination**: eliminate dominated strategies before recommending moves.
- **Face-saving > face-attacking**: diagnose off-ramps for public commitments, never attack
  positions directly.
- **Coalition mapping**: for org-level players, map veto holder, champion, opposition.
- **Escalation lock detection**: if both sides' threats mutually destroy value, recommend
  unilateral conditional de-escalation instead of "hold firm."
- **Information cost check**: before Phase 3, "Would revealing that I need this info cost more
  than it's worth?" If yes, proceed with incomplete data.
- **No forced clean answer**: if no dominant strategy and no clean equilibrium, say so.

## Coding rules (do's and don'ts)

- **[Do] Edit `skills/game-theorist/SKILL.md`**: single source of truth.
- **[Don't] Edit `.cursor/skills/` or `.windsurf/skills/`**: auto-generated by the sync workflow.
  Redirect edits to SKILL.md.
- **[Do] Keep the six phase headers in `Phase N: Name` format.** The skill breaks if they drift.
- **[Don't] Include API keys or secrets in committed files**: the repo is public.
- **[Do] Test skill end-to-end**: phases must fire one at a time before marking changes complete.

## Communication style notes

- **British English** in all text output.
- **Action > discussion:** recommend, then do. Concrete over abstract.
- **No "it depends":** end every analysis with a concrete move and explicit conditions.
