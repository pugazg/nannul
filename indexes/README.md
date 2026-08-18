# Indexes

Human-facing navigational and derived indexes for Nannūl belong here.

## Current indexes

### `nurpa-number-index.md`

Stable range/navigation index for the numbered source, including `nannul-%04d`, canonical file paths, and reserved source-gap positions `nannul-0073` and `nannul-0176`.

Machine-readable resolver: `data/nurpa-index.json`.

### `source-heading-index.md`

Human-facing exact source-heading index.

Validated state:

- **65** actual non-empty source-heading occurrences;
- **65** distinct exact heading strings;
- one explicit unheaded span, நூற்பாக்கள் **56–57**.

Machine-readable form: `data/source-heading-index.json`.

### `frequency-profiles.md`

Human-facing exact-surface frequency profile.

Validated whole-work totals:

- **460** canonical numbered records;
- **5,431** exact token occurrences;
- **2,837** unique exact surface forms;
- **2,037** hapax forms.

Machine-readable data: `data/frequency-profiles.json` and `data/frequency-tables.json`.

Audit: `audit/FREQUENCY_PROFILES.md`.

### `grammatical-terminology-review-queue.md`

Human-facing **Phase-1 discovery queue**.

Discovery state:

- exact-surface candidates: **455**;
- frequency-selected: **443**;
- source-heading-supported: **37**.

The queue remains mechanically generated and intentionally does not display human decisions as if they were discovery output. Candidate IDs remain stable SHA-256-derived exact-surface identifiers.

Machine-readable discovery data: `data/grammatical-terminology-candidates.json`.

Audit: `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`.

## Human terminology review surfaces

Human decisions are stored in:

- `data/grammatical-terminology-review.json`.

Current Phase-2 status after **Batches 001–002**:

- reviewed: **37**;
- accepted: **33**;
- rejected: **4**;
- needs-context: **0**;
- unreviewed: **418**.

Batch summaries:

- `reviews/terminology/batch-001-decisions.md`;
- `reviews/terminology/batch-002-decisions.md`.

Context evidence:

- Batch 001: `reviews/terminology/batch-001-contexts.*` and 20 per-candidate files;
- Batch 002: `reviews/terminology/batch-002-contexts.*` and 17 per-candidate files.

Review validation:

- `data/grammatical-terminology-review-validation.json` — **PASS**.

Audits:

- `audit/TERMINOLOGY_REVIEW_BATCH_001.md`;
- `audit/TERMINOLOGY_REVIEW_BATCH_002.md`.

### Heading-supported review tier

All **37 candidates carrying exact source-heading-token evidence have now been explicitly reviewed** across Batches 001 and 002.

The next review tier starts with the highest-priority **frequency-only** candidates.

A consolidated reviewed grammatical-term index should be generated only after a larger reviewed sample makes it useful; it must derive from the explicit review ledger, never from frequency/discovery rank alone.

## Index policy

Indexes are derived from verified canonical text and structure and never rewrite canonical Tamil.

Mechanical frequency/profile data and candidate-discovery ranking must remain distinguishable from analytical classification. Human terminology decisions remain provenance-backed and context-bounded, especially for mixed-use forms.

Future human-facing indexes may include:

- consolidated reviewed grammatical-term index;
- example-word index;
- referenced-author/work index;
- cross-reference index to Tolkāppiyam and other Tamil grammar works.
