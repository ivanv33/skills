# Review checklist and anti-patterns

## Two-minute review checklist (author self-check or reviewer)
- [ ] Caption states the **audience and the question** this diagram answers.
- [ ] **Title** includes diagram type and scope; status (current/proposed) is clear.
- [ ] **5-second test**: subject, new parts and the one question are visible at a glance.
- [ ] **Legend** present whenever the diagram uses colour, line styles, borders, icons or non-default shapes to mean something, and it explains every one of them; absent only when there is nothing to explain.
- [ ] **One abstraction level**; elements all at the same C4 level.
- [ ] Every element has **name, type, responsibility** and **technology** where applicable.
- [ ] Every arrow has a **verb label** matching its direction, with no bare arrows, plus **protocol** for inter-process calls including queues and replication.
- [ ] **Async vs sync** is distinguishable.
- [ ] Names are **consistent** with other diagrams, the prose and the code.
- [ ] **≤ ~15 elements**, readable at normal zoom, understandable in greyscale.
- [ ] Accompanying **prose**: walkthrough, quality attributes addressed, decision and alternatives.
- [ ] At least one **behavioural** diagram exists if ordering or failure handling matters.
- [ ] **Source is committed** (or linked) and editable by someone other than the author; owner named.

## Top anti-patterns to reject in review
1. **Unexplained conventions.** Colours, dashed lines or borders that mean something, with no legend to say what. (A plain diagram with no conventions doesn't need one.)
2. **Mixed abstraction levels.** Services, classes, servers and teams on one canvas.
3. **Unlabelled or "uses" arrows.** Relationships with no intent, direction or protocol.
4. **The "everything" diagram.** Fifty boxes trying to answer every question at once; split it by question.
5. **Diagram with no prose.** A picture with no walkthrough, no rationale and no quality attributes.
6. **Private notation.** Shapes and icons only the author can decode, or vendor icons without labels.
7. **Author-only maintainability.** A screenshot or proprietary file with no shared editable source.
8. **Stale-but-current.** A diagram presented as current that no longer matches production.
9. **Structure without behaviour.** Box diagrams for a design whose risk is in sequencing, retries or failure modes.
10. **Proposed vs existing ambiguity.** New components indistinguishable from what already exists.
11. **Code-level diagrams drawn by hand.** These rot fastest; generate them from code or skip them.

## How to give review feedback
Ask one person from the stated audience to explain the diagram back to you without help; where they stumble is where the diagram fails (V&B rule 7: review documentation for fitness of purpose). Lead with the one or two findings that most hurt that reader, name the checklist item or anti-pattern, and show the corrected source rather than describing the fix in words.
