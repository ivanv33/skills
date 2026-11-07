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
4. Be honest about misses. A goal that slipped, stated with the reason and what Aye did about it, reads as judgment; a goal that silently disappears reads as evasion when the manager remembers it.

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

**Q3 2026 review — Senior Engineer, Payments Platform**

**Summary**
I led the Ledger v2 write migration to completion and cut payout failures by two thirds, which together remove the two biggest sources of finance reconciliation work and on-call load on the team. I also took over on-call process ownership for the platform group.

**Goals and results**
- *Migrate all Ledger v2 writes* — done. Payouts and refunds double-write with zero reconciliation diffs over a full billing cycle; the read cutover is scheduled for October 14. Finance estimates this removes about 6 hours a week of manual reconciliation. (verify estimate)
- *Payout failure rate under 0.5%* — partially done: 1.4% in July to 0.6% in September. Configurable retries and the refund-cache fix account for most of the drop; the remaining failures are a bank-side issue now tracked with the Risk team.
- *On-call load down 30%* — missed: pages are down 22%. The alert cleanup slipped because I prioritised the migration; it is the first item in October.

**Scope, leadership and collaboration**
- Led the migration across Payments, Finance Engineering and SRE; wrote the cutover runbook that SRE now uses as the template for their own migrations.
- Ran the on-call retro and introduced a weekly SEV review for the platform group; both September SEV-3s had fixes merged within a day.
- Mentored Dana through her first production launch (retry-policy config), including the design review and rollout plan.
