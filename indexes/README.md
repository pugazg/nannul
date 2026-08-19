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

Current Phase-2 status after **Batches 001–008**:

- reviewed: **187**;
- accepted: **116**;
- rejected: **71**;
- needs-context: **0**;
- unreviewed: **268**.

Batch decision summaries and context packets exist for Batches 001–008 under `reviews/terminology/`.

Review validation: `data/grammatical-terminology-review-validation.json` — **PASS**.

Audits exist at `audit/TERMINOLOGY_REVIEW_BATCH_001.md` through `audit/TERMINOLOGY_REVIEW_BATCH_008.md`.

### Review-tier status

All **37 source-heading-supported candidates** were reviewed across Batches 001–002. Batches 003–008 continue the frequency-only tier while preserving the rule that frequency is review priority, not termhood.

Batch 008 accepted `அது`, `இயல்பு`, `பால்`, `குணம்`, `கு`, `உம்`, `ஐம்பால்`, `எதிர்மறை`, `பொது`, `பன்மை`, `அல்வழி`, and `அயல்`. It rejected 13 emphatic, inflected, numeral/quantifier, anaphoric, and verbal rule-language exact surfaces.

The review also now demonstrates a stable base/surface policy: an inflected surface can be rejected without prejudging its base, and a later base review may accept the underlying grammatical term when canonical contexts establish independent technical identity.

A consolidated reviewed grammatical-term index should be generated only after a larger reviewed sample makes it useful; it must derive from the explicit review ledger, never directly from mechanical rank.

## Index policy

Indexes derive from verified canonical text and structure and never rewrite canonical Tamil. Mechanical frequency/discovery data and human analytical decisions remain distinguishable, with context-bounded treatment for mixed-use forms.
