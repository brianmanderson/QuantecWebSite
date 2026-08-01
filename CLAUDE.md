# CLAUDE.md

Guidance for Claude Code when working in this repository.

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

- `index.html`, `about.html`, `resources.html`, `publications.html`, `contact.html`
  → `_layouts/default.html` (head, nav, footer) → `assets/css/style.css` (all styles).
- `_config.yml` — site config. Its `exclude:` list is load-bearing: anything not listed there
  is published to the live site.
- `CREDITS.md` — icon/asset attribution. Any new local asset needs a row here.
- `CNAME` — the custom domain, registered through Namecheap.
- `docs/` — notes converted from the original Word briefs; excluded from the build.

## Workflow rules

- **Every change goes through a PR branch. Never commit or push directly to `main`.** There is
  no `dev` branch in this repo, so `main` is the release branch: merging to it publishes to
  quantecradiation.org immediately via GitHub Pages. No CI, no staging, no test suite.
- **A change is not done until the `release` gate passes** — clean build, link checker,
  `_site/` inspection, and a rendered look at desktop and mobile widths. Don't ease it.

## The skills are the operational manual

Three tracked skills in `.claude/skills/`; their descriptions say when to load them.

- `preview` — read BEFORE the first `bundle`/`jekyll` command of a session. Ruby setup on this
  machine is non-obvious (winget's package needs a follow-up `ridk install 1`), and every page
  builds to a directory, not an `.html` file.
- `content-editing` — read BEFORE touching any page, the layout, or the stylesheet. Holds the
  content-accuracy rule, the CSS component vocabulary, and the CREDITS.md requirement.
- `release` — the gate above. Run it before any PR.

## Pitfalls

- The global `permalink: /:title/` in `_config.yml` applies to pages, so `about.html` is served
  at `/about/`. Nav links are correctly extensionless; adding `.html` breaks them. Changing that
  permalink rewrites every URL on a live public site.
- `_config.yml` changes are not picked up by `jekyll serve --watch`; restart the server or you
  are reading a stale build.
- Don't search or edit inside `_site/` — it is generated output and gitignored.

## Further reading

- [README.md](README.md) — what the site is, and verified local build steps.
- [docs/site-plan.md](docs/site-plan.md) — the original design brief: the QUANTEC citations the
  site was built from, plus sections (QUANTEC 2, author interviews) not yet built.
- [docs/update-requests.md](docs/update-requests.md) — an unimplemented content backlog.
