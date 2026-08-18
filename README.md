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
│           └── README.md
├── text/
│   └── tamil/
│       └── README.md
├── structure/
│   ├── README.md
│   └── sections.yml
├── indexes/
│   └── README.md
├── data/
│   └── README.md
├── commentaries/
│   └── README.md
├── translations/
│   └── en/
│       └── README.md
└── audit/
    └── README.md
```

## Initial source structure

The Project Madurai eText presents:

- சிறப்புப்பாயிரம்
- பொதுப்பாயிரம் — நூற்பா 1–55
- எழுத்ததிகாரம் — நூற்பா 56–257
- சொல்லதிகாரம் — நூற்பா 258–462

Detailed இயல்-level ranges are recorded in `structure/sections.yml`.

## Status

Repository initialized. Source ingestion and canonical text segmentation have not yet been declared complete.
