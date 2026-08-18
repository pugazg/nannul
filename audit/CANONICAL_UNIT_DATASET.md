# Canonical Unit Dataset Audit

## Scope

This audit covers the one-record-per-canonical-numbered-unit derived dataset for **நன்னூல்**.

The dataset is generated only from the completed and audited canonical Tamil layer. It does not alter source transcription.

## Inputs

- `text/tamil/` — completed canonical Tamil transcription;
- `structure/identifiers.yml` — stable identifier policy;
- `data/nurpa-index.json` — deterministic number/segment resolver;
- `audit/NANNUL_CANONICAL_COMPLETION.md` — end-to-end canonical completion state;
- `audit/SOURCE_VARIANTS.md` — source-witness discrepancy ledger.

## Reproducible generator

Generator:

`scripts/generate_nurpa_dataset.py`

Workflow:

`.github/workflows/generate-nurpa-dataset.yml`

The workflow successfully generated and committed the derived dataset on `main` with commit:

`d62b0a24cb9840b2ea8e5fcbfc8cb5eacb0fa356`

## Outputs

- `data/nurpa.json` — complete dataset object with metadata, source-gap metadata, and 460 canonical records;
- `data/nurpa.ndjson` — one canonical record per physical line for streaming/search/indexing workflows;
- `data/nurpa-validation.json` — deterministic generation/coverage validation and output hashes;
- `data/nurpa.schema.json` — JSON Schema for the dataset contract.

## Record contract

Each canonical numbered record contains:

- stable `id` (`nannul-%04d`);
- source `number`;
- exact canonical `text_ta` extracted from the audited Markdown;
- `text_line_count`;
- அதிகாரம்-level `section_id` / `section_label_ta`;
- இயல் or பொதுப்பாயிரம்-subsection `unit_id` / `unit_label_ta`;
- nearest source-supported Markdown heading as `topic_heading_ta`;
- exact `canonical_file` provenance path;
- `source_status: canonical`;
- controlling-source identifier;
- `source_variant_refs` where an already-documented witness discrepancy applies.

## Count validation

`data/nurpa-validation.json` reports:

- status: **PASS**;
- canonical record count: **460**;
- first number: **1**;
- last number: **462**;
- unique stable IDs: **460**;
- reserved source gaps: **73, 176**;
- missing expected canonical numbers: **none**;
- unexpected numbers: **none**.

### அதிகாரம்-level counts

- பொதுப்பாயிரம்: **55** records;
- எழுத்ததிகாரம்: **200** records;
- சொல்லதிகாரம்: **205** records.

Total: **460**.

The எழுத்ததிகாரம் count is 200 rather than the nominal 202 because the controlling current Project Madurai webpage does not display numbered 73 or 176.

## Source-gap validation

The generated NDJSON was checked across both gap boundaries:

- `nannul-0072` is followed by `nannul-0074`; no `nannul-0073` canonical record exists;
- `nannul-0175` is followed by `nannul-0177`; no `nannul-0176` canonical record exists.

The missing nominal positions remain represented only in dataset-level `source_gaps` metadata and in `structure/identifiers.yml`.

No historical-witness text was reconstructed into either gap.

## Variant linkage validation

The generated records link existing audit findings without changing canonical readings:

- 240, 241, 242 → `PM147-V002`;
- 343 → `PM147-V004`, retaining current-source `செய்தனெ`;
- 344 → `PM147-V005`, retaining the current-source trailing quotation mark after `பிற`.

`PM147-V001` and `PM147-V003` belong to source-gap metadata rather than canonical unit records because 73 and 176 are not displayed in the controlling witness.

## Boundary spot checks

Verified from `data/nurpa.ndjson`:

- first record: `nannul-0001` / 1;
- gap transition: 72 → 74;
- gap transition: 175 → 177;
- historical-numbering variant range: 240 → 241 → 242;
- textual-variant records: 343 and 344;
- final record: `nannul-0462` / 462.

The final record carries the canonical text of நூற்பா 462; the unnumbered terminal marker `நன்னூல் முற்றிற்று` remains part of the canonical file boundary rather than being fabricated as an additional numbered record.

## Output integrity hashes

From `data/nurpa-validation.json`:

- `data/nurpa.json` SHA-256: `a82d86a75012a1001a5a3d5c2a49034f868f5ba78c2da46bd84400ae19581874`;
- `data/nurpa.ndjson` SHA-256: `9dcfe6482228347d962a18c18fabefafd6b30a3d73a6d984585b324537c4fbd5`.

These hashes identify the generated derived-data snapshot. They are not hashes of the unresolved raw Project Madurai HTML source.

## Separation-of-layers check

This activity did **not**:

- modify any file under `text/tamil/`;
- insert stable IDs into canonical Tamil lines;
- modernize or normalize text;
- reconstruct 73 or 176;
- replace current-source readings with historical-witness readings;
- resolve the independent raw-HTML preservation gate.

## Raw-source preservation state

Exact-byte preservation of the live Project Madurai HTML remains separately open under:

- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`;
- `audit/RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md`.

The canonical-unit dataset is valid as a derivative of the audited canonical layer and does not claim to substitute for raw-source preservation.

## Result

**PASS — 460 one-record-per-canonical-unit Nannūl records are reproducibly generated, stable-ID-addressable, structurally linked, provenance-bearing, source-gap-safe, and validated without modifying the canonical Tamil layer.**
