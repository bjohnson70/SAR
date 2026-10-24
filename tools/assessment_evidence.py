"""Shared evidence references; methodology-specific decisions remain separate."""

from dataclasses import dataclass
from datetime import date
from enum import Enum


class EvidenceStatus(str, Enum):
    NOT_PROVIDED = "Not Provided"
    REPORTED = "Reported - Not Verified"
    VALIDATED = "Validated"
    REJECTED = "Rejected"


@dataclass(frozen=True)
class Evidence:
    reference: str
    source: str
    location: str
    verification_status: EvidenceStatus = EvidenceStatus.REPORTED
    verified_by: str | None = None
    verification_date: date | None = None

    @property
    def supports_reduction(self) -> bool:
        return (
            self.verification_status == EvidenceStatus.VALIDATED
            and bool(self.source.strip())
            and bool(self.location.strip())
            and bool(self.verified_by and self.verified_by.strip())
            and type(self.verification_date) is date
        )


@dataclass(frozen=True)
class AssessmentEvidence:
    assessment_id: str
    methodology_id: str
    methodology_version: str
    variable_id: str
    question_id: str
    response: str | None
    evidence_references: tuple[str, ...]
    evidence_status: EvidenceStatus
    raw_score: int
    effective_score: int | None
    assessment_status: str
    reviewer: str | None
    review_date: date | None
    reduction_justification: str
