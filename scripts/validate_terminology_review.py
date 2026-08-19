#!/usr/bin/env python3
"""Validate the human Nannul grammatical-terminology review ledger.

Structural/provenance validation only; semantic judgments remain human/editorial.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REVIEWS = ROOT / "reviews" / "terminology"
CANDIDATES = DATA / "grammatical-terminology-candidates.json"
CANDIDATE_VALIDATION = DATA / "grammatical-terminology-candidates-validation.json"
REVIEW = DATA / "grammatical-terminology-review.json"
NURPA = DATA / "nurpa.json"
OUT_VALIDATION = DATA / "grammatical-terminology-review-validation.json"
EXPECTED_TOTAL_CANDIDATES = 455
EXPECTED_GAPS = {73, 176}
EXPECTED_BATCH_COUNTS = {
    "NANNUL-TERM-REVIEW-001": 20,
    "NANNUL-TERM-REVIEW-002": 17,
    "NANNUL-TERM-REVIEW-003": 25,
    "NANNUL-TERM-REVIEW-004": 25,
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, value: object):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_batch_summary(batch_id: str, decisions: list[dict], filename: str) -> Path:
    path = REVIEWS / filename
    batch_num = batch_id.split("-")[-1]
    lines = [
        f"# Nannūl Grammatical Terminology Review — Batch {batch_num} Decisions",
        "",
        "Human/contextual review under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.",
        "",
        f"- Reviewed: **{len(decisions)}**",
        f"- Accepted: **{sum(1 for d in decisions if d['decision'] == 'accepted')}**",
        f"- Rejected: **{sum(1 for d in decisions if d['decision'] == 'rejected')}**",
        f"- Needs context: **{sum(1 for d in decisions if d['decision'] == 'needs-context')}**",
        "",
        "| Candidate | Exact form | Decision | Category | Reviewed evidence |",
        "|---|---|---|---|---|",
    ]
    for d in decisions:
        category = d.get("term_category") or "—"
        evidence = ", ".join(f"`{rid}`" for rid in d["reviewed_record_ids"])
        surface = d["surface_form_ta"].replace("|", "\\|")
        lines.append(f"| `{d['candidate_id']}` | `{surface}` | **{d['decision']}** | `{category}` | {evidence} |")
        lines += ["", f"**Rationale — `{surface}`:** {d['rationale']}"]
        if d.get("term_use_record_ids"):
            lines.append("Technical-use records: " + ", ".join(f"`{rid}`" for rid in d["term_use_record_ids"]) + ".")
        if d.get("non_term_use_record_ids"):
            lines.append("Known non-term-use records: " + ", ".join(f"`{rid}`" for rid in d["non_term_use_record_ids"]) + ".")
        if d.get("review_notes"):
            lines.append("Review note: " + d["review_notes"])
        lines.append("")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def main() -> None:
    candidate_validation = load_json(CANDIDATE_VALIDATION)
    candidates_obj = load_json(CANDIDATES)
    review = load_json(REVIEW)
    nurpa = load_json(NURPA)

    candidates = candidates_obj["candidates"]
    candidate_by_id = {c["candidate_id"]: c for c in candidates}
    record_by_id = {r["id"]: r for r in nurpa["records"]}
    decisions = review["decisions"]
    failures: list[dict] = []

    if len(candidates) != EXPECTED_TOTAL_CANDIDATES:
        failures.append({"reason": "candidate-count", "value": len(candidates)})
    if len(candidate_by_id) != len(candidates):
        failures.append({"reason": "candidate-ids-not-unique"})

    seen: set[str] = set()
    for d in decisions:
        cid = d["candidate_id"]
        if cid in seen:
            failures.append({"reason": "duplicate-decision", "candidate_id": cid})
        seen.add(cid)
        candidate = candidate_by_id.get(cid)
        if candidate is None:
            failures.append({"reason": "unknown-candidate", "candidate_id": cid})
            continue
        if candidate["surface_form_ta"] != d["surface_form_ta"]:
            failures.append({"reason": "surface-mismatch", "candidate_id": cid})

        reviewed = d.get("reviewed_record_ids", [])
        term_use = d.get("term_use_record_ids", [])
        non_term_use = d.get("non_term_use_record_ids", [])
        if not reviewed:
            failures.append({"reason": "no-reviewed-records", "candidate_id": cid})
        if len(reviewed) != len(set(reviewed)):
            failures.append({"reason": "duplicate-reviewed-record", "candidate_id": cid})
        for rid in reviewed:
            rec = record_by_id.get(rid)
            if rec is None:
                failures.append({"reason": "unknown-reviewed-record", "candidate_id": cid, "record_id": rid})
            elif rec["number"] in EXPECTED_GAPS:
                failures.append({"reason": "source-gap-used-as-reviewed-record", "candidate_id": cid, "record_id": rid})
        if not set(term_use).issubset(reviewed):
            failures.append({"reason": "term-use-not-subset-of-reviewed", "candidate_id": cid})
        if not set(non_term_use).issubset(reviewed):
            failures.append({"reason": "non-term-use-not-subset-of-reviewed", "candidate_id": cid})
        if set(term_use) & set(non_term_use):
            failures.append({"reason": "term-and-non-term-overlap", "candidate_id": cid})

        decision = d["decision"]
        if decision == "accepted":
            if not d.get("term_category"):
                failures.append({"reason": "accepted-without-category", "candidate_id": cid})
            if not term_use:
                failures.append({"reason": "accepted-without-term-use-record", "candidate_id": cid})
        elif decision == "rejected":
            if d.get("term_category") is not None:
                failures.append({"reason": "rejected-with-category", "candidate_id": cid})
            if term_use:
                failures.append({"reason": "rejected-with-term-use-record", "candidate_id": cid})
            if not non_term_use:
                failures.append({"reason": "rejected-without-non-term-context", "candidate_id": cid})
        elif decision != "needs-context":
            failures.append({"reason": "invalid-decision", "candidate_id": cid, "decision": decision})
        if not d.get("rationale"):
            failures.append({"reason": "missing-rationale", "candidate_id": cid})

    distribution = Counter(d["decision"] for d in decisions)
    computed_counts = {
        "candidate_surface_forms": len(candidates),
        "reviewed": len(decisions),
        "accepted": distribution.get("accepted", 0),
        "rejected": distribution.get("rejected", 0),
        "needs_context": distribution.get("needs-context", 0),
        "unreviewed": len(candidates) - len(decisions),
    }
    if review.get("counts") != computed_counts:
        failures.append({"reason": "ledger-counts-do-not-reconcile", "declared": review.get("counts"), "computed": computed_counts})
    expected_status = "review-complete" if computed_counts["unreviewed"] == 0 else ("review-not-started" if not decisions else "review-in-progress")
    if review.get("layer_status") != expected_status:
        failures.append({"reason": "layer-status-mismatch", "declared": review.get("layer_status"), "expected": expected_status})

    batches = {batch_id: [d for d in decisions if d.get("review_batch") == batch_id] for batch_id in EXPECTED_BATCH_COUNTS}
    for batch_id, expected in EXPECTED_BATCH_COUNTS.items():
        if len(batches[batch_id]) != expected:
            failures.append({"reason": "batch-count", "batch": batch_id, "expected": expected, "actual": len(batches[batch_id])})

    checks = {
        "candidate_discovery_validation_pass": candidate_validation.get("status") == "PASS",
        "candidate_count_is_455": len(candidates) == EXPECTED_TOTAL_CANDIDATES,
        "decision_candidate_ids_unique": len(seen) == len(decisions),
        "all_decisions_reference_valid_candidates_and_records": not failures,
        "ledger_counts_reconcile": review.get("counts") == computed_counts,
        "layer_status_matches_coverage": review.get("layer_status") == expected_status,
        "batch_001_has_20_decisions": len(batches["NANNUL-TERM-REVIEW-001"]) == 20,
        "batch_002_has_17_decisions": len(batches["NANNUL-TERM-REVIEW-002"]) == 17,
        "batch_003_has_25_decisions": len(batches["NANNUL-TERM-REVIEW-003"]) == 25,
        "batch_004_has_25_decisions": len(batches["NANNUL-TERM-REVIEW-004"]) == 25,
    }
    if candidate_validation.get("status") != "PASS":
        failures.append({"reason": "candidate-discovery-validation-not-pass"})

    REVIEWS.mkdir(parents=True, exist_ok=True)
    summary_paths = {
        batch_id: write_batch_summary(batch_id, batches[batch_id], f"batch-{batch_id.split('-')[-1]}-decisions.md")
        for batch_id in EXPECTED_BATCH_COUNTS
    }

    status = "PASS" if all(checks.values()) and not failures else "FAIL"
    category_counts = Counter(d.get("term_category") for d in decisions if d["decision"] == "accepted")
    validation = {
        "status": status,
        "source_review_ledger": "data/grammatical-terminology-review.json",
        "checks": checks,
        "counts": computed_counts,
        "batches": {
            batch_id: {
                "decision_count": len(rows),
                "accepted": sum(1 for d in rows if d["decision"] == "accepted"),
                "rejected": sum(1 for d in rows if d["decision"] == "rejected"),
                "needs_context": sum(1 for d in rows if d["decision"] == "needs-context"),
            }
            for batch_id, rows in batches.items()
        },
        "accepted_category_counts": {str(k): v for k, v in sorted(category_counts.items(), key=lambda kv: str(kv[0]))},
        "failures": failures,
        "interpretation_boundary": "PASS validates ledger identity, evidence links, decision structure, and counts; it does not replace human semantic review.",
        "hashes": {
            "data/grammatical-terminology-review.json": sha256(REVIEW),
            **{f"reviews/terminology/batch-{batch_id.split('-')[-1]}-decisions.md": sha256(path) for batch_id, path in summary_paths.items()},
        },
    }
    dump_json(OUT_VALIDATION, validation)
    if status != "PASS":
        raise SystemExit("Terminology review validation failed")
    print(json.dumps(validation, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
