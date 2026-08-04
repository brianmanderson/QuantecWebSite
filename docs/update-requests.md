# Pending site update requests

Transcribed verbatim from `UpdateRequests.docx` (dated 2025-07-16), which was an untracked
working file at the repo root.

The source document listed edits under bare headings like "Please edit to:" without naming the
panel. The section mapping below is *inferred* from the order matching the four organ panels on
what is now [quantec.html](../quantec.html).

## Implementation status

**Implemented on 2026-08-01**, in the branch that introduced `/quantec/` and `/quantec-2/`.

Both requested renames were applied: the constraints page moved to `/quantec/` and the
publications page became **AllTEC Publications**. The constraints tab was then relabelled
**Constraints** per ruling 3 below; its URL is still `/quantec/`. The sub-tabs are in-page section links
rather than a dropdown. The nav fits on one header row at 1280px (569px of a 594px budget) —
`assets/css/style.css` carries the measurement and the warning against widening it.

### Rulings — 2026-08-02

All six open points were settled by the site owner. **Do not re-flag these; they are decisions,
not defects.** The reasoning that was argued against each one is kept below so the trade-off
stays visible, but the ruling stands.

| # | Point | Ruling |
|---|---|---|
| 1 | Inferred panel mapping | **Confirmed correct.** The order-based mapping is what was intended. Closed. |
| 2 | Respiratory reworded | **Reverted.** Original four bullets restored verbatim. |
| 2b | Gastrointestinal reworded | **Reverted.** Original four bullets restored, plus the two requested additions. |
| 3 | Three QUANTEC-named destinations | **Constraints tab relabelled.** Nav now reads "Constraints"; the URL stays `/quantec/`. |
| 4 | Added sixth panel | **Kept** (Genitourinary and Pelvis). |
| 5 | Ear/cochlea under Head and Neck | **Kept as intentional.** The update request supersedes the design brief here. |

On 2 and 2b specifically: the restored bullets are the site owner's own words, supplied by them,
which is exactly what the content-accuracy rule requires — they are not model-generated. Two
caveats were raised and overruled, recorded here so nobody re-opens them:

- *"Trachea/bronchi guidelines"* — the original QUANTEC has no trachea or bronchi review, so
  this topic has no paper to link to. The panel now carries a note saying so rather than
  linking the bullet to an unrelated review.
- *"Lung V20/V30 constraints"* — the lung review's own abstract states there are "no evident
  threshold 'tolerance dose–volume' levels".

  **Follow-up, 2026-08-03.** Once the lung table was published, this bullet was briefly turned
  into a link to it. That made the mismatch concrete: Table 1's lung block carries `V20 ≤ 30%`
  and five mean-dose rows and **no V30 row at all** (verified against S16 of the summary paper;
  the only V30 on that page is the pericardium row in the heart block). A clinician clicking a
  bullet that says "V20/V30" and landing on a table without V30 is worse than not linking it.
  The bullet keeps the owner's wording, unlinked, and the panel note now states what the
  summary table actually carries. **Do not re-link it, and do not "fix" the wording** — the
  words are the owner's under ruling 2, and the absent V30 is the source's.

On 3: the two labels suggested were "Dose Constraints" and "Constraints by Organ". Neither fits
— they measure 610px and 639px against a 594px budget and wrap the header to two rows.
"Constraints" fits at 569px with 25px of slack and breaks the name collision just as completely.

### How the six organ cards route — settled, do not "normalise"

Five cards end with a single `.panel-link` arrow to their section of the Publications page. **The
Gastrointestinal card deliberately does not, and this is not an oversight** — it has been flagged
as one by more than one review, so it is written down here.

That card's six topics do not live in one section: small bowel, liver, kidney and stomach are
under Abdomen, rectal toxicity under Pelvis, esophagus under Thorax. A single "→ papers" arrow
would have to pick one and be wrong for the other two, so each bullet links to its own
destination and the card's note says that is what is happening. The `.panel-link` it originally
carried pointed at Abdomen alone and was removed for exactly this reason.

Every other card's topics do sit in one section, so they take the arrow. Respiratory was the
odd one out in the other direction until 2026-08-03 — per-bullet links but no arrow, on a card
whose topics are all under Thorax — and now matches its four siblings.

**The rule, if a card is ever added:** topics in one Publications section → one `.panel-link`
arrow, unlinked bullets. Topics scattered across sections → per-bullet links, no arrow, and a
note saying so. Do not make the six cards uniform for its own sake; the difference carries
information.

---

The original open list, kept for context. The numbering matches
[questions-for-project-lead.md](questions-for-project-lead.md) questions 1, 2, 2b, 3, 4, 5:

1. **The (inferred) panel mappings were acted on without confirmation.** The CNS,
   Cardiovascular, Respiratory and Gastrointestinal bullet edits below were applied on the
   assumption that the source document's unlabelled "Please edit to:" blocks map to those four
   panels in order. If the requester meant a different mapping, the bullets are on the wrong
   panels. This is the one with real consequences.
2. **The Respiratory panel was reworded despite this document saying "leave as is".** Its
   previous bullets were "Lung V20/V30 constraints", "Mean lung dose limits", "Pneumonitis risk
   models" and "Trachea/bronchi guidelines". The original QUANTEC has no trachea/bronchi review,
   and the lung review's own abstract states there are "no evident threshold 'tolerance
   dose–volume' levels", so naming V20/V30 as constraints overstated it. The panel now reads
   "Lung dose-volume effects / Symptomatic pneumonitis / Mean lung dose and DVH reduction /
   Dose-volume threshold analyses", every item taken from that paper's abstract, keywords or
   section headings.
2b. **The Gastrointestinal panel was reworded, not just added to.** This document asks only to
   *add* "Rectal toxicity" and "Esophageal dose-volume correlates". The four bullets already
   there ("Small bowel constraints", "Liver dose limits", "Kidney function preservation",
   "Gastric dose thresholds") were also rewritten, for the same reason as item 2 — none traced
   to a source. Same class of deviation as the Respiratory panel, and it was undisclosed until
   a review caught it.
3. **Three destinations now carry the QUANTEC name** — the QUANTEC tab, the QUANTEC section
   inside AllTEC Publications, and QUANTEC 2. This follows the request literally, but someone
   arriving cold and looking for a dose constraint has three plausible places to click.
4. **A sixth panel was added that this document does not ask for** — "Genitourinary and Pelvis"
   (bladder, rectal toxicity, penile bulb). Without it the bladder and penile bulb reviews had
   no signpost anywhere on the site, but it was implementer initiative, not a request.
5. **The Ear/cochlea review is filed under Head and Neck, not CNS.** `site-plan.md` lists it as
   "CNS: Ear"; this document puts "Cochlear dose thresholds" under Head and Neck and the QUANTEC
   2 site list does the same, so the site follows this document. Consequence: the CNS panel a
   user reaches from the home page's "CNS Tolerance" card has no hearing content.

Anything below this section is the original request text, unchanged.

## Home page (`index.html`)

In the "Key Resources & Areas of Focus" gallery:

- Move **Pediatric Guidelines** and **NTCP Modeling** to the right of the row.
- Add two new cards:
  - **GI/GU Toxicity** — 3–4 bullet lines, following the pattern of the other panels.
  - **Head and Neck** — dose-volume-response for xerostomia, hearing loss, edema/fibrosis and
    dysphagia.

## Resources tab (`resources.html`)

- Rename the tab from "Resources" to **QUANTEC**.

Panel edits:

- **Central Nervous System** (inferred) — replace bullets with:
  - Spinal cord dose-volume effects
  - Brain necrosis and cognitive decline
  - Brainstem injury
  - Optic nerves and chiasm dose-volume-response
- **Cardiovascular System** (inferred) — replace bullets with:
  - Heart dose constraints
  - Pericarditis
  - Cardiac mortality
  - Cardiac toxicity models
- **Respiratory System** (inferred) — "All good, leave as is."
- **Gastrointestinal System** (inferred) — add:
  - Rectal toxicity
  - Esophageal dose-volume correlates
- **Add a new panel** — heading **Head and Neck**, bullets:
  - Parotid gland salivary function preservation
  - Cochlear dose thresholds
  - Larynx/Pharynx dose-volume-response

A link to Publications is fine to keep, but note the Publications tab is being restructured
(below), so the link target may change.

## Publications tab (`publications.html`)

Rename to **AllTEC Publications** (or similar) with three sub-tabs:

| Sub-tab | Content |
|---|---|
| QUANTEC | Everything currently on the Publications page moves here. |
| HyTEC | Links below. |
| PENTEC | Links below. |

**HyTEC**

- Special issue of the *International Journal of Radiation Oncology Biology Physics*:
  <https://www.redjournal.org/issue/S0360-3016(20)X0015-0>
  (also at <https://www.sciencedirect.com/journal/international-journal-of-radiation-oncology-biology-physics/vol/110/issue/1>)
- Also available from the AAPM website: <https://www.aapm.org/pubs/HyTEC/>

**PENTEC**

- Website: <https://www.pentecradiation.org/>
- Special issue of the *International Journal of Radiation Oncology Biology Physics*:
  <https://www.redjournal.org/issue/S0360-3016(24)X0005-X>
  (also at <https://www.sciencedirect.com/journal/international-journal-of-radiation-oncology-biology-physics/vol/119/issue/2>)

## New tab: QUANTEC 2

Two sub-tabs: **Objectives** and **Sites/toxicities**.

### Objectives

> QUANTEC 2 objectives:
>
> Most of the data considered in the original QUANTEC reports came from the 3DCRT era.
> IMRT/VMAT technologies lead to DVHs distinctly different from 3DCRT. Consequently, toxicity
> data following IMRT/VMAT may, or may not, support recommendations made based on 3DCRT
> technology. In QUANTEC 2 dose-volume response and dose-volume threshold (DVH cut-off)
> analyses will be summarized. Toxicity data will be compared and contrasted between 3DCRT and
> IMRT/VMAT.
>
> Regional sensitivity or detailed substructure analyses have been performed for many sites,
> e.g., white matter tracts rather than whole brain. Treatment planning protocols including
> targeted sparing of organ-subvolumes or substructures will be summarized.
>
> Use of systemic therapy, in particular immunotherapy, has expanded since publication of the
> original QUANTEC reports. Systemic therapy serves as a mediator of the radiation response and
> this modulation will to be addressed when applicable.
>
> Machine learning in addition to traditional normal tissue complication probability models has
> become a common method to search for predictors of toxicity. Summary of these reports and
> their potential clinical use will be addressed.

### Sites/toxicities

- **CNS** — brain necrosis; brain cognition; brainstem; optic nerves/chiasm; brachial plexus
- **Head and neck** — cochlea/hearing loss; larynx; pharynx; salivary glands/xerostomia;
  mandible/necrosis; thyroid/hypothyroidism
- **Thorax** — lung; proximal airway; heart; esophagus; breast/fibrosis
- **Abdomen** — liver; stomach; small bowel; kidney
- **Pelvis and miscellaneous** — rectum; bladder; penile bulb and neurovascular bundle;
  bone marrow/hematologic toxicity; long bone/fracture
