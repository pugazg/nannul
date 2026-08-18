#!/usr/bin/env python3
"""Generate one-record-per-canonical-nurpa datasets from audited Markdown.

This script is intentionally deterministic and standard-library only. It reads the
existing canonical Tamil layer plus data/nurpa-index.json, validates the complete
number set against the controlling-witness gaps (73 and 176), and writes derived
machine-readable data without modifying any canonical Tamil file.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "data" / "nurpa-index.json"
OUT_JSON = ROOT / "data" / "nurpa.json"
OUT_NDJSON = ROOT / "data" / "nurpa.ndjson"
OUT_VALIDATION = ROOT / "data" / "nurpa-validation.json"

CONTROLLING_SOURCE = "project-madurai:pmuni0147"
EXPECTED_GAPS = {73: "PM147-V001", 176: "PM147-V003"}
KNOWN_VARIANTS = {
    240: ["PM147-V002"],
    241: ["PM147-V002"],
    242: ["PM147-V002"],
    343: ["PM147-V004"],
    344: ["PM147-V005"],
}

SECTION_LABELS = {
    "pothu-payiram": "பொதுப்பாயிரம்",
    "ezhuththathikaram": "எழுத்ததிகாரம்",
    "sollathikaram": "சொல்லதிகாரம்",
}

UNIT_LABELS = {
    "pothu-payiram-intro": "பொதுப்பாயிரம்",
    "nool-varalaru": "நூலினது வரலாறு",
    "aasiriyan-varalaru": "ஆசிரியனது வரலாறு",
    "paadam-sollal-varalaru": "பாடஞ் சொல்லலினது வரலாறு",
    "maanakkar-varalaru": "மாணாக்கனது வரலாறு",
    "paadam-kettal-varalaru": "பாடங் கேட்டலின் வரலாறு",
    "sirappu-payira-ilakkanam": "சிறப்புப்பாயிர இலக்கணம்",
    "ezhuthu-iyal": "எழுத்து இயல்",
    "pathaviyal": "பதவியல்",
    "uyireetru-punariyal": "உயிரீற்றுப் புணரியல்",
    "meyyeetru-punariyal": "மெய்யீற்றுப் புணரியல்",
    "urubu-punariyal": "உருபு புணரியல்",
    "peyariyal": "பெயரியல்",
    "vinaiyiyal": "வினையியல்",
    "pothuviyal": "பொதுவியல்",
    "idaiyiyal": "இடையியல்",
    "uriyiyal": "உரியியல்",
}

NUMBERED_RE = re.compile(r"^(\d+)\.\s*(.*)$")
HEADING_RE = re.compile(r"^(#{2,6})\s+(.+?)\s*$")


def stable_id(number: int) -> str:
    return f"nannul-{number:04d}"


def load_index() -> dict:
    with INDEX_PATH.open("r", encoding="utf-8") as handle:
        index = json.load(handle)
    if index["counts"] != {
        "nominal_numbered_positions": 462,
        "canonical_displayed_numbered_units": 460,
        "reserved_source_gap_positions": 2,
    }:
        raise ValueError("Unexpected counts in data/nurpa-index.json")
    gap_numbers = {item["number"] for item in index["source_gaps"]}
    if gap_numbers != set(EXPECTED_GAPS):
        raise ValueError(f"Unexpected source gaps in index: {sorted(gap_numbers)}")
    return index


def resolve_segment(number: int, segments: list[dict]) -> dict:
    matches = [segment for segment in segments if segment["start"] <= number <= segment["end"]]
    if len(matches) != 1:
        raise ValueError(f"Number {number} resolves to {len(matches)} segments")
    return matches[0]


def flush_record(
    records: list[dict],
    number: int | None,
    text_lines: list[str],
    topic_heading: str | None,
    canonical_file: str,
    segment: dict | None,
) -> None:
    if number is None:
        return
    if segment is None:
        raise ValueError(f"No segment for {number}")
    text = "\n".join(line for line in text_lines if line != "").strip()
    if not text:
        raise ValueError(f"Empty canonical text for {number}")
    records.append(
        {
            "id": stable_id(number),
            "number": number,
            "text_ta": text,
            "text_line_count": len(text.splitlines()),
            "section_id": segment["section_id"],
            "section_label_ta": SECTION_LABELS[segment["section_id"]],
            "unit_id": segment["unit_id"],
            "unit_label_ta": UNIT_LABELS[segment["unit_id"]],
            "topic_heading_ta": topic_heading,
            "canonical_file": canonical_file,
            "source_status": "canonical",
            "controlling_source": CONTROLLING_SOURCE,
            "source_variant_refs": KNOWN_VARIANTS.get(number, []),
        }
    )


def parse_canonical_file(canonical_file: str, segment: dict) -> list[dict]:
    path = ROOT / canonical_file
    if not path.is_file():
        raise FileNotFoundError(canonical_file)

    records: list[dict] = []
    current_number: int | None = None
    current_lines: list[str] = []
    current_heading: str | None = None
    current_record_heading: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()

        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush_record(
                records,
                current_number,
                current_lines,
                current_record_heading,
                canonical_file,
                segment,
            )
            current_number = None
            current_lines = []
            current_record_heading = None
            current_heading = heading_match.group(2).strip()
            continue

        number_match = NUMBERED_RE.match(line)
        if number_match:
            flush_record(
                records,
                current_number,
                current_lines,
                current_record_heading,
                canonical_file,
                segment,
            )
            current_number = int(number_match.group(1))
            current_lines = [number_match.group(2)]
            current_record_heading = current_heading
            continue

        if current_number is not None:
            if line == "---":
                flush_record(
                    records,
                    current_number,
                    current_lines,
                    current_record_heading,
                    canonical_file,
                    segment,
                )
                current_number = None
                current_lines = []
                current_record_heading = None
                continue
            if line.strip():
                current_lines.append(line)

    flush_record(
        records,
        current_number,
        current_lines,
        current_record_heading,
        canonical_file,
        segment,
    )
    return records


def build_records(index: dict) -> list[dict]:
    records: list[dict] = []
    for segment in index["segments"]:
        records.extend(parse_canonical_file(segment["canonical_file"], segment))

    # A canonical file can back multiple பொதுப்பாயிரம் structural segments, so
    # parsing segment-by-segment would duplicate it. Deduplicate by source number,
    # then resolve final structural parentage from the complete segment map.
    by_number: dict[int, dict] = {}
    duplicates: dict[int, list[dict]] = {}
    for record in records:
        number = record["number"]
        if number in by_number:
            duplicates.setdefault(number, [by_number[number]]).append(record)
        else:
            by_number[number] = record

    # Duplicates are expected only because multiple subsection segments can point
    # to the same physical canonical file. They must have identical source text.
    for number, group in duplicates.items():
        texts = {item["text_ta"] for item in group}
        if len(texts) != 1:
            raise ValueError(f"Conflicting duplicate text while deriving number {number}")

    final_records: list[dict] = []
    for number in sorted(by_number):
        record = by_number[number]
        segment = resolve_segment(number, index["segments"])
        record["section_id"] = segment["section_id"]
        record["section_label_ta"] = SECTION_LABELS[segment["section_id"]]
        record["unit_id"] = segment["unit_id"]
        record["unit_label_ta"] = UNIT_LABELS[segment["unit_id"]]
        record["canonical_file"] = segment["canonical_file"]
        final_records.append(record)

    return final_records


def validate(records: list[dict]) -> dict:
    numbers = [record["number"] for record in records]
    ids = [record["id"] for record in records]
    expected_numbers = [number for number in range(1, 463) if number not in EXPECTED_GAPS]

    if numbers != expected_numbers:
        missing = sorted(set(expected_numbers) - set(numbers))
        extra = sorted(set(numbers) - set(expected_numbers))
        raise ValueError(f"Canonical number-set mismatch: missing={missing}, extra={extra}")
    if len(numbers) != 460:
        raise ValueError(f"Expected 460 records, found {len(numbers)}")
    if len(set(numbers)) != len(numbers):
        raise ValueError("Duplicate source numbers in canonical records")
    if len(set(ids)) != len(ids):
        raise ValueError("Duplicate stable IDs in canonical records")
    if any(number in numbers for number in EXPECTED_GAPS):
        raise ValueError("A reserved source-gap position was emitted as canonical text")
    if any(not record["text_ta"].strip() for record in records):
        raise ValueError("Empty canonical text found")

    per_section = Counter(record["section_id"] for record in records)
    per_unit = Counter(record["unit_id"] for record in records)
    per_file = Counter(record["canonical_file"] for record in records)

    return {
        "status": "PASS",
        "record_count": len(records),
        "first_number": numbers[0],
        "last_number": numbers[-1],
        "unique_ids": len(set(ids)),
        "reserved_source_gaps": sorted(EXPECTED_GAPS),
        "missing_expected_canonical_numbers": [],
        "unexpected_numbers": [],
        "per_section_counts": dict(sorted(per_section.items())),
        "per_unit_counts": dict(sorted(per_unit.items())),
        "per_file_counts": dict(sorted(per_file.items())),
    }


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def write_outputs(index: dict, records: list[dict], validation: dict) -> None:
    dataset = {
        "schema_version": 1,
        "work": {
            "id": "nannul",
            "title_ta": "நன்னூல்",
            "author_ta": "பவணந்தி முனிவர்",
        },
        "derivation": {
            "source_layer": "text/tamil",
            "controlling_source": CONTROLLING_SOURCE,
            "identifier_policy": "structure/identifiers.yml",
            "segment_index": "data/nurpa-index.json",
            "canonical_completion_audit": "audit/NANNUL_CANONICAL_COMPLETION.md",
            "generator": "scripts/generate_nurpa_dataset.py",
            "status": "derived-from-audited-canonical-text",
        },
        "counts": {
            "nominal_numbered_positions": 462,
            "canonical_records": 460,
            "reserved_source_gap_positions": 2,
        },
        "source_gaps": index["source_gaps"],
        "records": records,
    }

    json_text = json.dumps(dataset, ensure_ascii=False, indent=2) + "\n"
    ndjson_text = "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in records
    )

    OUT_JSON.write_text(json_text, encoding="utf-8")
    OUT_NDJSON.write_text(ndjson_text, encoding="utf-8")

    validation = {
        **validation,
        "dataset": "data/nurpa.json",
        "ndjson": "data/nurpa.ndjson",
        "json_sha256": sha256_bytes(json_text.encode("utf-8")),
        "ndjson_sha256": sha256_bytes(ndjson_text.encode("utf-8")),
        "derivation_status": "no canonical Tamil text modified",
    }
    OUT_VALIDATION.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    index = load_index()
    records = build_records(index)
    validation = validate(records)
    write_outputs(index, records, validation)
    print(
        f"PASS: generated {len(records)} canonical records; "
        f"reserved gaps={sorted(EXPECTED_GAPS)}"
    )


if __name__ == "__main__":
    main()
