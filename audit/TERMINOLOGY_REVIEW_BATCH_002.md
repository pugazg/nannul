# Grammatical-Terminology Contextual Review — Batch 002 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 002** for Nannūl.

Batch ID:

`NANNUL-TERM-REVIEW-002`

Selection policy:

- all **17 remaining mechanically discovered candidates carrying exact source-heading-token evidence** after excluding the 20 candidates already reviewed in Batch 001;
- mechanical rank determined review order only and was never treated as semantic confidence;
- decisions use internal canonical Nannūl evidence only under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No Tolkāppiyam, commentary, dictionary, later grammar, or modern scholarship evidence was used for these first-pass decisions.

## Evidence tooling

Batch-002 evidence generator:

- `scripts/generate_terminology_review_batch_002.py`;
- `.github/workflows/generate-terminology-review-batch-002.yml`.

Generated evidence:

- `reviews/terminology/batch-002-contexts.json`;
- `reviews/terminology/batch-002-contexts.md`;
- `reviews/terminology/batch-002-candidate-01.md` through `batch-002-candidate-17.md`.

Each candidate packet carries:

1. complete exact-body occurrence numbers;
2. at least one exact-body occurrence from every structural unit in which the form appears;
3. one governed canonical context for every matching source heading, even when the heading token is not repeated verbatim in the body;
4. source-variant-linked body contexts where applicable.

Canonical Tamil and generated candidate-discovery data were not altered.

## Batch result

Batch 002 decisions:

- reviewed: **17**;
- accepted: **14**;
- rejected: **3**;
- needs-context: **0**.

Accepted exact forms:

- `பதம்` — `meta-grammar`;
- `வேற்றுமைப்` — `case`;
- `வினையெச்சம்` — `verb`;
- `விகுதி` — `morphology`;
- `போலி` — `other-grammar`;
- `இலக்கணம்` — `meta-grammar`;
- `உருபுகள்` — `morphology`;
- `பொருள்கோள்` — `syntax`;
- `இகர` — `phonology-letter-class`;
- `பிறப்பு` — `phonology-sound-process`;
- `உருவம்` — `orthography`;
- `அகர` — `phonology-letter-class`;
- `ஒழிபு` — `other-grammar`;
- `பெயரெச்சம்` — `verb`.

Rejected exact forms:

- `பொதுப்`;
- `சொல்லின்`;
- `சிறப்புப்`.

## Rejection rationale pattern

The three rejected forms demonstrate the distinction between **a technical expression** and **independent exact-form termhood**.

### `பொதுப்`

The exact bound modifier means “general/common” inside technical expressions such as `பொதுப் பாயிரம்` and `பொதுப் பெயர்`. The compounds are grammatical/editorial terms; the modifier itself is not independently indexed as a technical term.

### `சொல்லின்`

The exact form is a compositional genitive/oblique form of the already accepted term `சொல்` (“of the word/words”), including in the source heading `சொல்லின் பொதுவிலக்கணம்`. The heading is grammatical, but the inflected relational surface does not require a second independent term identity.

### `சிறப்புப்`

The exact bound modifier means “special/specific” inside technical compounds such as `சிறப்புப் பெயர்வினை` and `சிறப்புப் புணர்ச்சி`. As with `பொதுப்`, compound membership alone is not sufficient for independent termhood.

## Exact-form variants retained deliberately

Batch 002 also demonstrates that an inflected/bound exact surface **can** be accepted when its technical sense is independently useful and consistently supported.

For example:

- `வேற்றுமைப்` is accepted as a technical bound form carrying the grammatical case sense in expressions such as `வேற்றுமைப் பொருள்` and `வேற்றுமைப் புணர்ப்பு`;
- `உருபுகள்` is accepted as the plural exact form of `உருபு` because the plural form itself is a source heading and functions directly in grammatical classification.

These decisions do not merge the forms with their related candidates; exact surfaces remain independently addressable.

## Heading-supported evidence tier complete

Phase-1 discovery found **37 candidates with exact source-heading-token evidence**.

- Batch 001 reviewed the first **20**;
- Batch 002 reviewed the remaining **17**.

Therefore, after this batch:

**all 37 source-heading-supported candidate forms have an explicit human/contextual decision.**

Future batches can move to candidates supported only by corpus frequency/structural breadth without leaving any heading-supported candidate unresolved.

## Whole review-ledger state

After Batch 002:

- candidate surface forms: **455**;
- reviewed: **37**;
- accepted: **33**;
- rejected: **4**;
- needs-context: **0**;
- unreviewed: **418**;
- layer status: **review-in-progress**.

The terminology review layer is **not complete**.

## Decision storage

Human decisions are stored in:

`data/grammatical-terminology-review.json`

Batch-002 human-readable decision summary:

`reviews/terminology/batch-002-decisions.md`

The generated discovery files remain mechanically generated and are not hand-edited with editorial decisions.

## Validation

Validator:

`scripts/validate_terminology_review.py`

Workflow:

`.github/workflows/validate-terminology-review.yml`

Validation output:

`data/grammatical-terminology-review-validation.json`

Validation status: **PASS**.

Checks include:

- candidate discovery validation remains PASS;
- candidate count remains 455;
- decision candidate IDs remain unique;
- all reviewed evidence resolves to canonical non-gap records;
- accepted/rejected evidence structures satisfy ledger rules;
- ledger counts reconcile exactly;
- Batch 001 remains exactly 20 decisions;
- Batch 002 is exactly 17 decisions.

Validation failures: **none**.

Current validated review-ledger SHA-256:

`d8c461349249e9caa5ef0f340bc5433efcb34c2a9cb0ed4dba959198860af8de`

Current Batch-002 decision-summary SHA-256:

`43a42790afae4def88175ac43b4c9c8472984f37f73a6e7fd2cdd2ae31e9bb02`

## Source/canonical separation

This batch does not:

- modify canonical Tamil;
- reconstruct source gaps 73 or 176;
- normalize spelling/punctuation;
- merge exact surface forms;
- alter source variants;
- import external grammatical tradition into source evidence;
- convert frequency or heading presence automatically into termhood.

## Result

**PASS — Phase 2 Batch 002 is complete and audited: 17 candidates reviewed, 14 accepted, 3 rejected, 0 needs-context. The complete 37-candidate source-heading-supported evidence tier has now been reviewed.**

## Next activity

Begin Batch 003 from the **highest-priority unreviewed frequency-only candidates**. Keep the same small-batch contextual review, exact-surface identity, evidence ledger, mixed-use handling, and validation boundaries. A batch of roughly 20–25 candidates is appropriate.