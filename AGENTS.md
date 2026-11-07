This file provides guidance to AI coding agents when working with code in this repository.

## Architecture

```
architecture-diagrams/     → Architecture diagrams for design docs skill
gdrive/                    → Google Drive export skill
gmail/                     → Gmail interaction skill
karpathy-guidelines/       → LLM coding guidelines skill
setup-project-for-agent/   → Project onboarding skill
work-status/               → Weekly/monthly/quarterly/yearly work status and perf-review skill
work-status/               → Weekly/monthly/quarterly/yearly work status and perf-review skill
```

## Skills

| Skill | Description |
|-------|-------------|
| `architecture-diagrams` | Team standard for architecture diagrams in design docs: choose the few diagrams a design needs (C4 Context/Container, sequence, deployment, state), draw them as Mermaid or Structurizr source with titles, legends and labelled arrows, write the prose that carries rationale and quality attributes, and review existing diagrams against a checklist |
| `gdrive` | Export Google Docs as Markdown directly from the Drive API using Application Default Credentials |
| `gmail` | Read, search, send, and reply to Gmail messages using the Gmail API and Application Default Credentials. Use when the user asks about email, inbox, unread messages, or wants to send/reply to someone |
| `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria |
| `setup-project-for-agent` | Set up a local project's directory structure for AI agent use — AGENTS.md, skill symlinks, and Claude Code integration. Use when onboarding a new project or standardizing an existing one for AI agent workflows |
| `work-status` | Write a work status update at week, month, quarter or year cadence from memory, past conversations and connected apps; the longer the window, the higher the altitude and the stronger the self-advocacy, with quarter and year updates written as performance-review and promo evidence |
| `work-status` | Write a work status update at week, month, quarter or year cadence from memory, past conversations and connected apps; the longer the window, the higher the altitude and the stronger the self-advocacy, with quarter and year updates written as performance-review and promo evidence |

## Skill Design

Skills are symlinked into consuming projects, so each skill must be **independent, self-contained, and portable**. A skill directory should work correctly regardless of where it is linked from — no references to sibling skills or paths outside its own directory. The one shared location is `~/.agent/`, which is accessible to all agents and skills, but must not be abused; use it only for cross-cutting concerns like credentials or shared config, not as a dumping ground.

## Conventions

- **Commits:** Never mention `Co-Authored-By`.
- **Atomic Commits:** Break work into logical commits — not too granular. A single commit can span multiple files if they serve one purpose.
- **Stability:** Ensure the repository state is valid and runnable after each commit. Do not leave the repo in a broken state between commits.
- **Messages:** Use clear, descriptive commit messages.
