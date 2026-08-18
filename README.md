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

## Stable identifier / index status

**STABLE நூற்பா IDENTIFIER LAYER: ESTABLISHED AND AUDITED**

Numbered positions use `nannul-%04d`, for example `nannul-0001`, `nannul-0056`, `nannul-0258`, and `nannul-0462`.

The unnumbered சிறப்புப்பாயிரம் uses `nannul-sirappu-payiram`.

Because the controlling current webpage does not display numbered 73 or 176, `nannul-0073` and `nannul-0176` are reserved as **source-gap positions** and never point to reconstructed canonical text.

Primary artifacts:

- `structure/identifiers.yml`
- `data/nurpa-index.json`
- `indexes/nurpa-number-index.md`
- `audit/STABLE_IDENTIFIER_INDEX.md`

## Canonical unit dataset status

**ONE-RECORD-PER-CANONICAL-UNIT DATASET: GENERATED, VALIDATED, AND AUDITED**

Primary artifacts:

- `data/nurpa.json` — **460 canonical numbered records**;
- `data/nurpa.ndjson` — one canonical record per line;
- `data/nurpa-validation.json` — deterministic coverage/count/hash validation;
- `data/nurpa.schema.json` — JSON Schema contract;
- `scripts/generate_nurpa_dataset.py` — deterministic generator;
- `.github/workflows/generate-nurpa-dataset.yml` — reproducible workflow;
- `audit/CANONICAL_UNIT_DATASET.md` — dataset audit.

Validated invariant:

- nominal numbered positions: **462**;
- canonical numbered records: **460**;
- reserved source gaps: **73, 176**;
- missing expected canonical records: **none**;
- unexpected records: **none**.

## Source-heading / lexical concordance status

**SOURCE-HEADING + EXACT-SURFACE LEXICAL CONCORDANCE: GENERATED, CORRECTED, VALIDATED, AND AUDITED**

Heading layer:

- `data/source-heading-index.json` — **65 actual non-empty source-heading occurrences**;
- `indexes/source-heading-index.md` — human-facing heading index;
- one explicit unheaded span covers நூற்பாக்கள் **56–57**, before `எண்` begins at 58;
- no blank or fabricated heading is assigned to that span.

Lexical layer:

- `data/word-form-concordance.json` — **2,837 unique exact surface forms**;
- `data/token-occurrences.ndjson` — **5,431 exact token occurrences**;
- `data/concordance-validation.json` — **PASS** validation with output fingerprints;
- `scripts/generate_concordance.py` — deterministic generator;
- `.github/workflows/generate-concordance.yml` — reproducible workflow;
- `audit/HEADING_LEXICAL_CONCORDANCE.md` — formal audit.

Tokenization is deliberately lossless at the surface level: each token is an exact non-whitespace substring (`\S+`) of canonical `text_ta`. No punctuation stripping, Unicode normalization, spelling normalization, stemming, lemmatization, or sandhi splitting is applied. This keeps unusual and punctuation-bearing source forms visible rather than silently cleaning them.

## Exact-surface frequency/profile status

**SECTION / இயல் / SOURCE-HEADING FREQUENCY PROFILES: GENERATED, VALIDATED, AND AUDITED**

Primary artifacts:

- `data/frequency-profiles.json` — group summaries with top-20 exact surface forms;
- `data/frequency-tables.json` — complete exact-surface frequency tables for every group;
- `indexes/frequency-profiles.md` — human-facing whole-work and grouped profiles;
- `data/frequency-profiles-validation.json` — **PASS** reconciliation/integrity validation;
- `scripts/generate_frequency_profiles.py` — deterministic aggregation generator;
- `.github/workflows/generate-frequency-profiles.yml` — reproducible self-committing workflow;
- `audit/FREQUENCY_PROFILES.md` — formal audit.

Validated whole-work counts:

- canonical numbered records: **460**;
- exact token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**.

Validated profile dimensions:

- source-section / அதிகார-level profiles: **3**;
- இயல் / structural-unit profiles: **17**;
- actual source-heading profiles: **65**;
- explicit unheaded-span profiles: **1**.

All section, இயல், and heading-plus-unheaded token totals reconcile exactly to the global 5,431 occurrences, and token links/character offsets are revalidated against canonical `text_ta` during generation.

Frequency remains a purely descriptive mechanical layer. No frequent lexical form is automatically classified as a grammatical term.

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

See `audit/SOURCE_VARIANTS.md`. No secondary-witness reading is silently imported into canonical text or derived data.

## Completion / derived-layer audits

- `audit/EZHUTHTHATHIKARAM_COMPLETION.md`
- `audit/SOLLATHIKARAM_COMPLETION.md`
- `audit/NANNUL_CANONICAL_COMPLETION.md`
- `audit/STABLE_IDENTIFIER_INDEX.md`
- `audit/CANONICAL_UNIT_DATASET.md`
- `audit/HEADING_LEXICAL_CONCORDANCE.md`
- `audit/FREQUENCY_PROFILES.md`

## Raw-source preservation

Exact-byte preservation of the **current** Project Madurai HTML remains a separate archival gate.

Infrastructure present:

- `.github/workflows/vendor-project-madurai-source.yml`
- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`
- `audit/RAW_SOURCE_PRESERVATION_ATTEMPT_2026-08-18.md`
- raw-preservation state in `SOURCE_MANIFEST.yml`

Current raw-source status: **workflow/protocol configured, raw snapshot not yet materialized and hash-verified on `main`**.

Accordingly, `full_current_html_vendored` remains `false`. Parsed web text and the historical GitHub mirror are not substitutes for the controlling HTTP response bytes.

## Next derived-data activity

The next safe analytical milestone is a **reviewed grammatical-terminology candidate layer**.

The first phase should remain candidate discovery only: derive potentially significant repeated exact forms and source-heading cues from the validated mechanical data, attach stable நூற்பா provenance and occurrence evidence, and mark every candidate `unreviewed`. Frequency alone must never be treated as proof that a form is a grammatical technical term.
