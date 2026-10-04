"""Kiln self-kill time: real engine (cw 2.6.0) vs two arithmetic models.
true model: MOV.I bomb,@bomb writes to bomb + bomb.B (pointer is the bomb cell).
mov-relative model: the indirect is resolved from the MOV cell instead (suspected sim bug)."""
import subprocess, json
CW = "cw"  # cw 2.6.0 on PATH
N = 8000
open("idle.red", "w").write(";redcode-94\n;name idle\njmp 0\n")
def kiln(step):
    fn = f"kiln_{step}.red"
    open(fn, "w").write(f""";redcode-94
;name Kiln{step}
        ORG start
start   ADD.AB #{step}, bomb
        MOV.I  bomb, @bomb
        JMP.B  start, #0
bomb    DAT.F  #0, #0
        END
""")
    return fn
POS = {}
def dies_by(fn, c):
    out = subprocess.run([CW, "battle", "--json", "-c", str(c), "--pos", str(POS[fn]), fn, "idle.red"],
                         capture_output=True, text=True).stdout
    return out
def first_hit(step, offs):
    for k in range(1, N + 1):
        if (step * k) % N in offs: return k
def dead(fn, c):
    j = json.loads(dies_by(fn, c)); return j["result"]["w2"] == 1
rows = []
for step in [3039, 2667, 1067, 553, 100, 20, 4, 4004]:
    fn = kiln(step)
    # put the idle warrior on the cell Kiln's bombs reach last (or never), at least 100 away
    firsthit = {}
    for k in range(1, N + 1):
        firsthit.setdefault((3 + step * k) % N, k)
    POS[fn] = max(range(100, N - 100), key=lambda o: firsthit.get(o, 10**9))
    if not dead(fn, 80000):
        rows.append((step, "alive", None, None)); continue
    lo, hi = 1, 80000          # smallest cycle limit at which Kiln is already dead
    while lo < hi:
        m = (lo + hi) // 2
        if dead(fn, m): hi = m
        else: lo = m + 1
    k_true = first_hit(step, {N - 3, N - 2, N - 1})
    k_mov = first_hit(step, {N - 1, 0, 1})
    rows.append((step, lo, k_true, k_mov, POS[fn], firsthit.get(POS[fn])))
print("step  cw_dead_by_cycle  first_selfhit_bomb(true)  same(if @ resolved from MOV)")
for r in rows: print(*r, sep="\t")
