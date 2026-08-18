#!/usr/bin/env python3
"""Generate exact-surface frequency profiles for Nannul.

Inputs are already-audited derived layers:
- data/nurpa.json
- data/token-occurrences.ndjson
- data/source-heading-index.json
- data/concordance-validation.json

This script does not tokenize or normalize Tamil. It only aggregates the existing
exact token occurrences by source section, structural unit, source-heading
occurrence, and explicitly unheaded source span.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASET = ROOT / "data" / "nurpa.json"
TOKEN_NDJSON = ROOT / "data" / "token-occurrences.ndjson"
HEADING_INDEX = ROOT / "data" / "source-heading-index.json"
CONCORDANCE_VALIDATION = ROOT / "data" / "concordance-validation.json"

PROFILES_JSON = ROOT / "data" / "frequency-profiles.json"
TABLES_JSON = ROOT / "data" / "frequency-tables.json"
PROFILE_MD = ROOT / "indexes" / "frequency-profiles.md"
VALIDATION_JSON = ROOT / "data" / "frequency-profiles-validation.json"

EXPECTED_RECORDS = 460
EXPECTED_TOKEN_OCCURRENCES = 5431
EXPECTED_UNIQUE_FORMS = 2837
EXPECTED_GAPS = {73, 176}
TOP_N = 20


def dump_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_tokens() -> list[dict]:
    rows: list[dict] = []
    with TOKEN_NDJSON.open(encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            row["_input_line"] = line_number
            rows.append(row)
    return rows


def ordered_record_groups(records: list[dict], key_fn) -> OrderedDict[str, list[dict]]:
    groups: OrderedDict[str, list[dict]] = OrderedDict()
    for rec in records:
        key = key_fn(rec)
        groups.setdefault(key, []).append(rec)
    return groups


def token_stats(record_ids: list[str], tokens_by_record: dict[str, list[dict]]) -> tuple[dict, list[dict]]:
    occurrences = [tok for rid in record_ids for tok in tokens_by_record.get(rid, [])]
    counts: Counter[str] = Counter(tok["surface_form"] for tok in occurrences)
    first_seen: dict[str, int] = {}
    for tok in occurrences:
        first_seen.setdefault(tok["surface_form"], tok["occurrence_index"])

    frequency_rows = [
        {
            "surface_form": surface,
            "count": count,
            "first_seen_occurrence": first_seen[surface],
        }
        for surface, count in counts.items()
    ]
    frequency_rows.sort(key=lambda item: (-item["count"], item["first_seen_occurrence"], item["surface_form"]))

    stats = {
        "record_count": len(record_ids),
        "token_occurrences": len(occurrences),
        "unique_surface_forms": len(counts),
        "hapax_surface_forms": sum(1 for count in counts.values() if count == 1),
        "top_surface_forms": [
            {"surface_form": item["surface_form"], "count": item["count"]}
            for item in frequency_rows[:TOP_N]
        ],
    }
    return stats, frequency_rows


def number_span(records: list[dict]) -> dict:
    numbers = [r["number"] for r in records]
    return {
        "start_number": min(numbers),
        "end_number": max(numbers),
        "record_ids": [r["id"] for r in records],
    }


def profile_row(base: dict, records: list[dict], tokens_by_record: dict[str, list[dict]]) -> tuple[dict, dict]:
    span = number_span(records)
    stats, frequency_rows = token_stats(span["record_ids"], tokens_by_record)
    profile = {**base, **span, **stats}
    table = {
        **base,
        **span,
        "record_count": stats["record_count"],
        "token_occurrences": stats["token_occurrences"],
        "unique_surface_forms": stats["unique_surface_forms"],
        "surface_forms": frequency_rows,
    }
    return profile, table


def build_heading_membership(heading_index: dict) -> tuple[dict[str, dict], dict[str, dict]]:
    heading_by_record: dict[str, dict] = {}
    unheaded_by_record: dict[str, dict] = {}

    for heading in heading_index["heading_occurrences"]:
        for rid in heading["record_ids"]:
            if rid in heading_by_record or rid in unheaded_by_record:
                raise SystemExit(f"Duplicate heading membership for {rid}")
            heading_by_record[rid] = heading

    for span in heading_index["unheaded_spans"]:
        for rid in span["record_ids"]:
            if rid in heading_by_record or rid in unheaded_by_record:
                raise SystemExit(f"Duplicate heading membership for {rid}")
            unheaded_by_record[rid] = span

    return heading_by_record, unheaded_by_record


def build_profiles(records: list[dict], tokens: list[dict], heading_index: dict) -> tuple[dict, dict, list[dict]]:
    record_by_id = {r["id"]: r for r in records}
    tokens_by_record: dict[str, list[dict]] = defaultdict(list)
    token_link_failures: list[dict] = []

    for tok in tokens:
        rid = tok["record_id"]
        rec = record_by_id.get(rid)
        if rec is None:
            token_link_failures.append({"input_line": tok["_input_line"], "reason": "unknown-record-id", "record_id": rid})
            continue
        expected_surface = rec["text_ta"][tok["character_start"]:tok["character_end"]]
        if expected_surface != tok["surface_form"]:
            token_link_failures.append({
                "input_line": tok["_input_line"],
                "reason": "surface-offset-mismatch",
                "record_id": rid,
                "surface_form": tok["surface_form"],
            })
        if tok["number"] != rec["number"] or tok["section_id"] != rec["section_id"] or tok["unit_id"] != rec["unit_id"]:
            token_link_failures.append({
                "input_line": tok["_input_line"],
                "reason": "structural-metadata-mismatch",
                "record_id": rid,
            })
        if tok.get("topic_heading_ta") != rec.get("topic_heading_ta"):
            token_link_failures.append({
                "input_line": tok["_input_line"],
                "reason": "heading-metadata-mismatch",
                "record_id": rid,
            })
        tokens_by_record[rid].append(tok)

    section_groups = ordered_record_groups(records, lambda r: r["section_id"])
    unit_groups = ordered_record_groups(records, lambda r: r["unit_id"])
    heading_by_record, unheaded_by_record = build_heading_membership(heading_index)

    section_profiles: list[dict] = []
    section_tables: list[dict] = []
    for section_id, recs in section_groups.items():
        first = recs[0]
        base = {"section_id": section_id, "section_label_ta": first["section_label_ta"]}
        profile, table = profile_row(base, recs, tokens_by_record)
        section_profiles.append(profile)
        section_tables.append(table)

    unit_profiles: list[dict] = []
    unit_tables: list[dict] = []
    for unit_id, recs in unit_groups.items():
        first = recs[0]
        base = {
            "section_id": first["section_id"],
            "section_label_ta": first["section_label_ta"],
            "unit_id": unit_id,
            "unit_label_ta": first["unit_label_ta"],
        }
        profile, table = profile_row(base, recs, tokens_by_record)
        unit_profiles.append(profile)
        unit_tables.append(table)

    heading_profiles: list[dict] = []
    heading_tables: list[dict] = []
    for heading in heading_index["heading_occurrences"]:
        recs = [record_by_id[rid] for rid in heading["record_ids"]]
        base = {
            "heading_id": heading["heading_id"],
            "heading_text_ta": heading["heading_text_ta"],
            "section_id": heading["section_id"],
            "section_label_ta": heading["section_label_ta"],
            "unit_id": heading["unit_id"],
            "unit_label_ta": heading["unit_label_ta"],
        }
        profile, table = profile_row(base, recs, tokens_by_record)
        heading_profiles.append(profile)
        heading_tables.append(table)

    unheaded_profiles: list[dict] = []
    unheaded_tables: list[dict] = []
    for span in heading_index["unheaded_spans"]:
        recs = [record_by_id[rid] for rid in span["record_ids"]]
        base = {
            "unheaded_span_id": span["unheaded_span_id"],
            "status": span["status"],
            "section_id": span["section_id"],
            "section_label_ta": span["section_label_ta"],
            "unit_id": span["unit_id"],
            "unit_label_ta": span["unit_label_ta"],
        }
        profile, table = profile_row(base, recs, tokens_by_record)
        unheaded_profiles.append(profile)
        unheaded_tables.append(table)

    all_record_ids = [r["id"] for r in records]
    global_stats, global_frequency = token_stats(all_record_ids, tokens_by_record)
    global_profile = {
        "start_number": records[0]["number"],
        "end_number": records[-1]["number"],
        **global_stats,
    }
    global_table = {
        "start_number": records[0]["number"],
        "end_number": records[-1]["number"],
        "record_count": global_stats["record_count"],
        "token_occurrences": global_stats["token_occurrences"],
        "unique_surface_forms": global_stats["unique_surface_forms"],
        "surface_forms": global_frequency,
    }

    profiles = {
        "schema_version": 1,
        "work_id": "nannul",
        "source_dataset": "data/nurpa.json",
        "source_token_occurrences": "data/token-occurrences.ndjson",
        "source_heading_index": "data/source-heading-index.json",
        "aggregation_policy": {
            "surface_form": "exact existing token-occurrence surface_form; no re-tokenization or normalization",
            "group_order": "first canonical source occurrence",
            "frequency_order": "descending count, then first global occurrence, then exact surface form",
            "top_n": TOP_N,
            "interpretation": "mechanical frequency only; no grammatical-term classification",
        },
        "global": global_profile,
        "by_section": section_profiles,
        "by_unit": unit_profiles,
        "by_heading": heading_profiles,
        "unheaded_spans": unheaded_profiles,
    }

    tables = {
        "schema_version": 1,
        "work_id": "nannul",
        "frequency_semantics": "exact surface-form counts inherited from data/token-occurrences.ndjson; no normalization",
        "global": global_table,
        "by_section": section_tables,
        "by_unit": unit_tables,
        "by_heading": heading_tables,
        "unheaded_spans": unheaded_tables,
    }

    return profiles, tables, token_link_failures


def top_forms_text(profile: dict, limit: int = 5) -> str:
    forms = profile["top_surface_forms"][:limit]
    return ", ".join(f"`{item['surface_form']}` ({item['count']})" for item in forms) if forms else "—"


def write_markdown(profiles: dict) -> None:
    g = profiles["global"]
    lines = [
        "# Nannūl Exact-Surface Frequency Profiles",
        "",
        "These profiles aggregate the already validated exact token occurrences. They do **not** re-tokenize, normalize, stem, split sandhi, or classify grammatical terminology.",
        "",
        f"- Canonical numbered records: **{g['record_count']}**",
        f"- Exact token occurrences: **{g['token_occurrences']:,}**",
        f"- Unique exact surface forms: **{g['unique_surface_forms']:,}**",
        f"- Hapax surface forms in the complete work: **{g['hapax_surface_forms']:,}**",
        "",
        "## Whole-work leading exact surface forms",
        "",
    ]
    for item in g["top_surface_forms"]:
        lines.append(f"- `{item['surface_form']}` — **{item['count']}**")

    lines.extend([
        "",
        "## By source section / அதிகார-level division",
        "",
        "| Section | Numbers | Records | Tokens | Unique forms | Hapax forms | Leading exact forms |",
        "|---|---:|---:|---:|---:|---:|---|",
    ])
    for p in profiles["by_section"]:
        lines.append(
            f"| {p['section_label_ta']} | {p['start_number']}–{p['end_number']} | {p['record_count']} | "
            f"{p['token_occurrences']:,} | {p['unique_surface_forms']:,} | {p['hapax_surface_forms']:,} | {top_forms_text(p)} |"
        )

    lines.extend([
        "",
        "## By இயல் / structural unit",
        "",
        "| Unit | Parent section | Numbers | Records | Tokens | Unique forms | Hapax forms | Leading exact forms |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ])
    for p in profiles["by_unit"]:
        lines.append(
            f"| {p['unit_label_ta']} | {p['section_label_ta']} | {p['start_number']}–{p['end_number']} | {p['record_count']} | "
            f"{p['token_occurrences']:,} | {p['unique_surface_forms']:,} | {p['hapax_surface_forms']:,} | {top_forms_text(p)} |"
        )

    lines.extend([
        "",
        "## By actual source-heading occurrence",
        "",
        "| Heading ID | Exact source heading | Unit | Numbers | Records | Tokens | Unique forms | Leading exact forms |",
        "|---|---|---|---:|---:|---:|---:|---|",
    ])
    for p in profiles["by_heading"]:
        heading = p["heading_text_ta"].replace("|", "\\|")
        lines.append(
            f"| `{p['heading_id']}` | {heading} | {p['unit_label_ta']} | {p['start_number']}–{p['end_number']} | {p['record_count']} | "
            f"{p['token_occurrences']:,} | {p['unique_surface_forms']:,} | {top_forms_text(p)} |"
        )

    lines.extend(["", "## Unheaded source spans", ""])
    for p in profiles["unheaded_spans"]:
        lines.append(
            f"- `{p['unheaded_span_id']}` — {p['unit_label_ta']} — நூற்பாக்கள் {p['start_number']}–{p['end_number']}: "
            f"**{p['token_occurrences']}** token occurrences, **{p['unique_surface_forms']}** unique exact forms."
        )
    if not profiles["unheaded_spans"]:
        lines.append("- None.")

    lines.extend([
        "",
        "## Machine-readable outputs",
        "",
        "- `data/frequency-profiles.json` — group summaries and top-20 exact forms;",
        "- `data/frequency-tables.json` — complete exact surface-form frequency tables for every group;",
        "- `data/frequency-profiles-validation.json` — reconciliation and integrity checks.",
        "",
        "Frequency is descriptive only. A repeated lexical form is **not** classified as a grammatical term by this layer.",
    ])

    PROFILE_MD.parent.mkdir(parents=True, exist_ok=True)
    PROFILE_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def validate(records: list[dict], tokens: list[dict], heading_index: dict, profiles: dict, tables: dict, token_link_failures: list[dict]) -> dict:
    numbers = {r["number"] for r in records}
    expected_numbers = set(range(1, 463)) - EXPECTED_GAPS
    ids = [r["id"] for r in records]

    section_token_sum = sum(p["token_occurrences"] for p in profiles["by_section"])
    unit_token_sum = sum(p["token_occurrences"] for p in profiles["by_unit"])
    heading_token_sum = sum(p["token_occurrences"] for p in profiles["by_heading"])
    unheaded_token_sum = sum(p["token_occurrences"] for p in profiles["unheaded_spans"])

    section_record_ids = [rid for p in profiles["by_section"] for rid in p["record_ids"]]
    unit_record_ids = [rid for p in profiles["by_unit"] for rid in p["record_ids"]]
    heading_record_ids = [rid for p in profiles["by_heading"] for rid in p["record_ids"]]
    unheaded_record_ids = [rid for p in profiles["unheaded_spans"] for rid in p["record_ids"]]

    global_form_count_sum = sum(item["count"] for item in tables["global"]["surface_forms"])

    checks = {
        "canonical_record_count_is_460": len(records) == EXPECTED_RECORDS,
        "record_ids_unique": len(ids) == len(set(ids)),
        "canonical_numbers_match_expected_set": numbers == expected_numbers,
        "reserved_source_gaps_absent": EXPECTED_GAPS.isdisjoint(numbers),
        "input_token_occurrence_count_is_5431": len(tokens) == EXPECTED_TOKEN_OCCURRENCES,
        "input_token_links_and_offsets_match_canonical_records": not token_link_failures,
        "global_token_count_matches_input": profiles["global"]["token_occurrences"] == len(tokens),
        "global_unique_surface_forms_is_2837": profiles["global"]["unique_surface_forms"] == EXPECTED_UNIQUE_FORMS,
        "global_frequency_counts_reconcile": global_form_count_sum == len(tokens),
        "section_token_totals_reconcile": section_token_sum == len(tokens),
        "unit_token_totals_reconcile": unit_token_sum == len(tokens),
        "heading_plus_unheaded_token_totals_reconcile": heading_token_sum + unheaded_token_sum == len(tokens),
        "section_records_cover_canonical_records_once_in_source_order": section_record_ids == ids,
        "unit_records_cover_canonical_records_once_in_source_order": unit_record_ids == ids,
        "heading_plus_unheaded_records_cover_all_exactly_once": sorted(heading_record_ids + unheaded_record_ids) == sorted(ids) and len(heading_record_ids) + len(unheaded_record_ids) == len(ids),
        "heading_profile_count_matches_heading_index": len(profiles["by_heading"]) == heading_index["counts"]["heading_occurrences"],
        "unheaded_profile_count_matches_heading_index": len(profiles["unheaded_spans"]) == heading_index["counts"]["unheaded_spans"],
        "all_profile_frequency_tables_reconcile": all(
            sum(item["count"] for item in table["surface_forms"]) == table["token_occurrences"]
            for collection in (tables["by_section"], tables["by_unit"], tables["by_heading"], tables["unheaded_spans"])
            for table in collection
        ),
    }

    return {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "inputs": {
            "canonical_dataset": "data/nurpa.json",
            "token_occurrences": "data/token-occurrences.ndjson",
            "heading_index": "data/source-heading-index.json",
            "concordance_validation": "data/concordance-validation.json",
        },
        "checks": checks,
        "counts": {
            "canonical_records": len(records),
            "token_occurrences": len(tokens),
            "unique_surface_forms": profiles["global"]["unique_surface_forms"],
            "hapax_surface_forms": profiles["global"]["hapax_surface_forms"],
            "section_profiles": len(profiles["by_section"]),
            "unit_profiles": len(profiles["by_unit"]),
            "heading_profiles": len(profiles["by_heading"]),
            "unheaded_profiles": len(profiles["unheaded_spans"]),
        },
        "reserved_source_gaps": sorted(EXPECTED_GAPS),
        "token_link_failures": token_link_failures,
        "outputs": {
            "profiles": str(PROFILES_JSON.relative_to(ROOT)),
            "tables": str(TABLES_JSON.relative_to(ROOT)),
            "markdown": str(PROFILE_MD.relative_to(ROOT)),
        },
        "hashes": {},
        "derivation_status": "mechanical aggregation only; canonical Tamil and exact token surfaces unchanged",
    }


def main() -> None:
    dataset = json.loads(DATASET.read_text(encoding="utf-8"))
    heading_index = json.loads(HEADING_INDEX.read_text(encoding="utf-8"))
    concordance_validation = json.loads(CONCORDANCE_VALIDATION.read_text(encoding="utf-8"))
    tokens = load_tokens()
    records = dataset["records"]

    if concordance_validation.get("status") != "PASS":
        raise SystemExit("Input concordance validation is not PASS")
    if concordance_validation.get("counts", {}).get("token_occurrences") != EXPECTED_TOKEN_OCCURRENCES:
        raise SystemExit("Input concordance token count does not match expected audited count")
    if concordance_validation.get("counts", {}).get("unique_surface_forms") != EXPECTED_UNIQUE_FORMS:
        raise SystemExit("Input concordance unique-form count does not match expected audited count")

    profiles, tables, token_link_failures = build_profiles(records, tokens, heading_index)
    dump_json(PROFILES_JSON, profiles)
    dump_json(TABLES_JSON, tables)
    write_markdown(profiles)

    validation = validate(records, tokens, heading_index, profiles, tables, token_link_failures)
    for path in (PROFILES_JSON, TABLES_JSON, PROFILE_MD):
        validation["hashes"][str(path.relative_to(ROOT))] = sha256(path)
    dump_json(VALIDATION_JSON, validation)

    if validation["status"] != "PASS":
        raise SystemExit("Frequency-profile validation failed; inspect data/frequency-profiles-validation.json")
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
