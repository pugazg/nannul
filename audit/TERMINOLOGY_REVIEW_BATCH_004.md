# Grammatical-Terminology Contextual Review — Batch 004 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 004** for Nannūl.

Batch ID:

`NANNUL-TERM-REVIEW-004`

Selection policy:

- the **next 25 highest-priority unreviewed candidates with no exact source-heading-token evidence** after Batches 001–003;
- mechanical frequency/structural breadth determined review order only and was never treated as semantic confidence;
- decisions use internal canonical Nannūl contexts only under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No Tolkāppiyam, commentary, dictionary, later grammar, or modern scholarship evidence was used for these first-pass decisions.

## Evidence tooling

Batch-004 evidence generator:

- `scripts/generate_terminology_review_batch_004.py`;
- `.github/workflows/generate-terminology-review-batch-004.yml`.

Generated evidence:

- `reviews/terminology/batch-004-contexts.json`;
- `reviews/terminology/batch-004-contexts.md`;
- `reviews/terminology/batch-004-candidate-01.md` through `batch-004-candidate-25.md`.

The generator reuses the deterministic frequency-only review sampling established in Batch 003: complete occurrence coverage for modest-frequency forms, otherwise first/last occurrence, structural-unit coverage, evenly distributed samples, and any source-variant-linked records.

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

Batch 004 decisions:

- reviewed: **25**;
- accepted: **16**;
- rejected: **9**;
- needs-context: **0**.

### Accepted exact forms

- `ப` — `phonology-letter-class`;
- `ல` — `phonology-letter-class`;
- `முன்னிலை` — `other-grammar`;
- `ஏ` — `phonology-letter-class`;
- `இறுதி` — `morphology`;
- `ஓ` — `phonology-letter-class`;
- `வினா` — `syntax`;
- `அல்` — `morphology`;
- `க` — `phonology-letter-class`;
- `த` — `phonology-letter-class`;
- `ஞ` — `phonology-letter-class`;
- `ந` — `phonology-letter-class`;
- `அற்று` — `morphology`;
- `படர்க்கை` — `other-grammar`;
- `குறில்` — `phonology-letter-class`;
- `வ` — `phonology-letter-class`.

### Rejected exact forms

- `வழி`;
- `பிற`;
- `ஆதி`;
- `பிறவும்`;
- `மூ`;
- `இவை`;
- `ஓர்`;
- `எனும்`;
- `பெயரே`.

## Review findings

### Letter symbols remain independently useful terminology

Seven consonant symbols in this batch — `ப`, `ல`, `க`, `த`, `ஞ`, `ந`, `வ` — are directly enumerated and repeatedly manipulated as Tamil letters in phonological rules. Several also appear as grammatical endings or intermediate forms. They are accepted with exact-surface identity preserved rather than merged into broad letter classes.

The vowel symbols `ஏ` and `ஓ` are likewise accepted from explicit letter-class evidence and retain notes for additional grammatical uses.

### Person/deixis terminology is explicit

`முன்னிலை` and `படர்க்கை` are accepted because Nannūl explicitly organizes `தன்மை`, `முன்னிலை`, and `படர்க்கை` as grammatical person/deictic positions and systematically assigns pronouns and verbal forms to them.

### Frequency does not rescue ordinary enumerative language

The following high-frequency forms are rejected as independent terminology:

- `பிற`, `பிறவும்` — residual/“other(s)” expressions;
- `ஆதி` — “beginning with / and so on” enumerative language;
- `மூ`, `ஓர்` — numeral forms;
- `இவை` — demonstrative discourse reference;
- `வழி` — ordinary relational “way/by/through” usage.

Their grammatical surroundings do not make the exact surfaces standalone technical terms.

### Exact-form restraint continues

`எனும்` is rejected as a compositional quotative/attributive form related to the already reviewed `என` rather than a separate term identity.

`பெயரே` is rejected as a predicative/emphatic surface based on the grammatical base `பெயர்`. This decision does not reject the base term itself.

### Mixed-use grammatical forms remain context-bounded

`அல்` and `அற்று` are accepted because Nannūl explicitly lists them in grammatical ending/சாரியை inventories, while other occurrences retain ordinary negative/privative meanings. Technical and non-technical contexts are stored separately in the ledger.

## Whole review-ledger state

After Batch 004:

- candidate surface forms: **455**;
- reviewed: **87**;
- accepted: **67**;
- rejected: **20**;
- needs-context: **0**;
- unreviewed: **368**;
- layer status: **review-in-progress**.

Review coverage by batch:

- Batch 001: 20 decisions — 19 accepted / 1 rejected;
- Batch 002: 17 decisions — 14 accepted / 3 rejected;
- Batch 003: 25 decisions — 18 accepted / 7 rejected;
- Batch 004: 25 decisions — 16 accepted / 9 rejected.

The terminology review layer is **not complete**.

## Decision storage

Human decisions are stored only in:

`data/grammatical-terminology-review.json`

Batch-004 human-readable decision summary:

`reviews/terminology/batch-004-decisions.md`

Generated candidate-discovery artifacts remain mechanically generated and are not hand-edited with decisions.

## Validation

Validator:

`scripts/validate_terminology_review.py`

Workflow:

`.github/workflows/validate-terminology-review.yml`

Validation output:

`data/grammatical-terminology-review-validation.json`

Validation status: **PASS**.

Verified checks include:

- candidate discovery validation remains PASS;
- candidate count remains 455;
- decision candidate IDs remain unique;
- all evidence IDs resolve to canonical non-gap records;
- technical/non-technical evidence subsets are valid and non-overlapping;
- accepted/rejected decision requirements are satisfied;
- ledger counts reconcile exactly;
- Batch 001 remains exactly 20 decisions;
- Batch 002 remains exactly 17 decisions;
- Batch 003 remains exactly 25 decisions;
- Batch 004 is exactly 25 decisions.

Validation failures: **none**.

Current validated review-ledger SHA-256:

`b8088d9681f304245c19f09843fa111d20c441f492b6ca2c444bbd6846030c48`

Current Batch-004 decision-summary SHA-256:

`793ee980782dcfa16f6f2ce6b91720fbd0e7a1796664cb1ad79a405f376e3da6`

## Source/canonical separation

This batch does not:

- modify canonical Tamil;
- reconstruct source gaps 73 or 176;
- normalize spelling or punctuation;
- merge exact surface forms;
- alter source variants;
- import external grammatical evidence;
- infer termhood from frequency alone.

## Result

**PASS — Phase 2 Batch 004 is complete and audited: 25 frequency-only candidates reviewed, 16 accepted, 9 rejected, 0 needs-context. The review ledger now contains 87 explicit decisions, with 368 candidates remaining unreviewed.**

## Next activity

Continue Phase 2 with **Batch 005**, taking the next roughly 25 highest-priority unreviewed frequency-only candidates and preserving the same context-sampling, exact-form restraint, mixed-use handling, separate human ledger, and post-review validation boundaries.
