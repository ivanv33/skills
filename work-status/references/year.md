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

**2026 in review — Senior Engineer, Search Platform**

**The year in three sentences**
I took search from a system with a 4% zero-result rate and hourly index updates to one with a 1.8% zero-result rate and five-minute freshness in every region, and built the evaluation pipeline that every ranking change now has to pass. Together those are credited with about 0.5% of search-led orders and ended stale-price complaints as a support category. By Q3 I owned relevance quality for the whole marketplace, up from owning the query-rewriting service in January.

**Storylines**

**Search stopped returning nothing.** In January 4.1% of searches returned no results. I designed synonym expansion, shipped it region by region with a brand-name allowlist after merchant escalations, and handed the dictionary to the Catalogue team. Zero-result rate was 2.2% by March and 1.8% by October; Growth attributes about 0.3% of search-led orders to it. (verify: Growth's Q3 attribution memo)

**Ranking changes got a gate.** There was no offline evaluation; every change went straight to A/B. I built the eval pipeline and the first labelled sets, then moved labelling to a vendor when the Catalogue team could not staff it. Every ranking experiment since May has run through it; four were stopped before A/B on its score, saving roughly a month of test traffic each.

**Operating level**
- Owned relevance quality for the marketplace from Q3, a cross-team remit covering Search, Catalogue and Growth.
- Set the standard that ranking changes need an offline score before A/B; the Ads team adopted the same pipeline in Q4.
- Mentored Omar from his first launch to owning the indexing service.
