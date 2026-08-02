---
name: release
description: >
  The verification gate every change to quantecradiation.org must pass before it goes into a PR —
  a clean `bundle exec jekyll build`, the internal link/anchor checker, a check that nothing
  unintended landed in `_site/`, and a rendered look at the affected pages at desktop and mobile
  widths. Load this when you think a change is finished, before opening or updating a PR, and
  before merging to main. This repo has no CI and no test suite, and merging to main publishes
  the live site — skipping this gate ships breakage straight to clinicians with nothing in
  between.
---

# The "done" gate

This repo's definition of done. All four steps, in order, every time. Nothing here may be eased,
skipped, or declared "not applicable" to make a change pass.

Prerequisite: Ruby on `PATH` — see the `preview` skill for the one-time Windows setup.

```powershell
$env:Path = "C:\Ruby33-x64\bin;" + $env:Path
```

## 1. Clean build

```bash
bundle exec jekyll clean && bundle exec jekyll build
```

Must exit 0. `jekyll clean` first is not optional — an incremental build can hide a deletion or
a renamed permalink by leaving the old output in place.

The expected output is exactly this and nothing more:

```
Configuration file: .../\_config.yml
            Source: ...
       Destination: .../\_site
 Incremental build: disabled. Enable with --incremental
      Generating...
       Jekyll Feed: Generating feed for posts
                    done in N seconds.
 Auto-regeneration: disabled. Use --watch to enable.
```

Any additional line is a warning and fails the gate. The ones this site is prone to:
`Deprecation: ...`, `Build Warning: Layout 'x' requested ... does not exist` (a typo'd `layout:`
in front matter), `Invalid date`, and Liquid warnings about an undefined filter or variable —
usually a misspelled `relative_url`, which silently produces a wrong link rather than an error.

## 2. Internal links and anchors resolve

```bash
python .claude/skills/release/scripts/check_links.py _site
```

Must print `OK: all internal links and anchors resolve` and exit 0. It walks every built page,
resolves each internal `href`/`src` against the real `_site` tree, and verifies that every
`#fragment` matches an `id` (or `<a name>`) that actually exists on the destination page.

**It deliberately does not touch the network**, so the external links — the Red Journal article
URLs, ScienceDirect, AAPM, PENTEC, game-icons.net — are counted and skipped, not verified. If a
change adds or edits an external citation URL, open it in the browser and confirm it resolves to
the paper it claims. See the content-accuracy rule in the `content-editing` skill; a citation
that 404s is the mildest of the ways that can go wrong.

## 3. Nothing unintended got published

```bash
ls -R _site
```

Jekyll copies unrecognised files through verbatim, so a stray file at the repo root becomes a
public URL. The expected tree is `index.html`; `about/`, `quantec/`, `publications/`,
`quantec-2/`, `contact/` and `resources/` each holding `index.html`; `assets/css`,
`assets/images`; and `CNAME`, `feed.xml`, `robots.txt`, `sitemap.xml`.

`resources/` is a deliberate redirect stub, not a page — `/resources/` was the QUANTEC page
before it moved to `/quantec/`, and the stub carries the fragment across so the live
`/resources/#cns` deep link still lands on the right card. Do not remove it.

**This list goes stale every time a page is added.** If something unexpected appears, work out
which it is before acting: a stray *file* — a `.docx`, the `docs/` folder, an editor backup —
belongs in `exclude:` in `_config.yml`; a new *page* belongs in the list above. A build once
shipped `UpdateRequests.docx` to the public site, which is why this step exists — but
`exclude:`-ing a real page would silently unpublish it, which is worse.

## 4. Look at it, at both widths

The first three steps prove the site builds and links up. They cannot tell you the page looks
right. For any change touching markup or CSS:

1. `preview_start` `{name: "jekyll-serve"}` → <http://127.0.0.1:4000/>.
2. Visit every page the change touched, plus the home page.
3. `resize_window` `{preset: "desktop"}` and `{preset: "mobile"}`. The breakpoint is 768px,
   where the nav restacks and `.gallery-container` collapses to one column. Card grids and the
   header are where this site has actually broken before.
4. `read_console_messages` — should be clean. Font Awesome 404s only mean the CDN is
   unreachable; that is an environment artifact, not a regression.

Restart the preview after any `_config.yml` edit; the watcher does not reload it.

### Two browser-pane artifacts that look like site bugs

When the Browser pane is not actually displayed, the page does not composite frames. Two
consequences, both of which have already cost a session:

- **`computer{action:"screenshot"}` fails** with "the page is not compositing frames". Fall back
  to `read_page` and to `javascript_tool` reading `getComputedStyle` / `getBoundingClientRect` —
  that measures real layout and is a stronger check than eyeballing a screenshot anyway.
- **CSS transitions never advance**, so a transitioned property reads stuck at its start value.
  `.gallery-item` transitions `box-shadow`, so `/resources/#cns` reports its `:target` ring as
  `rgba(0,0,0,0) 0px 0px 0px 0px` and looks broken. It is not. Set
  `el.style.transition = 'none'` before reading, and the real value appears
  (`rgb(44,90,160) 0px 0px 0px 3px`). Do not "fix" a rule based on a mid-transition reading.

Useful one-liners for step 4, given the above:

```js
// no horizontal overflow, and which element is to blame if there is
document.documentElement.scrollWidth > innerWidth
[...document.querySelectorAll('*')].filter(e => e.getBoundingClientRect().width > innerWidth + 1)
// the responsive grid actually collapsed
getComputedStyle(document.querySelector('.gallery-container')).gridTemplateColumns
// the stylesheet loaded at all (CDN sheets read as CORS-blocked; the local one must not)
[...document.styleSheets].some(s => (s.href||'').includes('style.css'))
```

## Then, and only then: the PR

- **Never commit or push directly to `main`.** There is no `dev` branch here, so every change —
  including a one-line typo fix — goes through a branch and a pull request.
- Merging to `main` publishes to quantecradiation.org immediately via GitHub Pages. There is no
  staging environment and no CI to catch what this gate misses.
- Say in the PR body which steps you ran and what you saw. If you could not run step 4 (no
  browser tooling available, say), state that plainly and ask the owner for a visual check —
  do not quietly count the change as verified.
