---
name: content-editing
description: >
  Conventions for adding or changing clinical content on quantecradiation.org — which file each
  content type lives in, how the nav is wired, the CSS component vocabulary, the CREDITS.md rule
  for new icons and images, and the hard rule that dose constraints, citations, author lists and
  URLs must come from the user or a cited source and are never generated. Load this BEFORE
  editing any `.html` page, `_layouts/default.html`, or `assets/css/style.css`, and before adding
  a page, nav entry, card, or icon. Skipping it is how invented dose numbers or fabricated
  citations reach practising clinicians.
---

# Editing site content

## The content-accuracy rule — read this first

This site is read by radiation oncologists, medical physicists and dosimetrists making treatment
planning decisions. A plausible-looking wrong number here is a patient-safety problem, not a typo.

**Never generate, infer, complete, or "correct" any of the following from your own knowledge:**

- dose constraints, dose/volume thresholds, DVH cut-offs, V20/V30/mean-dose figures
- NTCP model parameters
- paper titles, author lists, journal/volume/page references, DOIs, article URLs
- claims about what a QUANTEC/HyTEC/PENTEC paper concluded

Every one of these must be **supplied by the user** or **copied from a source already cited in
this repo** — `docs/site-plan.md` and `docs/update-requests.md` hold the transcribed source
material the site was built from. If a value is needed and no source has it, stop and ask. Write
the section with a placeholder rather than a guess.

Two known traps already recorded in `docs/site-plan.md`: the source brief gives the *same* Red
Journal URL for "Pelvis: Rectum" and "Pelvis: Penile Bulb" (a copy/paste error — do not invent a
replacement), and `docs/update-requests.md` maps requested edits to the constraints panels by
*inferred* order. That mapping has been implemented but never confirmed — see the
"Implementation status" section of that file for it and the other open deviations.

Qualitative framing prose ("Evidence-based guidelines for lung dose limits and pneumonitis risk
assessment") is a different matter — that is site copy and can be edited freely, as long as it
does not assert a number or a finding.

## Where content lives

Flat repo, no `_posts`, no collections. One file per page:

| File | Page | What belongs here |
|---|---|---|
| `index.html` | `/` | Hero, mission, the "Key Resources & Areas of Focus" card grid, audience list, CTA |
| `about.html` | `/about/` | Project history and objectives |
| `quantec.html` | `/quantec/` | Organ-specific constraint panels, NTCP section |
| `publications.html` | `/publications/` | QUANTEC bibliography plus HyTEC and PENTEC — by far the largest page |
| `quantec-2.html` | `/quantec-2/` | QUANTEC 2 objectives and planned sites/toxicities |
| `contact.html` | `/contact/` | Corrections address, collaboration invitation |
| `resources.html` | `/resources/` | **Redirect stub only.** Do not put content here |
| `_layouts/default.html` | all | `<head>`, `{% seo %}`, header + nav, footer, the smooth-scroll script |
| `assets/css/style.css` | all | Every style rule; there is no per-page CSS |

`resources.html` was the constraints page until it moved to `/quantec/`. It is now a
`layout: null` stub that carries the URL fragment across so the live `/resources/#cns` deep link
still works. Anything written into it renders nowhere.

Each page is HTML with YAML front matter (`layout: default`, `title:`, `description:`). Both feed
`{% seo %}` in the layout, which builds the title, meta description, canonical URL, Open Graph
and JSON-LD — set both on any new page. **`title` must not repeat the site name**; `{% seo %}`
appends `| QUANTEC Radiation` itself, so "Publications" is right and "Publications - QUANTEC
Radiation" produces a doubled title. Liquid is otherwise used only for `relative_url` /
`absolute_url` filters and `site.*` values.

## Adding a page

1. Create `newpage.html` at the repo root with front matter (`layout: default`, `title`,
   `description`). The global `permalink: /:title/` makes it `/newpage/` — see the `preview`
   skill.
2. Add an `<li><a href="{{ '/newpage' | relative_url }}">…</a></li>` to the `<ul>` in
   `_layouts/default.html`. That `<ul>` is the *only* nav definition; there is no data file.
3. Always route links through `relative_url` (`{{ '/quantec/' | relative_url }}`), never a
   bare `/quantec/` or an absolute `https://quantecradiation.org/...`.
4. **The nav is full.** Six items measure 554px against a 594px budget at 1280px — 41px of
   slack. A seventh item, or renaming one to something longer, wraps the header to two rows.
   Measure before and after in the browser (see `preview`); do not eyeball it. The gap and link
   padding in `style.css` are already tightened for this and should not be widened.
5. Sub-navigation within a page uses `.subnav` — real `#anchor` links, no JS tab widget. The
   layout's smooth-scroll handler pushes the hash and moves focus, so those sections stay
   linkable, bookmarkable and reachable with the Back button. Keep that property if you touch
   the handler.
6. Renaming a page changes a live public URL. Leave a redirect stub at the old permalink that
   preserves the fragment — `resources.html` is the worked example.

## CSS component vocabulary

`assets/css/style.css` is a single hand-written stylesheet, roughly: reset → header → nav → hero
→ content sections → gallery → buttons → footer → responsive → utilities → publications-specific
block → print styles. Reuse the existing classes instead of adding new ones:

- `.hero` — the intro band at the top of every page (`<h2>` + `<p>`).
- `.content-section` — a standard body section, opened with an `<h3>` carrying a Font Awesome
  icon.
- `.image-gallery` > `.gallery-container` > `.gallery-item` — the responsive card grid used for
  the home page focus areas, the constraints organ panels and the QUANTEC 2 site groups. Wrap a
  card in `<a class="gallery-link">` to make the whole card clickable; give a card an `id` to
  make it a deep-link target (`/quantec/#cns` is highlighted by the `:target` rule).
  Every home-page card is a link — a card styled clickable that does nothing is a defect this
  site has shipped before.
- `.subnav` — in-page section tabs (Publications, QUANTEC 2). Pill-shaped anchor links.
- `.panel-link` — the "→ papers" route out of a card. `.panel-note` — a small grey note in a
  card, used where per-bullet links go to different destinations.
- `.organ-icon` — an anatomy SVG rendered via CSS `mask` so it inherits `currentColor`; set the
  file with an inline `--organ-icon` custom property.
- `.btn` / `.btn-secondary` — call-to-action links.
- Publications-only: `.container`, `.content-block`, `.highlight-box`, `.publication-list`,
  `.publication-item`, `.authors`, `.external-link`, `.organ-category`, `.category-title`,
  `.summary-links`.

External links carry `target="_blank" rel="noopener"`. Where the visible link text repeats
across many entries — the publications list is all "Read Full Text" — the link needs an
`aria-label` naming the specific paper, or a screen-reader user gets an undifferentiated list.

There are two mobile breakpoints (a general one and a publications-specific one). If you add a
component, add its responsive rule in the same pass — the grid does not collapse on its own.

Avoid inline `style="..."`. Several older ones remain (`index.html`'s list indent,
`quantec.html`'s NTCP section); prefer moving those into the stylesheet over adding more.

## Icons and images must be credited

Two icon systems are in play:

- **Font Awesome Free**, loaded from a CDN in `_layouts/default.html`, used as
  `<i class="fas fa-brain"></i>`. Covered by the blanket credit already in `CREDITS.md` — no new
  entry needed per icon.
- **Local SVGs** in `assets/images/icons/` (`ribcage`, `bowels`, `pelvis-bone`) from
  game-icons.net under CC BY 3.0, rendered via CSS `mask` + `currentColor` so they take the brand
  blue. Each is listed by file, icon name and author in `CREDITS.md`.

**Rule: any new local icon, image, or other asset added under `assets/` requires a row in
[CREDITS.md](../../../CREDITS.md)** giving the file path, the source, the author, the licence,
and any modification made. The footer in `_layouts/default.html` also carries a visible
game-icons.net attribution; if you add assets under a *different* licence that requires visible
credit, that footer line needs updating too.

Prefer a Font Awesome glyph when one exists. Reach for game-icons.net only for anatomy Font
Awesome lacks — that is the whole reason the local set exists.

Candidate hero images extracted from the original design brief sit in `docs/assets/`. They are
not published (the `docs` folder is excluded from the build) and their usage rights have not been
confirmed — do not move one into `assets/` without asking.

## Before you call it done

Run the `release` gate. A content change is not finished because the HTML looks right in the
diff; it is finished when the site builds clean and you have looked at the rendered page.
