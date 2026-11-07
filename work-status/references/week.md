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

**Week of March 9, 2026**

**Key accomplishments**
- Query rewriting: shipped the synonym expansion service to 100% of EU traffic; zero-result searches down from 4.1% to 2.6% on the week.
- Index freshness: landed the incremental indexer PR; product updates now show in search within 5 minutes instead of the hourly batch.
- Relevance evals: finished the labelled set for furniture queries (1,200 pairs) with the catalogue team.

**Decisions**
- Query rewriting: we will not expand brand names, after two false-positive escalations from merchants; keeping an allowlist instead.

**Still open**
- Waiting on Infra for the extra Elasticsearch capacity before rolling the incremental indexer to US.
- Furniture relevance experiment carries into next week; need Lena's review of the metric definition.
- Light week otherwise: out Monday.
