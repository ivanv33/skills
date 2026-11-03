---
tags: [architecture-diagrams]
max_turns: 30
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

For the design doc on adding rate limiting to our public API gateway (it's a single Envoy-based gateway service, we're adding a Redis-backed token bucket filter in front of the existing routes, nothing else changes) I need the full set: a system context diagram, container diagram, component diagram, class diagram of the filter, a deployment diagram and an ER diagram. Mermaid please. Put them all in rate-limiting-diagrams.md
