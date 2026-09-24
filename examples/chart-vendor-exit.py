#!/usr/bin/env python3
"""Do vendors lose one product, or all of them?"""
import json, pathlib, sys
import plate
from plate import INK, INK2, MUTED, RULE, GRID, FAINT

W = 880
GONE, PART, KEPT = "#b4472e", "#c08a3e", "#2f6f5e"
COLS, R, PITCH = 38, 4.6, 16.0


def main():
    here = pathlib.Path(__file__).resolve()
    src = sys.argv[1] if len(sys.argv) > 1 else str(sorted((here.parents[1] / "public").glob("survival-*.json"))[-1])
    d = json.load(open(src)); ex = d["vendor_exit"]; base = d["vendor_exit_base"]
    order = [("all", ex["all"], GONE), ("some", ex["some"], PART), ("none", ex["none"], KEPT)]
    rows = -(-base // COLS); H = 330 + rows * PITCH

    s = plate.open_svg(W, H,
        f"{100*ex['all']/base:.0f}% of multi-product vendors have left the marketplace entirely",
        subtitle=f"One mark per vendor with 3 or more listings ever seen, n={base:,}, "
                 f"coloured by how much of its catalogue is still on sale.")
    f, y = plate.frame(W, 88,
        who="Anyone depending on a vendor's catalogue rather than one listing",
        decide="Whether to treat a vendor's presence as more stable than a product's",
        wrong="Almost no vendor loses everything — exits are per-product, not per-vendor")
    s += f

    x0, top = 78, y + 34
    i = 0
    for _, n, col in order:
        for _ in range(n):
            cx = x0 + (i % COLS) * PITCH; cy = top + (i // COLS) * PITCH
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{R}" fill="{col}" fill-opacity="0.9"/>')
            i += 1
    lx = x0 + COLS * PITCH + 30
    for j, (lab, n, col) in enumerate(order):
        yy = top + 8 + j * 62
        s.append(f'<rect x="{lx}" y="{yy-10:.1f}" width="12" height="12" rx="2" fill="{col}"/>')
        s += plate.halo(lx + 19, yy, f"{n:,}", size=16, fill=INK)
        s.append(plate.txt(lx + 19 + 12 * len(f"{n:,}"), yy, f"  {100*n/base:.0f}%", size=11, fill=MUTED))
        txt = {"all": "lost EVERY listing", "some": "lost some, kept some",
               "none": "lost nothing"}[lab]
        s.append(plate.txt(lx, yy + 17, txt, size=10.5, fill=INK2))

    bot = top + rows * PITCH
    s += plate.wrap(x0, bot + 30,
        f"A vendor is inferred from the slug's leading token, which is NOT a published field — "
        f"Snowflake exposes no vendor anywhere reachable. It groups {base:,} multi-listing vendors "
        f"out of 1,356 distinct tokens, so it is a usable proxy and not a census.",
        size=10.5, fill=MUTED, chars=104, leading=13)

    s.append(f'<line x1="28" y1="{H-62:.1f}" x2="{W-28}" y2="{H-62:.1f}" stroke="{RULE}"/>')
    s += plate.wrap(28, H - 46,
        "Snowflake Marketplace sitemap, 41 snapshots 2023-03-07 to 2026-09-24. Vendor SIZE does not "
        "predict survival: listings from one-product and ten-plus-product vendors reach two years at "
        "62.5% and 61.0% respectively, flat across every band. Whether a vendor leaves matters; how "
        "big it is does not.",
        size=10, fill=MUTED, chars=132, leading=13)
    s.append("</svg>")
    out = here.parent / "charts" / "vendor-exit.svg"
    out.write_text("\n".join(s), encoding="utf-8")
    print(f"  wrote {out.name}  ({ex['all']}/{base} lost everything)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
