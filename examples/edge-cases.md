> **Note for contributors:** The corrections described below are already implemented in
> `SKILL.md`. Each entry explains *why* a phase is structured the way it is, not what
> remains to be added. Read these as rationale, not as a to-do list.

# Edge Cases

Eight failure modes where the default six-phase analysis produces bad advice. Each entry names
the problem, explains why the skill's default behaviour goes wrong, and provides the correction.

---

## 1. Information asymmetry trap

**Problem:** The skill defaults to "gather more information before moving." In Phase 1
(Deconstruction) and Phase 2 (Incentive Mapping), it encourages the user to map the other side's
true objectives and constraints. The implicit assumption is that more information is always better.

In high-stakes negotiations, this assumption fails. Asking too many questions reveals what you do
not know. A counterpart who notices you probing for their BATNA will raise their floor. A supplier
who sees you researching alternatives will accelerate the timeline. The information-gathering itself
is a costly signal.

The bigger failure: in some situations, acting on incomplete information with a plausible bluff
strictly dominates waiting. If the other side believes you have information you do not have, and
their behaviour under that belief is better for you than their behaviour under accurate information,
the bluff is the rational move.

**Correction:** At the end of Phase 2, add an explicit check before proceeding: "Would revealing
that you need this information cost more than the information is worth?" If the answer is yes, skip
to Phase 3 with the information you have and treat the missing variable as a range rather than an
unknown. Move on imperfect data. Acknowledge the uncertainty explicitly in Phase 5 as a contingency
condition rather than a reason to delay.

---

## 2. Repeat game vs. one-shot misclassification

**Problem:** The skill mentions game repetition in Phase 1 but does not force a classification. The
default analysis drifts toward cooperative strategies (tit-for-tat, reputation preservation,
relationship investment) because these are the frameworks that produce satisfying, nuanced advice.
But they are wrong for one-shot interactions.

In a one-shot game, reputation concerns are lower. Defection is often rational. The long-term costs
of aggressive tactics disappear when there is no long-term. A founder negotiating with a strategic
acquirer they will never see again, a one-time contractor renegotiating a final invoice, a company
exiting a supplier relationship: these are all one-shot games where the cooperative playbook is
actively harmful.

The misclassification runs in both directions. Users in genuine repeat games sometimes assume
one-shot dynamics and act aggressively, destroying relationships that would have compounded.

**Correction:** Make game-type classification a hard gate at Phase 1, not a soft consideration.
The output of Phase 1 must include one of these three explicit labels:

- **One-shot**: no anticipated future dealings with this player or their network. Apply pure EV
  maximisation. Reputation effects are minimal.
- **Repeated, finite**: known endpoint (e.g., a vendor contract with a set term). Cooperation
  breaks down near the end (unravelling effect). Apply forward-looking strategy but with a
  discounted cooperation horizon.
- **Repeated, indefinite**: ongoing relationship with no clear endpoint. Full tit-for-tat and
  reputation logic applies.

The classification changes Phase 3 (which strategies are available) and Phase 5
(recommendations). Surface the label prominently and ask the user to confirm it before proceeding.

---

## 3. Sunk cost commitment trap

**Problem:** When a counterpart has publicly committed to a position (a bid submitted, a term
sheet signed, an announcement made), the skill treats their stated position as approximately fixed
and works around it. This is wrong.

Sunk costs do not bind rational actors. What binds them is face-saving. The actual constraint is not
the position itself but the cost of being seen to abandon it. A supplier who publicly announced a
22% price increase cannot simply drop to 5%. This is not due to economic constraints; their other customers are watching. A VC who told their LP committee they offered $12M pre cannot
come back with $10M without an explanation.

The skill's default is to accept the commitment and find creative structures around it. This
concedes too much. The correct move is to identify the face-saving off-ramp and design the
negotiation around providing it.

**Correction:** Add an explicit step in Phase 3: "Has this player made a public or internal
commitment to their current position? If yes, identify the face-saving mechanism before proposing
any counter." The mechanisms are usually one of three types: (a) new information that justifies a
change ("given that X has changed..."), (b) a reframe that makes the new position continuous with
the old one ("this is consistent with what we said because..."), or (c) a structural change that
makes the old commitment technically inapplicable ("the deal structure is now different enough
that..."). Never attack the position directly. Attack the conditions that made it necessary. Offer a
new condition that makes a new position logical and face-saving. In Phase 5, the primary
recommendation must include the face-saving vehicle explicitly, not as an afterthought.

---

## 4. The coalition that is not unified

**Problem:** The skill models "the other side" as a single player with a single BATNA, a single set
of incentives, and a single decision-making process. This is almost never true.

Procurement committees, VC partnerships, co-founder teams, family offices, and enterprise buying
groups all have internal fault lines. The stated position is the output of an internal negotiation
that happened before you entered the room. The person across the table may not agree with the
position they are presenting. They may have been overruled internally. They may need the deal more
than their organisation's official stance suggests.

Missing this structure means missing the actual game. The target is not the organisation's stated position. It is the most favourable internal faction.

**Correction:** Add a mandatory step in Phase 2: "Map the decision-making unit. For each player,
identify: (a) who has veto power, (b) who is the internal champion, (c) who is quietly opposed, and
(d) whose incentives diverge from the organisation's stated incentives." Then in Phase 5: target
the champion with the information they need to win internally. Neutralise the veto holder's
objection before it surfaces. Do not waste time on the vocal opponent. Their opposition is
internal theatre. The deal is won or lost with the champion and the veto.

This changes the sequencing of Phase 5 entirely. The first move is often not a public position.
It is a private conversation with the internal champion.

---

## 5. Mutual escalation lock

**Problem:** When both parties have made credible, costly threats that, if executed, harm both
sides, the skill recommends holding firm. "Maintain your commitment device." "Do not concede under
pressure." This advice is correct for a test of resolve. It is wrong for a mutual escalation lock.

A lock is a specific condition: both sides have committed publicly and credibly to positions that,
if held simultaneously, produce the worst outcome for everyone. Classic prisoner's dilemma at the
macro level. The advice to "hold firm" treats a lock like a test of resolve, and in a lock that
destroys value for everyone including you.

The two situations look similar from the inside. Both involve credible threats. Both involve
pressure to concede. The difference is whether the other side also loses if they execute their
threat.

**Correction:** Introduce a diagnostic step in Phase 4: "Is this a test of resolve or a mutual
escalation lock?" The diagnostic is: "If both sides execute their threats simultaneously, who wins?"
If the answer is "neither side wins," it is a lock. In a lock, the strategy inverts: the first
mover who de-escalates unconditionally, with a stated condition attached, can extract a
concession precisely because they broke the impasse and the other side needs relief.

The de-escalation move must be: (a) unilateral (you move first, no pre-coordination), (b)
unconditional in form but conditional in language ("I am withdrawing X. I expect this creates space
for you to withdraw Y. If not, I reserve the right to re-escalate."), and (c) framed as confidence,
not weakness ("We are comfortable enough in our position to remove this threat and resolve this
through direct negotiation."). The skill should flag the mutual lock pattern explicitly and offer
this de-escalation structure as the primary recommendation when it is detected. In Phase 5, the
primary strategy must name the specific de-escalation move, the timing, and the conditional
language to use.

---

## 6. Information cascade

**Problem:** The skill treats each player's stated beliefs as independent inputs. In reality,
beliefs in a market or group context are often cascades - each actor observing the actions of
prior actors and updating their beliefs accordingly, regardless of their own private signal.

When an information cascade is running, the observed behaviour of players tells you almost nothing
about their private information. A VC who passes is not necessarily expressing a negative view on
your company; they may be the fourth firm in a row to pass, each one inferring from the prior
passes that there is something wrong, even if every individual firm's private signal was neutral.
The cascade has replaced independent assessment with herding.

The skill's default error is to take observed consensus as evidence of underlying reality. "Four
people rejected this deal structure" leads to "the market has assessed this deal structure as
problematic." That inference is wrong if those four rejections themselves drove subsequent
rejections. You may be facing a cascade, not a verdict.

**Correction:** In Phase 2, add an explicit cascade diagnostic: "Is there a sequence of observable
prior decisions by similar players that the current player is likely aware of? If yes, treat their
stated or observed position as potentially cascade-driven, not signal-driven." Then in Phase 5: the
move is to break the cascade mechanism by providing a credible private signal - new information,
an external validator, or a change in deal structure large enough to be read as a discontinuity.
The goal is not to argue against the consensus; it is to make the consensus irrelevant by
restarting the information flow.

---

## 7. Reputational lock-in

**Problem:** The skill models reputation as an asset you accumulate and protect. It is also a
constraint. A player with a strong reputation for a particular style of behaviour - aggressive
negotiation, fast decision-making, always anchoring high - cannot easily deviate from that
reputation without triggering reinterpretation of their past behaviour and future credibility.

The skill's default error is to treat your own reputation as fixed background and optimise moves
within it. This misses the cases where your reputation is itself the binding constraint: you cannot
make the dominant move because doing so would require acting out of character, and the
out-of-character signal would cost more than the gain from the move.

The symmetric error applies to counterparts. A negotiator known for never bluffing cannot make a
credible bluff even when a bluff is the optimal play. A firm known for hostile acquistions cannot
make a credible friendly offer to a target that has been watching them. The reputation locks out
the strategy.

**Correction:** In Phase 3, add a reputation filter before finalising the strategy space: "Which
moves are excluded because your reputation makes them non-credible? Which moves are excluded
because the counterpart's reputation makes the expected response non-credible?" Strategies that
require one side to act out of established character should be flagged as low-probability and
high-cost in Phase 5. If the optimal strategy requires reputation-inconsistent behaviour, Phase 6
(Dynamic Adaptation) should address what prior moves would need to have been made, or what
structural change would make the deviation credible. In some cases the correct recommendation is:
the optimal move is not available to you given your current reputation, and the plan is to earn it.

---

## 8. Regulatory framing shift

**Problem:** The skill models strategic situations as closed games between identified players with
fixed payoff structures. Regulatory environments are exogenous variables that change the payoffs
without changing the players.

The error shows up when one player has the ability to shift the regulatory frame - lobbying for
new rules, invoking existing regulations in novel ways, triggering antitrust review, or simply
being the first to involve a regulator. The skill does not model this as a strategic move because
it reads like a move outside the game. It is not. It is a second-order move that changes the rules
of the first-order game.

A competitor who cannot win on price can potentially win by triggering a regulatory review that
delays your product launch. A supplier who lacks bargaining power in negotiation can gain it by invoking
employment regulation, environmental compliance, or data protection review. A founder outgunned in
a term sheet negotiation can shift the frame by having counsel invoke securities law on a
technicality. These are all moves within a larger game.

**Correction:** In Phase 3 (Strategy Space), add an explicit category: "Second-order moves that
change the rules of the game." For each player, ask: "Does this player have access to a regulatory,
legal, or institutional mechanism that would change the payoff structure if invoked?" If yes, model
the regulatory option as one available strategy, with its own costs (relationship damage, legal
fees, reputational signal) and benefits (altered payoff matrix for the underlying game). In Phase 5,
if the counterpart has unexercised regulatory options, acknowledge that the current equilibrium is
contingent on them not invoking those options, and include a contingency for the case where they
do. Do not treat the absence of regulatory escalation as its impossibility.
