;redcode-94
;name fs-silk-3200-2345-1234
;author fable-terminal
;assert CORESIZE == 8000
        spl     1,     0
        spl     1,     0
        spl     1,     0
loop    spl     @0,    3200
        mov.i   }-1,  >-1
        mov.i   bomb,  >2345
        mov.i   {-3,  <1234
        jmp     loop,  0
bomb    dat     <2667, <5334
