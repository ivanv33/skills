# Aye — quarterly updates sent to Marcus, 2026

## Q1 2026 (sent Apr 1)

- Ledger v2: took over as tech lead from Priya in Feb. Design doc approved Mar 12 after two reviews (Finance Eng and SRE). Split the migration into double-write → read cutover → decommission.
- Charges double-write: built the event mapper and reconciliation job; flagged on for 5% of charges Mar 30. 0 diffs in the first 2 days.
- Payout reliability: failure rate 2.1% in Jan; investigated and found 60% of failures are retryable bank timeouts. No fix shipped yet.
- Onboarded Dana (joined Mar 2); pairing twice a week.
- Miss: double-write slipped two weeks because the event mapper needed a rewrite for multi-currency.

## Q2 2026 (sent Jul 1)

- Charges double-write at 100% since May 11; 0 diffs over a full billing cycle. Finance Eng signed off on the diff report format.
- Payout reliability: shipped the bank-timeout retry (single retry after 30s) in April; failure rate 2.1% → 1.4% by June. Goal was <1.5%: met.
- Wrote the "flag-flip runbook" after a near miss in May; Platform group adopted it.
- Reviewed Tom's idempotency-key redesign; caught the retry-storm case before launch.
- Dana shipped her first feature (payout status webhook) in June; I reviewed and ran the rollout with her.
- Miss: did not start the refunds double-write in Q2 as planned; charges took longer than estimated.

## Q3 2026 (sent Oct 1)

- Ledger v2: refunds (July) and payouts (Sept) double-write at 100%, 0 reconciliation diffs over a full billing cycle for refunds and 22 days for payouts. Read-cutover runbook written and reviewed; SRE adopting it as their template. Cutover Oct 14. Finance estimates the cutover removes ~6h/week of manual reconciliation.
- Payout reliability: failure rate 1.4% → 0.6%. Configurable retry backoff (Dana built, I designed and reviewed) and the refund-status cache fix. Failed-payout tickets 44 (Jul) → 9 (Sept). Remaining EU failures are bank-side; Risk sign-off on retry limits pending.
- On-call: became Platform group on-call process owner in July. Introduced the weekly SEV review (Helena and two other groups now attend). Pages 61 → 47 (-23%); goal was -30%, missed because alert cleanup slipped behind the migration.
- Led the SEV-2 in July (duplicate refund entries, ledger only, no customer impact); added a CI deploy-ordering check so it can't recur.
- Dana now owns the retry service.

## October 2026 notes (not yet sent)

- Oct 14: Ledger v2 read cutover for refunds and payouts done. No incidents. Finance stopped the weekly manual reconciliation on Oct 21 (Nadia confirmed in #finance-eng).
- Oct 6–9: alert cleanup done; Oct pages 38 (vs 61 in July, -38%).
- Oct 20: Risk (Omar) signed off on retry limits; high-risk merchants on retries from Oct 22. Oct failure rate 0.4%.
- Oct 27: Helena asked me to write the legacy-ledger decommission plan for the whole Platform org (3 teams), due end of Nov.
- Oct 28: Sofia's team copied the weekly SEV review for Identity group.
