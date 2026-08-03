# Papers to download

Tick these off as you go. Save each into this folder (`docs/papers/`) under the **filename**
given — everything here except `README.md` and this file is gitignored, so nothing you drop in
reaches the public repository, and `_config.yml` keeps it out of the site build too.

Two links per paper: **PDF** downloads directly; **Full text** is the article page, useful when
a PDF link misbehaves or you want to check a figure in place.

Two caveats before you start.

**These links are for you, in a real browser — not for me.** The `showPdf` endpoint sits behind
a Cloudflare bot challenge: `curl -I` on it returns `403` with `cf-mitigated: challenge`, and
opening it in the in-app browser pane served the "Just a moment…" interstitial, which then ran
a GPU-fingerprinting burst and preceded a hard crash of the Claude app on 2026-08-02. In your
own signed-in browser it is an ordinary download. Nothing in this repo should ever point an
automated fetch at these.

**Access:** when I checked, the publisher identified the session as a *"Generic Guest Account"*,
not a UC San Diego one. The QUANTEC supplement appears to be free to read, so the article pages
rendered anyway — but if a PDF asks you to pay, that is why, and going through the UCSD library
proxy should clear it.

## Introductory papers (3)

| ✓ | Paper | Save as | Links |
|---|---|---|---|
| ☐ | Guest Editor's Introduction to QUANTEC: A Users Guide | `quantec-00-users-guide.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903302-1) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03302-1/fulltext>) |
| ☐ | Quantitative Analyses of Normal Tissue Effects in the Clinic (QUANTEC): An Introduction to the Scientific Issues | `quantec-00-scientific-issues.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903300-8) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03300-8/fulltext>) |
| ☐ | Use of Normal Tissue Complication Probability Models in the Clinic | `quantec-00-ntcp-models.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903288-X) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03288-X/fulltext>) |

## Organ-specific papers (16)

| ✓ | Organ | Save as | Links |
|---|---|---|---|
| ☐ | CNS: Brain | `quantec-cns-brain.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903287-8) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03287-8/fulltext>) |
| ☐ | CNS: Optic Nerve/Chiasm | `quantec-cns-optic-nerve-chiasm.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903284-2) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03284-2/fulltext>) |
| ☐ | CNS: Brain Stem | `quantec-cns-brain-stem.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903582-2) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03582-2/fulltext>) |
| ☐ | CNS: Spinal Cord | `quantec-cns-spinal-cord.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903296-9) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03296-9/fulltext>) |
| ☐ | CNS: Ear | `quantec-cns-ear.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903298-2) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03298-2/fulltext>) |
| ☐ | Head and Neck: Parotid | `quantec-head-and-neck-parotid.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903289-1) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03289-1/fulltext>) |
| ☐ | Head and Neck: Larynx/Pharynx | `quantec-head-and-neck-larynx-pharynx.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903292-1) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03292-1/fulltext>) |
| ☐ | Thorax: Lung | `quantec-thorax-lung.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903293-3) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03293-3/fulltext>) |
| ☐ | Thorax: Heart | `quantec-thorax-heart.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903290-8) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03290-8/fulltext>) |
| ☐ | Thorax: Esophagus | `quantec-thorax-esophagus.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903283-0) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03283-0/fulltext>) |
| ☐ | Abdomen: Liver | `quantec-abdomen-liver.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903295-7) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03295-7/fulltext>) |
| ☐ | Abdomen: Stomach/Small Bowel | `quantec-abdomen-stomach-small-bowel.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903286-6) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03286-6/fulltext>) |
| ☐ | Abdomen: Kidney | `quantec-abdomen-kidney.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903282-9) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03282-9/fulltext>) |
| ☐ | Pelvis: Bladder | `quantec-pelvis-bladder.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903285-4) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03285-4/fulltext>) |
| ☐ | Pelvis: Rectum | `quantec-pelvis-rectum.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903291-X) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03291-X/fulltext>) |
| ☐ | Pelvis: Penile Bulb | `quantec-pelvis-penile-bulb.pdf` | [PDF](https://www.redjournal.org/action/showPdf?pii=S0360-3016%2809%2903294-5) · [Full text](<https://www.redjournal.org/article/S0360-3016(09)03294-5/fulltext>) |

## Start with these three

The agreed pilot is **lung, heart and spinal cord**. If you only grab a few, grab those —
they are enough to prove the table format and the verification protocol before committing to
the rest.

## Not single papers

HyTEC and PENTEC are whole special issues rather than individual articles, so there is no one
PDF to fetch. Their issue and website links are in
[../update-requests.md](../update-requests.md); pull individual articles from there if and
when we extend the tables beyond QUANTEC.

## A note on what happens to these

Values transcribed from these PDFs go onto a public clinical site, so the agreed rules are:
our own table structure rather than a reproduction of the publisher's, every value attributed
to paper and page, every number independently re-checked against the source by a separate
pass, and anything ambiguous in the original flagged to you rather than inferred.
