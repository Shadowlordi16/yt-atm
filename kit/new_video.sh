#!/usr/bin/env bash
# Stage 0: create a new video folder.   usage: bash kit/new_video.sh <slug>   (run from ~/Videos/yt-atm)
set -euo pipefail
SLUG="$1"; ROOT="$(cd "$(dirname "$0")/.." && pwd)"; V="$ROOT/$SLUG"
[ -e "$V" ] && { echo "$V already exists"; exit 1; }
mkdir -p "$V/raw" "$V/sourcing"
cp "$ROOT/kit/templates/SCRIPT.md" "$ROOT/kit/templates/SOURCES.md" "$ROOT/kit/templates/photos.json" "$V/"
cd "$V" && npx hyperframes init video --non-interactive >/dev/null 2>&1
mkdir -p video/assets/vo video/assets/img video/assets/audio
cp "$ROOT/kit/assets/paper.jpg" video/assets/paper.jpg
cp "$ROOT/kit/templates/build.py" video/build.py
echo "Created $V  ->  next: research + write SCRIPT.md and SOURCES.md (AGENTS.md stage 1-2)"
