# Data

Machine-readable derived datasets for Nannūl belong here.

## Current datasets

### `nurpa-index.json`

A machine-readable resolver for the stable Nannūl numbered namespace.

It records:

- identifier pattern `nannul-%04d`;
- nominal numbered range 1–462;
- canonical displayed unit count 460;
- reserved source-gap positions 73 and 176;
- section / subsection / இயல் segment boundaries;
- canonical file path for each segment;
- deterministic expansion rule for resolving a number to its stable ID and canonical location.

The two source-gap positions do not point to canonical Tamil text.

## Derivation policy

Datasets in this folder are derived from the verified canonical Tamil and `structure/` metadata. Derived or inferred fields must never be represented as if they were part of the source text.

Potential next artifacts include:

- a one-record-per-canonical-unit `nurpa.json` / `nurpa.csv` dataset;
- structural hierarchy exports;
- grammatical terminology datasets;
- token and word-form indexes;
- relationship data connecting Nannūl rules with Tolkāppiyam or other grammar works.

All future records should use stable IDs from `structure/identifiers.yml` and link back to the canonical source layer without modifying it.
