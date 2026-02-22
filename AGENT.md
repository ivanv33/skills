This file provides guidance to AI coding agents when working with code in this repository.

## Conventions

- **Commits:** Use the session's anime persona for `Co-Authored-By` (e.g., `Co-Authored-By: <name> <<name>@forsahnyc.com>`). Never mention Claude or AI.

## Commit Strategy

When asked to commit changes:
- **Atomic Commits:** Break work into logical commits — not too granular. A single commit can span multiple files if they serve one purpose. Avoid commits that only touch one line or one file when they're part of a larger logical change (e.g., "Add gmail search capability", "Refactor skills to use per-skill credential isolation").
- **Stability:** Ensure the repository state is valid and runnable after *each* commit. Do not leave the repo in a broken state between commits.
- **Messages:** Use clear, descriptive commit messages.
