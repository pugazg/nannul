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

Companion artifacts:

- `nurpa.ndjson`;
- `nurpa-validation.json` — **PASS**;
- `nurpa.schema.json`;
- `nurpa-index.json`.

Generator: `scripts/generate_nurpa_dataset.py`

Audit: `audit/CANONICAL_UNIT_DATASET.md`

## Source-heading / lexical layer

### `source-heading-index.json`

- actual non-empty source-heading occurrences: **65**;
- distinct exact heading texts: **65**;
- one explicit unheaded span: நூற்பாக்கள் **56–57**.

### `word-form-concordance.json`

Exact non-whitespace (`\S+`) surface-form concordance:

- token occurrences: **5,431**;
- unique exact surface forms: **2,837**.

No punctuation stripping, Unicode normalization, spelling normalization, stemming, lemmatization, or sandhi splitting is applied.

Companion occurrence stream: `token-occurrences.ndjson`.

Validation: `concordance-validation.json` — **PASS**.

Audit: `audit/HEADING_LEXICAL_CONCORDANCE.md`.

## Exact-surface frequency profiles

Artifacts:

- `frequency-profiles.json`;
- `frequency-tables.json`;
- `frequency-profiles-validation.json` — **PASS**.

Validated whole-work counts:

- canonical records: **460**;
- token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**.

Audit: `audit/FREQUENCY_PROFILES.md`.

## Grammatical-terminology candidate discovery

### `grammatical-terminology-candidates.json`

Phase-1 mechanically generated discovery data.

Validated discovery state:

- exact surface forms considered: **2,837**;
- discovered candidates: **455**;
- frequency-selected candidates: **443**;
- candidates with exact source-heading-token evidence: **37**.

Candidate IDs are stable exact-surface hashes of the form `nannul-term-candidate-<16 hex>`.

Generated candidate rows deliberately remain discovery artifacts and are never overwritten with human semantic decisions.

Companion artifacts:

- `grammatical-terminology-candidates.ndjson`;
- `grammatical-terminology-candidates-validation.json` — **PASS**;
- `grammatical-terminology-candidates.schema.json`.

Audit: `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`.

## Grammatical-terminology review ledger

### `grammatical-terminology-review.json`

Separate human/editorial decision ledger.

Current Phase-2 state after **Batches 001–002**:

- candidates: **455**;
- reviewed: **37**;
- accepted: **33**;
- rejected: **4**;
- needs-context: **0**;
- unreviewed: **418**;
- status: **review-in-progress**.

Batch results:

- Batch 001: **20 reviewed = 19 accepted + 1 rejected**;
- Batch 002: **17 reviewed = 14 accepted + 3 rejected**.

All **37 source-heading-supported candidates have now been reviewed**. Remaining candidates are in the frequency-only review tier.

Mixed-use candidates may carry both `term_use_record_ids` and `non_term_use_record_ids`; acceptance is context-bounded and never silently extended to every occurrence or related surface form.

Schema: `grammatical-terminology-review.schema.json`.

### `grammatical-terminology-review-validation.json`

Current validation: **PASS**.

Checks include candidate identity, canonical evidence links, source-gap exclusion, decision structure, evidence subsets, ledger count reconciliation, layer-status reconciliation, Batch-001 count 20, and Batch-002 count 17.

Current validated ledger SHA-256:

`d8c461349249e9caa5ef0f340bc5433efcb34c2a9cb0ed4dba959198860af8de`

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Human-readable decision summaries:

- `reviews/terminology/batch-001-decisions.md`;
- `reviews/terminology/batch-002-decisions.md`.

Audits:

- `audit/TERMINOLOGY_REVIEW_BATCH_001.md`;
- `audit/TERMINOLOGY_REVIEW_BATCH_002.md`.

## Derivation and interpretation policy

Everything in `data/` remains separated by evidentiary role:

- canonical-derived mechanical datasets preserve or aggregate source-supported data;
- candidate discovery prioritizes possible terms without deciding termhood;
- the review ledger is a distinct human analytical layer with explicit provenance and rationale.

External comparison with Tolkāppiyam, commentaries, dictionaries, or later grammar works must be tagged separately if introduced in later phases.
