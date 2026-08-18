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
- `TERMINOLOGY_CANDIDATE_DISCOVERY.md` — Phase-1 broad unreviewed grammatical-terminology candidate discovery audit.
- `TERMINOLOGY_REVIEW_BATCH_001.md` — Phase-2 contextual review Batch 001 audit.

## Documented source findings

- `PM147-V001`: controlling webpage omits displayed numbered 73; canonical handling applied.
- `PM147-V002`: historical-witness numbering anomaly around 240–242; current 240, 241, 242 sequence is canonical.
- `PM147-V003`: controlling webpage omits displayed numbered 176; canonical handling applied.
- `PM147-V004`: நூற்பா 343 is `செய்தனெ` in the current webpage and `செய்தென` in the historical mirror; current reading is canonical.
- `PM147-V005`: நூற்பா 344 has a trailing `"` in the current webpage and not in the historical mirror; current punctuation is canonical.
- பெயரியல் 258–319: continuous numbering.
- வினையியல் 320–351: continuous numbering.
- பொதுவியல் 352–419: continuous numbering.
- இடையியல் 420–441: continuous numbering.
- உரியியல் 442–462: continuous numbering; source terminates with `நன்னூல் முற்றிற்று`.

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
- grammatical-terminology contextual review Phase 2: **IN PROGRESS — BATCH 001 COMPLETE AND AUDITED**.

Current canonical boundary: **462 / `நன்னூல் முற்றிற்று`**.

The nominal numbered span is 1–462, while the controlling webpage displays 460 numbered units because 73 and 176 are absent. The stable namespace reserves those two positions as `source-gap`; downstream datasets contain only the 460 actually displayed canonical numbered units.

## Mechanical data status

Validated baselines:

- canonical records: **460**;
- exact token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**;
- source-section profiles: **3**;
- structural-unit profiles: **17**;
- source-heading profiles: **65**;
- unheaded-span profiles: **1**.

See `CANONICAL_UNIT_DATASET.md`, `HEADING_LEXICAL_CONCORDANCE.md`, and `FREQUENCY_PROFILES.md`.

## Grammatical-terminology candidate discovery status

Generated artifacts:

- `data/grammatical-terminology-candidates.json` — **455 mechanically discovered exact-surface candidates** with provenance/evidence;
- `data/grammatical-terminology-candidates.ndjson` — streaming candidate queue;
- `indexes/grammatical-terminology-review-queue.md` — ranked human-facing discovery queue;
- `data/grammatical-terminology-candidates-validation.json` — **PASS** discovery/integrity validation;
- `data/grammatical-terminology-candidates.schema.json` — discovery schema;
- `scripts/generate_terminology_candidates.py` — deterministic generator;
- `.github/workflows/generate-terminology-candidates.yml` — reproducible generation workflow.

Discovery rule: exact frequency >=3 **or** exact non-whitespace token match in a source-supported heading.

Validated discovery counts:

- candidate surface forms: **455**;
- frequency-selected: **443**;
- heading-matched: **37**.

The frequency and heading candidate sets overlap.

Candidate IDs use stable SHA-256-derived exact-surface identity and therefore do not change merely because review rank changes.

Generated discovery files retain `unreviewed` discovery state by design; human decisions are stored separately and must not be written back into these regenerated files.

See `TERMINOLOGY_CANDIDATE_DISCOVERY.md`.

## Grammatical-terminology review status

Human review is governed by:

- `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

Editorial decisions belong only in:

- `data/grammatical-terminology-review.json`;
- schema: `data/grammatical-terminology-review.schema.json`.

Validation:

- `scripts/validate_terminology_review.py`;
- `.github/workflows/validate-terminology-review.yml`;
- `data/grammatical-terminology-review-validation.json` — **PASS**.

### Batch 001

Selection: first 20 mechanically ranked candidates carrying exact source-heading-token evidence.

Current review ledger:

- candidate surface forms: **455**;
- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**;
- unreviewed: **435**;
- status: **review-in-progress**.

The single rejected candidate is `முன்`, which is treated as an ordinary relational expression embedded in technical grammatical statements rather than a standalone technical term.

Accepted decisions are context-bounded where the same exact form has ordinary or multiple senses. The ledger explicitly separates known technical and non-technical records for mixed forms such as `உயிர்`, `எண்`, `வேற்றுமை`, `மெய்`, `சொல்`, and `மாத்திரை`.

Human-readable decision summary:

- `reviews/terminology/batch-001-decisions.md`.

Audit:

- `TERMINOLOGY_REVIEW_BATCH_001.md`.

The terminology review layer is **not complete**; 435 candidates remain unreviewed.

## Raw-source preservation status

- exact-byte preservation protocol: **documented**;
- reproducible GitHub Actions retrieval workflow: **installed**;
- current raw Project Madurai HTML committed to `main`: **not yet verified / not present**;
- SHA-256 provenance for current raw HTML: **not yet available**.

See `RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` and `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`.

Raw-source preservation remains a separate archival state from the completed canonical transcription and derived-data layers.
