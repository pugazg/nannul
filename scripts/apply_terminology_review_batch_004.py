#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 004 to the review ledger."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-004-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-004"
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
    d("nannul-term-candidate-509403e7f807bdae", "ப", "accepted", "phonology-letter-class",
      "ப is explicitly enumerated as a வல்லினம் consonant and repeatedly functions as a letter symbol in phonological environments. The same exact form also appears in verbal-ending/intermediate inventories, so acceptance is context-bounded rather than limited to one grammatical domain.",
      ["nannul-0068", "nannul-0119", "nannul-0140", "nannul-0144", "nannul-0165", "nannul-0327"],
      ["nannul-0068", "nannul-0119", "nannul-0140", "nannul-0144", "nannul-0165", "nannul-0327"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-321ae55f16483bda", "ல", "accepted", "phonology-letter-class",
      "ல is explicitly enumerated as an இடையினம் consonant and is repeatedly treated as a letter/final consonant in phonological and case-related rules.",
      ["nannul-0070", "nannul-0097", "nannul-0191", "nannul-0227", "nannul-0230", "nannul-0312"],
      ["nannul-0070", "nannul-0097", "nannul-0191", "nannul-0227", "nannul-0230", "nannul-0312"], scope="broad-grammatical"),
    d("nannul-term-candidate-a804913e83185380", "முன்னிலை", "accepted", "other-grammar",
      "Nannūl explicitly organizes தன்மை, முன்னிலை, படர்க்கை as three grammatical person/deictic positions and repeatedly assigns pronouns and verbal endings to முன்னிலை. The form is therefore named grammatical metalanguage, not ordinary positional vocabulary in the reviewed contexts.",
      ["nannul-0266", "nannul-0285", "nannul-0330", "nannul-0335", "nannul-0337", "nannul-0440"],
      ["nannul-0266", "nannul-0285", "nannul-0330", "nannul-0335", "nannul-0337", "nannul-0440"], scope="broad-grammatical"),
    d("nannul-term-candidate-40b244f9010bf898", "வழி", "rejected", None,
      "Across the reviewed contexts வழி functions compositionally as 'way/path/by or after a condition' inside grammatical statements. The surrounding rules are technical, but the exact surface does not operate as an independent grammatical term.",
      ["nannul-0005", "nannul-0106", "nannul-0138", "nannul-0158", "nannul-0207", "nannul-0270", "nannul-0426"],
      non_term=["nannul-0005", "nannul-0106", "nannul-0138", "nannul-0158", "nannul-0207", "nannul-0270", "nannul-0426"]),
    d("nannul-term-candidate-32c41d3451176cc7", "பிற", "rejected", None,
      "பிற consistently supplies the ordinary residual/other sense ('other, others, etc.') in lists and rules. It is not independently defined or classified as grammatical metalanguage.",
      ["nannul-0023", "nannul-0126", "nannul-0186", "nannul-0229", "nannul-0276", "nannul-0343", "nannul-0441"],
      non_term=["nannul-0023", "nannul-0126", "nannul-0186", "nannul-0229", "nannul-0276", "nannul-0343", "nannul-0441"]),
    d("nannul-term-candidate-6a23ca3b786b56ea", "ஏ", "accepted", "phonology-letter-class",
      "ஏ is explicitly listed as a long vowel and is treated as a letter in articulatory and punarcci rules. Other reviewed contexts also use the same exact form as grammatical material in சாரியை/விளி/இடையியல் environments, so the technical scope is mixed.",
      ["nannul-0065", "nannul-0077", "nannul-0201", "nannul-0244", "nannul-0307", "nannul-0428"],
      ["nannul-0065", "nannul-0077", "nannul-0201", "nannul-0244", "nannul-0307", "nannul-0428"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-84df3a3903a9fc1f", "ஆதி", "rejected", None,
      "ஆதி functions as the ordinary enumerative expression 'beginning with / and so on' across grammatical and non-grammatical classifications. The reviewed evidence does not support an independent technical-term identity.",
      ["nannul-0072", "nannul-0136", "nannul-0196", "nannul-0296", "nannul-0340", "nannul-0446", "nannul-0453"],
      non_term=["nannul-0072", "nannul-0136", "nannul-0196", "nannul-0296", "nannul-0340", "nannul-0446", "nannul-0453"]),
    d("nannul-term-candidate-0512be82f9446405", "இறுதி", "accepted", "morphology",
      "இறுதி is repeatedly used as positional grammatical metalanguage for the final/end element of a word or expression, including final letters, final deletion/change, and sentence/poetic final position.",
      ["nannul-0094", "nannul-0122", "nannul-0214", "nannul-0307", "nannul-0311", "nannul-0392", "nannul-0417"],
      ["nannul-0094", "nannul-0122", "nannul-0214", "nannul-0307", "nannul-0311", "nannul-0392", "nannul-0417"], scope="broad-grammatical"),
    d("nannul-term-candidate-5b29394d18b24268", "பிறவும்", "rejected", None,
      "பிறவும் is the ordinary additive residual expression 'and others / and other such forms' used to leave enumerations open. It does not function as an independently classified grammatical term.",
      ["nannul-0140", "nannul-0188", "nannul-0244", "nannul-0269", "nannul-0367", "nannul-0461"],
      non_term=["nannul-0140", "nannul-0188", "nannul-0244", "nannul-0269", "nannul-0367", "nannul-0461"]),
    d("nannul-term-candidate-69e7de59bf42aada", "மூ", "rejected", None,
      "மூ is a numeral/combining form meaning three in the reviewed enumerations (three positions, three classes, three senses, etc.). Frequency inside grammatical inventories does not establish standalone technical termhood.",
      ["nannul-0063", "nannul-0142", "nannul-0143", "nannul-0266", "nannul-0324", "nannul-0447"],
      non_term=["nannul-0063", "nannul-0142", "nannul-0143", "nannul-0266", "nannul-0324", "nannul-0447"]),
    d("nannul-term-candidate-1b864dbc1be4e3f2", "ஓ", "accepted", "phonology-letter-class",
      "ஓ is explicitly listed as a long vowel and repeatedly functions as a letter in initial-position and punarcci rules. It also appears as grammatical material in இடைச்சொல் and விளி-related contexts.",
      ["nannul-0065", "nannul-0078", "nannul-0103", "nannul-0201", "nannul-0307", "nannul-0353"],
      ["nannul-0065", "nannul-0078", "nannul-0103", "nannul-0201", "nannul-0307", "nannul-0353"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-9600ae384add8ddf", "வினா", "accepted", "syntax",
      "Nannūl uses வினா explicitly for interrogative/question forms, classifies interrogative letters and words, distinguishes question functions, and lists வினா among grammatical semantic/particle functions.",
      ["nannul-0067", "nannul-0106", "nannul-0163", "nannul-0349", "nannul-0375", "nannul-0385", "nannul-0421"],
      ["nannul-0067", "nannul-0106", "nannul-0163", "nannul-0349", "nannul-0375", "nannul-0385", "nannul-0421"], scope="broad-grammatical"),
    d("nannul-term-candidate-766427f8a352b12d", "அல்", "accepted", "morphology",
      "The exact form அல் is explicitly listed among verbal endings/viguti and among சாரியை forms, while other contexts use ordinary negative/exclusion senses. It therefore has internally supported grammatical-form use but is not uniformly technical.",
      ["nannul-0140", "nannul-0141", "nannul-0207", "nannul-0244", "nannul-0280", "nannul-0331", "nannul-0450"],
      ["nannul-0140", "nannul-0244", "nannul-0331"],
      ["nannul-0141", "nannul-0207", "nannul-0280", "nannul-0450"], scope="mixed-context"),
    d("nannul-term-candidate-82c1bfbece726d1a", "இவை", "rejected", None,
      "இவை is the ordinary demonstrative pronoun 'these' used to point back to previously enumerated grammatical material. Its discourse function does not require a separate grammatical-term identity.",
      ["nannul-0003", "nannul-0041", "nannul-0125", "nannul-0144", "nannul-0316", "nannul-0374"],
      non_term=["nannul-0003", "nannul-0041", "nannul-0125", "nannul-0144", "nannul-0316", "nannul-0374"]),
    d("nannul-term-candidate-1bd75d2043346766", "ஓர்", "rejected", None,
      "ஓர் functions as the numeral/indefinite 'one/a certain' across the reviewed grammatical and ordinary classifications. It is not independently defined as technical metalanguage.",
      ["nannul-0004", "nannul-0072", "nannul-0129", "nannul-0301", "nannul-0380", "nannul-0420", "nannul-0445"],
      non_term=["nannul-0004", "nannul-0072", "nannul-0129", "nannul-0301", "nannul-0380", "nannul-0420", "nannul-0445"]),
    d("nannul-term-candidate-df9c04f9e4750980", "எனும்", "rejected", None,
      "எனும் is a compositional quotative/attributive form meaning 'called/termed' that introduces names and lists. The already reviewed base quotative form என has its own grammatical evidence; this inflected surface does not require an independent term identity.",
      ["nannul-0009", "nannul-0013", "nannul-0267", "nannul-0368", "nannul-0370", "nannul-0424", "nannul-0433"],
      non_term=["nannul-0009", "nannul-0013", "nannul-0267", "nannul-0368", "nannul-0370", "nannul-0424", "nannul-0433"]),
    d("nannul-term-candidate-4332d9db2936a85c", "க", "accepted", "phonology-letter-class",
      "க is explicitly enumerated as a வல்லினம் consonant and repeatedly functions as a letter symbol in phonological environments. It also occurs in verbal-ending inventories, so the exact form has multiple grammatical uses.",
      ["nannul-0068", "nannul-0102", "nannul-0119", "nannul-0140", "nannul-0165", "nannul-0224"],
      ["nannul-0068", "nannul-0102", "nannul-0119", "nannul-0140", "nannul-0165", "nannul-0224"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-6d321faedeede394", "த", "accepted", "phonology-letter-class",
      "த is explicitly enumerated as a வல்லினம் consonant and repeatedly functions as a letter symbol in phonological rules; it is also listed in grammatical ending/intermediate inventories.",
      ["nannul-0068", "nannul-0102", "nannul-0119", "nannul-0140", "nannul-0142", "nannul-0165"],
      ["nannul-0068", "nannul-0102", "nannul-0119", "nannul-0140", "nannul-0142", "nannul-0165"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-9843c57bcbbeb72b", "ஞ", "accepted", "phonology-letter-class",
      "ஞ is explicitly enumerated as a மெல்லினம் consonant and repeatedly treated as a letter in articulation, word-position, consonant-cluster, and punarcci rules.",
      ["nannul-0069", "nannul-0092", "nannul-0102", "nannul-0114", "nannul-0119", "nannul-0207"],
      ["nannul-0069", "nannul-0092", "nannul-0102", "nannul-0114", "nannul-0119", "nannul-0207"], scope="broad-grammatical"),
    d("nannul-term-candidate-746cc08d32535e2c", "ந", "accepted", "phonology-letter-class",
      "ந is explicitly enumerated as a மெல்லினம் consonant and repeatedly treated as a letter in articulation, word-position, consonant-cluster, and punarcci rules.",
      ["nannul-0069", "nannul-0092", "nannul-0102", "nannul-0119", "nannul-0158", "nannul-0207"],
      ["nannul-0069", "nannul-0092", "nannul-0102", "nannul-0119", "nannul-0158", "nannul-0207"], scope="broad-grammatical"),
    d("nannul-term-candidate-1ec5a36a3782e1a4", "அற்று", "accepted", "morphology",
      "அற்று is explicitly listed as a சாரியை and is used as a grammatical linking/formative element after particular pronoun/nominal forms. Other occurrences carry ordinary privative/residual senses, so acceptance is context-bounded.",
      ["nannul-0095", "nannul-0131", "nannul-0244", "nannul-0245", "nannul-0250", "nannul-0412"],
      ["nannul-0244", "nannul-0245", "nannul-0250"],
      ["nannul-0095", "nannul-0131", "nannul-0412"], scope="mixed-context"),
    d("nannul-term-candidate-cc048cf2cc5b37c0", "படர்க்கை", "accepted", "other-grammar",
      "Nannūl explicitly organizes தன்மை, முன்னிலை, படர்க்கை as the three grammatical person/deictic positions and systematically assigns nouns, pronouns, and finite verb forms to படர்க்கை.",
      ["nannul-0265", "nannul-0266", "nannul-0285", "nannul-0324", "nannul-0325", "nannul-0328", "nannul-0348"],
      ["nannul-0265", "nannul-0266", "nannul-0285", "nannul-0324", "nannul-0325", "nannul-0328", "nannul-0348"], scope="broad-grammatical"),
    d("nannul-term-candidate-5d62934869983b90", "பெயரே", "rejected", None,
      "பெயரே is a predicative/emphatic surface built from the independently meaningful grammatical base பெயர். The reviewed contexts repeatedly mean 'is/name/noun indeed' rather than establishing a separate technical category for the cliticized exact form.",
      ["nannul-0047", "nannul-0275", "nannul-0277", "nannul-0286", "nannul-0290", "nannul-0292", "nannul-0295"],
      non_term=["nannul-0047", "nannul-0275", "nannul-0277", "nannul-0286", "nannul-0290", "nannul-0292", "nannul-0295"],
      notes="Rejection concerns independent exact-form termhood only; it does not reject the base grammatical term பெயர்."),
    d("nannul-term-candidate-8c9d0755f2df765a", "குறில்", "accepted", "phonology-letter-class",
      "Nannūl explicitly defines the five short vowels as குறில் and repeatedly uses the term in phonological quantity, consonant-cluster, punarcci, and single-letter word conditions.",
      ["nannul-0064", "nannul-0091", "nannul-0092", "nannul-0119", "nannul-0129", "nannul-0158", "nannul-0228"],
      ["nannul-0064", "nannul-0091", "nannul-0092", "nannul-0119", "nannul-0129", "nannul-0158", "nannul-0228"], scope="broad-grammatical"),
    d("nannul-term-candidate-26d2bf5001380579", "வ", "accepted", "phonology-letter-class",
      "வ is explicitly enumerated as an இடையினம் consonant and repeatedly treated as a letter in articulation, word-position, cluster, and punarcci rules. It also appears in tense/intermediate grammatical inventories.",
      ["nannul-0070", "nannul-0092", "nannul-0102", "nannul-0114", "nannul-0117", "nannul-0144", "nannul-0207"],
      ["nannul-0070", "nannul-0092", "nannul-0102", "nannul-0114", "nannul-0117", "nannul-0144", "nannul-0207"], scope="multiple-grammatical-senses"),
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    existing = {row["candidate_id"] for row in ledger["decisions"]}
    if any(row.get("review_batch") == BATCH for row in ledger["decisions"]):
        raise SystemExit("Batch 004 already exists in ledger")
    collisions = [row["candidate_id"] for row in DECISIONS if row["candidate_id"] in existing]
    if collisions:
        raise SystemExit(f"Already-reviewed candidate IDs in Batch 004: {collisions}")
    if len(DECISIONS) != 25:
        raise SystemExit(f"Expected 25 Batch-004 decisions, got {len(DECISIONS)}")

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

    batch = [r for r in DECISIONS]
    lines = [
        "# Nannūl Grammatical Terminology Review — Batch 004 Decisions",
        "",
        "Human/contextual review under `docs/GRAMMATICAL_TERMINOLOGY_REVIEW_GUIDELINES.md`.",
        "",
        f"- Reviewed: **{len(batch)}**",
        f"- Accepted: **{sum(1 for r in batch if r['decision'] == 'accepted')}**",
        f"- Rejected: **{sum(1 for r in batch if r['decision'] == 'rejected')}**",
        f"- Needs context: **{sum(1 for r in batch if r['decision'] == 'needs-context')}**",
        "",
    ]
    for r in batch:
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
