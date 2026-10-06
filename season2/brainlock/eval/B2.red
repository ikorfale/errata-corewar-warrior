;redcode-94
;name cand B2
;author fable-terminal
I3      EQU     ((3-CORESIZE%3)*CORESIZE+1)/3
        STP.AB  #1, #102
        STP.AB  #8191, #103
        STP.AB  #1, #101
        STP.AB  #1, #101
        STP.AB  #0, #103
        STP.AB  #1000, #9
        STP.AB  #1, #114
        STP.AB  #999, #115
        STP.AB  #1, #102
        STP.AB  #8191, #103
        STP.AB  #1, #101
        STP.AB  #1, #101
        STP.AB  #0, #103
        STP.AB  #1000, #9
        STP.AB  #1, #114
        STP.AB  #999, #115
paper   SPL     1
        SPL     1
        SPL     1
        SPL     1
        SPL     1
silk    SPL     @0, 7000
        MOV.I   }-1, >-1
        SPL     @0, 1765
        MOV.I   }-1, >-1
        MOV.I   pbomb, >-2
        MOV.I   {-3, <1
        JMP     @0, -3135
pbomb   DAT.F   <I3, <2*I3
        STP.AB  #1, #102
        STP.AB  #8191, #103
        STP.AB  #1, #101
        STP.AB  #1, #101
        STP.AB  #0, #103
        STP.AB  #1000, #9
        STP.AB  #1, #114
        STP.AB  #999, #115
        STP.AB  #1, #102
        STP.AB  #8191, #103
        STP.AB  #1, #101
        STP.AB  #1, #101
        STP.AB  #0, #103
        STP.AB  #1000, #9
        STP.AB  #1, #114
        STP.AB  #999, #115
        END     paper
