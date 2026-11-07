# Weekly update

**Reader:** Aye's manager and teammates, usually in a Slack channel or a short email on Friday afternoon.
**Purpose:** keep people informed and surface anything that needs their help. Nobody is judging Aye's year on this; it should be quick to write and quick to read.
**Altitude:** ground level. Report what happened this week, in the words Aye would use at standup.
**Tone:** factual and modest. Credit is implicit in "I shipped"; no need to argue impact. Numbers go in when they are already at hand (a latency figure from a PR description, a count of tickets closed), not hunted for.
**Budget:** under about 250 words.

## Structure

Start with a bold title line: **Week of <Monday, Month D, YYYY>**. Then, each with a short bold header, in this order:

1. **Key accomplishments** — 3 to 6 bullets, outcome-oriented ("Shipped…", "Landed…", "Finished the design for…"), one line each, project name first.
2. **Decisions** — decisions made or agreed this week, one line each, with the reason in a few words. If none, say "No major decisions this week."
3. **Still open** — unresolved items, blockers, questions waiting on someone else, and what carries into next week. Name the person or team a blocker is waiting on; that is the most useful line in the update.

## What to leave out

- Routine reviews, meetings and small fixes unless they produced a result worth a line.
- Anything you did on Aye's behalf that Aye did not adopt.
- Personal items of any kind.

## Example

**Week of September 21, 2026**

**Key accomplishments**
- Ledger v2: landed the double-write cutover for payouts; 100% of new payouts now write to both ledgers with zero reconciliation diffs after 3 days.
- Payout retries: merged the retry-policy config PR; ops can now change backoff without a deploy.
- On-call: closed the SEV-3 from Tuesday (stale cache on refund status) and added a regression test.

**Decisions**
- Ledger v2: we will keep double-writing for two more weeks before flipping reads, to get a full billing cycle of diffs.

**Still open**
- Waiting on Risk for sign-off on the retry limits before enabling retries for high-risk merchants.
- Ledger v2 read cutover carries into next week; Priya is reviewing the runbook.
- Light week otherwise: two days out for the offsite.
