# Personal website — Minji Shon

Static site (plain HTML + CSS, no build step, no dependencies).
All content is drawn from `../overleaf_cv/main.tex` and `../CV_update.md`.

**Two versions live in this repo.** The richer v2 build was promoted to the root
URL on 2026-10-18 so that the link printed on every CV variant
(`minjishon.github.io`) now serves it. The original is kept as a backup.

| Version | URL | Role |
|---|---|---|
| **v2** (now at the root) | <https://minjishon.github.io> | **Live site.** What recruiters see. |
| **v1** | <https://minjishon.github.io/v1/> | Backup of the original build. `noindex`, so it does not compete in search. |
| `/v2/` | redirects to the root | Stubs kept so any previously shared `/v2/` link still works. |

```
personal_website/
├── index.html          LIVE (v2) Home: about, research, experience, education, skills, awards, contact
├── publications.html   LIVE (v2) Publications grouped by topic, with DOI links
├── cv.html             LIVE (v2) Embedded PDF viewer + download
├── .nojekyll           Tells GitHub Pages to serve files as-is
├── make_og_card.py     Regenerates assets/og-card.png
├── assets/             LIVE (v2) assets
│   ├── style.css       All styling (light + dark mode)
│   ├── Minji_Shon_CV.pdf
│   ├── og-card.png     Social-preview card (referenced by all three pages)
│   ├── figures/        Research and publication figures (v2 only)
│   ├── talks/          Placeholder for talk slides
│   └── logos/          gatech, samsung, intel, sogang, uconn
├── v1/                 BACKUP of the original site, with its own assets/
└── v2/                 Redirect stubs pointing at the root
```

**When editing, edit the root files.** `v1/` is a frozen backup; changes there are
invisible to anyone. A change meant to be seen goes in `index.html`,
`publications.html` or `cv.html` at the top level.

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
- **Publication status.** The MATRIX-A5 PDK paper is **accepted at JxCDC'26**
  (2026-10-17) and is listed on `publications.html` with an *Accepted* badge in
  both the live site and the v1 backup. The electro-thermal paper was rejected
  from IEDM'26 and **retargeted to IRPS'27** (submission Oct 2026); it stays
  described in the Research section and off `publications.html` until it is
  accepted. Do not quote its MAE or runtime numbers anywhere — they are still
  placeholders.
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
