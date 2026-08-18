# Canonical Tamil Text

This folder contains the repository's source-faithful Tamil text derived from the declared controlling source.

Current organization:

```text
text/tamil/
├── 00-sirappuppayiram.md
├── 01-pothuppayiram/
│   └── pothuppayiram-001-055.md
├── 02-ezhuththathikaram/
│   ├── 02-01-ezhuththu-iyal/
│   │   └── ezhuththu-iyal-056-127.md
│   └── 02-02-pathaviyal/
│       └── pathaviyal-128-150.md
└── 03-sollathikaram/            # later canonical stage
```

## Canonical status

- சிறப்புப்பாயிரம்: **complete from controlling source**
- பொதுப்பாயிரம் 1–55: **complete from controlling source**
- எழுத்ததிகாரம் 56–257:
  - எழுத்து இயல் 56–127: **canonicalized and audited**
  - பதவியல் 128–150: **canonicalized and audited**
  - உயிரீற்றுப் புணரியல் 151–203: **next**
  - மெய்யீற்றுப் புணரியல் 204–239: pending
  - உருபு புணரியல் 240–257: pending
- சொல்லதிகாரம் 258–462: **not yet canonicalized**

## Current boundary

Canonical Tamil currently reaches source நூற்பா **150**.

The controlling Project Madurai webpage does not display a numbered 73 between 72 and 74. The canonical layer preserves that state rather than importing 73 from a secondary witness. See `audit/SOURCE_VARIANTS.md` and `audit/CANONICAL_INGEST_056_127.md`.

The பதவியல் range 128–150 is continuous and is documented in `audit/CANONICAL_INGEST_128_150.md`.

## Rules

Each numbered நூற்பா retains its source number and wording. This layer must not contain translation, explanatory commentary, modernization, silent spelling correction, or text imported from a secondary witness.

Source discrepancies belong in `audit/` and must not be silently repaired in canonical text.
