#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 003.

Batch 003 contains the 25 highest-priority unreviewed frequency-only candidates.
Frequency and breadth determine review order only; decisions are based on internal
canonical contexts in reviews/terminology/batch-003-*.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-003-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-003"
BASIS = "internal-canonical-contexts-frequency-only-candidate-review"


def d(candidate_id, surface, decision, category, rationale, reviewed, term_use=None,
      non_term=None, notes=None, scope=None):
    row = {
        "candidate_id": candidate_id,
        "surface_form_ta": surface,
        "decision": decision,
        "term_category": category,
        "rationale": rationale,
        "reviewed_record_ids": reviewed,
        "term_use_record_ids": term_use or [],
        "non_term_use_record_ids": non_term or [],
        "external_evidence": [],
        "review_notes": notes,
        "review_batch": BATCH,
        "review_basis": BASIS,
    }
    if scope:
        row["technical_scope"] = scope
    return row


DECISIONS = [
    d("nannul-term-candidate-96dec81cd2555769", "ஆகும்", "rejected", None,
      "Across widely distributed contexts, ஆகும் is the ordinary copular/resultative verbal form used to state that something becomes, is, or counts as something. Its high frequency reflects rule-statement syntax, not independent grammatical termhood.",
      ["nannul-0004","nannul-0060","nannul-0134","nannul-0154","nannul-0243","nannul-0457"],
      non_term=["nannul-0004","nannul-0060","nannul-0134","nannul-0154","nannul-0243","nannul-0457"],
      notes="A technical rule may contain ஆகும் without making the copular form itself a terminology entry."),

    d("nannul-term-candidate-3afd94c8607bb591", "ஐ", "accepted", "phonology-letter-class",
      "ஐ is explicitly used as a Tamil vowel/letter symbol in எழுத்து இயல் and also as the accusative/case-marker form in உருபு and வேற்றுமை descriptions. The same surface also occurs as the numeral five, so acceptance is context-bounded.",
      ["nannul-0004","nannul-0060","nannul-0136","nannul-0203","nannul-0244","nannul-0255","nannul-0292","nannul-0449"],
      term_use=["nannul-0060","nannul-0136","nannul-0203","nannul-0244","nannul-0255","nannul-0292"],
      non_term=["nannul-0004","nannul-0449"],
      notes="Primary analytical category is the letter/vowel class; the ledger also preserves its distinct case-marker use.", scope="mixed-context-multiple-grammatical-senses"),

    d("nannul-term-candidate-655f5ff75649a436", "முதல்", "accepted", "meta-grammar",
      "Nannūl uses முதல் as grammatical metalanguage for initial/first position and in internal classifications such as முதல்–ஈறு–இடைநிலை and முதல்/ஈறு environments. It also has ordinary enumerative or relational uses, so the decision is context-bounded.",
      ["nannul-0005","nannul-0057","nannul-0151","nannul-0242","nannul-0316","nannul-0450"],
      term_use=["nannul-0005","nannul-0057","nannul-0151","nannul-0242","nannul-0316"],
      non_term=["nannul-0450"], scope="mixed-context"),

    d("nannul-term-candidate-0fe2f89a337b6903", "ஈர்", "accepted", "morphology",
      "Although ஈர் frequently functions as the numeral 'two', Nannūl also explicitly lists and describes ஈர் as a verbal ending/viguti, including the second-person plural paradigm. Those internal morphological uses justify context-bounded acceptance.",
      ["nannul-0012","nannul-0138","nannul-0140","nannul-0337","nannul-0446"],
      term_use=["nannul-0138","nannul-0140","nannul-0337"],
      non_term=["nannul-0012","nannul-0446"], scope="mixed-context"),

    d("nannul-term-candidate-9c7a8cc60c35994a", "என", "accepted", "particle",
      "என is used productively as a quotative/classifying particle throughout Nannūl and is explicitly treated within இடையியல், including the particle descriptions around நூற்பாக்கள் 424 and 428. Frequency is not the basis of acceptance; internal grammatical treatment is.",
      ["nannul-0002","nannul-0040","nannul-0070","nannul-0152","nannul-0424","nannul-0428"],
      term_use=["nannul-0002","nannul-0040","nannul-0070","nannul-0152","nannul-0424","nannul-0428"],
      scope="broad-grammatical"),

    d("nannul-term-candidate-b743a7797bfde38d", "என்", "accepted", "morphology",
      "என் has several uses, but Nannūl explicitly lists it among விகுதி and first-person verbal ending forms. It also occurs as possessive/quotative lexical material, so only the documented morphological contexts are treated as technical for this category.",
      ["nannul-0137","nannul-0140","nannul-0247","nannul-0331","nannul-0350","nannul-0439"],
      term_use=["nannul-0140","nannul-0331"],
      non_term=["nannul-0137","nannul-0247","nannul-0439"],
      notes="Other grammatical uses such as interrogative/quotative constructions are retained as reviewed context without forcing them into the morphology category.", scope="mixed-context"),

    d("nannul-term-candidate-1b5239a2e456ad8e", "ஈறு", "accepted", "morphology",
      "ஈறு is repeatedly used as explicit grammatical metalanguage for the final/ending position of letters, words, forms, and inflectional material, including the source topic inventory at நூற்பா 57 and numerous ending rules.",
      ["nannul-0057","nannul-0130","nannul-0151","nannul-0218","nannul-0307","nannul-0419"],
      term_use=["nannul-0057","nannul-0130","nannul-0151","nannul-0218","nannul-0307","nannul-0419"], scope="broad-grammatical"),

    d("nannul-term-candidate-269a43a35172207d", "இரு", "rejected", None,
      "The reviewed occurrences use இரு primarily as the numeral 'two', as part of ordinary counting/classification syntax, or as the lexical imperative 'be'. No independent technical term identity is established for this exact surface form.",
      ["nannul-0002","nannul-0040","nannul-0058","nannul-0128","nannul-0151","nannul-0454"],
      non_term=["nannul-0002","nannul-0040","nannul-0058","nannul-0128","nannul-0151","nannul-0454"]),

    d("nannul-term-candidate-2b55983c33fdc725", "என்ப", "rejected", None,
      "என்ப functions as an ordinary reportative/attributive verbal expression ('they say/call') that closes or supports definitions. Its recurrence is a stylistic feature of grammatical exposition rather than a standalone grammatical technical term.",
      ["nannul-0036","nannul-0050","nannul-0128","nannul-0198","nannul-0301","nannul-0391"],
      non_term=["nannul-0036","nannul-0050","nannul-0128","nannul-0198","nannul-0301","nannul-0391"]),

    d("nannul-term-candidate-aa9456d7a26a0ca2", "ஆம்", "accepted", "morphology",
      "ஆம் has ordinary copular/ordinal uses, but Nannūl also explicitly lists it among verbal endings/viguti and in the தன்மைப் பன்மை paradigm. It additionally appears in the இடையியல் asai-word inventory. These internal grammatical-form uses justify context-bounded acceptance.",
      ["nannul-0058","nannul-0140","nannul-0151","nannul-0249","nannul-0332","nannul-0441"],
      term_use=["nannul-0140","nannul-0332","nannul-0441"],
      non_term=["nannul-0058","nannul-0151","nannul-0249"], scope="mixed-context-multiple-grammatical-senses"),

    d("nannul-term-candidate-6e7752307962125a", "ஈற்று", "accepted", "morphology",
      "The bound exact form ஈற்று is used consistently in technical descriptions of final/ending position across letter, word, case, and verbal contexts. It is retained independently from ஈறு because the exact surface itself is pervasive grammatical metalanguage.",
      ["nannul-0097","nannul-0158","nannul-0202","nannul-0242","nannul-0304","nannul-0341"],
      term_use=["nannul-0097","nannul-0158","nannul-0202","nannul-0242","nannul-0304","nannul-0341"],
      notes="Accepted as a technical bound/attributive surface, not silently merged with ஈறு.", scope="technical-bound-form"),

    d("nannul-term-candidate-afec51864a333430", "இயல்பும்", "rejected", None,
      "The exact surface இயல்பும் is compositional இயல்பு plus the additive/conjunctive உம். Even where இயல்பு is technical, the clitic-bearing surface does not require a separate terminology identity; the base form can be reviewed independently.",
      ["nannul-0031","nannul-0158","nannul-0209","nannul-0255","nannul-0267","nannul-0313"],
      non_term=["nannul-0031","nannul-0158","nannul-0209","nannul-0255","nannul-0267","nannul-0313"],
      notes="Rejection concerns independent exact-form termhood, not whether இயல்பு itself is grammatical metalanguage."),

    d("nannul-term-candidate-2a5d9cc8cf620f64", "இடை", "accepted", "other-grammar",
      "இடை functions as grammatical shorthand for medial/intermediate position and, in several சொல்லதிகாரம் contexts, for the இடைச்சொல் class alongside உரி. It also has ordinary 'middle/between' uses, so acceptance is explicitly mixed-context.",
      ["nannul-0038","nannul-0092","nannul-0123","nannul-0141","nannul-0152","nannul-0239","nannul-0270","nannul-0374","nannul-0419"],
      term_use=["nannul-0092","nannul-0123","nannul-0141","nannul-0152","nannul-0239","nannul-0270","nannul-0374","nannul-0419"],
      non_term=["nannul-0038"],
      notes="The broad category other-grammar avoids collapsing its positional and word-class shorthand senses.", scope="mixed-context-multiple-grammatical-senses"),

    d("nannul-term-candidate-505e0e7bb5ea070b", "ஆறு", "rejected", None,
      "The reviewed occurrences use ஆறு overwhelmingly as the numeral six, with one ordinary 'way/manner' sense. Technical grammatical inventories being counted to six do not make the numeral itself a terminology entry.",
      ["nannul-0024","nannul-0061","nannul-0152","nannul-0343","nannul-0362","nannul-0422"],
      non_term=["nannul-0024","nannul-0061","nannul-0152","nannul-0343","nannul-0362","nannul-0422"]),

    d("nannul-term-candidate-ed094b09da798b5e", "பொருள்", "accepted", "semantics",
      "பொருள் is repeatedly used as grammatical/semantic metalanguage for meaning, referent, denotation, or the semantic content of a rule/expression, including word, case, and பொருள்கோள் discussions. The same form also has broader ordinary/philosophical senses.",
      ["nannul-0010","nannul-0022","nannul-0023","nannul-0036","nannul-0072","nannul-0132","nannul-0291","nannul-0346","nannul-0415","nannul-0443"],
      term_use=["nannul-0022","nannul-0023","nannul-0036","nannul-0072","nannul-0132","nannul-0291","nannul-0346","nannul-0415"],
      non_term=["nannul-0010","nannul-0443"], scope="mixed-context"),

    d("nannul-term-candidate-b4b2c40524b4ca04", "என்று", "accepted", "particle",
      "என்று is a quotative/classifying particle used throughout Nannūl and is explicitly present in the இடையியல் enumeration/particle discussion. Its grammatical function is internally supported even when it also serves ordinary reported-speech syntax.",
      ["nannul-0021","nannul-0041","nannul-0137","nannul-0257","nannul-0292","nannul-0428","nannul-0438","nannul-0460"],
      term_use=["nannul-0021","nannul-0041","nannul-0137","nannul-0257","nannul-0292","nannul-0428","nannul-0438","nannul-0460"], scope="broad-grammatical"),

    d("nannul-term-candidate-6791ec4383666049", "ஒற்று", "accepted", "phonology-letter-class",
      "ஒற்று is used systematically as technical phonological/orthographic metalanguage for consonantal/pulli-letter material and consonant position, including அளவு, doubling, deletion, and புணர்ச்சி rules.",
      ["nannul-0089","nannul-0099","nannul-0136","nannul-0142","nannul-0182","nannul-0205","nannul-0219","nannul-0371"],
      term_use=["nannul-0089","nannul-0099","nannul-0136","nannul-0142","nannul-0182","nannul-0205","nannul-0219","nannul-0371"], scope="broad-grammatical"),

    d("nannul-term-candidate-814fb946c7eb282d", "இயல்பே", "rejected", None,
      "The exact surface இயல்பே is a predicative/emphatic inflection of இயல்பு used to state that a form or rule is natural/regular. The technical concept may reside in இயல்பு, but the inflected exact surface does not warrant a separate term identity.",
      ["nannul-0004","nannul-0036","nannul-0047","nannul-0136","nannul-0153","nannul-0204","nannul-0379"],
      non_term=["nannul-0004","nannul-0036","nannul-0047","nannul-0136","nannul-0153","nannul-0204","nannul-0379"],
      notes="Rejection is about exact-form indexing only; the base form இயல்பு remains eligible for separate review."),

    d("nannul-term-candidate-958162d89e6f85f4", "ஒன்று", "rejected", None,
      "ஒன்று functions as the numeral/quantifier 'one' or an ordinary indefinite/unity expression across the reviewed contexts. Its use in grammatical enumerations does not establish independent technical termhood.",
      ["nannul-0061","nannul-0147","nannul-0188","nannul-0240","nannul-0269","nannul-0451"],
      non_term=["nannul-0061","nannul-0147","nannul-0188","nannul-0240","nannul-0269","nannul-0451"]),

    d("nannul-term-candidate-e863501be23aa0f1", "ஆ", "accepted", "phonology-letter-class",
      "ஆ is explicitly used as the long Tamil vowel/letter and in letter-initial/final rules. It also appears as a grammatical ending and interrogative/other form, so the phonological category is the primary analytical anchor rather than a claim of uniform sense.",
      ["nannul-0065","nannul-0076","nannul-0105","nannul-0140","nannul-0171","nannul-0304","nannul-0329","nannul-0353"],
      term_use=["nannul-0065","nannul-0076","nannul-0105","nannul-0140","nannul-0171","nannul-0304","nannul-0329","nannul-0353"],
      notes="Multiple grammatical uses are retained; primary category is phonology-letter-class.", scope="mixed-context-multiple-grammatical-senses"),

    d("nannul-term-candidate-71a55ac783462656", "ன", "accepted", "phonology-letter-class",
      "ன is repeatedly used as an exact Tamil consonant/letter symbol in letter classification, final-position, alternation, புணர்ச்சி, and case-related environments.",
      ["nannul-0069","nannul-0092","nannul-0107","nannul-0150","nannul-0198","nannul-0207","nannul-0227","nannul-0304"],
      term_use=["nannul-0069","nannul-0092","nannul-0107","nannul-0150","nannul-0198","nannul-0207","nannul-0227","nannul-0304"], scope="broad-grammatical"),

    d("nannul-term-candidate-3efce37a78b036a3", "ள", "accepted", "phonology-letter-class",
      "ள is repeatedly used as an exact Tamil consonant/letter symbol in classification, final-position, phonological alternation, and case/poetic environments.",
      ["nannul-0070","nannul-0092","nannul-0107","nannul-0158","nannul-0207","nannul-0227","nannul-0304","nannul-0312"],
      term_use=["nannul-0070","nannul-0092","nannul-0107","nannul-0158","nannul-0207","nannul-0227","nannul-0304","nannul-0312"], scope="broad-grammatical"),

    d("nannul-term-candidate-fdda3eb04f5332f9", "உயிர்மெய்", "accepted", "phonology-letter-class",
      "உயிர்மெய் is explicit Tamil grammatical metalanguage for the consonant-vowel composite letter class and is used consistently in letter counts, formation, initial/final position, deletion, and புணர்ச்சி rules.",
      ["nannul-0060","nannul-0061","nannul-0089","nannul-0109","nannul-0168","nannul-0197","nannul-0341"],
      term_use=["nannul-0060","nannul-0061","nannul-0089","nannul-0109","nannul-0168","nannul-0197","nannul-0341"], scope="broad-grammatical"),

    d("nannul-term-candidate-5c5c1736243095b1", "ஆய்தம்", "accepted", "phonology-letter-class",
      "ஆய்தம் is explicitly treated as a Tamil letter/sound category, counted among சார்பெழுத்து and described in articulation, அளவு, புணர்ச்சி, and deletion rules.",
      ["nannul-0060","nannul-0061","nannul-0092","nannul-0099","nannul-0195","nannul-0251"],
      term_use=["nannul-0060","nannul-0061","nannul-0092","nannul-0099","nannul-0195","nannul-0251"], scope="broad-grammatical"),

    d("nannul-term-candidate-f425cda05c3657a7", "இ", "accepted", "phonology-letter-class",
      "இ is explicitly used as the Tamil short i-vowel/letter in letter classification, articulation, அளவு, and phonological rules. It also occurs as a verbal ending and demonstrative-related form, so acceptance is not a claim of one uniform grammatical sense.",
      ["nannul-0060","nannul-0064","nannul-0066","nannul-0077","nannul-0099","nannul-0140","nannul-0162","nannul-0304"],
      term_use=["nannul-0060","nannul-0064","nannul-0066","nannul-0077","nannul-0099","nannul-0140","nannul-0162","nannul-0304"],
      notes="Primary category is the vowel/letter class; other grammatical uses remain contextually distinct.", scope="mixed-context-multiple-grammatical-senses"),
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    existing = {row["candidate_id"] for row in ledger["decisions"]}
    if any(row.get("review_batch") == BATCH for row in ledger["decisions"]):
        raise SystemExit("Batch 003 already exists in ledger")
    collisions = [row["candidate_id"] for row in DECISIONS if row["candidate_id"] in existing]
    if collisions:
        raise SystemExit(f"Already-reviewed candidate IDs in Batch 003: {collisions}")
    if len(DECISIONS) != 25:
        raise SystemExit(f"Expected 25 Batch-003 decisions, got {len(DECISIONS)}")

    ledger["decisions"].extend(DECISIONS)
    accepted = sum(1 for row in ledger["decisions"] if row["decision"] == "accepted")
    rejected = sum(1 for row in ledger["decisions"] if row["decision"] == "rejected")
    needs = sum(1 for row in ledger["decisions"] if row["decision"] == "needs-context")
    reviewed = len(ledger["decisions"])
    total = ledger["counts"]["candidate_surface_forms"]
    ledger["counts"] = {
        "candidate_surface_forms": total,
        "reviewed": reviewed,
        "accepted": accepted,
        "rejected": rejected,
        "needs_context": needs,
        "unreviewed": total - reviewed,
    }
    ledger["layer_status"] = "review-complete" if reviewed == total else "review-in-progress"
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    batch_rows = [row for row in ledger["decisions"] if row.get("review_batch") == BATCH]
    lines = [
        "# Nannūl Grammatical Terminology Review — Batch 003 Decisions",
        "",
        "Human/contextual review of the 25 highest-priority frequency-only candidates.",
        "",
        f"- Reviewed: **{len(batch_rows)}**",
        f"- Accepted: **{sum(1 for r in batch_rows if r['decision'] == 'accepted')}**",
        f"- Rejected: **{sum(1 for r in batch_rows if r['decision'] == 'rejected')}**",
        f"- Needs context: **{sum(1 for r in batch_rows if r['decision'] == 'needs-context')}**",
        "",
        "| Exact form | Decision | Category |",
        "|---|---|---|",
    ]
    for row in batch_rows:
        lines.append(f"| `{row['surface_form_ta']}` | **{row['decision']}** | `{row.get('term_category') or '—'}` |")
        lines += ["", f"**Rationale — `{row['surface_form_ta']}`:** {row['rationale']}"]
        if row.get("term_use_record_ids"):
            lines.append("Technical-use records: " + ", ".join(f"`{x}`" for x in row["term_use_record_ids"]) + ".")
        if row.get("non_term_use_record_ids"):
            lines.append("Known non-term-use records: " + ", ".join(f"`{x}`" for x in row["non_term_use_record_ids"]) + ".")
        if row.get("review_notes"):
            lines.append("Review note: " + row["review_notes"])
        lines.append("")
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": "PASS",
        "batch": BATCH,
        "batch_decisions": len(batch_rows),
        "batch_accepted": sum(1 for r in batch_rows if r["decision"] == "accepted"),
        "batch_rejected": sum(1 for r in batch_rows if r["decision"] == "rejected"),
        "ledger_counts": ledger["counts"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
