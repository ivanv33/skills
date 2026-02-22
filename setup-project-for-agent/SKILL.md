---
name: setup-project-for-agent
description: >
  Set up a local project's directory structure for AI agent use —
  AGENTS.md, skill symlinks, and AI Agent integration. Use when
  onboarding a new project or standardizing an existing one for AI agent
  workflows.
disable-model-invocation: true
---

# Setup Project for Agent

Prepare any local project for AI agent collaboration — sets up local
directory structure and symlinks. The algorithm below describes *what* to
accomplish at each phase — adapt the exact steps to the project's language,
tooling, and structure.

## Phase 1 — AGENTS.md and CLAUDE.md

AGENTS.md is the canonical agent-instructions file. CLAUDE.md is a local
symlink so that Claude Code discovers it automatically.

1. If `AGENTS.md` does not exist at the project root, create it with a minimal
   scaffold:
   - A heading that identifies the project
   - An **Architecture** section with a brief directory map
   - A **Skills** table (header only — rows are added in Phase 3)
   - A **Conventions** section for language runtime, test commands, and
     design principles relevant to the project
2. If `CLAUDE.md` does not exist, create a **relative symlink**
   `CLAUDE.md → AGENTS.md` at the project root.
   If `CLAUDE.md` already exists as a regular file, leave it alone and note
   the conflict to the user.

## Phase 2 — Directory structure

> **Skip this entire phase if the project is itself a skills collection**
> (i.e. skill directories live at the project root rather than under
> `.agent/skills/`).

1. Ensure `.agent/skills/` exists.
2. Ensure `.claude/` exists.
3. Ensure `.claude/skills` is a **relative symlink** pointing to
   `../.agent/skills`. If it already exists and points elsewhere, warn the
   user rather than overwriting.

## Phase 3 — Global skill installation

> **Skip this entire phase if the project is itself a skills collection.**

Global skills live in `~/.agent/skills/`. Each subdirectory there that
contains a `SKILL.md` is a skill eligible for linking.

If `~/.agent/skills/` does not exist or is empty, skip this phase and inform
the user that no global skills were found.

For **each** skill directory found in `~/.agent/skills/`:

1. **Document** — Read the `name` and `description` fields from the skill's
   `SKILL.md` YAML frontmatter. Add a row to the **Skills** table in
   `AGENTS.md` with the skill name and a short description. Do NOT include
   file paths but mention it's a global skill — the agent discovers them automatically.

## Phase 4 — Verify

After all phases, confirm the setup by listing:

- Whether AGENTS.md was created or already existed
- Whether CLAUDE.md symlink was created or already existed
- Which global skills were added to the **Skills** table (if any)
- Any warnings or conflicts encountered

Present this as a brief summary to the user.

## Edge cases

- **CLAUDE.md exists as a regular file** — Do not overwrite. Warn the user
  and suggest they reconcile manually.
- **A local skill name collides with a global skill** — The local skill takes
  precedence. Do not create the symlink; note the collision.
- **Permissions errors** — Report clearly; do not retry with elevated
  privileges.
