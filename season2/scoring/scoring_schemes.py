"""Does the season-2 hill ranking depend on the points rule? Re-rank the live table (hill_now2.json) under
several win/tie/loss rules. For cayde's poll 79341 (what should the hill measure)."""
import json
d = json.load(open(__import__('sys').argv[1] if len(__import__('sys').argv) > 1 else 'hill_2026-10-06.json')); mem = [m['id'] for m in d['members']]
NM = {w['id']: w['name'] for w in d['warriors']}; NM.update({m['id']: m['name'] for m in d['members']})
nm = lambda h: NM.get(h, h)[:34]
tab = {h: [0, 0, 0] for h in mem}
for k, v in d['results'].items():
    a, b = k.split(':')
    if a in tab and b in tab:
        tab[a][0] += v['w1']; tab[a][1] += v['ties']; tab[a][2] += v['w2']
        tab[b][0] += v['w2']; tab[b][1] += v['ties']; tab[b][2] += v['w1']
S = {'3/1/0': (3, 1, 0), '3/2/0': (3, 2, 0), '2/1/0': (2, 1, 0), 'wins': (1, 0, 0), 'W-L': (1, 0, -1), 'notlost': (1, 1, 0)}
rk = {s: sorted(tab, key=lambda h: (-(a * tab[h][0] + b * tab[h][1] + c * tab[h][2]), h)) for s, (a, b, c) in S.items()}
print(f"{'warrior':34s}     W     T     L " + ' '.join(f'{s:>7s}' for s in S))
for h in rk['3/1/0']:
    x, y, z = tab[h]
    print(f"{nm(h):34s} {x:5d} {y:5d} {z:5d} " + ' '.join(f'{rk[s].index(h) + 1:7d}' for s in S))
n = sum(tab[h][0] + tab[h][1] + tab[h][2] for h in tab) // 2
print(f"{len(mem)} members, {n} rounds; ties {sum(tab[h][1] for h in tab) / 2 / n:.0%} of rounds; columns = rank under each rule (win/tie/loss points)")
