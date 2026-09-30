;redcode-94
;name fs-stone-4165-2492
;author fable-terminal
;assert CORESIZE == 8000
loop    add.ab  #2492, ptr
        mov.i   bomb,  @ptr
        djn.f   loop,  <4165
ptr     dat     #0,    #2492
bomb    dat     #0,    #0
