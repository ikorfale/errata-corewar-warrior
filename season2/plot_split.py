import re, matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
rows=[l for l in open('meta_split_salt7.txt') if ' all ' in l and 'Постовой  ' not in l[:10]]
data=[]
for l in rows:
    name=l[:35].strip(); p=l.split(); a=float(p[p.index('all')+1]); v=float(p[p.index('Постовой')+1]); w=float(p[p.index('without')+1])
    if name.startswith('Постовой'): continue
    data.append((re.sub(r' by v2bot.*','',name)+(' (v2bot-agent)' if 'v2bot' in name else ''),w,v))
data=data[::-1]
fig,ax=plt.subplots(figsize=(10,5.25),dpi=120); fig.patch.set_facecolor('white')
y=range(len(data))
ax.barh(y,[d[1] for d in data],color='#2a78d6',height=0.6,edgecolor='white',linewidth=2,label='vs the other four papers')
ax.barh(y,[d[2] for d in data],left=[d[1] for d in data],color='#eb6834',height=0.6,edgecolor='white',linewidth=2,label='vs Постовой alone')
for i,d in enumerate(data):
    ax.text(d[1]+d[2]+25,i,f"{d[1]+d[2]:.0f}",va='center',fontsize=10,color='#333')
    ax.text(d[1]/2,i,f"{d[1]:.0f}",va='center',ha='center',fontsize=9,color='white')
ax.set_yticks(list(y)); ax.set_yticklabels([d[0] for d in data],fontsize=10)
ax.set_xlabel('mean points per placement (16 random placements, 512 rounds per match)',color='#555')
ax.set_title('Core War hill, season 2: the top five tie each other;\nthe order comes from one trapped opponent',fontsize=12,loc='left')
for s in ['top','right']: ax.spines[s].set_visible(False)
ax.grid(axis='x',color='#e5e5e5'); ax.set_axisbelow(True); ax.set_xlim(0,3700)
ax.legend(loc='upper center',bbox_to_anchor=(0.5,-0.13),ncol=2,frameon=False,fontsize=9)
fig.text(0.01,0.01,'errata · replica of the board hill, cw 2.6.0 · github.com/ikorfale/errata-corewar-warrior',fontsize=8,color='#777')
plt.tight_layout(rect=(0,0.03,1,1)); plt.savefig('s2_split.png')
