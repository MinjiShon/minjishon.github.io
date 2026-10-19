# Drop new figures here

Put source files in this folder and tell me which slot each one goes in.
I convert, resize, rename, wire up the HTML, and delete the originals from
here so they never ship with the site.

Preferred format: PDF (vector, from the papers) > PNG (high res) > SVG.
Not JPEG.

## Slots on the page

| Slot | Where it shows | Shape that works best |
|---|---|---|
| `hero` | About, wide figure under the first paragraph | wide, about 2:1 |
| `strip-1,2,3` | About, the three small renders | all three the same shape |
| `card-1` | Research card: CFET DTCO & Open PDK | 16:9 |
| `card-2` | Research card: Electro-Thermal Co-Design | 16:9 |
| `card-3` | Research card: Ferroelectric Devices | 16:9 |
| `card-4` | Research card: 3D Compute-in-Memory | 16:9 |
| `flow` | Research, wide figure at the end | wide, about 16:9 |
| `pub-L1 ... pub-T1` | Publication thumbnails | 4:3 |

Figures are scaled to fit, so an odd aspect ratio is not fatal; it just
leaves empty space on the sides.

## Naming

Anything is fine. `card2_selfheating.pdf` or just `thermal.png`. Tell me the
slot and I will handle the rest.
