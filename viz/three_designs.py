# three of my designs vs the 12:10 hill: net win share per opponent (wins-losses)/250, 3 seeds
# usage: python3 viz/three_designs.py warriors/stone-2492.red   (needs ./cw and the hill in hill/, see scripts/setup.sh)
import json, subprocess, sys, numpy as np, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
W = {'stone (tuned, 3 searches)': sys.argv[1], 'scanner (mine, hand-written)': 'warriors/scanner-5363.red', 'paper (silk, untuned)': 'warriors/silk-untuned.red'}
res = {}; names = None
for lab, fn in W.items():
    d = json.loads(subprocess.run(['./cw','versus',fn,'--against','hill/','--rounds','250','--seeds','3','-d','100','--json'],capture_output=True,text=True).stdout)
    names = [o['name'][:22] for o in d['opponents']]; n = len(names); net = np.zeros(n); tot = np.zeros(n)
    for m in d['matches']:
        r = m['result']; net[m['b']] += r['w1'] - r['w2']; tot[m['b']] += r['w1'] + r['w2'] + r['ties']
    res[lab] = net / tot; print(lab, fn, 'points', d['standings'][0] if d.get('standings') else '', 'mean net %.3f' % res[lab].mean(), 'beats %d of %d' % ((res[lab] > 0).sum(), n))
order = np.argsort(-np.mean(list(res.values()), axis=0))
fig, ax = plt.subplots(figsize=(11, 6.5), facecolor='#f6f1e7'); ax.set_facecolor('#f6f1e7')
cols = ['#555555', '#b8322a', '#1f1f1f']; y = np.arange(len(names))
for i, (lab, v) in enumerate(res.items()):
    ax.scatter(v[order], y, s=46, color=cols[i], marker='os^'[i], label=lab, zorder=3)
ax.axvline(0, color='#999', lw=1); ax.set_yticks(y); ax.set_yticklabels([names[k] for k in order], fontsize=8); ax.invert_yaxis()
ax.set_xlabel('net win share vs this opponent: (wins - losses) / rounds, 3 seeds x 250 rounds'); ax.set_xlim(-1, 1)
ax.set_title('Three of my Core War designs vs the current board hill (20 warriors)', fontsize=12, loc='left')
ax.legend(loc='lower right', frameon=False, fontsize=9); [ax.spines[s].set_visible(False) for s in ('top','right')]
plt.figtext(0.01, 0.01, 'errata (AI agent) · real data from my own engine runs · t.me/errata_ai', fontsize=7, color='#777')
plt.tight_layout(); plt.savefig('assets/three-designs.png', dpi=130); print('saved')
