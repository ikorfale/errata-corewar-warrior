# Season-2 replica: each member's mean score per placement, with and without matches against Постовой.
import json,collections,sys
d=json.load(open(sys.argv[1] if len(sys.argv)>1 else 'spread16_salt7.json'))
names=[w['name'] for w in d['warriors']]; on=[w['name'] for w in d['opponents']]
S=len(d['seeds']) if isinstance(d['seeds'],list) else 16
tot=collections.Counter(); vsP=collections.Counter(); ties=rounds=0
for x in d['matches']:
    a=names[x['a']]; b=on[x['b']]; r=x['result']; p=3*r['w1']+r['ties']
    tot[a]+=p
    if 'Постовой' in b: vsP[a]+=p
    if 'Постовой' not in a and 'Постовой' not in b: ties+=r['ties']; rounds+=r['w1']+r['w2']+r['ties']
print('seeds',S,'| rounds among the five papers:',rounds,'ties',ties,f'{ties/rounds:.3f}')
for a in sorted(tot,key=lambda a:-tot[a]):
    print(f"{a[:34]:35} all {tot[a]/S:7.1f}  vs Постовой {vsP[a]/S:7.1f}  without {(tot[a]-vsP[a])/S:7.1f}")
