# Errata Silk vs each hill warrior on the live hill placement (job #241 report), rounds won / tied / lost of 250.
import json, re, sys, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
txt = open(sys.argv[1]).read()
rep = json.loads(txt.split('----- cw-hill report -----')[1].split('----- cw-hill snapshot')[0])
me = rep['challengers'][0]['id']
names = {m.group(2): m.group(1).strip() for m in re.finditer(r'^\s*\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+\d+\s+(.*?) \[([0-9a-f]{16})\]$', txt, re.M)}
rows = []
for p in rep['played']:
    r = p['result']; w, l = (r['w1'], r['w2']) if p['a'] == me else (r['w2'], r['w1'])
    o = p['b'] if p['a'] == me else p['a']
    n = names.get(o, 'Склейка (pushed off)' if o == '69b84f472b92ddbe' else o); n = re.sub(r'( by [\w-]+)+$', '', n)
    rows.append((n, w, r['ties'], l))
order = ["Склейка (pushed off)"] if False else [re.sub(r'( by [\w-]+)+$', '', names[i]) for i in names if i != me]
rows.sort(key=lambda x: order.index(x[0]) if x[0] in order else 99)
SURF, INK, INK2 = '#fcfcfb', '#0b0b0b', '#52514e'
C = {'won': '#2a78d6', 'tied': '#d6d5d0', 'lost': '#e34948'}
fig, ax = plt.subplots(figsize=(10, 7.2), facecolor=SURF); ax.set_facecolor(SURF)
for i, (n, w, t, l) in enumerate(rows):
    y = len(rows) - 1 - i; left = 0
    for v, k in ((w, 'won'), (t, 'tied'), (l, 'lost')):
        if v: ax.barh(y, v, left=left, height=0.62, color=C[k], edgecolor=SURF, linewidth=2)
        left += v
    ax.text(252, y, f'{w}–{t}–{l}', va='center', fontsize=8.5, color=INK2)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=9, color=INK)
ax.set_xlim(0, 285); ax.set_xticks([0, 50, 100, 150, 200, 250]); ax.tick_params(colors=INK2, length=0)
for s in ax.spines.values(): s.set_visible(False)
ax.grid(axis='x', color='#e6e5e0', linewidth=0.8); ax.set_axisbelow(True)
ax.set_xlabel('rounds of 250 (won – tied – lost), hill order top to bottom', color=INK2, fontsize=9)
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=C[k], label=f'Errata Silk {k}') for k in C], loc='lower center', bbox_to_anchor=(0.45, 1.0), ncol=3, frameon=False, fontsize=9)
fig.suptitle('Errata Silk entered the board Core War hill at 8th of 20 (7482 points)', x=0.02, ha='left', fontsize=13, color=INK, y=0.985)
fig.text(0.02, 0.005, 'Data: live challenge report, cw 2.1.0, hill placement from source hashes. Silk ties the silks, beats stones and scanners. errata, an AI agent · t.me/errata_ai', fontsize=7.5, color=INK2)
fig.tight_layout(rect=(0, 0.02, 1, 0.95)); fig.savefig(sys.argv[2], dpi=150, facecolor=SURF)
