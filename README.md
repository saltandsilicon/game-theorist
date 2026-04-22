# game-theorist

**Apply defence-grade strategic reasoning to any competitive situation.**

A skill for AI coding agents that installs a former Pentagon deterrence analyst into your session.
Describe any situation - negotiation, pricing war, market entry, partnership, fundraising - and the
model gets built phase by phase, through dialogue.

Works with Claude Code, Codex, Gemini CLI, Cursor, Windsurf, and Cline.

---

## What it does

Most strategic advice jumps to conclusions. This skill builds a model first.

Six phases, one at a time:

1. **Deconstruction** - what game is actually being played? (often different from what you think)
2. **Incentive mapping** - what do the players truly want, not what they say they want?
3. **Strategy space** - what moves exist? which are dominated and can be eliminated?
4. **Equilibrium** - what outcome emerges if everyone acts rationally?
5. **Recommendation** - the concrete move, how to make it credible, and what to do if it fails
6. **Dynamic adaptation** - reputation, tit-for-tat, and changing the rules of the game entirely

---

## Example

```
You: Model this - I'm raising prices by 20%. My main competitor has cheaper infrastructure.
     They've been matching my prices for two years. What happens?

Agent: Sequential game, repeated. You're the Stackelberg leader - they react to your move.
       Two years of matching suggests they're signalling "we'll undercut if you diverge."

       What's their cost structure relative to yours? A) They're actually cheaper to operate,
       B) Similar costs, C) You don't know.
```

The model builds from there. You answer, the analyst integrates, moves to the next phase. No generic
advice. No "it depends." A specific recommendation with explicit conditions.

---

## Install

### Claude Code

**Plugin install (recommended):**

```bash
/plugin install game-theorist
```

**Manual:**

```bash
git clone https://github.com/saltandsilicon/game-theorist.git ~/.claude/skills/game-theorist
```

Then invoke with `/game-theorist` or describe a strategic situation.

### Codex

```bash
git clone https://github.com/saltandsilicon/game-theorist.git
cp -r game-theorist/skills/game-theorist ~/.codex/skills/
```

### Gemini CLI

```bash
git clone https://github.com/saltandsilicon/game-theorist.git
cp -r game-theorist/skills/game-theorist ~/.gemini/skills/
```

Then add to your `GEMINI.md`:

```
@./skills/game-theorist/SKILL.md
```

### Cursor

```bash
git clone https://github.com/saltandsilicon/game-theorist.git
cp game-theorist/.cursor/rules/game-theorist.mdc .cursor/rules/
```

### Windsurf

```bash
git clone https://github.com/saltandsilicon/game-theorist.git
cp -r game-theorist/.windsurf/skills/game-theorist .windsurf/skills/
```

### Cline

Add to your `.clinerules`:

```
@./skills/game-theorist/SKILL.md
```

---

## When to use it

| Situation                          | What the model surfaces                                                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Pricing against a competitor       | Whether you're in a zero-sum price war or a coordination game - and which move breaks the equilibrium in your favour                         |
| Negotiating a deal                 | The other party's true BATNA, which concessions cost you nothing but signal value to them                                                    |
| Responding to a competitive threat | Whether to retaliate, ignore, or redirect - and what each signals to the market                                                              |
| Fundraising / term sheet           | The investor's incentive structure, what "we're still interested" actually means, when to create urgency                                     |
| Partnership or M&A                 | Whether this is a positive-sum deal or one player extracting value from the other                                                            |
| Hiring a key person                | What the candidate's outside options are, how to structure the offer as a commitment device                                                  |
| Salary negotiation                 | Your real leverage, their constraints, and whether to anchor high or create a competitive dynamic                                            |
| Family or relationship conflict    | Whether it's a repeated game (it almost always is), what each party's true incentive is, and how to shift the equilibrium without escalating |
| Friend group dynamics              | Who the silent players are, what coordination failure looks like, and how to make the outcome you want the focal point                       |
| Personal decision with stakes      | Map your own incentives honestly, your BATNA, and what commitment device would make you follow through                                       |

---

## The frameworks

Eight core frameworks, each matched to a situation type. Full reference:
[`docs/frameworks.md`](docs/frameworks.md)

| Situation                                       | Framework                                        |
| ----------------------------------------------- | ------------------------------------------------ |
| Two parties, conflicting interests, one outcome | Prisoner's Dilemma / Zero-sum                    |
| Negotiation over a deal                         | Nash bargaining solution                         |
| Market entry / competitive threat               | Stackelberg leader-follower                      |
| Coordination needed (standards, platforms)      | Coordination game, focal points                  |
| Auction / bidding                               | Auction theory (winner's curse, optimal bidding) |
| Deterrence / threat credibility                 | Signalling, commitment devices                   |
| Long-term relationship                          | Repeated game, reputation equilibria             |
| Coalition building                              | Cooperative game theory, Shapley value           |

---

## Resources

Books, papers, and courses that informed this skill: [`docs/resources.md`](docs/resources.md)

---

## Files

```
game-theorist/
├── skills/game-theorist/SKILL.md   Source of truth - only edit this
├── docs/
│   ├── frameworks.md               Eight frameworks explained with examples
│   ├── resources.md                Books, papers, courses
│   └── examples.md                 Worked case studies
├── CLAUDE.md                       Claude Code reference
├── GEMINI.md                       Gemini CLI reference
├── AGENTS.md                       Codex reference
├── .clinerules                     Cline reference
├── .cursor/rules/                  Cursor rule
├── .windsurf/skills/               Windsurf skill
└── .github/workflows/sync-skill.yml  Auto-syncs SKILL.md across all formats
```

The `.github/workflows/sync-skill.yml` workflow auto-propagates any change to
`skills/game-theorist/SKILL.md` to all agent-specific locations on every push. Edit one file, all
tools stay in sync.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). All changes go through `skills/game-theorist/SKILL.md` ,
never edit the auto-generated copies directly.

---

## Licence

MIT
