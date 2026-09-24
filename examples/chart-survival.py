#!/usr/bin/env python3
"""How long a Snowflake Marketplace data listing stays on sale."""
import json, pathlib, sys
import plate
from plate import INK, INK2, MUTED, RULE, GRID, FAINT

W, H = 880, 600
SERIES = "#2f6f5e"
ALERT  = "#b4472e"


def main():
    here = pathlib.Path(__file__).resolve()
    src = sys.argv[1] if len(sys.argv) > 1 else str(sorted((here.parents[1] / "public").glob("survival-*.json"))[-1])
    d = json.load(open(src))
    km = d["km"]; n = d["n"]; deaths = d["deaths"]
    med = next((t for t, s in km if s <= 0.5), None)

    s = plate.open_svg(W, H,
        f"Half of Snowflake's data listings are withdrawn within {med:,} days",
        subtitle=f"Kaplan-Meier, {n:,} listings with an observed arrival. {deaths:,} withdrawals, "
                 f"{n-deaths:,} right-censored.")
    f, y = plate.frame(W, 88,
        who="Anyone about to build a pipeline on a third-party Snowflake listing",
        decide="Whether to depend on a listing still being on sale in a year, or two",
        wrong="The curve is flat — listings essentially never leave, and dependence is free")
    s += f

    x0, x1 = 84, W - 132
    top, bot = y + 34, H - 128
    XMAX = 1200
    def px(t): return x0 + (x1 - x0) * min(t, XMAX) / XMAX
    def py(v): return bot - (bot - top) * v

    for v in (0, .25, .5, .75, 1.0):
        gy = py(v)
        s.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="{GRID}"/>')
        s.append(plate.txt(x0 - 9, gy + 3.5, f"{int(v*100)}", size=10.5, fill=MUTED, anchor="end"))
    for t in (0, 365, 730, 1095):
        gx = px(t)
        s.append(f'<line x1="{gx:.1f}" y1="{top}" x2="{gx:.1f}" y2="{bot}" stroke="{GRID}"/>')
        s.append(plate.txt(gx, bot + 17, f"{t:,}", size=10.5, fill=MUTED, anchor="middle"))
    s.append(plate.txt(x0 - 9, top - 14, "% still listed", size=10, fill=MUTED, anchor="end"))
    s.append(plate.txt((x0 + x1) / 2, bot + 36, "days since first seen in the sitemap", size=10.5, fill=MUTED, anchor="middle"))

    # STEP function, not a smooth line: survival is constant between deaths and
    # a diagonal would assert a gradual decline that did not happen.
    pts = []
    pv = 1.0
    for t, v in km:
        if t > XMAX: break
        pts.append(f"{px(t):.1f},{py(pv):.1f}")
        pts.append(f"{px(t):.1f},{py(v):.1f}")
        pv = v
    pts.append(f"{px(XMAX):.1f},{py(pv):.1f}")
    s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{SERIES}" stroke-width="2.4"/>')

    if med and med <= XMAX:
        s.append(f'<line x1="{x0}" y1="{py(.5):.1f}" x2="{px(med):.1f}" y2="{py(.5):.1f}" '
                 f'stroke="{ALERT}" stroke-width="1.5" stroke-dasharray="4 3"/>')
        s.append(f'<line x1="{px(med):.1f}" y1="{py(.5):.1f}" x2="{px(med):.1f}" y2="{bot}" '
                 f'stroke="{ALERT}" stroke-width="1.5" stroke-dasharray="4 3"/>')
        s += plate.halo(px(med) - 10, py(.5) - 9, f"median {med:,} days", size=12, fill=ALERT, anchor="end")

    lx = x1 + 22
    s.append(plate.txt(lx, top + 4, "STILL LISTED AFTER", size=9, fill=MUTED, weight="700", spacing="0.8"))
    for i, mark in enumerate((90, 180, 365, 730, 1095)):
        v = next((s_ for t, s_ in reversed(km) if t <= mark), 1.0)
        s += plate.halo(lx, top + 26 + i * 30, f"{100*v:.1f}%", size=15, fill=INK)
        s.append(plate.txt(lx, top + 40 + i * 30, f"{mark:,} days", size=10, fill=MUTED))

    s.append(f'<line x1="28" y1="{H-74:.1f}" x2="{W-28}" y2="{H-74:.1f}" stroke="{RULE}"/>')
    s += plate.wrap(28, H - 58,
        f"Snowflake Marketplace sitemap: {d['snapshots']} snapshots, {d['span'][0]} to {d['span'][1]}, via "
        f"the Internet Archive plus one live capture. Listings "
        f"present in the first snapshot are EXCLUDED: their arrival was not observed, so their age "
        f"is unknown. A withdrawal is dated to the midpoint between the last snapshot showing it and "
        f"the next one. Gaps between snapshots run from days to two months, so short lives are the "
        f"least well resolved.",
        size=10, fill=MUTED, chars=132, leading=13)
    s.append("</svg>")
    out = here.parent / "charts" / "survival.svg"
    out.write_text("\n".join(s), encoding="utf-8")
    print(f"  wrote {out.name}  (median {med}d, n={n:,})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
