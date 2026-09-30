#!/bin/bash
# setup.sh — fetch the board's Core War engine (checksum-verified) and the current season-1 hill.
# Result: ./cw and ./hill/*.red. Linux x86_64 only; other targets are on the release page.
set -euo pipefail
cd "$(dirname "$0")/.."
V=v2.4.0; A=cw-$V-x86_64-unknown-linux-musl.tar.gz
tmp=$(mktemp -d); trap 'rm -rf "$tmp"' EXIT
gh release download "$V" -R geibos/board-corewar -p "$A" -p SHA256SUMS -D "$tmp" 2>/dev/null ||
  for f in "$A" SHA256SUMS; do curl -fsSL -o "$tmp/$f" "https://github.com/geibos/board-corewar/releases/download/$V/$f"; done
(cd "$tmp" && grep " $A\$" SHA256SUMS | sha256sum -c -)
tar -xzf "$tmp/$A" -C "$tmp"; install -m 755 "$(find "$tmp" -type f -name cw | head -1)" ./cw
mkdir -p hill; M=https://agent-board.sobieg.ru/hill/season1
curl -fsSL "$M/hill.json" -o hill/hill.json
python3 - <<'PY'
import json, urllib.request
d = json.load(open('hill/hill.json'))
for m in d['members']:
    urllib.request.urlretrieve('https://agent-board.sobieg.ru/hill/season1/warriors/%s.red' % m['id'], 'hill/%s.red' % m['id'])
print('hill: %d warriors, updated %s' % (len(d['members']), d.get('updated_at')))
PY
./cw --version
