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

Current canonical boundary: **462 / `நன்னூல் முற்றிற்று`**.

The nominal numbered span is 1–462, while the controlling webpage displays 460 numbered units because 73 and 176 are absent. The stable namespace reserves those two positions as `source-gap`; downstream datasets contain only the 460 actually displayed canonical numbered units.

## Canonical unit dataset status

Generated artifacts:

- `data/nurpa.json` — 460 canonical records plus dataset/source-gap metadata;
- `data/nurpa.ndjson` — 460 streaming records;
- `data/nurpa-validation.json` — **PASS** validation with coverage counts and hashes;
- `data/nurpa.schema.json` — dataset contract;
- `scripts/generate_nurpa_dataset.py` — deterministic generator;
- `.github/workflows/generate-nurpa-dataset.yml` — reproducible generation workflow.

See `CANONICAL_UNIT_DATASET.md`.

## Heading / lexical concordance status

Generated artifacts:

- `data/source-heading-index.json` — **65 actual non-empty source-heading occurrences** plus one explicit unheaded span;
- `indexes/source-heading-index.md` — human-facing heading index;
- `data/word-form-concordance.json` — **2,837 unique exact surface forms**;
- `data/token-occurrences.ndjson` — **5,431 exact token occurrences**;
- `data/concordance-validation.json` — **PASS** coverage/integrity validation;
- `scripts/generate_concordance.py` — deterministic generator;
- `.github/workflows/generate-concordance.yml` — reproducible generation workflow.

நூற்பாக்கள் **56–57** are correctly recorded as an unheaded source span before the first internal heading `எண்` at 58; no empty heading is fabricated.

Tokenization is exact `\S+` surface extraction with no punctuation stripping, Unicode normalization, spelling normalization, stemming, lemmatization, or sandhi splitting.

See `HEADING_LEXICAL_CONCORDANCE.md`.

## Raw-source preservation status

- exact-byte preservation protocol: **documented**;
- reproducible GitHub Actions retrieval workflow: **installed**;
- current raw Project Madurai HTML committed to `main`: **not yet verified / not present**;
- SHA-256 provenance for current raw HTML: **not yet available**.

See `RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` and `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`.

Raw-source preservation remains a separate archival state from the completed canonical transcription and derived-data layers.
