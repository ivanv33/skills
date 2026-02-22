#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source .env from cwd (project root) — portable, no path assumptions
if [[ -f .env ]]; then
    set -a
    source .env
    set +a
fi

export CLOUDSDK_CONFIG="$SKILL_DIR/.config/gcloud"
exec "$@"
