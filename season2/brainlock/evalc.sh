#!/bin/bash
cd "$(dirname "$0")"
for f in cand/*.red; do ../cw versus $f --hill ../lh3 --seeds 8 --salt 11 --per > ${f%.red}.s11.txt 2>&1; done
