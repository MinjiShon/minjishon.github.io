# Personal website — Minji Shon

Static site (plain HTML + CSS, no build step, no dependencies).
All content is drawn from `../overleaf_cv/main.tex` and `../CV_update.md`.

```
personal_website/
├── index.html          Home: about, research, experience, education, skills, awards, contact
├── publications.html   Publications grouped by topic, with DOI links
├── cv.html             Embedded PDF viewer + download
├── .nojekyll           Tells GitHub Pages to serve files as-is
└── assets/
    ├── style.css       All styling (light + dark mode)
    ├── Minji_Shon_CV.pdf
    └── logos/          gatech, samsung, intel, sogang, uconn
```

## Preview locally

```bash
cd personal_website
python3 -m http.server 8000
```

Then open <http://localhost:8000>. (Opening `index.html` directly by
double-clicking also works, but the embedded PDF on `cv.html` behaves better
over a local server.)

## Deploy to GitHub Pages

1. Create a GitHub repo named **`<your-username>.github.io`**
   (e.g. `minjishon.github.io`). Public.

2. From this folder:

   ```bash
   cd personal_website
   git init
   git add .
   git commit -m "Initial personal website"
   git branch -M main
   git remote add origin https://github.com/<your-username>/<your-username>.github.io.git
   git push -u origin main
   ```

3. On GitHub: **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)` → Save.**

4. Wait ~1 minute. The site is live at `https://<your-username>.github.io`.

To update later: edit files, then `git add . && git commit -m "update" && git push`.

### Custom domain (optional, later)

Buy a domain, add a file named `CNAME` in this folder containing just the domain
(e.g. `minjishon.com`), point the domain's DNS at GitHub Pages, then set it under
**Settings → Pages → Custom domain**.

## Updating content

| To change | Edit |
|---|---|
| Bio, experience, skills, awards | `index.html` |
| Publications | `publications.html` — copy an existing `<div class="pub">` block |
| CV PDF | Replace `assets/Minji_Shon_CV.pdf` (keep the filename) |
| Colors, fonts, spacing | `assets/style.css` — the `:root` block at the top |

### Adding a publication

Copy this block into the right `.pub-group` in `publications.html`:

```html
<div class="pub" id="L5">
  <div class="pub-id">[L5]</div>
  <div>
    <div class="pub-title">Paper title here</div>
    <div class="pub-authors"><span class="me">Shon, M.</span>, et al., Yu, S.</div>
    <div class="pub-venue"><span class="venue-name">IEDM</span>, 2027</div>
    <div class="pub-links">
      <a href="https://doi.org/..." target="_blank" rel="noopener">DOI</a>
    </div>
  </div>
</div>
```

`<span class="me">` bolds your name. Add
`<span class="badge badge-prep">In preparation</span>` inside `.pub-venue` for
unpublished work.

## Notes

- **Phone number is intentionally not on the site** (it stays in the PDF CV only).
- **Unpublished work is intentionally not listed.** The JXCDC PDK paper and the
  IEDM'26 electro-thermal paper are described in the Research section on the home
  page instead. Add them to `publications.html` once submitted/accepted.
- **Photo:** the hero uses `assets/Minji_Shon.jpg` (495×495 square). To swap it,
  replace that file or change the `src` in `index.html`. Use a square image —
  non-square ones get center-cropped. If the file is missing, the block removes
  itself and the layout closes up cleanly.
- **Anything inside this folder becomes public once deployed**, whether or not a
  page links to it. Keep unused personal images (ID/visa photos, scans) out of
  `assets/` rather than merely unlinking them.
- The `og:url` / `canonical` tags in each file assume
  `https://minjishon.github.io`. Update them if you use a different URL.
- Dark mode follows the visitor's system setting automatically.
