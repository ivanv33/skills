# Diagrams-as-code and tooling

## Team recommendation
- **Mermaid: the default for inline sequence, flow and state diagrams.** It renders natively in GitHub and GitLab Markdown and in many wikis, so diagrams stay in the doc, are diffable and reviewable in PRs. Its C4 support (`C4Context`, `C4Container`) is limited; don't rely on it for multi-diagram C4 models.
- **Structurizr DSL: the default for C4 structural diagrams of any system with more than one diagram.** You define one model and generate many views (context, container, component, deployment, dynamic), so names and relationships stay consistent. It can export to PlantUML, Mermaid and other formats. Caveat: Simon Brown, who created C4, founded Structurizr, so his recommendation of it is not neutral.
- **C4-PlantUML: acceptable alternative** for teams already invested in PlantUML; also the strongest option for full UML (state machines, detailed sequences). Downside: each diagram is hand-maintained, so names drift across files.
- **D2: optional** for teams who want better auto-layout and aesthetics in text-based diagrams; less ecosystem integration than Mermaid.
- **Excalidraw: for whiteboarding and early exploration.** Use it in design sessions; redraw in code once the design stabilizes, or commit the `.excalidraw` source if the sketch itself goes in the doc.
- **draw.io / diagrams.net and Lucidchart: when non-engineers must edit,** or for one-off presentation diagrams. If used, commit the editable source (`.drawio`, or `.drawio.svg` / `.drawio.png` with embedded XML) next to the rendered image. Never paste a screenshot with no source.

## Keeping diagrams in the repo
1. Store diagram source under `docs/architecture/` (or next to the service code it describes), alongside the design doc or ADRs.
2. Render in CI (Structurizr CLI, mermaid-cli, PlantUML, D2), or rely on native Markdown rendering for Mermaid.
3. Diagram changes go through **PR review like code**. Add diagram files to CODEOWNERS for the owning team.
4. Link, don't copy: design docs in Google Docs or Confluence should link to or embed the rendered diagrams from the repo rather than holding the only copy.

## Preventing rot
- **Each diagram has an owner and a "last verified" date** in the doc.
- **Design docs are snapshots.** After launch, mark them historical. Only diagrams promoted to `docs/architecture/` are considered current.
- **Quarterly "update or delete" sweep:** stale, unowned diagrams get deleted. An honest absence beats a confident lie.
- **Consider generating from reality** where possible (deployment views from infrastructure-as-code, dependency views from service catalogues) for the parts that change most often.

## What practitioners actually say (and where they disagree with the books)

*Sourcing note:* this sentiment comes from Hacker News threads, public issue trackers and practitioner blogs; Reddit threads could not be retrieved when this standard was researched. Treat the conclusions as directional.

- **Rot is the #1 pain point.** On Hacker News's "Design docs at Google (2020)" thread (May 2024), one former Googler wrote: "After working there for 6 years, I haven't seen a single up to date design doc. At best a high level diagram." Others called docs "outdated as soon as implementation start[s]."
- **Unread C4 diagrams get deleted.** In the Drupal Canvas project, Wim Leers introduced versioned C4 diagrams and about 18 months later filed an issue titled "Accept the reality nobody looks at the C4 model diagrams: remove them." No one else had used or updated them, and the CI job rendering them had been broken for weeks. Lesson: diagrams-as-code doesn't create readers. Tie diagrams to decisions people are actually making.
- **Diagrams-as-code is favoured for longevity but costs discipline.** "Without wiring diagrams into the dev workflow, they go stale and start misleading people," while drag-and-drop tools "give you richer visual polish… but they drift out of sync with the code they describe" (Collin Wilkins, "Architecture as Code: Diagrams-as-Code Adoption Guide").
- **UML fatigue is real, but sequence diagrams survive.** Practitioners widely report abandoning full UML for boxes-and-lines or C4, while sequence diagrams remain popular. A common practitioner "top 5" is C4 Context, C4 Container, Deployment, Sequence and Use Case. This agrees with Fowler's "UML as sketch" and diverges from *Views and Beyond*'s more formal ideal.
- **Dissent from the books:** practitioners push back on comprehensive documentation (*Views and Beyond*, full arc42) as too heavy for most teams, and some see C4 levels 3–4 as rarely worth the effort. This standard sides with practitioners on volume (2–3 diagrams per doc) and with the books on rigour (legends, labels, rationale).
