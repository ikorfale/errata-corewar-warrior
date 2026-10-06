;redcode-94
;name Контратип
;author xboss-xoxomo
;strategy Следующая копия после Интерпозитива.

ptr       DAT.F   #211, #100
inc       DAT.F   #1547, #1547
scan      ADD.F   inc, ptr
          SNE.I   *ptr, @ptr
          ADD.F   inc, ptr
          SNE.I   *ptr, @ptr
          ADD.F   inc, ptr
          SNE.I   *ptr, @ptr
          JMP.B   scan, $0
          MOV.B   ptr, cnt
          SNE.I   db, @ptr
          MOV.AB  ptr, cnt
          SLT.AB  #95, cnt
          JMP.B   scan, $0
          SUB.AB  #10, cnt
          SLT.AB  #94, cnt
          MOV.AB  #95, cnt
          MOV.BA  cnt, ptr
carpet    MOV.I   sb, }ptr
          JMN.A   carpet, ptr
          MOV.I   db, sb
          MOV.A   #26, ptr
          JMP.B   carpet, $0
db        DAT.F   $0, $0
sb        SPL.B   #0, #0
cnt       DAT.F   $0, $0
sloop     ADD.AB  #3364, sjp
          MOV.I   sbomb, @sjp
sjp       JMP.B   sloop, #1
sbomb     DAT.F   $0, $0
boot      MOV.I   }cp, >cp
          DJN.B   boot, #4
          JMP.B   cp+4000, $0
cp        DAT.F   #sloop, #4000
brain     LDP.AB  #0, res
          LDP.AB  #101, mode
          LDP.AB  #102, credit
          SLT.B   mode, #3
          MOV.AB  #0, mode
          SLT.B   credit, #1001
          MOV.AB  #10, credit
          JMZ.B   plogic, mode
          LDP.AB  #103, run
          MOD.AB  #2, res
          SEQ.AB  #0, res
          MOV.AB  #7999, run
          ADD.AB  #1, run
          SLT.B   run, #999
          JMP.B   lockp, $0
          SLT.B   run, @mode
          JMP.B   lockx, $0
          JMP.B   save, $0
plogic    JMZ.B   ploss, res
          SEQ.AB  #2, res
          ADD.AB  #5, credit
          DJN.B   psave, credit
toscan    MOV.AB  #1, mode
probe     LDP.AB  #103, run
          ADD.AB  #999, run
          JMP.B   save, $0
ploss     MOV.AB  #2, mode
          JMP.B   probe, $0
lockx     MOV.AB  #5, credit
          JMP.B   lockm, $0
lockp     SUB.AB  #990, run
          MOV.B   run, credit
lockm     MOV.AB  #0, mode
save      STP.B   mode, #101
          STP.B   run, #103
psave     STP.B   credit, #102
          MOV.I   pois0, save
          MOV.I   res, save+1
          MOV.I   res, save+2
          JMZ.B   paper, mode
          DJN.B   boot, mode
          JMP.B   scan, $0
res       DAT.F   $0, $0
mode      DAT.F   $0, $0
thrs      DAT.F   $0, $6
thrt      DAT.F   $0, $2
credit    DAT.F   $0, $0
run       DAT.F   $0, $0
pois0     STP.AB  #1, #7
paper     SPL.B   $1, $0
          SPL.B   $1, $0
          SPL.B   $1, $0
          SPL.B   $1, $0
silk      SPL.B   @0, $4200
          MOV.I   }-1, >-1
          SPL.B   @0, $2400
          MOV.I   }-1, >-1
          MOV.I   pbomb, >-2
          MOV.I   {-3, <1
          JMP.B   @0, $-1922
pbomb     DAT.F   <2667, <5334

          END boot
;копия 060
