"""tsearch.py OPP CELLS SECS SEED — search trap lists against one brainy opponent; other traps fixed (FIX)."""
import json, random, sys, time
from gen import render
from k1 import run
opp=sys.argv[1]; cells=[int(c) for c in sys.argv[2].split(',')]; secs=float(sys.argv[3]); tag=sys.argv[5]
FIX=json.loads(sys.argv[6]) if len(sys.argv)>6 else []
VALS=[0,1,2,3,4,5,9,10,13,14,100,999,1000,8191]
def rnd(): return (random.choice(VALS),random.choice(cells))
def ev(k):
    t=[tuple(x) for x in FIX]+k; t=t*2
    open(f'ts_{tag}.red','w').write(render(t,t,d1=7000,d2=1870,name='ts'))
    s=run(f'ts_{tag}.red',[opp],seeds=4)['standings'][0]; return s['score'],(s['wins'],s['losses'],s['ties'])
random.seed(int(sys.argv[4])); out=open(f'tsearch_{tag}.jsonl','a'); t0=time.time(); pool=[]
while time.time()-t0<secs:
    if pool and random.random()<0.6:
        k=list(random.choice(sorted(pool,reverse=True)[:5])[1]); i=random.randrange(len(k)+1)
        r=random.random()
        if r<0.4 and k: k[min(i,len(k)-1)]=rnd()
        elif r<0.6 and len(k)>1: k.pop(min(i,len(k)-1))
        else: k.insert(i,rnd())
        k=k[:5]
    else: k=[rnd() for _ in range(random.randint(1,3))]
    sc,wlt=ev(k); pool.append((sc,k)); out.write(json.dumps({'k':k,'sc':sc,'wlt':wlt})+'\n'); out.flush()
