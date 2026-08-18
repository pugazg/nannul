# நன்னூல் — Nannūl

A source-faithful digital repository for **பவணந்தி முனிவர் அருளிய நன்னூல்**, one of the major works of Tamil grammatical tradition.

## Current controlling digital source

- **Project Madurai eText:** `pmuni0147`
- Source page: https://www.projectmadurai.org/pm_etexts/utf8/pmuni0147.html
- Format: Tamil Unicode eText
- Work: **நன்னூல்**
- Author: **பவணந்தி முனிவர்**
- Source edition note: the Project Madurai header states that the Unicode text was made to conform to the edition edited by Mani Thirunavukkarasu Mudaliar and published by Vavilla Ramasamy Sastrulu & Sons, Madras, 1926.

The Project Madurai header and provenance must be preserved whenever its supplied text is archived or redistributed.

## Repository principles

1. Preserve source text separately from editorial or normalized representations.
2. Do not silently modernize spelling, punctuation, segmentation, or wording.
3. Record provenance for every imported source.
4. Keep commentary, interpretation, translations, and computational data separate from the canonical Tamil text.
5. Make every grammatical unit addressable by stable identifiers.
6. Treat source discrepancies as audit findings, not opportunities for silent correction.

## Repository layout

```text
nannul/
├── README.md
├── docs/
│   └── ARCHIVAL_GUIDELINES.md
├── sources/
│   └── project-madurai/
│       └── pmuni0147/
│           ├── README.md
│           ├── CURRENT_WEB_HEADER.txt
│           └── SOURCE_MANIFEST.yml
├── text/
│   └── tamil/
│       ├── 00-sirappuppayiram.md
│       ├── 01-pothuppayiram/
│       ├── 02-ezhuththathikaram/
│       │   ├── 02-01-ezhuththu-iyal/
│       │   ├── 02-02-pathaviyal/
│       │   ├── 02-03-uyireetru-punariyal/
│       │   ├── 02-04-meyyeetru-punariyal/
│       │   └── 02-05-urupu-punariyal/
│       └── 03-sollathikaram/
│           └── 03-01-peyariyal/
├── structure/
│   ├── README.md
│   └── sections.yml
├── indexes/
├── data/
├── commentaries/
├── translations/
│   └── en/
└── audit/
    ├── README.md
    ├── SOURCE_VARIANTS.md
    ├── CANONICAL_INGEST_056_127.md
    ├── CANONICAL_INGEST_128_150.md
    ├── CANONICAL_INGEST_151_203.md
    ├── CANONICAL_INGEST_204_239.md
    ├── CANONICAL_INGEST_240_257.md
    ├── EZHUTHTHATHIKARAM_COMPLETION.md
    └── CANONICAL_INGEST_258_319.md
```

## Source structure

The Project Madurai eText presents:

- சிறப்புப்பாயிரம்
- பொதுப்பாயிரம் — நூற்பா 1–55
- எழுத்ததிகாரம் — நூற்பா 56–257
- சொல்லதிகாரம் — நூற்பா 258–462

Detailed இயல்-level ranges are recorded in `structure/sections.yml`.

## Canonical status

- சிறப்புப்பாயிரம் — **canonicalized**
- பொதுப்பாயிரம் 1–55 — **canonicalized**
- எழுத்ததிகாரம் 56–257 — **canonicalized and audited in full**
  - எழுத்து இயல் 56–127 — complete
  - பதவியல் 128–150 — complete
  - உயிரீற்றுப் புணரியல் 151–203 — complete
  - மெய்யீற்றுப் புணரியல் 204–239 — complete
  - உருபு புணரியல் 240–257 — complete
- சொல்லதிகாரம் 258–462:
  - பெயரியல் 258–319 — **canonicalized and audited**
  - வினையியல் 320–351 — **next**
  - பொதுவியல் 352–419 — pending
  - இடையியல் 420–441 — pending
  - உரியியல் 442–462 — pending

Current canonical boundary: **நூற்பா 319**.

## Documented source-version findings

The controlling current webpage omits displayed numbered units at:

- 73 — between 72 and 74;
- 176 — between 175 and 177.

The canonical text preserves those source states and does not import the historical-witness readings.

The historical Project Madurai mirror also has a numbering anomaly around 240–242. The current webpage displays **240, 241, 242** continuously; that sequence is canonical and has been applied in `2.5 உருபு புணரியல்`.

The controlling webpage displays **258–319 continuously** in பெயரியல், with no additional numbering discrepancy observed.

See `audit/SOURCE_VARIANTS.md`, `audit/EZHUTHTHATHIKARAM_COMPLETION.md`, and `audit/CANONICAL_INGEST_258_319.md`.

## Next canonical activity

Proceed with **3.2 வினையியல், நூற்பாக்கள் 320–351**, under சொல்லதிகாரம், using the current Project Madurai Unicode webpage as the controlling witness.

The complete raw current webpage has not yet been vendored byte-for-byte into the repository; provenance/header material is preserved under `sources/`, and canonical transcription proceeds directly against the controlling webpage with batch audit records.
