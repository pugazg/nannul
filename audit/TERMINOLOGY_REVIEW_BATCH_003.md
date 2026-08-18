# Grammatical-Terminology Contextual Review — Batch 003 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 003** for Nannūl.

Batch ID:

`NANNUL-TERM-REVIEW-003`

Selection policy:

- the **25 highest-priority unreviewed candidates with no exact source-heading-token evidence**;
- all 37 heading-supported candidates had already been reviewed in Batches 001–002;
- mechanical frequency/structural breadth determined review order only and was never treated as semantic confidence;
- decisions use internal canonical Nannūl contexts only under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No Tolkāppiyam, commentary, dictionary, later grammar, or modern scholarship evidence was used for these first-pass decisions.

## Evidence tooling

Batch-003 evidence generator:

- `scripts/generate_terminology_review_batch_003.py`;
- `.github/workflows/generate-terminology-review-batch-003.yml`.

Generated evidence:

- `reviews/terminology/batch-003-contexts.json`;
- `reviews/terminology/batch-003-contexts.md`;
- `reviews/terminology/batch-003-candidate-01.md` through `batch-003-candidate-25.md`.

For each candidate the packet records:

1. all exact occurrence record IDs/numbers;
2. every structural unit in which the form occurs;
3. all occurrence records when the form is modest-frequency;
4. otherwise a deterministic broad sample spanning first/last occurrence, each structural unit, evenly distributed records, and any source-variant-linked occurrences;
5. exact canonical text and source-variant references for every selected review context.

No source-heading evidence is present for any Batch-003 candidate.

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

Batch 003 decisions:

- reviewed: **25**;
- accepted: **18**;
- rejected: **7**;
- needs-context: **0**.

### Accepted exact forms

- `ஐ` — `phonology-letter-class`;
- `முதல்` — `meta-grammar`;
- `ஈர்` — `morphology`;
- `என` — `particle`;
- `என்` — `morphology`;
- `ஈறு` — `morphology`;
- `ஆம்` — `morphology`;
- `ஈற்று` — `morphology`;
- `இடை` — `other-grammar`;
- `பொருள்` — `semantics`;
- `என்று` — `particle`;
- `ஒற்று` — `phonology-letter-class`;
- `ஆ` — `phonology-letter-class`;
- `ன` — `phonology-letter-class`;
- `ள` — `phonology-letter-class`;
- `உயிர்மெய்` — `phonology-letter-class`;
- `ஆய்தம்` — `phonology-letter-class`;
- `இ` — `phonology-letter-class`.

### Rejected exact forms

- `ஆகும்`;
- `இரு`;
- `என்ப`;
- `இயல்பும்`;
- `ஆறு`;
- `இயல்பே`;
- `ஒன்று`.

## Frequency-only review findings

Batch 003 establishes several important editorial patterns for the remaining candidate pool.

### High frequency is not termhood

`ஆகும்` is the highest-frequency candidate in this batch, with 73 exact occurrences, but the reviewed sample shows it functioning as ordinary copular/resultative rule-statement syntax. It is therefore rejected.

Similarly:

- `என்ப` is reportative/definitional prose rather than a technical term;
- `இரு`, `ஆறு`, and `ஒன்று` are primarily numeral or ordinary lexical forms inside grammatical enumerations.

This validates the separation between mechanical review priority and semantic decision.

### A frequency-only form can still be an internally explicit grammatical form

The absence of source-heading evidence does not prevent acceptance when Nannūl itself gives direct grammatical evidence in body text.

Examples:

- `ஈர்` is both the numeral two and an explicitly listed verbal ending/viguti;
- `என்` is explicitly listed among verbal endings despite other possessive/quotative uses;
- `ஆம்` occurs as a verbal ending and also in an இடையியல் asai-word inventory;
- `என` and `என்று` function as grammatical particles;
- `ஐ` is both a Tamil vowel/letter and the accusative/case-marker form.

These are accepted with context-bounded evidence rather than a claim that every occurrence has the same technical sense.

### Exact-form restraint for compositional inflections

`இயல்பும்` and `இயல்பே` are rejected as independent exact-form terminology entries.

The decision does **not** reject the possibility that the base form `இயல்பு` is technical. Instead:

- `இயல்பும்` is analyzed as `இயல்பு` plus additive/conjunctive `உம்`;
- `இயல்பே` is a predicative/emphatic surface based on `இயல்பு`.

The base candidate remains eligible for its own later contextual review. This avoids proliferating term identities merely because a technical base appears with ordinary inflectional/clitic material.

### Mixed grammatical senses remain explicit

Several accepted forms are technically useful in more than one grammatical domain:

- `ஐ` — vowel/letter plus case-marker use;
- `ஆம்` — verbal-ending and particle/asai-word use alongside ordinary copular uses;
- `இடை` — positional/medial metalanguage and shorthand for the இடைச்சொல் class;
- `ஆ` and `இ` — letter/vowel uses plus additional grammatical form uses.

The review ledger records technical/non-technical contexts and notes rather than collapsing these into one universal meaning.

## Whole review-ledger state

After Batch 003:

- candidate surface forms: **455**;
- reviewed: **62**;
- accepted: **51**;
- rejected: **11**;
- needs-context: **0**;
- unreviewed: **393**;
- layer status: **review-in-progress**.

The terminology review layer is **not complete**.

Review coverage by batch:

- Batch 001: 20 decisions — 19 accepted / 1 rejected;
- Batch 002: 17 decisions — 14 accepted / 3 rejected;
- Batch 003: 25 decisions — 18 accepted / 7 rejected.

## Decision storage

Human decisions are stored only in:

`data/grammatical-terminology-review.json`

Batch-003 human-readable decision summary:

`reviews/terminology/batch-003-decisions.md`

The generated candidate-discovery artifacts remain mechanically generated and are not hand-edited with decisions.

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
- Batch 003 is exactly 25 decisions.

Validation failures: **none**.

Current validated review-ledger SHA-256:

`f5cd2034a9ce085a1311be0ba856e1954080439c20ec9b9472e313419f04f01e`

Current Batch-003 decision-summary SHA-256:

`c059af7db437b685e3bd4aba145840d16e252a764d2686a8e22cb9bc42e15dbd`

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

**PASS — Phase 2 Batch 003 is complete and audited: 25 frequency-only candidates reviewed, 18 accepted, 7 rejected, 0 needs-context. The review ledger now contains 62 explicit decisions, with 393 candidates remaining unreviewed.**

## Next activity

Continue Phase 2 with **Batch 004**, taking the next roughly 25 highest-priority unreviewed frequency-only candidates. Preserve the same representative-context sampling, mixed-use handling, exact-form restraint, separate human ledger, and post-review validation boundaries.
