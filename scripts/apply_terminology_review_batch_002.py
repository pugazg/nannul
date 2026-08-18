#!/usr/bin/env python3
"""Apply human/contextual Nannul terminology review Batch 002 to the review ledger.

Decisions are based only on internal canonical Nannul evidence prepared under
reviews/terminology/batch-002-*. Generated candidate-discovery files are never
modified.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "grammatical-terminology-review.json"
SUMMARY = ROOT / "reviews" / "terminology" / "batch-002-decisions.md"
BATCH = "NANNUL-TERM-REVIEW-002"
BASIS = "internal-canonical-contexts-and-source-headings"


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
    d(
        "nannul-term-candidate-47b58d96bd85f891", "பதம்", "accepted", "meta-grammar",
        "Nannūl explicitly defines பதம் as a meaning-bearing unit, divides it into பகாப்பதம் and பகுபதம், and reuses the exact form in grammatical inventories and உருபு-related rules.",
        ["nannul-0057", "nannul-0129", "nannul-0254", "nannul-0128"],
        ["nannul-0057", "nannul-0129", "nannul-0254", "nannul-0128"],
        notes="The source heading பதம் (128–133) and the explicit definition at 128 provide direct internal term evidence.",
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-70d6fc2f1f337bad", "வேற்றுமைப்", "accepted", "case",
        "The bound exact form வேற்றுமைப் consistently carries the grammatical case sense in technical compounds such as வேற்றுமைப் பொருள் and வேற்றுமைப் புணர்ப்பு across punarcci contexts.",
        ["nannul-0151", "nannul-0212", "nannul-0242", "nannul-0238"],
        ["nannul-0151", "nannul-0212", "nannul-0242"],
        notes="This is an exact bound/attributive surface form of the already reviewed case term வேற்றுமை; it is retained independently rather than silently merged.",
        scope="technical-bound-form",
    ),
    d(
        "nannul-term-candidate-ff7b639378ce2c86", "வினையெச்சம்", "accepted", "verb",
        "Nannūl gives வினையெச்சம் a dedicated source heading and explicit verbal classification/definition, and uses the exact form in both வினையியல் and punarcci discussion.",
        ["nannul-0167", "nannul-0343", "nannul-0342"],
        ["nannul-0167", "nannul-0343"],
        notes="Nūṟpā 342 defines the category under the heading வினையெச்சம்; the body uses the segmented form வினையெச் சம்மே.",
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-3cc7806094981427", "விகுதி", "accepted", "morphology",
        "விகுதி is explicitly listed as a component of பகுபதம், receives its own heading, and is enumerated through verbal/name endings in பதவியல்.",
        ["nannul-0133", "nannul-0254", "nannul-0140"],
        ["nannul-0133", "nannul-0254", "nannul-0140"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-c91df5c7fce71d65", "பொதுப்", "rejected", None,
        "The exact bound form பொதுப் functions compositionally as the ordinary modifier 'general/common' inside technical expressions such as பொதுப் பாயிரம் and பொதுப் பெயர்; the reviewed evidence does not establish it as an independent grammatical technical term.",
        ["nannul-0003", "nannul-0312", "nannul-0001"],
        non_term=["nannul-0003", "nannul-0312"],
        notes="Technical compounds containing பொதுப் remain meaningful; rejection concerns independent exact-form termhood only.",
    ),
    d(
        "nannul-term-candidate-60bd7274594ffc5d", "போலி", "accepted", "other-grammar",
        "போலி is named as an எழுத்து இயல் topic and is also used in the classified expression இலக்கணப் போலி, supporting an internal grammatical concept of substitution/semblance rather than ordinary lexical use alone.",
        ["nannul-0057", "nannul-0267", "nannul-0122"],
        ["nannul-0057", "nannul-0267"],
        notes="The broad category other-grammar avoids over-narrowing a concept that appears in both letter-level and usage classification contexts.",
        scope="multiple-grammatical-senses",
    ),
    d(
        "nannul-term-candidate-173b59fbc007924b", "இலக்கணம்", "accepted", "meta-grammar",
        "Nannūl uses இலக்கணம் explicitly for grammar/rule formulation, contrasts இலக்கியம் with இலக்கணம், and employs the form in classifying usage as இலக்கணம் உடையது / இலக்கணப் போலி.",
        ["nannul-0141", "nannul-0267", "nannul-0047"],
        ["nannul-0141", "nannul-0267"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-f129dd4737adaa2d", "உருபுகள்", "accepted", "morphology",
        "The plural exact form உருபுகள் is a source heading and appears in explicit descriptions of grammatical markers and particle classes, retaining the technical sense of உருபு in plural form.",
        ["nannul-0242", "nannul-0420", "nannul-0240"],
        ["nannul-0242", "nannul-0420"],
        notes="The plural surface remains independently addressable and is not silently merged with singular உருபு.",
        scope="technical-inflectional-variant",
    ),
    d(
        "nannul-term-candidate-38add2df5dcb7d46", "பொருள்கோள்", "accepted", "syntax",
        "Nannūl explicitly names பொருள்கோள், states that there are eight types, and governs a dedicated 411–419 section describing methods by which textual order is construed for meaning.",
        ["nannul-0411"],
        ["nannul-0411"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-f7d70f4b2f728bd4", "இகர", "accepted", "phonology-letter-class",
        "இகர is used as the grammatical name of the i-vowel/இ-letter in ending and extension descriptions and occurs in the technical heading இகர வீற்றுச் சிறப்புவிதி.",
        ["nannul-0305", "nannul-0335", "nannul-0173"],
        ["nannul-0305", "nannul-0335"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-4e5e3237c758e7c2", "சொல்லின்", "rejected", None,
        "The exact form சொல்லின் is a compositional genitive/oblique form of சொல் ('of the word/words') in both the reviewed body context and the heading சொல்லின் பொதுவிலக்கணம். The base grammatical term சொல் is already independently reviewed; the inflected relational surface does not need a separate term entry.",
        ["nannul-0014", "nannul-0259"],
        non_term=["nannul-0014"],
        notes="Rejection does not deny that the governed heading is grammatical; it distinguishes term identity from an inflected syntactic form of the accepted term சொல்.",
    ),
    d(
        "nannul-term-candidate-95cb5664bc1e4936", "பிறப்பு", "accepted", "phonology-sound-process",
        "பிறப்பு is explicitly listed as an எழுத்து இயல் topic and heads the section explaining how differentiated letter sounds arise through articulatory effort and places of articulation.",
        ["nannul-0057", "nannul-0074"],
        ["nannul-0057"],
        notes="The governed definition uses பிறப்பே, while the exact candidate form occurs in the topic inventory at 57.",
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-9f30af081804037a", "உருவம்", "accepted", "orthography",
        "உருவம் is explicitly listed among the எழுத்து இயல் dimensions and receives a dedicated source heading governing the statement about letter shapes/forms and dot marking.",
        ["nannul-0057", "nannul-0098"],
        ["nannul-0057"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-3f8e59246d33784d", "அகர", "accepted", "phonology-letter-class",
        "அகர names the அ-vowel/letter in an explicit morphophonological rule and appears in the technical heading அகர வீற்றுச் சிறப்புவிதி.",
        ["nannul-0252", "nannul-0167"],
        ["nannul-0252"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-842e4e3df88fd099", "சிறப்புப்", "rejected", None,
        "The exact bound form சிறப்புப் functions as the ordinary modifier 'special/specific' inside distinct technical compounds (சிறப்புப் பெயர்வினை, சிறப்புப் புணர்ச்சி). The evidence supports those compounds, not independent termhood for the modifier itself.",
        ["nannul-0359", "nannul-0162"],
        non_term=["nannul-0359"],
        notes="This parallels the treatment of பொதுப்: technical compound membership alone does not create a standalone exact-form term.",
    ),
    d(
        "nannul-term-candidate-173b8dcc874200bd", "ஒழிபு", "accepted", "other-grammar",
        "ஒழிபு is used as named grammatical metalanguage in பொதுவியல் and is also the source heading for a dedicated வினையியல் residual/exceptional-rules section, supporting technical use without forcing a narrower modern category.",
        ["nannul-0360", "nannul-0347"],
        ["nannul-0360"],
        scope="broad-grammatical",
    ),
    d(
        "nannul-term-candidate-90d8fa6c597a2209", "பெயரெச்சம்", "accepted", "verb",
        "பெயரெச்சம் has a dedicated வினையியல் heading and definition and is used explicitly in the description of வினைத்தொகை, establishing a verbal/participial grammatical category.",
        ["nannul-0364", "nannul-0340"],
        ["nannul-0364"],
        notes="The governed definition at 340 uses the segmented form பெயரெச் சம்மே; the exact candidate occurs at 364.",
        scope="broad-grammatical",
    ),
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    existing = {row["candidate_id"] for row in ledger["decisions"]}
    if any(row["review_batch"] == BATCH for row in ledger["decisions"]):
        raise SystemExit("Batch 002 already exists in ledger")
    collisions = [row["candidate_id"] for row in DECISIONS if row["candidate_id"] in existing]
    if collisions:
        raise SystemExit(f"Already-reviewed candidate IDs in Batch 002: {collisions}")
    if len(DECISIONS) != 17:
        raise SystemExit(f"Expected 17 Batch-002 decisions, got {len(DECISIONS)}")

    ledger["decisions"].extend(DECISIONS)
    reviewed = len(ledger["decisions"])
    accepted = sum(r["decision"] == "accepted" for r in ledger["decisions"])
    rejected = sum(r["decision"] == "rejected" for r in ledger["decisions"])
    needs = sum(r["decision"] == "needs-context" for r in ledger["decisions"])
    total = ledger["counts"]["candidate_surface_forms"]
    ledger["counts"].update({
        "reviewed": reviewed,
        "accepted": accepted,
        "rejected": rejected,
        "needs_context": needs,
        "unreviewed": total - reviewed,
    })
    ledger["layer_status"] = "review-complete" if reviewed == total else "review-in-progress"
    LEDGER.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Nannūl Grammatical Terminology Review — Batch 002 Decisions",
        "",
        "Human/contextual review using internal canonical Nannūl evidence only.",
        "",
        f"- Reviewed in batch: **{len(DECISIONS)}**",
        f"- Accepted in batch: **{sum(r['decision'] == 'accepted' for r in DECISIONS)}**",
        f"- Rejected in batch: **{sum(r['decision'] == 'rejected' for r in DECISIONS)}**",
        f"- Needs context in batch: **{sum(r['decision'] == 'needs-context' for r in DECISIONS)}**",
        "",
        "| Exact form | Decision | Category |",
        "|---|---|---|",
    ]
    for row in DECISIONS:
        lines.append(f"| `{row['surface_form_ta']}` | **{row['decision']}** | `{row['term_category'] or '—'}` |")
    lines += ["", "## Decision rationales", ""]
    for row in DECISIONS:
        lines += [
            f"### `{row['surface_form_ta']}`",
            "",
            row["rationale"],
            "",
            f"Reviewed evidence: {', '.join(f'`{rid}`' for rid in row['reviewed_record_ids'])}",
            "",
        ]
    SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PASS",
        "batch": BATCH,
        "batch_decisions": len(DECISIONS),
        "batch_accepted": sum(r["decision"] == "accepted" for r in DECISIONS),
        "batch_rejected": sum(r["decision"] == "rejected" for r in DECISIONS),
        "ledger_reviewed": reviewed,
        "ledger_unreviewed": total - reviewed,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
