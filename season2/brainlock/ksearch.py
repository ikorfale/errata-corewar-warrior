import json, random, sys, time
from gen import render
from k1 import run
K='../cur3/00_e6837a4b53f7874e.red'
VALS={101:[0,1,2,3],102:[0,1,2,5,10,1000,8191],103:[0,1,2,5,999,1000,8000,8191]}
def rnd():
    n=random.randint(1,4); return [(random.choice(VALS[c]),c) for c in random.choices([101,102,103],k=n)]
def ev(k, seeds=4):
    t=[(1,113),(9,115)]+k+[(1000,9)]; t=t*3
    open('ks.red','w').write(render(t,t,d1=7000,d2=1870,name='ks'))
    s=run('ks.red',[K],seeds=seeds)['standings'][0]; return s['score'],(s['wins'],s['losses'],s['ties'])
random.seed(7); out=open('ksearch.jsonl','a'); t0=time.time(); pool=[]
while time.time()-t0<float(sys.argv[1]):
    if pool and random.random()<0.6:
        k=list(random.choice(sorted(pool,reverse=True)[:5])[1]); i=random.randrange(len(k)+1)
        if random.random()<0.5 and k: k[min(i,len(k)-1)]=rnd()[0]
        else: k.insert(i,rnd()[0])
        k=k[:5]
    else: k=rnd()
    sc,wlt=ev(k); pool.append((sc,k)); out.write(json.dumps({'k':k,'sc':sc,'wlt':wlt})+'\n'); out.flush()
