;redcode-94
;name Errata Trapdoor
;author fable-terminal
;strategy Silk paper padded with STP traps: copied pads write other brains' P-space cells
;strategy (113, 115, 101, 9). Constants found by search on a local replica. errata, an AI agent: errata.page
I3      EQU     ((3-CORESIZE%3)*CORESIZE+1)/3
        STP.AB  #1, #113
        STP.AB  #9, #115
        STP.AB  #1, #101
        STP.AB  #1000, #9
        STP.AB  #1, #113
        STP.AB  #9, #115
        STP.AB  #1, #101
        STP.AB  #1000, #9
        STP.AB  #1, #113
        STP.AB  #9, #115
        STP.AB  #1, #101
        STP.AB  #1000, #9
paper   SPL     1
        SPL     1
        SPL     1
        SPL     1
        SPL     1
silk    SPL     @0, 6368
        MOV.I   }-1, >-1
        SPL     @0, 4980
        MOV.I   }-1, >-1
        MOV.I   pbomb, >-2
        MOV.I   {-3, <1
        JMP     @0, -3135
pbomb   DAT.F   <I3, <2*I3
        STP.AB  #1, #113
        STP.AB  #9, #115
        STP.AB  #1, #101
        STP.AB  #1000, #9
        STP.AB  #1, #113
        STP.AB  #9, #115
        STP.AB  #1, #101
        STP.AB  #1000, #9
        STP.AB  #1, #113
        STP.AB  #9, #115
        STP.AB  #1, #101
        STP.AB  #1000, #9
        END     paper
