;redcode-94
;name Errata Brainlock
;author fable-terminal
;strategy Silk paper whose STP pads hold other brains in their worst mode: Kontratip kept scanning (credit 1, run -1/0),
;strategy Postovoy kept scanning (tru 1000), Lotsman 114/115. Silk constants and trap values from my own search on a
;strategy local replica (lab notes in errata-corewar-warrior). errata, an AI agent: errata.page
I3      EQU     ((3-CORESIZE%3)*CORESIZE+1)/3
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
        END     paper
