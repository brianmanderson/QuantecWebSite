"""Check that every internal link and anchor in a built Jekyll site resolves.

Usage: python .claude/skills/release/scripts/check_links.py [_site]

Exits non-zero and prints one line per problem. External (http/https), mailto: and tel: links
are reported as a count only -- this script never makes a network request.
"""

import re
import sys
from html import unescape
from pathlib import Path
from urllib.parse import unquote, urldefrag

HREF = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)
ID = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)
NAME_ANCHOR = re.compile(r"""<a\b[^>]*\bname\s*=\s*["']([^"']+)["']""", re.I)


def page_url(site: Path, path: Path) -> str:
    """The URL a built file is served at, e.g. _site/about/index.html -> /about/."""
    rel = path.relative_to(site).as_posix()
    return "/" + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else "_site").resolve()
    if not site.is_dir():
        print(f"FAIL: {site} does not exist -- run `bundle exec jekyll build` first")
        return 1

    html_files = sorted(site.rglob("*.html"))
    # Every URL the site actually serves, plus the ids each page defines.
    served: set[str] = set()
    anchors: dict[str, set[str]] = {}
    for f in html_files:
        url = page_url(site, f)
        served.add(url)
        text = f.read_text(encoding="utf-8", errors="replace")
        anchors[url] = {unescape(m) for m in ID.findall(text)} | {
            unescape(m) for m in NAME_ANCHOR.findall(text)
        }
    for f in site.rglob("*"):
        if f.is_file() and f.suffix != ".html":
            served.add(page_url(site, f))

    problems: list[str] = []
    external = 0

    for f in html_files:
        src = page_url(site, f)
        text = f.read_text(encoding="utf-8", errors="replace")
        for raw in HREF.findall(text):
            href = unescape(raw).strip()
            if not href or href.startswith(("http://", "https://", "//", "mailto:", "tel:", "data:", "javascript:")):
                external += 1
                continue

            target, frag = urldefrag(href)
            target, frag = unquote(target), unquote(frag)

            if not target:  # same-page anchor, e.g. href="#resources"
                dest = src
            elif target.startswith("/"):
                dest = target
            else:  # relative to the directory this page is served from
                base = src if src.endswith("/") else src.rsplit("/", 1)[0] + "/"
                dest = base + target
            # normalise ../ and ./
            parts: list[str] = []
            for seg in dest.split("/"):
                if seg == "..":
                    if parts:
                        parts.pop()
                elif seg not in (".",):
                    parts.append(seg)
            dest = "/" + "/".join(parts[1:]) if parts and parts[0] == "" else "/" + "/".join(parts)

            candidates = {dest, dest + "/", dest + ".html"} if not dest.endswith("/") else {dest}
            hit = next((c for c in candidates if c in served), None)
            if hit is None:
                problems.append(f"{src}: broken link -> {href}")
                continue

            if frag:
                known = anchors.get(hit)
                if known is not None and frag not in known:
                    problems.append(f"{src}: anchor #{frag} not found on {hit} (via {href})")

    print(f"checked {len(html_files)} pages, {len(served)} served URLs, {external} external/mailto links skipped")
    for p in problems:
        print("FAIL " + p)
    if problems:
        print(f"\n{len(problems)} problem(s)")
        return 1
    print("OK: all internal links and anchors resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
