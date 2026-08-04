# CLAUDE.md

## What this is

[quantecradiation.org](https://quantecradiation.org) — a Jekyll static site publishing
evidence-based radiation dose/constraint resources for radiation oncology, building on the
original QUANTEC (Quantitative Analyses of Normal Tissue Effects in the Clinic) reviews.

**The audience is practising clinicians** using this material for treatment planning. Dose
constraints, NTCP parameters, paper titles, author lists and citation URLs must come from the
user or from a source already cited in this repo. **Never generate, infer, or "correct" a
clinical number or a citation from your own knowledge** — a plausible-looking wrong value here
is a patient-safety problem. See the `content-editing` skill.

## Layout

Flat repo, no collections, no `_posts`. Pages are HTML with YAML front matter:

- `index.html`, `about.html`, `quantec.html`, `publications.html`, `quantec-2.html`,
  `contact.html` → `_layouts/default.html` (head, nav, footer) → `assets/css/style.css`.
  `resources.html` is a redirect stub for the pre-rename URL, not a page.
- `_config.yml` — site config. Its `exclude:` list is load-bearing: anything not listed there
  is published to the live site.
- `CREDITS.md` — attribution; any new local asset needs a row. `CNAME` — the custom domain.
- `docs/` — notes converted from the original Word briefs; excluded from the build.

The site originally stated no dose values at all: each organ topic routed to the review carrying
the constraint, deliberately, so clinicians planned from the paper rather than our summary of it.

**The owner reversed that on 2026-08-03.** All 18 organ entries of Table 1 of the QUANTEC summary
paper — 62 dose rows — are now transcribed into `/quantec/#data`. They carry that table's four
governing footnotes verbatim, and every table cites the page its rows came from and links its
organ review. The organ cards above the tables still route to the papers; the tables are an
addition to that routing, not a replacement for it. The transcription record and verification
evidence are in
[docs/constraints-pilot-lung-heart-cord.md](docs/constraints-pilot-lung-heart-cord.md) — read it
before changing, extending or "correcting" any value in those tables.

## Workflow rules

- **Every change goes through a PR branch. Never commit or push directly to `main`.** There is
  no `dev` branch in this repo, so `main` is the release branch: merging to it publishes to
  quantecradiation.org immediately via GitHub Pages. No CI, no staging, no test suite.
- **A change is not done until the `release` gate passes** — clean build, link checker,
  `_site/` inspection, and a rendered look at desktop and mobile widths. Don't ease it.

## The skills are the operational manual

Three tracked skills in `.claude/skills/`; their descriptions say when to load them.

- `preview` — read BEFORE the first `bundle`/`jekyll` command of a session. Ruby setup here is
  non-obvious (winget's package needs a follow-up `ridk install 1`).
- `content-editing` — read BEFORE touching any page, the layout, or the stylesheet. Holds the
  content-accuracy rule, the CSS component vocabulary, and the CREDITS.md requirement.
- `release` — the gate above. Run it before any PR.

Plus one tracked agent, `site-reviewer` — an independent read of the built site. Spawn it with a
fresh context and tell it nothing about what you changed; that independence is the point.

## Pitfalls

- The global `permalink: /:title/` applies to pages, so `about.html` serves at `/about/`. Nav
  links are correctly extensionless; adding `.html` breaks them, and changing that permalink
  rewrites every URL on a live public site.
- `_config.yml` changes are not picked up by `jekyll serve --watch` — restart, or you are
  reading a stale build. Don't search or edit inside generated `_site/`.

## Further reading

- [README.md](README.md) — what the site is, and verified local build steps.
- [docs/site-plan.md](docs/site-plan.md) — the original brief: the QUANTEC citations the site
  was built from, plus the Marks/Bentzen interview questions, still unbuilt.
- [docs/update-requests.md](docs/update-requests.md) — the content backlog, implemented
  2026-08-01. Its "Rulings" section records six decisions the owner made on 2026-08-02 —
  read it before "fixing" anything it covers; those are decisions, not defects.
