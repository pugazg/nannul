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

Primary artifacts include `source-heading-index.json`, `word-form-concordance.json`, `token-occurrences.ndjson`, `frequency-profiles.json`, and PASS validation artifacts. Exact-surface tokenization performs no punctuation stripping, Unicode/spelling normalization, stemming, lemmatization, or sandhi splitting.

## Grammatical-terminology candidate discovery

`grammatical-terminology-candidates.json` is the generated Phase-1 discovery layer.

- exact surface forms considered: **2,837**;
- discovered candidates: **455**;
- frequency-selected: **443**;
- source-heading-supported: **37**.

Candidate IDs are stable exact-surface hashes: `nannul-term-candidate-<16 hex>`. Generated candidate data is never overwritten with human decisions.

## Grammatical-terminology review ledger

`grammatical-terminology-review.json` is the separate human/editorial decision ledger.

Current Phase-2 state after **Batches 001–008**:

- candidates: **455**;
- reviewed: **187**;
- accepted: **116**;
- rejected: **71**;
- needs-context: **0**;
- unreviewed: **268**;
- status: **review-in-progress**.

Batch results:

- Batch 001: **20 = 19 accepted + 1 rejected**;
- Batch 002: **17 = 14 accepted + 3 rejected**;
- Batch 003: **25 = 18 accepted + 7 rejected**;
- Batch 004: **25 = 16 accepted + 9 rejected**;
- Batch 005: **25 = 18 accepted + 7 rejected**;
- Batch 006: **25 = 12 accepted + 13 rejected**;
- Batch 007: **25 = 7 accepted + 18 rejected**;
- Batch 008: **25 = 12 accepted + 13 rejected**.

All **37 source-heading-supported candidates** were completed in Batches 001–002. Batches 003–008 are frequency-only review tiers.

Mixed-use candidates may carry both `term_use_record_ids` and `non_term_use_record_ids`; acceptance remains context-bounded.

### Review validation

`grammatical-terminology-review-validation.json` — **PASS**.

Validation checks candidate identity, canonical evidence links, source-gap exclusion, decision structure, evidence-subset/overlap rules, ledger count/status reconciliation, and exact batch boundaries through Batch 008.

Current validated ledger SHA-256:

`66f4f44fa5eb862379524a719a6fa1f8ee7a0f58a7bc899863bd69d562eba3ed`

Batch-008 decision-summary SHA-256:

`e4da47483b92771abfca9d450bf2c4448f1994d9c5925bf49febbe985d7d1cc3`

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Human-readable summaries and audits exist for Batches 001–008 under `reviews/terminology/` and `audit/` respectively.

## Derivation and interpretation policy

Canonical-derived mechanical datasets, candidate discovery, and human review remain separate evidentiary layers. External Tolkāppiyam/commentary/dictionary/later-grammar evidence must be tagged separately if introduced later.
