;redcode-94
;name silk8192
;author fable-terminal
I3      EQU     ((3-CORESIZE%3)*CORESIZE+1)/3
PD1     EQU     (CORESIZE*2957)/10000
PD2     EQU     (CORESIZE*4050)/10000
PJ      EQU     (CORESIZE*-1937)/10000
paper   SPL     1
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
        END     paper
