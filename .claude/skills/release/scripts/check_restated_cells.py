"""Verify every restated table cell still matches the merged cell it stands in for.

A cell merged with `rowspan` renders in its first row only, so the stacked phone layout cannot
reach it from any later row. Where the merged value is one a reader must not lose — a dose, not a
qualifier — the markup restates it in the later row and CSS shows whichever copy the current
layout needs. That leaves two copies of a clinical value in the page, and nothing but this check
stops them drifting apart.

Usage:  python check_restated_cells.py _site
Exits 0 and prints OK when every pair matches, or 1 naming the mismatch.
"""

import pathlib
import re
import sys
from html.parser import HTMLParser


class Cells(HTMLParser):
    """Collect the inner HTML of cells carrying the classes we care about, per table."""

    WANTED = ("grouped-value", "dose-restated")

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.tables = []
        self.depth = 0
        self.kind = None
        self.buf = []
        self.caption = None
        self.cap_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table":
            self.tables.append({"caption": "", "cells": []})
        elif not self.tables:
            return
        elif tag == "caption":
            self.cap_buf = []
        elif tag == "td":
            cls = (a.get("class") or "").split()
            hit = next((w for w in self.WANTED if w in cls), None)
            if hit:
                self.kind, self.buf, self.depth = hit, [], 0
        elif self.kind is not None:
            self.depth += 1
            self.buf.append(self.get_starttag_text())

    def handle_startendtag(self, tag, attrs):
        if self.kind is not None:
            self.buf.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if not self.tables:
            return
        if tag == "caption" and self.cap_buf is not None:
            self.tables[-1]["caption"] = " ".join("".join(self.cap_buf).split())
            self.cap_buf = None
        elif tag == "td" and self.kind is not None:
            self.tables[-1]["cells"].append((self.kind, "".join(self.buf).strip()))
            self.kind = None
        elif self.kind is not None and self.depth > 0:
            self.depth -= 1
            self.buf.append(f"</{tag}>")

    def handle_data(self, data):
        if self.kind is not None:
            self.buf.append(data)
        elif self.cap_buf is not None:
            self.cap_buf.append(data)

    def handle_entityref(self, name):
        if self.kind is not None:
            self.buf.append(f"&{name};")

    def handle_charref(self, name):
        if self.kind is not None:
            self.buf.append(f"&#{name};")


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "_site")
    pairs = failures = 0
    for page in sorted(root.rglob("*.html")):
        p = Cells()
        p.feed(page.read_text(encoding="utf-8"))
        for t in p.tables:
            merged = [v for k, v in t["cells"] if k == "grouped-value"]
            restated = [v for k, v in t["cells"] if k == "dose-restated"]
            if not merged and not restated:
                continue
            name = t["caption"].split(" Every row")[0].strip() or page.name
            if not merged or not restated:
                print(
                    f"FAIL {name}: {len(merged)} merged cell(s) but {len(restated)} restated — "
                    "a restatement without its merged cell (or vice versa) means one layout "
                    "shows the value and the other shows nothing"
                )
                failures += 1
                continue
            for r in restated:
                pairs += 1
                if r != merged[0]:
                    failures += 1
                    print(f"FAIL {name}: restated cell does not match the merged cell")
                    print(f"      merged:   {merged[0]}")
                    print(f"      restated: {r}")
    if failures:
        print(f"\n{failures} mismatch(es). The two copies of a value must be identical.")
        return 1
    print(f"OK: {pairs} restated cell(s) match the merged cell they stand in for")
    return 0


if __name__ == "__main__":
    sys.exit(main())
