"""Pure Markdown presentation of separate assessment results; no PDF generation."""

from dataclasses import dataclass
import re

from srat import SratResult


HEADINGS = (
    "Executive Summary", "Software, Purpose and Scope", "Information and Assets",
    "Submitted Facts and Reported Safeguards", "Prior Assessment and Approval History",
    "Preliminary Risk Analysis", "Risk Rating", "Assumptions, Unknowns and Source Limitations",
    "Conclusion and Next Steps",
)
DISCLAIMER = (
    "This preliminary assessment assumes the submitted information is accurate for purposes of analysis. "
    "Submitted facts and safeguards have not been independently verified. The preliminary risk conclusion "
    "is not software approval, authorization to implement, certification of compliance, formal risk "
    "acceptance, or a final security determination."
)


@dataclass(frozen=True)
class MethodologyResult:
    assessment_id: str
    methodology_id: str
    version: str
    title: str
    conclusion: str
    findings: tuple[str, ...] = ()
    applicability: tuple[str, ...] = ()


def _text(value: object) -> str:
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ").replace("#", "\\#")


def render_srat(result: SratResult) -> str:
    lines = [
        "### DDS SRAT — Software and Vendor Risk",
        f"Assessment: {_text(result.assessment_id)}; methodology: {result.methodology_id} "
        f"{result.methodology_version}; implementation: {result.implementation_version}.",
        "",
        "| Variable | Raw worksheet score | Effective SRAT score | Assessment status | Complete | Evidence status / references | Reviewer/date | Comments / gaps |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for category in result.categories:
        score = "EXCLUDED — approved N/A" if category.excluded else str(category.effective_score)
        review = f"{category.reviewer or 'NOT PROVIDED'} / {category.review_date or 'NOT PROVIDED'}"
        comments = "; ".join((category.reviewer_comments,) + category.gaps)
        references = sorted({reference for record in category.evidence_records for reference in record.evidence_references})
        evidence = f"{category.evidence_status.value}; {', '.join(references) or 'NO REFERENCES'}"
        lines.append("| " + " | ".join(_text(item) for item in (
            f"{category.variable_id} — {category.name}", category.raw_score, score,
            category.assessment_status.value, "YES" if category.complete else "NO",
            evidence, review, comments,
        )) + " |")
    lines += [
        "",
        f"**Total numerical score:** {result.total if result.total is not None else 'UNDEFINED — no applicable categories'}.",
        f"**Overall SRAT classification:** {result.classification.value}.",
        f"**Provisional:** {'YES' if result.provisional else 'NO'}; applicable categories: {result.applicable_count}; "
        f"approved exclusions: {', '.join(result.excluded_variables) or 'NONE'}.",
        "Approved N/A categories are excluded from the sum; no denominator normalization or reduced-scope threshold is inferred.",
        "",
        "**Outstanding SRAT assessment gaps:**",
    ]
    lines += [f"- {_text(gap)}" for gap in result.gaps] or ["- None recorded."]
    lines += [
        "",
        "A default HIGH reflects incomplete SRAT assurance, not a confirmed control deficiency, "
        "NIST impact categorization, NIST control-applicability decision, or software approval.",
    ]
    return "\n".join(lines)


def render_report(
    assessment_id: str,
    sections: tuple[str, ...],
    qualitative_conclusion: str,
    srat_result: SratResult | None = None,
    methodology_results: tuple[MethodologyResult, ...] = (),
) -> str:
    """Preserve supplied qualitative/NIST/privacy results without deriving crosswalks."""
    if len(sections) != 9:
        raise ValueError("Exactly nine section bodies required")
    if not assessment_id.strip():
        raise ValueError("Assessment identifier required")
    if qualitative_conclusion not in ("LOW", "MODERATE", "HIGH", "UNRESOLVED"):
        raise ValueError("Invalid preliminary qualitative conclusion")
    if srat_result is not None and srat_result.assessment_id != assessment_id:
        raise ValueError("SRAT result belongs to a different assessment")
    if any(re.search(r"^##\s+", section, re.MULTILINE) for section in sections):
        raise ValueError("Section bodies must not add top-level report sections")
    other = {result.methodology_id: result for result in methodology_results}
    if len(other) != len(methodology_results) or {"DDS-SRAT", "SAR-QUALITATIVE"} & set(other):
        raise ValueError("Duplicate or reserved methodology result identifier")
    if any(result.assessment_id != assessment_id for result in methodology_results):
        raise ValueError("Methodology result belongs to a different assessment")
    if any(not result.methodology_id.strip() or not result.version.strip() for result in methodology_results):
        raise ValueError("Methodology identifier and version required")
    defaults = (
        ("NIST-FIPS199", "NIST/FIPS 199 — Security Categorization"),
        ("NIST-SP80053", "NIST SP 800-53 Rev. 5 — Control Applicability and Assessment"),
        ("PRIVACY", "Privacy and PHI/PII Assessments"),
    )
    for identifier, title in defaults:
        if identifier not in other:
            other[identifier] = MethodologyResult(
                assessment_id, identifier, "NOT ASSESSED", title, "NOT ASSESSED"
            )
    lines = ["# SAR Preliminary Assessment", "", "**NOT AN APPROVAL**", "", DISCLAIMER, ""]
    for number, (heading, body) in enumerate(zip(HEADINGS, sections), 1):
        lines += [f"## {number}. {heading}", "", body, ""]
        if number == 7:
            lines += [
                "### SAR Preliminary Qualitative Assessment",
                f"**Overall preliminary conclusion:** {qualitative_conclusion}.",
                "Supplied scenario-based conclusion; not calculated from SRAT.", "",
                render_srat(srat_result) if srat_result else "### DDS SRAT — Software and Vendor Risk\nNOT EXECUTED — no numerical result available.",
                "",
            ]
            for result in other.values():
                lines += [
                    f"### {_text(result.title)}",
                    f"Methodology: {_text(result.methodology_id)}; version: {_text(result.version)}.",
                    f"Conclusion: {_text(result.conclusion)}.",
                    "Applicability: " + (_text("; ".join(result.applicability)) or "NOT PROVIDED"),
                    "Findings: " + (_text("; ".join(result.findings)) or "NOT PROVIDED"), "",
                ]
            lines += ["No combined numerical score or SRAT-to-NIST conversion is calculated.", ""]
        if number == 9:
            lines += [
                f"**Overall preliminary qualitative conclusion:** {qualitative_conclusion}.",
                "**NOT AN APPROVAL.** Final SRAT PDF generation is reviewer-requested only; "
                "this function returns Markdown and generates no PDF.",
                "", DISCLAIMER, "",
            ]
    return "\n".join(lines)
