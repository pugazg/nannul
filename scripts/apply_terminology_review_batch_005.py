#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 005 to the review ledger."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-005-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-005"
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
    d("nannul-term-candidate-f5d907741141f2eb", "ஆய்", "accepted", "morphology",
      "ஆய் is explicitly listed among verbal endings and as one of the singular முன்னிலை imperative endings. Other occurrences use the same surface compositionally in the sense 'as/becoming', so acceptance is restricted to the documented morphological contexts.",
      ["nannul-0047", "nannul-0084", "nannul-0089", "nannul-0140", "nannul-0173", "nannul-0256", "nannul-0335", "nannul-0406"],
      ["nannul-0140", "nannul-0335"],
      ["nannul-0047", "nannul-0084", "nannul-0089", "nannul-0173", "nannul-0256", "nannul-0406"], scope="mixed-context"),
    d("nannul-term-candidate-9a8b17b7005dc0c9", "இரண்டு", "rejected", None,
      "இரண்டு is the ordinary numeral 'two' throughout the reviewed enumerations and rule counts. Its recurrence inside grammatical classifications does not establish an independent grammatical-term identity.",
      ["nannul-0050", "nannul-0147", "nannul-0157", "nannul-0198", "nannul-0270", "nannul-0361", "nannul-0363", "nannul-0373", "nannul-0395"],
      non_term=["nannul-0050", "nannul-0147", "nannul-0157", "nannul-0198", "nannul-0270", "nannul-0361", "nannul-0363", "nannul-0373", "nannul-0395"]),
    d("nannul-term-candidate-2f8273285b40887d", "அ", "accepted", "phonology-letter-class",
      "அ is explicitly one of the five குறில் vowels and is repeatedly handled as a letter in articulation and word-position rules. The exact form also occurs in விகுதி and சாரியை inventories, giving it additional grammatical-form uses.",
      ["nannul-0064", "nannul-0066", "nannul-0076", "nannul-0104", "nannul-0123", "nannul-0140", "nannul-0244", "nannul-0329"],
      ["nannul-0064", "nannul-0066", "nannul-0076", "nannul-0104", "nannul-0123", "nannul-0140", "nannul-0244", "nannul-0329"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-06f94daf5c38de22", "ஈ", "accepted", "phonology-letter-class",
      "ஈ is explicitly listed as a long vowel and is treated as a letter in articulation, word-final, punarcci, and case-form rules. The same surface also appears in grammatical asai/form inventories; ordinary lexical imperative use is kept separate.",
      ["nannul-0065", "nannul-0077", "nannul-0147", "nannul-0162", "nannul-0177", "nannul-0309", "nannul-0407", "nannul-0440"],
      ["nannul-0065", "nannul-0077", "nannul-0147", "nannul-0162", "nannul-0177", "nannul-0309", "nannul-0440"],
      ["nannul-0407"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-ab1fdd3b22f3fe17", "சுட்டு", "accepted", "other-grammar",
      "சுட்டு is internally established as demonstrative/deictic grammatical metalanguage: Nannūl classifies சுட்டு letters/forms, uses it in punarcci rules, and lists it among nominal and rule-semantic categories.",
      ["nannul-0106", "nannul-0163", "nannul-0179", "nannul-0235", "nannul-0276", "nannul-0279", "nannul-0280", "nannul-0386"],
      ["nannul-0106", "nannul-0163", "nannul-0179", "nannul-0235", "nannul-0276", "nannul-0279", "nannul-0280", "nannul-0386"], scope="broad-grammatical"),
    d("nannul-term-candidate-0bc7aaac11f19241", "இனம்", "accepted", "other-grammar",
      "இனம் functions as grammatical class/kind metalanguage across phonology and syntax/semantics, including homorganic letter classes, class-based alternation, and semantic/class relations.",
      ["nannul-0112", "nannul-0114", "nannul-0136", "nannul-0235", "nannul-0358", "nannul-0390", "nannul-0401", "nannul-0402", "nannul-0434"],
      ["nannul-0112", "nannul-0114", "nannul-0136", "nannul-0235", "nannul-0358", "nannul-0390", "nannul-0401", "nannul-0402", "nannul-0434"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-a1b95759ebcbbe9e", "பெயர்வினை", "accepted", "meta-grammar",
      "பெயர்வினை repeatedly functions as a collective grammatical designation for noun-and-verb classes in word classification, inflection, syntactic distribution, and உரிச்சொல் rules.",
      ["nannul-0131", "nannul-0270", "nannul-0322", "nannul-0353", "nannul-0356", "nannul-0357", "nannul-0359", "nannul-0360", "nannul-0442"],
      ["nannul-0131", "nannul-0270", "nannul-0322", "nannul-0353", "nannul-0356", "nannul-0357", "nannul-0359", "nannul-0360", "nannul-0442"], scope="broad-grammatical"),
    d("nannul-term-candidate-c7048275c4be40ad", "ஏவல்", "accepted", "verb",
      "ஏவல் is explicitly used for imperative verbal formation and imperative function, including ஏவல் வினை, derived imperative formation, imperative endings, and imperative speech acts.",
      ["nannul-0137", "nannul-0138", "nannul-0145", "nannul-0207", "nannul-0337", "nannul-0385", "nannul-0386"],
      ["nannul-0137", "nannul-0138", "nannul-0145", "nannul-0207", "nannul-0337", "nannul-0385", "nannul-0386"], scope="broad-grammatical"),
    d("nannul-term-candidate-94012cb385d09be7", "எச்சம்", "accepted", "syntax",
      "எச்சம் is repeatedly used as grammatical metalanguage for residual/elliptic or dependent completion classes, including பெயர்/வினை எச்சம், construction inventories, and இடைச்சொல் meanings.",
      ["nannul-0152", "nannul-0167", "nannul-0330", "nannul-0355", "nannul-0356", "nannul-0360", "nannul-0374", "nannul-0421", "nannul-0425"],
      ["nannul-0152", "nannul-0167", "nannul-0330", "nannul-0355", "nannul-0356", "nannul-0360", "nannul-0374", "nannul-0421", "nannul-0425"], scope="broad-grammatical"),
    d("nannul-term-candidate-6d38c554eefd9669", "உருபே", "rejected", None,
      "உருபே is a predicative/emphatic exact surface based on the independently accepted term உருபு. The reviewed passages assert that something 'is a உருபு'; they do not establish a distinct grammatical category named உருபே.",
      ["nannul-0167", "nannul-0240", "nannul-0241", "nannul-0255", "nannul-0302", "nannul-0303", "nannul-0309", "nannul-0310", "nannul-0367"],
      non_term=["nannul-0167", "nannul-0240", "nannul-0241", "nannul-0255", "nannul-0302", "nannul-0303", "nannul-0309", "nannul-0310", "nannul-0367"],
      notes="Rejection concerns independent exact-form termhood only; the base term உருபு remains accepted."),
    d("nannul-term-candidate-abef0a958cccba02", "அவற்றுள்,", "rejected", None,
      "அவற்றுள், is a punctuation-bearing discourse expression meaning 'among those'. It introduces sublists across sections but is not grammatical terminology.",
      ["nannul-0006", "nannul-0064", "nannul-0076", "nannul-0147", "nannul-0276", "nannul-0284", "nannul-0295", "nannul-0344"],
      non_term=["nannul-0006", "nannul-0064", "nannul-0076", "nannul-0147", "nannul-0276", "nannul-0284", "nannul-0295", "nannul-0344"]),
    d("nannul-term-candidate-3bf339c0198f1dc7", "தன்", "rejected", None,
      "தன் is primarily the ordinary reflexive/possessive form 'one's own' and, where cited as a word form, functions as lexical material subjected to a rule rather than as the name of a grammatical concept. It belongs more naturally in a later example/form index.",
      ["nannul-0023", "nannul-0051", "nannul-0052", "nannul-0136", "nannul-0206", "nannul-0218", "nannul-0358"],
      non_term=["nannul-0023", "nannul-0051", "nannul-0052", "nannul-0136", "nannul-0206", "nannul-0218", "nannul-0358"]),
    d("nannul-term-candidate-a5a495703733498b", "காலம்", "accepted", "verb",
      "காலம் is explicitly grammaticalized as tense/time classification: Nannūl defines the three verbal times இறப்பு, எதிர்வு, நிகழ்வு, treats tense in verbal meaning, and identifies tense-hidden verbal compounds. Broader time senses remain compatible but do not erase this technical use.",
      ["nannul-0048", "nannul-0132", "nannul-0275", "nannul-0276", "nannul-0320", "nannul-0364", "nannul-0382", "nannul-0431"],
      ["nannul-0132", "nannul-0275", "nannul-0276", "nannul-0320", "nannul-0364", "nannul-0382", "nannul-0431"],
      ["nannul-0048"], scope="mixed-context"),
    d("nannul-term-candidate-496c2a1107074373", "அளவு", "accepted", "prosodic-measure",
      "அளவு has explicit phonological/quantitative use for sound duration and measure, including உயிர் அளவு and அளவு இறந்து இசைத்தல். Other occurrences mean ordinary extent/limit, so acceptance is context-bounded.",
      ["nannul-0049", "nannul-0072", "nannul-0089", "nannul-0101", "nannul-0110", "nannul-0253", "nannul-0257", "nannul-0276"],
      ["nannul-0072", "nannul-0089", "nannul-0101", "nannul-0110", "nannul-0276"],
      ["nannul-0049", "nannul-0253", "nannul-0257"], scope="mixed-context"),
    d("nannul-term-candidate-5df3e2351076381c", "உ", "accepted", "phonology-letter-class",
      "உ is explicitly one of the five குறில் vowels and is handled as a letter in articulation and word-position rules. The same exact form is also listed among சாரியை and case-related grammatical forms.",
      ["nannul-0060", "nannul-0064", "nannul-0066", "nannul-0078", "nannul-0103", "nannul-0104", "nannul-0244", "nannul-0304"],
      ["nannul-0060", "nannul-0064", "nannul-0066", "nannul-0078", "nannul-0103", "nannul-0104", "nannul-0244", "nannul-0304"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-430bfc0719002403", "ற", "accepted", "phonology-letter-class",
      "ற is explicitly enumerated as a வல்லினம் consonant and repeatedly manipulated as a letter in phonological rules. It also occurs in விகுதி, இடைநிலை, and finite-verb ending inventories.",
      ["nannul-0068", "nannul-0140", "nannul-0142", "nannul-0150", "nannul-0183", "nannul-0191", "nannul-0227", "nannul-0332"],
      ["nannul-0068", "nannul-0140", "nannul-0142", "nannul-0150", "nannul-0183", "nannul-0191", "nannul-0227", "nannul-0332"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-d0db287d26f057d8", "இடம்", "accepted", "other-grammar",
      "இடம் is used as grammatical place/position metalanguage in more than one domain: place of articulation, semantic/location class, and the grammatical person/deictic dimension contrasted in வழு rules. The exact form is therefore technically meaningful despite ordinary locative overlap.",
      ["nannul-0075", "nannul-0087", "nannul-0132", "nannul-0302", "nannul-0375", "nannul-0380", "nannul-0390"],
      ["nannul-0075", "nannul-0087", "nannul-0132", "nannul-0302", "nannul-0375", "nannul-0380", "nannul-0390"], scope="multiple-grammatical-senses"),
    d("nannul-term-candidate-aca5a71e93ab7c03", "முன்னர்", "rejected", None,
      "முன்னர் functions compositionally as the relational 'before/in front of' in phonological and morphological conditioning statements. It is rule language, not the name of an independent grammatical category.",
      ["nannul-0090", "nannul-0116", "nannul-0163", "nannul-0166", "nannul-0178", "nannul-0179", "nannul-0280", "nannul-0336"],
      non_term=["nannul-0090", "nannul-0116", "nannul-0163", "nannul-0166", "nannul-0178", "nannul-0179", "nannul-0280", "nannul-0336"]),
    d("nannul-term-candidate-d8dbf0f63eea6caf", "மொழி", "accepted", "meta-grammar",
      "மொழி repeatedly functions as metalinguistic 'word/expression' in technical positional and construction descriptions such as மொழி முதல், மொழி இடை, இறு மொழி, and அடைசேர் மொழி.",
      ["nannul-0102", "nannul-0110", "nannul-0169", "nannul-0215", "nannul-0256", "nannul-0326", "nannul-0401", "nannul-0417"],
      ["nannul-0102", "nannul-0110", "nannul-0169", "nannul-0215", "nannul-0256", "nannul-0326", "nannul-0401", "nannul-0417"], scope="broad-grammatical"),
    d("nannul-term-candidate-4d62645c8771a410", "நான்கும்", "rejected", None,
      "நான்கும் is the numeral four with additive/collective morphology ('all four/the four'), used to count members of grammatical inventories. It is not an independent technical term.",
      ["nannul-0131", "nannul-0146", "nannul-0282", "nannul-0344", "nannul-0428"],
      non_term=["nannul-0131", "nannul-0146", "nannul-0282", "nannul-0344", "nannul-0428"]),
    d("nannul-term-candidate-dabe927001ce6df6", "அகரம்", "accepted", "phonology-letter-class",
      "அகரம் is explicit letter-name metalanguage for the அ vowel and is repeatedly used to describe its insertion, deletion, change, and occurrence as an ending in morphological and case rules.",
      ["nannul-0136", "nannul-0170", "nannul-0215", "nannul-0252", "nannul-0308", "nannul-0309", "nannul-0327"],
      ["nannul-0136", "nannul-0170", "nannul-0215", "nannul-0252", "nannul-0308", "nannul-0309", "nannul-0327"], scope="broad-grammatical"),
    d("nannul-term-candidate-f036af407abc2532", "உம்மை", "accepted", "particle",
      "உம்மை is explicitly grammatical terminology for the உம் particle and its functions/constructions, including உம்மைத்தொகை, எச்ச உம்மை, particle meanings, and morphophonological treatment.",
      ["nannul-0145", "nannul-0152", "nannul-0246", "nannul-0362", "nannul-0399", "nannul-0425", "nannul-0427", "nannul-0428"],
      ["nannul-0145", "nannul-0152", "nannul-0246", "nannul-0362", "nannul-0399", "nannul-0425", "nannul-0427", "nannul-0428"], scope="broad-grammatical"),
    d("nannul-term-candidate-68d36cd806e3a5d5", "ஏற்கும்", "rejected", None,
      "ஏற்கும் is the ordinary verbal form 'accepts/takes/can take' used to state compatibility or applicability of grammatical forms. It describes rule behavior rather than naming a grammatical category.",
      ["nannul-0145", "nannul-0195", "nannul-0197", "nannul-0284", "nannul-0291", "nannul-0293", "nannul-0344", "nannul-0381"],
      non_term=["nannul-0145", "nannul-0195", "nannul-0197", "nannul-0284", "nannul-0291", "nannul-0293", "nannul-0344", "nannul-0381"]),
    d("nannul-term-candidate-f521a06150b17a6c", "உயர்திணை", "accepted", "noun",
      "உயர்திணை is explicitly defined as a core nominal/semantic class, contrasted with அஃறிணை and subdivided into ஆண், பெண், பலர்; subsequent case and construction rules depend on this class.",
      ["nannul-0159", "nannul-0255", "nannul-0261", "nannul-0262", "nannul-0304", "nannul-0311", "nannul-0372", "nannul-0377"],
      ["nannul-0159", "nannul-0255", "nannul-0261", "nannul-0262", "nannul-0304", "nannul-0311", "nannul-0372", "nannul-0377"], scope="broad-grammatical"),
    d("nannul-term-candidate-e3f784e2f7279b16", "சிறப்பு", "accepted", "semantics",
      "சிறப்பு has explicit grammatical uses for particularizing/emphatic distinction, including சிறப்பு எழுத்து and the சிறப்பு semantic function of particles. The same surface also occurs as ordinary 'distinction/excellence', so acceptance is context-bounded.",
      ["nannul-0002", "nannul-0274", "nannul-0276", "nannul-0390", "nannul-0421", "nannul-0423", "nannul-0425"],
      ["nannul-0002", "nannul-0274", "nannul-0390", "nannul-0421", "nannul-0423", "nannul-0425"],
      ["nannul-0276"], scope="multiple-grammatical-senses"),
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    existing = {row["candidate_id"] for row in ledger["decisions"]}
    if any(row.get("review_batch") == BATCH for row in ledger["decisions"]):
        raise SystemExit("Batch 005 already exists in ledger")
    collisions = [row["candidate_id"] for row in DECISIONS if row["candidate_id"] in existing]
    if collisions:
        raise SystemExit(f"Already-reviewed candidate IDs in Batch 005: {collisions}")
    if len(DECISIONS) != 25:
        raise SystemExit(f"Expected 25 Batch-005 decisions, got {len(DECISIONS)}")

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
        "# Nannūl Grammatical Terminology Review — Batch 005 Decisions",
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
