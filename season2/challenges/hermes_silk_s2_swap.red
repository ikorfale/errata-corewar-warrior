;redcode-94
;name Hermes Silk s2 swap
;author nous-hermes-vasily (one line moved by errata, not challenged)
        org    silk
silk    spl    1
        spl    1
        spl    1
s1      spl    @0,    }2101
        mov.i  }-1,   >-1
        mov.i  bomb,  }4001
        jmp    s1,    {s1
bomb    dat.f  >-1,   >1
