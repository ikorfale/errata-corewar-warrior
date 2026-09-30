;redcode-94
;name Errata Silk
;author fable-terminal
;assert CORESIZE == 8000
        spl     1,     0
        spl     1,     0
        spl     1,     0
loop    spl     @0,    2804
        mov.i   }-1,  >-1
        mov.i   bomb,  >1349
        mov.i   {-3,  <5168
        jmp     loop,  0
bomb    dat     <2667, <5334
