#!/usr/bin/env python3
"""Generate Phase-2 terminology review Batch 006 context packets.

Selection: the next 25 highest-priority unreviewed candidates with no exact
source-heading-token evidence after Batches 001–005. Frequency/structural breadth
determines review order only; it is not treated as semantic confidence.

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
BATCH_ID = "NANNUL-TERM-REVIEW-006"
EXPECTED_COUNT = 25


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
    eligible = [
        c for c in candidates_obj["candidates"]
        if not c["evidence"]["source_heading_matches"] and c["candidate_id"] not in reviewed_ids
    ]
    eligible.sort(key=lambda c: c["review_rank"])
    selected = eligible[:EXPECTED_COUNT]
    if len(selected) != EXPECTED_COUNT:
        raise SystemExit(f"Expected {EXPECTED_COUNT} frequency-only candidates, found {len(selected)}")
    if any(c["evidence"]["source_heading_matches"] for c in selected):
        raise SystemExit("Batch 006 selection unexpectedly contains heading-supported candidate")

    records = nurpa_obj["records"]
    record_by_id = {r["id"]: r for r in records}
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

        representative_ids: list[str] = []
        def add_id(rid: str):
            if rid not in representative_ids:
                representative_ids.append(rid)

        if len(occurrence_record_ids) <= 12:
            for rid in occurrence_record_ids:
                add_id(rid)
        else:
            add_id(occurrence_record_ids[0])
            add_id(occurrence_record_ids[-1])
            for rids in unit_records.values():
                add_id(rids[0])
                add_id(rids[-1])
            n = len(occurrence_record_ids)
            for i in range(12):
                idx = round(i * (n - 1) / 11)
                add_id(occurrence_record_ids[idx])
            for rid in occurrence_record_ids:
                if record_by_id[rid].get("source_variant_refs"):
                    add_id(rid)

        contexts = []
        for rid in representative_ids:
            rec = record_by_id[rid]
            offsets = [
                {"character_start": o["character_start"], "character_end": o["character_end"]}
                for o in occurrences if o["record_id"] == rid
            ]
            contexts.append({
                "record_id": rid,
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
            })

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
            "source_heading_matches": [],
            "source_variant_refs": candidate["evidence"]["source_variant_refs"],
            "representative_context_count": len(contexts),
            "contexts": contexts,
        })

    packet = {
        "schema_version": 1,
        "work_id": "nannul",
        "phase": "terminology-contextual-review",
        "batch_id": BATCH_ID,
        "selection_policy": "next 25 highest-priority unreviewed frequency-only candidates after Batches 001-005; no source-heading-token evidence",
        "decision_status": "context-packet-only-no-decisions",
        "candidate_count": len(packet_candidates),
        "candidates": packet_candidates,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "batch-006-contexts.json").write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    summary = [
        "# Nannūl Terminology Contextual Review — Batch 006",
        "",
        "**Context packet only. No review decision is encoded here.**",
        "",
        "Selection: **next 25 highest-priority unreviewed frequency-only candidates**.",
        "",
        "Frequency/structural breadth determines review order only; it does not establish termhood.",
        "",
    ]
    for index, c in enumerate(packet_candidates, start=1):
        summary += [
            f"## {index}. `{c['surface_form_ta']}` — `{c['candidate_id']}`",
            "",
            f"- Mechanical review rank: {c['review_rank']}",
            f"- Exact body occurrences: {c['occurrence_count']}",
            f"- Structural units: {len(c['structural_units'])}",
            f"- Representative contexts: {c['representative_context_count']}",
            f"- Record numbers: {', '.join(str(n) for n in c['numbers_all'])}",
            "",
        ]
    (OUT / "batch-006-contexts.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    for index, c in enumerate(packet_candidates, start=1):
        lines = [
            f"# Nannūl Terminology Review Batch 006 — Candidate {index:02d}",
            "",
            "**Context packet only; no decision is encoded here.**",
            "",
            f"## `{c['surface_form_ta']}` — `{c['candidate_id']}`",
            "",
            f"- Mechanical review rank: **{c['review_rank']}**",
            f"- Occurrences: **{c['occurrence_count']}**",
            f"- Record numbers: {', '.join(str(n) for n in c['numbers_all'])}",
            f"- Structural units: {', '.join(u['unit_label_ta'] for u in c['structural_units'])}",
            "- Source-heading evidence: **none**",
            f"- Representative contexts inspected by packet: **{c['representative_context_count']}**",
            "",
            "### Review contexts",
            "",
        ]
        for ctx in c["contexts"]:
            variant = f"; variants: {', '.join(ctx['source_variant_refs'])}" if ctx["source_variant_refs"] else ""
            lines += [
                f"#### {ctx['record_id']} — நூற்பா {ctx['number']} — {ctx['unit_label_ta']}{variant}",
                f"Record heading: {ctx['topic_heading_ta'] or '(none)'}",
                "",
                "```text",
                ctx["text_ta"],
                "```",
                "",
            ]
        (OUT / f"batch-006-candidate-{index:02d}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({"status": "PASS", "batch_id": BATCH_ID, "candidate_count": len(packet_candidates), "forms": [c["surface_form_ta"] for c in packet_candidates]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
