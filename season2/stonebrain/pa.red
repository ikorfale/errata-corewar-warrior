;redcode-94
;name A
        LDP.AB  #0, r
        JMZ.B   die, r
l       JMP     l
die     DAT 0,0
r       DAT 0,0
