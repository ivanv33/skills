---
name: work-status
description: Write Aye's work status update at any cadence — weekly status, monthly report, quarterly review, or year-end self-review / brag doc — from memory, past conversations and connected apps (GitHub, Slack, Jira, calendar, git). The longer the window, the higher the altitude and the stronger the self-advocacy; quarter and year updates are written as performance-review evidence. Use whenever Aye asks for a status update, work summary, "what did I do this week/month/quarter/year", perf or self-review material, promo packet input, or a brag doc, and when run on a Friday, month-end, quarter-end or year-end schedule.
---

# Work status

Usage: `work-status [week|month|quarter|year] [DATE]`

- Cadence defaults to `week`. `weekly-status` is an alias for `work-status week`.
- `DATE` is any date inside the period you want (`YYYY-MM-DD`). If omitted, use the period containing today.

You are usually running as a scheduled task (Friday afternoon, last business day of the month, quarter end, year end) or were invoked by hand. Nobody is watching, so never ask a question — make a reasonable call and note it in the update with "(verify)". Your job: write Aye's status update for the period and deliver it as a message.

## Why cadence changes the job

The same raw activity has to be told four different ways, because each cadence has a different reader and a different purpose:

| Cadence | Reader | Purpose | Altitude | Words |
|---|---|---|---|---|
| week | manager, team channel | keep people informed, surface blockers | ground level: what happened | ~250 |
| month | manager, skip-level | show progress against goals | themes and outcomes, not events | ~350 |
| quarter | manager writing a perf review, calibration | prove impact | goals vs results, quantified | ~500 |
| year | self-review, promo packet | make the case for Aye's level and trajectory | narrative arc, scope, growth | ~800 |

As the window grows, two dials turn up together:

1. **Altitude.** A week lists events. A month groups events into a few themes. A quarter measures those themes against what Aye set out to do. A year tells the story of what Aye became responsible for and what changed because of it. Small things that were worth a weekly bullet (a bug fix, a review, a meeting) disappear at month level unless they add up to something; at quarter and year level only outcomes survive.
2. **Self-advocacy.** A weekly update is modest and factual. A quarterly or yearly update is Aye's evidence in a performance process where nobody else will make the case: claim credit for what Aye led, state the business outcome, put a number on it, and say what would not have happened otherwise. Advocacy never means inventing: every claim must trace back to something gathered, and anything inferred is marked "(verify)". See `references/impact.md` for how to turn activity into honest impact statements.

Read the reference for the chosen cadence before writing; it holds the structure, the word budget, and worked examples:

- `references/week.md`
- `references/month.md`
- `references/quarter.md`
- `references/year.md`

## Step 1 — Establish the window

Get the current date and time from a tool or the system; never guess it. Then run:

```bash
python3 $SKILL_DIR/scripts/window.py <cadence> [DATE]
```

(`$SKILL_DIR` is the directory holding this SKILL.md.) It prints the start, the end, and the title to use. Weeks run Monday 00:00 to Sunday 23:59; months, quarters and years are calendar periods. If the period contains today, the window ends right now. Timezone is America/New_York unless memory says otherwise. If Aye's company uses a fiscal calendar and memory records it, pass `--fiscal-start-month`.

## Step 2 — Gather what Aye did

Use every source below that is available in this session; silently skip any that isn't. Do not stall on a missing or unauthenticated connection — move on and name the gap in the sources line at the end.

**Memory first.** Read whatever persistent memory or notes you have about Aye (for example `/profile.md`, `/topics/recent-work.md`, everything under `/areas/`, or the equivalent profile, notes and project files in your environment). You need Aye's role and level, the names and current status of ongoing projects, the goals Aye set for the period if any were written down, and the company's fiscal calendar if it has one. Use memory to name things correctly, to spot status changes, and at quarter and year level to know what Aye was *supposed* to achieve. Memory is not the record of the period's work.

**Compound from shorter reports.** Longer cadences are built from shorter ones whenever those exist: a month from that month's weekly updates, a quarter from its monthly updates, a year from its quarterly updates. Look for earlier updates in memory, notes, sent Slack messages, sent email, or docs before mining raw activity. They already carry Aye's own framing and save a great deal of reading. Fill gaps with raw activity; never rely on earlier updates alone, because they miss what happened after they were sent.

**Past conversations.** If you can list past conversations or sessions, list those updated inside the window. For a week, read about 20 per page and paginate back up to about 5 pages. For a month, go up to about 15 pages. For a quarter or year, do not try to read everything: search for the project names and goals from memory and for follow-ups on the main topics, and lean on the compounded reports and connected apps instead. Use the snippet or summary; open a full conversation only when the snippet does not make clear what was accomplished or decided. Attribute carefully: only what Aye actually did, said or decided counts. Your own suggestions and drafts are not accomplishments or decisions unless Aye explicitly adopted them.

**Connected apps.** Check your available tools and integrations (connectors, MCP servers, CLIs) for GitHub, Slack, Google Calendar, Gmail, Google Drive, docs, Jira or Linear. For any that is connected and usable, pull the window's activity: PRs opened, reviewed and merged, commits, design docs written or reviewed, meetings attended and run, Slack threads Aye posted in, tickets moved and closed. If you are in a workspace with git, run `git log --author=<Aye> --since=<start> --until=<end>`. At quarter and year level, prefer each app's own aggregates (PR counts, closed tickets per epic, releases, docs by title) over scrolling through individual items.

**Collect evidence for impact, not just activity.** From week level up, note any number attached to the work as you go: latency, error rate, cost, revenue, adoption, time saved, tickets closed, people unblocked, incidents avoided. At quarter and year level these numbers are the update; without them you will be writing a long list of activities, which is what the reader is trying to avoid.

## Step 3 — Write the update

Follow the structure in the cadence reference. Rules that apply at every cadence:

- First person ("I"), plain and direct, ready to paste as-is into Slack, email, or a review form. Short bullets or short prose. No tables.
- Project or theme name first in each bullet; outcome before activity ("Shipped X, cutting Y by Z" rather than "Worked on X").
- No preamble, no meta-commentary about how the update was gathered, no mention of chats or tools inside the update itself.
- If a fact is uncertain (an ambiguous snippet, a number you inferred), append "(verify)" to that bullet rather than dropping it or stating it flatly.
- Work only. Leave out anything personal: health, home or real estate, car, travel, family, fitness, side projects that are clearly personal.
- If the period looks light or a source had nothing, say so in one line rather than padding with filler. A short honest update beats a long inflated one at every cadence, including the yearly one.
- Respect the word budget for the cadence. The budget is what makes the reader actually read it.

## Step 4 — Deliver

Send the finished update as a message to Aye through whatever user-facing channel the harness provides (a send-message or notify tool, a configured Slack or email channel); if there is none, output it as your final response. After the update, add a divider line ("---") and one short line naming what it drew on, e.g. "Sources: 12 chats this week, GitHub, Slack" or "Sources: 3 monthly updates, GitHub, Jira; Slack was not connected in this run" — so Aye knows what is and isn't covered.
