# Stable Identifier / Canonical Index Audit

## Scope

This audit covers the first post-transcription structural layer for **நன்னூல்**:

- stable identifier policy;
- deterministic numbered namespace;
- source-gap handling;
- machine-readable segment index;
- human-facing number index.

No canonical Tamil text was modified in this activity.

## Inputs

- `docs/ARCHIVAL_GUIDELINES.md`
- `structure/sections.yml`
- completed and audited canonical Tamil files under `text/tamil/`
- `audit/SOURCE_VARIANTS.md`
- `audit/NANNUL_CANONICAL_COMPLETION.md`

## Identifier scheme

Numbered positions use:

`nannul-%04d`

Examples:

- 1 → `nannul-0001`
- 56 → `nannul-0056`
- 258 → `nannul-0258`
- 462 → `nannul-0462`

The unnumbered சிறப்புப்பாயிரம் is represented separately as:

`nannul-sirappu-payiram`

## Namespace integrity

Nominal numbered positions: **462**.

Controlling-witness canonical numbered units: **460**.

Reserved source-gap positions: **2**:

- `nannul-0073` / 73 / `PM147-V001`;
- `nannul-0176` / 176 / `PM147-V003`.

Those two identifiers are reserved only to keep the namespace stable across the nominal source numbering. They do not assert that canonical text exists for 73 or 176.

Therefore:

- 462 deterministic numeric identifiers are addressable;
- 460 resolve to canonical Tamil units;
- 2 resolve explicitly to `source-gap` status;
- no reconstructed source text is introduced.

## Structural coverage

The machine-readable segment map covers the complete nominal range without overlap or uncovered positions:

- பொதுப்பாயிரம் 1–55;
- எழுத்ததிகாரம் 56–257;
- சொல்லதிகாரம் 258–462.

Within பொதுப்பாயிரம், the source-supported subsection ranges from `structure/sections.yml` are retained in the machine index.

Within எழுத்ததிகாரம் and சொல்லதிகாரம், each இயல் resolves to its existing canonical file.

## Files created

- `structure/identifiers.yml`
- `data/nurpa-index.json`
- `indexes/nurpa-number-index.md`

## Separation of layers

The identifier/index layer is derived metadata only.

It does not:

- insert IDs into canonical Tamil lines;
- renumber source units;
- reconstruct source gaps;
- normalize source wording;
- modify punctuation or spacing;
- import historical-witness readings.

Future applications, APIs, commentary, translations, and cross-work mappings should use these stable IDs as external references rather than rewriting the canonical source layer.

## Raw-source preservation dependency

The exact-byte Project Madurai raw HTML preservation gate remains open and is independently tracked under:

- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`;
- `audit/RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md`.

Stable IDs are derived from the already completed canonical/audited structure and do not change the status of that raw-source gate.

## Result

**PASS — a deterministic stable identifier namespace and canonical number/segment index are established without modifying the completed canonical Tamil transcription.**

Recommended next structural activity: generate a one-record-per-canonical-unit dataset carrying stable ID, source number, structural parents, canonical file, and source-gap-safe provenance fields; then validate its 460 canonical records against the audited canonical files.
