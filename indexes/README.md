# Indexes

Human-facing navigational and derived indexes for Nannūl belong here.

## Current indexes

### `nurpa-number-index.md`

Stable range/navigation index for the numbered Nannūl source.

It documents:

- `nannul-%04d` as the numbered stable-ID scheme;
- all source-supported section / subsection / இயல் ranges;
- canonical file paths;
- reserved source-gap positions `nannul-0073` and `nannul-0176`;
- `nannul-sirappu-payiram` for the unnumbered சிறப்புப்பாயிரம்.

Machine-readable resolver: `data/nurpa-index.json`.

### `source-heading-index.md`

Human-facing index of the exact source-supported heading occurrences carried by the canonical unit dataset.

Validated state:

- **65** actual non-empty source-heading occurrences;
- **65** distinct exact heading strings;
- one explicitly represented unheaded span, நூற்பாக்கள் **56–57**, before `எண்` begins at 58.

No empty/fabricated heading is assigned to the unheaded span.

Machine-readable form: `data/source-heading-index.json`.

### `frequency-profiles.md`

Human-facing exact-surface frequency profile generated from the validated occurrence layer.

It provides:

- whole-work exact-surface frequency leaders;
- **3** source-section / அதிகார-level profiles;
- **17** இயல் / structural-unit profiles;
- **65** actual source-heading profiles;
- **1** explicit unheaded-span profile;
- record, token, unique-form, and hapax counts;
- leading exact surface forms for each group.

Validated whole-work totals are **460 canonical numbered records**, **5,431 exact token occurrences**, **2,837 unique exact surface forms**, and **2,037 hapax surface forms**.

Machine-readable summaries: `data/frequency-profiles.json`.

Complete exact-surface group tables: `data/frequency-tables.json`.

Validation: `data/frequency-profiles-validation.json`.

Audit: `audit/FREQUENCY_PROFILES.md`.

### `grammatical-terminology-review-queue.md`

Human-facing **Phase-1 candidate discovery queue** for grammatical-terminology review.

Discovery state:

- discovered exact-surface candidates: **455**;
- candidates meeting frequency >=3: **443**;
- candidates with exact source-heading-token evidence: **37**.

Candidate IDs are stable SHA-256-derived identifiers tied to the exact surface form; review rank is separately recalculable.

The queue is intentionally broad. Its score ranks review priority only and does not assert technical-term status. Because it is a regenerated discovery artifact, its candidate rows remain `unreviewed`; human decisions are maintained separately rather than written into this file.

Machine-readable discovery data: `data/grammatical-terminology-candidates.json`.

Discovery validation: `data/grammatical-terminology-candidates-validation.json`.

Audit: `audit/TERMINOLOGY_CANDIDATE_DISCOVERY.md`.

## Human terminology review surfaces

Human decisions are stored in:

- `data/grammatical-terminology-review.json`.

Current Phase-2 status after **Batch 001**:

- reviewed: **20**;
- accepted: **19**;
- rejected: **1**;
- needs-context: **0**;
- unreviewed: **435**.

Human-readable Batch-001 decisions:

- `reviews/terminology/batch-001-decisions.md`.

Context packets used for review:

- `reviews/terminology/batch-001-contexts.md`;
- `reviews/terminology/batch-001-candidate-01.md` through `batch-001-candidate-20.md`.

Review validation:

- `data/grammatical-terminology-review-validation.json` — **PASS**.

Audit:

- `audit/TERMINOLOGY_REVIEW_BATCH_001.md`.

A consolidated **reviewed grammatical-term index** should be generated only after enough explicit review-ledger decisions exist to justify a separate stable human-facing index; it must derive from the review ledger, never from frequency/discovery rank alone.

## Index policy

Indexes are derived from verified canonical text and structure. They use stable நூற்பா IDs wherever individual units are addressed and never rewrite canonical Tamil.

Mechanical frequency/profile data and candidate-discovery ranking must remain distinguishable from analytical classification. Frequent or heading-linked surface forms are not automatically grammatical terms.

Human terminology decisions must remain provenance-backed and context-bounded, particularly for mixed-use forms whose exact surface may be technical in one நூற்பா and ordinary in another.

Future human-facing indexes may include:

- consolidated reviewed grammatical-term index derived only from explicit review-ledger decisions;
- example-word index;
- referenced-author/work index;
- cross-reference index to Tolkāppiyam and other Tamil grammar works.
