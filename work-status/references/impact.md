# Writing impact statements

Status updates at month level and above are judged on impact, and the people reading them are comparing Aye against others whose updates are written to persuade. This guide is how to persuade without inflating.

## The pattern

Every impact bullet answers four things, usually in this order:

1. **What I did** — the action, with Aye as the subject. "I led", "I shipped", "I redesigned", "I negotiated".
2. **What changed** — the outcome in the world, not the artefact. Not "merged the retry PR" but "payouts now retry automatically".
3. **By how much** — the number: before and after, a percentage, a count, a time, money. One number per bullet is usually enough; two is the maximum.
4. **Why it mattered** — the business or team consequence, in a few words: cost, revenue, risk, customer experience, someone's time, a dependency unblocked.

Example: "I shipped configurable payout retries, cutting failed payouts from 1.4% to 0.6% in a quarter and removing the single largest source of finance support tickets."

If you have the first two but not the number, write the bullet anyway and mark the gap: "cut failed payouts noticeably (verify: get the before/after rate)". A visible gap is useful to Aye; a vague bullet is not.

## Activity to outcome

Translate as you write. A short ladder:

- "Worked on X" → "Shipped X" → "Shipped X, which now does Y" → "Shipped X, which now does Y, cutting Z by N%".
- "Attended the design review" → nothing, unless Aye changed the design: "Caught the double-charge edge case in the refunds design review; the fix went in before launch."
- "Reviewed 23 PRs" → "Reviewed every migration PR (23), which is why the cutover shipped with no post-launch fixes."
- "Helped Dana" → "Mentored Dana through her first production launch; she now owns the retry service."

## Credit, precisely

- Use "I led" only for things Aye drove end to end or was the accountable owner of. Use "I built", "I designed", "I shipped" for things Aye did. Use "with <name or team>" for shared work and name who owned the rest.
- Precise credit is more persuasive than broad credit. "I led the migration across three teams; SRE owned the rollout" is believable. "I delivered the migration" with no mention of the three other people reads as a claim the reader will check.
- Never promote your own suggestions into Aye's decisions. If Aye adopted a suggestion you made, Aye decided; if not, it did not happen.

## Numbers you can use

Look for these while gathering, and record where each came from:

- Rates and latencies before and after (error rate, p95, failure rate, conversion).
- Counts over time (tickets, incidents, pages, support requests, PRs by others on Aye's tooling).
- Money and time (cost saved, revenue protected, hours a week removed from someone's job).
- Adoption (teams using a tool, services on a standard, docs linked from other teams).
- Scale (users, requests, transactions touched by the change).

A number must come from something you gathered: a PR description, a dashboard someone quoted in a chat, a ticket, an earlier update. Rounding is fine; estimating is fine if marked "(verify)"; inventing is not.

## Level language

Performance and promotion rubrics tend to grade these, so make them visible when the evidence supports them:

- **Scope:** one service → a system → a cross-team programme → an organisational standard.
- **Direction:** Aye decided what should be built, not just how.
- **Multiplier:** others became faster or better because of Aye (mentoring, tooling, docs, standards, reviews that changed designs).
- **Judgment:** calls that avoided cost or risk, including the call to stop or cut scope.
- **Ownership under pressure:** incidents led, launches run, deadlines held or renegotiated early.

Use the plain version of the term ("I set the direction for", "SRE adopted it as their template") rather than the rubric word ("demonstrated multiplier impact"). The reader maps it to the rubric themselves and trusts the plain version more.

## Misses

State them. One line for the miss, one for the reason, one for what Aye did about it. A review with no misses in it is read as unreliable, and a miss that the manager already knows about and that is missing from the document costs more than the miss itself.
