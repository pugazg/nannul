# Source Heading / Lexical Concordance Audit

## Scope

This audit covers the reproducible derived heading and lexical-concordance layer for **நன்னூல்**.

The layer is generated from the already validated one-record-per-canonical-unit dataset:

`data/nurpa.json`

No canonical Tamil file under `text/tamil/` is modified by this activity.

## Generator and workflow

- generator: `scripts/generate_concordance.py`
- workflow: `.github/workflows/generate-concordance.yml`

Generated outputs:

- `data/source-heading-index.json`
- `indexes/source-heading-index.md`
- `data/word-form-concordance.json`
- `data/token-occurrences.ndjson`
- `data/concordance-validation.json`

## Source-heading model

The heading index records only **non-empty source-supported headings** already represented by the canonical Markdown-derived `topic_heading_ta` field.

Validation result:

- canonical numbered records covered: **460**;
- actual source-heading occurrences: **65**;
- distinct exact heading texts: **65**;
- unheaded source spans: **1**;
- records in unheaded spans: **2**.

### Unheaded span 56–57

நூற்பாக்கள் **56–57** in `எழுத்து இயல்` occur before the first internal source heading `எண்`, which begins with நூற்பா 58.

The first generator version exposed this as an empty heading occurrence. That representation was rejected during audit review and the generator was corrected.

The final model therefore records 56–57 separately as:

- status: `no-internal-source-heading`;
- no fabricated or empty source heading;
- the next actual heading occurrence is `எண்` beginning at 58.

This correction affected only derived heading metadata. Canonical Tamil was unchanged.

## Exact-surface lexical policy

A lexical token is defined mechanically as an **exact non-whitespace substring** matched by Python regular expression `\S+` over each canonical record's `text_ta`.

The generator deliberately performs **no**:

- punctuation stripping;
- Unicode normalization;
- spelling normalization;
- stemming or lemmatization;
- sandhi splitting;
- grammatical interpretation;
- editorial token merging or splitting.

Therefore punctuation-bearing and unusual source-supported forms remain distinct exact surface forms. For example, punctuation attached to a word remains part of that token; the source-supported trailing quotation mark in நூற்பா 344 is not silently removed by the concordance layer.

Each token occurrence records:

- global occurrence index;
- exact surface form;
- stable நூற்பா record ID;
- source number;
- section and structural unit IDs;
- source-supported topic heading when present;
- exact character start/end offsets within `text_ta`;
- line number;
- starting column;
- token position within the line.

## Lexical result

Final validated counts:

- canonical records processed: **460**;
- token occurrences: **5,431**;
- unique exact surface forms: **2,837**.

`data/word-form-concordance.json` groups occurrences by exact surface form in first-source-occurrence order.

`data/token-occurrences.ndjson` preserves one occurrence per line for streaming/search/indexing use.

## Coverage and integrity validation

`data/concordance-validation.json` reports **PASS**.

All of the following checks pass:

- canonical record count is 460;
- stable record IDs are unique;
- source numbers are unique;
- source numbers match the expected canonical set;
- reserved gaps 73 and 176 are absent from canonical records;
- heading occurrences plus unheaded spans cover all 460 records exactly once in source order;
- every heading occurrence has a non-empty source-supported heading;
- every token is verified as the exact substring at its stored character offsets;
- sum of per-form occurrence counts equals total token occurrences;
- every surface form is non-empty.

No missing expected canonical number, unexpected number, or substring validation failure remains.

## Output fingerprints

The corrected validated outputs have SHA-256 fingerprints:

- `data/source-heading-index.json` — `65591573d351f86dd19c1bd4b9c6359e275190244c8e9248d8cfcb799c6912f0`
- `indexes/source-heading-index.md` — `8582d23f82357697d743f48d9e9d1895d1512203768231c6464bafad6ed3d096`
- `data/word-form-concordance.json` — `1d525db1ed62a810fe65ffc6c345691ad594707f5badd5a3fb9ed2792d4e8a86`
- `data/token-occurrences.ndjson` — `078ed8c4e8ed71b081efa41fffe99e51cc9989f6d6e966f4a070100e81e62a44`

These hashes are also recorded by the reproducible validation output.

## Layer separation

This activity is a derived-data operation only.

It does not:

- rewrite canonical Tamil;
- create text for missing 73 or 176;
- normalize source spellings;
- alter documented variants at 240–242, 343, or 344;
- promote lexical surface forms to grammatical interpretations;
- change the controlling-source policy.

## Raw-source preservation dependency

The exact-byte current Project Madurai raw-HTML preservation gate remains independently open. This concordance milestone neither depends on nor changes `full_current_html_vendored: false`.

## Result

**PASS — the source-supported heading index and exact-surface lexical concordance are generated, corrected, validated, fingerprinted, and audited across all 460 canonical numbered Nannūl records without modifying canonical Tamil.**

A suitable next derived-data milestone is to build deterministic **frequency/profile summaries by அதிகாரம், இயல், and source heading**, followed separately by an explicitly reviewed grammatical-terminology candidate layer. Frequency data can remain mechanical; grammatical-term classification must remain analytical and auditable.
