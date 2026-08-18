#!/usr/bin/env python3
"""Generate an unreviewed grammatical-terminology candidate queue for Nannul.

This is candidate DISCOVERY only. It does not classify or accept any surface form as
a grammatical technical term.

Inputs are existing validated derived layers only:
- data/nurpa.json
- data/token-occurrences.ndjson
- data/source-heading-index.json
- data/frequency-profiles-validation.json

Selection is deliberately mechanical and broad:
1. exact surface form occurs at least MIN_FREQUENCY times in canonical token data; OR
2. exact surface form is also an exact non-whitespace token in a source-supported heading.

No canonical Tamil is modified. No lexical normalization, punctuation stripping,
stemming, lemmatization, sandhi splitting, semantic grouping, or synonym merging is
performed.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
INDEX_DIR = ROOT / "indexes"

NURPA = DATA_DIR / "nurpa.json"
TOKENS = DATA_DIR / "token-occurrences.ndjson"
HEADINGS = DATA_DIR / "source-heading-index.json"
UPSTREAM_VALIDATION = DATA_DIR / "frequency-profiles-validation.json"

OUT_JSON = DATA_DIR / "grammatical-terminology-candidates.json"
OUT_NDJSON = DATA_DIR / "grammatical-terminology-candidates.ndjson"
OUT_MD = INDEX_DIR / "grammatical-terminology-review-queue.md"
OUT_VALIDATION = DATA_DIR / "grammatical-terminology-candidates-validation.json"

EXPECTED_RECORD_COUNT = 460
EXPECTED_TOKEN_COUNT = 5431
EXPECTED_GAPS = {73, 176}
MIN_FREQUENCY = 3
HEADING_TOKEN_RE = re.compile(r"\S+", re.UNICODE)
SAMPLE_LIMIT = 8
CANDIDATE_HASH_HEX = 16


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_ndjson(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid NDJSON at {path}:{line_number}: {exc}") from exc
    return rows


def dump_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def stable_candidate_id(surface: str) -> str:
    digest = hashlib.sha256(surface.encode("utf-8")).hexdigest()[:CANDIDATE_HASH_HEX]
    return f"nannul-term-candidate-{digest}"


def priority_score(total_count: int, section_count: int, unit_count: int, heading_match: bool) -> tuple[int, list[str]]:
    """Mechanical review-priority score, explicitly not semantic confidence."""
    score = 0
    reasons: list[str] = []

    if heading_match:
        score += 5
        reasons.append("exact-source-heading-token-match:+5")

    if total_count >= 10:
        score += 3
        reasons.append("frequency>=10:+3")
    elif total_count >= 5:
        score += 2
        reasons.append("frequency>=5:+2")
    elif total_count >= MIN_FREQUENCY:
        score += 1
        reasons.append(f"frequency>={MIN_FREQUENCY}:+1")

    if unit_count >= 3:
        score += 2
        reasons.append("structural-units>=3:+2")
    elif unit_count >= 2:
        score += 1
        reasons.append("structural-units>=2:+1")

    if section_count >= 2:
        score += 1
        reasons.append("major-sections>=2:+1")

    return score, reasons


def heading_evidence(headings: dict) -> tuple[dict[str, list[dict]], set[str]]:
    by_token: dict[str, list[dict]] = defaultdict(list)
    exact_tokens: set[str] = set()

    for heading in headings["heading_occurrences"]:
        text = heading["heading_text_ta"]
        seen_here: set[str] = set()
        for match in HEADING_TOKEN_RE.finditer(text):
            token = match.group(0)
            exact_tokens.add(token)
            if token in seen_here:
                continue
            seen_here.add(token)
            by_token[token].append({
                "heading_id": heading["heading_id"],
                "heading_text_ta": text,
                "section_id": heading["section_id"],
                "unit_id": heading["unit_id"],
                "start_number": heading["start_number"],
                "end_number": heading["end_number"],
                "match_policy": "exact non-whitespace heading token; no normalization",
            })
    return by_token, exact_tokens


def main() -> None:
    upstream = load_json(UPSTREAM_VALIDATION)
    if upstream.get("status") != "PASS":
        raise SystemExit("Upstream frequency profile validation is not PASS")

    dataset = load_json(NURPA)
    records = dataset["records"]
    if len(records) != EXPECTED_RECORD_COUNT:
        raise SystemExit(f"Expected {EXPECTED_RECORD_COUNT} canonical records; found {len(records)}")

    record_by_id = {r["id"]: r for r in records}
    if len(record_by_id) != EXPECTED_RECORD_COUNT:
        raise SystemExit("Canonical record IDs are not unique")

    canonical_numbers = {r["number"] for r in records}
    expected_numbers = set(range(1, 463)) - EXPECTED_GAPS
    if canonical_numbers != expected_numbers:
        raise SystemExit("Canonical number set no longer matches expected 1-462 excluding 73 and 176")

    token_rows = load_ndjson(TOKENS)
    if len(token_rows) != EXPECTED_TOKEN_COUNT:
        raise SystemExit(f"Expected {EXPECTED_TOKEN_COUNT} exact token occurrences; found {len(token_rows)}")

    headings = load_json(HEADINGS)
    heading_by_token, heading_tokens = heading_evidence(headings)
    known_heading_texts = {x["heading_text_ta"] for x in headings["heading_occurrences"]}

    form_counts: Counter[str] = Counter()
    form_occurrences: dict[str, list[dict]] = defaultdict(list)
    token_link_failures: list[dict] = []

    for row in token_rows:
        surface = row["surface_form"]
        record = record_by_id.get(row["record_id"])
        if record is None:
            token_link_failures.append({"reason": "unknown-record-id", "occurrence": row})
            continue
        if row["number"] != record["number"] or row["section_id"] != record["section_id"] or row["unit_id"] != record["unit_id"]:
            token_link_failures.append({"reason": "structural-link-mismatch", "occurrence": row})
            continue
        start = row["character_start"]
        end = row["character_end"]
        if record["text_ta"][start:end] != surface:
            token_link_failures.append({"reason": "character-offset-mismatch", "occurrence": row})
            continue
        form_counts[surface] += 1
        form_occurrences[surface].append(row)

    if token_link_failures:
        raise SystemExit("Token links no longer match canonical records; inspect upstream derived data")

    selected_forms = {
        form for form, count in form_counts.items()
        if count >= MIN_FREQUENCY or form in heading_tokens
    }

    candidates: list[dict] = []
    for surface in selected_forms:
        occurrences = form_occurrences[surface]
        record_ids = list(dict.fromkeys(o["record_id"] for o in occurrences))
        sections = list(dict.fromkeys(o["section_id"] for o in occurrences))
        units = list(dict.fromkeys(o["unit_id"] for o in occurrences))
        topic_headings = list(dict.fromkeys(o["topic_heading_ta"] for o in occurrences if o.get("topic_heading_ta")))
        heading_matches = heading_by_token.get(surface, [])
        score, score_reasons = priority_score(len(occurrences), len(sections), len(units), bool(heading_matches))

        first = occurrences[0]
        first_record = record_by_id[first["record_id"]]
        variant_refs = sorted({
            variant
            for rid in record_ids
            for variant in record_by_id[rid].get("source_variant_refs", [])
        })

        discovery_reasons: list[str] = []
        if len(occurrences) >= MIN_FREQUENCY:
            discovery_reasons.append(f"exact-surface-frequency>={MIN_FREQUENCY}")
        if heading_matches:
            discovery_reasons.append("exact-source-heading-token-match")

        candidates.append({
            "candidate_id": stable_candidate_id(surface),
            "surface_form_ta": surface,
            "review_status": "unreviewed",
            "term_decision": None,
            "term_category": None,
            "review_notes": None,
            "discovery_reasons": discovery_reasons,
            "review_priority_score": score,
            "review_priority_score_basis": score_reasons,
            "evidence": {
                "occurrence_count": len(occurrences),
                "record_count": len(record_ids),
                "major_section_count": len(sections),
                "structural_unit_count": len(units),
                "topic_heading_context_count": len(topic_headings),
                "major_section_ids": sections,
                "structural_unit_ids": units,
                "topic_headings_ta": topic_headings,
                "source_heading_matches": heading_matches,
                "source_variant_refs": variant_refs,
                "first_occurrence": {
                    "record_id": first["record_id"],
                    "number": first["number"],
                    "section_id": first["section_id"],
                    "unit_id": first["unit_id"],
                    "topic_heading_ta": first.get("topic_heading_ta"),
                    "character_start": first["character_start"],
                    "character_end": first["character_end"],
                    "canonical_file": first_record["canonical_file"],
                },
                "sample_occurrences": [
                    {
                        "record_id": o["record_id"],
                        "number": o["number"],
                        "section_id": o["section_id"],
                        "unit_id": o["unit_id"],
                        "topic_heading_ta": o.get("topic_heading_ta"),
                        "character_start": o["character_start"],
                        "character_end": o["character_end"],
                    }
                    for o in occurrences[:SAMPLE_LIMIT]
                ],
            },
            "interpretation_warning": "Discovery candidate only. Unreviewed frequency/heading evidence is not a claim that this is a grammatical technical term.",
        })

    # Highest review priority first; then frequency; then first source occurrence; then exact surface.
    first_index = {form: occs[0]["occurrence_index"] for form, occs in form_occurrences.items()}
    candidates.sort(key=lambda c: (
        -c["review_priority_score"],
        -c["evidence"]["occurrence_count"],
        first_index[c["surface_form_ta"]],
        c["surface_form_ta"],
    ))
    for index, candidate in enumerate(candidates, start=1):
        candidate["review_rank"] = index

    output = {
        "schema_version": 2,
        "work_id": "nannul",
        "layer_status": "candidate-discovery-unreviewed",
        "source_layers": {
            "canonical_dataset": "data/nurpa.json",
            "token_occurrences": "data/token-occurrences.ndjson",
            "source_heading_index": "data/source-heading-index.json",
            "upstream_validation": "data/frequency-profiles-validation.json",
        },
        "discovery_policy": {
            "surface_form_policy": "exact existing token surface; no normalization",
            "minimum_frequency": MIN_FREQUENCY,
            "selection_rule": f"exact occurrence count >= {MIN_FREQUENCY} OR exact non-whitespace token match in a source-supported heading",
            "heading_matching": "exact non-whitespace token equality; no normalization",
            "candidate_id": f"nannul-term-candidate- + first {CANDIDATE_HASH_HEX} hex characters of SHA-256(exact UTF-8 surface_form_ta); stable across ranking changes",
            "priority_score": "mechanical review ordering only; NOT probability/confidence of termhood",
            "default_review_status": "unreviewed",
            "automatic_term_acceptance": False,
        },
        "counts": {
            "canonical_records": len(records),
            "token_occurrences": len(token_rows),
            "all_unique_surface_forms": len(form_counts),
            "candidate_surface_forms": len(candidates),
            "frequency_selected_candidates": sum(1 for c in candidates if f"exact-surface-frequency>={MIN_FREQUENCY}" in c["discovery_reasons"]),
            "heading_matched_candidates": sum(1 for c in candidates if "exact-source-heading-token-match" in c["discovery_reasons"]),
            "reviewed_candidates": 0,
            "accepted_terms": 0,
            "rejected_candidates": 0,
        },
        "reserved_source_gaps": sorted(EXPECTED_GAPS),
        "candidates": candidates,
    }
    dump_json(OUT_JSON, output)

    with OUT_NDJSON.open("w", encoding="utf-8", newline="\n") as f:
        for candidate in candidates:
            f.write(json.dumps(candidate, ensure_ascii=False, separators=(",", ":")) + "\n")

    lines = [
        "# Nannūl Grammatical-Terminology Candidate Review Queue",
        "",
        "**Phase 1: candidate discovery only. Nothing in this file is automatically accepted as a grammatical technical term.**",
        "",
        f"Candidates enter this queue when their exact surface form occurs at least **{MIN_FREQUENCY}** times in canonical token data or exactly matches a non-whitespace token in a source-supported heading.",
        "",
        "Candidate IDs are stable hashes of the exact UTF-8 surface form; review rank is separate and may change when evidence changes.",
        "",
        "Ranking is mechanical review priority, not semantic confidence. Every candidate begins `unreviewed` with no category or term decision.",
        "",
        f"- Candidates: **{len(candidates)}**",
        f"- Exact token occurrences considered: **{len(token_rows)}**",
        f"- Unique exact surface forms considered: **{len(form_counts)}**",
        "",
        "| Rank | Candidate | Exact form | Score | Occurrences | Records | Units | Heading cue | Status |",
        "|---:|---|---|---:|---:|---:|---:|---|---|",
    ]
    for c in candidates:
        heading_cue = "yes" if c["evidence"]["source_heading_matches"] else "no"
        exact = c["surface_form_ta"].replace("|", "\\|")
        lines.append(
            f"| {c['review_rank']} | `{c['candidate_id']}` | `{exact}` | {c['review_priority_score']} | "
            f"{c['evidence']['occurrence_count']} | {c['evidence']['record_count']} | "
            f"{c['evidence']['structural_unit_count']} | {heading_cue} | `unreviewed` |"
        )
    lines.extend([
        "",
        "Machine-readable evidence: `data/grammatical-terminology-candidates.json`.",
        "",
        "Streaming review form: `data/grammatical-terminology-candidates.ndjson`.",
        "",
        "A later review phase must explicitly decide `accepted` / `rejected` / `needs-context` and may assign a grammatical category. Discovery ranking must never be promoted automatically to a term decision.",
    ])
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    candidate_forms = [c["surface_form_ta"] for c in candidates]
    candidate_ids = [c["candidate_id"] for c in candidates]
    expected_selected = {
        form for form, count in form_counts.items()
        if count >= MIN_FREQUENCY or form in heading_tokens
    }
    evidence_failures: list[dict] = []
    for c in candidates:
        form = c["surface_form_ta"]
        if c["candidate_id"] != stable_candidate_id(form):
            evidence_failures.append({"candidate_id": c["candidate_id"], "reason": "candidate-id-does-not-match-exact-surface-hash"})
        if c["evidence"]["occurrence_count"] != form_counts[form]:
            evidence_failures.append({"candidate_id": c["candidate_id"], "reason": "occurrence-count-mismatch"})
        if any(h["heading_text_ta"] not in known_heading_texts for h in c["evidence"]["source_heading_matches"]):
            evidence_failures.append({"candidate_id": c["candidate_id"], "reason": "unknown-heading-evidence"})
        if c["review_status"] != "unreviewed" or c["term_decision"] is not None or c["term_category"] is not None:
            evidence_failures.append({"candidate_id": c["candidate_id"], "reason": "candidate-was-auto-classified"})

    checks = {
        "upstream_validation_is_pass": upstream.get("status") == "PASS",
        "canonical_record_count_is_460": len(records) == EXPECTED_RECORD_COUNT,
        "reserved_source_gaps_absent": EXPECTED_GAPS.isdisjoint(canonical_numbers),
        "input_token_occurrence_count_is_5431": len(token_rows) == EXPECTED_TOKEN_COUNT,
        "token_links_and_offsets_match_canonical_records": not token_link_failures,
        "candidate_forms_unique": len(candidate_forms) == len(set(candidate_forms)),
        "candidate_ids_unique": len(candidate_ids) == len(set(candidate_ids)),
        "candidate_ids_match_exact_surface_hashes": all(c["candidate_id"] == stable_candidate_id(c["surface_form_ta"]) for c in candidates),
        "candidate_set_exactly_matches_discovery_rule": set(candidate_forms) == expected_selected,
        "all_candidates_unreviewed": all(c["review_status"] == "unreviewed" for c in candidates),
        "no_candidate_has_automatic_term_decision": all(c["term_decision"] is None for c in candidates),
        "no_candidate_has_automatic_term_category": all(c["term_category"] is None for c in candidates),
        "all_candidate_occurrence_counts_reconcile": not evidence_failures,
        "review_ranks_contiguous": [c["review_rank"] for c in candidates] == list(range(1, len(candidates) + 1)),
    }

    validation = {
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "counts": output["counts"],
        "reserved_source_gaps": sorted(EXPECTED_GAPS),
        "token_link_failures": token_link_failures,
        "candidate_evidence_failures": evidence_failures,
        "outputs": {
            "candidate_json": str(OUT_JSON.relative_to(ROOT)),
            "candidate_ndjson": str(OUT_NDJSON.relative_to(ROOT)),
            "review_queue_markdown": str(OUT_MD.relative_to(ROOT)),
        },
        "hashes": {},
        "interpretation_boundary": "PASS validates mechanical discovery/evidence only; it does not validate grammatical termhood.",
    }
    for path in (OUT_JSON, OUT_NDJSON, OUT_MD):
        validation["hashes"][str(path.relative_to(ROOT))] = sha256(path)
    dump_json(OUT_VALIDATION, validation)

    if validation["status"] != "PASS":
        raise SystemExit("Terminology candidate validation failed; inspect data/grammatical-terminology-candidates-validation.json")

    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
