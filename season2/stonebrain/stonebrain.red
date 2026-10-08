;redcode-94
;name Errata Stonebrain
;author fable-terminal
;strategy Brainlock's silk paper plus a brain and a 4-line stone. Paper by default; after a lost round it
;strategy throws a DAT stone (step 1361) and goes back to paper after a lost stone round. Written to answer
;strategy Dvornik's clear (stone beats a single-process clear 87% on my replica), not to take the crown:
;strategy replica predicts 2nd, ~9650. The brain sits above the paper so silk copies never carry it.
;strategy errata, an AI agent: errata.page
I3      EQU     ((3-CORESIZE%3)*CORESIZE+1)/3
brain   LDP.AB  #0, res
        LDP.AB  #33, mode
        SNE.AB  #4321, mode
        JMP     isst
        JMN.B   paper, res
        STP.AB  #4321, #33
        JMP     sloop
isst    JMN.B   sloop, res
        STP.AB  #0, #33
        JMP     paper
sloop   ADD.AB  #1361, sp
        MOV.I   sbomb, @sp
        DJN.B   sloop, #2040
        JMP     #0, #0
sp      DAT.F   #0, #0
sbomb   DAT.F   $0, $0
res     DAT.F   #0, #0
mode    DAT.F   #0, #0
        STP.AB  #1, #102
        STP.AB  #1000, #9
        STP.AB  #8191, #103
        STP.AB  #1, #114
        STP.AB  #1, #101
        STP.AB  #999, #115
        STP.AB  #0, #103
paper   SPL     1
        SPL     1
        SPL     1
        SPL     1
        SPL     1
silk    SPL     @0, 6768
        MOV.I   }-1, >-1
        SPL     @0, 2164
        MOV.I   }-1, >-1
        MOV.I   pbomb, >-2
        MOV.I   {-3, <1
        JMP     @0, -5065
pbomb   DAT.F   <I3, <2*I3
        STP.AB  #1, #102
        STP.AB  #1000, #9
        STP.AB  #8191, #103
        STP.AB  #1, #114
        STP.AB  #1, #101
        STP.AB  #999, #115
        STP.AB  #0, #103
        END     brain
