---
name: gdrive
description: Export Google Docs as Markdown directly from the Drive API using Application Default Credentials
---

# GDrive Export Skill

CLI for exporting Google Docs to Markdown (or other formats) via the Drive API.

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
$SKILL_DIR/with_env.sh gcloud auth application-default login --scopes="https://www.googleapis.com/auth/drive.readonly,https://www.googleapis.com/auth/cloud-platform"
```

**API not enabled** (accessNotConfigured):
```bash
$SKILL_DIR/with_env.sh gcloud services enable drive.googleapis.com
```

## Commands

### `query` - Search for Google Docs

Use this to find the document ID of a file by its name.

```bash
<cmd> query "My Project Notes"
<cmd> query "My Project Notes" --meta
```

- `name`: Required. Part or all of the file name to search for.
- `--meta`: Optional. Include metadata (created/modified time, owner, shared with, link) in results.

### `get` - Export a Google Doc

Accepts a raw document ID or a full Google Docs URL. When the URL contains a `?tab=t.{TAB_ID}` parameter, that specific tab is exported.

```bash
<cmd> get 1ABCdefGhI_JkLmNoPqRsTuVwXyZ > mynotes.md
<cmd> get 1ABCdefGhI_JkLmNoPqRsTuVwXyZ -o notes.md
<cmd> get "https://docs.google.com/document/d/1ABCdefGhI_JkLmNoPqRsTuVwXyZ/edit"
<cmd> get "https://docs.google.com/document/d/1ABCdefGhI_JkLmNoPqRsTuVwXyZ/edit?tab=t.abc123"
```

If you specify an output file (`-o`), you will get progress logs. If you do not specify one, the tool will output purely the document contents to `stdout`.

Tab-specific exports use an authenticated web endpoint. If the requested format is not supported for tab export (e.g., markdown), it falls back to plain text with a warning.

- `doc_id`: Required. Document ID or full Google Docs URL (tab param supported).
- `-o`, `--output`: Optional. Output filename (default: stdout).
- `-f`, `--format`: Optional. Export format — guessed from `-o` extension if not provided. Defaults to `md`. Supported: `md`, `txt`, `pdf`, `rtf`, `docx`, `html`, `epub`.
