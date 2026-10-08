# Figures used on the v2 site

Every image here came from **your own** work: the paper source folders under
`Research/Paper_Writing/` and the thesis proposal under `Research/PhD_Thesis/`.
Nothing was downloaded or generated.

| File on the site | Where it appears | Copied from (relative to `Research/`) |
|---|---|---|
| `hero-scaling.jpg` | About, wide figure under the first paragraph | `PhD_Thesis/Proposal/paper/figures/fig1.2.png` |
| `cfet-devices.jpg` | About, "Device" in the three-up strip | `Paper_Writing/2026_IEDM/Figures/cfet_devices.png` |
| `bspdn-package.jpg` | About, "Package" in the three-up strip | `Paper_Writing/2026_IEDM/Figures/bspdn_package (2).png` |
| `system-stack.jpg` | About, "System" in the three-up strip | `Paper_Writing/2026_IEDM/Figures/system_stack (3).png` |
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
im.thumbnail((860, 10000), Image.LANCZOS)   # 1200 for the two wide figures
im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
EOF
```

Widths used: **1200** for `hero-scaling`, **980** for `dtco-flow`, **860** for the
research-card figures, **760** for the three small renders.

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
