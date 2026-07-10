# QuantecWebSite

Source for [quantecradiation.org](http://quantecradiation.org/) — a Jekyll static site providing evidence-based radiation dose/constraint resources for radiation oncology professionals, building on the original QUANTEC (Quantitative Analyses of Normal Tissue Effects in the Clinic) initiative.

## How it's built

- Plain Jekyll site: pages (`index.html`, `about.html`, `publications.html`, `resources.html`, `contact.html`) rendered through `_layouts/default.html`, styled by `assets/css/style.css`.
- Focus areas presented on the site: cardiac toxicity, pulmonary effects, CNS tolerance, optic structures, pediatric guidelines, and NTCP modeling.
- `CNAME` points GitHub Pages at the custom domain; the domain is registered through [Namecheap](https://ap.www.namecheap.com/dashboard).
- Asset/icon credits are in `CREDITS.md`.

## Run locally

Requires Ruby with Bundler (plugins: jekyll-feed, jekyll-sitemap, jekyll-seo-tag).

```
bundle install
bundle exec jekyll serve
```

## Contact

BrianAnderson@ucsd.edu
