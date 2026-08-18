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
4. Keep commentary, interpretation, translations, and computational data separate from canonical Tamil.
5. Make grammatical units addressable by stable identifiers.
6. Treat source discrepancies as audit findings, not opportunities for silent correction.

## Canonical Tamil status

**SOURCE-DERIVED CANONICAL TAMIL INGESTION: COMPLETE**

- சிறப்புப்பாயிரம் — canonicalized;
- பொதுப்பாயிரம் 1–55 — canonicalized;
- எழுத்ததிகாரம் 56–257 — canonicalized and fully audited;
- சொல்லதிகாரம் 258–462 — canonicalized and fully audited.

Current canonical boundary: **நூற்பா 462 / `நன்னூல் முற்றிற்று`**.

The nominal numbered span is 1–462. The controlling current webpage does not display 73 or 176, so the canonical numbered layer contains **460 displayed records**, with those two positions preserved as source gaps rather than reconstructed.

## Stable identifier / canonical data status

**STABLE-ID + ONE-RECORD-PER-CANONICAL-UNIT LAYERS: COMPLETE AND AUDITED**

- numbered stable IDs: `nannul-%04d`;
- source gaps: `nannul-0073`, `nannul-0176`;
- canonical data: `data/nurpa.json` — **460 records**;
- streaming form: `data/nurpa.ndjson`;
- validation: `data/nurpa-validation.json` — **PASS**.

Audits:

- `audit/STABLE_IDENTIFIER_INDEX.md`;
- `audit/CANONICAL_UNIT_DATASET.md`.

## Heading / lexical / frequency status

**SOURCE-HEADING + EXACT-SURFACE LEXICAL + FREQUENCY LAYERS: GENERATED, VALIDATED, AND AUDITED**

Validated baseline:

- source-heading occurrences: **65**;
- one explicit unheaded span: நூற்பாக்கள் 56–57;
- exact token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax forms: **2,037**.

Tokenization is exact non-whitespace (`\S+`) extraction with no punctuation stripping, Unicode normalization, spelling normalization, stemming, lemmatization, or sandhi splitting.

Primary audits:

- `audit/HEADING_LEXICAL_CONCORDANCE.md`;
- `audit/FREQUENCY_PROFILES.md`.

## Grammatical-terminology candidate discovery

**PHASE 1 — COMPLETE, VALIDATED, AND AUDITED**

Discovery rule:

- exact surface occurrence count >= 3, **or**
- exact non-whitespace token match in a source-supported heading.

Validated discovery result:

- exact surface forms considered: **2,837**;
- candidate surface forms: **455**;
- frequency-selected candidates: **443**;
- source-heading-supported candidates: **37**.

Candidate identity is stable across ranking changes: `nannul-term-candidate-<16 hex>`, derived from SHA-256 over the exact UTF-8 surface form.

Generated discovery artifacts remain separate from human decisions.

Audit: `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`.

## Grammatical-terminology contextual review

**PHASE 2 — IN PROGRESS; BATCHES 001–002 COMPLETE AND AUDITED**

Review policy:

- `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

Human decision ledger:

- `data/grammatical-terminology-review.json`.

Current validated ledger:

- candidates: **455**;
- reviewed: **37**;
- accepted: **33**;
- rejected: **4**;
- needs-context: **0**;
- unreviewed: **418**;
- layer status: **review-in-progress**.

Validation:

- `data/grammatical-terminology-review-validation.json` — **PASS**;
- `scripts/validate_terminology_review.py`;
- `.github/workflows/validate-terminology-review.yml`.

### Batch 001

Selection: first 20 mechanically ranked source-heading-supported candidates.

Result:

- **20 reviewed**;
- **19 accepted**;
- **1 rejected** — `முன்`;
- **0 needs-context**.

Audit: `audit/TERMINOLOGY_REVIEW_BATCH_001.md`.

### Batch 002

Selection: the remaining **17 source-heading-supported candidates**.

Result:

- **17 reviewed**;
- **14 accepted**;
- **3 rejected** — `பொதுப்`, `சொல்லின்`, `சிறப்புப்`;
- **0 needs-context**.

Accepted Batch-002 forms include `பதம்`, `வேற்றுமைப்`, `வினையெச்சம்`, `விகுதி`, `போலி`, `இலக்கணம்`, `உருபுகள்`, `பொருள்கோள்`, `இகர`, `பிறப்பு`, `உருவம்`, `அகர`, `ஒழிபு`, and `பெயரெச்சம்`.

Audit: `audit/TERMINOLOGY_REVIEW_BATCH_002.md`.

### Heading-supported tier complete

Phase-1 discovery identified **37 candidates with exact source-heading-token evidence**.

- Batch 001 reviewed 20;
- Batch 002 reviewed 17.

Therefore **all 37 source-heading-supported candidates now have explicit contextual decisions**.

The next review tier starts with the highest-priority **frequency-only** candidates. Frequency remains a prioritization signal only; it is never automatic termhood.

## Documented source-version findings

The canonical edition follows the current Project Madurai webpage. Documented differences against the older official Project Madurai GitHub mirror include:

- current webpage omits displayed 73;
- current webpage omits displayed 176;
- historical numbering anomaly around 240–242;
- நூற்பா 343: current `செய்தனெ` vs historical `செய்தென`;
- நூற்பா 344: current trailing `"` after `பிற` vs no trailing quote in the historical mirror.

See `audit/SOURCE_VARIANTS.md`.

## Completion / derived-layer audits

- `audit/EZHUTHTHATHIKARAM_COMPLETION.md`
- `audit/SOLLATHIKARAM_COMPLETION.md`
- `audit/NANNUL_CANONICAL_COMPLETION.md`
- `audit/STABLE_IDENTIFIER_INDEX.md`
- `audit/CANONICAL_UNIT_DATASET.md`
- `audit/HEADING_LEXICAL_CONCORDANCE.md`
- `audit/FREQUENCY_PROFILES.md`
- `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_001.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_002.md`

## Raw-source preservation

Exact-byte preservation of the **current** Project Madurai HTML remains a separate archival gate.

Infrastructure is present, but the raw snapshot is not yet materialized and SHA-256-verified on `main`; `full_current_html_vendored` therefore remains `false`.

## Next analytical activity

Begin **Phase 2 Batch 003** with roughly **20–25 highest-priority unreviewed frequency-only candidates**.

Use the same controls established in Batches 001–002: stable exact-surface identity, internal canonical contexts first, explicit mixed-use handling, separate human decision ledger, and post-review structural/provenance validation.
