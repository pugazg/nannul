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
- `NANNUL_CANONICAL_COMPLETION.md` — end-to-end canonical completion audit for the full work.
- `RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` — exact-byte Project Madurai raw-source retrieval attempt and unresolved materialization state.
- `STABLE_IDENTIFIER_INDEX.md` — stable நூற்பா identifier namespace and canonical segment-index audit.
- `CANONICAL_UNIT_DATASET.md` — reproducible 460-record canonical unit dataset audit.
- `HEADING_LEXICAL_CONCORDANCE.md` — source-supported heading index and exact-surface lexical concordance audit.
- `FREQUENCY_PROFILES.md` — deterministic exact-surface frequency/profile aggregation audit.
- `TERMINOLOGY_CANDIDATE_DISCOVERY.md` — Phase-1 broad grammatical-terminology candidate discovery audit.
- `TERMINOLOGY_REVIEW_BATCH_001.md` — Phase-2 contextual review Batch 001 audit.
- `TERMINOLOGY_REVIEW_BATCH_002.md` — Phase-2 contextual review Batch 002 audit and heading-supported-tier completion record.

## Documented source findings

- `PM147-V001`: controlling webpage omits displayed numbered 73; canonical handling applied.
- `PM147-V002`: historical-witness numbering anomaly around 240–242; current 240, 241, 242 sequence is canonical.
- `PM147-V003`: controlling webpage omits displayed numbered 176; canonical handling applied.
- `PM147-V004`: நூற்பா 343 is `செய்தனெ` in the current webpage and `செய்தென` in the historical mirror; current reading is canonical.
- `PM147-V005`: நூற்பா 344 has a trailing `"` in the current webpage and not in the historical mirror; current punctuation is canonical.

## Verification progress

- சிறப்புப்பாயிரம்: canonicalized.
- பொதுப்பாயிரம் 1–55: canonicalized.
- எழுத்ததிகாரம் 56–257: **canonicalized and fully batch-audited**.
- சொல்லதிகாரம் 258–462: **canonicalized and fully batch-audited**.
- full source-derived canonical Tamil layer: **COMPLETE**.
- stable identifier / range index layer: **ESTABLISHED AND AUDITED**.
- one-record-per-canonical-unit data layer: **GENERATED, VALIDATED, AND AUDITED**.
- source-heading / exact-surface lexical concordance layer: **GENERATED, CORRECTED, VALIDATED, AND AUDITED**.
- exact-surface frequency/profile layer: **GENERATED, VALIDATED, AND AUDITED**.
- grammatical-terminology candidate discovery Phase 1: **GENERATED, STABLE-ID-CORRECTED, VALIDATED, AND AUDITED**.
- grammatical-terminology contextual review Phase 2: **IN PROGRESS — BATCHES 001–002 COMPLETE AND AUDITED**.

Current canonical boundary: **462 / `நன்னூல் முற்றிற்று`**.

The nominal numbered span is 1–462, while the controlling webpage displays 460 numbered units because 73 and 176 are absent. Downstream canonical datasets preserve those two positions as source gaps rather than reconstructed text.

## Mechanical-data baseline

- canonical records: **460**;
- exact token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**;
- source-section profiles: **3**;
- structural-unit profiles: **17**;
- source-heading profiles: **65**;
- unheaded-span profiles: **1**.

## Grammatical-terminology discovery status

Phase-1 discovery remains a generated mechanical layer:

- candidate surface forms: **455**;
- frequency-selected candidates: **443**;
- candidates with exact source-heading-token evidence: **37**.

Candidate IDs are SHA-256-derived from exact UTF-8 surface forms. Generated candidate files remain discovery artifacts and are not edited with human decisions.

## Grammatical-terminology review status

Human review is governed by `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md` and stored in `data/grammatical-terminology-review.json`.

Validation:

- `scripts/validate_terminology_review.py`;
- `.github/workflows/validate-terminology-review.yml`;
- `data/grammatical-terminology-review-validation.json` — **PASS**.

### Batch 001

- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**.

Rejected exact form: `முன்`.

Audit: `TERMINOLOGY_REVIEW_BATCH_001.md`.

### Batch 002

Selection: all **17 remaining source-heading-supported candidates** after Batch 001.

- reviewed: **17**;
- accepted: **14**;
- rejected: **3**;
- needs-context: **0**.

Rejected exact forms:

- `பொதுப்`;
- `சொல்லின்`;
- `சிறப்புப்`.

Audit: `TERMINOLOGY_REVIEW_BATCH_002.md`.

### Whole review ledger after Batch 002

- candidate surface forms: **455**;
- reviewed: **37**;
- accepted: **33**;
- rejected: **4**;
- needs-context: **0**;
- unreviewed: **418**;
- status: **review-in-progress**.

All **37 candidates with source-heading-token evidence have now been explicitly reviewed**. The next review tier begins with the highest-priority frequency-only candidates.

## Raw-source preservation status

- exact-byte preservation protocol: **documented**;
- reproducible GitHub Actions retrieval workflow: **installed**;
- current raw Project Madurai HTML committed to `main`: **not yet verified / not present**;
- SHA-256 provenance for current raw HTML: **not yet available**.

Raw-source preservation remains a separate archival state from the completed canonical transcription and derived/review layers.
