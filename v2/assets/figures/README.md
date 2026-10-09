# Figures used on the v2 site

Images you supplied yourself are marked as such below. The rest were taken
from your paper source folders under `Research/Paper_Writing/` and the thesis
proposal under `Research/PhD_Thesis/`, and are placeholders until you replace
them. Nothing was downloaded or generated.

| File on the site | Where it appears | Copied from (relative to `Research/`) |
|---|---|---|
| `hero-scaling.jpg` | About, wide figure under the first paragraph | supplied by Minji as `scaling.pdf` (credited 2026 VLSI Short Course, IBM) |
| `stack-integration.jpg` | About, wide figure replacing the old three-up strip | supplied by Minji as `fig1.png` |
| `pdk-gds.jpg` | Research card 1, and publication [L1] | `Paper_Writing/2026_JXCDC/jxcdc-paper/figures/gds.png` |
| `thermal-delay.jpg` | Research card 2, and publication [R1] | `Paper_Writing/2026_IEDM/Figures/F1_thermal_delay.png` |
| `fe-nand.jpg` | Research card 3 | `PhD_Thesis/Proposal/paper/figures/fig2.12.png` |
| `memory-pyramid.jpg` | Research card 4 | `PhD_Thesis/Proposal/paper/figures/fig1.4.png` |
| `dtco-flow.jpg` | Research, wide figure at the end of the section | `Paper_Writing/2026_IEDM/Figures/fig-framework.png` |

Note that `Paper_Writing/2026_IEDM/` is the DeepSim electro-thermal paper now
retargeted to IRPS'27, so those figures belong to [R1].

## Replacing one

Keep the filename and the page picks up the new image with no HTML edit:

```bash
cd CV/personal_website/v2/assets/figures
python3 - <<'EOF'
from PIL import Image
src = "/full/path/to/your/new_figure.png"
dst = "pdk-gds.jpg"            # the name you are replacing
im = Image.open(src).convert("RGB")
im.thumbnail((860, 10000), Image.LANCZOS)   # 1600 for the two wide figures
im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
EOF
```

Widths used: **1600** for the two wide figures (`hero-scaling`,
`stack-integration`), **980** for `dtco-flow`, **860** for the research-card
figures.

If you change what a figure *shows*, update its `alt` text and caption in
`v2/index.html` too — the alt text describes the current image.

## Adding thumbnails to the other publications

`v2/publications.html` gives [L1] and [R1] real thumbnails. The other ten entries
use a navy monogram tile, because the right figure for each was not certain.
To add one, drop the file in here and swap the tile:

```html
<!-- from -->
<div class="pub-thumb empty" aria-hidden="true">L2</div>
<!-- to -->
<div class="pub-thumb">
  <img src="assets/figures/l2-dtco.jpg" width="860" height="500" loading="lazy"
       alt="describe what the figure shows">
</div>
```
