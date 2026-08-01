# Pending site update requests

Transcribed verbatim from `UpdateRequests.docx` (dated 2025-07-16), which was an untracked
working file at the repo root.

The source document listed edits under bare headings like "Please edit to:" without naming the
panel. The section mapping below is *inferred* from the order matching the four organ panels on
what is now [constraints.html](../constraints.html).

## Implementation status

**Implemented on 2026-08-01**, in the branch that introduced `/constraints/` and `/quantec-2/`.
Three things about that are still open and should not be treated as settled:

1. **The (inferred) panel mappings were acted on without confirmation.** The CNS,
   Cardiovascular, Respiratory and Gastrointestinal bullet edits below were applied on the
   assumption that the source document's unlabelled "Please edit to:" blocks map to those four
   panels in order. That assumption is still unconfirmed. If the requester meant a different
   mapping, the bullets are on the wrong panels.
2. **Two requested renames were deliberately not made.** The constraints page is labelled
   "Constraints", not "QUANTEC", and the publications page kept "Publications" rather than
   "AllTEC Publications". Reason: a literal reading produced three destinations named some
   variant of QUANTEC, and the longer labels overflowed the header — six nav items measured
   766px against a 594px budget at 1280px, wrapping the header to two rows. The sub-tabs were
   delivered as in-page section links rather than a dropdown.
3. **The Respiratory panel was reworded despite this document saying "leave as is".** Its
   previous bullets ("Lung V20/V30 constraints", "Mean lung dose limits", "Pneumonitis risk
   models", "Trachea/bronchi guidelines") asserted specifics that trace to no source, and
   trachea/bronchi is not an organ the original QUANTEC covered. Removing them was chosen over
   preserving them; that is a direct conflict with the request and needs a ruling.

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
