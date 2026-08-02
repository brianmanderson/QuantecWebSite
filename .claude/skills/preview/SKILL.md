---
name: preview
description: >
  How to build and serve quantecradiation.org locally with Jekyll, and how to look at a change in
  a browser before calling it done. Load this BEFORE the first `bundle` or `jekyll` command of a
  session, before starting or restarting the dev server, and whenever `bundle install` fails,
  `jekyll serve` won't start, or a page 404s locally that you expect to exist. Skipping it costs
  you the Windows Ruby setup (the toolchain winget installs is incomplete) and leads to
  "it looks fine in the HTML" claims that were never actually rendered.
---

# Preview the site locally

## One-time machine setup (Windows)

This machine had no Ruby until it was installed for this repo. If `ruby -v` fails, redo this:

```powershell
winget install --id RubyInstallerTeam.RubyWithDevKit.3.3 --exact --silent
```

**The winget package alone is not enough.** It ships RubyInstaller but does not unpack MSYS2, so
gems with native extensions (`json`, `bigdecimal`, `http_parser.rb`, `eventmachine`) fail with
`MSYS2 could not be found. Please run 'ridk install'`. Finish the install:

```powershell
ridk install 1
```

`1` is the MSYS2 base install, and it is sufficient for this Gemfile — all four native gems
build against it. Pass the number as an argument; bare `ridk install` opens an interactive menu
and hangs a non-interactive shell.

Do **not** bother with `ridk install 1 3` (the MINGW dev toolchain). On this machine step 3 dies
with `pacman failed` / "could not find or read directory (root: /, dbpath: /var/lib/pacman/)".
That failure is harmless and not worth debugging — `bundle install` completes without it.

Stay on **Ruby 3.3**, which is what GitHub Pages builds with. Ruby 3.4+ removed `csv`, `base64`,
and `logger` from the default gems, and this repo's Gemfile does not declare them.

Ruby installs to `C:\Ruby33-x64\bin`. A shell opened before the install will not have it on
`PATH`; prepend it rather than reasoning about why `bundle` is missing:

```powershell
$env:Path = "C:\Ruby33-x64\bin;" + $env:Path
```

## Install dependencies

```bash
bundle install
```

`Gemfile.lock` is tracked and pins the platform. If bundler complains that the lockfile does not
have your platform, `bundle lock --add-platform x64-mingw-ucrt` rather than deleting the lock.

## Serve

Use the tracked preview config, not a raw `jekyll serve` in a Bash call:

- `preview_start` with `{name: "jekyll-serve"}` → runs
  `bundle exec jekyll serve --host 127.0.0.1 --port 4000` from `.claude/launch.json`.
- Open **<http://127.0.0.1:4000/>**.
- Jekyll watches and rebuilds on save, but `_config.yml` changes are **not** picked up by the
  watcher — restart the server after editing it, or you will be looking at a stale build and
  concluding your change did nothing.

To build without serving (this is what the release gate runs):

```bash
bundle exec jekyll build
```

Output lands in `_site/`, which is gitignored.

## URLs: every page is a directory, not an `.html` file

`_config.yml` sets a global `permalink: /:title/`, and in Jekyll 4 that applies to pages as well
as posts. So `about.html` at the repo root builds to `_site/about/index.html` and is served at
`/about/`. Verified from a real build — the whole `_site` tree is:

```
_site/{index.html, about/, constraints/, publications/, quantec-2/, contact/, resources/}/index.html
_site/{CNAME, feed.xml, robots.txt, sitemap.xml}
_site/assets/...
```

Consequences worth knowing before you "fix" a link:

- The nav in `_layouts/default.html` correctly links to `/about`, `/quantec/`, `/contact`.
  Adding `.html` to those would break them — there is no `about.html` in the output.
- `/resources/` is a redirect stub, not a page: it was the constraints page before the rename
  and forwards to `/quantec/` preserving the fragment. Leave it in place.
- `publications.html` *also* sets `permalink: /publications/` explicitly in its front matter.
  That is redundant with the global rule but harmless; leave it.
- Deleting or changing the global `permalink` silently changes every URL on a live public site.
  Don't touch it without a redirect plan.

## Anything not excluded gets published

Jekyll copies unrecognised files through to `_site` verbatim. Before this was fixed, a build
shipped `UpdateRequests.docx` to the public site. `_config.yml`'s `exclude:` list now covers
`docs`, `*.docx`, the Gemfiles, and the two root markdown files. **After adding any new
top-level file or folder to the repo, build and check whether it landed in `_site/`.**

Dotfiles and dot-directories (`.claude/`, `.git/`) are excluded by Jekyll automatically.

## Verify a change visually — this is the actual bar

Reading the HTML you just wrote is not verification. For any change that touches markup or CSS:

1. Start the preview and navigate to the page you changed.
2. `read_page` (or a screenshot) and confirm the change is present in the rendered output.
3. Check **both widths**. The breakpoint is at 768px in `assets/css/style.css`, where the nav
   restacks and the gallery grid collapses to one column. Use `resize_window` with
   `preset: "mobile"` and `preset: "desktop"`.
4. If you added or changed a link or anchor, click it. Anchor targets like
   `/quantec/#cns` depend on an `id` that actually exists on a `.gallery-item`.

Console errors are worth a glance too — the layout pulls Font Awesome from a CDN, so icons
silently disappear when offline. That is an environment artifact, not a bug to chase.

## Related skills

- `release` — the full gate a change must pass before it goes into a PR.
- `content-editing` — where content lives and the rules for changing it.
