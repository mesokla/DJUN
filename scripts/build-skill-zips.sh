#!/usr/bin/env bash
# Пакує скіли для завантаження в claude.ai (Settings → Capabilities → Skills → Upload skill).
# Використання: bash scripts/build-skill-zips.sh [назва-скілу ...]   (за замовчуванням: scenarist scenarist-mesokla)
set -euo pipefail
cd "$(dirname "$0")/.."
bash scripts/sync-skills.sh >/dev/null
mkdir -p dist
[ $# -eq 0 ] && set -- scenarist scenarist-mesokla
for name in "$@"; do
  rm -f "dist/$name.zip"
  (cd .claude/skills && zip -qr "../../dist/$name.zip" "$name" -x '*.DS_Store')
  echo "built dist/$name.zip"
done
