# Raw Source Preservation Attempt — 2026-08-18

## Scope

- Work: **நன்னூல்**
- Controlling digital source: Project Madurai `pmuni0147`
- URL: `https://www.projectmadurai.org/pm_etexts/utf8/pmuni0147.html`
- Objective: preserve the current HTML HTTP response body byte-for-byte with SHA-256 provenance.

## Source verification

The current Project Madurai page was reachable through web retrieval on 2026-08-18 and was verified to present:

- `நன்னூல்` / பவணந்தி முனிவர்;
- Project Madurai preparation/provenance header;
- redistribution statement requiring the header page to remain intact;
- the expected work structure through சொல்லதிகாரம்;
- terminal marker `நன்னூல் முற்றிற்று`.

This web verification is sufficient to confirm the declared source remains live, but parsed/rendered web retrieval is **not** treated as a byte-for-byte archival copy.

## Exact-byte retrieval attempts

### Local/container retrieval

Direct byte download from the execution environment failed because outbound DNS/network resolution was unavailable. No local raw file was obtained and no checksum was computed.

### Repository-side GitHub Actions retrieval

A reproducible workflow was added:

`.github/workflows/vendor-project-madurai-source.yml`

It is designed to:

1. fetch the declared Project Madurai URL with `curl --fail --location`;
2. preserve the raw response body under `sources/project-madurai/pmuni0147/raw/pmuni0147.html`;
3. capture HTTP headers;
4. verify title and terminal marker;
5. compute SHA-256 and byte count;
6. write `RETRIEVAL.yml`;
7. commit the archival outputs to `main` if the bytes differ.

The workflow was committed and a second workflow-file push was made to trigger its `push` event.

## Verification result

Expected output checked on GitHub `main`:

`sources/project-madurai/pmuni0147/raw/RETRIEVAL.yml`

Result at the time of this audit: **not present**.

The connected GitHub capability available for this work does not expose workflow dispatch. The local environment also does not provide the `gh` CLI. Therefore the workflow could not be explicitly dispatched from this execution context.

## Archival decision

**RAW SOURCE PRESERVATION IS NOT YET COMPLETE.**

The repository deliberately does **not**:

- reconstruct HTML from parsed web text;
- copy the older Project Madurai GitHub mirror into the controlling raw-source path;
- invent a SHA-256 value or byte count;
- mark `full_current_html_vendored` as true.

This prevents a provenance error in which a derived representation is mislabelled as the controlling HTTP response bytes.

## Durable infrastructure added

- `.github/workflows/vendor-project-madurai-source.yml`
- `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`
- raw-source preservation block in `sources/project-madurai/pmuni0147/SOURCE_MANIFEST.yml`

## Current status

- canonical Tamil ingestion: **COMPLETE**;
- canonical completion audits: **COMPLETE**;
- raw-source preservation protocol: **COMPLETE**;
- reproducible retrieval workflow: **INSTALLED**;
- raw current HTML snapshot: **NOT YET MATERIALIZED / NOT VERIFIED**;
- SHA-256 provenance for raw current HTML: **NOT YET AVAILABLE**.

Completion must follow the gate defined in `sources/project-madurai/pmuni0147/RAW_SOURCE_PRESERVATION.md`.
