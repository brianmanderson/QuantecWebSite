# Original site plan and source citations

Transcribed from `Website design.docx`, the brief that the current site was built from. It is
the authoritative source for the citations and links already on the site, and it contains
planned material that has **not** been built yet.

The .docx embedded three candidate hero images, extracted here so nothing depends on the binary:
[image1](assets/website-design-image1.png) (963×805),
[image2](assets/website-design-image2.png) (1141×737),
[image3](assets/website-design-image3.png) (831×235). The brief flags image3 as low resolution
("resolution is crap"). None of them are used on the site yet, and `docs/` is excluded from the
Jekyll build, so they are not published — moving one into `assets/images/` is what would put it
live, and doing so requires an entry in [CREDITS.md](../CREDITS.md) plus confirmation that the
site has the right to use it.

## Domain

- `quantecradiation.org`, registered through [Namecheap](https://www.namecheap.com).
- Layout inspiration: PENTEC's site.
- Wanted: a hero image, ideally a rotating set.
- Wanted: visual treatment for "In collaboration between AAPM, ASTRO and ESTRO". **Do not use
  the organization logos** — as of the brief this is only an agreement reached at the ASTRO
  kick-off meeting, nothing formal.

## Tab 1 after Home: QUANTEC

### Publication

QUANTEC (Quantitative Analysis of Normal Tissue Effects in the Clinic) reports were published as
a special issue of the *International Journal of Radiation Oncology Biology Physics* (Red
Journal), 2010, Vol. 76, No. 3, Supplement:
<https://www.redjournal.org/issue/S0360-3016(10)X0002-5>

The issue included 3 introductory, 16 organ-specific and 5 vision papers.

### QUANTEC objective

From the introductory paper "Use of normal tissue probability models in the clinic" — Lawrence B.
Marks, Ellen D. Yorke, Andrew Jackson, Randall K. Ten Haken, Louis S. Constine, Avraham Eisbruch,
Søren M. Bentzen, Jiho Nam, and Joseph O. Deasy; *IJROBP* 2010, Vol. 76, No. 3, Supplement,
pp. S10–S19:

> The Quantitative Analysis of Normal Tissue Effects in the Clinic (QUANTEC) review summarizes
> the currently available three-dimensional dose/volume/outcome data to update and refine the
> normal tissue dose/volume tolerance guidelines provided by the classic Emami et al. paper
> published in 1991. A "clinician's view" on using the QUANTEC information in a responsible
> manner is presented along with a description of the most commonly used normal tissue
> complication probability (NTCP) models. A summary of organ-specific dose/volume/outcome data,
> based on the QUANTEC reviews, is included.

### Introductory QUANTEC papers

| Paper | Authors | Link |
|---|---|---|
| Guest Editor's Introduction to QUANTEC: A User Guide | Lawrence B. Marks, Randall K. Ten Haken, May K. Martel | <https://www.redjournal.org/article/S0360-3016(09)03302-1/fulltext> |
| Quantitative Analyses of Normal Tissue Effects in the Clinic (QUANTEC): An Introduction to the Scientific Issue | Søren M. Bentzen, Louis S. Constine, Joseph O. Deasy, Avi Eisbruch, Andrew Jackson, Lawrence B. Marks, Randall K. Ten Haken, Ellen D. Yorke | <https://www.redjournal.org/article/S0360-3016(09)03300-8/fulltext> |
| Use of normal tissue probability models in the clinic | Lawrence B. Marks, Ellen D. Yorke, Andrew Jackson, Randall K. Ten Haken, Louis S. Constine, Avraham Eisbruch, Søren M. Bentzen, Jiho Nam, Joseph O. Deasy | <https://www.redjournal.org/article/S0360-3016(09)03288-X/fulltext> |

### Organs covered in the original QUANTEC

| Site | Link |
|---|---|
| CNS: Brain | <https://www.redjournal.org/article/S0360-3016(09)03287-8/fulltext> |
| CNS: Optic Nerve/Chiasm | <https://www.redjournal.org/article/S0360-3016(09)03284-2/fulltext> |
| CNS: Brain Stem | <https://www.redjournal.org/article/S0360-3016(09)03582-2/fulltext> |
| CNS: Spinal Cord | <https://www.redjournal.org/article/S0360-3016(09)03296-9/fulltext> |
| CNS: Ear | <https://www.redjournal.org/article/S0360-3016(09)03298-2/fulltext> |
| Head and Neck: Parotid | <https://www.redjournal.org/article/S0360-3016(09)03289-1/fulltext> |
| Head and Neck: Larynx/Pharynx | <https://www.redjournal.org/article/S0360-3016(09)03292-1/fulltext> |
| Thorax: Lung | <https://www.redjournal.org/article/S0360-3016(09)03293-3/fulltext> |
| Thorax: Heart | <https://www.redjournal.org/article/S0360-3016(09)03290-8/fulltext> |
| Thorax: Esophagus | <https://www.redjournal.org/article/S0360-3016(09)03283-0/fulltext> |
| Abdomen: Liver | <https://www.redjournal.org/article/S0360-3016(09)03295-7/fulltext> |
| Abdomen: Stomach/Small Bowel | <https://www.redjournal.org/article/S0360-3016(09)03286-6/fulltext> |
| Abdomen: Kidney | <https://www.redjournal.org/article/S0360-3016(09)03282-9/fulltext> |
| Pelvis: Bladder | <https://www.redjournal.org/article/S0360-3016(09)03285-4/fulltext> |
| Pelvis: Rectum | <https://www.redjournal.org/article/S0360-3016(09)03291-X/fulltext> |
| Pelvis: Penile Bulb | <https://www.redjournal.org/article/S0360-3016(09)03291-X/fulltext> |

Note: the brief gives the **same URL** for Pelvis: Rectum and Pelvis: Penile Bulb. That is
almost certainly a copy/paste error in the source document — verify the Penile Bulb DOI against
the Red Journal issue before relying on it, and do not silently substitute a guess.

**This has already gone wrong once.** [publications.html:243](../publications.html:243) links
Penile Bulb to `S0360-3016(09)03294-5` — a *third* value that appears in neither this document
nor `update-requests.md`. It entered in commit `0387d2d` ("fix broken links", 2026-06-07),
which appears to have resolved the duplicate above by substituting a plausible PII. It is live
on quantecradiation.org. Nobody should replace it with another guess: check the table of
contents of *IJROBP* 2010, Vol. 76, No. 3, Supplement, and record the confirmed PII here first.

### QUANTEC summary table

- <https://www.redjournal.org/article/S0360-3016(09)03288-X/fulltext>
- <https://en.wikibooks.org/wiki/Radiation_Oncology/Toxicity/QUANTEC>

### Planned: interviews with Lawrence Marks and Søren Bentzen

Questions drafted in the brief; answers not yet collected. Not built on the site.

1. What do you regard as the biggest success of the QUANTEC effort?
2. Anything you wish was included in the QUANTEC but was not?
3. QUANTEC has led to HyTEC, PENTEC, now re-irradiation effort and QUANTEC 2 are in progress.
   Did you see this happening when you had a QUANTEC kick-off workshop in Madison, Wisconsin in
   October of 2007?
4. We now know much more about tumor and normal tissue response. However, a common view is
   improvements in outcomes are a result of better imaging, including multi-modality, which
   allow to more accurately delineate target volumes and organs at risk, and better targeting,
   due to rapid acceptance of IGRT. What do you see as a potential next big step to more than
   incrementally improve cancer care outcomes?
5. Lists of authors between QUANTEC, HyTEC and PENTEC show lots of commonalities. What attracts
   and motivates oncologists, physicists and biostatisticians to participate in these efforts?
6. As I understand, QUANTEC 2 will attract new, younger oncologists, physicists and
   biostatisticians. What advice would you like to give them to make QUANTEC 2 a success?
7. Anything else you may want to share?

## Tab 2 after Home: QUANTEC 2

Not built yet. See also the later, revised wording in [update-requests.md](update-requests.md),
which supersedes this section where the two disagree.

### Rationale for a QUANTEC update

> Most of the data considered in the original QUANTEC reports came from the 3DCRT era. IMRT/VMAT
> technologies lead to DVHs distinctly different from 3DCRT. Consequently, toxicity data
> following IMRT/VMAT may, or may not, support recommendations made based on 3DCRT technology.
>
> For certain sites regional sensitivity or detailed substructure analyses have been performed,
> e.g., white matter tracts rather than treating brain as a single organ at risk.
> Recommendations including targeted sparing of organ-subvolumes at risk may further inform
> treatment planning.
>
> Use of systemic therapy, in particular immunotherapy, has expanded since publication of the
> original QUANTEC reports. Systemic therapy serves as a mediator of the radiation response and
> this modulation needs to be addressed.
>
> Machine learning in addition to traditional normal tissue complication probability models has
> become a common method to search for predictors of toxicity. Summary of these reports and
> their potential clinical use should be addressed in the QUANTEC update.

### Sites/toxicities planned for an update

Brain · Brainstem · Cochlea/hearing loss · Larynx/Pharynx · Optic Nerves/Chiasm ·
Parotid/Xerostomia · Lung · Heart · Esophagus · Liver · Stomach, Small Bowel · Kidney · Rectum ·
Bladder · Penile Bulb

### New sites/toxicities

Mandible/necrosis · Bone marrow/hematologic toxicity · Long bone/fracture · Breast/fibrosis ·
Thyroid/hypothyroidism · Brachial plexus/plexopathy

### Kick-off meeting

Took place during the ASTRO annual meeting, September 30th, 2025, and included representation
from AAPM, ASTRO and ESTRO.

### Timeline

"QUANTEC 2 is planned to be completed before radiotherapy becomes obsolete."
