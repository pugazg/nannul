#!/usr/bin/env python3
"""Generate a contextual review packet for Nannul terminology Phase 2 Batch 1.

This script is a derived review aid only. It does not make or write terminology
review decisions.

Selection: first 20 candidates in mechanical review-rank order that carry exact
source-heading-token evidence.

For each candidate the packet includes:
- stable candidate ID and exact surface form;
- discovery rank/score and all source-heading evidence;
- complete occurrence coverage by record and structural unit;
- representative full canonical contexts: first occurrence, one occurrence from
  every structural unit, at least one candidate occurrence from every matching
  source-heading range, and every occurrence in a source-variant-linked record.

No canonical Tamil is changed or normalized.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT_DIR = ROOT / "reviews" / "terminology"

CANDIDATES = DATA / "grammatical-terminology-candidates.json"
TOKENS = DATA / "token-occurrences.ndjson"
NURPA = DATA / "nurpa.json"
OUT_JSON = OUT_DIR / "batch-001-contexts.json"
OUT_MD = OUT_DIR / "batch-001-contexts.md"
BATCH_SIZE = 20


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_ndjson(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def main() -> None:
    candidates_obj = load_json(CANDIDATES)
    nurpa_obj = load_json(NURPA)
    token_rows = load_ndjson(TOKENS)
    record_by_id = {r["id"]: r for r in nurpa_obj["records"]}

    selected = [
        c for c in candidates_obj["candidates"]
        if c["evidence"]["source_heading_matches"]
    ][:BATCH_SIZE]

    if len(selected) != BATCH_SIZE:
        raise SystemExit(f"Expected {BATCH_SIZE} heading-supported candidates, found {len(selected)}")

    occurrences_by_form: dict[str, list[dict]] = defaultdict(list)
    selected_forms = {c["surface_form_ta"] for c in selected}
    for row in token_rows:
        if row["surface_form"] in selected_forms:
            occurrences_by_form[row["surface_form"]].append(row)

    packet_candidates = []
    for candidate in selected:
        surface = candidate["surface_form_ta"]
        occurrences = occurrences_by_form[surface]
        if len(occurrences) != candidate["evidence"]["occurrence_count"]:
            raise SystemExit(f"Occurrence count mismatch for {surface}")

        record_ids = list(dict.fromkeys(o["record_id"] for o in occurrences))
        units: dict[str, list[str]] = defaultdict(list)
        for rid in record_ids:
            rec = record_by_id[rid]
            units[rec["unit_id"]].append(rid)

        selected_context_ids: list[str] = []
        # First occurrence.
        selected_context_ids.append(occurrences[0]["record_id"])
        # At least one occurrence from every structural unit.
        for unit_id in units:
            selected_context_ids.append(units[unit_id][0])
        # At least one candidate occurrence inside every matching source-heading range.
        for heading in candidate["evidence"]["source_heading_matches"]:
            heading_occurrence = next(
                (
                    o for o in occurrences
                    if heading["start_number"] <= o["number"] <= heading["end_number"]
                ),
                None,
            )
            if heading_occurrence is None:
                raise SystemExit(
                    f"Heading evidence for {surface} has no candidate occurrence in "
                    f"{heading['start_number']}-{heading['end_number']}"
                )
            selected_context_ids.append(heading_occurrence["record_id"])
        # Every candidate-occurrence record carrying a documented source variant.
        for rid in record_ids:
            if record_by_id[rid].get("source_variant_refs"):
                selected_context_ids.append(rid)
        selected_context_ids = list(dict.fromkeys(selected_context_ids))

        contexts = []
        for rid in selected_context_ids:
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
            "record_ids_all": record_ids,
            "numbers_all": [record_by_id[rid]["number"] for rid in record_ids],
            "structural_units": [
                {
                    "unit_id": uid,
                    "unit_label_ta": record_by_id[rids[0]]["unit_label_ta"],
                    "record_ids": rids,
                }
                for uid, rids in units.items()
            ],
            "source_heading_matches": candidate["evidence"]["source_heading_matches"],
            "source_variant_refs": candidate["evidence"]["source_variant_refs"],
            "representative_contexts": contexts,
        })

    packet = {
        "schema_version": 2,
        "work_id": "nannul",
        "phase": "terminology-contextual-review",
        "batch_id": "NANNUL-TERM-REVIEW-001",
        "selection_policy": "first 20 mechanical-rank candidates carrying exact source-heading-token evidence",
        "context_selection_policy": "first occurrence + one per structural unit + one in every matching source-heading range + all variant-linked candidate records",
        "decision_status": "context-packet-only-no-decisions",
        "candidate_count": len(packet_candidates),
        "candidates": packet_candidates,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Nannūl Terminology Contextual Review — Batch 001",
        "",
        "**Derived review packet only. This file makes no term decisions.**",
        "",
        "Selection: first 20 mechanically ranked candidates with exact source-heading-token evidence.",
        "",
        "For each candidate, all heading evidence and complete record-number coverage are listed; full canonical text is included for the first occurrence, one occurrence in every structural unit, at least one candidate occurrence inside every matching source-heading range, and any source-variant-linked occurrence.",
        "",
    ]
    for c in packet_candidates:
        lines += [
            f"## {c['review_rank']}. `{c['surface_form_ta']}` — `{c['candidate_id']}`",
            "",
            f"- Occurrences: **{c['occurrence_count']}**",
            f"- Record numbers with the exact form: {', '.join(str(n) for n in c['numbers_all'])}",
            f"- Structural units: {', '.join(u['unit_label_ta'] for u in c['structural_units'])}",
            f"- Source-heading matches: **{len(c['source_heading_matches'])}**",
            "",
            "### Source-heading evidence",
            "",
        ]
        for h in c["source_heading_matches"]:
            lines.append(f"- `{h['heading_id']}` — **{h['heading_text_ta']}** — {h['start_number']}–{h['end_number']}")
        lines += ["", "### Representative canonical contexts", ""]
        for ctx in c["representative_contexts"]:
            variant = f"; variants: {', '.join(ctx['source_variant_refs'])}" if ctx["source_variant_refs"] else ""
            lines += [
                f"#### {ctx['record_id']} — நூற்பா {ctx['number']} — {ctx['unit_label_ta']}{variant}",
                "",
                f"Source heading: {ctx['topic_heading_ta'] or '(none)'}",
                "",
                "```text",
                ctx["text_ta"],
                "```",
                "",
            ]

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PASS", "batch_id": packet["batch_id"], "candidate_count": len(packet_candidates)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
