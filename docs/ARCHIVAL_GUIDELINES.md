# Nannūl Archival Guidelines

## 1. Source authority

For the current ingestion phase, the controlling digital source is Project Madurai eText `pmuni0147`:

https://www.projectmadurai.org/pm_etexts/utf8/pmuni0147.html

The source header, acknowledgements, provenance, and redistribution notice must be retained with any archived copy derived from that eText.

## 2. Source fidelity

Do not silently:

- modernize Tamil spelling;
- normalize punctuation;
- rewrite sandhi or word spacing;
- regularize numbering;
- repair apparent typographical errors;
- replace historical grammatical terminology;
- merge or split நூற்பா text without recording the editorial operation.

If a suspected source problem is found, preserve the source reading and record the issue under `audit/`.

## 3. Layer separation

The repository must maintain distinct layers:

- `sources/` — untouched or source-faithful captured source material and provenance;
- `text/tamil/` — canonical repository transcription/segmentation derived from a declared source;
- `structure/` — hierarchy, identifiers, ranges, and relationships;
- `indexes/` — human-facing navigational indexes;
- `data/` — machine-readable derived datasets;
- `commentaries/` — historical or modern commentary, each with separate provenance;
- `translations/` — translations derived from the verified Tamil layer;
- `audit/` — verification reports, discrepancies, and source checks.

No commentary or inferred interpretation belongs inside source transcription files.

## 4. Stable identifiers

Numbered நூற்பாக்கள் should receive stable identifiers using zero-padded numbers, for example:

- `nannul-0001`
- `nannul-0056`
- `nannul-0258`
- `nannul-0462`

The unnumbered சிறப்புப்பாயிரம் must be represented separately rather than forcing it into the numbered sequence.

## 5. Structural hierarchy

Use the hierarchy explicitly supported by the controlling source. For `pmuni0147`, preserve its section and இயல் boundaries and record the corresponding நூற்பா ranges in `structure/sections.yml`.

## 6. Derived data

Machine-readable datasets may include tokens, terms, cross-references, grammatical categories, examples, and links to Tolkāppiyam or other works. Every derived claim must be distinguishable from source text and should identify its derivation method or reviewer where appropriate.

## 7. Commentary and comparison

Future comparison with Tolkāppiyam, Sangam literature, Nannūl commentaries, or later grammar works should be stored as references or analytical layers. Such material must never be inserted into the canonical source text as if it were part of Pavaṇanti's text.

## 8. Translation

Translation begins only from a verified Tamil unit. Preserve grammatical terminology where a forced English equivalent would erase a Tamil category; use glosses and notes instead of silently flattening distinctions.

## 9. Audit trail

Every substantial ingestion or editorial phase should leave a concise audit record containing:

- source used;
- range processed;
- verification method;
- unresolved uncertainties;
- any deviations from the source representation.
