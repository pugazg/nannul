#!/usr/bin/env python3
"""Split terminology Batch 1 context packet into 4 readable 5-candidate parts."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "reviews" / "terminology" / "batch-001-contexts.json"
OUT = ROOT / "reviews" / "terminology"
PART_SIZE = 5

packet = json.loads(SRC.read_text(encoding="utf-8"))
candidates = packet["candidates"]
if len(candidates) != 20:
    raise SystemExit(f"Expected 20 candidates, found {len(candidates)}")

for part_index in range(4):
    subset = candidates[part_index * PART_SIZE:(part_index + 1) * PART_SIZE]
    lines = [
        f"# Nannūl Terminology Review Batch 001 — Part {part_index + 1}",
        "",
        "**Context packet only; no decisions are encoded here.**",
        "",
    ]
    for c in subset:
        lines += [
            f"## {c['review_rank']}. `{c['surface_form_ta']}` — `{c['candidate_id']}`",
            "",
            f"- Occurrences: **{c['occurrence_count']}**",
            f"- Record numbers: {', '.join(str(n) for n in c['numbers_all'])}",
            f"- Structural units: {', '.join(u['unit_label_ta'] for u in c['structural_units'])}",
            "- Source-heading evidence:",
        ]
        for h in c["source_heading_matches"]:
            lines.append(f"  - `{h['heading_id']}` — **{h['heading_text_ta']}** — {h['start_number']}–{h['end_number']}")
        lines += ["", "### Representative contexts", ""]
        for ctx in c["representative_contexts"]:
            variant = f"; variants: {', '.join(ctx['source_variant_refs'])}" if ctx["source_variant_refs"] else ""
            lines += [
                f"#### {ctx['record_id']} — நூற்பா {ctx['number']} — {ctx['unit_label_ta']}{variant}",
                f"Heading: {ctx['topic_heading_ta'] or '(none)'}",
                "",
                "```text",
                ctx["text_ta"],
                "```",
                "",
            ]
    path = OUT / f"batch-001-part-{part_index + 1:02d}.md"
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("PASS: wrote 4 review packet parts")
