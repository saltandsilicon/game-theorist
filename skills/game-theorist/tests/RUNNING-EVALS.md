# Running the evals

This folder contains manual eval cases for the skill.

Use them to check that the skill still behaves correctly after edits. The main thing to catch is
process drift: the skill must ask one question first, then run the six phases one at a time.

## Quick check

1. Pick a case from `evals.json`.
2. Run the skill with the case's `input` in your agent session.
3. Compare the transcript with the case's `expected_behaviour`.
4. Score it with `rubric.md`.

## What must not break

- The skill opens with exactly one clarifying question.
- Phase 1 appears before all other phases.
- The agent waits for user input between phases.
- Should-not-trigger cases do not start the six-phase flow.
- Phase 5 ends with a concrete move, not a vague hedge.

## Scoring

Use the six dimensions in `rubric.md`.

- General pass: weighted score >= 0.7, no gate breached.
- High-stakes pass: weighted score >= 0.9, no gate breached.
- Process fidelity is a hard gate. If the agent dumps all six phases at once, the case fails.

## Optional judge check

For a stricter review, paste the transcript, the selected case, and `rubric.md` into a separate
model session. Ask it to score each rubric dimension as `0.0`, `0.5`, or `1.0`, and to cite the turn
that caused any score below `1.0`.

This is optional. The evals are designed to be readable and useful without extra infrastructure.
