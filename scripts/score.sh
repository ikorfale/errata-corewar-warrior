#!/bin/bash
# score.sh [seeds] — score every warrior in warriors/ against hill/ (average per seed, as the hill prints it).
set -euo pipefail
cd "$(dirname "$0")/.."
for w in warriors/*.red; do printf '%-28s ' "$(basename "$w")"; ./cw versus "$w" --against hill/ --seeds "${1:-3}" -d 100 2>/dev/null | grep -m1 -E '^\s*1\s' || echo '?'; done
