# Grammatical-Terminology Contextual Review — Batch 005 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 005** for Nannūl.

Batch ID: `NANNUL-TERM-REVIEW-005`

Selection policy:

- next **25 highest-priority unreviewed frequency-only candidates** after Batches 001–004;
- no exact source-heading-token evidence in the selected tier;
- frequency and structural breadth determine review order only;
- decisions use internal canonical Nannūl contexts only under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No external Tolkāppiyam, commentary, dictionary, later-grammar, or modern-scholarship evidence was used.

## Evidence tooling

- `scripts/generate_terminology_review_batch_005.py`
- `.github/workflows/generate-terminology-review-batch-005.yml`
- `reviews/terminology/batch-005-contexts.json`
- `reviews/terminology/batch-005-contexts.md`
- `reviews/terminology/batch-005-candidate-01.md` through `batch-005-candidate-25.md`

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

- reviewed: **25**
- accepted: **18**
- rejected: **7**
- needs-context: **0**

### Accepted exact forms

- `ஆய்` — `morphology`
- `அ` — `phonology-letter-class`
- `ஈ` — `phonology-letter-class`
- `சுட்டு` — `other-grammar`
- `இனம்` — `other-grammar`
- `பெயர்வினை` — `meta-grammar`
- `ஏவல்` — `verb`
- `எச்சம்` — `syntax`
- `காலம்` — `verb`
- `அளவு` — `prosodic-measure`
- `உ` — `phonology-letter-class`
- `ற` — `phonology-letter-class`
- `இடம்` — `other-grammar`
- `மொழி` — `meta-grammar`
- `அகரம்` — `phonology-letter-class`
- `உம்மை` — `particle`
- `உயர்திணை` — `noun`
- `சிறப்பு` — `semantics`

### Rejected exact forms

- `இரண்டு`
- `உருபே`
- `அவற்றுள்,`
- `தன்`
- `முன்னர்`
- `நான்கும்`
- `ஏற்கும்`

## Review findings

### Internal body text continues to establish strong terminology without heading evidence

Batch 005 supplies direct internal definitions/classifications for several important forms:

- `சுட்டு` — demonstrative/deictic grammar;
- `பெயர்வினை` — collective noun/verb metalanguage;
- `ஏவல்` — imperative verbal function;
- `எச்சம்` — residual/dependent syntactic or grammatical completion;
- `காலம்` — tense/time classification, including இறப்பு / எதிர்வு / நிகழ்வு;
- `உம்மை` — the உம் particle and its constructions/functions;
- `உயர்திணை` — an explicit nominal/semantic class contrasted with அஃறிணை.

These demonstrate again that heading evidence is not required when canonical body text explicitly supports termhood.

### Exact letter-name and letter-symbol treatment remains stable

`அ`, `ஈ`, `உ`, and `ற` are accepted from explicit letter-class evidence. `அகரம்` is independently accepted as letter-name metalanguage used in insertion, deletion, alternation, and ending rules.

### Mixed-use forms are bounded rather than flattened

- `ஆய்` is technical as a verbal/imperative ending but ordinary/compositional elsewhere;
- `ஈ` is a vowel/grammatical form but also occurs lexically as the imperative 'give';
- `காலம்` is a tense category in grammar but can also denote ordinary/contextual time;
- `அளவு` has phonological quantitative use and ordinary extent/limit uses;
- `சிறப்பு` has explicit grammatical particularizing/emphatic uses while also retaining ordinary qualitative meaning.

Technical and non-technical record IDs are stored separately in the review ledger.

### Exact-form restraint continues

`உருபே` is rejected as an independent term identity because it is the predicative/emphatic surface of the already accepted base `உருபு`.

Similarly, `அவற்றுள்,`, `நான்கும்`, and `ஏற்கும்` remain discourse/numeral/verbal rule language rather than terminology.

`தன்` is treated as lexical/pronominal material subjected to grammatical rules rather than the name of a grammatical concept; a later example-word/form index can represent such material without polluting the terminology layer.

### Relational wording remains distinct from technical position labels

`முன்னர்` is rejected as ordinary relational 'before', while the independently reviewed technical forms `முன்னிலை` and `இடம்` remain accepted where Nannūl establishes grammatical positional/person or articulatory senses.

## Whole review-ledger state

After Batch 005:

- candidate surface forms: **455**
- reviewed: **112**
- accepted: **85**
- rejected: **27**
- needs-context: **0**
- unreviewed: **343**
- layer status: **review-in-progress**

Review coverage:

- Batch 001: 20 — 19 accepted / 1 rejected
- Batch 002: 17 — 14 accepted / 3 rejected
- Batch 003: 25 — 18 accepted / 7 rejected
- Batch 004: 25 — 16 accepted / 9 rejected
- Batch 005: 25 — 18 accepted / 7 rejected

The terminology review layer is **not complete**.

## Decision storage

Human decisions remain only in:

`data/grammatical-terminology-review.json`

Batch summary:

`reviews/terminology/batch-005-decisions.md`

Generated discovery artifacts remain read-only mechanical data.

## Validation

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Validation output: `data/grammatical-terminology-review-validation.json`

Status: **PASS**

Verified constraints include:

- candidate discovery remains PASS;
- 455 candidates remain stable;
- decision candidate IDs are unique;
- evidence resolves only to canonical non-gap records;
- technical/non-technical evidence subsets are valid and non-overlapping;
- accepted/rejected decision requirements are satisfied;
- ledger counts/status reconcile;
- batch counts are exactly **20 + 17 + 25 + 25 + 25**.

Validation failures: **none**.

Validated review-ledger SHA-256:

`6f4652e888c850d6aa4168628cdebf7682f8178436ced4179e2441f6ab58d891`

Batch-005 decision-summary SHA-256:

`46b5becb88075d80a96bbf21f8bf86f1a49871bac2d2af8d237688a2de33d222`

## Source/canonical separation

This batch does not modify canonical Tamil, reconstruct gaps 73/176, normalize spelling or punctuation, merge exact surface forms, alter source variants, import external grammatical evidence, or infer termhood from frequency alone.

## Result

**PASS — Phase 2 Batch 005 is complete and audited: 25 frequency-only candidates reviewed, 18 accepted, 7 rejected, 0 needs-context. The ledger now contains 112 explicit decisions, with 343 candidates remaining unreviewed.**

## Next activity

Continue Phase 2 with **Batch 006**, taking the next 25 highest-priority unreviewed frequency-only candidates under the same deterministic context-sampling, exact-form restraint, mixed-use handling, separate-ledger, and post-review validation rules.
