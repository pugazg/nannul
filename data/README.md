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

## Exact-surface frequency profiles

### `frequency-profiles.json`

Mechanical summary profiles over the already-validated exact token occurrences.

Validated dimensions:

- source-section / அதிகார-level profiles: **3**;
- இயல் / structural-unit profiles: **17**;
- actual source-heading profiles: **65**;
- explicit unheaded-span profiles: **1**.

Whole-work validated counts remain:

- canonical records: **460**;
- token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**.

Each profile records record/token/form counts plus its top 20 exact surface forms. The frequency ordering is deterministic: descending count, first global occurrence, then exact surface form.

### `frequency-tables.json`

Complete exact-surface frequency tables for the whole work and every section, இயல், source-heading occurrence, and unheaded span.

### `frequency-profiles-validation.json`

**PASS** reconciliation/integrity report.

Human-readable profile: `indexes/frequency-profiles.md`

Generator: `scripts/generate_frequency_profiles.py`

Workflow: `.github/workflows/generate-frequency-profiles.yml`

Audit: `audit/FREQUENCY_PROFILES.md`

## Grammatical-terminology candidate discovery

### `grammatical-terminology-candidates.json`

Phase-1 mechanically generated candidate-discovery dataset.

Validated discovery state:

- all unique exact surface forms considered: **2,837**;
- discovered candidate surface forms: **455**;
- candidates meeting exact frequency >=3: **443**;
- candidates with exact source-heading-token evidence: **37**.

The frequency and heading sets overlap. Candidate selection is deliberately broad and is not a grammatical-term assertion.

Candidate IDs are stable across ranking changes: `nannul-term-candidate-<16 hex>`, where the suffix is the first 16 hexadecimal characters of SHA-256 over the exact UTF-8 surface form.

Each candidate carries exact-surface frequency, record/section/இயல் breadth, source-heading evidence when present, stable நூற்பா occurrence samples, variant references, and a mechanical review-priority score. The score is **not** semantic confidence.

The generated discovery data deliberately retains its `unreviewed` status fields. Human decisions are stored separately and are never written back into generated candidate records.

### `grammatical-terminology-candidates.ndjson`

Streaming form of the 455 discovery candidates.

### `grammatical-terminology-candidates-validation.json`

**PASS** validation ensuring the discovery rule is reproduced exactly, stable candidate IDs match exact-surface hashes, evidence counts reconcile, and the generated layer contains no automatic semantic decision.

### `grammatical-terminology-candidates.schema.json`

Schema contract for the generated discovery layer.

Generator: `scripts/generate_terminology_candidates.py`

Workflow: `.github/workflows/generate-terminology-candidates.yml`

Human discovery queue: `indexes/grammatical-terminology-review-queue.md`

Audit: `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`

## Grammatical-terminology review ledger

### `grammatical-terminology-review.json`

Separate human/editorial decision ledger. It is **not generated from frequency**.

Current Phase-2 state after Batch 001:

- candidates: **455**;
- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**;
- unreviewed: **435**;
- status: **review-in-progress**.

The accepted/rejected decision applies to the exact surface form and documented reviewed contexts, not automatically to every occurrence or related spelling.

Mixed-use candidates can carry both `term_use_record_ids` and `non_term_use_record_ids`, allowing technical and ordinary uses of the same exact form to remain distinct.

Do not place human decisions in the generated candidate files. Review decisions belong only in this ledger under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

Schema: `grammatical-terminology-review.schema.json`.

### `grammatical-terminology-review-validation.json`

**PASS** structural/provenance validation of the human ledger.

It checks candidate identity, canonical நூற்பா evidence links, source-gap exclusion, decision requirements, mixed-use evidence subsets, count reconciliation, review coverage/status, and Batch-001 decision count.

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Human-readable Batch-001 decision summary: `reviews/terminology/batch-001-decisions.md`.

Audit: `audit/TERMINOLOGY_REVIEW_BATCH_001.md`.

Current Batch-001 decision result: **19 accepted / 1 rejected / 0 needs-context**. The only rejection is exact form `முன்`, which the reviewed Nannūl contexts support as an ordinary relational word embedded inside technical grammatical statements rather than a standalone technical term.

## Derivation and interpretation policy

Everything in `data/` remains separated by evidentiary role:

- canonical-derived mechanical datasets preserve or aggregate source-supported data;
- candidate discovery prioritizes possible terms without deciding termhood;
- the review ledger is a distinct human analytical layer with explicit provenance and rationale.

Derived or inferred fields must never be represented as if they were part of the source text. External comparison with Tolkāppiyam, commentaries, dictionaries, or later grammar works must be tagged separately if introduced in later phases.
