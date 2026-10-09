"""Season-2 final vs my freeze13 forecast (8 placements, salt 505) and the noise of an 8-placement replica,
estimated from the final's own 32 runs per pair (random 8-of-32 subsets)."""
import re, random, statistics as st, sys, os
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.dirname(H)
fin = os.path.join(C, "final/run/season2/final-32900213.txt")
runs = {}
for line in open(fin):
    p = line.split()
    if len(p) == 7 and re.fullmatch(r"[0-9a-f]{16}", p[0]):
        a, b, k, _, wa, wb, t = p[0], p[1], int(p[2]), p[3], int(p[4]), int(p[5]), int(p[6])  # line: a b run offset Wa Wb T (fixed 09.10: was read as Wa T Wb)
        runs.setdefault((a, b), {})[k] = (wa, t, wb)
names, pred = {}, {}
for line in open(os.path.join(C, "pred13/table_s8_salt505.txt")):
    m = re.match(r"\s*\d+\s+([\d.]+)\s+12\s+\d+\s+\d+\s+\d+\s+(.*) \(pred13/members/([0-9a-f]{16})\.red\)", line)
    if m: pred[m.group(3)] = float(m.group(1)); names[m.group(3)] = m.group(2)
ids = sorted(names)
npairs = len(runs); nfull = sum(len(v) == 32 for v in runs.values())
print(f"pairs with data {npairs}/78, complete (32 runs) {nfull}")
def total(w, pick):
    s = 0.0
    for (a, b), r in runs.items():
        if w not in (a, b): continue
        ks = pick(sorted(r))
        s += st.mean((3 * r[k][0] + r[k][1]) if w == a else (3 * r[k][2] + r[k][1]) for k in ks)
    return s
final = {w: total(w, lambda ks: ks) for w in ids}
rng = random.Random(9)
sd8 = {}
for w in ids:
    xs = [total(w, lambda ks: rng.sample(ks, 8)) for _ in range(200)]
    sd8[w] = st.pstdev(xs)
order = sorted(ids, key=lambda w: -final[w]); porder = sorted(ids, key=lambda w: -pred[w])
print(f"{'#':>2} {'warrior':24} {'final':>8} {'pred':>8} {'err':>6} {'sd8':>5} pred#")
errs = []
for i, w in enumerate(order, 1):
    e = pred[w] - final[w]; errs.append(abs(e))
    print(f"{i:2} {names[w][:24]:24} {final[w]:8.1f} {pred[w]:8.1f} {e:+6.0f} {sd8[w]:5.0f} {porder.index(w)+1}")
within = sum(x <= 150 for x in errs)
print(f"within 150: {within}/13; median |err| {st.median(errs):.0f}; max |err| {max(errs):.0f}")
print(f"ranks 1-5 unchanged: {order[:5] == porder[:5]}")
print(f"median sd of an 8-placement total (8-of-32 subsets of the final): {st.median(sd8.values()):.0f}, max {max(sd8.values()):.0f}")
