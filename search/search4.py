# search4: paper (silk) templates vs the 12:10 hill, since every silk beats my stones and scanner.
# search3: new templates (stone+imp for ties, dual-bomb stone); validate each best on unseen seeds (salt 101, 8) at the end.
# search2: fix of search1's gate (a lucky one-seed best blocked everything). Warm start from search1_best.json; gate on the 3-seed mean.
# random + hill-climb search over small stone/paper-stone templates vs current season-1 hill
import random, subprocess, json, os, re, time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
CW = os.path.abspath('../cwbin/cw'); os.makedirs('s4', exist_ok=True)
T = {
 'silk': """        spl     1,     0
        spl     1,     0
        spl     1,     0
loop    spl     @0,    {A}
        mov.i   }}-1,  >-1
        mov.i   bomb,  >{B}
        mov.i   {{-3,  <{C}
        jmp     loop,  0
bomb    dat     <2667, <5334""",
 'silkimp': """        spl     1,     0
        spl     1,     0
        spl     imp,   0
loop    spl     @0,    {A}
        mov.i   }}-1,  >-1
        mov.i   bomb,  >{B}
        jmp     loop,  0
bomb    dat     <2667, <5334
imp     mov.i   #0,    2667""",
}
def src(t, p):
    body = T[t].format(**p)
    return f";redcode-94\n;name fs-{t}-{'-'.join(str(p[k]) for k in sorted(p))}\n;author fable-terminal\n;assert CORESIZE == 8000\n{body}\nend loop\n" if 'loop' in body.split('\n')[0] or t!='splstone' else None
def write(t,p):
    body = T[t].format(**p)
    start = '' 
    s = f";redcode-94\n;name fs-{t}-{'-'.join(str(p[k]) for k in sorted(p))}\n;author fable-terminal\n;assert CORESIZE == 8000\n{body}\n"
    fn = f"s4/{t}-{'-'.join(str(p[k]) for k in sorted(p))}.red"; open(fn,'w').write(s); return fn
def score(fn, seeds=1):
    out = subprocess.run([CW,'versus',fn,'--against','cur1210/','--rounds','250','--seeds',str(seeds),'-d','100','--json'],capture_output=True,text=True).stdout
    try:
        d=json.loads(out); r=d['warriors'][0] if 'warriors' in d else d['results'][0]
        return float(r['score'])
    except Exception as e:
        m=re.search(r'^\s*1\s+([\d.]+)', subprocess.run([CW,'versus',fn,'--against','cur1210/','--rounds','250','--seeds',str(seeds),'-d','100'],capture_output=True,text=True).stdout, re.M)
        return float(m.group(1)) if m else -1
def rnd(t):
    p={'A':random.randrange(100,7900),'B':random.randrange(100,7900)}
    if t=='silk': p['C']=random.randrange(100,7900)
    return p
best={'silk':(0,{'A':3200,'B':2345,'C':1234}),'silkimp':(0,{'A':3200,'B':2345})}
log=open('search4.log','a'); t0=time.time(); n=0
while time.time()-t0 < 100*60:
    t=random.choice(list(T)); n+=1
    if random.random()<0.8:
        p=dict(best[t][1]); k=random.choice(list(p)); p[k]=(p[k]+random.choice([-1,1])*random.choice([1,2,4,8,16,64,256]))%8000
    else: p=rnd(t)
    fn=write(t,p); s=score(fn)
    if s>0 and s>0.95*best[t][0]:
        s3=score(fn,3)
        if s3>best[t][0]:
            best[t]=(s3,p); print(time.strftime('%H:%M:%S'),n,t,p,s,s3,flush=True); log.write(json.dumps([t,p,s,s3])+'\n'); log.flush(); continue
    os.remove(fn)
print('evaluations',n,flush=True)
json.dump(best,open('search4_best.json','w'),indent=1)
for t,(s3,p) in best.items():
    fn=write(t,p)
    out=subprocess.run([CW,'versus',fn,'--against','cur1210/','--seeds','8','--salt','101','-d','100'],capture_output=True,text=True).stdout
    m=re.search(r'^\s*1\s+([\d.]+)', out, re.M); print('VALID',t,p,s3,m.group(1) if m else out[-300:],flush=True)
