# நன்னூல் — Nannūl

A source-faithful digital repository for **பவணந்தி முனிவர் அருளிய நன்னூல்**, one of the major works of Tamil grammatical tradition.

## Current controlling digital source

- **Project Madurai eText:** `pmuni0147`
- Source page: https://www.projectmadurai.org/pm_etexts/utf8/pmuni0147.html
- Format: Tamil Unicode eText
- Work: **நன்னூல்**
- Author: **பவணந்தி முனிவர்**
- Source edition note: Project Madurai states that the Unicode text conforms to the edition edited by Mani Thirunavukkarasu Mudaliar and published by Vavilla Ramasamy Sastrulu & Sons, Madras, 1926.

The Project Madurai header and provenance must be preserved whenever its supplied text is archived or redistributed.

## Repository principles

1. Preserve source text separately from editorial or normalized representations.
2. Do not silently modernize spelling, punctuation, segmentation, or wording.
3. Record provenance for every imported source.
4. Keep commentary, interpretation, translations, and computational data separate from the canonical Tamil text.
5. Make every grammatical unit addressable by stable identifiers.
6. Treat source discrepancies as audit findings, not opportunities for silent correction.

## Source structure

The Project Madurai eText presents:

- சிறப்புப்பாயிரம்
- பொதுப்பாயிரம் — நூற்பா 1–55
- எழுத்ததிகாரம் — நூற்பா 56–257
- சொல்லதிகாரம் — நூற்பா 258–462

Detailed இயல்-level ranges are recorded in `structure/sections.yml`.

## Canonical status

**SOURCE-DERIVED CANONICAL TAMIL INGESTION: COMPLETE**

- சிறப்புப்பாயிரம் — **canonicalized**
- பொதுப்பாயிரம் 1–55 — **canonicalized**
- எழுத்ததிகாரம் 56–257 — **canonicalized and audited in full**
- சொல்லதிகாரம் 258–462 — **canonicalized and audited in full**
  - பெயரியல் 258–319 — complete
  - வினையியல் 320–351 — complete
  - பொதுவியல் 352–419 — complete
  - இடையியல் 420–441 — complete
  - உரியியல் 442–462 — complete

Current canonical boundary: **நூற்பா 462 / `நன்னூல் முற்றிற்று`**.

## Stable identifier / index status

**STABLE நூற்பா IDENTIFIER LAYER: ESTABLISHED AND AUDITED**

Numbered positions use the deterministic identifier scheme:

`nannul-%04d`

Examples: `nannul-0001`, `nannul-0056`, `nannul-0258`, `nannul-0462`.

The unnumbered சிறப்புப்பாயிரம் uses:

`nannul-sirappu-payiram`

Because the controlling current webpage does not display numbered 73 or 176, `nannul-0073` and `nannul-0176` are reserved as **source-gap positions** and do not point to reconstructed canonical text.

Structural/index artifacts:

- `structure/identifiers.yml`
- `data/nurpa-index.json`
- `indexes/nurpa-number-index.md`
- `audit/STABLE_IDENTIFIER_INDEX.md`

This layer is derived metadata only; canonical Tamil files were not rewritten to insert IDs.

## Canonical unit dataset status

**ONE-RECORD-PER-CANONICAL-UNIT DATASET: GENERATED, VALIDATED, AND AUDITED**

Primary artifacts:

- `data/nurpa.json` — complete dataset object with **460 canonical numbered records**;
- `data/nurpa.ndjson` — one canonical record per line;
- `data/nurpa-validation.json` — deterministic coverage/count/hash validation;
- `data/nurpa.schema.json` — JSON Schema contract;
- `scripts/generate_nurpa_dataset.py` — deterministic generator;
- `.github/workflows/generate-nurpa-dataset.yml` — reproducible generation workflow;
- `audit/CANONICAL_UNIT_DATASET.md` — completed dataset audit.

Each record carries stable ID, source number, exact canonical Tamil text, structural parents, nearest source-supported topic heading, canonical-file provenance, controlling-source status, and applicable source-variant references.

Validated invariant:

- nominal numbered positions: **462**;
- canonical numbered records: **460**;
- reserved source gaps: **73, 176**;
- missing expected canonical records: **none**;
- unexpected records: **none**;
- unique stable IDs: **460**.

The dataset does not reconstruct either source gap and does not alter canonical Tamil.

## Numbering state of the controlling source

The nominal numbered span is **1–462**. The current Project Madurai webpage does not display numbered **73** or **176**, so the completed canonical layer contains **460 displayed numbered நூற்பாக்கள்**, plus the unnumbered சிறப்புப்பாயிரம்.

Those source-version gaps are preserved rather than silently reconstructed.

## Documented source-version findings

The canonical edition follows the current Project Madurai webpage. Differences documented against the older official Project Madurai GitHub mirror include:

- missing displayed 73 in the current webpage;
- missing displayed 176 in the current webpage;
- historical numbering anomaly around 240–242;
- நூற்பா 343: current `செய்தனெ` vs historical `செய்தென`;
- நூற்பா 344: current trailing `"` after `பிற` vs no trailing quote in the historical mirror.

See `audit/SOURCE_VARIANTS.md` and the batch audit files. No secondary-witness reading is silently imported into canonical text.

## Completion audits

- `audit/EZHUTHTHATHIKARAM_COMPLETION.md`
- `audit/SOLLATHIKARAM_COMPLETION.md`
- `audit/NANNUL_CANONICAL_COMPLETION.md`
- `audit/STABLE_IDENTIFIER_INDEX.md`
- `audit/CANONICAL_UNIT_DATASET.md`

## Raw-source preservation

Exact-byte preservation of the **current** Project Madurai HTML is tracked separately from canonical completion.

Infrastructure present:

- `.github/workflows/vendor-project-madurai-source.yml` — reproducible direct-HTTP fetch/checksum workflow;
- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md` — archival protocol and completion gate;
- `audit/RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` — dated retrieval-attempt audit;
- `SOURCE_MANIFEST.yml` raw-preservation state and target paths.

Current raw-source status: **workflow/protocol configured, raw snapshot not yet materialized and hash-verified on `main`**.

Accordingly, `full_current_html_vendored` remains `false`. Parsed web text and the historical GitHub mirror are not accepted as substitutes for the controlling HTTP response bytes.

## Next derived-data activity

With stable IDs and the 460-record canonical dataset established, the next safe source-derived milestone is a **source-supported topic-heading / concordance layer**:

1. index every distinct source heading and the stable நூற்பா IDs governed by it;
2. build a lossless lexical concordance from the canonical `text_ta` field without spelling normalization;
3. keep later grammatical-term interpretation separate from this purely derived lexical layer.

That will provide a reliable basis for search, terminology study, commentary linking, and later comparison with Tolkāppiyam or other Tamil grammatical works without changing the canonical source layer.
