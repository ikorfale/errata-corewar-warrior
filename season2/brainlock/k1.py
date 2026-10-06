import subprocess, json, sys
from gen import render, TD
CW='../cw'
def run(f, opp, seeds=8, salt=3):
    r = subprocess.run([CW,'versus',f,'--against',*opp,'-s','8192','-c','65536','-p','8192','-l','128','-d','128','--rounds','512','--seeds',str(seeds),'--salt',str(salt),'--per','--json'],capture_output=True,text=True)
    d=json.loads(r.stdout); return d
if __name__=="__main__":
  d=run('../cur3/10_5fb0dd81cab344cf.red',['../cur3/00_e6837a4b53f7874e.red'])
  print(json.dumps(d)[:1500])
