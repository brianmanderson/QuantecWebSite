# QuantecWebSite

Source for [quantecradiation.org](http://quantecradiation.org/) — a Jekyll static site providing evidence-based radiation dose/constraint resources for radiation oncology professionals, building on the original QUANTEC (Quantitative Analyses of Normal Tissue Effects in the Clinic) initiative.

## How it's built

- Plain Jekyll site: pages (`index.html`, `about.html`, `quantec.html`, `publications.html`, `quantec-2.html`, `contact.html`) rendered through `_layouts/default.html`, styled by `assets/css/style.css`. `resources.html` is a redirect stub preserving the pre-rename `/resources/` URL.
- Focus areas presented on the site: CNS tolerance, head and neck, cardiac toxicity, pulmonary effects, GI/GU toxicity, optic structures, pediatric guidelines, and NTCP modeling.
- Most organ topics do not restate dose values: they route to the peer-reviewed review that carries the constraint, so what a clinician plans from is the source rather than a summary. The exception, ruled by the site owner on 2026-08-03, is spinal cord, lung and heart — `/quantec/#data` states those values directly, transcribed from Table 1 of the QUANTEC summary paper with its governing footnotes verbatim and every row attributed to its source page. See `docs/constraints-pilot-lung-heart-cord.md`.
- `CNAME` points GitHub Pages at the custom domain; the domain is registered through [Namecheap](https://ap.www.namecheap.com/dashboard).
- Asset/icon credits are in `CREDITS.md`.

## Run locally

Requires **Ruby 3.3** (what GitHub Pages builds with; 3.4+ drops stdlib gems this Gemfile does
not declare) and Bundler. Plugins: jekyll-feed, jekyll-sitemap, jekyll-seo-tag.

On Windows, install Ruby and then finish the toolchain — the winget package alone leaves MSYS2
unpacked, and gems with native extensions fail with `MSYS2 could not be found`:

```powershell
winget install --id RubyInstallerTeam.RubyWithDevKit.3.3 --exact --silent
ridk install 1
```

Ruby lands in `C:\Ruby33-x64\bin`; open a new shell so it is on `PATH`. Then, from the repo root:

```bash
bundle install
bundle exec jekyll serve
```

Open <http://127.0.0.1:4000/>. `bundle exec jekyll build` writes to `_site/` without serving.

Note that `jekyll serve --watch` does not reload `_config.yml` — restart the server after
editing it.

## Contributing

`main` is the release branch: merging to it publishes the live site via GitHub Pages. Work on a
branch and open a pull request; there is no CI, so build the site and check the affected pages
in a browser at desktop and mobile widths before asking for a review.

Working notes and the original design brief live in [`docs/`](docs/), which is excluded from the
Jekyll build.

## Contact

BrianAnderson@ucsd.edu
