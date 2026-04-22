# Frameworks Reference

Eight core frameworks. Each maps to a class of situation. The skill selects the right one after
Phase 1: Deconstruction.

---

## 1. Prisoner's Dilemma / Zero-sum

**When**: Two parties have conflicting interests and one outcome. What one gains, the other loses,
or both lose if they fail to coordinate.

**The structure**: Each player can cooperate or defect. If both cooperate, both do reasonably well.
If one defects while the other cooperates, the defector wins big. If both defect, both lose. The
dominant strategy is to defect, even though mutual cooperation is better for everyone.

**Key insight**: Rational individual behaviour produces collectively bad outcomes. The equilibrium
is stable but Pareto-inferior.

**Business examples**:

- Two airlines pricing the same route (both discount until neither is profitable)
- Two startups racing to close the same enterprise deal
- Salary negotiation when both sides have real outside options

**What to do**: Change the payoff structure (make defection costly via contract), create
repeated-game dynamics (form a relationship so reputation matters), or find a commitment device that
makes cooperation credible.

---

## 2. Nash Bargaining Solution

**When**: Two parties negotiate a deal where both gain from agreement but disagree on how to split
the surplus.

**The structure**: Each player has a BATNA (best alternative to negotiated agreement). The surplus
is the difference between the deal value and both BATNAs combined. The Nash bargaining solution
splits the surplus based on each player's relative bargaining power, typically equally when power is
symmetric.

**Key insight**: Your BATNA is your real position. Improving your BATNA strengthens you more than
any negotiating tactic.

**Business examples**:

- Negotiating a partnership revenue split
- Term sheet negotiation with an investor
- Acquisition price negotiation

**What to do**: Before negotiating, improve your outside option. Know the other party's BATNA, it
sets the floor for what they will accept. The party with the worse BATNA concedes more.

---

## 3. Stackelberg Leader-Follower

**When**: One player moves first, the other observes and responds. The first-mover has a structural
advantage, or disadvantage, depending on the game.

**The structure**: The leader chooses a strategy knowing the follower will respond optimally. The
leader works backwards from the follower's response function to choose the move that maximises their
own outcome.

**Key insight**: In quantity competition (Cournot), being the leader is an advantage, you commit to
a quantity and the follower scales back. In price competition (Bertrand), being first can be a
disadvantage, the follower undercuts you.

**Business examples**:

- A market leader setting prices that forces competitors into a price-taker position
- A startup entering a market already occupied by an established player
- Announcing a product roadmap publicly to shape competitor investment decisions

**What to do**: Identify whether you are the leader or follower. If leader: commit credibly and
early. If follower: observe, wait, and exploit the leader's constraints.

---

## 4. Coordination Game / Focal Points

**When**: All parties benefit from coordinating on the same outcome, but there is no obvious way to
coordinate, especially without communication.

**The structure**: Multiple Nash equilibria exist. The question is which one will be selected.
Schelling's focal point theory: players converge on "salient" solutions, the obvious answer that
stands out without negotiation.

**Key insight**: In coordination games, the winner is often whoever makes their preferred
equilibrium the most salient one.

**Business examples**:

- Platform wars (VHS vs Betamax, iOS vs Android)
- Industry standards, whoever establishes the reference standard wins
- Two companies trying to agree on a joint venture structure without tipping their hand

**What to do**: Make your preferred outcome the focal point through public commitment, industry
lobbying, early adopter lock-in, or simply being first and loud.

---

## 5. Auction Theory

**When**: Multiple parties bid for a single prize. The mechanism design, how the auction is
structured, determines who wins and at what price.

**Key concepts**:

- **Winner's Curse**: In common-value auctions (where the prize is worth the same to all bidders),
  the winner tends to have the most optimistic estimate and overpays. Optimal bidding requires
  shading your bid downward relative to your estimate.
- **Revenue Equivalence Theorem**: Under certain conditions, all standard auction formats (English,
  Dutch, first-price, second-price) produce the same expected revenue for the seller.
- **Second-price (Vickrey) auction**: Bidding your true value is the dominant strategy. Use this
  when you want to elicit honest valuations.

**Business examples**:

- Bidding on a government contract
- Acquiring a company through a competitive process
- Google Ads / programmatic advertising
- Fundraising when multiple VCs are interested

**What to do**: In first-price auctions, shade your bid below your true valuation. In common-value
settings, shade further to correct for winner's curse. When running an auction (selling), consider
second-price formats to maximise participation and honest bidding.

---

## 6. Signalling and Commitment Devices

**When**: One party has private information the other wants. Or one party wants to make a threat or
promise credible.

**Signalling theory** (Spence): A signal is credible only if it is costly enough that the other type
cannot profitably mimic it. A cheap signal is worthless, anyone can send it.

**Commitment devices**: Removing your own flexibility makes threats credible. Burning the boats,
signing a public contract, making a public announcement, these constrain your future self and change
the other player's beliefs about what you will do.

**Business examples**:

- Hiring a known investor as a board member signals quality to future investors
- Publishing pricing publicly commits you to not offering secret discounts (credible commitment to
  fairness)
- A startup publicly announcing "we will not sell to [large competitor]" changes acquisition
  dynamics
- Education as a signal of ability (costly, therefore credible, even if it adds no skills)

**What to do**: To send a credible signal, make it costly. To make a threat credible, remove your
option to back down. To evaluate others' signals, ask: could someone who lacks the underlying
quality send this signal at a similar cost? If yes, the signal is noise.

---

## 7. Repeated Games and Reputation Equilibria

**When**: The same players interact repeatedly over time, and future payoffs matter.

**The structure**: In a one-shot game, defection is dominant. In a repeated game, cooperation can be
sustained as an equilibrium, because the threat of future punishment (retaliation, lost cooperation)
outweighs the short-term gain from defecting.

**Folk Theorem**: In infinitely repeated games, virtually any outcome including full cooperation can
be sustained as a Nash equilibrium, as long as players are sufficiently patient (discount rate is
high enough).

**Reputation effects**: In repeated games with uncertainty about player types, reputation becomes a
strategic asset. Being known as tough, reliable, or fair changes what others expect, and changes
what they do.

**Business examples**:

- Long-term vendor relationships (both sides cooperate because they will interact again)
- A VC's reputation in the founder community (affects deal access forever)
- How a company responds to the first employee who leaves shapes all future departures

**What to do**: In repeated interactions, choose your reputation on purpose. Decide early what you
want to be known for, reliable, tough, creative, and play consistently. The first defection is the
most expensive: it reveals your type.

---

## 8. Cooperative Game Theory / Shapley Value

**When**: Players can form coalitions and share the surplus. The question is how to divide payoffs
fairly given each player's contribution.

**Shapley value**: A method for fair division based on each player's marginal contribution across
all possible coalitions. Compute the average of what each player adds when they join each possible
subset of the coalition.

**Key insight**: The Shapley value is the uniquely fair solution given four axioms: efficiency (full
surplus distributed), symmetry (equal contributors get equal shares), null player (zero contributors
get zero), and additivity (contributions add up correctly).

**Business examples**:

- Splitting a joint venture profit among three partners with different contributions
- Attribution in a multi-channel marketing funnel (which channel deserves credit for the
  conversion?)
- Equity splits among co-founders with different roles and timing
- Revenue sharing in a platform ecosystem

**What to do**: When designing a coalition or profit-sharing arrangement, compute Shapley values to
ensure the split is defensible and stable. Unstable distributions (where some coalition would be
better off leaving) lead to defection.
