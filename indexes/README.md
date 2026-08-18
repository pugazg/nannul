# Indexes

Human-facing navigational and derived indexes for Nannūl belong here.

## Current indexes

### `nurpa-number-index.md`

Stable range/navigation index for the numbered Nannūl source.

It documents:

- `nannul-%04d` as the numbered stable-ID scheme;
- all source-supported section / subsection / இயல் ranges;
- canonical file paths;
- reserved source-gap positions `nannul-0073` and `nannul-0176`;
- `nannul-sirappu-payiram` for the unnumbered சிறப்புப்பாயிரம்.

Machine-readable resolver: `data/nurpa-index.json`.

### `source-heading-index.md`

Human-facing index of the exact source-supported heading occurrences carried by the canonical unit dataset.

Validated state:

- **65** actual non-empty source-heading occurrences;
- **65** distinct exact heading strings;
- one explicitly represented unheaded span, நூற்பாக்கள் **56–57**, before `எண்` begins at 58.

No empty/fabricated heading is assigned to the unheaded span.

Machine-readable form: `data/source-heading-index.json`.

### `frequency-profiles.md`

Human-facing exact-surface frequency profile generated from the validated occurrence layer.

It provides:

- whole-work exact-surface frequency leaders;
- **3** source-section / அதிகார-level profiles;
- **17** இயல் / structural-unit profiles;
- **65** actual source-heading profiles;
- **1** explicit unheaded-span profile;
- record, token, unique-form, and hapax counts;
- leading exact surface forms for each group.

Validated whole-work totals are **460 canonical numbered records**, **5,431 exact token occurrences**, **2,837 unique exact surface forms**, and **2,037 hapax surface forms**.

Machine-readable summaries: `data/frequency-profiles.json`.

Complete exact-surface group tables: `data/frequency-tables.json`.

Validation: `data/frequency-profiles-validation.json`.

Audit: `audit/FREQUENCY_PROFILES.md`.

## Index policy

Indexes are derived from verified canonical text and structure. They use stable நூற்பா IDs wherever individual units are addressed and never rewrite canonical Tamil.

Mechanical frequency/profile data must remain distinguishable from analytical classification. In particular, frequent surface forms are not automatically grammatical terms.

Future human-facing indexes may include:

- reviewed grammatical-term index;
- example-word index;
- referenced-author/work index;
- cross-reference index to Tolkāppiyam and other Tamil grammar works.
