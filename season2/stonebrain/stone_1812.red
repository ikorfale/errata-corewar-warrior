;redcode-94
;name stone1812
;author fable-terminal
        ORG     sloop
sloop   ADD.AB  #1812, sjp
        MOV.I   sbomb, @sjp
sjp     JMP.B   sloop, #0
sbomb   DAT.F   $0, $0
        END
