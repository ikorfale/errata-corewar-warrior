#!/usr/bin/env python3
"""search_v1.py — random search + hill-climb over a trap paper for season 2 of the board's Core War hill.
Genome: silk distances d1, d2, jump j; trap kinds, count and place (before/after the paper); imp spiral on/off.
Fitness: mean points per placement vs the replica hill lh/ (cw versus --hill), 4 placements, salt 0.
Every evaluation is appended to search1/evals.jsonl (resumable); at the end the top 6 are re-scored on salt 101 x 8."""
import json, os, random, subprocess, sys, time, hashlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CW = './cw'; OUT = 'search1'; LOG = f'{OUT}/evals.jsonl'
BUDGET = float(sys.argv[1]) if len(sys.argv) > 1 else 6300  # seconds
TRAPS = {'P7': 'STP.AB  #1, #7', 'P9': 'STP.AB  #1000, #9', 'L113': 'STP.AB  #1, #113',
         'L115': 'STP.AB  #9, #115', 'K101': 'STP.AB  #1, #101'}
I3 = '((3-CORESIZE%3)*CORESIZE+1)/3'

def render(g, name='v1'):
    tr = [TRAPS[k] for k in g['kinds']] or [TRAPS['P7']]
    pad = ''.join(f'        {tr[i % len(tr)]}\n' for i in range(g['n']))
    pre = pad if g['place'] in ('before', 'both') else ''
    post = pad if g['place'] in ('after', 'both') else ''
    imp = g['imp']
    s = [';redcode-94', f';name {name}', ';author fable-terminal', f'I3      EQU     {I3}', pre.rstrip('\n')]
    if imp:
        s += ['start   SPL     paper', '        SPL     1', '        SPL     1', '        SPL     1', '        SPL     2',
              '        JMP     @0, imp', '        ADD     #I3, -1']
    s += ['paper   SPL     1'] * 1 + ['        SPL     1'] * (3 if imp else 4)
    s += [f'silk    SPL     @0, {g["d1"]}', '        MOV.I   }-1, >-1', f'        SPL     @0, {g["d2"]}',
          '        MOV.I   }-1, >-1', '        MOV.I   pbomb, >-2', '        MOV.I   {-3, <1', f'        JMP     @0, {g["j"]}',
          'pbomb   DAT.F   <I3, <2*I3']
    if imp: s += ['imp     MOV.I   #0, I3']
    s += [post.rstrip('\n'), f'        END     {"start" if imp else "paper"}']
    return '\n'.join(x for x in s if x != '') + '\n'

def score(g, seeds=4, salt=0):
    src = render(g); h = hashlib.sha1(src.encode()).hexdigest()[:10]
    f = f'{OUT}/w_{h}.red'; open(f, 'w').write(src)
    r = subprocess.run([CW, 'versus', f, '--hill', 'lh', '--seeds', str(seeds), '--salt', str(salt), '--jobs', '1', '--json'],
                       capture_output=True, text=True, timeout=900)
    d = json.loads(r.stdout); s = d['standings'][0]
    os.remove(f)
    return s['score'], h

def rand_g():
    return {'d1': random.randrange(200, 7992), 'd2': random.randrange(200, 7992), 'j': random.randrange(-7900, -200),
            'kinds': random.sample(list(TRAPS), random.randint(1, 3)), 'n': random.choice([0, 2, 4, 6, 8, 10, 12, 16]),
            'place': random.choice(['before', 'after', 'both']), 'imp': random.random() < 0.5}

def mutate(g):
    g = json.loads(json.dumps(g)); k = random.choice(['d1', 'd2', 'j', 'd', 'kinds', 'n', 'place', 'imp'])
    if k in ('d1', 'd2'): g[k] = max(130, min(8060, g[k] + random.randint(-300, 300)))
    elif k == 'j': g[k] = max(-8060, min(-130, g[k] + random.randint(-300, 300)))
    elif k == 'd': g['d1'], g['d2'] = g['d2'], g['d1']
    elif k == 'kinds': g['kinds'] = random.sample(list(TRAPS), random.randint(1, 3))
    elif k == 'n': g['n'] = max(0, min(24, g['n'] + random.choice([-4, -2, 2, 4])))
    elif k == 'place': g['place'] = random.choice(['before', 'after', 'both'])
    else: g['imp'] = not g['imp']
    return g

def main():
    random.seed(int(time.time()))
    done = [json.loads(l) for l in open(LOG)] if os.path.exists(LOG) else []
    t0 = time.time()
    base = {'d1': 2422, 'd2': 3317, 'j': -1586, 'kinds': ['P7', 'P9'], 'n': 8, 'place': 'before', 'imp': False}  # = v0/silktrap
    pool = [(e['score'], e['g']) for e in done] or []
    if not pool:
        sc, h = score(base); pool.append((sc, base)); open(LOG, 'a').write(json.dumps({'g': base, 'score': sc, 'h': h, 'src': 'base'}) + '\n')
    i = 0
    while time.time() - t0 < BUDGET:
        pool.sort(key=lambda x: -x[0])
        g = rand_g() if random.random() < 0.25 else mutate(random.choice(pool[:5])[1])
        try: sc, h = score(g)
        except Exception as e: print('fail', e, flush=True); continue
        pool.append((sc, g)); i += 1
        open(LOG, 'a').write(json.dumps({'g': g, 'score': sc, 'h': h, 't': round(time.time() - t0)}) + '\n')
        print(i, round(sc, 1), 'best', round(max(p[0] for p in pool), 1), flush=True)
    pool.sort(key=lambda x: -x[0]); seen = set(); val = []
    for sc, g in pool:
        k = json.dumps(g, sort_keys=True)
        if k in seen: continue
        seen.add(k); v, h = score(g, seeds=8, salt=101); val.append({'g': g, 'score4': sc, 'val8': v, 'h': h})
        print('VAL', round(sc, 1), round(v, 1), g, flush=True)
        if len(val) >= 6: break
    json.dump(val, open(f'{OUT}/validation.json', 'w'), indent=1)
    best = max(val, key=lambda x: x['val8']); open(f'{OUT}/best.red', 'w').write(render(best['g'], 'Errata Trapdoor'))
    print('BEST', best)

if __name__ == '__main__': main()
