# Yearly update (self-review / brag doc)

**Reader:** the people who decide Aye's rating, compensation and promotion: the manager writing the review, the skip-level, a promotion committee reading a packet. Often Aye's own future self, mining it for a résumé or a new-job conversation.
**Purpose:** make the case for Aye's level and trajectory. A year has too much in it to list; the document has to say what the year was *about* and let the strongest evidence carry it.
**Altitude:** narrative arc. Three to five storylines that explain the year, each told as before/after. Scope expansion over time is itself a storyline: what Aye was trusted with in January versus December.
**Tone:** the strongest honest case. Claim ownership and outcomes plainly, in the first person, with numbers, and connect them to what the business cares about. Where Aye operated at the next level (set direction, owned something cross-team, made others more effective, was the person people came to), say so in those terms, because promotion cases are built from exactly that language and the reader is looking for it. Every claim still needs a trace back to evidence; "(verify)" still marks inference. Read `impact.md` before writing.
**Budget:** under about 800 words. If Aye asks for a longer brag doc for their own records, drop the budget but keep the structure.

## How to build it

1. Start from the year's quarterly updates if they exist, then monthly, then memory. You are looking for the handful of outcomes that would survive being summarised in one sentence by a skip-level.
2. Pick the storylines. Good ones: a project owned end to end, a metric moved over the year, a responsibility gained, a problem that stopped recurring, a capability the team did not have in January. Each storyline gets a before, an after, a number, and what Aye specifically did to cause it.
3. Collect the level evidence separately: direction set, decisions made that others followed, cross-team ownership, people grown, standards or tools adopted beyond the team, the hard calls. Promotion rubrics are written in these terms and this section is the one that gets read twice.
4. Write the growth section honestly: what Aye could not do in January and can now, what went wrong and what changed because of it. It is the section that makes the rest trustworthy.
5. End with where Aye is heading, phrased as outcomes and scope, not tasks.

## Structure

Bold title line: **YYYY in review — <Aye's role>** (or **YYYY self-review**, if memory shows Aye's company uses that term). Then, each with a short bold header:

1. **The year in three sentences** — what Aye owned, the headline outcomes with numbers, and how Aye's scope changed between the start and end of the year.
2. **Storylines** — 3 to 5, each a bold one-line title followed by a short paragraph or 2 to 4 bullets: before, what I did, after (with the number), why it mattered to the business.
3. **Operating level** — evidence Aye worked at (or above) the expectations of the level: direction set, cross-team ownership, decisions others followed, people mentored and their outcomes, standards or tooling adopted outside the team, incidents or crises led. Concrete, named, no adjectives doing the work.
4. **Growth and misses** — two to four lines: what Aye learned, what missed and what changed because of it.
5. **Next year** — the scope and outcomes Aye intends to take on, in a few lines.

## What to leave out

- Anything a quarterly update would have called a supporting bullet. At year level only outcomes and level evidence survive.
- Quarters and months as organising units, except to show a before/after.
- Personal items of any kind, even ones that explain a slow quarter; those belong in a conversation, not the document.

## Example excerpt

**2026 in review — Senior Engineer, Payments Platform**

**The year in three sentences**
I took Ledger v2 from a design doc to the system of record for all payout and refund writes, and cut payout failures from 2.1% to 0.4% along the way. Together those removed roughly a day a week of finance reconciliation and about a third of the team's on-call pages. By Q3 I owned the platform group's on-call process and the migration across three teams, up from owning a single service in January.

**Storylines**

**Ledger v2 became the system of record.** In January it was a design doc with no owner. I took it on, split it into write migration and read cutover, and drove it across Payments, Finance Engineering and SRE. All writes migrated by September with zero reconciliation diffs over a full billing cycle; reads cut over in October with no customer-visible incident. Finance has stopped its weekly manual reconciliation. (verify: finance confirmed in Nov)

**Payout failures stopped being an on-call problem.** 2.1% failure rate in Q1, 0.4% in Q4. Configurable retries, the refund-cache fix, and the bank-side retry agreement with Risk account for the drop. Failed-payout tickets fell from about 40 a month to under 10.

**Operating level**
- Led a three-team migration end to end, including the cutover runbook SRE adopted as their template.
- Owned on-call process for the platform group from Q3; introduced the weekly SEV review, which two other groups have since copied.
- Mentored Dana through her first production launch and design review; she now owns the retry service.
