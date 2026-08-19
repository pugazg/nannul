#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 006 to the review ledger."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-006-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-006"
BASIS = "internal-canonical-contexts-frequency-only-tier"


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
    d("nannul-term-candidate-052c25b366fb4eae", "மூன்று", "rejected", None,
      "மூன்று is the ordinary numeral 'three' throughout enumerations, counts, and rule conditions. Frequency inside grammar does not create an independent technical-term identity.",
      ["nannul-0005", "nannul-0061", "nannul-0099", "nannul-0179", "nannul-0188", "nannul-0324", "nannul-0395"],
      non_term=["nannul-0005", "nannul-0061", "nannul-0099", "nannul-0179", "nannul-0188", "nannul-0324", "nannul-0395"]),
    d("nannul-term-candidate-a8ed19c744f51189", "வேறு", "rejected", None,
      "வேறு functions relationally as 'different/separate/other' or as lexical material in the reviewed rules. It is not independently defined or classified as grammatical terminology.",
      ["nannul-0008", "nannul-0139", "nannul-0316", "nannul-0330", "nannul-0339", "nannul-0389", "nannul-0414"],
      non_term=["nannul-0008", "nannul-0139", "nannul-0316", "nannul-0330", "nannul-0339", "nannul-0389", "nannul-0414"]),
    d("nannul-term-candidate-509871dd2710d320", "இயல்", "rejected", None,
      "The exact surface இயல் is used compositionally for nature, functioning, convention, or manner in the reviewed passages. Although இயல் occurs inside grammatical expressions, these contexts do not establish this exact surface as a separate technical term or section-name identity.",
      ["nannul-0020", "nannul-0129", "nannul-0267", "nannul-0383", "nannul-0391", "nannul-0403", "nannul-0420"],
      non_term=["nannul-0020", "nannul-0129", "nannul-0267", "nannul-0383", "nannul-0391", "nannul-0403", "nannul-0420"],
      notes="This does not affect source-supported compound/section labels containing இயல் or later review of other exact surfaces."),
    d("nannul-term-candidate-f768eb5fbe483462", "தன்மை", "accepted", "other-grammar",
      "Nannūl explicitly groups தன்மை, முன்னிலை, and படர்க்கை as three grammatical person/deictic positions and assigns pronouns and verbal endings to தன்மை. The ordinary 'nature/quality' sense in the prefatory passage is kept separate.",
      ["nannul-0049", "nannul-0266", "nannul-0282", "nannul-0285", "nannul-0324", "nannul-0330", "nannul-0331"],
      ["nannul-0266", "nannul-0282", "nannul-0285", "nannul-0324", "nannul-0330", "nannul-0331"],
      ["nannul-0049"], scope="mixed-context"),
    d("nannul-term-candidate-fa7220e14e13848a", "தான்", "rejected", None,
      "தான் is a pronoun/lexical form that Nannūl classifies and subjects to grammatical rules; elsewhere it is ordinary reflexive/emphatic language. The exact form is therefore example-language rather than the name of a grammatical concept.",
      ["nannul-0052", "nannul-0247", "nannul-0282", "nannul-0287", "nannul-0303", "nannul-0314", "nannul-0441"],
      non_term=["nannul-0052", "nannul-0247", "nannul-0282", "nannul-0287", "nannul-0303", "nannul-0314", "nannul-0441"]),
    d("nannul-term-candidate-c4a099c2dece5513", "எழுத்து", "accepted", "orthography",
      "எழுத்து is a foundational grammatical unit explicitly defined and repeatedly used for letters, letter counts, word length, shared letters, and phonological/orthographic behavior.",
      ["nannul-0058", "nannul-0074", "nannul-0129", "nannul-0130", "nannul-0146", "nannul-0158", "nannul-0391"],
      ["nannul-0058", "nannul-0074", "nannul-0129", "nannul-0130", "nannul-0146", "nannul-0158", "nannul-0391"], scope="broad-grammatical"),
    d("nannul-term-candidate-fe9756bfc7336c88", "உளவே", "rejected", None,
      "உளவே is an existential/predicative form meaning roughly 'there are / do exist'. It closes grammatical assertions but does not name a grammatical category or technical concept.",
      ["nannul-0122", "nannul-0185", "nannul-0202", "nannul-0341", "nannul-0351", "nannul-0380", "nannul-0408"],
      non_term=["nannul-0122", "nannul-0185", "nannul-0202", "nannul-0341", "nannul-0351", "nannul-0380", "nannul-0408"]),
    d("nannul-term-candidate-b9f7b36d07efa027", "து", "accepted", "morphology",
      "து is explicitly listed among verbal endings and is used in nominal/pronominal and finite-verb paradigms. Some passages cite the same surface as lexical/example material, so acceptance is bounded to the grammatical-form contexts.",
      ["nannul-0129", "nannul-0140", "nannul-0158", "nannul-0279", "nannul-0314", "nannul-0328", "nannul-0331"],
      ["nannul-0140", "nannul-0279", "nannul-0314", "nannul-0328", "nannul-0331"],
      ["nannul-0129", "nannul-0158"], scope="mixed-context"),
    d("nannul-term-candidate-e5cf084bae0c4aab", "ஆன்", "accepted", "morphology",
      "ஆன் has several explicit grammatical uses: verbal ending, சாரியை, third-case marker, and masculine படர்க்கை ending. Nannūl directly enumerates each of these uses.",
      ["nannul-0140", "nannul-0244", "nannul-0249", "nannul-0297", "nannul-0318", "nannul-0325"],
      ["nannul-0140", "nannul-0244", "nannul-0249", "nannul-0297", "nannul-0318", "nannul-0325"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-1a7d01c05036ff8c", "இடத்து", "rejected", None,
      "இடத்து is an inflected locative surface built on இடம் and used compositionally in grammatical prose. The independently reviewed base இடம் carries the grammatical concept; this exact inflected form does not require a separate term identity.",
      ["nannul-0142", "nannul-0144", "nannul-0255", "nannul-0265", "nannul-0275", "nannul-0353", "nannul-0420"],
      non_term=["nannul-0142", "nannul-0144", "nannul-0255", "nannul-0265", "nannul-0275", "nannul-0353", "nannul-0420"]),
    d("nannul-term-candidate-d6820636711d0ab1", "இடத்தும்", "rejected", None,
      "இடத்தும் is the locative/additive inflected surface of இடம் and functions compositionally as 'in the place(s)/positions too'. It is not a separate technical term.",
      ["nannul-0154", "nannul-0229", "nannul-0230", "nannul-0259", "nannul-0324", "nannul-0370", "nannul-0416"],
      non_term=["nannul-0154", "nannul-0229", "nannul-0230", "nannul-0259", "nannul-0324", "nannul-0370", "nannul-0416"]),
    d("nannul-term-candidate-303d4ab9b05f2188", "ஆகலும்", "rejected", None,
      "ஆகலும் is compositional verbal rule-language ('becoming/occurring also') used to state permitted transformations. It does not independently name the transformations themselves.",
      ["nannul-0170", "nannul-0233", "nannul-0341", "nannul-0351", "nannul-0353"],
      non_term=["nannul-0170", "nannul-0233", "nannul-0341", "nannul-0351", "nannul-0353"]),
    d("nannul-term-candidate-22132f51d7a3a31f", "இறு", "accepted", "morphology",
      "இறு functions systematically as grammatical positional metalanguage meaning 'ending in / having as final', governing word-final letters and forms across punarcci, case, nominal, and verbal rules.",
      ["nannul-0207", "nannul-0230", "nannul-0256", "nannul-0280", "nannul-0306", "nannul-0326"],
      ["nannul-0207", "nannul-0230", "nannul-0256", "nannul-0280", "nannul-0306", "nannul-0326"], scope="broad-grammatical"),
    d("nannul-term-candidate-8334c92da63cf56c", "அம்", "accepted", "morphology",
      "அம் is explicitly listed among verbal endings and சாரியை forms and appears in inflectional/punarcci rules. Two prefatory occurrences use the same surface adjectivally, so technical and ordinary uses are separated.",
      ["nannul-0004", "nannul-0041", "nannul-0140", "nannul-0202", "nannul-0244", "nannul-0332"],
      ["nannul-0140", "nannul-0202", "nannul-0244", "nannul-0332"],
      ["nannul-0004", "nannul-0041"], scope="mixed-context"),
    d("nannul-term-candidate-87d04524e56dbe6e", "நான்கு", "rejected", None,
      "நான்கு is the ordinary numeral 'four' in counts, enumerations, and repetition limits. The surrounding grammar does not make the numeral itself a technical term.",
      ["nannul-0004", "nannul-0247", "nannul-0319", "nannul-0368", "nannul-0370", "nannul-0395"],
      non_term=["nannul-0004", "nannul-0247", "nannul-0319", "nannul-0368", "nannul-0370", "nannul-0395"]),
    d("nannul-term-candidate-af7efddab539ec53", "இல்", "accepted", "case",
      "இல் has explicit grammatical-form uses, most clearly as a locative இடப்பொருள் case marker and also as an absence/negative word discussed by the grammar. Other occurrences use the same surface compositionally as ordinary negation, so acceptance is context-bounded.",
      ["nannul-0009", "nannul-0036", "nannul-0233", "nannul-0295", "nannul-0302", "nannul-0406"],
      ["nannul-0233", "nannul-0302", "nannul-0406"],
      ["nannul-0009", "nannul-0036", "nannul-0295"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-e7beb50714a3d8f2", "ஆதல்", "rejected", None,
      "ஆதல் is a verbal-noun/compositional expression of becoming or being used to describe grammatical transformations. The transformations are technical; the exact verbal noun is not an independent term.",
      ["nannul-0013", "nannul-0136", "nannul-0308", "nannul-0309"],
      non_term=["nannul-0013", "nannul-0136", "nannul-0308", "nannul-0309"]),
    d("nannul-term-candidate-9f399f23fe5b3586", "ஏற்புழி", "accepted", "meta-grammar",
      "ஏற்புழி is recurrent metagrammatical rule-application language: Nannūl explicitly tells the reader to identify the appropriate context and repeatedly conditions phonological, tense, syntactic, and பொருள்கோள் operations on that context.",
      ["nannul-0015", "nannul-0188", "nannul-0384", "nannul-0394", "nannul-0418", "nannul-0419"],
      ["nannul-0015", "nannul-0188", "nannul-0384", "nannul-0394", "nannul-0418", "nannul-0419"], scope="rule-application-condition"),
    d("nannul-term-candidate-ce45f9ba23bbd5d0", "ஐயம்", "accepted", "semantics",
      "ஐயம் is explicitly grammaticalized as uncertainty/doubt: it is listed among semantic functions of இடைச்சொல்/உம்மை and used in a rule governing uncertain திணை/பால் reference. Ordinary pedagogical 'doubt' uses are kept separate.",
      ["nannul-0023", "nannul-0029", "nannul-0376", "nannul-0421", "nannul-0425", "nannul-0435"],
      ["nannul-0376", "nannul-0421", "nannul-0425", "nannul-0435"],
      ["nannul-0023", "nannul-0029"], scope="mixed-context"),
    d("nannul-term-candidate-1ebf89cacccb3817", "வன்மை", "accepted", "phonology-letter-class",
      "வன்மை is used technically for strong/hard consonantal behavior in articulation and punarcci rules. The teacher-description occurrence means ordinary strength/command and is recorded separately.",
      ["nannul-0026", "nannul-0075", "nannul-0159", "nannul-0226", "nannul-0233"],
      ["nannul-0075", "nannul-0159", "nannul-0226", "nannul-0233"],
      ["nannul-0026"], scope="mixed-context"),
    d("nannul-term-candidate-a160bc93a792e076", "ஆகி", "rejected", None,
      "ஆகி is a participial/compositional form meaning 'becoming/as' used to link definitions and descriptions. It does not independently name a grammatical category.",
      ["nannul-0030", "nannul-0128", "nannul-0131", "nannul-0148", "nannul-0322", "nannul-0442"],
      non_term=["nannul-0030", "nannul-0128", "nannul-0131", "nannul-0148", "nannul-0322", "nannul-0442"]),
    d("nannul-term-candidate-e02d4ecbfbaf85c6", "காரணம்", "accepted", "semantics",
      "காரணம் is used as a technical causal relation in grammatical explanation and name formation, and Nannūl explicitly contrasts cause and resulting action in a semantic rule. It also appears among prefatory explanatory conditions.",
      ["nannul-0048", "nannul-0058", "nannul-0275", "nannul-0405"],
      ["nannul-0048", "nannul-0058", "nannul-0275", "nannul-0405"], scope="broad-grammatical"),
    d("nannul-term-candidate-fae8dd868f675e67", "முறை", "accepted", "meta-grammar",
      "முறை is explicitly enumerated among the domains treated in எழுத்து இயல் and repeatedly denotes grammatical order/sequence or rule ordering, including case-name order and bounded repetition order.",
      ["nannul-0057", "nannul-0079", "nannul-0282", "nannul-0292", "nannul-0298", "nannul-0395"],
      ["nannul-0057", "nannul-0079", "nannul-0282", "nannul-0292", "nannul-0298", "nannul-0395"], scope="grammatical-order-method"),
    d("nannul-term-candidate-5a8c7f4399e07d49", "உயிரும்", "rejected", None,
      "உயிரும் is the additive/conjunctive surface of the already accepted base term உயிர். The passages use the technical base with உம்; they do not establish a distinct term identity for உயிரும்.",
      ["nannul-0059", "nannul-0102", "nannul-0163", "nannul-0188", "nannul-0256", "nannul-0341"],
      non_term=["nannul-0059", "nannul-0102", "nannul-0163", "nannul-0188", "nannul-0256", "nannul-0341"],
      notes="Rejection concerns independent exact-form identity only; the base term உயிர் remains accepted."),
    d("nannul-term-candidate-2e91ead4c74e3103", "எட்டு", "rejected", None,
      "எட்டு is the ordinary numeral 'eight' in letter counts, grammatical enumerations, and semantic inventories. It is not an independent grammatical term.",
      ["nannul-0061", "nannul-0110", "nannul-0188", "nannul-0249", "nannul-0423", "nannul-0454"],
      non_term=["nannul-0061", "nannul-0110", "nannul-0188", "nannul-0249", "nannul-0423", "nannul-0454"]),
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    existing = {row["candidate_id"] for row in ledger["decisions"]}
    if any(row.get("review_batch") == BATCH for row in ledger["decisions"]):
        raise SystemExit("Batch 006 already exists in ledger")
    collisions = [row["candidate_id"] for row in DECISIONS if row["candidate_id"] in existing]
    if collisions:
        raise SystemExit(f"Already-reviewed candidate IDs in Batch 006: {collisions}")
    if len(DECISIONS) != 25:
        raise SystemExit(f"Expected 25 Batch-006 decisions, got {len(DECISIONS)}")

    ledger["decisions"].extend(DECISIONS)
    accepted = sum(1 for r in ledger["decisions"] if r["decision"] == "accepted")
    rejected = sum(1 for r in ledger["decisions"] if r["decision"] == "rejected")
    needs = sum(1 for r in ledger["decisions"] if r["decision"] == "needs-context")
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

    lines = [
        "# Nannūl Grammatical Terminology Review — Batch 006 Decisions", "",
        "Human/contextual review under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.", "",
        f"- Reviewed: **{len(DECISIONS)}**",
        f"- Accepted: **{sum(1 for r in DECISIONS if r['decision'] == 'accepted')}**",
        f"- Rejected: **{sum(1 for r in DECISIONS if r['decision'] == 'rejected')}**",
        f"- Needs context: **{sum(1 for r in DECISIONS if r['decision'] == 'needs-context')}**", "",
    ]
    for r in DECISIONS:
        lines += [f"## `{r['surface_form_ta']}` — **{r['decision']}**", "",
                  f"- Candidate: `{r['candidate_id']}`",
                  f"- Category: `{r['term_category'] or '—'}`",
                  f"- Reviewed evidence: {', '.join('`'+x+'`' for x in r['reviewed_record_ids'])}", "",
                  r["rationale"], ""]
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
