# Grammatical-Terminology Contextual Review — Batch 006 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 006** for Nannūl.

Batch ID: `NANNUL-TERM-REVIEW-006`

Selection policy:

- next **25 highest-priority unreviewed frequency-only candidates** after Batches 001–005;
- no exact source-heading-token evidence in the selected tier;
- frequency and structural breadth determine review order only;
- decisions use internal canonical Nannūl contexts only under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No external Tolkāppiyam, commentary, dictionary, later-grammar, or modern-scholarship evidence was used.

## Evidence tooling

- `scripts/generate_terminology_review_batch_006.py`
- `.github/workflows/generate-terminology-review-batch-006.yml`
- `reviews/terminology/batch-006-contexts.json`
- `reviews/terminology/batch-006-contexts.md`
- `reviews/terminology/batch-006-candidate-01.md` through `batch-006-candidate-25.md`

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

- reviewed: **25**
- accepted: **12**
- rejected: **13**
- needs-context: **0**

### Accepted exact forms

- `தன்மை` — `other-grammar`
- `எழுத்து` — `orthography`
- `து` — `morphology`
- `ஆன்` — `morphology`
- `இறு` — `morphology`
- `அம்` — `morphology`
- `இல்` — `case`
- `ஏற்புழி` — `meta-grammar`
- `ஐயம்` — `semantics`
- `வன்மை` — `phonology-letter-class`
- `காரணம்` — `semantics`
- `முறை` — `meta-grammar`

### Rejected exact forms

- `மூன்று`
- `வேறு`
- `இயல்`
- `தான்`
- `உளவே`
- `இடத்து`
- `இடத்தும்`
- `ஆகலும்`
- `நான்கு`
- `ஆதல்`
- `ஆகி`
- `உயிரும்`
- `எட்டு`

## Review findings

### Person/deixis tier gains its third core term

`தன்மை` is accepted from explicit internal evidence alongside previously accepted `முன்னிலை` and `படர்க்கை`. Nannūl directly treats the three as grammatical person/deictic positions and assigns pronouns and finite verb forms to them. The ordinary sense 'nature/quality' in the prefatory passage is stored separately.

### Foundational metalinguistic terms are now explicit

`எழுத்து` is accepted as the grammatical/orthographic unit itself. `முறை` is accepted as grammatical ordering/method metalanguage, and `ஏற்புழி` as recurrent rule-application/context metalanguage: Nannūl repeatedly conditions operations on where they appropriately apply.

### Exact-form restraint remains strict

`இயல்` is rejected at the exact-surface level because the reviewed passages use it compositionally for nature/function/convention rather than clearly establishing an independent term identity. This does not affect compound source labels containing `இயல்`.

Likewise:

- `இடத்து` and `இடத்தும்` are inflected surfaces of already accepted `இடம்`;
- `ஆகலும்`, `ஆதல்`, and `ஆகி` are compositional verbal rule-language;
- `உயிரும்` is the additive surface of the already accepted base `உயிர்`.

None is promoted merely because its base or surrounding phrase is technical.

### Grammatical-form exact surfaces remain valid when Nannūl enumerates them

`து`, `ஆன்`, `இறு`, `அம்`, and `இல்` are accepted because Nannūl explicitly uses them in inflectional, case, சாரியை, ending, or positional grammatical systems. Mixed ordinary/example uses are separated where present.

### Semantic/phonological terms remain context-bounded

- `ஐயம்` is accepted for grammatical uncertainty/doubt functions while ordinary pedagogical doubt remains non-term use;
- `வன்மை` is accepted for strong/hard consonantal behavior while the teacher-description sense 'strength/command' is non-term;
- `காரணம்` is accepted as a grammatical/semantic causal relation;
- `இல்` is accepted for locative/case and explicitly discussed absence-word uses, while ordinary negative constructions remain separate.

### Numerals remain non-terminological

`மூன்று`, `நான்கு`, and `எட்டு` are rejected as ordinary numerals used in counts and enumerations. This continues the treatment established for `ஒன்று`, `இரண்டு`, `ஆறு`, `மூ`, and `நான்கும்` in earlier batches.

## Whole review-ledger state

After Batch 006:

- candidate surface forms: **455**
- reviewed: **137**
- accepted: **97**
- rejected: **40**
- needs-context: **0**
- unreviewed: **318**
- layer status: **review-in-progress**

Review coverage:

- Batch 001: 20 — 19 accepted / 1 rejected
- Batch 002: 17 — 14 accepted / 3 rejected
- Batch 003: 25 — 18 accepted / 7 rejected
- Batch 004: 25 — 16 accepted / 9 rejected
- Batch 005: 25 — 18 accepted / 7 rejected
- Batch 006: 25 — 12 accepted / 13 rejected

The terminology review layer is **not complete**.

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
- batch counts are exactly **20 + 17 + 25 + 25 + 25 + 25**.

Validation failures: **none**.

Validated review-ledger SHA-256:

`c74aeb4499997bee191547156295d5a5208c004f63a5ff9c22ae6ac2db3b5979`

Batch-006 decision-summary SHA-256:

`8e40f179189f9c47d17efe38b624c8dd211e8bef1ee88c6b5a8660bae7c72847`

## Source/canonical separation

This batch does not modify canonical Tamil, reconstruct gaps 73/176, normalize spelling or punctuation, merge exact surface forms, alter source variants, import external grammatical evidence, or infer termhood from frequency alone.

## Result

**PASS — Phase 2 Batch 006 is complete and audited: 25 frequency-only candidates reviewed, 12 accepted, 13 rejected, 0 needs-context. The ledger now contains 137 explicit decisions, with 318 candidates remaining unreviewed.**

## Next activity

Continue Phase 2 with **Batch 007**, taking the next 25 highest-priority unreviewed frequency-only candidates under the same deterministic context-sampling, exact-form restraint, mixed-use handling, separate-ledger, and post-review validation rules.
