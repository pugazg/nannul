# Grammatical-Terminology Contextual Review — Batch 008 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 008** for Nannūl.

Batch ID: `NANNUL-TERM-REVIEW-008`

Selection policy:

- next **25 highest-priority unreviewed frequency-only candidates** after Batches 001–007;
- no exact source-heading-token evidence in the selected tier;
- frequency/structural breadth determined review order only;
- decisions used internal canonical Nannūl contexts under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

The selected ranks were 156–178 and 186–187; ranks 179–185 were already resolved earlier through the heading-supported tier and therefore were not re-reviewed.

No external Tolkāppiyam, commentary, dictionary, later-grammar, or modern-scholarship evidence was used.

## Evidence tooling

- `scripts/generate_terminology_review_batch_008.py`
- `.github/workflows/generate-terminology-review-batch-008.yml`
- `reviews/terminology/batch-008-contexts.json`
- `reviews/terminology/batch-008-contexts.md`
- `reviews/terminology/batch-008-candidate-01.md` through `batch-008-candidate-25.md`

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

- reviewed: **25**
- accepted: **12**
- rejected: **13**
- needs-context: **0**

### Accepted exact forms

- `அது` — `case`, context-bounded to explicit case-marker use
- `இயல்பு` — `meta-grammar`, context-bounded
- `பால்` — `noun`, context-bounded to grammatical gender/class use
- `குணம்` — `semantics`
- `கு` — `morphology`
- `உம்` — `particle`
- `ஐம்பால்` — `noun`
- `எதிர்மறை` — `semantics`
- `பொது` — `meta-grammar`
- `பன்மை` — `noun`
- `அல்வழி` — `other-grammar`
- `அயல்` — `morphology`

### Rejected exact forms

- `பொருளே`
- `நின்ற`
- `உயர்`
- `ஒன்றே`
- `உற`
- `வருமே`
- `அவற்று`
- `வவ்வும்`
- `ஒன்பதும்`
- `சில`
- `அனைத்தும்`
- `இருமையும்`
- `உருபின்`

## Review findings

### Previously deferred base forms can now be resolved cleanly

Earlier batches rejected exact inflected/compositional surfaces `இயல்பும்` and `இயல்பே` without prejudging their base. Batch 008 now accepts `இயல்பு` itself because Nannūl repeatedly uses it as rule metalanguage for the natural/default/unmodified outcome contrasted with விகாரம், மிகுதல், and திரிபு.

The same exact-form logic is preserved in the opposite direction:

- `பொருளே` remains rejected while the base `பொருள்` is already accepted;
- `உருபின்` remains rejected while `உருபு` is already accepted;
- `வவ்வும்` remains rejected while the exact letter/form `வ` is already accepted;
- `உயர்` is not promoted separately from the explicit accepted category `உயர்திணை`.

### Grammatical gender/number terminology is explicit

`பால்`, `ஐம்பால்`, and `பன்மை` are accepted from direct internal grammatical evidence.

- `பால்` has explicit gender/class use in பெயரியல் and concord/deviation classification;
- `ஐம்பால்` names the five gender/person-number classes across tense, word meaning, and finite-verbal distribution;
- `பன்மை` is explicitly contrasted with ஒருமை and governs nominal and verbal agreement/distribution.

Broader non-gender senses of `பால்` are stored separately.

### Exact grammatical forms continue to be retained

`அது`, `கு`, and `உம்` are accepted where Nannūl itself enumerates or manipulates those exact surfaces as grammatical forms.

- `அது` is accepted only for its explicit place in the eight-case inventory; demonstrative/anaphoric uses remain non-term contexts;
- `கு` participates across case, விகுதி, சாரியை, and finite-verb morphology;
- `உம்` is directly used as grammatical suffix/particle material in multiple systems.

### Core semantic/classificatory metalanguage remains recoverable

`குணம்`, `எதிர்மறை`, and `பொது` are accepted from repeated grammatical classificatory use.

- `குணம்` functions as quality/property metalanguage and is directly paired with பண்பு;
- `எதிர்மறை` is an explicit negative/oppositional grammatical meaning/function;
- `பொது` carries a stable common/general classificatory role across letters, words, and grammatical categories rather than merely serving as incidental prose.

### புணர்ச்சி terminology gains `அல்வழி`

`அல்வழி` is accepted as a stable technical category repeatedly contrasted with `வேற்றுமை` in புணர்ச்சி. It conditions phonological alternations throughout உயிரீற்றுப் புணரியல் and மெய்யீற்றுப் புணரியல் and is not ordinary relational language in these contexts.

`அயல்` is also accepted as technical positional metalanguage for the adjacent/neighboring segment in vocative and related transformation rules.

### Numeral, quantifier, pronoun, and rule-language surfaces remain restrained

The following are rejected despite grammatical surroundings:

- numeral/emphatic surfaces: `ஒன்றே`, `ஒன்பதும்`, `இருமையும்`;
- quantifier/example forms: `சில`, `அனைத்தும்`;
- anaphoric surface: `அவற்று`;
- rule-language verbal forms: `நின்ற`, `உற`, `வருமே`.

Frequency remains a review-order signal only.

## Whole review-ledger state

After Batch 008:

- candidate surface forms: **455**
- reviewed: **187**
- accepted: **116**
- rejected: **71**
- needs-context: **0**
- unreviewed: **268**
- layer status: **review-in-progress**

Review coverage:

- Batch 001: 20 — 19 accepted / 1 rejected
- Batch 002: 17 — 14 accepted / 3 rejected
- Batch 003: 25 — 18 accepted / 7 rejected
- Batch 004: 25 — 16 accepted / 9 rejected
- Batch 005: 25 — 18 accepted / 7 rejected
- Batch 006: 25 — 12 accepted / 13 rejected
- Batch 007: 25 — 7 accepted / 18 rejected
- Batch 008: 25 — 12 accepted / 13 rejected

The terminology review layer is **not complete**.

## Validation

Validator: `scripts/validate_terminology_review.py`

Workflow: `.github/workflows/validate-terminology-review.yml`

Validation output: `data/grammatical-terminology-review-validation.json`

Status: **PASS**

Verified constraints include stable candidate identity, canonical non-gap evidence, technical/non-technical evidence subset rules, decision requirements, ledger reconciliation, and exact batch counts **20 + 17 + 25 + 25 + 25 + 25 + 25 + 25**.

Validation failures: **none**.

Validated review-ledger SHA-256:

`66f4f44fa5eb862379524a719a6fa1f8ee7a0f58a7bc899863bd69d562eba3ed`

Batch-008 decision-summary SHA-256:

`e4da47483b92771abfca9d450bf2c4448f1994d9c5925bf49febbe985d7d1cc3`

## Source/canonical separation

This batch does not modify canonical Tamil, reconstruct gaps 73/176, normalize spelling or punctuation, merge exact surface forms, alter source variants, import external grammatical evidence, or infer termhood from frequency alone.

## Result

**PASS — Phase 2 Batch 008 is complete and audited: 25 frequency-only candidates reviewed, 12 accepted, 13 rejected, 0 needs-context. The ledger now contains 187 explicit decisions, with 268 candidates remaining unreviewed.**

## Next activity

Continue Phase 2 with **Batch 009**, taking the next 25 highest-priority unreviewed frequency-only candidates under the same deterministic context-sampling, exact-form restraint, mixed-use handling, separate-ledger, and post-review validation rules.
