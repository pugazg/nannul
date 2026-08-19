#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 007."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
PACKET = ROOT / "reviews" / "terminology" / "batch-007-contexts.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-007-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-007"
BASIS = "internal-canonical-contexts-frequency-only-tier"

CONFIG = {
    "ஏழ்": ("rejected", None, "The exact form is the ordinary numeral seven across counts and enumerations; grammatical surroundings do not establish independent termhood.", []),
    "ஒழி": ("rejected", None, "ஒழி functions compositionally as 'excluding/except' inside rules and classifications rather than as the name of an independent grammatical concept.", []),
    "ட": ("accepted", "phonology-letter-class", "ட is explicitly enumerated as a வல்லினம் consonant and also occurs in grammatical ending/intermediate inventories and phonological alternation rules.", [68,140,142,183,209,332]),
    "இரண்டும்": ("rejected", None, "இரண்டும் is the inflected numeral 'both/two' used to count grammatical items; it is not an independent technical term.", []),
    "இசை": ("accepted", "other-grammar", "இசை has internally supported grammatical uses involving phonological/prosodic sound, tense/semantic indication, semantic concordance, and particle meaning; ordinary lexical/speech-label uses remain separate.", [101,144,419,424]),
    "ஐந்து": ("rejected", None, "ஐந்து is the ordinary numeral five in inventories and counts, not an independent grammatical term.", []),
    "ஆறும்": ("rejected", None, "ஆறும் is an inflected numeral/counting surface ('six/all six') used within grammatical enumeration, not a standalone term identity.", []),
    "நெறியே": ("rejected", None, "நெறியே is a predicative/emphatic surface meaning 'is the rule/method'; the passages do not establish this exact surface as an independent term identity.", []),
    "தம்": ("accepted", "morphology", "தம் is explicitly listed and manipulated as a சாரியை/form in உருபு-punarcci contexts, while other occurrences are ordinary possessive/reflexive language; acceptance is context-bounded.", [221,244,246]),
    "தாம்": ("rejected", None, "தாம் is a pronoun/example word form subjected to grammatical description; it does not name the grammatical category itself.", []),
    "இயலும்": ("rejected", None, "இயலும் is ordinary finite/compositional rule language ('may/does occur') and not an independent technical term.", []),
    "அன்": ("accepted", "morphology", "அன் is explicitly enumerated as a விகுதி/சாரியை and as an inflectional ending in verbal and nominal systems.", [140,244,251,325,331]),
    "ஊர்": ("accepted", "morphology", "ஊர் is explicitly listed as a grammatical ending/form in விகுதி and finite-verb paradigms; ordinary lexical 'village/place' occurrences are kept separate.", [140,327,332]),
    "தொழில்": ("accepted", "semantics", "தொழில் is repeatedly used as grammatical action/function metalanguage in tense, அல்வழி, word-formation, nominal-semantic, and உரிச்சொல் classifications.", [142,152,256,275,393,453]),
    "இல": ("rejected", None, "இல functions as negative/existential or example lexical material in the reviewed rules; it is not established as the name of a grammatical category.", []),
    "மூன்றும்": ("rejected", None, "மூன்றும் is an inflected numeral surface used for counts and grouped examples, not independent terminology.", []),
    "எழுவாய்": ("accepted", "syntax", "எழுவாய் is explicitly used as the syntactic subject/nominative construction in case, non-compound construction, agreement, and பொருள்கோள் rules.", [152,294,295,374,381,415]),
    "உள": ("rejected", None, "உள is existential/example lexical material and a cited word form; the reviewed passages do not establish it as an independent grammatical term.", []),
    "பல": ("rejected", None, "பல is the ordinary 'many/plural' lexical/numeral form and example noun material; the grammatical category is expressed elsewhere by technical labels such as பன்மை.", []),
    "ஒன்றன்": ("rejected", None, "ஒன்றன் is a genitive/singular numeral surface used inside rules and examples, not an independent grammatical term identity.", []),
    "உருபும்": ("rejected", None, "உருபும் is the additive/conjunctive surface of the already accepted base உருபு; it does not require a separate term identity.", []),
    "புலவர்": ("rejected", None, "புலவர் denotes scholars/grammarians as people and attribution, not a grammatical concept.", []),
    "இன்றி": ("rejected", None, "இன்றி is ordinary negative/converb lexical material, including a cited வினையெச்சம் example; being an example form does not make it a term name.", []),
    "ஆகா": ("rejected", None, "ஆகா is a negative verbal/compositional surface used in rule statements rather than an independent grammatical term.", []),
    "வழியே": ("rejected", None, "வழியே is the emphatic/predicative surface of relational வழி ('by the rule/way'); it does not establish a separate technical identity.", []),
}


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    packet = json.loads(PACKET.read_text(encoding="utf-8"))
    if any(d.get("review_batch") == BATCH for d in ledger["decisions"]):
        raise SystemExit("Batch 007 already exists in ledger")
    candidates = packet["candidates"]
    if len(candidates) != 25 or set(CONFIG) != {c["surface_form_ta"] for c in candidates}:
        raise SystemExit("Batch 007 decision config does not match generated packet")

    rows = []
    for c in candidates:
        surface = c["surface_form_ta"]
        decision, category, rationale, term_numbers = CONFIG[surface]
        reviewed = c["record_ids_all"]
        num_to_id = {n: rid for n, rid in zip(c["numbers_all"], c["record_ids_all"])}
        term_use = [num_to_id[n] for n in term_numbers]
        non_term = [rid for rid in reviewed if rid not in term_use] if decision == "accepted" else list(reviewed)
        rows.append({
            "candidate_id": c["candidate_id"], "surface_form_ta": surface,
            "decision": decision, "term_category": category, "rationale": rationale,
            "reviewed_record_ids": reviewed, "term_use_record_ids": term_use,
            "non_term_use_record_ids": non_term, "external_evidence": [],
            "review_notes": None, "review_batch": BATCH, "review_basis": BASIS,
            **({"technical_scope": "mixed-context"} if decision == "accepted" and non_term else {})
        })

    ledger["decisions"].extend(rows)
    accepted = sum(d["decision"] == "accepted" for d in ledger["decisions"])
    rejected = sum(d["decision"] == "rejected" for d in ledger["decisions"])
    needs = sum(d["decision"] == "needs-context" for d in ledger["decisions"])
    reviewed = len(ledger["decisions"]); total = ledger["counts"]["candidate_surface_forms"]
    ledger["counts"] = {"candidate_surface_forms": total, "reviewed": reviewed, "accepted": accepted, "rejected": rejected, "needs_context": needs, "unreviewed": total-reviewed}
    ledger["layer_status"] = "review-complete" if reviewed == total else "review-in-progress"
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    lines = ["# Nannūl Grammatical Terminology Review — Batch 007 Decisions", "", f"- Reviewed: **{len(rows)}**", f"- Accepted: **{sum(r['decision']=='accepted' for r in rows)}**", f"- Rejected: **{sum(r['decision']=='rejected' for r in rows)}**", "- Needs context: **0**", ""]
    for r in rows:
        lines += [f"## `{r['surface_form_ta']}` — **{r['decision']}**", "", f"- Candidate: `{r['candidate_id']}`", f"- Category: `{r['term_category'] or '—'}`", "", r["rationale"], ""]
    SUMMARY.write_text("\n".join(lines)+"\n", encoding="utf-8")

if __name__ == "__main__":
    main()
