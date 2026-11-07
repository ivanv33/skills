# Monthly update

**Reader:** Aye's manager, often forwarded to a skip-level or dropped into a team monthly report.
**Purpose:** show progress against what the team is trying to achieve this quarter. The reader wants to know whether things are on track and what changed, not what happened each day.
**Altitude:** themes, not events. Group the month's work into 2 to 4 themes (usually the projects or goals Aye owns) and describe each theme by its outcome. A weekly bullet like "fixed the stale refund cache" only survives if it is part of a theme ("on-call: cut refund-status incidents from 4 to 0 by fixing cache invalidation").
**Tone:** confident and specific. This is where numbers start to matter: where a weekly update could say "shipped X", a monthly update says what X changed. Claim what Aye led; say "with <person/team>" for what was shared.
**Budget:** under about 350 words.

## How to build it

1. Read the month's weekly updates if they exist. Every bullet in them is a candidate; most will merge or drop.
2. Cluster the candidates by project or goal. If memory lists quarterly goals, use those as the clusters.
3. For each cluster write one outcome sentence first, then at most two supporting bullets. If you cannot write an outcome sentence, the cluster is activity without a result yet: say so plainly ("in progress, read cutover planned for October").
4. Pull forward anything that changed direction during the month; a manager would rather hear it here than in the quarterly review.

## Structure

Bold title line: **<Month YYYY> update**. Then, each with a short bold header:

1. **Highlights** — 2 to 4 themes. One outcome sentence per theme with a number where there is one, followed by at most two supporting bullets.
2. **Against goals** — one line per quarterly goal Aye owns or contributes to: on track / at risk / done, and the one-phrase reason. If no goals are written down anywhere, say "No written goals for the quarter; themes above are my own grouping."
3. **Decisions and changes of direction** — one line each with the reason. If none, say so.
4. **Risks and next month** — what is at risk, who or what it depends on, and the two or three things Aye will push next month.

## What to leave out

- Individual PRs, tickets, meetings and reviews. Count them if the count is the point ("reviewed 23 PRs for the migration") and otherwise drop them.
- Weeks. The reader does not care which week something landed.
- Personal items of any kind.

## Example

**March 2026 update**

**Highlights**
- Zero-result searches: down from 4.1% to 2.2% across all regions after synonym expansion reached 100%, which the growth team estimates is worth about 0.3% of search-led orders. (verify estimate)
  - Brand-name expansion excluded after merchant escalations; allowlist in place.
  - Catalogue team now owns the synonym dictionary; I handed over the tooling on the 20th.
- Index freshness: product changes appear in search within 5 minutes in EU and US, down from an hourly batch; merchant complaints about stale prices fell from 19 in February to 3.
- Relevance evals: a labelled furniture set (1,200 query/product pairs) is live in the eval pipeline, so ranking experiments in that category now have an offline score before an A/B test.

**Against goals**
- Q1 goal "zero-result rate under 2.5%": done.
- Q1 goal "index freshness under 10 minutes in all regions": on track, APAC still on the hourly batch pending Infra capacity.
- Q1 goal "offline relevance evals for the top 3 categories": at risk; furniture done, apparel and electronics slipped to April.

**Decisions and changes of direction**
- Excluded brand names from synonym expansion; precision mattered more than the small recall gain.
- Moved the eval sets after furniture to a shared labelling vendor instead of the catalogue team, who cannot staff it in April.

**Risks and next month**
- APAC freshness depends on Infra's Elasticsearch capacity request, open since the 12th.
- April: APAC incremental indexer, apparel eval set, start the ranking experiment on furniture.
