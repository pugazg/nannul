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

Current canonical boundary: **462 / `நன்னூல் முற்றிற்று`**.

The nominal numbered span is 1–462, while the controlling webpage displays 460 numbered units because 73 and 176 are absent. This state is preserved rather than editorially reconstructed.

## Raw-source preservation status

- exact-byte preservation protocol: **documented**;
- reproducible GitHub Actions retrieval workflow: **installed**;
- current raw Project Madurai HTML committed to `main`: **not yet verified / not present**;
- SHA-256 provenance for current raw HTML: **not yet available**.

See `RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` and `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`.

Raw-source preservation remains a separate archival state from the completed canonical transcription.
