# Raw Source Preservation — Project Madurai `pmuni0147`

## Purpose

This document governs preservation of the **raw current HTML response body** for the declared controlling source:

`https://www.projectmadurai.org/pm_etexts/utf8/pmuni0147.html`

The canonical Tamil transcription is already complete and audited. Raw-source preservation is a separate archival layer and must not modify the canonical text.

## Preservation rule

A file may be labelled as the raw controlling source only when it is obtained directly from the declared Project Madurai URL as HTTP response bytes.

The following are **not acceptable substitutes** for the raw file:

- parsed or rendered browser text;
- search-engine extracts;
- reconstructed HTML;
- the older Project Madurai GitHub mirror;
- normalized or reformatted copies;
- the repository canonical transcription.

## Target archival files

The reproducible vendoring workflow writes to:

```text
sources/project-madurai/pmuni0147/raw/
├── pmuni0147.html
├── pmuni0147.html.sha256
├── RETRIEVAL.yml
└── HTTP_HEADERS.txt
```

### `pmuni0147.html`

The unchanged HTTP response body returned by the controlling source URL.

### `pmuni0147.html.sha256`

SHA-256 checksum generated from the archived HTML bytes.

### `RETRIEVAL.yml`

Records:

- source URL;
- UTC retrieval timestamp;
- retrieval method;
- byte count;
- SHA-256 digest;
- validation checks;
- archival role.

### `HTTP_HEADERS.txt`

HTTP response headers captured during retrieval. These are provenance metadata and are not part of the literary text.

## Reproducible retrieval workflow

Workflow:

`.github/workflows/vendor-project-madurai-source.yml`

The workflow:

1. downloads the controlling URL with `curl --fail --location`;
2. preserves the returned response body without textual normalization;
3. verifies that the file is non-empty;
4. verifies that it contains `நன்னூல்`;
5. verifies that it contains the terminal marker `நன்னூல் முற்றிற்று`;
6. computes SHA-256 and byte count;
7. captures HTTP headers and UTC retrieval time;
8. commits the archival files to `main` only when the retrieved bytes differ from the repository copy.

## Current status

**Configured, but raw snapshot not yet materialized in the repository.**

As of 2026-08-18, the workflow is installed on `main`, but the expected `raw/` output files have not been verified as present. Therefore:

- `full_current_html_vendored` must remain `false`;
- no checksum may be claimed yet;
- no parsed web representation may be promoted to raw-source status;
- the historical Project Madurai GitHub mirror remains a secondary witness only.

This status is intentionally conservative. Completion requires the four target archival files to exist on `main` and the SHA-256 in `RETRIEVAL.yml` to match `pmuni0147.html.sha256` and the archived HTML bytes.

## Completion gate

Raw-source preservation may be marked **COMPLETE** only after all of the following are verified from GitHub `main`:

- `raw/pmuni0147.html` exists and is non-empty;
- `raw/pmuni0147.html.sha256` exists;
- `raw/RETRIEVAL.yml` exists;
- `raw/HTTP_HEADERS.txt` exists;
- recorded SHA-256 matches the archived file;
- recorded byte count matches the archived file;
- archived file contains the work title/header material;
- archived file contains `நன்னூல் முற்றிற்று`;
- Project Madurai header is retained intact within the archived HTML;
- `SOURCE_MANIFEST.yml` is then updated from `full_current_html_vendored: false` to `true` with the verified hash and byte count.

Until that gate passes, canonical completion and raw-source preservation remain distinct statuses.
