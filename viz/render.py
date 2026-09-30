"""Render a real Core War round from `cw trace` as frames: each core cell coloured by its last writer."""
import json, subprocess, sys, os
import numpy as np, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
A, B, rnd, every, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
cw = os.path.expanduser('~/work/lab/cwbin/cw')
d = json.loads(subprocess.run([cw, 'trace', A, B, '--rounds', str(rnd), '--record', str(rnd), '--every', str(every)],
                              capture_output=True, text=True, check=True).stdout)
rec = d['recorded'][0]; info = d['rounds'][rnd - 1]; names = [w['name'] for w in d['warriors']]
W, H = 100, 80; core = np.full(8000, -1)
for w, start, ln in rec['start']: core[start:start + ln] = w
cols = np.array([[0xf4, 0xef, 0xe4], [0xb3, 0x26, 0x1e], [0x22, 0x22, 0x22]]) / 255
os.makedirs(out, exist_ok=True)
json.dump({'names': names, 'round': info, 'score': d['score'], 'frames': len(rec['frames'])}, open(f'{out}/meta.json', 'w'), ensure_ascii=False)
for i, f in enumerate(rec['frames']):
    for c, w in f['writes']: core[c] = w
    img = cols[core + 1].reshape(H, W, 3)
    fig = plt.figure(figsize=(8, 7.2), dpi=120, facecolor='#f4efe4'); ax = fig.add_axes([0.03, 0.08, 0.94, 0.82])
    ax.imshow(img, interpolation='nearest'); ax.set_axis_off()
    p = f.get('processes', [0, 0])
    fig.text(0.03, 0.94, f'{names[0]}', color='#b3261e', fontsize=15, family='serif', weight='bold')
    fig.text(0.97, 0.94, f'{names[1]}', color='#222222', fontsize=15, family='serif', weight='bold', ha='right')
    fig.text(0.03, 0.03, f'cycle {f["cycle"]:>6}   processes {p[0]} : {p[1]}', fontsize=11, family='monospace', color='#222')
    fig.text(0.97, 0.03, 'real match, cw trace · errata', fontsize=10, family='serif', style='italic', color='#666', ha='right')
    fig.savefig(f'{out}/f{i:04d}.png', facecolor=fig.get_facecolor()); plt.close(fig)
print(json.dumps({'round': info, 'score': d['score'], 'frames': len(rec['frames'])}))
