# Structure

This folder records the hierarchy and stable addressing model of the Nannūl edition independently of the Tamil text files.

## Current structural files

- `sections.yml` — source-supported section, subsection, அதிகாரம், and இயல் boundaries from Project Madurai `pmuni0147`.
- `identifiers.yml` — stable identifier scheme for numbered நூற்பாக்கள் and the unnumbered சிறப்புப்பாயிரம்.

## Stable identifiers

Numbered positions use zero-padded identifiers:

- `nannul-0001`
- `nannul-0056`
- `nannul-0258`
- `nannul-0462`

The unnumbered opening uses:

`nannul-sirappu-payiram`

The nominal positions `nannul-0073` and `nannul-0176` are reserved as `source-gap` identifiers because the controlling current webpage does not display numbered 73 or 176. They must not be treated as canonical-text records.

## Related indexes/data

- `data/nurpa-index.json` — machine-readable segment resolver and deterministic ID expansion rule.
- `indexes/nurpa-number-index.md` — human-facing range/index documentation.
- `audit/STABLE_IDENTIFIER_INDEX.md` — integrity audit for the identifier/index layer.

Future structural files may include topic headings appearing inside இயல்கள், cross-references between நூற்பாக்கள், and comparison mappings to Tolkāppiyam and later Tamil grammatical works.

Structural metadata is derived data and must not be confused with the source transcription itself. Stable IDs should be used by commentary, translation, APIs, and comparison layers as external references rather than inserted into canonical Tamil lines.
