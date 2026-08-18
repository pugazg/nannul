# Indexes

Human-facing navigational indexes for Nannūl belong here.

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

## Index policy

Indexes are derived from verified canonical text and structure. They use stable நூற்பா IDs wherever individual units are addressed and never rewrite canonical Tamil.

Future human-facing indexes may include:

- grammatical-term index;
- example-word index;
- referenced-author/work index;
- cross-reference index to Tolkāppiyam and other Tamil grammar works;
- frequency/profile summaries by அதிகாரம், இயல், and source heading.

Analytical classifications must remain distinguishable from mechanical/source-supported indexes.
