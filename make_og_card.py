#!/usr/bin/env python3
"""Regenerate assets/og-card.png (the 1200x630 social-share card).

No generator existed, so this reproduces the original card's geometry, which was
measured off the Aug 2026 PNG: 85px margins, logos scaled by height and centred
on y=519.5, navy gradient from the CV's accent colour to a darker corner.

Run from the site root:  python3 assets/make_og_card.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
TL, BR = (31, 59, 102), (18, 34, 60)          # accent navy -> dark corner
WHITE, RULE = (255, 255, 255), (120, 170, 230)
SUBTITLE_C, DESC_C = (198, 216, 240), (150, 180, 220)
MARGIN = 85

SERIF_B = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
SERIF   = "/System/Library/Fonts/Supplemental/Georgia.ttf"
SANS    = "/System/Library/Fonts/Supplemental/Arial.ttf"

NAME      = "Minji Shon"
SUBTITLE  = ["Ph.D. Candidate · Electrical & Computer Engineering",
             "Georgia Institute of Technology"]
DESC      = ["Reliability- and thermal-aware DTCO/STCO for advanced 3D logic and memory",
             "Reliability intern at Intel \u00b7 7 years of Samsung Design-for-Reliability"]
URL       = "minjishon.github.io"
LOGOS     = [("assets/logos/gatech.png", 72),
             ("assets/logos/intel.png", 54),
             ("assets/logos/samsung.png", 40)]
LOGO_GAP, LOGO_CY = 46, 520


def fit(path, text, target_w, lo=8, hi=200):
    """Largest size whose rendered width stays within target_w."""
    best = lo
    while lo <= hi:
        mid = (lo + hi) // 2
        f = ImageFont.truetype(path, mid)
        if f.getbbox(text)[2] - f.getbbox(text)[0] <= target_w:
            best, lo = mid, mid + 1
        else:
            hi = mid - 1
    return best


def gradient():
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        for x in range(W):
            t = (x / W + y / H) / 2
            px[x, y] = tuple(round(TL[i] + (BR[i] - TL[i]) * t) for i in range(3))
    return img


def white_logo(path, height):
    im = Image.open(path).convert("RGBA")
    w = round(im.width * height / im.height)
    im = im.resize((w, height), Image.LANCZOS)
    solid = Image.new("RGBA", im.size, WHITE + (0,))
    solid.putalpha(im.getchannel("A"))
    return solid


def main():
    img = gradient()
    d = ImageDraw.Draw(img)

    # sizes calibrated against the original card's measured text widths
    f_name = ImageFont.truetype(SERIF_B, fit(SERIF_B, NAME, 497))
    f_sub  = ImageFont.truetype(SERIF,   fit(SERIF, SUBTITLE[1], 432))
    f_desc = ImageFont.truetype(SANS,    min(fit(SANS, ln, 900) for ln in DESC))
    f_url  = ImageFont.truetype(SANS,    fit(SANS, URL, 189))

    d.text((MARGIN, 105), NAME, font=f_name, fill=WHITE, anchor="la")
    d.rectangle([84, 213, 180, 216], fill=RULE)
    for i, line in enumerate(SUBTITLE):
        d.text((MARGIN, 250 + i * 44), line, font=f_sub, fill=SUBTITLE_C, anchor="la")
    for i, line in enumerate(DESC):
        d.text((MARGIN, 361 + i * 38), line, font=f_desc, fill=DESC_C, anchor="la")

    x = MARGIN
    for path, h in LOGOS:
        logo = white_logo(path, h)
        img.paste(logo, (x, LOGO_CY - h // 2), logo)
        x += logo.width + LOGO_GAP

    d.text((W - MARGIN, LOGO_CY), URL, font=f_url, fill=DESC_C, anchor="rm")
    img.save("assets/og-card.png")
    print(f"wrote assets/og-card.png  name={f_name.size} sub={f_sub.size} "
          f"desc={f_desc.size} url={f_url.size}")


if __name__ == "__main__":
    main()
