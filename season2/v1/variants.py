# variants of the search1 winner: add Постовой's cells (P7, P9) to the trap mix; scored like search1 but on salt 303 x 8
import json, subprocess, sys
sys.argv = [sys.argv[0]]
from search_v1 import render
base = {'d1': 6368, 'd2': 4980, 'j': -3135, 'kinds': ['L113', 'L115', 'K101'], 'n': 12, 'place': 'both', 'imp': False}
V = {'base': base,
     'five15': dict(base, kinds=['L113', 'L115', 'K101', 'P7', 'P9'], n=15),
     'five10': dict(base, kinds=['L113', 'L115', 'K101', 'P7', 'P9'], n=10),
     'four12P9': dict(base, kinds=['L113', 'L115', 'K101', 'P9'], n=12)}
for k, g in V.items():
    if k == 'base': continue
    f = f'variants/{k}.red'; open(f, 'w').write(render(g, f'Errata Trapdoor {k}'))
    r = subprocess.run(['./cw', 'versus', f, '--hill', 'lh', '--seeds', '8', '--salt', '303', '--jobs', '1', '--per'], capture_output=True, text=True)
    print(k, g, '\n', r.stdout, flush=True)
