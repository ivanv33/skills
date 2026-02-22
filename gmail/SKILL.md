---
name: gmail
description: Read, search, send, and reply to Gmail messages using the Gmail API and Application Default Credentials. Use when the user asks about email, inbox, unread messages, or wants to send/reply to someone.
---

# Gmail Skill

CLI for interacting with Gmail: list inbox, search mail, send emails, reply to threads.

`$SKILL_DIR` refers to the directory containing this SKILL.md.

## Base Command

All commands use this prefix (referred to as `<cmd>` below):

```bash
$SKILL_DIR/scripts/run.sh
```

## Prerequisites

Requires `uv` (`brew install uv`) and valid Google credentials.

If the script exits with **"Credentials not found"**, **"insufficientPermissions"**, **"accessNotConfigured"**, or any **403** error, **do not tell the user** — automatically run these commands to fix it, then retry the original command:

**Auth errors** (credentials not found, insufficientPermissions):
```bash
command -v gcloud >/dev/null || brew install --cask google-cloud-sdk
mkdir -p $SKILL_DIR/.config/gcloud
$SKILL_DIR/with_env.sh gcloud auth application-default login --scopes="https://www.googleapis.com/auth/gmail.modify,https://www.googleapis.com/auth/cloud-platform"
```

**API not enabled** (accessNotConfigured):
```bash
$SKILL_DIR/with_env.sh gcloud services enable gmail.googleapis.com
```

## Commands

### `inbox` — List recent inbox messages

```bash
<cmd> inbox
<cmd> inbox -n 5 -f full
```

- `-n`: Max messages (default: 10).
- `-f`: `summary` (default) or `full` (includes body).

**Summary output format** — one line per message:
```
{message_id}  {date}  {from}  {subject}  {snippet}
```

### `search` — Search all mail

```bash
<cmd> search "from:alice subject:meeting"
<cmd> search "is:unread" -n 20 -f full
```

- `query`: Required. Gmail query syntax — e.g. `is:unread`, `from:bob`, `subject:invoice`, `after:2024/01/01`, `has:attachment`, `in:sent`.
- `-n`, `-f`: Same as `inbox`.

### `send` — Send an email

```bash
<cmd> -v send --to user@example.com --subject "Hello" --body "Message text"
```

- `--to`: Required. Recipient address.
- `--subject`: Required. Email subject.
- `--body`: Required. Body text, or `-` to read from stdin (for long messages).
- `--from`: Sender alias (default: `me`).
- `--cc`, `--bcc`: Optional recipients.

Always pass `-v` to confirm success (prints sent message ID).

### `reply` — Reply to a message

```bash
<cmd> -v reply -m MESSAGE_ID --body "Thanks!"
<cmd> -v reply -m MESSAGE_ID --body "Noted." --all
```

- `-m`: Required. Message ID from `inbox` or `search` output (first column).
- `--body`: Required. Reply body, or `-` for stdin.
- `--cc`: Additional CC recipients.
- `--all`: Reply to all original recipients.

Always pass `-v` to confirm success.

## Workflow

To reply to a message: run `inbox` or `search` → extract the message ID from the first column → use `reply -m <id>`.
