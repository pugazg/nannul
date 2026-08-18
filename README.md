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

Current canonical boundary: **நூற்பா 462 / `நன்னூல் முற்றிற்று`**.

The nominal numbered span is 1–462. The controlling current webpage does not display numbered 73 or 176, so the completed canonical layer contains **460 displayed numbered நூற்பாக்கள்**, plus the unnumbered சிறப்புப்பாயிரம். Those source-version gaps are preserved rather than reconstructed.

## Stable identifier / index status

**STABLE நூற்பா IDENTIFIER LAYER: ESTABLISHED AND AUDITED**

Numbered positions use `nannul-%04d`; `nannul-0073` and `nannul-0176` are reserved `source-gap` positions. The unnumbered சிறப்புப்பாயிரம் uses `nannul-sirappu-payiram`.

Primary artifacts:

- `structure/identifiers.yml`
- `data/nurpa-index.json`
- `indexes/nurpa-number-index.md`
- `audit/STABLE_IDENTIFIER_INDEX.md`

## Canonical unit dataset status

**ONE-RECORD-PER-CANONICAL-UNIT DATASET: GENERATED, VALIDATED, AND AUDITED**

Primary artifacts:

- `data/nurpa.json` — **460 canonical numbered records**;
- `data/nurpa.ndjson`;
- `data/nurpa-validation.json`;
- `data/nurpa.schema.json`;
- `scripts/generate_nurpa_dataset.py`;
- `.github/workflows/generate-nurpa-dataset.yml`;
- `audit/CANONICAL_UNIT_DATASET.md`.

Validated invariant: **462 nominal numbered positions = 460 canonical records + source gaps 73 and 176**.

## Source-heading / lexical concordance status

**SOURCE-HEADING + EXACT-SURFACE LEXICAL CONCORDANCE: GENERATED, CORRECTED, VALIDATED, AND AUDITED**

- `data/source-heading-index.json` — **65 actual non-empty source-heading occurrences**;
- one explicit unheaded span covers நூற்பாக்கள் **56–57** before `எண்` begins at 58;
- `data/word-form-concordance.json` — **2,837 unique exact surface forms**;
- `data/token-occurrences.ndjson` — **5,431 exact token occurrences**;
- `data/concordance-validation.json` — **PASS**;
- `audit/HEADING_LEXICAL_CONCORDANCE.md`.

Tokenization is lossless exact non-whitespace extraction (`\S+`), with no punctuation stripping, Unicode normalization, spelling normalization, stemming, lemmatization, or sandhi splitting.

## Exact-surface frequency/profile status

**SECTION / இயல் / SOURCE-HEADING FREQUENCY PROFILES: GENERATED, VALIDATED, AND AUDITED**

- canonical records: **460**;
- token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**;
- source-section profiles: **3**;
- இயல் / structural-unit profiles: **17**;
- actual source-heading profiles: **65**;
- explicit unheaded-span profiles: **1**.

Primary artifacts include `data/frequency-profiles.json`, `data/frequency-tables.json`, `indexes/frequency-profiles.md`, `data/frequency-profiles-validation.json`, and `audit/FREQUENCY_PROFILES.md`.

Frequency remains descriptive only and never constitutes automatic grammatical classification.

## Grammatical-terminology candidate discovery status

**PHASE 1 — CANDIDATE DISCOVERY: COMPLETE, VALIDATED, AND AUDITED**

Discovery rule:

- exact surface occurrence count >= **3**, **or**
- exact non-whitespace token match in a source-supported heading.

Validated discovery result:

- exact surface forms considered: **2,837**;
- candidates: **455**;
- frequency-selected candidates: **443**;
- heading-matched candidates: **37**.

Primary generated artifacts:

- `data/grammatical-terminology-candidates.json`;
- `data/grammatical-terminology-candidates.ndjson`;
- `indexes/grammatical-terminology-review-queue.md`;
- `data/grammatical-terminology-candidates-validation.json`;
- `data/grammatical-terminology-candidates.schema.json`;
- `scripts/generate_terminology_candidates.py`;
- `.github/workflows/generate-terminology-candidates.yml`;
- `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`.

Candidate identity is stable across ranking changes: each ID is `nannul-term-candidate-<16 hex>`, derived from SHA-256 over the exact UTF-8 surface form.

Generated candidate rows remain `unreviewed` by design. They are discovery artifacts and are never overwritten with human semantic decisions.

## Grammatical-terminology contextual review status

**PHASE 2 — HUMAN/CONTEXTUAL REVIEW: IN PROGRESS**

Review policy:

- `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

Human decision ledger:

- `data/grammatical-terminology-review.json`;
- schema: `data/grammatical-terminology-review.schema.json`.

### Batch 001 — complete and audited

Selection: first **20** mechanically ranked candidates carrying exact source-heading-token evidence.

Result:

- total candidates: **455**;
- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**;
- unreviewed: **435**.

The only rejected exact form is `முன்`: internal Nannūl evidence supports it as an ordinary relational expression inside technical grammatical rules/headings rather than as a standalone grammatical term.

Accepted forms are context-bounded when necessary. The ledger explicitly distinguishes technical and known ordinary uses for mixed forms such as `உயிர்`, `எண்`, `வேற்றுமை`, `மெய்`, `சொல்`, and `மாத்திரை` rather than declaring every occurrence technical.

Review evidence/tooling:

- `reviews/terminology/batch-001-contexts.json`;
- `reviews/terminology/batch-001-contexts.md`;
- `reviews/terminology/batch-001-candidate-01.md` through `batch-001-candidate-20.md`;
- `scripts/generate_terminology_review_packet.py`;
- `scripts/split_terminology_review_packet.py`;
- `.github/workflows/generate-terminology-review-packet.yml`.

The review packet distinguishes **heading-only evidence** from exact body-token evidence and never fabricates a body occurrence merely because a source heading contains the candidate.

Review validation:

- `scripts/validate_terminology_review.py`;
- `.github/workflows/validate-terminology-review.yml`;
- `data/grammatical-terminology-review-validation.json` — **PASS**;
- `reviews/terminology/batch-001-decisions.md` — human-readable decision summary;
- `audit/TERMINOLOGY_REVIEW_BATCH_001.md` — formal audit.

The terminology layer is **not complete**: **435 candidates remain unreviewed**.

## Documented source-version findings

The canonical edition follows the current Project Madurai webpage. Differences documented against the older official Project Madurai GitHub mirror include:

- missing displayed 73 in the current webpage;
- missing displayed 176 in the current webpage;
- historical numbering anomaly around 240–242;
- நூற்பா 343: current `செய்தனெ` vs historical `செய்தென`;
- நூற்பா 344: current trailing `"` after `பிற` vs no trailing quote in the historical mirror.

See `audit/SOURCE_VARIANTS.md`. No secondary-witness reading is silently imported into canonical text or derived data.

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

## Raw-source preservation

Exact-byte preservation of the **current** Project Madurai HTML remains a separate archival gate.

Infrastructure present:

- `.github/workflows/vendor-project-madurai-source.yml`
- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`
- `audit/RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md`
- raw-preservation state in `SOURCE_MANIFEST.yml`.

Current raw-source status: **workflow/protocol configured, raw snapshot not yet materialized and hash-verified on `main`**. `full_current_html_vendored` therefore remains `false`.

## Next analytical activity

Continue **Phase 2 contextual terminology review** with the remaining source-heading-supported candidates before moving to candidates supported only by frequency.

The next batch should use the same boundaries established in Batch 001: stable candidate identity, internal canonical contexts first, explicit heading/body evidence distinction, mixed-use recording, separate human decision ledger, and post-review structural/provenance validation.
