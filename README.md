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

## Raw-source preservation

Exact-byte preservation of the **current** Project Madurai HTML is tracked separately from canonical completion.

Infrastructure now present:

- `.github/workflows/vendor-project-madurai-source.yml` — reproducible direct-HTTP fetch/checksum workflow;
- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md` — archival protocol and completion gate;
- `audit/RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md` — dated retrieval-attempt audit;
- `SOURCE_MANIFEST.yml` raw-preservation state and target paths.

Current raw-source status: **workflow/protocol configured, raw snapshot not yet materialized and hash-verified on `main`**.

Accordingly, `full_current_html_vendored` remains `false`. Parsed web text and the historical GitHub mirror are not accepted as substitutes for the controlling HTTP response bytes.

## Remaining work outside canonical transcription

The immediate unresolved archival gate is materializing and SHA-256-verifying the current raw Project Madurai HTML under `sources/project-madurai/pmuni0147/raw/`.

After that gate passes, future work can proceed in separate layers such as stable நூற்பா IDs and indexes, machine-readable structured data, commentary, comparative grammar, translations, and critical/source comparison. These must not silently alter the completed canonical Tamil layer.
