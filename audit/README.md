# Audit

Verification records, discrepancies, and editorial decisions belong here.

Each audit identifies source/version, range, verification method, anomalies, unresolved readings, and repository-side transformations.

## Current audit records

- `SOURCE_VARIANTS.md` — source-witness differences.
- `CANONICAL_INGEST_056_127.md` — எழுத்து இயல் 56–127.
- `CANONICAL_INGEST_128_150.md` — பதவியல் 128–150.
- `CANONICAL_INGEST_151_203.md` — உயிரீற்றுப் புணரியல் 151–203.
- `CANONICAL_INGEST_204_239.md` — மெய்யீற்றுப் புணரியல் 204–239.
- `CANONICAL_INGEST_240_257.md` — உருபு புணரியல் 240–257.
- `EZHUTHTHATHIKARAM_COMPLETION.md` — authority-level completion audit for எழுத்ததிகாரம் 56–257.
- `CANONICAL_INGEST_258_319.md` — பெயரியல் 258–319.
- `CANONICAL_INGEST_320_351.md` — வினையியல் 320–351.
- `CANONICAL_INGEST_352_419.md` — பொதுவியல் 352–419.
- `CANONICAL_INGEST_420_441.md` — இடையியல் 420–441.
- `CANONICAL_INGEST_442_462.md` — உரியியல் 442–462.
- `SOLLATHIKARAM_COMPLETION.md` — authority-level completion audit for சொல்லதிகாரம் 258–462.
- `NANNUL_CANONICAL_COMPLETION.md` — end-to-end canonical completion audit.
- `RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` — exact-byte raw-source retrieval attempt.
- `STABLE_IDENTIFIER_INDEX.md` — stable நூற்பா identifier/index audit.
- `CANONICAL_UNIT_DATASET.md` — reproducible 460-record canonical dataset audit.
- `HEADING_LEXICAL_CONCORDANCE.md` — source-heading / exact-surface concordance audit.
- `FREQUENCY_PROFILES.md` — deterministic frequency/profile audit.
- `TERMINOLOGY_CANDIDATE_DISCOVERY.md` — Phase-1 terminology discovery audit.
- `TERMINOLOGY_REVIEW_BATCH_001.md` — Phase-2 contextual review Batch 001.
- `TERMINOLOGY_REVIEW_BATCH_002.md` — Phase-2 contextual review Batch 002 and heading-supported-tier completion.
- `TERMINOLOGY_REVIEW_BATCH_003.md` — first frequency-only contextual review batch.

## Canonical / mechanical-data status

- source-derived canonical Tamil: **COMPLETE** through 462 / `நன்னூல் முற்றிற்று`;
- nominal numbered span: **1–462**;
- displayed canonical numbered records: **460**;
- reserved source gaps: **73, 176**;
- exact token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax forms: **2,037**;
- source-heading occurrences: **65**;
- explicit unheaded span: நூற்பாக்கள் **56–57**.

## Grammatical-terminology discovery

Phase 1 remains a generated mechanical layer:

- candidate surface forms: **455**;
- frequency-selected candidates: **443**;
- candidates with exact source-heading-token evidence: **37**.

Discovery rank is review priority only, never semantic confidence.

## Grammatical-terminology contextual review

Human review is governed by `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md` and stored only in `data/grammatical-terminology-review.json`.

Validation:

- `scripts/validate_terminology_review.py`;
- `.github/workflows/validate-terminology-review.yml`;
- `data/grammatical-terminology-review-validation.json` — **PASS**.

### Batch 001 — heading-supported

- reviewed: **20**;
- accepted: **19**;
- rejected: **1** (`முன்`);
- needs-context: **0**.

### Batch 002 — remaining heading-supported

- reviewed: **17**;
- accepted: **14**;
- rejected: **3** (`பொதுப்`, `சொல்லின்`, `சிறப்புப்`);
- needs-context: **0**.

After Batch 002, all **37 source-heading-supported candidates** had explicit decisions.

### Batch 003 — first frequency-only batch

Selection: **25 highest-priority unreviewed frequency-only candidates**.

- reviewed: **25**;
- accepted: **18**;
- rejected: **7**;
- needs-context: **0**.

Rejected exact forms:

- `ஆகும்`;
- `இரு`;
- `என்ப`;
- `இயல்பும்`;
- `ஆறு`;
- `இயல்பே`;
- `ஒன்று`.

Batch 003 confirmed that high frequency alone does not imply termhood, while frequency-only forms can still be accepted when Nannūl explicitly treats them as grammatical forms in body text—for example `ஐ`, `ஈர்`, `என`, `என்`, `ஆம்`, `ஒற்று`, `உயிர்மெய்`, and `ஆய்தம்`.

### Whole review ledger after Batch 003

- candidate surface forms: **455**;
- reviewed: **62**;
- accepted: **51**;
- rejected: **11**;
- needs-context: **0**;
- unreviewed: **393**;
- status: **review-in-progress**.

Validation enforces batch counts **20 + 17 + 25**, canonical evidence linkage, source-gap exclusion, evidence-subset rules, and exact count reconciliation.

## Raw-source preservation status

- exact-byte preservation protocol: documented;
- reproducible GitHub Actions retrieval workflow: installed;
- current raw Project Madurai HTML committed to `main`: **not yet verified / not present**;
- SHA-256 provenance for current raw HTML: **not yet available**.

Raw-source preservation remains separate from the completed canonical and derived/review layers.
