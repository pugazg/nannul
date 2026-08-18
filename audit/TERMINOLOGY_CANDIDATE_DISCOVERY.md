# Grammatical-Terminology Candidate Discovery Audit

## Scope

This audit covers **Phase 1: mechanical candidate discovery** for a future reviewed Nannūl grammatical-terminology layer.

Candidate discovery is not term classification.

## Inputs

The generator consumes only already validated repository layers:

- `data/nurpa.json` — 460 canonical numbered records;
- `data/token-occurrences.ndjson` — 5,431 exact token occurrences;
- `data/source-heading-index.json` — 65 source-supported heading occurrences plus the explicit unheaded span;
- `data/frequency-profiles-validation.json` — required upstream `PASS` gate.

No canonical Tamil file is modified.

## Generator and workflow

- generator: `scripts/generate_terminology_candidates.py`
- workflow: `.github/workflows/generate-terminology-candidates.yml`

Generated outputs:

- `data/grammatical-terminology-candidates.json`
- `data/grammatical-terminology-candidates.ndjson`
- `indexes/grammatical-terminology-review-queue.md`
- `data/grammatical-terminology-candidates-validation.json`

Schema:

- `data/grammatical-terminology-candidates.schema.json`

## Discovery rule

An exact surface form becomes a candidate when either:

1. its exact canonical token occurrence count is **3 or more**; or
2. it exactly matches a non-whitespace token in a source-supported heading.

The rule deliberately does not perform:

- Unicode normalization;
- punctuation stripping;
- spelling normalization;
- stemming or lemmatization;
- sandhi splitting;
- semantic grouping;
- synonym merging;
- grammatical interpretation.

The resulting pool is intentionally broad and is expected to contain false positives.

## Result

Validated Phase-1 counts:

- canonical records: **460**;
- exact token occurrences: **5,431**;
- all unique exact surface forms: **2,837**;
- discovered candidate surface forms: **455**;
- candidates meeting frequency >=3: **443**;
- candidates with exact source-heading-token evidence: **37**;
- reviewed candidates: **0**;
- accepted terms: **0**;
- rejected candidates: **0**.

The frequency and heading sets overlap, so their counts are not additive.

## Review-priority ranking

Every candidate receives a mechanical review-priority score based on:

- exact source-heading-token evidence;
- exact occurrence frequency;
- structural-unit breadth;
- major-section breadth.

The score is **not** a probability, confidence score, or grammatical-term decision.

The ranking correctly surfaces many plausible high-value review targets, while also retaining ordinary/connective/high-frequency forms that may later be rejected. This broadness is intentional because Phase 1 optimizes recall and provenance, not semantic precision.

## Stable candidate identity correction

The first generated queue used rank-derived candidate IDs. During audit review this was rejected because candidate identity would have changed if future evidence changed the rank.

The generator was corrected before Phase-1 closeout.

Final candidate IDs are:

`nannul-term-candidate-<16 hex>`

where the suffix is the first 16 hexadecimal characters of SHA-256 over the **exact UTF-8 surface form**.

Consequences:

- candidate identity is stable across rank/frequency changes;
- review rank remains independently recalculable;
- differently spelled or punctuated exact forms remain independently addressable;
- validation checks both ID uniqueness and exact-surface/hash correspondence.

This correction changed derived candidate identifiers only. Canonical Tamil and exact token occurrences were untouched.

## Validation

`data/grammatical-terminology-candidates-validation.json` reports **PASS**.

Checks include:

- upstream frequency validation is PASS;
- 460 canonical records remain present;
- source gaps 73 and 176 remain absent;
- exactly 5,431 token occurrences are linked back to canonical record IDs and character offsets;
- candidate forms are unique;
- candidate IDs are unique;
- every candidate ID matches the exact-surface SHA-256 policy;
- the candidate set exactly matches the documented discovery rule;
- every candidate is `unreviewed`;
- no candidate has an automatic term decision;
- no candidate has an automatic term category;
- evidence occurrence counts reconcile;
- review ranks are contiguous.

## Output fingerprints

Final generated SHA-256 fingerprints:

- `data/grammatical-terminology-candidates.json` — `bd98b575cb3e4816f8409bcdd9bc493747625fdd87520dd9d1a8c76737337e18`
- `data/grammatical-terminology-candidates.ndjson` — `bdd9cb80ad278dad286210713d613a8a838ff6750788733489ebd3835dc2a67f`
- `indexes/grammatical-terminology-review-queue.md` — `a5192f4f631fdb5033d73f802fe44ccd36c3832aade2228b0339a2d62ef27b29`

## Review separation

Generated candidate files are read-only derived artifacts. Human review decisions must not be written into them because regeneration would overwrite those edits.

The review protocol is documented at:

`docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`

A separate decision ledger is initialized at:

`data/grammatical-terminology-review.json`

with schema:

`data/grammatical-terminology-review.schema.json`

Current ledger state:

- candidates: **455**;
- reviewed: **0**;
- accepted: **0**;
- rejected: **0**;
- needs-context: **0**;
- unreviewed: **455**.

Allowed future decisions are `accepted`, `rejected`, and `needs-context`, each requiring explicit contextual review and rationale under the review guidelines.

## Layer separation

This activity does not:

- change canonical Tamil;
- reconstruct 73 or 176;
- normalize lexical surfaces;
- alter source variants;
- claim that frequency means technicality;
- automatically classify a grammatical category;
- use Tolkāppiyam/commentary evidence to alter Nannūl source data.

## Raw-source preservation dependency

The exact-byte current Project Madurai raw-HTML preservation gate remains independently open and unchanged.

## Result

**PASS — Phase-1 grammatical-terminology candidate discovery is complete, reproducible, stable-ID-addressable, evidence-backed, and explicitly unreviewed across 455 exact surface forms.**

## Suitable next activity

Begin **Phase 2 human/contextual review** in a small ranked batch, preferably the highest-priority heading-supported candidates first. Review decisions must be written only to the separate review ledger and accompanied by stable நூற்பா evidence and rationale.
