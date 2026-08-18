# Data

Machine-readable derived datasets for Nannūl belong here.

## Canonical unit dataset

### `nurpa.json`

Primary one-record-per-canonical-numbered-unit dataset.

- canonical records: **460**;
- source range represented: 1–462 with controlling-source gaps 73 and 176 absent from records;
- stable IDs: `nannul-%04d`;
- exact `text_ta` derived from audited canonical Markdown;
- structural parents, source-supported heading, canonical-file provenance, and source-variant references retained.

### `nurpa.ndjson`

Streaming/search-friendly form of the same 460 canonical records, one JSON object per line.

### `nurpa-validation.json`

Generation and coverage validation, including record counts, section/இயல் counts, reserved gaps, and SHA-256 fingerprints.

### `nurpa.schema.json`

JSON Schema contract for `nurpa.json`.

### `nurpa-index.json`

Stable-number/segment resolver for the nominal 1–462 namespace. Positions 73 and 176 resolve as reserved source gaps rather than canonical text.

Generator: `scripts/generate_nurpa_dataset.py`

Workflow: `.github/workflows/generate-nurpa-dataset.yml`

Audit: `audit/CANONICAL_UNIT_DATASET.md`

## Source-heading index

### `source-heading-index.json`

Derived index of source-supported heading occurrences across the 460 canonical records.

Current validated state:

- actual non-empty source-heading occurrences: **65**;
- distinct exact heading texts: **65**;
- unheaded source spans: **1**;
- unheaded records: **2** — நூற்பாக்கள் 56–57 before the first internal heading `எண்` at 58.

The index does not invent a blank heading for 56–57. Human-readable form: `indexes/source-heading-index.md`.

## Exact-surface lexical concordance

### `word-form-concordance.json`

Exact-surface form concordance generated mechanically from `nurpa.json`.

Token definition: each **non-whitespace substring** (`\S+`) in canonical `text_ta`.

Validated counts:

- token occurrences: **5,431**;
- unique exact surface forms: **2,837**.

No punctuation stripping, Unicode normalization, spelling normalization, stemming, lemmatization, or sandhi splitting is applied. Source punctuation therefore remains part of a surface form when attached in the canonical text.

### `token-occurrences.ndjson`

One record per exact token occurrence, carrying stable நூற்பா ID, source number, structure/heading context, character offsets, line, column, and token position.

### `concordance-validation.json`

Coverage/integrity checks and SHA-256 fingerprints for both the heading and lexical outputs.

Generator: `scripts/generate_concordance.py`

Workflow: `.github/workflows/generate-concordance.yml`

Audit: `audit/HEADING_LEXICAL_CONCORDANCE.md`

## Derivation policy

Everything in `data/` is derived from the verified canonical Tamil and structural metadata. Derived or inferred fields must never be represented as if they were part of the source text.

The current mechanical layers deliberately stop short of claiming that a frequent or repeated lexical surface form is a grammatical term. Grammatical-term classification belongs in a separate reviewed analytical layer.

Suitable next derived artifacts include section/இயல்/heading frequency profiles, grammatical-terminology candidate datasets, and relationship data connecting Nannūl rules with Tolkāppiyam or other grammar works.
