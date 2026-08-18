# Source Variant Audit

This file records differences between source witnesses. No witness may silently overwrite the controlling source.

## Witnesses

### A — controlling source
- Project Madurai current Unicode webpage
- `https://www.projectmadurai.org/pm_etexts/utf8/pmuni0147.html`
- displayed last revision: 31 August 2021

### B — historical secondary witness
- Project Madurai official GitHub mirror
- repository: `project-madurai/pm-repo-html`
- path: `html/pmuni0147.html`
- branch: `master`
- blob SHA: `1ebf6e496a39520391830733f9c25de173b1f5b6`

The historical mirror is not textually identical to the current webpage. It frequently separates morphological components that are joined in the current webpage and contains older formatting/numbering states.

## Variant PM147-V001 — நூற்பா 73

**Location:** எழுத்ததிகாரம் → எழுத்து இயல், between நூற்பா 72 and 74.

**Controlling current webpage (A):**
- displays நூற்பா 72;
- then the heading `பிறப்பு`;
- then நூற்பா 74;
- no numbered 73 is displayed in the rendered text.

**Historical Project Madurai mirror (B):**
- includes a subsection `2.1.3. முறை`;
- includes a numbered நூற்பா 73 before `2.1.4. பிறப்பு` / நூற்பா 74.

**Repository treatment:**
- do not silently insert historical-witness 73 into the canonical text derived from A;
- canonical range 56–127 now preserves the sequence 72 → `பிறப்பு` → 74;
- retain B's reading only in a variant/secondary-witness layer unless a later editorial decision changes the controlling-source policy;
- canonical ingest record: `audit/CANONICAL_INGEST_056_127.md`.

**Status:** OPEN AS SOURCE-VERSION DISCREPANCY — canonical handling applied; no repository transcription error remains.

## Variant PM147-V002 — numbering around உருபு புணரியல்

**Location:** எழுத்ததிகாரம் → உருபு புணரியல், நூற்பா 240–242.

**Controlling current webpage (A):** numbers the sequence 240, 241, 242.

**Historical Project Madurai mirror (B):** the older HTML currently shows 240 followed by 242 and another 242, indicating an older numbering/markup anomaly.

**Repository treatment:** current webpage A controls canonical numbering; preserve the historical anomaly only as witness evidence.

**Status:** RESOLVED FOR CANONICAL NUMBERING — use A.
