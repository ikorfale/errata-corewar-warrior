import json, random, sys, time
from gen import render, TD
from k1 import run
OPP=['kscan.red','kboot.red','pscan.red','lscan.red']
def ev(g, seeds=2, salt=3):
    open(f'ss_{salt}.red','w').write(render(TD,TD,d1=g[0],d2=g[1],j=g[2],name='ss'))
    d=run(f'ss_{salt}.red',OPP,seeds=seeds,salt=salt); return d['standings'][0]['score']
random.seed(int(sys.argv[2]) if len(sys.argv)>2 else 1); out=open('ssearch.jsonl','a'); t0=time.time()
pool=[(ev(g),g) for g in [(6368,4980,-3135),(7000,1870,-3135)]]
for sc,g in pool: out.write(json.dumps({'g':g,'sc':sc,'ref':1})+'\n')
while time.time()-t0<float(sys.argv[1]):
    if random.random()<0.3: g=(random.randrange(200,8000),random.randrange(200,8000),-random.randrange(200,8000))
    else:
        g=list(sorted(pool,reverse=True)[random.randrange(min(4,len(pool)))][1]); i=random.randrange(3)
        g[i]=max(130,min(8060,abs(g[i])+random.randint(-250,250)))*(1 if i<2 else -1); g=tuple(g)
    sc=ev(g); pool.append((sc,g)); out.write(json.dumps({'g':g,'sc':sc})+'\n'); out.flush()
