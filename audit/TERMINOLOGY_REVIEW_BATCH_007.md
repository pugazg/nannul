# Grammatical-Terminology Contextual Review — Batch 007 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 007** for Nannūl.

Batch ID: `NANNUL-TERM-REVIEW-007`

Selection policy:

- next **25 highest-priority unreviewed frequency-only candidates** after Batches 001–006;
- no exact source-heading-token evidence in the selected tier;
- frequency/structural breadth determined review order only;
- decisions used internal canonical Nannūl contexts under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No external Tolkāppiyam, commentary, dictionary, later-grammar, or modern-scholarship evidence was used.

## Evidence tooling

- `scripts/generate_terminology_review_batch_007.py`
- `.github/workflows/generate-terminology-review-batch-007.yml`
- `reviews/terminology/batch-007-contexts.json`
- `reviews/terminology/batch-007-contexts.md`
- `reviews/terminology/batch-007-candidate-01.md` through `batch-007-candidate-25.md`

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

- reviewed: **25**
- accepted: **7**
- rejected: **18**
- needs-context: **0**

### Accepted exact forms

- `ட` — `phonology-letter-class`
- `இசை` — `other-grammar`, context-bounded
- `தம்` — `morphology`, context-bounded
- `அன்` — `morphology`
- `ஊர்` — `morphology`, context-bounded
- `தொழில்` — `semantics`
- `எழுவாய்` — `syntax`

### Rejected exact forms

- `ஏழ்`
- `ஒழி`
- `இரண்டும்`
- `ஐந்து`
- `ஆறும்`
- `நெறியே`
- `தாம்`
- `இயலும்`
- `இல`
- `மூன்றும்`
- `உள`
- `பல`
- `ஒன்றன்`
- `உருபும்`
- `புலவர்`
- `இன்றி`
- `ஆகா`
- `வழியே`

## Review findings

### Frequency-only review is becoming more selective

Batch 007 has the lowest acceptance count so far: **7/25**. This is not a change in policy. As review rank descends, the queue increasingly contains numerals, pronouns, discourse language, inflected surfaces, and example forms that are frequent in grammatical prose without being grammatical terms themselves.

### Numeral surfaces remain non-terminological

`ஏழ்`, `ஐந்து`, `ஆறும்`, `இரண்டும்`, and `மூன்றும்` are ordinary numeral/counting surfaces. Their occurrence inside grammatical inventories does not create term identity.

### Exact-form restraint continues

- `உருபும்` is rejected as the additive surface of accepted base `உருபு`;
- `வழியே` is a predicative/emphatic relational surface, consistent with earlier rejection of `வழி`;
- `நெறியே` is a predicative/emphatic surface meaning 'is the rule/method', not an independent term;
- `இயலும்`, `இன்றி`, and `ஆகா` are verbal/compositional rule language;
- `ஒன்றன்` is a genitive numeral surface.

### Example words remain separate from terminology

`தாம்`, `உள`, `பல`, and `புலவர்` are lexical/pronominal/person-denoting material. Nannūl may classify or manipulate such words, but that does not make the exact word itself the name of the grammatical category.

### Grammatical form identities remain valid when explicitly enumerated

`அன்`, `தம்`, and `ஊர்` are accepted where Nannūl explicitly treats the exact forms as விகுதி/சாரியை/finite-verb material. For `தம்` and `ஊர்`, ordinary lexical uses are stored separately from technical-use contexts.

### Core syntax and semantic metalanguage remains recoverable without headings

`எழுவாய்` is a strong internally attested syntactic term across case, construction, agreement, and பொருள்கோள் contexts.

`தொழில்` is accepted as action/function semantic metalanguage across tense, அல்வழி, word-formation, nominal, and உரிச்சொல் classifications.

`இசை` is accepted only context-bounded: Nannūl uses it in phonological/prosodic, tense/semantic-indication, semantic-concordance, and particle-function contexts, while ordinary lexical/speech-label uses remain non-term evidence.

## Whole review-ledger state

After Batch 007:

- candidate surface forms: **455**
- reviewed: **162**
- accepted: **104**
- rejected: **58**
- needs-context: **0**
- unreviewed: **293**
- layer status: **review-in-progress**

Review coverage:

- Batch 001: 20 — 19 accepted / 1 rejected
- Batch 002: 17 — 14 accepted / 3 rejected
- Batch 003: 25 — 18 accepted / 7 rejected
- Batch 004: 25 — 16 accepted / 9 rejected
- Batch 005: 25 — 18 accepted / 7 rejected
- Batch 006: 25 — 12 accepted / 13 rejected
- Batch 007: 25 — 7 accepted / 18 rejected

The terminology review layer is **not complete**.

## Validation

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Validation output: `data/grammatical-terminology-review-validation.json`

Status: **PASS**

Verified constraints include stable candidate identity, canonical non-gap evidence, technical/non-technical evidence subset rules, decision requirements, ledger reconciliation, and exact batch counts **20 + 17 + 25 + 25 + 25 + 25 + 25**.

Validation failures: **none**.

Validated review-ledger SHA-256:

`6533411e9fea2ed8945342270aa617055effdd04654969f176a9af6f2e539112`

Batch-007 decision-summary SHA-256:

`1cda2eedf9f0698b5012fcdff295fc454d80e4336df43f050078199f6a6ec574`

## Source/canonical separation

This batch does not modify canonical Tamil, reconstruct gaps 73/176, normalize spelling or punctuation, merge exact surface forms, alter source variants, import external grammatical evidence, or infer termhood from frequency alone.

## Result

**PASS — Phase 2 Batch 007 is complete and audited: 25 frequency-only candidates reviewed, 7 accepted, 18 rejected, 0 needs-context. The ledger now contains 162 explicit decisions, with 293 candidates remaining unreviewed.**

## Next activity

Continue Phase 2 with **Batch 008**, taking the next 25 highest-priority unreviewed frequency-only candidates under the same deterministic context-sampling, exact-form restraint, mixed-use handling, separate-ledger, and post-review validation rules.
