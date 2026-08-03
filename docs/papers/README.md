# Local paper store — never committed

Put downloaded QUANTEC / HyTEC / PENTEC PDFs here. Every PDF in this folder is gitignored, so the
files stay on disk for fast local reference and never reach the public GitHub repository. Three
text files here *are* tracked: this README, `download-list.md`, and `organise-papers.py`.

## Getting the set — one command

Download the papers through your own browser (see [download-list.md](download-list.md) for all 24
links), leave them named as they arrive, then:

```
python organise-papers.py
```

It reads each PDF's own title page, renames it to the convention below, moves it here, and then
verifies the store is the complete supplement — 24 papers spanning S1–S160 with no gap and no
overlap. It refuses to move a file whose filename disagrees with its contents rather than
guessing, because a mis-served download landing under the wrong organ name is the failure this
repo cannot afford. `--verify-only` checks what you already have; `--source PATH` if your
downloads are not in `~/Downloads/Quantec`. Needs `pip install pypdf`.

## Why these are not committed, and will not be

Asked and settled on 2026-08-03. **Free to read is not free to redistribute.** The QUANTEC
supplement is free to read on redjournal.org, but that is a publisher access decision, not a
licence. All 24 PDFs carry *"Copyright © 2010 Elsevier Inc. … All rights reserved"* on page 1,
and a full-text search of all 24 turns up no open-access, Creative Commons, or reuse-permission
statement anywhere. This repository is public, so committing them would be republication.

Link to the papers — the site already does, for every one of them. Do not host them. If a
collaborator needs the set, point them at `download-list.md` and this script; that round trip
takes about twenty minutes.

They are also invisible to the site build: `_config.yml` excludes the whole `docs` folder, so
nothing here is published to quantecradiation.org. Both protections matter — gitignore alone
would still let a stray `jekyll build` copy files into `_site` if the exclude were ever removed.

## Why the PDFs are not fetched automatically

`redjournal.org` returns HTTP 403 to every scripted request; it sits behind a Cloudflare bot
challenge. Working around that is out of scope, and the articles are paywalled Elsevier content
in any case. **Download them yourself through institutional access** and drop them in here.

## Naming

Name each file after the organ or paper so it can be matched to a citation without opening it:

```
quantec-lung.pdf
quantec-heart.pdf
quantec-spinal-cord.pdf
quantec-ntcp-models.pdf        # Marks et al., "Use of Normal Tissue Complication
                               # Probability Models in the Clinic", S10-S19
```

The authoritative citation list, with the PII for each paper, is in
[../site-plan.md](../site-plan.md).

## Before any number from these papers reaches the site

Read the transcription rules in the `content-editing` skill first. In short: every dose value,
volume threshold and endpoint on the site must be transcribed from the PDF and then
independently re-checked against it. Nothing in this folder may be summarised from memory, and
no value may be filled in by inference when a cell is unclear — flag it and ask.

A wrong digit on a page a clinician plans from is a patient-safety problem, not a typo.
