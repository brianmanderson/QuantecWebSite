#!/usr/bin/env python3
"""Organise downloaded QUANTEC PDFs into this folder, and verify the set is complete.

The papers are copyrighted Elsevier articles ("All rights reserved" on every one), so they are
never committed - see the gitignore rules and README.md in this folder. This script exists so a
collaborator can get from "24 files called PIIS0360301609032829.pdf" to a correctly named,
verified local store in one command, without anyone having to host the PDFs.

Usage:
    python organise-papers.py                      # from ~/Downloads/Quantec into this folder
    python organise-papers.py --source PATH
    python organise-papers.py --verify-only        # just check what is already here

Identification does NOT trust the download filename. Each file is matched by reading its own
title page - the supplement page range plus the section label the publisher prints on it. The
filename PII is used only as a cross-check, and a disagreement is reported rather than resolved,
because a mis-served download that silently lands under the wrong organ name is exactly the
failure this repo cannot afford.

Requires pypdf (pip install pypdf).
"""

import argparse
import logging
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("pypdf is required: pip install pypdf")

# pypdf logs its own parse warnings to stderr, which interleave ahead of this script's output and
# read as a crash. Each unreadable file is reported by name below anyway.
logging.getLogger("pypdf").setLevel(logging.CRITICAL)

# (compact PII as it appears in the download filename, canonical name, first page, last page)
# Page ranges are from each paper's own title page and together cover S1-S160 with no gap.
PAPERS = [
    ("S0360301609033021", "quantec-00-users-guide.pdf", 1, 2),
    ("S0360301609033008", "quantec-00-scientific-issues.pdf", 3, 9),
    ("S036030160903288X", "quantec-00-ntcp-models.pdf", 10, 19),
    ("S0360301609032878", "quantec-cns-brain.pdf", 20, 27),
    ("S0360301609032842", "quantec-cns-optic-nerve-chiasm.pdf", 28, 35),
    ("S0360301609035822", "quantec-cns-brain-stem.pdf", 36, 41),
    ("S0360301609032969", "quantec-cns-spinal-cord.pdf", 42, 49),
    ("S0360301609032982", "quantec-cns-ear.pdf", 50, 57),
    ("S0360301609032891", "quantec-head-and-neck-parotid.pdf", 58, 63),
    ("S0360301609032921", "quantec-head-and-neck-larynx-pharynx.pdf", 64, 69),
    ("S0360301609032933", "quantec-thorax-lung.pdf", 70, 76),
    ("S0360301609032908", "quantec-thorax-heart.pdf", 77, 85),
    ("S0360301609032830", "quantec-thorax-esophagus.pdf", 86, 93),
    ("S0360301609032957", "quantec-abdomen-liver.pdf", 94, 100),
    ("S0360301609032866", "quantec-abdomen-stomach-small-bowel.pdf", 101, 107),
    ("S0360301609032829", "quantec-abdomen-kidney.pdf", 108, 115),
    ("S0360301609032854", "quantec-pelvis-bladder.pdf", 116, 122),
    ("S036030160903291X", "quantec-pelvis-rectum.pdf", 123, 129),
    ("S0360301609032945", "quantec-pelvis-penile-bulb.pdf", 130, 134),
    ("S0360301609032970", "quantec-vision-dose-accumulation.pdf", 135, 139),
    ("S0360301609035810", "quantec-vision-imaging.pdf", 140, 144),
    ("S0360301609035792", "quantec-vision-biomarkers.pdf", 145, 150),
    ("S036030160903301X", "quantec-vision-data-pooling.pdf", 151, 154),
    ("S0360301609032994", "quantec-vision-lessons-reporting.pdf", 155, 160),
]

BY_PAGES = {(p[2], p[3]): p for p in PAPERS}
BY_PII = {p[0]: p for p in PAPERS}
PAGE_RE = re.compile(r"pp\.\s*S(\d+)\W{1,3}S(\d+)")


def read_page_range(pdf_path):
    """Return (first, last) supplement page numbers from the paper's own title page."""
    try:
        text = PdfReader(str(pdf_path)).pages[0].extract_text() or ""
    except Exception as exc:                                    # unreadable / not a PDF
        return None, f"could not read: {exc}"
    match = PAGE_RE.search(text.replace("\n", " "))
    if not match:
        return None, "no 'pp. Sx-Sy' line on the title page"
    return (int(match.group(1)), int(match.group(2))), None


def organise(source, dest):
    pdfs = sorted(source.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs in {source}")
        return 0

    moved = problems = 0
    for pdf in pdfs:
        pages, err = read_page_range(pdf)
        if err:
            print(f"  SKIP  {pdf.name}: {err}")
            problems += 1
            continue

        paper = BY_PAGES.get(pages)
        if paper is None:
            print(f"  SKIP  {pdf.name}: pages S{pages[0]}-S{pages[1]} match no known QUANTEC paper")
            problems += 1
            continue

        # Cross-check against the filename PII. Report disagreement; never silently prefer one.
        stem = pdf.stem.upper()
        if stem.startswith("PII"):
            claimed = BY_PII.get(stem[3:])
            if claimed is not None and claimed is not paper:
                print(f"  STOP  {pdf.name}: filename says {claimed[1]}, "
                      f"but its title page reads S{pages[0]}-S{pages[1]} = {paper[1]}. "
                      f"Not moved - check this download.")
                problems += 1
                continue

        target = dest / paper[1]
        if target.exists():
            print(f"  have  {paper[1]}")
            continue
        pdf.rename(target)
        print(f"  moved {pdf.name} -> {paper[1]}  (S{pages[0]}-S{pages[1]})")
        moved += 1

    print(f"\n{moved} moved, {problems} problem(s).")
    return problems


def verify(dest):
    """Confirm the local store is the complete supplement: all 24, S1-S160, no gap."""
    print("Verifying local store...")
    missing = [p[1] for p in PAPERS if not (dest / p[1]).exists()]
    present = [p for p in PAPERS if (dest / p[1]).exists()]

    gaps = []
    expected_next = 1
    for _, name, first, last in sorted(present, key=lambda p: p[2]):
        if first != expected_next:
            gaps.append(f"S{expected_next} (before {name})")
        expected_next = last + 1

    print(f"  {len(present)}/{len(PAPERS)} papers present")
    if missing:
        print(f"  MISSING ({len(missing)}):")
        for name in missing:
            print(f"    - {name}")
    if gaps:
        print(f"  page-range gaps at: {', '.join(gaps)}")

    if not missing and not gaps:
        print(f"  pages S1-S{present[-1][3]} contiguous, no gap, no overlap")
        print("\nOK: complete QUANTEC supplement (3 introductory, 16 organ-specific, 5 vision).")
        return 0
    print("\nIncomplete. Links for the missing papers are in download-list.md.")
    return 1


def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, default=Path.home() / "Downloads" / "Quantec",
                        help="folder holding the freshly downloaded PDFs")
    parser.add_argument("--dest", type=Path, default=here,
                        help="the local paper store (defaults to this script's folder)")
    parser.add_argument("--verify-only", action="store_true",
                        help="do not move anything, just check what is already present")
    args = parser.parse_args()

    if not args.verify_only:
        if not args.source.is_dir():
            print(f"Source folder does not exist: {args.source}")
            print("Download the papers first - see download-list.md.")
            return 1
        print(f"Organising {args.source} -> {args.dest}")
        organise(args.source, args.dest)
        print()

    return verify(args.dest)


if __name__ == "__main__":
    sys.exit(main())
