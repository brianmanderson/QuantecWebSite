# Local paper store — never committed

Put downloaded QUANTEC / HyTEC / PENTEC PDFs here. Everything in this folder except this README
is gitignored, so the files stay on disk for fast local reference and never reach the public
GitHub repository.

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
