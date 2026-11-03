# Sources and further reading

## Core principles behind the standard
1. Diagrams exist to communicate, not to decorate (V&B rule 1: write from the reader's point of view).
2. One diagram answers one question (C4; arc42 runtime view).
3. Abstractions first, notation second; C4 is deliberately notation- and tooling-independent.
4. Every diagram has a title, a legend and a stated audience.
5. Views over the one-diagram-to-rule-them-all: module, component-and-connector and allocation views serve different stakeholders (V&B; SAiP).
6. Sketch vs blueprint: know which you're making. Sketch is the most common and most useful for communication (UMLD).
7. Optimize for being read, not for being drawn: avoid ambiguity, use a standard organization, don't repeat information (V&B rules 2–4).
8. Rationale is part of the architecture (V&B rule 5; Google design-doc guidance).
9. Quality attributes drive structure (SAiP).
10. Keep diagrams close to the code, current but not too current; update at milestones, delete what no one maintains (V&B rule 6).
11. Review documentation for fitness of purpose (V&B rule 7).
12. Most teams need only the top two C4 levels (Simon Brown).

## Books

**Simon Brown, *The C4 Model: Visualizing Software Architecture* (O'Reilly, 1st ed., June 2026)**
- Successor to his retired Leanpub book. Twelve chapters, roughly one per diagram type, plus notation, going beyond the basics, and putting C4 into practice.
- Read: System Context and Container chapters, the notation chapter, Dynamic and Deployment chapters.
- Online: c4model.com ("Diagrams → Notation", "Review checklist", "Microservices → Queues and topics"); structurizr.com/docs.

**Clements et al., *Documenting Software Architectures: Views and Beyond* (Addison-Wesley/SEI, 2nd ed., 2010)**
- Read: the Prologue ("Seven Rules for Sound Documentation"); Part I on module, component-and-connector and allocation styles; chapters on documenting interfaces and behaviour; "Choosing the Views" and "Building the Documentation Package" (view packets, templates).
- Online: SEI Views and Beyond resources at sei.cmu.edu.

**Martin Fowler, *UML Distilled* (Addison-Wesley, 3rd ed., 2003)**
- Read: ch. 1 (sketch vs blueprint vs programming language), ch. 4 (Sequence Diagrams), ch. 8 (Deployment), ch. 10 (State Machine), ch. 11 (Activity). Skip the rest unless needed.
- Online: martinfowler.com/bliki/UmlAsSketch.html.

**Bass, Clements, Kazman, *Software Architecture in Practice* (Addison-Wesley, 4th ed., 2021)**
- Read: ch. 3 (Understanding Quality Attributes: the six-part scenario), the quality-attribute chapters you care about for their tactics catalogues, ch. 22 (Documenting an Architecture).

**Gharbi, Koschel, Rausch, Tiemeyer, *Software Architecture Fundamentals* (Rheinwerk, 2nd ed., 2024; iSAQB CPSA-F study guide)**
- Read: the chapter on describing and communicating software architectures.
- Pair with arc42: docs.arc42.org sections 3 (Context and Scope), 5 (Building Block View: "Level-1 is your friend"), 6 (Runtime View), 7 (Deployment View), 9 (Architecture Decisions).

**Joseph Ingeno, *Software Architect's Handbook* (Packt, 1st ed., 2018)**
- Read: ch. 4 (Quality Attributes), ch. 8 (microservices, serverless, cloud-native), ch. 12 (Documenting and Reviewing Software Architectures: views, UML, ATAM and ARID).

## Practitioner links
- Malte Ubl, "Design Docs at Google" (industrialempathy.com): context and scope, system-context diagram, alternatives considered.
- c4model.com review checklist.
- Martin Fowler, "UmlAsSketch".
- Simon Brown on dev.to, "Software architecture diagrams – which tool should we use?": multi-renderer approach via Structurizr DSL.
- Gregor Hohpe, *The Software Architect Elevator* / architectelevator.com: the lines (relationships) are where the architecture is. Not verified in the original research pass.

## Caveats
- **Reddit coverage gap.** Practitioner sentiment comes from Hacker News, issue trackers and blogs; Reddit threads could not be retrieved. Validate with a manual pass before formal adoption.
- **Chapter numbers** are given from known tables of contents; the O'Reilly C4 book is cited at chapter-topic level. Verify against your copies.
- **Edition check.** Only the 2018 first edition of Ingeno's handbook was confirmed as current.
- **Vendor bias.** Structurizr is created by C4's author; tool-comparison articles from diagram vendors were discounted.
