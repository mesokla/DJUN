#!/usr/bin/env bash
# Копіює спільне ядро (content-core/) у кожен скіл-сценарист.
# Правиш методику тільки в content-core/, потім запускаєш: bash scripts/sync-skills.sh
set -euo pipefail
cd "$(dirname "$0")/.."
for skill in .claude/skills/scenarist-*/; do
  dest="${skill}references/core"
  rm -rf "$dest"; mkdir -p "$dest"
  cp content-core/references/*.md "$dest/"
  cp content-core/engine.md "$dest/engine.md"
  echo "synced → $dest"
done
