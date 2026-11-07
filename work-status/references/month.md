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

**September 2026 update**

**Highlights**
- Ledger v2 migration: payouts now double-write to both ledgers with zero reconciliation diffs across a full billing cycle, which clears the last blocker for the read cutover.
  - Double-write for payouts landed on the 24th; refunds followed on the 29th.
  - Cutover runbook reviewed by Priya and the SRE on-call.
- Payout reliability: cut failed-payout tickets from 31 in August to 9 in September by shipping configurable retries and fixing the stale refund-status cache. (verify the August count)
- Team: ran the on-call retro and introduced a weekly 30-minute SEV review; the two September SEV-3s both had fixes merged within a day.

**Against goals**
- Q3 goal "Ledger v2 writes migrated": done.
- Q3 goal "payout failure rate under 0.5%": on track, 0.6% as of the 30th.
- Q3 goal "on-call load down 30%": at risk; pages are down but the alert cleanup slipped to October.

**Decisions and changes of direction**
- Kept double-writing two extra weeks before flipping reads, to get a full billing cycle of diffs.
- Dropped the custom retry scheduler in favour of config-driven backoff; the scheduler would have taken another month for no measurable gain.

**Risks and next month**
- Read cutover depends on Risk signing off on retry limits for high-risk merchants; waiting since the 22nd.
- October: flip Ledger v2 reads, finish alert cleanup, write the Q4 plan for deprecating the old ledger.
