"""Forecast vs final, season 2: per-placement totals, with the measured 8-placement spread (±2 sd) around each forecast."""
import re, matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
rows = []
for line in open("comparison.txt"):
    m = re.match(r"\s*(\d+) (.{24})\s+([\d.]+)\s+([\d.]+)\s+([+-]\d+)\s+(\d+)", line)
    if m: rows.append((m.group(2).strip(), float(m.group(3)), float(m.group(4)), float(m.group(6))))
rows = rows[::-1]
fig, ax = plt.subplots(figsize=(10, 6.2), dpi=120)
ax.axvspan(-100, 100, color="#f3e1dc", zorder=0)
ax.axvline(0, color="#999", lw=1)
for i, (n, f, p, sd) in enumerate(rows):
    ax.plot([-2 * sd, 2 * sd], [i, i], color="#b8b2a6", lw=8, solid_capstyle="butt", zorder=1)
    ax.scatter(f - p, i, s=52, color="#d08a1e" if n.startswith("Errata") else "#1f5f8b", zorder=3)
    ax.text(155, i, f"#{len(rows) - i}  {f:,.0f}", va="center", fontsize=8, color="#555")
ax.set_xlim(-150, 210)
ax.set_yticks(range(len(rows))); ax.set_yticklabels([n for n, *_ in rows])
ax.set_xlabel("final minus forecast, points per placement (final total / 32)")
ax.set_title("Core War hill, season 2: final vs the forecast I committed before the freeze\n"
             "all 13 ranks held · dot = error · grey bar = ±2 sd of an 8-placement total (measured) · pink = the ±100 I guessed",
             fontsize=10, loc="left")
for s in ("top", "right"): ax.spines[s].set_visible(False)
ax.grid(axis="x", color="#eee"); plt.tight_layout(); plt.savefig("final_vs_forecast.png")
