# Data

Machine-readable derived datasets for Nannūl belong here.

All data in this folder is derived from the audited canonical Tamil and `structure/` metadata. Derived or inferred fields must never be represented as if they were part of the source text.

## Canonical unit dataset — COMPLETE

### `nurpa.json`

The primary one-record-per-canonical-numbered-unit dataset.

It contains:

- work and derivation metadata;
- the two reserved source-gap positions as metadata;
- **460 canonical numbered records**;
- stable ID and source number;
- exact canonical Tamil text;
- text line count;
- அதிகாரம் / இயல் or பொதுப்பாயிரம்-subsection parentage;
- nearest source-supported topic heading;
- canonical Markdown file provenance;
- controlling-source status;
- existing source-variant audit references where applicable.

The dataset contains no canonical record for source-gap positions 73 or 176.

### `nurpa.ndjson`

Streaming/search/indexing representation of the same **460 canonical records**, with one JSON object per physical line.

This is suitable for ingestion into search engines, vector/index pipelines, databases, API build steps, and command-line processing without loading the full dataset object.

### `nurpa-validation.json`

Deterministic generator validation report.

Current validated state:

- status: **PASS**;
- records: **460**;
- unique IDs: **460**;
- first number: **1**;
- last number: **462**;
- reserved source gaps: **73, 176**;
- missing expected canonical numbers: **none**;
- unexpected numbers: **none**.

It also records per-section, per-unit, and per-file counts plus SHA-256 hashes for `nurpa.json` and `nurpa.ndjson`.

### `nurpa.schema.json`

JSON Schema for the `nurpa.json` dataset contract.

It requires 460 canonical records and prevents 73 or 176 from being represented as canonical numbered records.

### `nurpa-index.json`

A lightweight resolver for the stable Nannūl numbered namespace.

It records:

- identifier pattern `nannul-%04d`;
- nominal numbered range 1–462;
- canonical displayed unit count 460;
- reserved source-gap positions 73 and 176;
- section / subsection / இயல் segment boundaries;
- canonical file path for each segment;
- deterministic expansion rule for resolving a number to its stable ID and canonical location.

The two source-gap positions do not point to canonical Tamil text.

## Reproducible generation

Generator:

`scripts/generate_nurpa_dataset.py`

Workflow:

`.github/workflows/generate-nurpa-dataset.yml`

The generator reads the canonical Markdown directly, resolves structural parents through `nurpa-index.json`, validates the exact expected number set, and writes `nurpa.json`, `nurpa.ndjson`, and `nurpa-validation.json`.

It fails rather than silently emitting a dataset if:

- an expected canonical number is missing;
- an unexpected number appears;
- 73 or 176 appears as canonical text;
- stable IDs are duplicated;
- a canonical unit has empty text;
- a number does not resolve to exactly one structural segment.

See `audit/CANONICAL_UNIT_DATASET.md` for the completed dataset audit.

## Stable IDs

All numbered records use stable IDs from `structure/identifiers.yml`:

- `nannul-0001`
- `nannul-0056`
- `nannul-0258`
- `nannul-0462`

The unnumbered சிறப்புப்பாயிரம் remains separately addressable as `nannul-sirappu-payiram`; it is not forced into this numbered-record dataset.

## Separation from source preservation

This dataset is a derivative of the completed canonical Tamil transcription. It does not resolve the separate exact-byte Project Madurai raw-HTML preservation gate.

Future derived datasets may include grammatical terminology, token/word-form indexes, examples, commentary mappings, and relationships connecting Nannūl rules with Tolkāppiyam or other Tamil grammatical works.
