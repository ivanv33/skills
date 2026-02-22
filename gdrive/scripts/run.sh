#!/usr/bin/env bash
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
exec "$SKILL_DIR/with_env.sh" uv run "$SKILL_DIR/scripts/gdrive.py" "$@"
