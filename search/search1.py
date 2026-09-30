"""Random search plus hill-climbing over three small warrior templates, scored against a
directory of hill warriors with the board's engine (`cw versus`, 250 rounds, 1 seed to screen,
3 seeds to accept). Improvements are appended to search1.log as [template, params, 1-seed, 3-seed].
env: CW = path to the cw binary (default ../cw), HILL = directory of hill .red files (default ../hill/)
Runs for 3.5 hours; on one CPU a screen costs about a second."""
import random, subprocess, json, os, re, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CW = os.path.abspath(os.environ.get('CW', '../cw')); HILL = os.environ.get('HILL', '../hill/')
os.makedirs('s1', exist_ok=True)
T = {
 'stone': """loop    add.ab  #{S}, ptr
        mov.i   bomb,  @ptr
        djn.f   loop,  <{G}
ptr     dat     #0,    #{S}
bomb    dat     #0,    #0""",
 'splstone': """        spl     #0,    <{G}
loop    add.ab  #{S}, ptr
        mov.i   bomb,  @ptr
        jmp     loop,  <{G2}
ptr     dat     #0,    #{S}
bomb    dat     #0,    #0""",
 'stoneclear': """loop    add.ab  #{S}, ptr
        mov.i   bomb,  @ptr
        jmn     loop,  @ptr2
        spl     #0,    0
clr     mov.i   cb,    >ptr
        djn.f   clr,   <{G}
ptr     dat     #0,    #{S}
ptr2    dat     #0,    #{K}
cb      dat     #0,    #0
bomb    dat     #0,    #0""",
}
def write(t,p):
    body = T[t].format(**p)
    s = f";redcode-94\n;name fs-{t}-{'-'.join(str(p[k]) for k in sorted(p))}\n;author fable-terminal\n;assert CORESIZE == 8000\n{body}\n"
    fn = f"s1/{t}-{'-'.join(str(p[k]) for k in sorted(p))}.red"; open(fn,'w').write(s); return fn
def score(fn, seeds=1):
    out = subprocess.run([CW,'versus',fn,'--against',HILL,'--rounds','250','--seeds',str(seeds),'-d','100','--json'],capture_output=True,text=True).stdout
    try:
        d=json.loads(out); r=d['warriors'][0] if 'warriors' in d else d['results'][0]
        return float(r['score'])
    except Exception as e:
        m=re.search(r'^\s*1\s+([\d.]+)', subprocess.run([CW,'versus',fn,'--against',HILL,'--rounds','250','--seeds',str(seeds),'-d','100'],capture_output=True,text=True).stdout, re.M)
        return float(m.group(1)) if m else -1
def rnd(t):
    p={'S':random.randrange(2,4000),'G':random.randrange(-4000,4000)}
    if t=='splstone': p['G2']=random.randrange(-4000,4000)
    if t=='stoneclear': p['K']=random.randrange(10,4000)
    return p
best={}; log=open('search1.log','a'); t0=time.time()
while time.time()-t0 < 3.5*3600:
    t=random.choice(list(T))
    if t in best and random.random()<0.6:
        p=dict(best[t][1]); k=random.choice(list(p)); p[k]=(p[k]+random.choice([-1,1])*random.choice([1,2,4,8,16,64,256]))%8000
    else: p=rnd(t)
    fn=write(t,p); s=score(fn)
    if s<=0: os.remove(fn); continue
    if t not in best or s>best[t][0]:
        s3=score(fn,3)
        if t not in best or s3>best[t][2]:
            best[t]=(s,p,s3); print(time.strftime('%H:%M:%S'),t,p,s,s3,flush=True); log.write(json.dumps([t,p,s,s3])+'\n'); log.flush(); continue
    os.remove(fn)
json.dump({k:v for k,v in best.items()},open('search1_best.json','w'),indent=1)
