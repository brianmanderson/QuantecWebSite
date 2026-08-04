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

## 4. Look at it, at the widths that matter

The first three steps prove the site builds and links up. They cannot tell you the page looks
right. For any change touching markup or CSS:

1. `preview_start` `{name: "jekyll-serve"}` → <http://127.0.0.1:4000/>.
2. Visit every page the change touched, plus the home page.
3. `resize_window` `{preset: "desktop"}` and `{preset: "mobile"}`. The breakpoint is 768px,
   where the nav restacks and `.gallery-container` collapses to one column. Card grids and the
   header are where this site has actually broken before.
4. **If the change touched a responsive layout whose content carries a `min-width`, measure at
   breakpoint + 1px as well, then walk up until `scrollWidth <= clientWidth` on the scroll
   container.** A breakpoint is where a layout *switches*, not where the new layout *fits* —
   different numbers whenever the content has a floor. 1280 and 375 sit either side of the
   switch, so they prove the switch fires and nothing else. On 2026-08-03 the band between them
   was real: every constraint table on `/quantec/` clipped its rightmost column — Notes, which
   carries the caveats qualifying the dose numbers — from 769px up, because the stacked layout
   was keyed to the generic 768px breakpoint. The gate passed at 1280 and 375; an independent
   `site-reviewer` run found the band afterwards, and PR #20 rekeyed the block to 880px.

   **Never read the fitting width off the rendered content.** `.constraint-table` is `width: 100%`
   above a `min-width: 680px` floor, so it measures whatever the wrapper gives it. Reading its
   width at the point clipping stopped therefore just restates the viewport, and that circularity
   is how 880px was derived from a table "needing 736px": at 881px the table does measure 736px,
   and 881 − 145px of page chrome is 736.

   **But do not then reach for the `min-width` floor either.** That was tried on 2026-08-03 and
   was wrong in the dangerous direction: it gave "the content fits at 825px", and forcing the
   wrapper to 680px in fact clips the liver table by 25px — its Notes column, the exact failure
   this whole item exists to catch. The floor is a floor, not a requirement. Two tables' content
   has always exceeded it.

   **Measure each table's intrinsic width.** Neither circular nor the floor:

   ```js
   t.style.width = 'min-content'; t.style.minWidth = '0';   // then read getBoundingClientRect
   ```

   As of 2026-08-04: liver 703px (widest), cochlea 610, bladder 575, stomach 294 — so the grid
   genuinely fits from about 850px and 880 carries ~30px of margin. Kidney was the widest at
   736px until its Technique and Fractionation columns moved into its caption; that 736 also
   equalled 881 − 145 was a coincidence, and it is what made a correct figure look circular.

   **A walk-up loop cannot find this number**, which is why the bad figure above went unchallenged.
   The stacked layout is already live below the breakpoint, so a loop that starts under it returns
   its own start value and looks like a confident answer. Probe the grid by forcing wrapper widths
   at a viewport *above* the breakpoint, or by measuring intrinsic width as above. Allow ~2px for
   the wrapper's borders — every table reads 2px over at exactly its own width, so `+2` is the
   noise floor, not a clip.
5. **Sweep *below* the breakpoint as well, not just 375px.** This file used to assert here that
   the stacked layout "never clips". It did. The stacked cells were a CSS grid whose value track
   was `1fr`, and an auto-sized track cannot shrink below its content's min-content width, so one
   unbreakable token — the bladder Notes cell's "size/shape/location", 128px — put a floor under
   the whole table. Bladder overflowed its wrapper by 5px at 375px, 20px at 360px and 60px at
   320px, where seven other tables joined it. Eight review rounds and a 375px-only mobile check
   never saw it, because 375 is where it happened to be smallest. Below the breakpoint the wrapper
   does not scroll (`overflow-x: visible`), so a clip here spills onto the page instead of hiding
   behind a scrollbar. Use the same iframe harness as (a), stepping
   `[320, 360, 375, 390, 414, 480, 600, 768, 880]`. `minmax(0, 1fr)` is the fix when the cell is a
   grid; `table-layout: fixed` is the same fix for the inner tables these cells became on
   2026-08-04.
6. `read_console_messages` — should be clean. Font Awesome 404s only mean the CDN is
   unreachable; that is an environment artifact, not a regression.

Restart the preview after any `_config.yml` edit; the watcher does not reload it.

### Three browser-pane artifacts that look like site bugs

When the Browser pane is not actually displayed, the page does not composite frames. Three
consequences, all of which have already cost a session:

- **`computer{action:"screenshot"}` fails** with "the page is not compositing frames". Fall back
  to `read_page` and to `javascript_tool` reading `getComputedStyle` / `getBoundingClientRect` —
  that measures real layout and is a stronger check than eyeballing a screenshot anyway.
- **CSS transitions never advance**, so a transitioned property reads stuck at its start value.
  `.gallery-item` transitions `box-shadow`, so `/resources/#cns` reports its `:target` ring as
  `rgba(0,0,0,0) 0px 0px 0px 0px` and looks broken. It is not. Set
  `el.style.transition = 'none'` before reading, and the real value appears
  (`rgb(44,90,160) 0px 0px 0px 3px`). Do not "fix" a rule based on a mid-transition reading.
- **`resize_window` silently clamps the width.** It reports success while `innerWidth` stays
  around 441px. Every narrower width then measures that same layout, so the check *looks* clean
  and describes a width nobody uses — and because 441 is under 768, a mobile check passes
  without ever rendering mobile. Measure exact widths in an iframe instead: an iframe
  establishes its own viewport, so media queries resolve at the width you set. Read `innerWidth`
  back and never report a width you did not read back from the thing you measured.

The two measurements item 4 asks for, and why the iframe is not optional. Resizing the iframe
re-resolves its media queries, so neither needs a reload per width — but both need the forced
reflow, because `requestAnimationFrame` never fires in a pane that is not compositing.

**(a) Confirm nothing clips at breakpoint + 1 and above.** This is the check that must pass:

```js
(async () => {
  const f = document.createElement('iframe');
  f.style.cssText = 'position:fixed;left:-9999px;top:0;height:900px;border:0;width:881px;';
  f.src = '/quantec/'; document.body.appendChild(f);
  await new Promise(r => f.onload = r);
  const d = f.contentDocument, out = {};
  for (const w of [881, 882, 885, 900, 1000, 1280]) {
    f.style.width = w + 'px';
    void d.documentElement.offsetWidth;                  // sync reflow; rAF never fires here
    if (f.contentWindow.innerWidth !== w) throw new Error('width lied: ' + f.contentWindow.innerWidth);
    out[w] = [...d.querySelectorAll('.constraint-table-wrap')]  // the scroll container
      .filter(e => e.scrollWidth > e.clientWidth)
      .map(e => `${e.id}(+${e.scrollWidth - e.clientWidth})`).join(' ') || 'clean';
  }
  return out;                                            // every entry must read "clean"
})()
```

**(b) Derive the number the breakpoint should be, if you need to change it.** Intrinsic width,
measured above the breakpoint so the grid layout is the one being probed — a loop walking up from
below it measures the stacked layout and returns its own start value:

```js
(async () => {
  const f = document.createElement('iframe');
  f.style.cssText = 'position:fixed;left:-9999px;top:0;height:900px;border:0;width:1400px;';
  f.src = '/quantec/'; document.body.appendChild(f);
  await new Promise(r => f.onload = r);
  const d = f.contentDocument;
  void d.documentElement.offsetWidth;
  return [...d.querySelectorAll('.constraint-table')].map(t => {
    const prev = t.style.cssText;
    t.style.width = 'min-content'; t.style.minWidth = '0';   // defeat width:100% AND the floor
    const w = Math.ceil(t.getBoundingClientRect().width);
    t.style.cssText = prev;
    return {id: t.closest('.constraint-table-wrap').id, intrinsic: w};
  }).sort((a, b) => b.intrinsic - a.intrinsic);             // widest first; add ~145px of chrome
})()
```

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
