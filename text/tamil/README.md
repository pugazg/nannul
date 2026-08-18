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
│   ├── 02-02-pathaviyal/
│   │   └── pathaviyal-128-150.md
│   ├── 02-03-uyireetru-punariyal/
│   │   └── uyireetru-punariyal-151-203.md
│   ├── 02-04-meyyeetru-punariyal/
│   │   └── meyyeetru-punariyal-204-239.md
│   └── 02-05-urupu-punariyal/
│       └── urupu-punariyal-240-257.md
└── 03-sollathikaram/
    └── 03-01-peyariyal/
        └── peyariyal-258-319.md
```

## Canonical status

- சிறப்புப்பாயிரம்: **complete from controlling source**
- பொதுப்பாயிரம் 1–55: **complete from controlling source**
- எழுத்ததிகாரம் 56–257: **canonicalized and audited in full**
  - எழுத்து இயல் 56–127: complete
  - பதவியல் 128–150: complete
  - உயிரீற்றுப் புணரியல் 151–203: complete
  - மெய்யீற்றுப் புணரியல் 204–239: complete
  - உருபு புணரியல் 240–257: complete
- சொல்லதிகாரம் 258–462:
  - பெயரியல் 258–319: **canonicalized and audited**
  - வினையியல் 320–351: **next**
  - பொதுவியல் 352–419: pending
  - இடையியல் 420–441: pending
  - உரியியல் 442–462: pending

## Current boundary

Canonical Tamil currently reaches source நூற்பா **319**.

The next source unit is **320**, beginning `3.2 வினையியல்` under சொல்லதிகாரம்.

## Controlling-source numbering findings

The current Project Madurai webpage does not display:

- numbered 73 between 72 and 74;
- numbered 176 between 175 and 177.

The canonical layer preserves those source states rather than importing readings from the historical Project Madurai witness.

The older witness also has a numbering anomaly around 240–242; the current webpage's continuous **240, 241, 242** sequence is canonical.

The பெயரியல் range **258–319** is continuous in the controlling webpage with no missing or duplicate number observed.

See `audit/SOURCE_VARIANTS.md`, `audit/EZHUTHTHATHIKARAM_COMPLETION.md`, and `audit/CANONICAL_INGEST_258_319.md`.

## Rules

Each numbered நூற்பா retains its source number and wording. This layer must not contain translation, explanatory commentary, modernization, silent spelling correction, or text imported from a secondary witness.

Source discrepancies belong in `audit/` and must not be silently repaired in canonical text.
