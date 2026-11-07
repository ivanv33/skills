# Quarterly update

**Reader:** Aye's manager, who will use it to write Aye's performance review and defend the rating in calibration against people who have never seen Aye's work. Sometimes Aye pastes it straight into a self-review form.
**Purpose:** prove impact. The question the reader must be able to answer from this document alone is "what is different for the business because Aye was here this quarter, and at what level was Aye operating?"
**Altitude:** goals versus results. Events and even themes are now evidence, not content. Each section should read as a claim with its proof.
**Tone:** advocate, with receipts. This is the point in the ladder where modesty actively hurts Aye, because the people being compared against are not being modest. State what Aye led and what would not have happened otherwise; quantify every outcome you can; name the scope (cross-team, org-wide, customer-facing). Keep "(verify)" on any number or causal claim you inferred rather than found. Share credit precisely ("with Priya", "the SRE team owned the rollout") because precise credit is more believable than vague credit, not less. Read `impact.md` before writing.
**Budget:** under about 500 words.

## How to build it

1. Start from the quarter's monthly updates if they exist, then the goals in memory. For each goal, find the result and the number.
2. Make a list of candidate impact statements using the pattern in `impact.md` (what I did, what changed, by how much, why it mattered). Keep the 4 to 6 strongest. Everything else is either a supporting bullet or cut.
3. Separately list evidence of *how* Aye worked: things that show scope and level rather than output. Leading a project across teams, unblocking others, mentoring, setting a standard others adopted, running an incident, making a call that saved time. Perf processes grade on these explicitly, and they are the items most likely to be forgotten.
4. Keep each goal block at quarter altitude. It is a claim and its proof, not the story of how the work was done: the load test, who reviewed what, the date each piece landed, and PR numbers belong in the monthly updates. If a bullet does not change whether the reader believes the result, cut it. This is also how the budget is met; a quarter that runs long has almost always leaked month-level narrative into the goal blocks.
5. Be honest about misses. A goal that slipped, stated with the reason and what Aye did about it, reads as judgment; a goal that silently disappears reads as evasion when the manager remembers it.

## Structure

Bold title line: **Q<N> YYYY review — <Aye's role>** (use the fiscal quarter label if memory says the company uses one). Then, each with a short bold header:

1. **Summary** — two or three sentences: the quarter in one breath. What Aye owned, the headline outcome with its number, and the one thing that mattered most.
2. **Goals and results** — one block per goal Aye owned or was a named contributor to. Line one: the goal and its status (done / partially done / missed). Then 1 to 3 bullets of results with numbers. For a miss, the reason and what changed as a result.
3. **Impact beyond goals** — unplanned work that produced an outcome: incidents handled, a decision that avoided cost, a customer saved, a tool other teams adopted. Same impact pattern.
4. **Scope, leadership and collaboration** — how Aye worked: projects led, people mentored or unblocked, cross-team work, standards set, reviews and designs that shaped others' work. Concrete, with names of teams and projects. This section is where a level case is made; do not skip it even when it is short.
5. **What I learned / would do differently** — two or three lines. Candour here makes the rest credible, and review forms ask for it.
6. **Next quarter** — the three or four things Aye intends to deliver, phrased as outcomes.

## What to leave out

- Anything without an outcome, unless it is the honest statement that a goal has no outcome yet.
- Lists of PRs, tickets, or meetings. Use counts only where the count is impressive on its own.
- Weeks and months as organising units.
- Personal items of any kind.

## Example excerpt

**Q1 2026 review — Senior Engineer, Search Platform**

**Summary**
I led the zero-result reduction programme to its target a month early and made search index freshness a five-minute guarantee in two of three regions, which together removed the two most common merchant complaints about search. I also set up the offline relevance evaluation pipeline the ranking team now uses for every experiment.

**Goals and results**
- *Zero-result rate under 2.5%* — done: 4.1% in January to 2.2% in March. Synonym expansion, which I designed and shipped, accounts for most of the drop; the growth team attributes roughly 0.3% of search-led orders to it. (verify attribution)
- *Index freshness under 10 minutes in all regions* — partially done: EU and US at 5 minutes, APAC still hourly. The APAC rollout is blocked on an Infra capacity request I opened on March 12; it should have gone in during February.
- *Offline relevance evals for the top 3 categories* — missed: one of three. I underestimated labelling effort and moved the remaining sets to a vendor in late March; apparel lands in April.

**Scope, leadership and collaboration**
- Led the synonym programme across Search, Catalogue and Growth; handed the dictionary tooling to Catalogue so it runs without me.
- Built the offline eval pipeline the ranking team now gates experiments on; two experiments were stopped before A/B on its score.
- Mentored Omar through his first production launch (the incremental indexer), including the rollout plan and the on-call handover.
