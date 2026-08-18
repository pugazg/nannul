# Exact-Surface Frequency Profile Audit

## Scope

This audit covers the deterministic frequency/profile layer for **நன்னூல்**.

The layer aggregates already-audited derived data from:

- `data/nurpa.json` — 460 canonical numbered records;
- `data/token-occurrences.ndjson` — 5,431 exact token occurrences;
- `data/source-heading-index.json` — source-supported heading occurrences and the explicit unheaded span;
- `data/concordance-validation.json` — required upstream PASS gate.

No canonical Tamil file is edited, and this activity does not re-tokenize the source.

## Generator and workflow

- generator: `scripts/generate_frequency_profiles.py`
- workflow: `.github/workflows/generate-frequency-profiles.yml`

Generated outputs:

- `data/frequency-profiles.json`
- `data/frequency-tables.json`
- `indexes/frequency-profiles.md`
- `data/frequency-profiles-validation.json`

The workflow regenerates the profiles on relevant `main` changes and commits generated outputs only when they differ.

## Aggregation policy

The frequency unit is the already-validated exact `surface_form` from `data/token-occurrences.ndjson`.

This activity performs **no**:

- re-tokenization;
- punctuation stripping;
- Unicode normalization;
- spelling normalization;
- stemming or lemmatization;
- sandhi splitting;
- grammatical-term classification;
- semantic grouping.

Group ordering follows first canonical source occurrence. Within each frequency table, exact forms are ordered by:

1. descending occurrence count;
2. first global occurrence;
3. exact surface form as a deterministic final tie-break.

The summary profile retains the top 20 exact forms for each group. `data/frequency-tables.json` retains the complete exact-surface frequency table for every group.

## Validated profile dimensions

The final generated layer contains:

- source-section / அதிகார-level profiles: **3**;
- இயல் / structural-unit profiles: **17**;
- actual source-heading occurrence profiles: **65**;
- explicit unheaded-span profiles: **1**.

The unheaded profile corresponds to நூற்பாக்கள் **56–57**, matching the already-audited heading model; it is not assigned a fabricated heading.

## Whole-work result

Validated exact-surface totals:

- canonical numbered records: **460**;
- token occurrences: **5,431**;
- unique exact surface forms: **2,837**;
- hapax exact surface forms: **2,037**.

The whole-work leading exact forms in the generated profile begin:

- `ஆகும்` — 73;
- `ஐ` — 32;
- `முதல்` — 31;
- `ஈர்` — 25;
- `முன்` — 24.

These are mechanical surface counts only. Frequency does not imply grammatical-term status.

## Section-level reconciliation

The three source-section / அதிகார-level divisions reconcile as follows:

| Section | Records | Token occurrences | Unique exact forms | Hapax forms |
|---|---:|---:|---:|---:|
| பொதுப்பாயிரம் | 55 | 864 | 725 | 639 |
| எழுத்ததிகாரம் | 200 | 2,282 | 1,223 | 891 |
| சொல்லதிகாரம் | 205 | 2,285 | 1,399 | 1,029 |

Section token totals sum exactly to **5,431**.

## Integrity validation

`data/frequency-profiles-validation.json` reports **PASS**.

All checks pass, including:

- canonical record count remains 460;
- stable record IDs remain unique;
- canonical numbers match the expected set 1–462 excluding source gaps 73 and 176;
- 73 and 176 remain absent;
- input token occurrence count is exactly 5,431;
- every token record ID, structural field, heading field, and stored character offset still matches the canonical record;
- global token and surface-form counts reconcile;
- section token totals reconcile to the global total;
- இயல் token totals reconcile to the global total;
- source-heading plus unheaded token totals reconcile to the global total;
- section and இயல் record groupings each cover all canonical records once in source order;
- source-heading plus unheaded record grouping covers every canonical record exactly once;
- heading/unheaded profile counts match the audited heading index;
- every full frequency table reconciles to its group's token total.

No token-link failure remains.

## Output fingerprints

Final generated SHA-256 fingerprints:

- `data/frequency-profiles.json` — `9faf914312835823e23511f3af0c9bde564d53df6ea3be21146dc7446db7d4f4`
- `data/frequency-tables.json` — `cc91cd5608280eea0e7f79969a136ef06cb9f0029be97e3acb2244b62dcbee27`
- `indexes/frequency-profiles.md` — `84acee313fc20167a10b5ccc4f58c5d4145a07de8f2743030f6f7c093e466101`

The fingerprints are recorded by the reproducible validation output.

## Layer separation

This milestone is purely derived and mechanical.

It does not:

- rewrite canonical Tamil;
- reconstruct source gaps 73 or 176;
- alter documented source variants;
- normalize lexical forms;
- declare any frequent word to be a grammatical technical term;
- infer equivalence between differently spelled or punctuated surface forms;
- introduce Tolkāppiyam, commentary, or other external-witness interpretations.

## Raw-source preservation dependency

The exact-byte current Project Madurai raw-HTML preservation gate remains independently open. This frequency milestone neither depends on nor changes that archival state.

## Result

**PASS — exact-surface frequency profiles and complete group frequency tables are reproducibly generated and reconciled across all 460 canonical numbered records, 5,431 token occurrences, 17 structural units, 65 source-heading occurrences, and the single explicit unheaded span without modifying canonical Tamil.**

## Suitable next activity

The next layer may begin a **reviewed grammatical-terminology candidate dataset**.

That layer must remain explicitly analytical. A safe first phase is candidate discovery only: derive high-value repeated exact forms and source-heading cues, attach provenance and occurrence evidence, and mark every candidate `unreviewed` rather than asserting grammatical meaning automatically.
