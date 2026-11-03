# Expressing quality attributes and rationale

## Write quality attributes as scenarios, not adjectives
"Highly available" is not reviewable. *Software Architecture in Practice* (SAiP) defines a six-part quality-attribute scenario: **source, stimulus, environment, artifact, response, response measure**. A lightweight form for design docs:

> *When [stimulus] occurs under [environment], [artifact] shall [response] within [measure].*

Example: "When one availability zone fails during peak traffic, Checkout API continues serving requests with p99 < 400 ms and no lost orders."

## Map each scenario to where the architecture handles it
In the narrative under each diagram, add a short block:

- **Latency:** which hops are on the critical path; caches; sync vs async boundaries. A sequence diagram is the natural place to annotate a latency budget per hop.
- **Availability:** redundancy, failover and degradation modes. Show replicas and zones on the deployment diagram; show the failure path as its own dynamic diagram.
- **Security:** trust boundaries (draw as a dashed boundary box), authn/authz points, encryption in transit and at rest. A data-flow diagram is best for sensitive data.
- **Scalability / modifiability:** which containers scale independently; which boundaries isolate change.

## Name the tactics
SAiP catalogues design *tactics* per quality attribute: redundancy, heartbeat and retry for availability; caching and concurrency for performance; authenticate/authorize actors for security; encapsulation and intermediaries for modifiability. Naming the tactic ("we use the *retry with idempotency key* tactic here") makes the design reviewable and searchable.

## Annotate diagrams sparingly
Put at most one short tag on an element or arrow (e.g., "p99 ≤ 50 ms", "RPO 0", "PII") and explain it in the text. Diagrams show *where*; prose explains *why*.

## Record rationale and alternatives
From *Views and Beyond* rule 5 and Google's design-doc guidance, which frames the whole doc as the place to write down "the trade-offs you made in designing your software". For each significant decision:

- **Decision:** one sentence.
- **Drivers:** which quality-attribute scenarios or constraints forced it.
- **Alternatives considered:** 1–3, each with why it was rejected.
- **Consequences:** what gets harder, and known risks.

Durable decisions go into an ADR in the repo, linked from the design doc.

## The view packet
In *Views and Beyond* terms, each diagram plus its prose is a *view packet*: the primary presentation (the picture), the element catalog (what each element is and does), context (how this view relates to others), and rationale. A diagram without the other three parts is an incomplete packet, which is why a picture with no walkthrough is an anti-pattern.
