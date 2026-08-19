# Indexes

Human-facing navigational and derived indexes for Nannūl belong here.

## Current indexes

### `nurpa-number-index.md`

Stable range/navigation index for the numbered source, including `nannul-%04d`, canonical file paths, and reserved source-gap positions `nannul-0073` and `nannul-0176`.

Machine-readable resolver: `data/nurpa-index.json`.

### `source-heading-index.md`

Validated exact source-heading index:

- **65** actual non-empty source-heading occurrences;
- **65** distinct exact heading strings;
- one explicit unheaded span, நூற்பாக்கள் **56–57**.

### `frequency-profiles.md`

Validated whole-work totals:

- **460** canonical numbered records;
- **5,431** exact token occurrences;
- **2,837** unique exact surface forms;
- **2,037** hapax forms.

### `grammatical-terminology-review-queue.md`

Human-facing Phase-1 mechanical discovery queue:

- exact-surface candidates: **455**;
- frequency-selected: **443**;
- source-heading-supported: **37**.

Candidate IDs remain stable SHA-256-derived exact-surface identifiers. The queue does not encode human decisions.

## Human terminology review surfaces

Human decisions: `data/grammatical-terminology-review.json`.

Current Phase-2 status after **Batches 001–005**:

- reviewed: **112**;
- accepted: **85**;
- rejected: **27**;
- needs-context: **0**;
- unreviewed: **343**.

Batch decision summaries:

- `reviews/terminology/batch-001-decisions.md`
- `reviews/terminology/batch-002-decisions.md`
- `reviews/terminology/batch-003-decisions.md`
- `reviews/terminology/batch-004-decisions.md`
- `reviews/terminology/batch-005-decisions.md`

Context evidence exists for all five batches under `reviews/terminology/`.

Review validation: `data/grammatical-terminology-review-validation.json` — **PASS**.

Audits:

- `audit/TERMINOLOGY_REVIEW_BATCH_001.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_002.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_003.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_004.md`
- `audit/TERMINOLOGY_REVIEW_BATCH_005.md`

### Review-tier status

All **37 source-heading-supported candidates** were reviewed across Batches 001–002. Batches 003–005 continue the frequency-only tier while preserving the rule that frequency is review priority, not termhood.

A consolidated reviewed grammatical-term index should be generated only after a larger reviewed sample makes it useful; it must derive from the explicit review ledger, never directly from mechanical rank.

## Index policy

Indexes derive from verified canonical text and structure and never rewrite canonical Tamil. Mechanical frequency/discovery data and human analytical decisions remain distinguishable, with context-bounded treatment for mixed-use forms.
