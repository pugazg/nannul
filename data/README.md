# Data

Machine-readable derived datasets for Nannūl belong here.

## Canonical unit dataset

`nurpa.json` is the primary one-record-per-canonical-numbered-unit dataset.

- canonical records: **460**;
- represented source range: 1–462 with controlling-source gaps 73 and 176 absent from records;
- stable IDs: `nannul-%04d`;
- exact `text_ta` derived from audited canonical Markdown.

Companion artifacts: `nurpa.ndjson`, `nurpa-validation.json` (**PASS**), `nurpa.schema.json`, and `nurpa-index.json`.

## Source-heading / lexical / frequency layers

Validated mechanical baseline:

- source-heading occurrences: **65**;
- explicit unheaded span: நூற்பாக்கள் **56–57**;
- token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax forms: **2,037**.

Primary artifacts include `source-heading-index.json`, `word-form-concordance.json`, `token-occurrences.ndjson`, `frequency-profiles.json`, and their PASS validation artifacts.

Exact-surface tokenization performs no punctuation stripping, Unicode/spelling normalization, stemming, lemmatization, or sandhi splitting.

## Grammatical-terminology candidate discovery

`grammatical-terminology-candidates.json` is the generated Phase-1 discovery layer.

- exact surface forms considered: **2,837**;
- discovered candidates: **455**;
- frequency-selected: **443**;
- source-heading-supported: **37**.

Candidate IDs are stable exact-surface hashes: `nannul-term-candidate-<16 hex>`. Generated candidate data is never overwritten with human decisions.

## Grammatical-terminology review ledger

`grammatical-terminology-review.json` is the separate human/editorial decision ledger.

Current Phase-2 state after **Batches 001–006**:

- candidates: **455**;
- reviewed: **137**;
- accepted: **97**;
- rejected: **40**;
- needs-context: **0**;
- unreviewed: **318**;
- status: **review-in-progress**.

Batch results:

- Batch 001: **20 = 19 accepted + 1 rejected**;
- Batch 002: **17 = 14 accepted + 3 rejected**;
- Batch 003: **25 = 18 accepted + 7 rejected**;
- Batch 004: **25 = 16 accepted + 9 rejected**;
- Batch 005: **25 = 18 accepted + 7 rejected**;
- Batch 006: **25 = 12 accepted + 13 rejected**.

All **37 source-heading-supported candidates** were completed in Batches 001–002. Batches 003–006 are frequency-only review tiers.

Mixed-use candidates may carry both `term_use_record_ids` and `non_term_use_record_ids`; acceptance remains context-bounded.

### Review validation

`grammatical-terminology-review-validation.json` — **PASS**.

Validation checks candidate identity, canonical evidence links, source-gap exclusion, decision structure, evidence-subset/overlap rules, ledger count/status reconciliation, and batch counts **20 + 17 + 25 + 25 + 25 + 25**.

Current validated ledger SHA-256:

`c74aeb4499997bee191547156295d5a5208c004f63a5ff9c22ae6ac2db3b5979`

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Human-readable summaries:

- `reviews/terminology/batch-001-decisions.md`
- `reviews/terminology/batch-002-decisions.md`
- `reviews/terminology/batch-003-decisions.md`
- `reviews/terminology/batch-004-decisions.md`
- `reviews/terminology/batch-005-decisions.md`
- `reviews/terminology/batch-006-decisions.md`

Audits:

- `audit/TERMINOLOGY_REVIEW_BATCH_001.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_002.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_003.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_004.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_005.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_006.md`

## Derivation and interpretation policy

Canonical-derived mechanical datasets, candidate discovery, and human review remain separate evidentiary layers. External Tolkāppiyam/commentary/dictionary/later-grammar evidence must be tagged separately if introduced later.
