#!/usr/bin/env python3
"""Generate Phase-2 terminology review Batch 002 context packets.

Selection: all remaining candidates with exact source-heading-token evidence after
excluding candidate IDs already present in the human review ledger.

This generator prepares evidence only. It never writes review decisions.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "reviews" / "terminology"

CANDIDATES = DATA / "grammatical-terminology-candidates.json"
REVIEW = DATA / "grammatical-terminology-review.json"
TOKENS = DATA / "token-occurrences.ndjson"
NURPA = DATA / "nurpa.json"
BATCH_ID = "NANNUL-TERM-REVIEW-002"
EXPECTED_COUNT = 17


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_ndjson(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def main() -> None:
    candidates_obj = load_json(CANDIDATES)
    review_obj = load_json(REVIEW)
    nurpa_obj = load_json(NURPA)
    tokens = load_ndjson(TOKENS)

    reviewed_ids = {d["candidate_id"] for d in review_obj["decisions"]}
    selected = [
        c for c in candidates_obj["candidates"]
        if c["evidence"]["source_heading_matches"] and c["candidate_id"] not in reviewed_ids
    ]
    if len(selected) != EXPECTED_COUNT:
        raise SystemExit(f"Expected {EXPECTED_COUNT} remaining heading-supported candidates, found {len(selected)}")

    records = nurpa_obj["records"]
    record_by_id = {r["id"]: r for r in records}
    record_by_number = {r["number"]: r for r in records}
    selected_forms = {c["surface_form_ta"] for c in selected}
    occurrences_by_form: dict[str, list[dict]] = defaultdict(list)
    for row in tokens:
        if row["surface_form"] in selected_forms:
            occurrences_by_form[row["surface_form"]].append(row)

    packet_candidates = []
    for candidate in selected:
        surface = candidate["surface_form_ta"]
        occurrences = occurrences_by_form[surface]
        if len(occurrences) != candidate["evidence"]["occurrence_count"]:
            raise SystemExit(f"Occurrence count mismatch for {surface}")

        occurrence_record_ids = list(dict.fromkeys(o["record_id"] for o in occurrences))
        unit_records: dict[str, list[str]] = defaultdict(list)
        for rid in occurrence_record_ids:
            unit_records[record_by_id[rid]["unit_id"]].append(rid)

        contexts: list[dict] = []
        context_keys: set[tuple[str, str]] = set()

        def add_context(record_id: str, evidence_role: str, heading=None):
            key = (record_id, evidence_role)
            if key in context_keys:
                return
            context_keys.add(key)
            rec = record_by_id[record_id]
            offsets = [
                {"character_start": o["character_start"], "character_end": o["character_end"]}
                for o in occurrences if o["record_id"] == record_id
            ]
            contexts.append({
                "record_id": record_id,
                "number": rec["number"],
                "section_id": rec["section_id"],
                "section_label_ta": rec["section_label_ta"],
                "unit_id": rec["unit_id"],
                "unit_label_ta": rec["unit_label_ta"],
                "topic_heading_ta": rec.get("topic_heading_ta"),
                "canonical_file": rec["canonical_file"],
                "source_variant_refs": rec.get("source_variant_refs", []),
                "text_ta": rec["text_ta"],
                "candidate_offsets": offsets,
                "evidence_role": evidence_role,
                "source_heading_evidence": heading,
            })

        # First exact body occurrence.
        add_context(occurrences[0]["record_id"], "first-body-occurrence")
        # One exact body occurrence from every structural unit.
        for unit_id, rids in unit_records.items():
            add_context(rids[0], "structural-unit-body-occurrence")
        # Governed context for every source-heading match. Heading evidence may be
        # heading-only and therefore need not repeat the exact token in body text.
        for heading in candidate["evidence"]["source_heading_matches"]:
            start = heading["start_number"]
            governed = record_by_number.get(start)
            if governed is None:
                # Source gaps are not expected in heading starts, but fail loudly.
                raise SystemExit(f"No canonical governed record for heading start {start}: {surface}")
            add_context(governed["id"], "source-heading-governed-context", heading)
        # Every exact body occurrence linked to a documented source variant.
        for rid in occurrence_record_ids:
            if record_by_id[rid].get("source_variant_refs"):
                add_context(rid, "source-variant-linked-body-occurrence")

        packet_candidates.append({
            "candidate_id": candidate["candidate_id"],
            "review_rank": candidate["review_rank"],
            "surface_form_ta": surface,
            "review_priority_score": candidate["review_priority_score"],
            "occurrence_count": len(occurrences),
            "record_ids_all": occurrence_record_ids,
            "numbers_all": [record_by_id[rid]["number"] for rid in occurrence_record_ids],
            "structural_units": [
                {
                    "unit_id": uid,
                    "unit_label_ta": record_by_id[rids[0]]["unit_label_ta"],
                    "record_ids": rids,
                }
                for uid, rids in unit_records.items()
            ],
            "source_heading_matches": candidate["evidence"]["source_heading_matches"],
            "source_variant_refs": candidate["evidence"]["source_variant_refs"],
            "contexts": contexts,
        })

    packet = {
        "schema_version": 1,
        "work_id": "nannul",
        "phase": "terminology-contextual-review",
        "batch_id": BATCH_ID,
        "selection_policy": "all remaining source-heading-supported candidates after excluding reviewed candidate IDs",
        "decision_status": "context-packet-only-no-decisions",
        "candidate_count": len(packet_candidates),
        "candidates": packet_candidates,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "batch-002-contexts.json").write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    summary = [
        "# Nannūl Terminology Contextual Review — Batch 002",
        "",
        "**Context packet only. No review decision is encoded here.**",
        "",
        f"Candidates: **{len(packet_candidates)}** remaining source-heading-supported exact forms.",
        "",
    ]
    for index, c in enumerate(packet_candidates, start=1):
        summary += [
            f"## {index}. `{c['surface_form_ta']}` — `{c['candidate_id']}`",
            "",
            f"- Mechanical review rank: {c['review_rank']}",
            f"- Exact body occurrences: {c['occurrence_count']}",
            f"- Source-heading matches: {len(c['source_heading_matches'])}",
            f"- Record numbers: {', '.join(str(n) for n in c['numbers_all'])}",
            "",
        ]
    (OUT / "batch-002-contexts.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    # One readable file per candidate for contextual review.
    for index, c in enumerate(packet_candidates, start=1):
        lines = [
            f"# Nannūl Terminology Review Batch 002 — Candidate {index:02d}",
            "",
            "**Context packet only; no decision is encoded here.**",
            "",
            f"## `{c['surface_form_ta']}` — `{c['candidate_id']}`",
            "",
            f"- Mechanical review rank: **{c['review_rank']}**",
            f"- Occurrences: **{c['occurrence_count']}**",
            f"- Record numbers: {', '.join(str(n) for n in c['numbers_all'])}",
            f"- Structural units: {', '.join(u['unit_label_ta'] for u in c['structural_units'])}",
            "- Source-heading evidence:",
        ]
        for h in c["source_heading_matches"]:
            lines.append(f"  - `{h['heading_id']}` — **{h['heading_text_ta']}** — {h['start_number']}–{h['end_number']}")
        lines += ["", "### Review contexts", ""]
        for ctx in c["contexts"]:
            variant = f"; variants: {', '.join(ctx['source_variant_refs'])}" if ctx["source_variant_refs"] else ""
            heading_note = ""
            if ctx["source_heading_evidence"]:
                h = ctx["source_heading_evidence"]
                heading_note = f"\nSource-heading evidence: **{h['heading_text_ta']}** ({h['start_number']}–{h['end_number']})"
            lines += [
                f"#### {ctx['record_id']} — நூற்பா {ctx['number']} — {ctx['unit_label_ta']}{variant}",
                f"Evidence role: `{ctx['evidence_role']}`",
                f"Record heading: {ctx['topic_heading_ta'] or '(none)'}{heading_note}",
                "",
                "```text",
                ctx["text_ta"],
                "```",
                "",
            ]
        (OUT / f"batch-002-candidate-{index:02d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": "PASS",
        "batch_id": BATCH_ID,
        "candidate_count": len(packet_candidates),
        "forms": [c["surface_form_ta"] for c in packet_candidates],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
