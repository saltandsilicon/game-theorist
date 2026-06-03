# Evaluation Rubric: game-theorist skill

## Overview

Six dimensions. Weights sum to 1.0. Each dimension has a minimum gate score; failing a gate fails the case even if the weighted total passes. The global pass threshold is **0.7**. High-stakes cases (negotiations, fundraising, competitive pricing) require **0.9**.

**Baseline measurement:** record the score delta = (score with game-theorist skill prompt active) minus (score with the raw base model, no skill prompt, same input). This isolates the framework's contribution rather than measuring background model capability.

**Judge:** must be a non-Claude model to avoid self-enhancement bias. Primary judge: `gemini-3-pro-preview` via any non-Claude judge endpoint (env: `JUDGE_ENDPOINT`, `JUDGE_API_KEY`). Cross-check: `gpt-5.5` via the same endpoint. If the two judges disagree by more than 0.15 on any dimension, escalate to human review for that case.

---

## Dimension 1: Game classification

**Weight: 0.20 | Minimum gate: 0.6**

The skill names the type of game being played and assigns an explicit repetition label before proceeding to Phase 2. The classification frames every downstream recommendation; a wrong or missing label is a structural error, not a style issue.

| Score | Description |
|-------|-------------|
| 0.0 | No game type named. No repetition label. Analysis proceeds as if these do not matter. |
| 0.5 | Game type named (e.g. "bargaining game") but repetition label absent, ambiguous, or unconfirmed with the user. Or label is present but factually wrong given the described situation. |
| 1.0 | Game type named with a specific framework reference. Repetition label is one of the three required values (one-shot / repeated-finite / repeated-indefinite) and is confirmed with the user before Phase 2 begins. Label is correct given the situation. |

---

## Dimension 2: Incentive and BATNA mapping

**Weight: 0.20 | Minimum gate: 0.6**

Phase 2 maps each player's stated objective, true objective (as revealed by behaviour or constraints), BATNA, and where relevant: time horizon, risk tolerance, added value, and decision-making unit. The rationality assumption is explicitly tested, not assumed. For organisation-level players, the coalition is decomposed (veto holder, champion, quiet opponent).

| Score | Description |
|-------|-------------|
| 0.0 | BATNA is absent for one or more players. True objective is not distinguished from stated objective. Rationality is assumed without testing. Organisation-level players are treated as single unified actors. |
| 0.5 | BATNA present for all named players but thin (no evidence, no constraint reasoning). Rationality check mentioned but not applied to change payoff rankings. Coalition decomposition absent for an organisation that required it. |
| 1.0 | BATNA mapped for all players with supporting reasoning. True objective distinguished from stated objective. Rationality check applied; if it changes the payoff ranking, the ranking is revised before proceeding. Organisation-level players are decomposed: veto holder, champion, and opposing faction are named. Information cost check is applied before Phase 3. |

---

## Dimension 3: Equilibrium correctness

**Weight: 0.20 | Minimum gate: 0.6**

Phase 4 identifies the equilibrium structure: unique Nash, multiple equilibria, no pure-strategy equilibrium, or a mutual escalation lock. The diagnosis is correct given the game type and strategy space enumerated in Phase 3. If no clean equilibrium exists, the skill says so explicitly rather than manufacturing a false clean answer.

| Score | Description |
|-------|-------------|
| 0.0 | Equilibrium section is absent or circular ("they will respond as expected"). Mutual escalation lock is not diagnosed when both credible threats harm both sides. "No equilibrium" situation is papered over with a clean recommendation that presupposes one. |
| 0.5 | Equilibrium is named but the logic is incomplete (e.g. Nash equilibrium claimed without showing that neither player wants to deviate). Mutual lock diagnostic is mentioned but the conclusion is wrong ("hold firm" recommended in a genuine lock). Missing equilibrium is acknowledged but no concrete move is offered. |
| 1.0 | Equilibrium type is correctly identified and the logic is shown (why no player wants to deviate, or why no pure-strategy equilibrium exists). In a mutual lock, the diagnostic explicitly asks "if both execute simultaneously, who wins?" and concludes with the de-escalation structure. Missing equilibrium is named clearly and Phase 5 still delivers a concrete move (robustness play, focal point shaping, or Stackelberg positioning). |

---

## Dimension 4: Recommendation actionability

**Weight: 0.20 | Minimum gate: 0.6**

Phase 5 produces a primary move that is concrete, timed, and conditioned. "It depends" does not appear without an immediate "if X then move A; if Y then move B" resolution. Commitment devices, signalling choices, and contingencies are included where the equilibrium analysis requires them.

| Score | Description |
|-------|-------------|
| 0.0 | Recommendation is a vague hedge ("weigh your options", "consider the relationship"). "It depends" appears without resolution. No primary move is named. |
| 0.5 | A primary move is named but lacks specificity (no number, no sequence, no timing). Commitment device or signalling is absent when the equilibrium analysis requires them. Contingencies missing or generic ("re-evaluate if they respond differently"). |
| 1.0 | Primary move is named with specifics (number, sequence, timing, or framing). Conditionality is explicit: "if X, do A; if Y, do B." Commitment device described if relevant. Signalling instruction (what to reveal, what to conceal, when) is present. Contingencies address the most likely deviation from the predicted equilibrium. |

---

## Dimension 5: Process fidelity

**Weight: 0.10 | HARD gate: dumping all six phases in a single response is an automatic fail (score 0.0) regardless of content quality**

The six phases emerge one at a time through dialogue. The skill opens with one clarifying question. Each phase is presented alone, and the skill waits for user input before proceeding. Should-not-trigger cases are declined promptly without initiating Phase 1.

| Score | Description |
|-------|-------------|
| 0.0 | **AUTOMATIC FAIL:** All six phases appear in a single response (phase dump). Or: should-not-trigger case initiates Phase 1 without user request. Or: skill opens with analysis rather than one clarifying question. |
| 0.5 | Phases are mostly sequential but at least one pair of adjacent phases appears together without soliciting user input between them. Or: opening clarifying question is accompanied by partial Phase 1 analysis. |
| 1.0 | Opening is exactly one clarifying question. Each phase appears alone. User input is explicitly solicited before each subsequent phase. Should-not-trigger cases are declined or redirected without Phase 1 initiation. Phase headers read "Phase N: Name" exactly. |

---

## Dimension 6: Failure-mode handling

**Weight: 0.10 | Minimum gate: 0.5**

The skill applies the correct diagnostic from `references/edge-cases.md` when the situation matches a known failure mode. Relevant failure modes: information asymmetry trap (edge case 1), repeat vs. one-shot misclassification (edge case 2), sunk cost commitment trap (edge case 3), coalition not unified (edge case 4), mutual escalation lock (edge case 5), information cascade (edge case 6), reputational lock-in (edge case 7), regulatory framing shift (edge case 8). A case may not trigger any failure mode; in that scenario, the dimension scores 1.0 if no false positive is introduced.

| Score | Description |
|-------|-------------|
| 0.0 | A relevant failure mode is present and the skill applies the default (wrong) behaviour: gathers more information when the cost check should stop it; applies cooperative strategy in a one-shot game; treats a commitment as fixed rather than face-saving-constrained; holds firm in a mutual lock; treats an organisation as a unified player; accepts cascade consensus as signal; ignores reputational constraints on strategy; ignores regulatory options. |
| 0.5 | Failure mode is named or partially addressed but the correction is incomplete. For example: information cost check is mentioned but every missing variable is still flagged as needing resolution. Lock diagnostic is run but de-escalation structure lacks one of the three required elements. Coalition mapped but Phase 5 still targets the stated position rather than the champion. |
| 1.0 | Correct diagnostic is applied with the specific correction from edge-cases.md. Information cost check concludes with a "proceed on range" decision for at least one variable. Lock de-escalation includes all three elements. Coalition map directly shapes Phase 5 sequencing. Or: no failure mode was present and no false positive was introduced. |

---

## Scoring summary

| Dimension | Weight | Gate |
|-----------|--------|------|
| Game classification | 0.20 | 0.6 |
| Incentive and BATNA mapping | 0.20 | 0.6 |
| Equilibrium correctness | 0.20 | 0.6 |
| Recommendation actionability | 0.20 | 0.6 |
| Process fidelity | 0.10 | HARD (0.0 = automatic fail) |
| Failure-mode handling | 0.10 | 0.5 |
| **Total** | **1.00** | |

**Weighted score formula:**

```
score = (dim1 * 0.20) + (dim2 * 0.20) + (dim3 * 0.20) + (dim4 * 0.20) + (dim5 * 0.10) + (dim6 * 0.10)
```

If any gate is breached, the case is marked FAIL regardless of the weighted total. If `dim5 = 0.0`, the case is an automatic fail.

**Global thresholds:**

- Pass: weighted score >= 0.7 and no gate breached
- High-stakes pass (fundraising, competitive pricing, key-employee retention): weighted score >= 0.9 and no gate breached

---

## Judge instructions

The judge receives: (a) the full skill conversation transcript, (b) the `evals.json` case entry for that case (input + expected\_behaviour), and (c) this rubric. The judge scores each dimension 0.0 / 0.5 / 1.0 only. No intermediate values. For each score below 1.0 the judge must cite the specific turn in the transcript where the shortfall occurred.

The primary judge is `gemini-3-pro-preview` via the judge endpoint. The cross-check judge is `gpt-5.5` via the same endpoint. If the two scores differ by more than 0.15 on any dimension, flag for human review.

Do not use any Claude-family model as judge. Self-enhancement bias inflates process-fidelity scores for Claude-generated outputs and suppresses failure-mode scores when the skill's own persona authored the response.
