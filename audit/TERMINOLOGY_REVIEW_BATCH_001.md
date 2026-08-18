# Grammatical-Terminology Contextual Review — Batch 001 Audit

## Scope

This audit closes **Phase 2 contextual terminology review — Batch 001** for Nannūl.

Batch ID:

`NANNUL-TERM-REVIEW-001`

Selection policy:

- first **20** candidates in mechanical review-rank order that carry exact source-heading-token evidence;
- candidate discovery rank was used only to choose review order, never as semantic confidence;
- decisions were made from internal Nannūl canonical evidence under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.

No external Tolkāppiyam, commentary, dictionary, later grammar, or modern scholarship evidence was used to make this first-pass batch decision.

## Evidence preparation

Review packet tooling:

- `scripts/generate_terminology_review_packet.py`;
- `.github/workflows/generate-terminology-review-packet.yml`;
- `scripts/split_terminology_review_packet.py`.

Generated review evidence is under:

`reviews/terminology/`

including:

- `batch-001-contexts.json`;
- `batch-001-contexts.md`;
- four convenience part files;
- twenty one-candidate context files.

The final context-packet policy includes:

1. first exact body occurrence;
2. at least one exact body occurrence from each structural unit in which the candidate occurs;
3. one governed canonical context for every matching source heading;
4. every candidate body-occurrence record linked to a documented source variant.

### Heading-only evidence correction

During packet review, an important modeling distinction was identified: an exact candidate may occur in a **source heading** without being repeated verbatim in the governed நூற்பா body.

The packet generator was corrected so it does not fabricate or require a body occurrence in such cases. It records the governed canonical context as `heading-context-only` while preserving heading evidence separately.

This is relevant, for example, to source-heading evidence such as:

- `முற்று வினை`;
- `வினைச் சொல்`;
- `உயிரீற்று முன் வல்லினம்`;
- `வருமொழித் தகர நகரத் திரிபு`.

This correction affected derived review tooling only. Canonical Tamil, heading text, and candidate-discovery data were not altered.

## Decision result

The separate human review ledger is:

`data/grammatical-terminology-review.json`

Batch 001 result:

- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**.

Whole review-ledger state after this batch:

- candidate surface forms: **455**;
- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**;
- unreviewed: **435**;
- layer status: **review-in-progress**.

The terminology layer is therefore **not complete**.

## Accepted exact forms

The 19 accepted exact forms are:

- `உயிர்` — `phonology-letter-class`;
- `எண்` — `meta-grammar`;
- `ய` — `phonology-letter-class`;
- `வேற்றுமை` — `case`;
- `ர` — `phonology-letter-class`;
- `உருபு` — `morphology`;
- `ழ` — `phonology-letter-class`;
- `மெய்` — `phonology-letter-class`;
- `வினை` — `verb`;
- `பெயர்` — `noun`;
- `முற்று` — `verb`;
- `சொல்` — `meta-grammar`;
- `இடைநிலை` — `morphology`;
- `சாரியை` — `morphology`;
- `பாயிரம்` — `textual-pedagogy`;
- `பகுதி` — `morphology`;
- `மாத்திரை` — `prosodic-measure`;
- `வல்லினம்` — `phonology-letter-class`;
- `திரிபு` — `phonology-sound-process`.

Categories are analytical metadata only and do not alter source text.

## Rejected exact form

### `முன்`

Decision: **rejected**.

Across reviewed body contexts and source headings, `முன்` functions compositionally as the ordinary relational expression “before/in front of” inside otherwise technical grammatical descriptions. The fact that it appears inside technical headings does not make the exact surface form itself a standalone grammatical technical term.

This rejection demonstrates the reason candidate discovery and human review are separate layers.

## Mixed and polysemous use

Acceptance never means that every occurrence of an exact form is technical.

Batch 001 explicitly records mixed-use evidence where supported internally. Examples include:

- `உயிர்` — vowel-class uses versus living-being/life uses;
- `எண்` — grammatical/numeral-class metalanguage versus ordinary enumeration/counting;
- `வேற்றுமை` — grammatical case versus ordinary difference/distinction;
- `மெய்` — consonantal metalanguage versus bodily/sensory use;
- `சொல்` — grammatical word/expression versus ordinary imperative “say”;
- `மாத்திரை` — measured sound-duration unit versus restrictive “merely/only”;
- `திரிபு` — grammatical/sound-change use alongside a broader variation sense;
- `பெயர்`, `முற்று`, and `இடைநிலை` — accepted with multiple grammatical senses rather than forced into one uniform semantic definition.

The ledger uses `term_use_record_ids`, `non_term_use_record_ids`, `technical_scope`, and notes to keep these distinctions explicit.

## Decision storage boundary

Human judgments are stored only in:

`data/grammatical-terminology-review.json`

They are **not** written into regenerated discovery artifacts:

- `data/grammatical-terminology-candidates.json`;
- `data/grammatical-terminology-candidates.ndjson`;
- `indexes/grammatical-terminology-review-queue.md`.

Those discovery artifacts continue to describe candidates as mechanically discovered/unreviewed because they are not the editorial decision layer.

Human-readable Batch-001 decisions are generated at:

`reviews/terminology/batch-001-decisions.md`

## Review validation

Validator:

`scripts/validate_terminology_review.py`

Workflow:

`.github/workflows/validate-terminology-review.yml`

Validation output:

`data/grammatical-terminology-review-validation.json`

Validation status: **PASS**.

Verified checks include:

- upstream candidate-discovery validation is PASS;
- candidate count remains 455;
- decision candidate IDs are unique;
- every decision maps to an existing stable candidate and exact surface form;
- every reviewed நூற்பா ID exists in the canonical dataset and is not source gap 73 or 176;
- technical/non-technical evidence lists are valid subsets of reviewed evidence and do not overlap;
- accepted decisions carry a category and at least one positive technical-use record;
- rejected decisions carry no term category or technical-use record and do carry non-term evidence;
- ledger counts reconcile exactly;
- layer status matches review coverage;
- Batch 001 contains exactly 20 decisions.

Validation failures: **none**.

Current review-ledger SHA-256 recorded by validation:

`c28e87bfbcd8e05dffdb76ca598aff39ff196c7134d727ce2a61a02489d98a7f`

Batch decision summary SHA-256:

`2b5b7322bfd063bd341e2a12f484bd58b30725ab9b3c7f552bad683be50344fd`

The validator checks structural and provenance integrity; it does not replace contextual human interpretation.

## Source/canonical separation

This batch does not:

- modify canonical Tamil;
- reconstruct missing source positions 73 or 176;
- normalize spelling or punctuation;
- merge distinct exact surface forms;
- change documented source variants;
- alter stable candidate identities;
- treat frequency as termhood;
- import external grammatical traditions into Nannūl source evidence.

## Result

**PASS — Phase 2 contextual review Batch 001 is complete and audited: 20 candidates reviewed, 19 accepted, 1 rejected, 0 needs-context, with 435 candidates remaining unreviewed.**

## Next review activity

Continue Phase 2 with the remaining source-heading-supported candidates before moving into candidates supported only by frequency. The next batch should preserve the same evidence-packet, mixed-use, decision-ledger, and validation boundaries.
