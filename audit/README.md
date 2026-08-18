# Audit

Verification records, discrepancies, and editorial decisions belong here.

Each audit should identify:

- source and version checked;
- நூற்பா or section range;
- verification method;
- source anomalies or suspected errors;
- unresolved readings;
- any repository-side transformation made for structure or encoding.

The audit layer exists so that the canonical Tamil text remains traceable and corrections are never silent.

## Current audit records

- `SOURCE_VARIANTS.md` — differences between the controlling Project Madurai webpage and secondary/historical witnesses.
- `CANONICAL_INGEST_056_127.md` — எழுத்து இயல் 56–127.
- `CANONICAL_INGEST_128_150.md` — பதவியல் 128–150.
- `CANONICAL_INGEST_151_203.md` — உயிரீற்றுப் புணரியல் 151–203.
- `CANONICAL_INGEST_204_239.md` — மெய்யீற்றுப் புணரியல் 204–239.
- `CANONICAL_INGEST_240_257.md` — உருபு புணரியல் 240–257.
- `EZHUTHTHATHIKARAM_COMPLETION.md` — authority-level completion audit for எழுத்ததிகாரம் 56–257.
- `CANONICAL_INGEST_258_319.md` — பெயரியல் 258–319.

## Current findings

- `PM147-V001`: controlling webpage omits displayed numbered 73 between 72 and 74; canonical handling applied without restoring the secondary-witness text.
- `PM147-V002`: historical-witness numbering anomaly around 240–242; canonical handling applied using the current webpage's 240, 241, 242 sequence.
- `PM147-V003`: controlling webpage omits displayed numbered 176 between 175 and 177; canonical handling applied without restoring the secondary-witness text.
- பதவியல் 128–150: continuous numbering; no source-numbering discrepancy observed.
- மெய்யீற்றுப் புணரியல் 204–239: continuous numbering; no source-numbering discrepancy observed.
- உருபு புணரியல் 240–257: continuous numbering in the controlling current webpage.
- பெயரியல் 258–319: continuous numbering; no source-numbering discrepancy observed.

## Verification progress

- சிறப்புப்பாயிரம்: canonicalized.
- பொதுப்பாயிரம் 1–55: canonicalized.
- எழுத்ததிகாரம் 56–257: **canonicalized and fully batch-audited**.
- சொல்லதிகாரம்:
  - பெயரியல் 258–319: **canonicalized and batch-audited**.
  - next: வினையியல் 320–351.

Current canonical boundary: **319**.

The complete source must eventually be verified through நூற்பா 462 before the whole canonical Tamil layer can be declared source-verified.
