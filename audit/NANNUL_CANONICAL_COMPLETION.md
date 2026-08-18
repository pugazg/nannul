# Nannūl Canonical Completion Audit

## Scope

This audit closes the source-derived canonical Tamil ingestion of **பவணந்தி முனிவர் அருளிய நன்னூல்** against the declared controlling digital witness:

- Project Madurai eText: `pmuni0147`
- controlling witness: current Tamil Unicode webpage
- source edition lineage stated by Project Madurai: edition edited by Mani Thirunavukkarasu Mudaliar, Vavilla Ramasamy Sastrulu & Sons, Madras, 1926

This completion status applies to the repository's **canonical Tamil transcription layer**. It is not a claim of manuscript collation, critical-edition establishment, or complete byte-for-byte preservation of the Project Madurai webpage HTML.

## Canonical components completed

### Unnumbered opening

- `0. சிறப்புப்பாயிரம்` — canonicalized from the controlling source.

### Numbered source

- `1. பொதுப்பாயிரம்` — 1–55 — canonicalized.
- `2. எழுத்ததிகாரம்` — nominal 56–257 — canonicalized and fully audited.
- `3. சொல்லதிகாரம்` — 258–462 — canonicalized and fully audited.

The controlling webpage then displays the terminal marker:

`நன்னூல் முற்றிற்று`

This marker is retained at the end of the final canonical உரியியல் file.

## அதிகாரம் completion records

- `EZHUTHTHATHIKARAM_COMPLETION.md` — எழுத்ததிகாரம் 56–257.
- `SOLLATHIKARAM_COMPLETION.md` — சொல்லதிகாரம் 258–462.

## Numbering state of the controlling witness

The nominal numbered span is **1–462**.

The current Project Madurai webpage does not display two numbered units:

- **73** — current source displays 72 → `பிறப்பு` → 74;
- **176** — current source displays 175 → `ஈகார வீற்றுச் சிறப்புவிதி` → 177.

Therefore:

- nominal numbered positions: **462**;
- displayed numbered நூற்பாக்கள் in the controlling witness: **460**;
- repository canonical numbered units: **460**;
- editorial reconstruction of missing numbers: **none**.

The historical Project Madurai GitHub mirror contains readings for 73 and 176, but those readings remain secondary-witness evidence and were not inserted into the controlling-source canonical layer.

## Other documented source-version findings

`SOURCE_VARIANTS.md` records all source-version discrepancies encountered during ingestion:

- `PM147-V001` — missing displayed 73 in the current webpage;
- `PM147-V002` — historical-mirror numbering anomaly around 240–242; current 240, 241, 242 sequence controls canonically;
- `PM147-V003` — missing displayed 176 in the current webpage;
- `PM147-V004` — நூற்பா 343 current `செய்தனெ` vs historical `செய்தென`;
- `PM147-V005` — நூற்பா 344 current trailing quotation mark after `பிற` vs none in the historical mirror.

No secondary-witness reading was silently imported into canonical text.

## End-to-end boundary verification

Verified canonical progression:

1. unnumbered `சிறப்புப்பாயிரம்`;
2. numbered பொதுப்பாயிரம் 1–55;
3. எழுத்ததிகாரம் nominal 56–257, preserving current-source gaps at 73 and 176;
4. சொல்லதிகாரம் 258–462 continuously;
5. terminal source marker `நன்னூல் முற்றிற்று`;
6. Project Madurai webpage footer/revision material excluded from the literary canonical layer.

## Fidelity policy applied throughout

The canonical layer preserves source-supported:

- wording;
- numbering;
- spelling;
- punctuation;
- repetitions;
- unusual grammatical or typographical forms;
- source headings and structural boundaries.

The canonical layer does not silently:

- modernize Tamil;
- normalize punctuation or spacing;
- repair source numbering;
- reconstruct missing text;
- substitute historical-witness readings;
- mix commentary, translation, interpretation, or normalized computational data into source transcription.

## Remaining archival/source work outside canonical completion

The **full current raw Project Madurai HTML has not yet been vendored byte-for-byte**. Provenance/header material is preserved under `sources/project-madurai/pmuni0147/`, and the complete source-derived canonical Tamil layer is now present in `text/tamil/`.

Future work may include raw-source preservation, stable unit IDs/indexes, structured data, commentary layers, comparative grammar work, translations, or critical/source comparison. None of those should alter the completed canonical layer without an explicit audited editorial decision.

## Result

**PASS — the source-derived canonical Tamil ingestion of Nannūl is complete end-to-end against the current Project Madurai `pmuni0147` webpage, from சிறப்புப்பாயிரம் through நூற்பா 462 and `நன்னூல் முற்றிற்று`.**
