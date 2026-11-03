# Choosing diagrams

Use this as a decision guide. Each entry gives the situation, what the diagram shows, and a "stop here if…" rule that tells you when you have drawn enough. Source attributions: *C4* (Simon Brown, *The C4 Model*), *V&B* (*Documenting Software Architectures: Views and Beyond*), *UMLD* (*UML Distilled*), *arc42* (the arc42 template).

## System Context diagram (C4 level 1)
- **Use when:** introducing a new system, changing who or what integrates with it, or writing for mixed technical and non-technical readers.
- **Shows:** your system as one box, its users (people) and the external systems it depends on or serves.
- **Stop here if:** the doc's decision is about scope, ownership or integrations rather than internal structure.

## Container diagram (C4 level 2) — the default "if you can draw only one" diagram
- **Use when:** the design adds or changes deployable or runnable units (services, web apps, databases, queues, functions) or the technology choices between them.
- **Shows:** the containers inside your system boundary, their responsibilities, technologies, and labelled interactions (protocol, sync vs async).
- **Stop here if:** the change is between services rather than inside one. This covers most design docs.

## Component diagram (C4 level 3)
- **Use when:** the decision is about the internal decomposition of *one* container (e.g., splitting a monolith module, introducing a hexagonal boundary).
- **Shows:** major components inside one container and their dependencies.
- **Stop here if:** reviewers can evaluate the design without seeing code-level structure. Almost always stop here; skip the Code level (C4) unless a specific pattern is the point. Simon Brown notes most teams use only the top two levels and jokes C4 "could just as well be called 'C2 plus two optional levels'".

## Deployment diagram (C4 supplementary; arc42 section 7; V&B allocation view)
- **Use when:** the design changes infrastructure, regions, environments, scaling or failure domains.
- **Shows:** containers mapped onto infrastructure nodes (clusters, regions, managed services), including replication and zones.
- **Stop here if:** you've shown where things run and which failure boundaries matter. Don't reproduce Terraform.

## Sequence / dynamic diagram (C4 dynamic; UMLD ch. 4; arc42 runtime view)
- **Use when:** ordering, timing, retries, idempotency, auth hand-offs or failure handling matters. In practice, every non-trivial design.
- **Shows:** a single scenario: numbered interactions between elements already named on your structural diagram.
- **Stop here if:** you've covered the happy path plus the one failure path that keeps you up at night. Two or three scenarios maximum (arc42: "a representative selection", not every scenario).

## State machine diagram (UMLD ch. 10)
- **Use when:** an entity has a lifecycle with rules (order, subscription, job, payment) and illegal transitions are a source of bugs.
- **Shows:** states, transitions, triggering events and guards.
- **Stop here if:** every state and transition is listed; don't add implementation detail.

## Activity / flow diagram (UMLD ch. 11)
- **Use when:** explaining a business process or pipeline with branching and parallelism, especially across teams or humans.
- **Stop here if:** a numbered list would say the same thing. arc42 explicitly allows a numbered list of steps for runtime scenarios.

## Data-flow diagram
- **Use when:** the core questions are where data goes, who owns it and where it crosses a trust boundary: privacy reviews, threat models, analytics pipelines.
- **Shows:** data stores, processes, flows and trust boundaries; label flows with the data, not the verb.
- **Stop here if:** every flow of sensitive data and every trust boundary crossing is visible.

## System Landscape diagram (C4 supplementary)
- **Use when:** the doc concerns a portfolio of systems (platform strategy, org-wide migration), not one system.

## How many diagrams does a design doc need?

| Scope of the design | Diagrams |
|---|---|
| Small change (one service, no new integrations) | 0–1. A sequence diagram if behaviour changes; often none. |
| Typical feature or service design | 2–3. Context *or* Container, plus one or two sequence diagrams. |
| New system or major re-architecture | 4–6. Context, Container, Deployment, two or three dynamic diagrams, optionally one state machine. |
| More than six | You are probably writing reference documentation, not a design doc. Move it to an arc42-style architecture doc and link to it. |

## Time-boxing rules of thumb
- Whole diagramming effort for a typical design doc: about 2 hours, plus revisions after review.
- If a diagram takes more than 45 minutes, it is answering more than one question. Split it.
- If you are fighting the layout engine for more than 10 minutes, switch tools or simplify; layout perfection is not the goal.
- Draw throwaway sketches freely; only promote a sketch into the doc if it has a stated audience and question.
