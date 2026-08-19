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
OUT = DATA / "grammatical-terminology-review-validation.json"
EXPECTED_TOTAL = 455
GAPS = {73, 176}
EXPECTED_BATCHES = {
    "NANNUL-TERM-REVIEW-001": 20,
    "NANNUL-TERM-REVIEW-002": 17,
    "NANNUL-TERM-REVIEW-003": 25,
    "NANNUL-TERM-REVIEW-004": 25,
    "NANNUL-TERM-REVIEW-005": 25,
    "NANNUL-TERM-REVIEW-006": 25,
    "NANNUL-TERM-REVIEW-007": 25,
    "NANNUL-TERM-REVIEW-008": 25,
}


def load(path: Path): return json.loads(path.read_text(encoding="utf-8"))
def sha(path: Path): return hashlib.sha256(path.read_bytes()).hexdigest()


def write_summary(batch_id: str, rows: list[dict]) -> Path:
    num = batch_id.split("-")[-1]
    path = REVIEWS / f"batch-{num}-decisions.md"
    lines = [
        f"# Nannūl Grammatical Terminology Review — Batch {num} Decisions", "",
        "Human/contextual review under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.", "",
        f"- Reviewed: **{len(rows)}**",
        f"- Accepted: **{sum(r['decision']=='accepted' for r in rows)}**",
        f"- Rejected: **{sum(r['decision']=='rejected' for r in rows)}**",
        f"- Needs context: **{sum(r['decision']=='needs-context' for r in rows)}**", "",
        "| Candidate | Exact form | Decision | Category | Reviewed evidence |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        surface = r["surface_form_ta"].replace("|", "\\|")
        evidence = ", ".join(f"`{x}`" for x in r["reviewed_record_ids"])
        lines.append(f"| `{r['candidate_id']}` | `{surface}` | **{r['decision']}** | `{r.get('term_category') or '—'}` | {evidence} |")
        lines += ["", f"**Rationale — `{surface}`:** {r['rationale']}"]
        if r.get("term_use_record_ids"):
            lines.append("Technical-use records: " + ", ".join(f"`{x}`" for x in r["term_use_record_ids"]) + ".")
        if r.get("non_term_use_record_ids"):
            lines.append("Known non-term-use records: " + ", ".join(f"`{x}`" for x in r["non_term_use_record_ids"]) + ".")
        if r.get("review_notes"): lines.append("Review note: " + r["review_notes"])
        lines.append("")
    path.write_text("\n".join(lines)+"\n", encoding="utf-8")
    return path


def main() -> None:
    candidate_validation = load(CANDIDATE_VALIDATION)
    candidate_obj = load(CANDIDATES)
    ledger = load(REVIEW)
    nurpa = load(NURPA)
    candidates = candidate_obj["candidates"]
    candidate_by_id = {c["candidate_id"]: c for c in candidates}
    record_by_id = {r["id"]: r for r in nurpa["records"]}
    decisions = ledger["decisions"]
    failures = []

    if len(candidates) != EXPECTED_TOTAL: failures.append({"reason":"candidate-count","actual":len(candidates)})
    if len(candidate_by_id) != len(candidates): failures.append({"reason":"candidate-ids-not-unique"})

    seen = set()
    for d in decisions:
        cid = d["candidate_id"]
        if cid in seen: failures.append({"reason":"duplicate-decision","candidate_id":cid})
        seen.add(cid)
        c = candidate_by_id.get(cid)
        if not c:
            failures.append({"reason":"unknown-candidate","candidate_id":cid}); continue
        if c["surface_form_ta"] != d["surface_form_ta"]: failures.append({"reason":"surface-mismatch","candidate_id":cid})
        reviewed = d.get("reviewed_record_ids", [])
        term = d.get("term_use_record_ids", [])
        nonterm = d.get("non_term_use_record_ids", [])
        if not reviewed: failures.append({"reason":"no-reviewed-records","candidate_id":cid})
        if len(reviewed) != len(set(reviewed)): failures.append({"reason":"duplicate-reviewed-record","candidate_id":cid})
        for rid in reviewed:
            rec = record_by_id.get(rid)
            if not rec: failures.append({"reason":"unknown-reviewed-record","candidate_id":cid,"record_id":rid})
            elif rec["number"] in GAPS: failures.append({"reason":"source-gap-used","candidate_id":cid,"record_id":rid})
        if not set(term).issubset(reviewed): failures.append({"reason":"term-use-not-subset","candidate_id":cid})
        if not set(nonterm).issubset(reviewed): failures.append({"reason":"non-term-use-not-subset","candidate_id":cid})
        if set(term) & set(nonterm): failures.append({"reason":"term-nonterm-overlap","candidate_id":cid})
        if d["decision"] == "accepted":
            if not d.get("term_category"): failures.append({"reason":"accepted-without-category","candidate_id":cid})
            if not term: failures.append({"reason":"accepted-without-term-evidence","candidate_id":cid})
        elif d["decision"] == "rejected":
            if d.get("term_category") is not None: failures.append({"reason":"rejected-with-category","candidate_id":cid})
            if term: failures.append({"reason":"rejected-with-term-evidence","candidate_id":cid})
            if not nonterm: failures.append({"reason":"rejected-without-nonterm-evidence","candidate_id":cid})
        elif d["decision"] != "needs-context": failures.append({"reason":"invalid-decision","candidate_id":cid})
        if not d.get("rationale"): failures.append({"reason":"missing-rationale","candidate_id":cid})

    dist = Counter(d["decision"] for d in decisions)
    counts = {
        "candidate_surface_forms": len(candidates), "reviewed": len(decisions),
        "accepted": dist.get("accepted",0), "rejected": dist.get("rejected",0),
        "needs_context": dist.get("needs-context",0), "unreviewed": len(candidates)-len(decisions),
    }
    if ledger.get("counts") != counts: failures.append({"reason":"ledger-counts-do-not-reconcile"})
    expected_status = "review-complete" if counts["unreviewed"] == 0 else ("review-not-started" if not decisions else "review-in-progress")
    if ledger.get("layer_status") != expected_status: failures.append({"reason":"layer-status-mismatch"})

    batches = {bid:[d for d in decisions if d.get("review_batch")==bid] for bid in EXPECTED_BATCHES}
    for bid, expected in EXPECTED_BATCHES.items():
        if len(batches[bid]) != expected: failures.append({"reason":"batch-count","batch":bid,"expected":expected,"actual":len(batches[bid])})

    REVIEWS.mkdir(parents=True, exist_ok=True)
    summaries = {bid: write_summary(bid, rows) for bid, rows in batches.items()}
    checks = {
        "candidate_discovery_validation_pass": candidate_validation.get("status") == "PASS",
        "candidate_count_is_455": len(candidates) == EXPECTED_TOTAL,
        "decision_candidate_ids_unique": len(seen) == len(decisions),
        "all_decisions_reference_valid_candidates_and_records": not failures,
        "ledger_counts_reconcile": ledger.get("counts") == counts,
        "layer_status_matches_coverage": ledger.get("layer_status") == expected_status,
        **{f"batch_{bid[-3:]}_has_{expected}_decisions": len(batches[bid]) == expected for bid, expected in EXPECTED_BATCHES.items()},
    }
    if candidate_validation.get("status") != "PASS": failures.append({"reason":"candidate-discovery-validation-not-pass"})
    status = "PASS" if all(checks.values()) and not failures else "FAIL"
    category_counts = Counter(d.get("term_category") for d in decisions if d["decision"]=="accepted")
    result = {
        "status": status,
        "source_review_ledger": "data/grammatical-terminology-review.json",
        "checks": checks, "counts": counts,
        "batches": {bid:{"decision_count":len(rows),"accepted":sum(d["decision"]=="accepted" for d in rows),"rejected":sum(d["decision"]=="rejected" for d in rows),"needs_context":sum(d["decision"]=="needs-context" for d in rows)} for bid,rows in batches.items()},
        "accepted_category_counts": {str(k):v for k,v in sorted(category_counts.items(), key=lambda x:str(x[0]))},
        "failures": failures,
        "interpretation_boundary": "PASS validates ledger identity, evidence links, decision structure, and counts; it does not replace human semantic review.",
        "hashes": {"data/grammatical-terminology-review.json": sha(REVIEW), **{f"reviews/terminology/{p.name}":sha(p) for p in summaries.values()}},
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    if status != "PASS": raise SystemExit("Terminology review validation failed")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__": main()
