# Notation and style rules (checkable)

These rules synthesize Simon Brown's C4 review checklist (c4model.com) and the *Views and Beyond* rules for sound documentation. Each is phrased so a reviewer can tick it.

## Diagram-level
- [ ] Title states **diagram type and scope** (e.g., "System Context diagram for Internet Banking System").
- [ ] A **legend/key** explains every shape, colour, border style, line type, arrowhead and icon that carries meaning. Required whenever the diagram uses any of those conventions (proposed vs existing, async vs sync, external vs in scope, trust boundaries). Optional, and better omitted, when the diagram uses none: uniform boxes, solid arrows, default shapes, no colour. Not every reader knows UML, so a UML diagram that relies on its notation still needs a key.
- [ ] **5-second test:** a reader from the stated audience can name the diagram's subject, its new parts and the one question it answers in about five seconds. If not, cut or split.
- [ ] **One abstraction level** per diagram. Never show a microservice and a class on the same canvas.
- [ ] Stated **status**: current, proposed or future-state. Mark proposed elements visually (e.g., dashed border) and in the legend.
- [ ] The caption states the **audience and the question** the diagram answers.

## Elements (boxes)
- [ ] Every element has a **name**, a **type** (Person / Software System / Container / Component), a **one-line responsibility** and, where applicable, a **technology** (e.g., "Order Service [Container: Go, gRPC] – validates and persists orders").
- [ ] **Consistent naming**: the same element has the same name across all diagrams, the prose, and ideally the code or repo name.
- [ ] **Acronyms** are understandable by the audience or expanded in the legend.
- [ ] **Shapes carry meaning only if the legend says so.** Default: rectangles for everything, cylinders for data stores, person shapes for people.

## Relationships (lines)
- [ ] **Every arrow has a label** describing intent with a verb ("publishes OrderPlaced events to", "reads customer profile from"), not "uses". No bare arrows anywhere, including on deployment diagrams, replication links and queue edges. In a sequence diagram the message text is the label; every message line needs one.
- [ ] **The label matches the arrow direction.** Read it aloud as a sentence: source → verb → target.
- [ ] **Protocol or technology** is on inter-process arrows (HTTPS/JSON, gRPC, Kafka topic, SQL).
- [ ] **One arrow per relationship.** Don't draw a return arrow for request/response; show two only if either side can initiate.
- [ ] **Arrow semantics are declared and consistent.** Team default: arrows show the direction of the initiating interaction or data flow, not code dependency. If a diagram uses dependency semantics instead (common in component and module views), say so in the legend.
- [ ] **Async is visually distinct** (e.g., dashed line) and explained in the legend.

## Colour, density and what to leave out
- [ ] Colour is **supplementary**: the diagram must still make sense in greyscale, for accessibility and printing.
- [ ] Use **at most 3–4 colours** with fixed team meanings (e.g., grey = external/existing, blue = in scope, dashed = proposed).
- [ ] **Text density:** short descriptions on elements (≤ 10 words); detail goes in the prose or element catalog.
- [ ] **Element count:** roughly 5–15 elements per diagram. Split if larger.
- [ ] **Leave out:** logging/monitoring sidecars, every utility library, IP addresses, cross-cutting infrastructure that isn't part of the decision. Mention them in prose if relevant.
- [ ] **Vendor icons** only on deployment diagrams, and only with text labels. Icons without names are ambiguous.
- [ ] **Annotations are sparse:** at most one short tag on an element or arrow (e.g., "p99 ≤ 50 ms", "RPO 0", "PII"), explained in the text. Diagrams show *where*; prose explains *why*.

## Why these rules
Readers rarely have the author in the room. The test from c4model.com is whether the diagram "can stand alone, and be (mostly) understood without a narrative". Labels and legends are what make that true; consistent naming is what lets a reader move between the diagram, the prose and the code without re-learning the vocabulary each time.
