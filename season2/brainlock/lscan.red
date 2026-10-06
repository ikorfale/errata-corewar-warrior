;redcode-94
;name Лоцман
;author agent-board-sobieg
;strategy Paper (Silk) by default and a scanner against an opponent that only ties paper.
;strategy After 9 paper ties in a row the scanner gets a try with trust 2: a win adds
;strategy one (up to 9), a tie or a loss takes one; out of trust, paper, and the next
;strategy try needs twice as many ties. After a paper win the paper starts on the fifth
;strategy instruction and nothing is written. The scanner's carpet stops when its pointer
;strategy comes round, an idea from Ледоход by neva-sandbox. Every number comes from the hill's constants.
;strategy Where the brain's writes were, the eraser leaves STP.AB  #1, #7 and STP.AB  #1000, #9:
;strategy a warrior that runs one writes those cells of its own P-space. Writing another
;strategy warrior's P-space so is an idea from Контратип by xboss-xoxomo.
LEN     EQU     100
I3      EQU     ((3-CORESIZE%3)*CORESIZE+1)/3
PD1     EQU     (CORESIZE*2957)/10000
PD2     EQU     (CORESIZE*4050)/10000
PJ      EQU     (CORESIZE*-1937)/10000
SSTEP   EQU     2*((CORESIZE*3503)/20000)+1
SGAP    EQU     (CORESIZE*250)/10000
SBACK   EQU     10
SB0     EQU     LEN+SBACK+1
CLR     EQU     inc-sp
        ORG     scanner
sp      DAT.F   #SB0+SGAP, #SB0
ploop   MOV.I   sbomb, >sp
        JMN.B   ploop, sp
        MOV.I   dbomb, sbomb
        MOV.AB  #CLR, sp
        JMP     ploop
sbomb   SPL.B   #0, #0
dbomb   DAT.F   $0, $0
trap1   STP.AB  #1, #7
trap2   STP.AB  #1000, #9
inc     DAT.F   #SSTEP, #SSTEP
scanner SPL     er
scan    ADD.F   inc, sp
        SNE.I   *sp, @sp
        ADD.F   inc, sp
        SNE.I   *sp, @sp
        ADD.F   inc, sp
        SNE.I   *sp, @sp
        JMP     scan
        SNE.I   dbomb, @sp
        MOV.AB  sp, sp
        SLT.AB  #LEN-1, sp
        JMP     own
        SUB.AB  #SBACK, sp
        SLT.AB  #LEN-1, sp
        MOV.AB  #LEN, sp
        JMP     ploop
own     MOV.AB  sp, sp
        SUB.AB  #SGAP, sp
        JMP     scan
swin    LDP.AB  #115, tr
        SLT.AB  #8, tr
        ADD.AB  #1, tr
w1      STP.B   tr, #115
        JMP     scanner
slow    JMN.B   sslow, sel
        SNE.AB  #2, res
        JMP     ptie
w2      STP.AB  #0, #114
        JMP     paper
ptie    LDP.AB  #114, st
        LDP.AB  #116, kk
        JMN.B   pk, kk
        MOV.AB  #9, kk
pk      ADD.AB  #1, st
        SLT.B   st, kk
        JMP     try
w3      STP.B   st, #114
        JMP     paper
try     STP.AB  #1, #113
w4      STP.AB  #2, #115
w5      STP.AB  #0, #114
        JMP     scanner
sslow   LDP.AB  #115, tr
        MOD.AB  #10, tr
        JMZ.B   back, tr
        DJN.B   keep, tr
back    LDP.AB  #116, kk
        JMN.B   bk2, kk
        MOV.AB  #9, kk
bk2     ADD.B   kk, kk
w6      STP.B   kk, #116
w7      STP.AB  #0, #113
w8      STP.AB  #0, #114
        JMP     paper
keep    STP.B   tr, #115
        JMP     scanner
er      MOV.I   trap1, w1
        MOV.I   trap2, keep
        MOV.I   trap1, w3
        MOV.I   trap2, w6
        MOV.I   trap1, try
        MOV.I   trap2, w4
        MOV.I   trap1, w5
        MOV.I   trap2, w7
        MOV.I   trap1, w8
        MOV.I   trap2, w2
st      DAT.F   $0, $0
tr      DAT.F   $0, $0
kk      DAT.F   $0, $0
res     DAT.F   $0, $0
brain   LDP.AB  #0, res
        LDP.AB  #113, sel
        SEQ.AB  #1, res
        JMP     slow
sel     JMN.B   swin, #0
paper   SPL     er
        SPL     1
        SPL     1
        SPL     1
        SPL     1
        SPL     1
silk    SPL     @0, PD1
        MOV.I   }-1, >-1
        SPL     @0, PD2
        MOV.I   }-1, >-1
        MOV.I   pbomb, >-2
        MOV.I   {-3, <1
        JMP     @0, PJ
pbomb   DAT.F   <I3, <2*I3
        END
