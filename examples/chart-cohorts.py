#!/usr/bin/env python3
"""Survival by year of arrival: is the marketplace getting better at keeping listings?"""
import json, pathlib, sys
import plate
from plate import INK, INK2, MUTED, RULE, GRID, FAINT

W, H = 880, 580
COL = {"2023": "#b4472e", "2024": "#c08a3e", "2025": "#2f6f5e"}


def main():
    here = pathlib.Path(__file__).resolve()
    src = sys.argv[1] if len(sys.argv) > 1 else str(sorted((here.parents[1] / "public").glob("survival-*.json"))[-1])
    d = json.load(open(src)); coh = d["cohorts"]

    def at(km, day):
        return next((s for t, s in reversed(km) if t <= day), 1.0)
    y23, y25 = 100 * at(coh["2023"]["km"], 365), 100 * at(coh["2025"]["km"], 365)

    s = plate.open_svg(W, H,
        f"Listings arriving in 2025 survive their first year {y25-y23:.0f} points better than 2023's",
        subtitle="Kaplan-Meier by year of arrival. Only listings whose arrival was observed; "
                 "2026 is excluded because its window is shorter than a year.")
    f, y = plate.frame(W, 88,
        who="Anyone judging whether this marketplace is stabilising or churning harder",
        decide="Whether a listing's VINTAGE, not just its age, predicts that it will last",
        wrong="The three curves overlap — then arrival year carries nothing")
    s += f

    x0, x1 = 84, W - 150
    top, bot = y + 34, H - 120
    XMAX = 730
    def px(t): return x0 + (x1 - x0) * min(t, XMAX) / XMAX
    def py(v): return bot - (bot - top) * v
    for v in (0, .25, .5, .75, 1.0):
        gy = py(v)
        s.append(f'<line x1="{x0}" y1="{gy:.1f}" x2="{x1}" y2="{gy:.1f}" stroke="{GRID}"/>')
        s.append(plate.txt(x0 - 9, gy + 3.5, f"{int(v*100)}", size=10.5, fill=MUTED, anchor="end"))
    for t in (0, 365, 730):
        gx = px(t)
        s.append(f'<line x1="{gx:.1f}" y1="{top}" x2="{gx:.1f}" y2="{bot}" stroke="{GRID}"/>')
        s.append(plate.txt(gx, bot + 17, f"{t:,}", size=10.5, fill=MUTED, anchor="middle"))
    s.append(plate.txt(x0 - 9, top - 14, "% still listed", size=10, fill=MUTED, anchor="end"))
    s.append(plate.txt((x0 + x1) / 2, bot + 36, "days since first seen", size=10.5, fill=MUTED, anchor="middle"))

    for yr in ("2023", "2024", "2025"):
        km = coh[yr]["km"]
        # STOP EACH CURVE AT ITS OWN LAST OBSERVATION, not at XMAX. A 2025
        # listing cannot have been watched for 730 days, so extending its line
        # to the right edge draws a flat tail that reads as "no more deaths"
        # when it means "no more observation" -- the line would be asserting
        # survival past the data that supports it.
        horizon = km[-1][0] if km else 0
        end = min(XMAX, horizon)
        pts = []; pv = 1.0
        for t, v in km:
            if t > end: break
            pts += [f"{px(t):.1f},{py(pv):.1f}", f"{px(t):.1f},{py(v):.1f}"]; pv = v
        pts.append(f"{px(end):.1f},{py(pv):.1f}")
        s.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{COL[yr]}" stroke-width="2.4"/>')
        if end < XMAX:
            s.append(f'<circle cx="{px(end):.1f}" cy="{py(pv):.1f}" r="3.6" fill="{plate.SURFACE}" '
                     f'stroke="{COL[yr]}" stroke-width="2"/>')
            s += plate.halo(px(end) + 8, py(pv) + 4, "follow-up ends", size=9.5, fill=COL[yr])

    lx = x1 + 22
    s.append(plate.txt(lx, top + 2, "ARRIVED IN", size=9, fill=MUTED, weight="700", spacing="0.9"))
    for i, yr in enumerate(("2023", "2024", "2025")):
        yy = top + 24 + i * 52
        s.append(f'<rect x="{lx}" y="{yy-9:.1f}" width="11" height="11" rx="2" fill="{COL[yr]}"/>')
        s += plate.halo(lx + 17, yy, yr, size=13, fill=INK)
        s.append(plate.txt(lx, yy + 16, f"{100*at(coh[yr]['km'],365):.1f}% at 1 year", size=10.5, fill=INK2))
        s.append(plate.txt(lx, yy + 29, f"n = {coh[yr]['n']:,}", size=10, fill=MUTED))

    s.append(f'<line x1="28" y1="{H-76:.1f}" x2="{W-28}" y2="{H-76:.1f}" stroke="{RULE}"/>')
    s += plate.wrap(28, H - 60,
        "Snowflake Marketplace sitemap, 41 snapshots via the Internet Archive plus one live capture. "
        "THE TREND RUNS AGAINST ITS OWN BIAS: 2023 is the sparsest year sampled (38-day median gaps "
        "against 29 in 2025), and sparse sampling MISSES short-lived listings entirely, which inflates "
        "that year's survival. The real gap is therefore wider than drawn, not narrower.",
        size=10, fill=MUTED, chars=132, leading=13)
    s.append("</svg>")
    out = here.parent / "charts" / "cohorts.svg"
    out.write_text("\n".join(s), encoding="utf-8")
    print(f"  wrote {out.name}  (2023 {y23:.1f}% -> 2025 {y25:.1f}% at 1yr)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
