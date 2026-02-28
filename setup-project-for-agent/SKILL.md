---
name: setup-project-for-agent
description: >
  Set up a local project's directory structure for AI agent use —
  AGENTS.md, skills. Use when onboarding a new project or
  standardizing an existing one for AI agent workflows.
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
   `AGENTS.md` with the skill name, its `~/.agent/skills/<skill-name>/`
   path, and a short description.

## Phase 4 — Verify

After all phases, confirm the setup by listing:

- Whether AGENTS.md was created or already existed
- Whether CLAUDE.md symlink was created or already existed
- Which global skills were added to the **Skills** table (if any)
- Any warnings or conflicts encountered

Present this as a brief summary to the user.

## Phase 5 — Terminal Shift+Enter for new lines

Configure Shift+Enter to insert a new line in the editor's integrated terminal
instead of executing the command. Requires changes in two places: the editor
keybindings and the user's shell rc file.

### Step 1 — Detect editor flavor

Check which editor is installed by looking for the keybindings directory.
Use the **first match** found:

| Editor   | macOS path                                                        | Linux path                                  |
|----------|-------------------------------------------------------------------|---------------------------------------------|
| VSCodium | `~/Library/Application Support/VSCodium/User/keybindings.json`    | `~/.config/VSCodium/User/keybindings.json`  |
| VS Code  | `~/Library/Application Support/Code/User/keybindings.json`        | `~/.config/Code/User/keybindings.json`      |
| Cursor   | `~/Library/Application Support/Cursor/User/keybindings.json`      | `~/.config/Cursor/User/keybindings.json`    |

If none are found, skip this phase and inform the user.

### Step 2 — Editor keybindings

Ensure the detected `keybindings.json` exists and contains the following entry.
If the file does not exist, create it as a JSON array with this single entry.
If the file exists, parse the array and only append the entry when no existing
object has both `"key": "shift+enter"` and `"when": "terminalFocus"`.

The editor sends the escape sequence `ESC[13;2u` (kitty keyboard protocol
encoding for Shift+Enter). Do **not** send a raw `\n` — the PTY layer can
translate it into a carriage return before the shell sees it.

```json
{
  "key": "shift+enter",
  "command": "workbench.action.terminal.sendSequence",
  "args": { "text": "\u001b[13;2u" },
  "when": "terminalFocus"
}
```

### Step 3 — Detect shell and configure

Determine the user's shell from the `$SHELL` environment variable, then bind
the `ESC[13;2u` sequence to a widget/function that inserts a literal newline
into the edit buffer. Only append if the block is not already present in the
rc file (grep for `13;2u`).

| Shell | RC file      | Lines to add |
|-------|--------------|--------------|
| zsh   | `~/.zshrc`   | `_insert_newline() { LBUFFER+=$'\n' }` | | | | `zle -N _insert_newline` |
| | | `bindkey '\e[13;2u' _insert_newline` |
| bash  | `~/.bashrc`  | `bind '"\e[13;2u": "\C-v\C-j"'` |
| fish  | `~/.config/fish/config.fish` | `bind \e\[13\;2u 'commandline -i \n'` |

If the shell is not in the table above, skip and inform the user.

## Edge cases

- **CLAUDE.md exists as a regular file** — Do not overwrite. Warn the user
  and suggest they reconcile manually.
- **A local skill name collides with a global skill** — The local skill takes
  precedence. Do not create the symlink; note the collision.
- **Permissions errors** — Report clearly; do not retry with elevated
  privileges.
