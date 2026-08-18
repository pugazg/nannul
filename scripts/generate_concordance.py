#!/usr/bin/env python3
"""Generate source-heading and exact-surface lexical concordances for Nannul.

Derived inputs only:
- data/nurpa.json

This script never edits canonical Tamil files. Lexical tokens are exact non-whitespace
substrings of each record's text_ta. No Unicode normalization, punctuation stripping,
stemming, sandhi splitting, case folding, or spelling normalization is applied.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "nurpa.json"
HEADING_JSON = ROOT / "data" / "source-heading-index.json"
HEADING_MD = ROOT / "indexes" / "source-heading-index.md"
CONCORDANCE_JSON = ROOT / "data" / "word-form-concordance.json"
TOKEN_NDJSON = ROOT / "data" / "token-occurrences.ndjson"
VALIDATION_JSON = ROOT / "data" / "concordance-validation.json"

TOKEN_RE = re.compile(r"\S+", re.UNICODE)
EXPECTED_RECORD_COUNT = 460
EXPECTED_GAPS = {73, 176}
EXPECTED_NUMBERS = set(range(1, 463)) - EXPECTED_GAPS


def dump_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def build_heading_index(records: list[dict]) -> dict:
    occurrences: list[dict] = []
    current: dict | None = None

    for rec in records:
        key = (
            rec["canonical_file"],
            rec["section_id"],
            rec["unit_id"],
            rec.get("topic_heading_ta"),
        )
        if current is None or current["_key"] != key:
            if current is not None:
                current.pop("_key")
                occurrences.append(current)
            current = {
                "_key": key,
                "heading_id": f"nannul-heading-{len(occurrences) + 1:03d}",
                "heading_text_ta": rec.get("topic_heading_ta"),
                "section_id": rec["section_id"],
                "section_label_ta": rec["section_label_ta"],
                "unit_id": rec["unit_id"],
                "unit_label_ta": rec["unit_label_ta"],
                "canonical_file": rec["canonical_file"],
                "start_number": rec["number"],
                "end_number": rec["number"],
                "record_ids": [rec["id"]],
            }
        else:
            current["end_number"] = rec["number"]
            current["record_ids"].append(rec["id"])

    if current is not None:
        current.pop("_key")
        occurrences.append(current)

    for item in occurrences:
        item["record_count"] = len(item["record_ids"])

    distinct_texts = []
    seen = set()
    for item in occurrences:
        text = item["heading_text_ta"]
        if text not in seen:
            seen.add(text)
            distinct_texts.append(text)

    return {
        "schema_version": 1,
        "work_id": "nannul",
        "source_dataset": "data/nurpa.json",
        "derivation_policy": "contiguous occurrences of exact topic_heading_ta values already derived from audited canonical Markdown headings",
        "counts": {
            "canonical_records": len(records),
            "heading_occurrences": len(occurrences),
            "distinct_heading_texts": len(distinct_texts),
        },
        "heading_occurrences": occurrences,
    }


def write_heading_markdown(index: dict) -> None:
    lines = [
        "# Nannūl Source Heading Index",
        "",
        "This index is derived from the source-supported Markdown headings already attached to canonical records in `data/nurpa.json`.",
        "",
        "It records **heading occurrences**, not editorial topics. Identical heading text appearing in different structural locations remains separately addressable.",
        "",
        "No heading wording is normalized or translated.",
        "",
        f"- Canonical records covered: **{index['counts']['canonical_records']}**",
        f"- Heading occurrences: **{index['counts']['heading_occurrences']}**",
        f"- Distinct exact heading texts: **{index['counts']['distinct_heading_texts']}**",
        "",
        "| Heading ID | Exact source-supported heading | Structural unit | Numbers | Records |",
        "|---|---|---|---:|---:|",
    ]
    for h in index["heading_occurrences"]:
        heading = (h["heading_text_ta"] or "").replace("|", "\\|")
        unit = h["unit_label_ta"].replace("|", "\\|")
        numbers = str(h["start_number"]) if h["start_number"] == h["end_number"] else f"{h['start_number']}–{h['end_number']}"
        lines.append(
            f"| `{h['heading_id']}` | {heading} | {unit} | {numbers} | {h['record_count']} |"
        )
    lines.extend([
        "",
        "Machine-readable form: `data/source-heading-index.json`.",
        "",
        "Stable நூற்பா IDs remain authoritative for individual unit addressing; heading IDs address derived heading occurrences only.",
    ])
    HEADING_MD.parent.mkdir(parents=True, exist_ok=True)
    HEADING_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_lexical_concordance(records: list[dict]) -> tuple[dict, list[dict], dict]:
    forms: OrderedDict[str, dict] = OrderedDict()
    all_occurrences: list[dict] = []
    record_token_counts: dict[str, int] = {}
    substring_validation_failures: list[dict] = []

    global_index = 0
    for rec in records:
        text = rec["text_ta"]
        per_line_token_index: defaultdict[int, int] = defaultdict(int)
        record_count = 0

        for match in TOKEN_RE.finditer(text):
            surface = match.group(0)
            start = match.start()
            end = match.end()
            line_number = text.count("\n", 0, start) + 1
            line_start = text.rfind("\n", 0, start) + 1
            column_start = start - line_start + 1
            per_line_token_index[line_number] += 1
            global_index += 1
            record_count += 1

            if text[start:end] != surface:
                substring_validation_failures.append({
                    "record_id": rec["id"],
                    "start": start,
                    "end": end,
                    "surface_form": surface,
                })

            occurrence = {
                "occurrence_index": global_index,
                "surface_form": surface,
                "record_id": rec["id"],
                "number": rec["number"],
                "section_id": rec["section_id"],
                "unit_id": rec["unit_id"],
                "topic_heading_ta": rec.get("topic_heading_ta"),
                "character_start": start,
                "character_end": end,
                "line_number": line_number,
                "column_start": column_start,
                "token_index_in_line": per_line_token_index[line_number],
            }
            all_occurrences.append(occurrence)

            if surface not in forms:
                forms[surface] = {
                    "surface_form": surface,
                    "count": 0,
                    "first_seen_occurrence": global_index,
                    "first_seen_record_id": rec["id"],
                    "occurrences": [],
                }
            entry = forms[surface]
            entry["count"] += 1
            entry["occurrences"].append({
                "record_id": rec["id"],
                "number": rec["number"],
                "character_start": start,
                "character_end": end,
                "line_number": line_number,
                "token_index_in_line": per_line_token_index[line_number],
            })

        record_token_counts[rec["id"]] = record_count

    concordance = {
        "schema_version": 1,
        "work_id": "nannul",
        "source_dataset": "data/nurpa.json",
        "tokenization": {
            "unit": "exact non-whitespace substring matched by Python regex \\S+",
            "normalization": "none",
            "punctuation_stripping": False,
            "unicode_normalization": False,
            "stemming": False,
            "sandhi_splitting": False,
            "ordering": "first occurrence in canonical source order",
        },
        "counts": {
            "canonical_records": len(records),
            "token_occurrences": len(all_occurrences),
            "unique_surface_forms": len(forms),
        },
        "forms": list(forms.values()),
    }

    validation = {
        "record_token_counts": record_token_counts,
        "substring_validation_failures": substring_validation_failures,
    }
    return concordance, all_occurrences, validation


def write_token_ndjson(occurrences: list[dict]) -> None:
    TOKEN_NDJSON.parent.mkdir(parents=True, exist_ok=True)
    with TOKEN_NDJSON.open("w", encoding="utf-8", newline="\n") as f:
        for occurrence in occurrences:
            f.write(json.dumps(occurrence, ensure_ascii=False, separators=(",", ":")) + "\n")


def validate_dataset(records: list[dict], heading_index: dict, concordance: dict, lexical_validation: dict) -> dict:
    numbers = [r["number"] for r in records]
    ids = [r["id"] for r in records]
    number_set = set(numbers)

    heading_record_ids = [rid for h in heading_index["heading_occurrences"] for rid in h["record_ids"]]
    heading_coverage_ok = heading_record_ids == ids

    total_form_counts = sum(item["count"] for item in concordance["forms"])
    token_occurrences = concordance["counts"]["token_occurrences"]

    status = "PASS"
    checks = {
        "record_count_is_460": len(records) == EXPECTED_RECORD_COUNT,
        "record_ids_unique": len(ids) == len(set(ids)),
        "numbers_unique": len(numbers) == len(number_set),
        "numbers_match_expected_canonical_set": number_set == EXPECTED_NUMBERS,
        "source_gaps_absent_from_records": EXPECTED_GAPS.isdisjoint(number_set),
        "heading_index_covers_records_in_source_order_exactly_once": heading_coverage_ok,
        "surface_form_substrings_match_exact_text": not lexical_validation["substring_validation_failures"],
        "sum_of_concordance_counts_matches_occurrences": total_form_counts == token_occurrences,
        "all_surface_forms_nonempty": all(item["surface_form"] for item in concordance["forms"]),
    }
    if not all(checks.values()):
        status = "FAIL"

    return {
        "status": status,
        "source_dataset": "data/nurpa.json",
        "checks": checks,
        "counts": {
            "canonical_records": len(records),
            "heading_occurrences": heading_index["counts"]["heading_occurrences"],
            "distinct_heading_texts": heading_index["counts"]["distinct_heading_texts"],
            "token_occurrences": token_occurrences,
            "unique_surface_forms": concordance["counts"]["unique_surface_forms"],
        },
        "reserved_source_gaps": sorted(EXPECTED_GAPS),
        "missing_expected_canonical_numbers": sorted(EXPECTED_NUMBERS - number_set),
        "unexpected_numbers": sorted(number_set - EXPECTED_NUMBERS),
        "substring_validation_failures": lexical_validation["substring_validation_failures"],
        "outputs": {
            "heading_json": str(HEADING_JSON.relative_to(ROOT)),
            "heading_markdown": str(HEADING_MD.relative_to(ROOT)),
            "word_form_concordance": str(CONCORDANCE_JSON.relative_to(ROOT)),
            "token_occurrences_ndjson": str(TOKEN_NDJSON.relative_to(ROOT)),
        },
        "hashes": {},
        "derivation_status": "derived only from validated data/nurpa.json; no canonical Tamil text modified",
    }


def main() -> None:
    dataset = json.loads(DATASET.read_text(encoding="utf-8"))
    records = dataset["records"]

    if len(records) != EXPECTED_RECORD_COUNT:
        raise SystemExit(f"Expected {EXPECTED_RECORD_COUNT} records, found {len(records)}")

    heading_index = build_heading_index(records)
    dump_json(HEADING_JSON, heading_index)
    write_heading_markdown(heading_index)

    concordance, occurrences, lexical_validation = build_lexical_concordance(records)
    dump_json(CONCORDANCE_JSON, concordance)
    write_token_ndjson(occurrences)

    validation = validate_dataset(records, heading_index, concordance, lexical_validation)
    for path in (HEADING_JSON, HEADING_MD, CONCORDANCE_JSON, TOKEN_NDJSON):
        validation["hashes"][str(path.relative_to(ROOT))] = sha256(path)
    dump_json(VALIDATION_JSON, validation)

    if validation["status"] != "PASS":
        raise SystemExit("Concordance validation failed; inspect data/concordance-validation.json")

    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
