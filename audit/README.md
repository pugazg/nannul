# Audit

Verification records, discrepancies, and editorial decisions belong here.

Each audit identifies source/version, range, verification method, anomalies, unresolved readings, and repository-side transformations.

## Current audit records

- `SOURCE_VARIANTS.md` — source-witness differences.
- `CANONICAL_INGEST_056_127.md` through `CANONICAL_INGEST_442_462.md` — canonical ingestion audits.
- `EZHUTHTHATHIKARAM_COMPLETION.md` — எழுத்ததிகாரம் completion.
- `SOLLATHIKARAM_COMPLETION.md` — சொல்லதிகாரம் completion.
- `NANNUL_CANONICAL_COMPLETION.md` — end-to-end canonical completion.
- `RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` — unresolved exact-byte raw-source retrieval attempt.
- `STABLE_IDENTIFIER_INDEX.md` — stable நூற்பா identifier/index audit.
- `CANONICAL_UNIT_DATASET.md` — reproducible 460-record canonical dataset audit.
- `HEADING_LEXICAL_CONCORDANCE.md` — source-heading / exact-surface concordance audit.
- `FREQUENCY_PROFILES.md` — deterministic frequency/profile audit.
- `TERMINOLOGY_CANDIDATE_DISCOVERY.md` — Phase-1 terminology discovery audit.
- `TERMINOLOGY_REVIEW_BATCH_001.md` — Phase-2 contextual review Batch 001.
- `TERMINOLOGY_REVIEW_BATCH_002.md` — Batch 002 and heading-supported-tier completion.
- `TERMINOLOGY_REVIEW_BATCH_003.md` — first frequency-only batch.
- `TERMINOLOGY_REVIEW_BATCH_004.md` — second frequency-only batch.
- `TERMINOLOGY_REVIEW_BATCH_005.md` — third frequency-only batch.
- `TERMINOLOGY_REVIEW_BATCH_006.md` — fourth frequency-only batch.

## Canonical / mechanical-data status

- canonical Tamil: **COMPLETE** through 462 / `நன்னூல் முற்றிற்று`;
- canonical numbered records: **460**;
- reserved source gaps: **73, 176**;
- exact token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax forms: **2,037**;
- source-heading occurrences: **65**;
- explicit unheaded span: நூற்பாக்கள் **56–57**.

## Grammatical-terminology discovery

- candidate surface forms: **455**;
- frequency-selected candidates: **443**;
- candidates with exact source-heading-token evidence: **37**.

Discovery rank is review priority only, never semantic confidence.

## Grammatical-terminology contextual review

Human review is stored only in `data/grammatical-terminology-review.json` and validated by `scripts/validate_terminology_review.py` / `.github/workflows/validate-terminology-review.yml`.

Current validation: **PASS**.

Batch results:

- Batch 001 — 20 = **19 accepted + 1 rejected**;
- Batch 002 — 17 = **14 accepted + 3 rejected**;
- Batch 003 — 25 = **18 accepted + 7 rejected**;
- Batch 004 — 25 = **16 accepted + 9 rejected**;
- Batch 005 — 25 = **18 accepted + 7 rejected**;
- Batch 006 — 25 = **12 accepted + 13 rejected**.

Whole ledger after Batch 006:

- candidates: **455**;
- reviewed: **137**;
- accepted: **97**;
- rejected: **40**;
- needs-context: **0**;
- unreviewed: **318**;
- status: **review-in-progress**.

Validation enforces batch counts **20 + 17 + 25 + 25 + 25 + 25**, canonical evidence linkage, source-gap exclusion, evidence-subset rules, and exact count/status reconciliation.

## Raw-source preservation status

- exact-byte preservation protocol: documented;
- reproducible GitHub Actions retrieval workflow: installed;
- current raw Project Madurai HTML committed to `main`: **not yet verified / not present**;
- SHA-256 provenance for current raw HTML: **not yet available**.

Raw-source preservation remains separate from the completed canonical and derived/review layers.
