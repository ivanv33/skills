# Activity export — Jul 1 to Sep 30, 2026

Combined dump: chat summaries (C), GitHub (G), Slack (S), calendar (M), Jira (J). Author is Aye unless stated.

## July

- 2026-07-01 (C) Chat "Q3 planning": Aye revised Q3 goals with Marcus: all Ledger v2 writes migrated, payout failure rate <0.5%, on-call pages down 30% for the Platform group. Aye noted failure rate currently 1.4%.
- 2026-07-02 (G) PR #4120 merged: "ledger-v2: double-write for refunds (behind flag)". 
- 2026-07-03 (C) Chat "car inspection": Aye asked which garages in Brooklyn do same-day inspections.
- 2026-07-07 (M) Took over Platform group on-call process ownership from Priya. Calendar: "On-call handover".
- 2026-07-08 (S) #payments-platform: Aye posted the Ledger v2 write-migration plan: refunds July, payouts September, cutover October.
- 2026-07-09 (J) PAY-881 "Failed payouts spike for EU merchants" — Aye investigated: bank-side timeouts, not our bug. Comment: "We retry once after 30s; bank needs ~90s. Proposing configurable backoff."
- 2026-07-10 (C) Chat "retry backoff design": Aye drafted a one-page design for configurable retry backoff. Decided against building a scheduler: "config-driven backoff, done in 2 weeks vs 6 for a scheduler, same measured gain."
- 2026-07-14 (G) PR #4151 merged: "refunds double-write: reconciliation job + diff report".
- 2026-07-15 (M) Incident SEV-2: duplicate refund ledger entries for 0.3% of refunds for 40 minutes. Aye was IC. Root cause: flag flipped before reconciliation job deployed. Fixed by replaying; no customer impact (ledger only).
- 2026-07-16 (C) Chat "SEV-2 postmortem": Aye wrote the postmortem. Action items: deploy ordering check in CI (Aye), runbook for flag flips (Aye).
- 2026-07-17 (C) Chat "marathon plan": Aye asked for a 16-week marathon training plan.
- 2026-07-20 (J) PAY-890 "Configurable retry backoff" created, assigned Dana. Aye: "Dana will build; I'll review and pair on the rollout plan."
- 2026-07-22 (G) PR #4177 merged: "ci: enforce migration/flag deploy ordering". 
- 2026-07-24 (S) #platform-oncall: Aye proposed a weekly 30-min SEV review for the Platform group. 6 thumbs up, Helena: "yes please".
- 2026-07-28 (M) First weekly SEV review held.
- 2026-07-29 (C) Chat "August status": Aye said July failure rate ended at 1.3%; refunds double-write at 100% with 0 diffs for 10 days.
- 2026-07-30 (C) Chat "apartment lease renewal": personal, negotiating rent.

## August

- 2026-08-03 (G) PR #4210 merged (author Dana, reviewed by Aye, 4 rounds): "retry-service: configurable backoff policy".
- 2026-08-04 (M) Design review: payouts double-write. Aye presented. Jonas (SRE) raised the partial-write-on-crash case; Aye agreed to add an outbox. 
- 2026-08-05 (C) Chat "outbox pattern": Aye decided to use a transactional outbox for payouts double-write rather than dual commits. Reason: crash safety, SRE requirement.
- 2026-08-10 (S) #payments-platform: Aye: "Retry backoff live for 10% of merchants. EU failure rate on that cohort 0.9% vs 1.4%."
- 2026-08-11 (J) PAY-903 "Stale refund status cache" — Aye picked up after 3 support tickets. 
- 2026-08-12 (C) Chat "dentist": personal.
- 2026-08-14 (G) PR #4241 merged: "refund-status: invalidate cache on ledger event". Linked PAY-903.
- 2026-08-17 (M) Aye out: vacation Aug 17–21.
- 2026-08-24 (S) #platform-oncall: Aye: "July→Aug pages for Platform group: 61 → 49. Alert cleanup (noisy disk alerts) still to do."
- 2026-08-25 (G) PR #4260 merged: "ledger-v2: payouts double-write with transactional outbox (flagged)".
- 2026-08-26 (C) Chat "retry rollout": Aye and Dana planned the 100% rollout; Aye asked Dana to write the rollout doc and present it. Dana presented Aug 28.
- 2026-08-27 (J) Failed-payout support tickets in August: 31 (Aye's note in PAY-881: "31 in Aug, 44 in July").
- 2026-08-28 (S) #payments-platform: Retry backoff at 100%. Aye: "Expect Sept failure rate ~0.7%."
- 2026-08-31 (C) Chat "Sept status": Aye noted Aug failure rate 1.0%; payouts double-write ready to flag on after one more load test.

## September

- 2026-09-01 (M) Load test with SRE (Jonas). Outbox handled 3x peak. Aye flipped payouts double-write to 10%.
- 2026-09-03 (C) Chat "finance reconciliation": Nadia (Finance Eng) told Aye finance spends ~6h/week manually reconciling payouts against legacy ledger; Ledger v2 reads would remove it. Aye: "good number for the cutover case."
- 2026-09-08 (G) PR #4302 merged: "payouts double-write: 100%". 
- 2026-09-09 (S) #payments-platform: Aye: "Payouts double-write at 100%, 0 diffs so far."
- 2026-09-10 (J) PAY-915 "Risk sign-off on retry limits for high-risk merchants" — Aye opened, assigned to Risk team (Omar). 
- 2026-09-14 (C) Chat "Q4 plan draft": Aye drafted the Q4 plan: read cutover Oct 14, decommission plan by Nov, alert cleanup first week of Oct.
- 2026-09-15 (M) Mid-quarter check-in with Marcus. Marcus: "on-call target at risk, migration is the priority, fine."
- 2026-09-16 (C) Chat "flight to Lisbon": personal travel in November.
- 2026-09-21 (C) Chat "cutover runbook": Aye wrote the Ledger v2 read-cutover runbook, asked Priya to review.
- 2026-09-22 (S) #risk-payments: Aye pinged Omar on PAY-915; no reply yet.
- 2026-09-22 (M) On-call: SEV-3, refund status page showed stale state for ~2h. Cause: cache invalidation missed the "reversed" event. Aye fixed same day.
- 2026-09-23 (G) PR #4330 merged: "refund-status: invalidate on reversed event + regression test". 
- 2026-09-23 (C) Chat "retry config PR": Aye reviewed and merged Dana's PR #4328 "retry-service: policy config via admin UI" (ops can change backoff without deploy).
- 2026-09-24 (C) Chat "double-write cycle": Aye decided to keep double-writing two more weeks before flipping reads, to get a full billing cycle of diffs. "Cutover moves Oct 7 → Oct 14."
- 2026-09-24 (M) Out Thu–Fri: team offsite (no work items).
- 2026-09-25 (C) Chat "running shoes": personal.
- 2026-09-28 (M) Priya reviewed the cutover runbook; two comments addressed. Jonas: "SRE will use this as the template for our own migrations."
- 2026-09-29 (G) PR #4341 merged: "ledger-v2: refunds+payouts reconciliation report, daily".
- 2026-09-29 (S) #platform-oncall: Aye: "Sept pages: 47 (vs 61 in July, -23%). Alert cleanup slipped to Oct."
- 2026-09-30 (C) Chat "Sept numbers": Aye: Sept failure rate 0.6%; Sept failed-payout tickets 9; 0 reconciliation diffs across full billing cycle for refunds, 22 days for payouts; EU remaining failures are bank-side, tracked with Risk.
- 2026-09-30 (C) Chat "team dinner": Aye asked where to book a dinner for 8 near the office. (unclear if work)
