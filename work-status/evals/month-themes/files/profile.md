# Aye — profile

- Role: Senior Software Engineer, Payments Platform team, Northwind Commerce (NYC, America/New_York). Level L5. Manager: Marcus Lee. Skip: Helena Ruiz (Director, Platform).
- Team: Payments Platform (6 engineers). Peers: Priya Natarajan (staff eng), Dana Okafor (eng, joined March 2026), Tom Berg (eng), Sofia Alvarez (eng). SRE partner: Jonas Weber.
- Company uses calendar quarters. Perf cycle: self-reviews due mid-December, calibration in January.

## Ongoing projects (as of Oct 2026)

- **Ledger v2 migration** — replace the legacy ledger (Rails, single Postgres) with the new event-sourced ledger service. Aye is the tech lead since February 2026 (took over from Priya). Phases: double-write (writes go to both), read cutover, legacy decommission.
- **Payout reliability** — reduce failed payouts to merchants. Aye owns this. Metric: payout failure rate (dashboard "payouts/failure_rate").
- **On-call health** — Aye became on-call process owner for the Platform group in July 2026.
- **Retry service** — small service for payout retry policy; Dana owns it since September, Aye mentors.

## 2026 goals (written in Jan with Marcus, revised in July)

- Q1: Ledger v2 design approved; double-write for charges.
- Q2: double-write for charges live; payout failure rate under 1.5%.
- Q3: all Ledger v2 writes migrated; payout failure rate under 0.5%; on-call pages down 30% for the group.
- Q4: Ledger v2 read cutover; legacy ledger decommission plan; failure rate under 0.4%.
