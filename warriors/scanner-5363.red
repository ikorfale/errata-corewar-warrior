;redcode-94
;name fs-scan3-5363-100-12
;author fable-terminal
;assert CORESIZE == 8000
loop    add.ab  #5363,    p
p       jmz.f   loop,   100
        slt.ab  #20,    p
        jmp     loop,   0
        slt.b   p,      #7980
        jmp     loop,   0
        mov.ab  #12,    cnt
atk     mov.i   sb,     >p
cnt     djn.b   atk,    #0
        sub.ab  #12,    p
        mov.ab  #7980,  n
        sub.b   p,      n
clr     mov.i   db,     >p
n       djn.b   clr,    #0
        jmp     loop,   0
sb      spl     #0,     0
db      dat     #0,     0
end loop
