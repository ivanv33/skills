---
name: architecture-diagrams
description: Team standard for architecture diagrams in design docs — choose the few diagrams a design needs (C4 Context/Container, sequence, deployment, state), draw them as Mermaid or Structurizr source with titles, legends and labelled arrows, write the prose that carries rationale and quality attributes, and review existing diagrams against a checklist. Use whenever the user is writing or reviewing a design doc, RFC, ADR or architecture section, asks for a system/service/component/sequence/deployment diagram, asks "which diagrams should I include", or pastes a diagram and asks whether it is any good — even if they don't say "architecture" or "C4".
license: MIT
---

# Architecture Diagrams in Design Docs

Draw a **small set of diagrams, each built to answer one question for a named audience**. For most design docs that means one C4 Context or Container diagram plus one sequence diagram for the riskiest flow. Every diagram gets a title, a legend, labelled arrows and a paragraph of prose. Source lives next to the code and is either updated or deleted. This is the shared core of the C4 model, arc42, *Documenting Software Architectures: Views and Beyond*, *UML Distilled* and *Software Architecture in Practice*, with one practitioner correction baked in: **a diagram nobody maintains is worse than no diagram.**

## When this skill applies

- Writing the architecture section of a design doc, RFC or ADR.
- Someone asks for "a diagram of the system", "a sequence diagram for X", "a deployment diagram".
- Reviewing a design doc or a pasted diagram for quality.
- Deciding which diagrams (and how many) a design needs.

Scale the output to the request. A bare "add a diagram to this doc" wants one or two diagrams, each with a title, legend and a short walkthrough paragraph, and nothing else bolted on; the quality-attribute scenarios, decision records and maintenance line in steps 6 and 8 belong in a full Architecture section, not in every answer. If the user only wants a quick throwaway sketch to think with, draw it and skip the ceremony, but say which rules you skipped. The full rigour below is for an Architecture section that will be read by others and kept.

## The eight rules that matter most

1. **One diagram, one question, one audience.** If you can't write the question in the caption, don't draw the diagram.
2. **Start at the top.** Context first, then containers; go deeper only where the design decision actually lives. Most teams never need C4 level 3 or 4.
3. **Title and labelled arrows, always; a legend whenever the picture uses a convention.** Every arrow carries a verb. A legend is required the moment a diagram uses colour, dashed lines, dashed borders, icons or non-default shapes to mean something; a plain sequence diagram or a flowchart with uniform boxes and solid arrows can skip it, and should, because an empty legend is noise. Readers shouldn't need the author in the room either way.
4. **Never mix abstraction levels** on one canvas: services and classes, or servers and teams, don't share a diagram.
5. **Show structure *and* behaviour.** One box diagram plus one sequence diagram for the critical path beats five box diagrams.
6. **Prose carries the reasoning.** Rationale, rejected alternatives and quality-attribute trade-offs go in the text beside the diagram, not in the picture.
7. **Pass the 5-second test.** A reader from the stated audience should get the diagram's main point in about five seconds: what the subject is, what is new, and the one question it answers. That caps a diagram at roughly 5–15 elements and forces the most important path to be visually dominant. Sketch, don't blueprint: design-doc diagrams communicate selected aspects; they are not complete specifications.
8. **Diagrams live with the code and die when they lie.** Commit the source, review it in PRs, name an owner, delete what no longer matches reality.

## Workflow

Time-box the whole diagramming effort for a typical design doc at about two hours.

### 1. Name the audience and the question first

Write the caption before anything else: *"For [audience], this diagram shows [question]."* Example: "For the payments on-call team: how does a refund flow through the system when the provider times out?" If the user hasn't told you the audience, infer it from the doc and state your assumption.

### 2. Choose the diagrams

Pick from the decision guide in `references/choosing-diagrams.md` (read it when the choice isn't obvious). The short version:

| Question the doc must answer | Diagram | Stop when… |
|---|---|---|
| Who/what does this system talk to? Scope, ownership, integrations | **C4 System Context** | the decision is about scope, not internals |
| What runs where, with which tech, talking how? | **C4 Container** (the default if you draw only one) | the change is between services, not inside one |
| How is *one* container decomposed? | C4 Component | reviewers can judge the design without code structure |
| What happens, in what order, and what if it fails? | **Sequence / dynamic** | you have the happy path plus the one failure path that keeps you up at night |
| Where does it run; what are the failure domains? | Deployment | you've shown zones, replicas, failure boundaries (don't reproduce Terraform) |
| What states can this entity be in? | State machine | every state and legal transition is listed |
| Where does data go and where does it cross a trust boundary? | Data-flow | every sensitive flow and boundary crossing is visible |

How many: a small change needs 0–1 diagrams; a typical feature or service design 2–3; a new system or re-architecture 4–6. More than six means you're writing reference documentation, not a design doc; move it to an arc42-style architecture doc and link.

### 3. List the model before drawing

Write the elements as text first: name, type (Person / Software System / Container / Component), one-line responsibility, technology. Then the relationships as `A → verb → B [protocol]`. The picture is generated from this model, which is why names stay consistent across every diagram and the prose.

### 4. Draw it as source

Default to **Mermaid** inline in the Markdown doc for sequence, flow, state and single C4 diagrams; it renders natively in GitHub/GitLab and is diffable in PRs. Use **Structurizr DSL** when several diagrams describe the same system, so one model generates consistent views. `assets/mermaid-examples.md` has starter snippets for each diagram type that already satisfy the notation rules; `references/tooling.md` covers the full tool choice and how to keep diagrams in the repo.

Never deliver a diagram as a screenshot or a description of a picture with no editable source.

### 5. Apply the notation rules

Full checklist in `references/notation-rules.md`. The ones that are most often broken:

- Title states **type and scope** ("Container diagram: Checkout system (proposed)").
- A **legend** explains every shape, colour, line style and arrowhead the diagram uses to carry meaning. Skip it only when there is nothing to explain: no colour, no dashed lines or borders, no icons, default shapes. Never skip it on a diagram that distinguishes proposed from existing or async from sync.
- Every element has **name, type, responsibility, technology** ("Order Service [Container: Go, gRPC] – validates and persists orders").
- Every arrow has a **verb label** that reads as a sentence in the arrow's direction, plus a **protocol** on inter-process calls. "Uses" is not a label. Queue, topic and replication arrows are inter-process too: "publishes RefundRequested to [AMQP]", "replicates to [Redis async replication]", not just a verb.
- **Arrows show the initiating interaction or data flow**, not code dependency, unless the legend says otherwise. One arrow per request/response.
- **Async is visually distinct** (dashed) and named in the legend.
- **Proposed vs existing is distinguishable** (dashed border or colour, in the legend).
- Colour is supplementary; at most 3–4 colours; must still read in greyscale.
- Leave out logging sidecars, utility libraries, IPs, and cross-cutting infrastructure that isn't part of the decision.

### 6. Write the prose beside each diagram

When writing a full Architecture section, each diagram gets a 2–5 sentence walkthrough, the quality attributes it addresses, the key decision and the alternatives rejected. When the user asked only for a diagram, the walkthrough alone is enough. Write quality attributes as scenarios, not adjectives: *"When [stimulus] under [environment], [artifact] shall [response] within [measure]."* Name the tactic used (retry with idempotency key, active redundancy, caching). `references/quality-attributes-and-rationale.md` has the scenario format, the decision-record format and where each attribute belongs on which diagram.

Use `assets/architecture-section-template.md` as the skeleton for the whole Architecture section: it has slots for context, structure, runtime scenarios, deployment, quality attributes, decisions and diagram maintenance. Fill it rather than inventing a layout.

### 7. Review before handing over

Apply the 5-second test first: cover the prose, look at the diagram, and ask whether someone from the stated audience would name its subject, its new parts and its question in five seconds. If not, cut elements or split it before checking anything else. Then run the checklist in `references/review-checklist.md` on your own output, or on the user's diagrams when reviewing. Reject the anti-patterns it lists: no legend, mixed levels, "uses" arrows, the everything-diagram, a diagram with no prose, private notation, screenshot-only, stale-but-current, structure without behaviour, hand-drawn code-level diagrams.

When reviewing someone else's diagram, lead with the one or two problems that most hurt a reader, quote the checklist item, and show the fixed source rather than describing the fix.

### 8. Plan for maintenance

Add a maintenance line under the section: owner, last-verified date, source path, and whether the diagrams get promoted to `docs/architecture/` after launch or the doc gets marked historical. Design docs are snapshots; stale diagrams presented as current are the number-one practitioner complaint.

## Distributed and microservice systems

These produce the worst "everything" diagrams. Key moves: state whose boundary perspective you're drawing from (one team's services as containers vs other teams' services as external systems), draw each service with its own datastore so shared databases are visibly shared, model queues and topics as elements with dashed async arrows, show relationships on the container diagram and *flows* on sequence diagrams, and draw one container diagram per bounded context rather than one of sixty services. Details in `references/distributed-systems.md`.

## Reference files

- `references/choosing-diagrams.md` — the full decision guide per diagram type, with "use when" and "stop here if" rules, and diagram counts.
- `references/notation-rules.md` — checkable notation and style rules (diagram, element, relationship, colour and density).
- `references/quality-attributes-and-rationale.md` — quality-attribute scenarios, tactics, decision/alternatives format.
- `references/distributed-systems.md` — patterns for microservice, async and cloud-native diagrams.
- `references/tooling.md` — Mermaid vs Structurizr vs PlantUML vs draw.io, repo layout, rot prevention, and what practitioners actually report.
- `references/review-checklist.md` — the two-minute review checklist and the anti-pattern list.
- `references/sources.md` — the books and links behind this standard, what to read in each, and known caveats.
- `assets/architecture-section-template.md` — the Architecture section skeleton to paste into a design doc.
- `assets/mermaid-examples.md` — Mermaid snippets for Context, Container, sequence, state and deployment diagrams that already follow the rules.
