import sys
def make(U,PASSES,pads=True,name='t-cl'):
    L=[';redcode-94',';name '+name,';author fable-terminal','        ORG     clear','first   DAT.F   #0, #0']
    if pads: L+=['        STP.AB  #1, #102','        STP.AB  #1000, #9','        STP.AB  #8191, #103','        STP.AB  #1, #114','        STP.AB  #1, #101','        STP.AB  #999, #115','        STP.AB  #0, #103']
    L+=['clear   MOV.AB  #(CORESIZE-LEN)/%d, cnt'%U,'        MOV.AB  #(last-cptr), cptr']
    L+=[('cloop' if i==0 else '     ')+'   MOV.I   cb, >cptr' for i in range(U)]
    L+=['        DJN.B   cloop, cnt','        DJN.B   clear, passes','        MOV.I   cdb, cb','        JMP     clear',
        'cb      SPL.B   #0, #0','cdb     DAT.F   $0, $0','passes  DAT.F   #0, #%d'%PASSES,'cnt     DAT.F   #0, #0','cptr    DAT.F   #0, #0','last    DAT.F   #0, #0','LEN     EQU     (last-first+1)','        END']
    return '\n'.join(L)+'\n'
for U in (8,12,16):
  for P in (1,2,3):
    for pads in (True,False):
      open(f'd1/cl/u{U}p{P}{"pad" if pads else "nop"}.red','w').write(make(U,P,pads,f't-cl-u{U}p{P}'))
