# Demo: Salary negotiation, late-stage startup

A complete conversation with the game-theorist skill. The user is a senior product designer being
recruited by a Series B startup. The situation is anonymised but based on a real negotiation
pattern. All six phases are run in sequence.

---

**User:** I need to negotiate a job offer. They came in at $155K. I am currently at $148K. They
seem excited but say the budget is tight.

**Agent:** Describe the situation in 2-3 sentences. Who are the players, and what is at stake?

---

**User:** It is a Series B startup, about 80 people, SaaS product. I am a senior product designer
with 7 years of experience. Their recruiter has called me three times in two weeks. The role has
apparently been open for about three months.

**Agent:** Phase 1: Deconstruction.

Game type: **sequential, one-shot in form but with reputation externalities.** You move (accept,
reject, counter), they respond. The recruiter's behaviour, three calls in two weeks and three months
open, is a signal. Either the role is hard to fill or you are the preferred candidate after failed
offers. Probably both.

One-shot or repeated: you will interact with this company for years if you join, but this
negotiation itself is one-shot. That matters. Be direct. Relationship preservation is post-offer.

Before I map incentives: do you have any other active offers or a genuine willingness to decline and
stay in your current role?

---

**User:** I have been doing a casual process at one other company but nothing firm. I could stay at
my current job but it is not exciting.

**Agent:** Phase 2: Incentive Mapping.

**You:**
- Stated objective: better compensation
- True objective: better compensation plus a role that is more stimulating
- BATNA: stay at current job (not bad but not exciting). No hard alternative offer.
- Time pressure: low (you have a job). But you care about this specific role.
- Risk tolerance: moderate (you are not desperate but you want this)

**Them (recruiter + hiring manager):**
- Stated objective: fill the role at $155K
- True objective: close the role. Three months open is expensive. The hiring manager is probably
  frustrated. The recruiter's credibility is on the line.
- BATNA: restart the search. Given three months already spent, their BATNA is poor.
- Time pressure: high. Every week unfilled is a cost and a signal to the team.

Key asymmetry: they need this closed more than you do. "Budget is tight" is standard recruiter
language that means almost nothing. It is designed to anchor your counter-offer low.

One question: do you know what a senior designer earns at comparable Series B companies in your
market? This matters for Phase 3.

---

**User:** Based on what I have seen, the range is probably $160-175K. Some outliers at $180K.

**Agent:** Phase 3: Strategy Space.

Your available moves:

1. Accept $155K. Dominated. You leave $5-20K on the table with a credible basis for more.
2. Counter at $160K. Modest. Signals you researched the market but did not anchor high.
3. Counter at $170K with anchoring rationale. Stronger. Sets the midpoint at $162-163K, which is
   your real target.
4. Counter at $175K with a framing device. Aggressive but defensible if done correctly.
5. Ask for a signing bonus instead of base increase. Useful if they have a hard base salary cap.

Dominated strategies: accepting $155K without countering is dominated by any counter-offer move.
Asking for $180K without a rationale is dominated by $175K with a rationale.

The strongest structure: **anchor at $170K, name your basis, offer a trade.** "Based on comparable
roles at Series B companies in this city, the band is $160-175K for my level. I am targeting $170K.
If the base is genuinely constrained, I am open to looking at the total package: signing bonus,
equity, or review timeline."

This does three things: (a) it anchors in the market, not your current salary; (b) it signals
flexibility without conceding on price; (c) it introduces alternatives that may be easier for them
to approve than a base increase.

Phase 4: Equilibrium.

If you counter at $170K: the equilibrium depends on their true budget. If they have room, they come
back at $162-165K. If they are genuinely constrained at $155K, they offer a signing bonus or
accelerated review. Either way, you end up above $155K. The Nash bargaining solution here splits the
surplus between their floor ($155K) and your anchor ($170K), which lands at approximately $162-163K,
unless your anchor credibly resets the midpoint higher.

If you stay silent after countering: silence after a counter is a commitment device. Do not fill
the silence. It signals you are comfortable with the alternative (staying put).

---

**User:** What if they come back and say they really cannot go above $158K?

**Agent:** Phase 4 continues: test the constraint before accepting it.

"Cannot go above $158K" is a different statement depending on what is driving it:

- **Hard cap (salary band):** real but often has workarounds (signing bonus, extra equity, faster
  review cycle, remote flexibility, PTO).
- **Recruiter authority limit:** the recruiter cannot approve more but the hiring manager can.
- **Test of your resolve:** they want to see if you fold.

You cannot know which without testing. Respond: "I hear you. Is the $158K a hard cap on base, or
is there flexibility in the total package? I want to make this work. I am just trying to
understand what we are working with."

This is a question, not a counter. It does not concede and it does not escalate. It forces them to
be specific. If they say "total package is flexible," you have your opening. If they say "base is
capped but we can do a $10K signing bonus," you are at an effective $168K equivalent in year one.
Take it.

---

**User:** They came back at $162K base, no signing bonus. Is this good?

**Agent:** Phase 5: Recommendation.

$162K is the predicted equilibrium outcome ($155K floor + $170K anchor divided). That is the model
working correctly.

Whether to accept depends on one thing you have not named: what is the equity situation? At a
Series B, $5-10K of additional salary matters less than whether the equity is worth something.

If you have not negotiated equity yet: do it now, before you accept. Ask for the equity grant in
units (not percentage), the last preferred price (for your own valuation), and the vesting schedule.
A standard four-year vest with a one-year cliff is normal. Anything less than four years or more
than a one-year cliff should be pushed back on.

If equity is reasonable: accept $162K, ask for a 6-month performance review with a named salary
target ($168K) as a milestone. This converts the current negotiation into a longer game where you
have a defined path to your real number. Get it in writing.

**Commitment device:** send a written summary of what you agreed to (base, start date, review
timeline, equity grant) before you sign anything. Paper-trails the verbal commitment and makes it
harder for them to walk it back when the offer letter arrives.

**Contingency:** if the offer letter comes in below $162K, do not sign and do not negotiate by
email. Call the recruiter. Paper trails create escalation dynamics. Calls resolve them.

---

**User:** One more thing: they offered 0.08% equity. Is that good?

**Agent:** Phase 6: Dynamic Adaptation.

0.08% at a Series B requires a calculation, not an opinion.

To evaluate it:

1. Ask for the total shares outstanding (fully diluted). 0.08% of 10M shares is different from
   0.08% of 100M shares.
2. Find the last round's preferred price (the Series B price per share). That gives you a current
   paper value for your grant.
3. Estimate a realistic exit multiple. Series B companies that make it to exit typically exit at
   5-15x their last round valuation. Apply that to the fully diluted cap table, not just the
   preferred.

At a typical Series B with a $50M post-money valuation and 0.08% fully diluted: your equity is
worth $40K today on paper. At a 5x exit ($250M), it is worth $200K pre-tax. At 10x, $400K. That
is equity-as-lottery-ticket, not compensation. It changes the risk calculation,
not the immediate economics.

If 0.08% feels low: the market for a senior designer at Series B is roughly 0.05-0.15% depending
on the stage and the role's criticality. You are in range. Ask if there is a refresh schedule
(additional grants tied to performance or tenure milestones). Good companies have them. It is a
proxy for how they think about retaining people long-term.

**Final framing:** you got $162K up from $155K, a 6-month review path, and equity in range. That
is a strong result given your BATNA was a mildly unsatisfying job, not a competing offer. The
negotiation worked because you anchored correctly, did not reveal urgency, and offered a trade
(total package flexibility) instead of drawing a hard line.

The role's quality matters more than the last $8K. If the role accelerates your career, it is
the right call.

---

*Analysis complete. Six phases, one situation, zero generic advice.*
