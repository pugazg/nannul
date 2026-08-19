#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 008 to the review ledger."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-008-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-008"
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
    d("nannul-term-candidate-db56d52541cff59a", "பொருளே", "rejected", None,
      "பொருளே is an emphatic/predicative surface built from the already reviewed grammatical base பொருள். The passages use it to close definitions ('the meaning is ...') rather than name a distinct grammatical category.",
      ["nannul-0047", "nannul-0298", "nannul-0299", "nannul-0300", "nannul-0450"],
      non_term=["nannul-0047", "nannul-0298", "nannul-0299", "nannul-0300", "nannul-0450"],
      notes="Rejection concerns independent exact-form termhood only; the base பொருள் remains accepted."),
    d("nannul-term-candidate-2be4e532280a168e", "நின்ற", "rejected", None,
      "நின்ற is a participial verbal form ('standing/remained/positioned') used compositionally inside rules and prefatory prose. It does not name a grammatical category.",
      ["nannul-0055", "nannul-0109", "nannul-0136", "nannul-0165", "nannul-0253"],
      non_term=["nannul-0055", "nannul-0109", "nannul-0136", "nannul-0165", "nannul-0253"]),
    d("nannul-term-candidate-a15cc2dde39cdc29", "அது", "accepted", "case",
      "The exact form அது is explicitly enumerated among the eight case forms in நூற்பா 292, establishing a technical case-marker use. Elsewhere the same surface is demonstrative/anaphoric prose, so acceptance is restricted to the case context.",
      ["nannul-0058", "nannul-0128", "nannul-0180", "nannul-0292", "nannul-0315"],
      ["nannul-0292"],
      ["nannul-0058", "nannul-0128", "nannul-0180", "nannul-0315"], scope="mixed-context"),
    d("nannul-term-candidate-9eceb41e91ce119e", "உயர்", "rejected", None,
      "உயர் functions as an adjectival/abbreviatory modifier ('high/higher') inside expressions such as உயர் பெயர் and high-class/person references. The reviewed corpus already carries the explicit category உயர்திணை; the bare modifier does not require an independent term identity.",
      ["nannul-0061", "nannul-0289", "nannul-0308", "nannul-0309", "nannul-0349"],
      non_term=["nannul-0061", "nannul-0289", "nannul-0308", "nannul-0309", "nannul-0349"],
      notes="Rejection does not affect the accepted term உயர்திணை."),
    d("nannul-term-candidate-e2ca8a58ed948407", "ஒன்றே", "rejected", None,
      "ஒன்றே is the numeral ஒன்று with emphatic/predicative ஏ. It counts or predicates singularity in grammatical inventories but does not name a distinct grammatical term.",
      ["nannul-0061", "nannul-0099", "nannul-0263", "nannul-0284", "nannul-0324"],
      non_term=["nannul-0061", "nannul-0099", "nannul-0263", "nannul-0284", "nannul-0324"]),
    d("nannul-term-candidate-a6b7d3b4f9e13596", "உற", "rejected", None,
      "உற is verbal rule-language ('touch/join/receive/occur') describing articulation, combination, or attachment. The operations described are technical, but the verb itself is not a category label.",
      ["nannul-0077", "nannul-0079", "nannul-0082", "nannul-0235", "nannul-0355"],
      non_term=["nannul-0077", "nannul-0079", "nannul-0082", "nannul-0235", "nannul-0355"]),
    d("nannul-term-candidate-a7a25d02f2b6d60a", "வருமே", "rejected", None,
      "வருமே is a finite/predicative verbal surface ('will/does come') used to state rule outcomes. It is compositional rule prose, not independent grammatical terminology.",
      ["nannul-0077", "nannul-0079", "nannul-0148", "nannul-0189", "nannul-0336"],
      non_term=["nannul-0077", "nannul-0079", "nannul-0148", "nannul-0189", "nannul-0336"]),
    d("nannul-term-candidate-25c84c02b2405027", "அவற்று", "rejected", None,
      "அவற்று is an inflected anaphoric/demonstrative form referring back to previously named items. It organizes grammatical prose but does not independently name a grammatical category.",
      ["nannul-0091", "nannul-0265", "nannul-0337", "nannul-0389"],
      non_term=["nannul-0091", "nannul-0265", "nannul-0337", "nannul-0389"]),
    d("nannul-term-candidate-f5e807545b8d9b02", "இயல்பு", "accepted", "meta-grammar",
      "இயல்பு is repeatedly used as technical rule metalanguage for the natural/default/unmodified outcome contrasted with விகாரம், மிகுதல், திரிபு, or special rule behavior. The ordinary 'natural' measure example at நூற்பா 100 is kept separate.",
      ["nannul-0100", "nannul-0177", "nannul-0209", "nannul-0303", "nannul-0323"],
      ["nannul-0177", "nannul-0209", "nannul-0303", "nannul-0323"],
      ["nannul-0100"], scope="mixed-context"),
    d("nannul-term-candidate-5bab471766d5b7a3", "பால்", "accepted", "noun",
      "பால் has explicit grammatical category use for gender/classification, especially in பெயரியல் and the list of grammatical concord/deviation dimensions. Broader 'type/class' uses in other structural statements are distinguished from this technical gender sense.",
      ["nannul-0110", "nannul-0128", "nannul-0281", "nannul-0375"],
      ["nannul-0281", "nannul-0375"],
      ["nannul-0110", "nannul-0128"], scope="mixed-context"),
    d("nannul-term-candidate-342bfaee41f9fcf0", "வவ்வும்", "rejected", None,
      "வவ்வும் is an additive/inflected surface used when the வ-letter/form participates in rules. The independent exact letter symbol வ is already accepted; this surface does not require a separate term identity.",
      ["nannul-0125", "nannul-0162", "nannul-0163", "nannul-0199", "nannul-0280"],
      non_term=["nannul-0125", "nannul-0162", "nannul-0163", "nannul-0199", "nannul-0280"],
      notes="Rejection does not affect the accepted exact letter term வ."),
    d("nannul-term-candidate-0036152a7825b6be", "ஒன்பதும்", "rejected", None,
      "ஒன்பதும் is the numeral ஒன்பது with additive/emphatic உம். It counts members or participates as a numeral in rules and does not name an independent grammatical category.",
      ["nannul-0130", "nannul-0197", "nannul-0199", "nannul-0249", "nannul-0360"],
      non_term=["nannul-0130", "nannul-0197", "nannul-0199", "nannul-0249", "nannul-0360"]),
    d("nannul-term-candidate-042079729c9a5c29", "குணம்", "accepted", "semantics",
      "குணம் is explicit grammatical/semantic metalanguage for quality/property: it participates in word derivation and naming classifications and is directly paired/defined with பண்பு in உரியியல்.",
      ["nannul-0132", "nannul-0276", "nannul-0393", "nannul-0443", "nannul-0453"],
      ["nannul-0132", "nannul-0276", "nannul-0393", "nannul-0443", "nannul-0453"], scope="broad-grammatical"),
    d("nannul-term-candidate-026d2745ef2fa5e8", "கு", "accepted", "morphology",
      "கு is explicitly enumerated as grammatical form material in விகுதி and சாரியை inventories, as a case form in the eight-case list, and in finite-verb morphology. Its exact-form identity is therefore directly supported across several morphological systems.",
      ["nannul-0140", "nannul-0244", "nannul-0292", "nannul-0318", "nannul-0331"],
      ["nannul-0140", "nannul-0244", "nannul-0292", "nannul-0318", "nannul-0331"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-bb743a6496b36449", "உம்", "accepted", "particle",
      "உம் is explicitly treated as grammatical form material: it appears in விகுதி/finite-verb inventories and as the additive/enumerative particle whose presence or absence affects constructions. The exact surface therefore has internally established grammatical-form identity.",
      ["nannul-0140", "nannul-0245", "nannul-0332", "nannul-0341", "nannul-0368"],
      ["nannul-0140", "nannul-0245", "nannul-0332", "nannul-0341", "nannul-0368"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-9ce8726ddf051576", "ஐம்பால்", "accepted", "noun",
      "ஐம்பால் is explicit grammatical metalanguage for the five gender/person-number classes. Nannūl repeatedly applies it to tense intermediates, word meaning, and finite-verbal distribution.",
      ["nannul-0142", "nannul-0143", "nannul-0144", "nannul-0259", "nannul-0339"],
      ["nannul-0142", "nannul-0143", "nannul-0144", "nannul-0259", "nannul-0339"], scope="broad-grammatical"),
    d("nannul-term-candidate-126a09361d989d16", "சில", "rejected", None,
      "சில is the ordinary quantifier/example word 'some/few'. Nannūl may subject the lexical form to rules or use it to qualify subsets, but it is not itself the name of a grammatical category.",
      ["nannul-0144", "nannul-0170", "nannul-0184", "nannul-0207", "nannul-0280"],
      non_term=["nannul-0144", "nannul-0170", "nannul-0184", "nannul-0207", "nannul-0280"]),
    d("nannul-term-candidate-9df9ac6baa7afaf7", "எதிர்மறை", "accepted", "semantics",
      "எதிர்மறை is explicitly grammaticalized as negative/oppositional meaning and constructional function. It is listed in verbal behavior, residual-expression classes, and இடைச்சொல் semantic inventories.",
      ["nannul-0145", "nannul-0360", "nannul-0421", "nannul-0423", "nannul-0425"],
      ["nannul-0145", "nannul-0360", "nannul-0421", "nannul-0423", "nannul-0425"], scope="broad-grammatical"),
    d("nannul-term-candidate-98933144f98dfc1b", "பொது", "accepted", "meta-grammar",
      "பொது functions as grammatical classificatory metalanguage for what is common/general across letters, words, persons/classes, and verbal behavior. In several passages it is predicative/category-bearing rather than merely incidental prose.",
      ["nannul-0146", "nannul-0260", "nannul-0274", "nannul-0285", "nannul-0323"],
      ["nannul-0146", "nannul-0260", "nannul-0274", "nannul-0285", "nannul-0323"], scope="broad-grammatical"),
    d("nannul-term-candidate-43a3fb0360037479", "அனைத்தும்", "rejected", None,
      "அனைத்தும் is the ordinary universal quantifier 'all/everything' used to scope grammatical statements. It does not name an independent technical category.",
      ["nannul-0153", "nannul-0177", "nannul-0265", "nannul-0450", "nannul-0461"],
      non_term=["nannul-0153", "nannul-0177", "nannul-0265", "nannul-0450", "nannul-0461"]),
    d("nannul-term-candidate-566314ad081edc4f", "இருமையும்", "rejected", None,
      "இருமையும் is a compositional 'both/both kinds' expression whose referent changes by rule. It is not a stable independent grammatical category label.",
      ["nannul-0162", "nannul-0260", "nannul-0264", "nannul-0319", "nannul-0405"],
      non_term=["nannul-0162", "nannul-0260", "nannul-0264", "nannul-0319", "nannul-0405"]),
    d("nannul-term-candidate-5f0ae1d04a06120b", "பன்மை", "accepted", "noun",
      "பன்மை is an explicit grammatical number category. Nannūl contrasts it with ஒருமை and applies it to nominal reference, agreement, person/deictic positions, and verbal endings.",
      ["nannul-0167", "nannul-0287", "nannul-0289", "nannul-0332", "nannul-0337"],
      ["nannul-0167", "nannul-0287", "nannul-0289", "nannul-0332", "nannul-0337"], scope="broad-grammatical"),
    d("nannul-term-candidate-69581fe956e9727e", "உருபின்", "rejected", None,
      "உருபின் is the genitive/oblique surface of the already accepted base term உருபு. It means 'of the form/case-marker' inside rules and does not establish a separate term identity.",
      ["nannul-0238", "nannul-0245", "nannul-0246", "nannul-0317", "nannul-0354"],
      non_term=["nannul-0238", "nannul-0245", "nannul-0246", "nannul-0317", "nannul-0354"],
      notes="Rejection concerns independent exact-form termhood only; the base உருபு remains accepted."),
    d("nannul-term-candidate-3b116b11f8dc5e98", "அல்வழி", "accepted", "other-grammar",
      "அல்வழி is a stable technical category repeatedly contrasted with வேற்றுமை in புணர்ச்சி. Nannūl uses it to define the non-case syntactic/sandhi environment and to condition phonological alternations across both உயிரீற்று and மெய்யீற்று rules.",
      ["nannul-0151", "nannul-0152", "nannul-0171", "nannul-0177", "nannul-0178", "nannul-0181", "nannul-0211", "nannul-0220", "nannul-0224", "nannul-0227", "nannul-0229", "nannul-0230", "nannul-0232"],
      ["nannul-0151", "nannul-0152", "nannul-0171", "nannul-0177", "nannul-0178", "nannul-0181", "nannul-0211", "nannul-0220", "nannul-0224", "nannul-0227", "nannul-0229", "nannul-0230", "nannul-0232"], scope="broad-grammatical"),
    d("nannul-term-candidate-0ee5530767e93806", "அயல்", "accepted", "morphology",
      "அயல் is repeatedly used as positional grammatical metalanguage for the adjacent/neighboring segment in vocative and related alternation rules. Its recurrence in structured transformation descriptions establishes a stable technical positional sense.",
      ["nannul-0303", "nannul-0307", "nannul-0308", "nannul-0309", "nannul-0310", "nannul-0311", "nannul-0312", "nannul-0353"],
      ["nannul-0303", "nannul-0307", "nannul-0308", "nannul-0309", "nannul-0310", "nannul-0311", "nannul-0312", "nannul-0353"], scope="broad-grammatical"),
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    existing = {row["candidate_id"] for row in ledger["decisions"]}
    if any(row.get("review_batch") == BATCH for row in ledger["decisions"]):
        raise SystemExit("Batch 008 already exists in ledger")
    collisions = [row["candidate_id"] for row in DECISIONS if row["candidate_id"] in existing]
    if collisions:
        raise SystemExit(f"Already-reviewed candidate IDs in Batch 008: {collisions}")
    if len(DECISIONS) != 25:
        raise SystemExit(f"Expected 25 Batch-008 decisions, got {len(DECISIONS)}")

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
        "# Nannūl Grammatical Terminology Review — Batch 008 Decisions",
        "",
        "Human/contextual review under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.",
        "",
        f"- Reviewed: **{len(DECISIONS)}**",
        f"- Accepted: **{sum(1 for r in DECISIONS if r['decision'] == 'accepted')}**",
        f"- Rejected: **{sum(1 for r in DECISIONS if r['decision'] == 'rejected')}**",
        f"- Needs context: **{sum(1 for r in DECISIONS if r['decision'] == 'needs-context')}**",
        "",
    ]
    for r in DECISIONS:
        lines += [
            f"## `{r['surface_form_ta']}` — **{r['decision']}**",
            "",
            f"- Candidate: `{r['candidate_id']}`",
            f"- Category: `{r['term_category'] or '—'}`",
            f"- Reviewed evidence: {', '.join('`'+x+'`' for x in r['reviewed_record_ids'])}",
            "",
            r["rationale"],
            "",
        ]
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
