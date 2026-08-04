# Transcription pilot — lung, heart, spinal cord

Status: **published.** The site owner ruled on 2026-08-03 to publish these on `/quantec/`. All
14 rows are live in the "Dose/volume/outcome data" section of that page, with the two governing
footnotes reproduced verbatim and each table attributed to its source page. This document
remains the transcription record and the verification evidence behind them.

## Source

Every value below comes from **one** source: Table 1, "QUANTEC Summary: Approximate
Dose/Volume/Outcome Data for Several Organs Following Conventional Fractionation", in

> Marks LB, Yorke ED, Jackson A, Ten Haken RK, Constine LS, Eisbruch A, Bentzen SM, Nam J,
> Deasy JO. "Use of Normal Tissue Complication Probability Models in the Clinic."
> *IJROBP* 2010;76(3 Suppl):S10–S19.

Local copy: `docs/papers/quantec-00-ntcp-models.pdf`. The table runs S15–S18; the rows
transcribed here are on **S15** (spinal cord) and **S16** (lung, heart).

This is the table the Guest Editor's introduction calls out as "a large summary table of
dose/volume/outcome data", and the one `site-plan.md` already links as the QUANTEC summary table.

## The two footnotes that govern every number below

Both are transcribed verbatim from S18. They are not optional context; they change how the
values may be used.

> **\*** All data are estimated from the literature summarized in the QUANTEC reviews unless
> otherwise noted. Clinically, these data should be applied with caution. Clinicians are
> strongly advised to use the individual QUANTEC articles to check the applicability of these
> limits to the clinical situation at hand. They largely do not reflect modern IMRT.

> **†** All at standard fractionation (i.e., 1.8–2.0 Gy per daily fraction) unless otherwise
> noted. Vx is the volume of the organ receiving ≥ x Gy. Dmax = Maximum radiation dose.

## Spinal cord — S15

Organ review: Kirkpatrick JP, van der Kogel AJ, Schultheiss TE, "Radiation Dose–Volume Effects
in the Spinal Cord", S42–S49 (`quantec-cns-spinal-cord.pdf`).

| Volume segmented | Irradiation type | Endpoint | Dose / dose-volume parameter | Rate | Notes (verbatim) |
|---|---|---|---|---|---|
| Partial organ | 3D-CRT | Myelopathy | Dmax = 50 Gy | 0.2% | Including full cord cross-section |
| Partial organ | 3D-CRT | Myelopathy | Dmax = 60 Gy | 6% | |
| Partial organ | 3D-CRT | Myelopathy | Dmax = 69 Gy | 50% | |
| Partial organ | SRS (single fraction) | Myelopathy | Dmax = 13 Gy | 1% | Partial cord cross-section irradiated |
| Partial organ | SRS (hypofraction) | Myelopathy | Dmax = 20 Gy | 1% | 3 fractions, partial cord cross-section irradiated |

## Lung — S16

Organ review: Marks LB, Bentzen SM, Deasy JO, et al., "Radiation Dose–Volume Effects in the
Lung", S70–S76 (`quantec-thorax-lung.pdf`).

| Volume segmented | Irradiation type | Endpoint | Dose / dose-volume parameter | Rate | Notes (verbatim) |
|---|---|---|---|---|---|
| Whole organ | 3D-CRT | Symptomatic pneumonitis | V20 ≤ 30% | <20% | For combined lung. Gradual dose response |
| Whole organ | 3D-CRT | Symptomatic pneumonitis | Mean dose = 7 Gy | 5% | Excludes purposeful whole lung irradiation |
| Whole organ | 3D-CRT | Symptomatic pneumonitis | Mean dose = 13 Gy | 10% | " |
| Whole organ | 3D-CRT | Symptomatic pneumonitis | Mean dose = 20 Gy | 20% | " |
| Whole organ | 3D-CRT | Symptomatic pneumonitis | Mean dose = 24 Gy | 30% | " |
| Whole organ | 3D-CRT | Symptomatic pneumonitis | Mean dose = 27 Gy | 40% | " |

## Heart — S16

Organ review: Gagliardi G, Constine LS, Moiseenko V, et al., "Radiation Dose–Volume Effects in
the Heart", S77–S85 (`quantec-thorax-heart.pdf`).

| Volume segmented | Irradiation type | Endpoint | Dose / dose-volume parameter | Rate | Notes (verbatim) |
|---|---|---|---|---|---|
| Pericardium | 3D-CRT | Pericarditis | Mean dose < 26 Gy | <15% | Based on single study |
| Pericardium | 3D-CRT | Pericarditis | V30 < 46% | <15% | |
| Whole organ | 3D-CRT | Long-term cardiac mortality | V25 < 10% | <1% | Overly safe risk estimate based on model predictions |

## Where the site's wording departs from the source — ruled 2026-08-03

The tables above are the verbatim transcription. The published tables differ from it in exactly
two ways, both owner decisions, both recorded here so the difference is never mistaken for a
transcription error.

1. **`SRS (hypofraction)` is published as `SRS (3 fraction)`.** The source's own Notes cell for
   that row says "3 fractions", so the number is the source's, not ours — this relabels using a
   fact the source states rather than introducing one. The transcription tables above keep the
   source's wording.
2. **That row's note is published as "Partial cord cross-section irradiated"**, dropping the
   leading "3 fractions," which the new label now carries. No information is lost; the wording
   is otherwise the source's.

3. **The column headed `Irradiation type` in the source is published as `Fractionation scheme`,
   and its `3D-CRT` value as `Conventional (1.8–2.0 Gy/fraction)`.** The dose-per-fraction figure
   is the source's: footnote † to Table 1 reads "All at standard fractionation (i.e., 1.8–2.0 Gy
   per daily fraction) unless otherwise noted", and the SRS rows are the "otherwise noted" ones.

   **Note what this trades away.** 3D-CRT is a delivery *technique*; conventional fractionation is
   a dose-per-fraction *schedule*. They are not synonyms, and the source's column recorded the
   former. Because the technique is what underpins the modern-IMRT caveat, it is preserved in the
   provenance line under each table — "The source records these rows as 3D-CRT (3-dimensional
   conformal radiotherapy)" — rather than being dropped.

### The modern-IMRT caveat is now stated only where a source says it

Table 1's `*` footnote ("They largely do not reflect modern IMRT") is a blanket statement across
every organ in the table. It remains quoted verbatim in the box above all three tables, which is
where a blanket statement belongs.

Beside the individual tables it appears **only for lung**, because only the lung review makes the
point about its own data (p. S72):

> Finally, it is likely that the MLD–RP relationship may have lower predictive power for
> "nonstandard" dose distributions not included in these analyses, for example after stereotactic
> body radiotherapy (SBRT), Intensity-Modulated Radiation Therapy (IMRT), or proton therapy.

**The spinal cord review was considered and rejected as a citation.** It contains a sentence
naming conformal techniques — "making application of these findings to highly conformal
radiotherapy techniques, such as stereotactic body RT (SBRT) or intensity-modulated proton
therapy, difficult" — but in context that is about extrapolating *partial-cord-volume animal
data*, inside the reirradiation discussion, and it names intensity-modulated **proton** therapy.
It is not a statement that the table's values do not reflect IMRT, and citing it as one would
misrepresent it. The heart review contains no such statement at all.

Presentation-only, no wording changed: columns whose value is identical in every row are hoisted
out of the grid into the table caption (lung, for instance, is "every row: whole organ, 3D-CRT,
endpoint symptomatic pneumonitis"), and cells identical across a contiguous group are merged.
The Rate column is deliberately **never** merged — spinal cord rows 4 and 5 are both 1%, but
that is a coincidence between two different techniques, and merging them would assert a grouping
the source does not make.

## Verification record

The protocol requires every number to be re-checked against the source by a separate pass. Two
*independent extraction methods* were run over the same PDF and their results compared:

1. `pdftotext -layout` — preserves visual column position
2. `pdftotext` (reading order) — preserves the PDF's internal text sequence

They agree on every value in all three tables. The agreement is meaningful because the two
methods fail differently: layout mode reconstructs columns geometrically and can bind a value to
the wrong row when a cell wraps; reading order cannot, but loses the visual grouping.

**One real ambiguity was caught this way and resolved.** In layout mode the lung block rendered
as five mean-dose rows against a vertically displaced rate column, admitting two readings:
7→5, 13→10, 20→20, 24→30, 27→40, or 7→5, 20→10, 27→20 with 30 and 40 orphaned. Layout mode alone
could not distinguish them. Reading order emitted the doses as one run (7, 13, 20, 24, 27) and
the rates as another (5, 10, 20, 30, 40), fixing the pairing as one-to-one. Had only layout mode
been used, a wrong pairing was a live possibility — a 20 Gy mean lung dose reads as 10%
pneumonitis instead of 20%.

### Transcription hazard worth recording

The PDFs encode `≤` and `≥` as characters that `pdftotext` emits as `#` and `$`. So the source
line `V20 # 30%` is **V20 ≤ 30%**, and `Grade $3 acute esophagitis` is **Grade ≥3**. Anyone
extending this to the other organs must convert these deliberately; read literally, `#` and `$`
silently drop the inequality direction.

## Flagged, not inferred

- **Lung, mean-dose rows.** The "Excludes purposeful whole lung irradiation" note is written
  once in the source, spanning the grouped mean-dose rows. It is reproduced above with `"` on
  the continuation rows rather than repeated as if separately stated.
- **Heart, second pericarditis row.** The Notes cell is empty in the source. Left empty; not
  back-filled from the row above.
- **Spinal cord SRS rows.** The source gives both the single-fraction and 3-fraction rows a rate
  of 1%. That is what it says; it is not a duplication error introduced here.
- **No values were taken from the three organ reviews themselves.** Only the cross-organ summary
  table was transcribed. The organ papers contain further dose-volume detail, NTCP fits and
  study-by-study tables that are *not* represented above — notably the lung paper's logistic fit
  (TD50 = 30.8 Gy, and a probit/Lyman n=1 fit giving TD50 = 31.4 Gy, m = 0.45), which is a
  different kind of statement from the binned rates in the summary table. Extending the pilot to
  those requires a separate decision about scope.

## The design question — ruled 2026-08-03

**Ruling: publish on `/quantec/`.** The site owner chose this over keeping the values local or
limiting the page to endpoint/parameter names. Recorded here so it is not re-flagged as a
defect; the reasoning argued against it is kept below so the trade-off stays visible.

What shipped as a result:

- The three tables live in `/quantec/#data`, reachable from the CNS, Cardiovascular and
  Respiratory cards.
- Both QUANTEC footnotes are reproduced verbatim above the tables, including "Clinicians are
  strongly advised to use the individual QUANTEC articles" and "They largely do not reflect
  modern IMRT".
- Each table carries its source page and a link to the organ review.
- The lung table carries an added line noting that the review finds no evident threshold
  tolerance dose–volume levels, so those values are points on a gradual dose response rather
  than thresholds. This keeps ruling 2's substance intact while stating the numbers.
- `quantec.html`'s "How to use this page" prose no longer claims values are never restated.

### The argument that was made against, and overruled

`CLAUDE.md` records the site's current design as deliberate:

> The site states no dose values: each organ topic routes to the review carrying the constraint,
> deliberately, so clinicians plan from the paper rather than our summary of it.

Publishing the tables above reverses that. Two things make this worth an explicit decision
rather than an assumption:

1. **QUANTEC's own authors argue against the summary being the endpoint.** The `*` footnote
   tells clinicians to "use the individual QUANTEC articles to check the applicability of these
   limits", and warns the data "largely do not reflect modern IMRT" — which in 2026 is most
   thoracic treatment. A table on the site is a summary of a summary the authors already
   qualified.
2. **The owner has already ruled once in this territory.** `update-requests.md` ruling 2 reverted
   "Lung V20/V30 constraints" as overstating the evidence, on the grounds that the lung review's
   abstract says there are "no evident threshold 'tolerance dose–volume' levels". The summary
   table's `V20 ≤ 30%` row is exactly that number. Publishing it re-raises a question that was
   settled the other way ten months ago.

None of this makes publishing wrong — it is a real editorial choice with a real upside, and the
values above are verified and ready. It was the site owner's call, and it was made: publish.
