# Transcription pilot — lung, heart, spinal cord

Status: **published, and since extended to the whole table.** The site owner ruled on 2026-08-03
to publish these on `/quantec/`. The pilot's 14 rows went live first; the same protocol was then
run over the rest of Table 1, and all **18 organ entries / 62 dose rows** are now in the
"Dose/volume/outcome data" section of that page, with the four governing footnotes reproduced
verbatim and each table attributed to its source page. This document remains the transcription
record and the verification evidence behind them — the sections below are in the order the work
was done, so the pilot's three organs come first and the extensions follow.

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

## The four footnotes that govern the numbers below

All four are transcribed verbatim from S18. They are not optional context; they change how the
values may be used and what the notation means. The site reproduces all four in the box above
the tables.

> **\*** All data are estimated from the literature summarized in the QUANTEC reviews unless
> otherwise noted. Clinically, these data should be applied with caution. Clinicians are
> strongly advised to use the individual QUANTEC articles to check the applicability of these
> limits to the clinical situation at hand. They largely do not reflect modern IMRT.

> **†** All at standard fractionation (i.e., 1.8–2.0 Gy per daily fraction) unless otherwise
> noted. Vx is the volume of the organ receiving ≥ x Gy. Dmax = Maximum radiation dose.

> **‖** Dx = minimum dose received by the "hottest" x% (or x cc's) of the organ.

> **††** Classic Radiation induced liver disease (RILD) involves anicteric hepatomegaly and
> ascites, typically occurring between 2 weeks and 3 months after therapy. Classic RILD also
> involves elevated alkaline phosphatase (more than twice the upper limit of normal or baseline
> value).

The first two govern every organ in the table. **‖** and **††** were added to the site when the
abdomen and pelvis tables landed and the notation they define came into use — ‖ for the liver
`D100`, penile bulb `D90`/`D60–70`, brain stem `D1–10 cc` and stomach `D100` rows, †† for the
liver endpoint. They were re-verified against S18 on 2026-08-03 and recorded here, because for a
while the site carried four footnotes while this record documented two.

Table 1 has five further footnotes, all organ-specific rather than governing. Each is carried on
the site next to the table it belongs to rather than in the box: **‡** Non-TBI (kidney, in the
caption); **§** with combined chemotherapy (small bowel, in the caption); **¶** severe xerostomia
depends on other factors including submandibular dose (parotid, in the provenance line);
**\*\*** estimated by Dr. Eisbruch (larynx edema rows, in the provenance line); **‡‡** the optic
neuropathy cases in the 55–60 Gy range received ≥59 Gy, excluding pituitary-tumour patients
(optic nerve, in the provenance line).

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

## Extension to CNS, head and neck, and thorax — 2026-08-03

Eight further organs transcribed from the same Table 1, by the same two-method protocol. Rows
below are the verbatim transcription; page is where each row appears.

**Brain** (S15) — whole organ, endpoint symptomatic necrosis. 3D-CRT: Dmax <60 Gy → <3%;
Dmax = 72 Gy → 5%; Dmax = 90 Gy → 10% (one note across the three: "Data at 72 and 90 Gy,
extrapolated from BED models"). SRS single fraction: V12 <5–10 cc → <20%, "Rapid rise when
V12 > 5–10 cc".

**Brain stem** (S15) — whole organ, endpoint permanent cranial neuropathy or necrosis.
Irradiation type "Whole organ": Dmax <54 Gy → <5%. 3D-CRT: D1–10 cc ≤59 Gy → <5%;
Dmax <64 Gy → <5%, "Point dose <<1 cc". SRS single fraction: Dmax <12.5 Gy → <5%, "For patients
with acoustic tumors".

**Optic nerve / chiasm** (S15) — whole organ, endpoint optic neuropathy. 3D-CRT: Dmax <55 Gy →
<3%; Dmax 55–60 Gy → 3–7%; Dmax >60 Gy → >7–20% (one note across the three: "Given the small
size, 3D CRT is often whole organ‡‡"). SRS single fraction: Dmax <12 Gy → <10%.

**Cochlea** (S15) — whole organ, endpoint sensory neural hearing loss. 3D-CRT: mean dose ≤45 Gy
→ <30%, "Mean dose to cochlear, hearing at 4 kHz". SRS single fraction: prescription dose ≤14 Gy
→ <25%, "Serviceable hearing".

**Parotid** (S15–S16) — 3D-CRT, endpoint long-term parotid salivary function reduced to <25% of
pre-RT level. Bilateral whole parotid glands: mean dose <25 Gy → <20%, "For combined parotid
glands¶". Unilateral whole parotid gland: mean dose <20 Gy → <20%, "For single parotid gland.
At least one parotid gland spared to <20 Gy¶". Bilateral whole parotid glands: mean dose <39 Gy
→ <50%, "For combined parotid glands (per Fig. 3 in paper)¶".

> **The third parotid row was missed on the first pass, in both the page and this record**, and
> was caught by an independent review on 2026-08-03. The cause is worth remembering: the parotid
> block is the only organ whose rows straddle the S15/S16 page break, and the extraction that
> built this entry stopped at the page boundary. The omission dropped the entire 50% risk level
> for parotid while the page claimed to publish every organ entry.
>
> **How to avoid repeating it:** when transcribing a table that spans pages, extract each page
> and then check the top of the *next* page for continuation rows before moving on. S17 and S18
> were re-checked afterwards and both begin with a fresh organ header, so parotid was the only
> organ affected.

**Pharynx** (S16) — pharyngeal constrictors, irradiation type "Whole organ", endpoint
symptomatic dysphagia and aspiration. Mean dose <50 Gy → <20%, "Based on Section B4 in paper".

**Larynx** (S16) — whole organ, 3D-CRT. Vocal dysfunction: Dmax <66 Gy → <20%, "With
chemotherapy, based on single study (see Section A4.2 in paper)". Aspiration: mean dose <50 Gy →
<30%, "With chemotherapy, based on single study (see Fig. 1 in paper)". Edema: mean dose <44 Gy →
<20%; V50 <27% → <20% (one note across the two edema rows, "Without chemotherapy, based on
single study in patients without larynx cancer\*\*"). The first two notes were omitted from this
record on the first pass though the page carried them correctly — noted so nobody later
"corrects" the page down to the record.

**Esophagus** (S16) — whole organ, 3D-CRT. Grade ≥3 acute esophagitis: mean dose <34 Gy → 5–20%,
"Based on RTOG and several studies". Grade ≥2 acute esophagitis: V35 <50%, V50 <40%, V70 <20%,
each → <30% (one note across the three: "A variety of alternate threshold doses have been
implicated. Appears to be a dose/volume response").

Footnote markers above are Table 1's own: ‡‡ records that the optic neuropathy cases in the
55–60 Gy range received ≥59 Gy and that patients with pituitary tumours are excluded; ¶ that
severe xerostomia depends on other factors including submandibular dose; \*\* that the larynx
edema rows are an estimate by Dr Eisbruch. All three are reproduced on the site next to their
tables.

### The "Irradiation type" column had to be split — ruled 2026-08-03

The pilot published that column as `Fractionation scheme` with `3D-CRT` rendered as
`Conventional (1.8–2.0 Gy/fraction)`. **That does not generalise.** Four organs carry values in
that column which are not fractionation schemes at all: brain stem row 1 and pharynx read
"Whole organ", liver reads "3D-CRT or Whole organ", kidney "Bilateral whole organ or 3D-CRT".

The column is therefore split into **Technique** (the source's value verbatim) and
**Fractionation** (conventional / single fraction / 3 fractions, per footnote †). Nothing is
reinterpreted and both facts are stated. Cord, lung and heart were migrated to the same scheme.

### Pelvis — 2026-08-03

**Rectum** (S18) — whole organ, 3D-CRT, prostate cancer treatment. The five constraints
V50 <50%, V60 <35%, V65 <25%, V70 <20%, V75 <15% are **one set**, not five independent rows.
The rectum review settles it: they are "a conservative starting point for 3D treatment planning",
and following them "should limit Grade ≥2 late rectal toxicity to <15% and the probability of
Grade ≥3 late rectal toxicity to <10% for prescriptions up to 79.2 Gy in standard 1.8- to 2-Gy
fractions". The review adds they "have yet to be validated as 'relatively-safe'". Table 1 alone
was ambiguous here — it renders the endpoint/rate pair alongside each of the five dose lines,
which reads equally well as five rows with individual rates. The organ paper resolved it.

**Bladder** (S18) — whole organ, 3D-CRT, endpoint Grade ≥3 late RTOG. Dmax <65 Gy → <6%,
"Bladder cancer treatment…". V65 ≤50%, V70 ≤35%, V75 ≤25%, V80 ≤15% → **no rate given**.
That blank is real, not an extraction failure: the bladder review offers those limits "in the
absence of any reliable data", citing the conventional-fractionation arm of RTOG 0415. The site
prints "Not stated" rather than an empty cell, so the absence cannot be mistaken for an omission
on our side.

**Penile bulb** (S18) — whole organ, 3D-CRT, endpoint severe erectile dysfunction. Mean dose to
95% of gland <50 Gy → <35%; D90 <50 Gy → <35%; D60–70 <70 Gy → <55%.

### Abdomen — 2026-08-03 (completes the table)

**Liver** (S17) — endpoint classic RILD throughout. Whole liver − GTV: mean dose <30–32 Gy →
<5% and <42 Gy → <50% ("Excluding patients with pre-existing liver disease or hepatocellular
carcinoma…"); mean dose <28 Gy → <5% and <36 Gy → <50% ("In patients with Child-Pugh A
pre-existing liver disease or hepatocellular carcinoma, excluding hepatitis B reactivation as an
endpoint"). SBRT: <13 Gy/3 fx primary, <18 Gy/6 fx primary, <15 Gy/3 fx metastases, <20 Gy/6 fx
metastases, all → <5%. >700 cc of normal liver: Dmax <15 Gy → <5%, critical-volume based.

The SBRT rows were the ambiguous ones — four doses and four notes, interleaved. **The liver
review confirms the pairing verbatim**: "< 13 Gy for primary liver cancer, in three fractions
< 18 Gy for primary liver cancer, in six fractions < 15 Gy for liver metastases, in three
fractions < 20 Gy for liver metastases, in six fractions", plus "≥ 700 mL of normal liver
receives ≤ 15 Gy in three to five fractions".

**Kidney** (S17) — bilateral whole kidney (non-TBI, footnote ‡), endpoint clinically relevant
renal dysfunction. Mean dose <15–18 Gy → <5%; mean dose <28 Gy → <50%; V12 <55%, V20 <32%,
V23 <30%, V28 <20% → <5%, "For combined kidney".

Row 3 was flagged unresolved in the previous pass and is **now resolved**: the kidney review's
Table 5 is headed "Suggested dose–volume constraints for estimated risk of <5%" and carries
**all four** constraints, each attributed to a study — V12 <55% (Welz et al.), V20 <32% (Jansen
et al.), V23 <30% and V28 <20% (Nevinny-Stickel et al.).

> **Corrected 2026-08-03 after an independent review.** This record and the site previously said
> Table 5 listed only V12 and V28, and that V20 and V23 "appear in the summary table only". That
> was wrong: all four are in Table 5. The error came from asserting a negative on the strength of
> an extraction window that had simply cut off before the remaining rows — the `sed` range used
> to read Table 5 ended mid-table. **Never conclude "the source does not say X" from an
> extraction that merely did not show X**; re-extract with the range widened, or search the whole
> document for the term, before writing an absence down.

**Stomach** (S17) — whole organ, endpoint ulceration. D100 <45 Gy → <7%. The organ review states
no comparable predictive model of acute toxicity is available for stomach.

**Small bowel** (S17) — 3D-CRT, endpoint Grade ≥3 acute toxicity with combined chemotherapy
(footnote §). Individual small bowel loops: V15 <120 cc → <10%. Entire potential space within
the peritoneal cavity: V45 <195 cc → <10%. Both confirmed by the organ review: "V15 = 120 cc if
individual bowel loops are outlined or V45 = 195 cc if entire peritoneal potential space of
bowel is outlined".

**The Technique / Fractionation split earned itself here.** Liver is the only organ whose
fractionation genuinely varies within one table — 3, 6, and 3–5 fractions alongside conventional
rows. Under the pilot's single "Fractionation scheme" column those rows could not have been
expressed without either dropping the technique or inventing a combined label.

### Transcription complete

All **18 organ entries** in Table 1 are transcribed and published: brain, brain stem, optic
nerve/chiasm, spinal cord, cochlea, parotid, pharynx, larynx, lung, heart, esophagus, liver,
kidney, stomach, small bowel, rectum, bladder, penile bulb. 62 dose rows across five body-system
groups.

### Superseded — was "still to transcribe"

Abdomen (liver, stomach/small bowel, kidney) and pelvis (rectum, bladder, penile bulb). Kidney
is partly resolved: rows 1 and 2 are cross-confirmed by the kidney review, which states "a
threshold dose for RT injury of 15 Gy with a 5% and 50% risk of injury at 5 years for
whole-kidney RT of 18 Gy and 28 Gy, respectively" — matching mean dose <15–18 → <5% and mean
dose <28 → <50%. **The third kidney row is not yet resolved**: whether V12 <55%, V20 <32%,
V23 <30%, V28 <20% are one row of alternatives or several, and how they pair to rates, cannot be
settled from the text extraction and must not be guessed.

## Where the site's wording departs from the source — ruled 2026-08-03

The tables above are the verbatim transcription. The published tables differ from it in the ways
listed below, all owner decisions, all recorded here so the difference is never mistaken for a
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

   (Superseded in part by the Technique / Fractionation split ruled later the same day, above:
   the source's `Irradiation type` value is now published verbatim in a **Technique** column and
   the fractionation schedule stated separately. Kept here because the provenance-line convention
   it established is still in force.)

4. **The Technique column no longer distinguishes "Whole organ" from "3D-CRT" — every
   conventional-fractionation row now reads `3D-CRT`.** Owner decision, 2026-08-03, for
   readability across the 18 tables. Five organs carried a technique value that was not plain
   `3D-CRT`, and all five are now published as `3D-CRT`:

   | Organ | Source's `Irradiation type` | Published as |
   |---|---|---|
   | Brain stem | `Whole organ` (Dmax <54 Gy row only) | `3D-CRT` |
   | Pharynx | `Whole organ` | `3D-CRT` |
   | Liver | `3D-CRT or Whole organ` (both <5% rows) | `3D-CRT` |
   | Kidney | `Bilateral whole organ or 3D-CRT`; `Bilateral whole organ` | `3D-CRT` |
   | Stomach | `Whole organ` | `3D-CRT` |

   **What this trades away, and what protects it.** The source's column distinguished data drawn
   from whole-organ irradiation from data drawn from partial-organ conformal treatment; that
   distinction is gone from the grid. Two things keep it recoverable. Each of the five provenance
   lines now names the source's own value verbatim — for kidney, all three of them. And the
   *volume* irradiated is a different column and was **not** touched: "whole organ" still appears
   in the Volume segmented column and in the captions that hoist it (brain, brain stem, optic
   nerve, cochlea, larynx, lung, esophagus, stomach, rectum, bladder, penile bulb; heart's
   `Whole organ` row; kidney's "bilateral whole kidney"). **Anyone applying this ruling further
   must not confuse the two columns** — collapsing Volume segmented would destroy a clinical
   fact, not a label.

   The optic nerve table keeps the source's note "Given the small size, 3D-CRT is often whole
   organ", which is the source's own wording and now reads as support for the collapse.

5. **Rows are ordered by technique, then by number of fractions; identical adjacent cells are
   merged.** Owner decision, 2026-08-03, same request as 4. Presentation only — no value, note
   or pairing changed.

   Only the **liver** table's row order actually moved. Its SBRT block was interleaved in the
   source (3 fx, 6 fx, 3 fx, 6 fx) and is now grouped 3 fx (13 Gy primary, 15 Gy metastases),
   6 fx (18 Gy primary, 20 Gy metastases), 3–5 fx (Dmax 15 Gy). Every dose keeps the note it
   came with; the pairing is the one the liver review confirms verbatim, quoted in the Abdomen
   section above. Its provenance line states that the order is not the source's.

   Merges added: liver (Volume across the eight `Whole liver − GTV` rows, Technique across the
   four 3D-CRT and five SBRT rows, Fractionation within each fraction count); brain stem (the
   three conventional rows, now one group); spinal cord (Technique `SRS` across its single- and
   3-fraction rows); larynx (`Edema` endpoint ×2); esophagus (`Grade ≥2 acute esophagitis`
   endpoint ×3).

   Three tables lost their Technique column entirely to the caption, because ruling 4 left it
   with one value: **kidney** (Technique and Fractionation both), **pharynx** and **stomach**.
   That is the convention below — a column identical in every row belongs in the caption — and
   applying it to only some of the three was itself caught as an inconsistency by review: stomach
   would have shown a grid cell implying a per-row distinction that a one-row table cannot have,
   while kidney showed the same collapsed value in its caption. Brain stem and liver keep the
   column, because SRS/SBRT rows make it genuinely vary.

   **The Rate column is still never merged**, for the reason recorded below. The same reasoning
   blocked one further merge: the two spinal cord SRS rows now carry identical *note* text, but
   only because ruling 2 above moved "3 fractions," out of the 3-fraction row's note. The source
   wrote two different notes there, so merging them would assert a grouping the source does not
   make. They are left as two cells.

   **One CSS rule had to change with them** (`assets/css/style.css`). Row separators were drawn
   on the bottom of each cell, with `tbody tr:last-child td` clearing them on the last row. A
   merged cell belongs to the row it *starts* in, so that selector cannot reach one spanning into
   the last row, and six tables drew a 1px stub across part of their bottom edge — four of them
   newly, from the merges above. Separators are now anchored to the top of each body cell, which
   is rowspan-proof. The comment on the rule says so; don't reintroduce `border-bottom` there.

### The modern-IMRT caveat is now stated only where a source says it

Table 1's `*` footnote ("They largely do not reflect modern IMRT") is a blanket statement across
every organ in the table. It remains quoted verbatim in the box above the tables, which is
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

They agree on every value in all 18 tables — the pilot's three, and the 15 added when the same
protocol was run over the rest of Table 1. The agreement is meaningful because the two methods
fail differently: layout mode reconstructs columns geometrically and can bind a value to the
wrong row when a cell wraps; reading order cannot, but loses the visual grouping.

Re-run in full on 2026-08-03 by an independent review with no knowledge of what had changed:
all 62 dose rows across the 18 tables re-checked against pp. S15–S18 by both methods, plus the
four footnote blockquotes, the kidney Table 5 provenance claim, the lung S72 quote, and all 19
citation links against the organ PDFs' own title pages. No discrepancy found.

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

- The tables live in `/quantec/#data`, grouped under five body-system headings and reachable
  from every organ card above them. (The pilot shipped three tables reached from the CNS,
  Cardiovascular and Respiratory cards; all 18 are now published and all six cards route to
  them.)
- The QUANTEC footnotes are reproduced verbatim above the tables, including "Clinicians are
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
2. **The owner has already ruled once in this territory.** `update-requests.md` ruling 2 restored
   "Lung V20/V30 constraints" verbatim, overruling an implementer rewrite that had removed it on
   the grounds that the lung review's abstract says there are "no evident threshold
   'tolerance dose–volume' levels". The summary table's `V20 ≤ 30%` row is exactly that number.

   > **Corrected 2026-08-03.** This point previously read that ruling 2 "reverted 'Lung V20/V30
   > constraints' as overstating the evidence" and that publishing "re-raises a question settled
   > the other way ten months ago". That inverted the ruling. Ruling 2 reverted the *rewrite*,
   > putting the owner's V20/V30 wording back — so the owner was content to name V20 as a
   > constraint, and this point in fact cut **in favour of** publishing the row, not against it.
   > Left in place rather than deleted because an argument recorded backwards is worth showing
   > as such: anyone re-reading this section was being told the owner had ruled against a thing
   > they had ruled for.

None of this makes publishing wrong — it is a real editorial choice with a real upside, and the
values above are verified and ready. It was the site owner's call, and it was made: publish.

**Postscript, 2026-08-03.** The tension in point 2 resolved itself once the table was live. The
card was asserting a V30 constraint that Table 1 does not carry, so the owner dropped V30 from
that bullet; it now reads "Lung V20 constraints". V20 stands, published and cited. The full
account is in ruling 2's follow-up in [update-requests.md](update-requests.md).
