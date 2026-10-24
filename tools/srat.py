"""DDS SRAT v1r5 calculations, independent of intake, NIST and presentation."""

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import Mapping

from assessment_evidence import AssessmentEvidence, Evidence, EvidenceStatus


METHODOLOGY_ID = "DDS-SRAT"
METHODOLOGY_VERSION = "v1r5"
IMPLEMENTATION_VERSION = "1.0.0"
WORKBOOK_SHA256 = "20d716ee47e4b504a218f28ad978454d863135ca66dc8e46ae319cb58465053c"
VARIABLES = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X")


class AssessmentStatus(str, Enum):
    NOT_ASSESSED = "Not Assessed"
    IN_PROGRESS = "In Progress"
    ASSESSED = "Assessed"
    NA_PENDING = "Not Applicable - Pending Review"
    NA_APPROVED = "Not Applicable - Approved"


class Classification(str, Enum):
    LOW = "LOW"
    LOW_MEDIUM = "LOW MEDIUM"
    MEDIUM = "MEDIUM"
    MEDIUM_HIGH = "MEDIUM HIGH"
    HIGH = "HIGH"
    UNCLASSIFIED = "UNCLASSIFIED - source band missing for 26"
    PROVISIONAL_NA = "PROVISIONAL - N/A classification policy pending CISO approval"
    NO_APPLICABLE = "NO APPLICABLE CATEGORIES - reviewer/CISO review required"
    INVALID = "INVALID - not an integer total in 10-30"


@dataclass(frozen=True)
class Variable:
    identifier: str
    name: str
    worksheet: str
    score_cell: str
    scoring_cells: tuple[str, ...]
    context_cells: tuple[str, ...] = ()

    @property
    def required_cells(self) -> tuple[str, ...]:
        return self.context_cells + self.scoring_cells


def _cells(first: int, last: int) -> tuple[str, ...]:
    return tuple(f"B{row}" for row in range(first, last + 1))


VARIABLE_DEFINITIONS = (
    Variable("I", "Vendor risk management", "VARIABLE I", "D6", _cells(3, 5)),
    Variable("II", "Compliance and certifications", "VARIABLE II", "D9", _cells(3, 8)),
    Variable("III", "PHI/PII exposure and encryption", "VARIABLE III", "D7", _cells(3, 6)),
    Variable("IV", "Alerts and vulnerability management", "VARIABLE IV", "D9", _cells(3, 8)),
    Variable("V", "Vendor security/privacy practices", "VARIABLE V", "D8", _cells(3, 7)),
    Variable("VI", "Sensitive-data safeguards", "VARIABLE VI", "D11", _cells(3, 10)),
    Variable("VII", "Third parties and APIs", "VARIABLE VII", "D9", _cells(3, 8)),
    Variable("VIII", "Adversarial robustness", "VARIABLE VIII", "D5", _cells(3, 4)),
    Variable("IX", "Vendor viability/support", "VARIABLE IX", "D6", _cells(3, 5)),
    Variable("X", "Generative AI", "VARIABLE X (GenAI QUESTIONS)", "D20",
             ("B14", "B19"), _cells(3, 10)),
)

QUESTION_TOPICS = {
    "I": ("Risk policy", "Risk program", "Annual organization-wide risk assessment"),
    "II": ("GDPR compliance", "HIPAA compliance", "CCPA compliance", "SOC 2 Type 2",
           "Product ADA/508 accessibility", "Deliverables ADA/508 accessibility"),
    "III": ("PHI/PII stored or processed", "PHI/PII encryption",
            "AES-256 minimum at rest", "TLS 1.3 minimum with secure ciphers in transit"),
    "IV": ("Patch/security alerts", "Database monitoring and alarms", "Regular updates/patch process",
           "Automatic patching", "Client-accessible update documentation", "Vulnerability policy/process"),
    "V": ("NIST SP 800-53/framework adherence", "California collection/privacy notices where applicable",
          "FIPS", "Uptime/availability/incident-response SLAs", "Backup/recovery/location/migration details"),
    "VI": ("Sensitive-data encryption at rest/in transit", "Access controls", "Vendor privacy impact assessment",
           "DDS data not shared with third parties", "Published access-control policy", "Daily database backups",
           "Disaster recovery plan", "Incident response plan"),
    "VII": ("No external transfer and encryption", "External transfer with encryption",
            "Documented third parties/API protections", "No third-party integrations",
            "SaaS on a major cloud provider", "Vendor security questionnaire"),
    "VIII": ("Documented robustness/resilience evaluation and benchmarks",
             "Adversarial findings used for model improvement and safeguards"),
    "IX": ("Reputation/support/training track record", "Public ratings average four to five stars",
           "Continuous application/data/infrastructure/network/organization/product security monitoring"),
    "X": ("AI performance training/validation", "Sensitive-data encryption/access/anonymization",
          "Independent bias audit and representative training", "AI transparency/explainability",
          "Enterprise cloud integrations", "LLM identity/details", "Ethics/privacy/human-rights evaluation",
          "Enterprise private-repository data handling", "SIMM 5310-C PTA/PIA completed",
          "PIA risk level: Low, Medium or High"),
}


@dataclass(frozen=True)
class QuestionResponse:
    cell: str
    response: str | None = None
    evidence_references: tuple[str, ...] = ()


@dataclass(frozen=True)
class CategoryAssessment:
    variable_id: str
    responses: tuple[QuestionResponse, ...] = ()
    status: AssessmentStatus = AssessmentStatus.NOT_ASSESSED
    reviewer: str | None = None
    review_date: date | None = None
    reduction_justification: str = ""
    na_justification: str = ""


def _initial_categories() -> tuple[CategoryAssessment, ...]:
    return tuple(CategoryAssessment(variable) for variable in VARIABLES)


@dataclass(frozen=True)
class SratAssessment:
    assessment_id: str
    categories: tuple[CategoryAssessment, ...] = field(default_factory=_initial_categories)
    evidence: tuple[Evidence, ...] = ()
    genai_use: bool | None = None


@dataclass(frozen=True)
class CategoryResult:
    variable_id: str
    name: str
    raw_score: int
    effective_score: int | None
    assessment_status: AssessmentStatus
    complete: bool
    evidence_status: EvidenceStatus
    reviewer: str | None
    review_date: date | None
    reviewer_comments: str
    excluded: bool
    gaps: tuple[str, ...]
    evidence_records: tuple[AssessmentEvidence, ...]


@dataclass(frozen=True)
class SratResult:
    assessment_id: str
    categories: tuple[CategoryResult, ...]
    total: int | None
    classification: Classification
    provisional: bool
    applicable_count: int
    excluded_variables: tuple[str, ...]
    gaps: tuple[str, ...]
    methodology_id: str = field(default=METHODOLOGY_ID, init=False)
    methodology_version: str = field(default=METHODOLOGY_VERSION, init=False)
    implementation_version: str = field(default=IMPLEMENTATION_VERSION, init=False)


def _answer(value: str | None) -> str:
    return value.casefold() if isinstance(value, str) else ""


def worksheet_score(variable_id: str, responses: Mapping[str, str | None]) -> int:
    """Reproduce each guarded worksheet D-cell, before SAR evidence gating."""
    definition = next((item for item in VARIABLE_DEFINITIONS if item.identifier == variable_id), None)
    if definition is None:
        raise ValueError(f"Unknown SRAT variable: {variable_id}")
    if any(responses.get(cell) in (None, "") for cell in definition.scoring_cells):
        return 3
    answers = {cell: _answer(responses.get(cell)) for cell in definition.scoring_cells}
    yes = sum(answer == "yes" for answer in answers.values())
    if variable_id == "I":
        return 1 if yes == 3 else 2 if 1 <= yes < 3 else 3
    if variable_id == "II":
        return 1 if yes == 6 else 2 if 1 <= yes < 6 else 3
    if variable_id == "III":
        if answers["B3"] == "no":
            return 1
        return 1 if yes == 4 else 2 if 2 <= yes < 4 else 3
    if variable_id == "IV":
        return 1 if yes == 6 else 2 if 1 <= yes < 6 else 3
    if variable_id == "V":
        return 1 if yes == 5 else 2 if 1 <= yes < 5 else 3
    if variable_id == "VI":
        return 1 if yes == 8 else 2 if 1 <= yes < 8 else 3
    if variable_id == "VII":
        return 1 if yes == 6 else 2 if 1 <= yes < 6 else 3
    if variable_id == "VIII":
        return 1 if yes == 2 else 2 if yes == 1 else 3
    if variable_id == "IX":
        return 1 if yes == 3 else 2 if 1 <= yes < 4 else 3
    if answers["B14"] != "yes":
        return 3
    return {"low": 1, "medium": 2, "high": 3}.get(answers["B19"], 3)


def classify_total(total: object) -> Classification:
    """Source A33 bands, only within the all-ten-applicable integer domain."""
    if type(total) is not int or not 10 <= total <= 30:
        return Classification.INVALID
    if total == 10:
        return Classification.LOW
    if total <= 15:
        return Classification.LOW_MEDIUM
    if total <= 20:
        return Classification.MEDIUM
    if total <= 25:
        return Classification.MEDIUM_HIGH
    if total == 26:
        return Classification.UNCLASSIFIED
    return Classification.HIGH


def _evidence_status(references: tuple[str, ...], evidence: Mapping[str, Evidence]) -> EvidenceStatus:
    if not references or any(reference not in evidence for reference in references):
        return EvidenceStatus.NOT_PROVIDED
    items = tuple(evidence[reference] for reference in references)
    if any(item.verification_status == EvidenceStatus.REJECTED for item in items):
        return EvidenceStatus.REJECTED
    if any(item.verification_status == EvidenceStatus.NOT_PROVIDED for item in items):
        return EvidenceStatus.NOT_PROVIDED
    if all(item.supports_reduction for item in items):
        return EvidenceStatus.VALIDATED
    return EvidenceStatus.REPORTED


def _valid_response(variable_id: str, cell: str, value: str | None) -> bool:
    allowed = ("low", "medium", "high") if variable_id == "X" and cell == "B19" else ("yes", "no")
    return _answer(value) in allowed


def _evaluate_category(
    category: CategoryAssessment,
    definition: Variable,
    assessment: SratAssessment,
    evidence: Mapping[str, Evidence],
) -> CategoryResult:
    if not isinstance(category.status, AssessmentStatus):
        raise ValueError(f"{category.variable_id}: invalid assessment status")
    responses = {response.cell: response for response in category.responses}
    if len(responses) != len(category.responses) or set(responses) - set(definition.required_cells):
        raise ValueError(f"{category.variable_id}: duplicate or unknown question cell")
    raw = worksheet_score(category.variable_id, {cell: item.response for cell, item in responses.items()})
    reviewed = bool(category.reviewer and category.reviewer.strip()) and type(category.review_date) is date
    gaps = []
    excluded = False
    if category.status == AssessmentStatus.NA_APPROVED:
        excluded = (
            reviewed and bool(category.na_justification.strip())
            and (category.variable_id != "X" or assessment.genai_use is False)
        )
        if not excluded:
            gaps.append("N/A approval lacks reviewer/date/basis or conflicts with GenAI scope")
    if category.status == AssessmentStatus.NA_PENDING:
        gaps.append("N/A pending review; category remains applicable at HIGH")
    if category.variable_id == "X" and not excluded and assessment.genai_use is not True:
        gaps.append("GenAI scope unknown or absent; explicit applicability review required")

    question_states = []
    valid_answers = True
    for cell in definition.required_cells:
        response = responses.get(cell, QuestionResponse(cell))
        status = _evidence_status(response.evidence_references, evidence)
        question_states.append((response, status))
        if not excluded:
            if not _valid_response(category.variable_id, cell, response.response):
                valid_answers = False
                gaps.append(f"{cell}: unanswered/unknown/N/A/invalid response")
            if status != EvidenceStatus.VALIDATED:
                gaps.append(f"{cell}: supporting evidence not validated ({status.value})")

    statuses = tuple(status for _, status in question_states)
    if EvidenceStatus.REJECTED in statuses:
        evidence_status = EvidenceStatus.REJECTED
    elif EvidenceStatus.NOT_PROVIDED in statuses:
        evidence_status = EvidenceStatus.NOT_PROVIDED
    elif all(status == EvidenceStatus.VALIDATED for status in statuses):
        evidence_status = EvidenceStatus.VALIDATED
    else:
        evidence_status = EvidenceStatus.REPORTED
    complete = category.status == AssessmentStatus.ASSESSED and valid_answers
    if not excluded:
        if category.status != AssessmentStatus.ASSESSED:
            gaps.append(f"Assessment status: {category.status.value}")
        if not reviewed:
            gaps.append("Reviewer determination and review date required")
        if raw < 3 and not category.reduction_justification.strip():
            gaps.append("Score-reduction justification required")
    can_reduce = (
        complete and evidence_status == EvidenceStatus.VALIDATED and reviewed
        and bool(category.reduction_justification.strip())
        and (category.variable_id != "X" or assessment.genai_use is True)
    )
    effective = None if excluded else raw if can_reduce and type(raw) is int and raw in (1, 2, 3) else 3
    records = tuple(
        AssessmentEvidence(
            assessment.assessment_id, METHODOLOGY_ID, METHODOLOGY_VERSION,
            category.variable_id, f"{category.variable_id}.{response.cell}", response.response,
            response.evidence_references, status, raw, effective, category.status.value,
            category.reviewer, category.review_date, category.reduction_justification,
        )
        for response, status in question_states
    )
    return CategoryResult(
        category.variable_id, definition.name, raw, effective, category.status, complete,
        evidence_status, category.reviewer, category.review_date,
        "; ".join(comment for comment in (
            category.reduction_justification,
            f"N/A basis: {category.na_justification}" if category.na_justification else "",
        ) if comment),
        excluded, tuple(gaps), records,
    )


def assess(assessment: SratAssessment) -> SratResult:
    """Return a new SRAT-only result; never accept or mutate other methodologies."""
    if not assessment.assessment_id.strip():
        raise ValueError("Assessment identifier required")
    if assessment.genai_use is not None and type(assessment.genai_use) is not bool:
        raise ValueError("GenAI use must be True, False or None")
    categories = {category.variable_id: category for category in assessment.categories}
    if len(assessment.categories) != 10 or set(categories) != set(VARIABLES):
        raise ValueError("Exactly one category for each SRAT variable I-X is required")
    evidence = {item.reference: item for item in assessment.evidence}
    if len(evidence) != len(assessment.evidence) or any(not reference.strip() for reference in evidence):
        raise ValueError("Evidence references must be unique and nonempty")
    results = tuple(
        _evaluate_category(categories[definition.identifier], definition, assessment, evidence)
        for definition in VARIABLE_DEFINITIONS
    )
    applicable = tuple(result for result in results if not result.excluded)
    excluded = tuple(result.variable_id for result in results if result.excluded)
    scores = []
    for result in applicable:
        value = result.effective_score
        if type(value) is not int or value not in (1, 2, 3):
            raise ValueError(f"{result.variable_id}: invalid effective SRAT score")
        scores.append(value)
    total = sum(scores) if scores else None
    classification = (
        Classification.NO_APPLICABLE if not applicable
        else Classification.PROVISIONAL_NA if excluded
        else classify_total(total)
    )
    gaps = tuple(f"{result.variable_id}: {gap}" for result in results for gap in result.gaps)
    if excluded:
        gaps += ("Approved N/A excluded from sum; reduced-scope classification awaits CISO aggregation policy.",)
    if classification == Classification.UNCLASSIFIED:
        gaps += ("Source A33 leaves 26 unclassified; proposed >=26 correction is not approved.",)
    provisional = bool(gaps) or classification in (
        Classification.INVALID, Classification.NO_APPLICABLE, Classification.PROVISIONAL_NA,
    )
    return SratResult(
        assessment.assessment_id, results, total, classification, provisional,
        len(applicable), excluded, gaps,
    )
