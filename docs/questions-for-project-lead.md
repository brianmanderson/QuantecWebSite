# Questions for the project lead

The site has been updated from the requests in `UpdateRequests.docx` (now transcribed as
[update-requests.md](update-requests.md)). Six points could not be settled from the document
alone. Each one below says what the site currently does, so you can confirm or correct it
without needing to look at the code.

Answers can go straight back into this file, or reply however is easiest and they will be
recorded here and in `update-requests.md`.

---

## 1. Which panel does each set of bullets belong to?

**Why we're asking:** in the request document, four sets of bullet edits appear under bare
headings reading "Please edit to:" — none of them names which panel it applies to. We matched
them to the panels *in the order they appear*. If that guess is wrong, the bullets are on the
wrong organ systems.

This is the one with real consequences, so it is worth a careful look.

| Panel on the site | Bullets it now shows |
|---|---|
| Central Nervous System | Spinal cord dose-volume effects · Brain necrosis and cognitive decline · Brainstem injury · Optic nerves and chiasm dose-volume-response |
| Cardiovascular System | Heart dose constraints · Pericarditis · Cardiac mortality · Cardiac toxicity models |
| Respiratory System | see question 2 |
| Gastrointestinal | Esophageal dose-volume correlates · Liver dose-volume effects · Stomach and small bowel · Kidney dose-volume effects · Rectal toxicity — **see question 2b, this panel was also reworded** |
| Head and Neck *(new)* | Parotid gland salivary function preservation · Cochlear dose thresholds · Larynx/Pharynx dose-volume-response |

**Question:** is that the mapping you intended?

---

## 2. The Respiratory panel

**Why we're asking:** the request says "All good — leave as is" for Respiratory. But the four
bullets that were there could not be supported:

- *"Lung V20/V30 constraints"* — the QUANTEC lung review's own abstract says "there are no
  evident threshold 'tolerance dose–volume' levels", so naming V20/V30 as constraints reads as
  more definite than the paper.
- *"Trachea/bronchi guidelines"* — the original QUANTEC has no trachea or bronchi review.
- *"Mean lung dose limits"* and *"Pneumonitis risk models"* were fine in substance.

The panel now reads: **Lung dose-volume effects · Symptomatic pneumonitis · Mean lung dose and
DVH reduction · Dose-volume threshold analyses** — every one drawn from the lung review's own
abstract, keywords and section headings.

**Question:** is that an acceptable reading of "leave as is", or would you rather have the
original four back as written?

---

## 2b. The Gastrointestinal panel was reworded too, not just added to

**Why we're asking:** the request for this panel was to **add** two lines — "Rectal toxicity"
and "Esophageal dose-volume correlates". We did that, but we also rewrote the four that were
already there, for the same reason as question 2: none of them could be traced to a source.

| Was | Is now |
|---|---|
| Small bowel constraints | Stomach and small bowel |
| Gastric dose thresholds | *(merged into the line above)* |
| Liver dose limits | Liver dose-volume effects |
| Kidney function preservation | Kidney dose-volume effects |
| — | Esophageal dose-volume correlates *(requested)* |
| — | Rectal toxicity *(requested)* |

The new wording tracks the QUANTEC paper titles more closely and states no dose figure, but it
is a change you did not ask for.

**Question:** keep the reworded bullets, or restore your original four alongside the two
additions?

---

## 3. Tab names

The request asked for "Resources" → **QUANTEC** and "Publications" → **AllTEC Publications**.
Both are now in place.

Worth flagging: the site now has three destinations carrying the QUANTEC name — the **QUANTEC**
tab (dose constraints by organ), a **QUANTEC** section inside AllTEC Publications (the 2010
papers), and the **QUANTEC 2** tab. Someone arriving cold and looking for a dose constraint has
three plausible places to click.

**Question:** is that acceptable, or would you like the constraints tab named something that
distinguishes it — "Dose Constraints" or "Constraints by Organ", say?

---

## 4. A sixth panel we added

The request names four panels to edit plus one new one (Head and Neck) — five in all. We added a
sixth, **Genitourinary and Pelvis** (bladder, rectal toxicity, penile bulb), because otherwise the
bladder and penile bulb reviews had no signpost anywhere on the site — they were reachable only
by scrolling the publications list.

**Question:** keep it, or drop it?

---

## 5. Where does the Ear / cochlea review belong?

The design brief lists the ear review under **CNS: Ear**. The update request puts "Cochlear dose
thresholds" under **Head and Neck**, and the QUANTEC 2 site list does the same. The site
currently follows the update request — the ear paper sits under Head and Neck.

The effect: someone clicking "CNS Tolerance" on the home page finds no hearing content there.

**Question:** Head and Neck (current), or move it back under CNS?

---

## Not a question — one thing you should know

The site links the penile bulb review as
`redjournal.org/article/S0360-3016(09)03294-5`. The design brief gave the *same* URL for both
rectum and penile bulb, which looked like a copy/paste error, and for a while it appeared
someone had substituted a guess.

We checked both against the journal. `03294-5` is "Radiation Dose–Volume Effects and the Penile
Bulb" (Roach III et al., S130–S134) and `03291-X` is the rectal injury review. Both entries on
the site are correct; it was the brief that had the duplicate. No action needed — recorded so
nobody re-opens it.

The same check turned up four transcription slips in the brief, now corrected on the site and in
our copy of it: **Mary** K. Martel (not May), "A **Users** Guide", "Scientific **Issues**", and
"Use of Normal Tissue **Complication** Probability Models in the Clinic".
