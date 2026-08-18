# எழுத்ததிகாரம் Completion Audit — 56–257

## Scope

This audit closes the first அதிகாரம்-level canonical ingestion milestone for **நன்னூல்**:

- அதிகாரம்: **2. எழுத்ததிகாரம்**
- Nominal source range: **56–257**
- Controlling witness: current Project Madurai Unicode webpage `pmuni0147`

## Completed இயல்கள்

1. `2.1 எழுத்து இயல்` — 56–127
2. `2.2 பதவியல்` — 128–150
3. `2.3 உயிரீற்றுப் புணரியல்` — 151–203
4. `2.4 மெய்யீற்றுப் புணரியல்` — 204–239
5. `2.5 உருபு புணரியல்` — 240–257

Each இயல் has a dedicated canonical file and batch audit.

## Batch audits

- `CANONICAL_INGEST_056_127.md`
- `CANONICAL_INGEST_128_150.md`
- `CANONICAL_INGEST_151_203.md`
- `CANONICAL_INGEST_204_239.md`
- `CANONICAL_INGEST_240_257.md`

## Controlling-source numbering state

The nominal range 56–257 contains two missing displayed numbers in the controlling current webpage:

- **73** — current webpage displays 72 → `பிறப்பு` → 74;
- **176** — current webpage displays 175 → `ஈகார வீற்றுச் சிறப்புவிதி` → 177.

These readings are preserved exactly as source-version states. The corresponding readings in the older Project Madurai GitHub mirror were not imported into the canonical layer.

The historical mirror also contains a numbering anomaly around 240–242. The current controlling webpage displays **240, 241, 242** continuously, and that sequence is the canonical repository sequence.

All three witness issues are documented in `SOURCE_VARIANTS.md` as `PM147-V001`, `PM147-V002`, and `PM147-V003`.

## Canonical count note

The nominal source-number span 56–257 contains 202 possible integer numbers. Because the controlling webpage does not display numbered 73 or 176, the canonical எழுத்ததிகாரம் contains **200 displayed numbered நூற்பாக்கள்** while retaining the nominal structural range **56–257**.

This count describes the controlling witness; it is not an editorial renumbering.

## Source fidelity

Across all five இயல்கள்:

- numbering was not regularized;
- source-supported punctuation and spelling were retained;
- no missing source number was silently reconstructed;
- no historical-witness text was inserted into the controlling-source canonical layer;
- commentary, translation, and interpretation remain separate.

## Boundary verification

- எழுத்ததிகாரம் begins at நூற்பா **56**.
- Final நூற்பா is **257**.
- The current Project Madurai webpage then begins **3. சொல்லதிகாரம்**, with `3.1 பெயரியல்` at நூற்பா **258**.

## Result

**PASS — எழுத்ததிகாரம் 56–257 is canonicalized and batch-audited in full against the current controlling Project Madurai webpage.**

Next canonical milestone: **சொல்லதிகாரம் 258–462**, beginning with `3.1 பெயரியல் 258–319`.
