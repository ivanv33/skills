---
tags: [architecture-diagrams]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

quick one - I'm writing an RFC for adding Stripe refunds to our checkout service. It's one existing Go service (checkout-api) plus a new background worker that picks refund jobs off our existing RabbitMQ and calls Stripe. The scary part is Stripe timing out and us double-refunding. My tech lead keeps asking for "the architecture diagrams" and I don't know how many I need or which ones. Tell me what to include and draft them for me, mermaid is fine. Save it as refunds-rfc-architecture.md
