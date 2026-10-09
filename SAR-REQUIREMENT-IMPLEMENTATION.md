# SAR Requirement Governance Mechanism

**SAR-CODEX-070 | PROVISIONAL IMPLEMENTATION FOR CISO REVIEW**

This increment implements a small structural mechanism for Requirement governance records. It does not create an operational Requirement Catalog, approve the SI-12(3) Requirement, decide applicability, or execute assessment logic. The CISO-approved principles are design authority; schema and validator details here are provisional implementation choices awaiting review.

## Files

- `schemas/sar-requirement-record.schema.json` - JSON Schema Draft 2020-12 for a provisional Requirement governance record.
- `requirements/examples/si-12-3.proposed.yaml` - non-operational SI-12(3) proposal with unresolved parameter and applicability.
- `tools/validate_requirement.py` - deterministic schema and pinned-artifact/candidate-reference validator plus read-only readiness report.
- `tests/requirements/test_validate_requirement.py` - focused offline `unittest` coverage.

The existing validated candidate and pinned source artifacts are read-only inputs. No governed model, candidate, source manifest, or Requirement Catalog was modified or created.

## Record Structure

The schema requires separate sections for:

- `identity`: logical ID and immutable version fields;
- `lifecycle`: governance state, currentness state, and predecessor/successor references;
- `source_provenance`: source family/version/revision/path, source object/parts, validated Candidate Boundary, and source relationships;
- `normative_content`: source-bound obligation reference, controlled representation, and parameter dependencies;
- `governance`: review state and distinct Requirement approval state/record;
- `applicability`: unresolved status and source-role state;
- `execution_boundary`: non-executable state and blocked parameter-dependent evaluation; and
- `history`: typed, dated provenance events.

The schema rejects extra fields, including applicability determinations, findings, severity, risk decisions, or authorization fields. Its built-in approval constraints require a compatible lifecycle/review state and a structured Requirement-governance decision record. A source-boundary validation reference is a separate object and cannot satisfy the Requirement approval record.

`record_context: GOVERNANCE_RECORD` identifies the intended record form only; it does not register a record in an operational catalog or prove that an approval is authentic. The checked-in SI-12(3) record remains `NON_OPERATIONAL_EXAMPLE`.

## Identifier and Lifecycle

The example uses `EXAMPLE-REQ-0001` and `EXAMPLE-VERSION-1` only as conspicuously provisional placeholders. This is not production syntax and is not derived from `SI-12(3)` or the Candidate Boundary ID. The approved design principle is a stable opaque logical identity plus a separate immutable version; production grammar and allocation authority remain undecided.

The schema's provisional lifecycle values are `PROPOSED`, `HUMAN_REVIEWED`, `APPROVED`, `REJECTED`, `SUPERSEDED`, and `RETIRED`. Currentness is a separate field. These field names/enumerations are implementation choices for review, not a production policy. Historical revisions and approval decisions should be appended/preserved rather than overwritten.

## SI-12(3) Example

The YAML record references:

- Candidate Boundary `cbr-nist-sp800-53-rev5-si-12-3-smt`, status `VALIDATED`;
- NIST SP 800-53 Rev. 5 OSCAL release `5.2.0`, pinned commit `78650f02ad9321bb7b817846f8fbd4f2bcd620de`;
- source object `si-12.3`, normative part `si-12.3_smt`;
- parameter `si-12.3_prm_1`, state `UNRESOLVED`; and
- source relationship `si-12.3 --required--> #si-12`.

The example lifecycle is `PROPOSED`, Requirement approval is `NOT_APPROVED`, applicability is `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`, and execution is `NON_EXECUTABLE`. The controlled representation is a summary linked to the exact normative source reference and approved boundary record; it supplies no technique or retention period.

## Approval Record

For a future human Requirement decision, the schema requires a decision (`APPROVE` or `REJECT`), authority, ISO date, scope fixed to `REQUIREMENT_GOVERNANCE_ONLY`, exact logical ID/version, decision provenance, and a decision reference. Approval requires `HUMAN_REVIEWED` plus an explicit approval record and a corresponding history event. A boundary-fidelity approval is explicitly scoped `SOURCE_BOUNDARY_FIDELITY_ONLY` and is not accepted as Requirement approval. No real Requirement approval is recorded in the example.

Approved-state tests construct only an in-memory `SYNTHETIC_TEST_FIXTURE`, labeled with a non-real authority and decision reference. It is never written as a record or included in the example.

## Validator and Readiness

Run the structural validator with its default repository paths:

```powershell
python tools/validate_requirement.py
```

Override inputs if needed:

```powershell
python tools/validate_requirement.py --requirement requirements/examples/si-12-3.proposed.yaml --requirement-schema schemas/sar-requirement-record.schema.json --source-manifest sources/nist-sp800-53-rev5.oscal-source.yaml --candidate-set sources/nist-sp800-53-rev5.si-12.candidate-boundaries.yaml --source-slice sources/nist-sp800-53-rev5.ac-2-si-12.slice.yaml
```

It checks schema conformance; manifest/candidate/source object identity; candidate existence and `VALIDATED` state; source object, part, parameter, and parent relationship consistency; approval/lifecycle/history consistency; unresolved parameter representation; and structurally valid, non-self-referential supersession references. It does not fetch network resources or modify any record.

The dry-run readiness summary uses validator-process statuses, not SAR assessment/lifecycle decisions:

- `BLOCKED`: structural errors exist;
- `HUMAN_REQUIREMENT_REVIEW_REQUIRED`: record is structurally consistent but lacks recorded human review/approval prerequisites;
- `HUMAN_REQUIREMENT_APPROVAL_REQUIRED`: human review is recorded but Requirement approval is not;
- `APPROVAL_ALREADY_RECORDED_NO_CHANGE`: an approval record is already present; no action or transition is performed.

For the SI-12(3) example, expected readiness is `HUMAN_REQUIREMENT_REVIEW_REQUIRED`. The tool never changes lifecycle, creates an approval, assigns parameters, selects systems, or makes a promotion decision. Unresolved organization-defined values are permitted in the Requirement representation under approved design; any evaluation that depends on one remains blocked until a properly authorized, scoped, versioned assignment and a separate governed rule exist.

## Tests

Run the focused offline suite:

```powershell
python -m unittest discover -s tests/requirements -v
```

The tests cover valid proposed structure, identity/version omissions, candidate/source/part/parameter/relationship mismatches, non-validated candidates, approval-state inconsistencies, synthetic approval structure, unresolved-versus-assigned parameter conflicts, malformed source revision, invalid self-supersession, readiness blockers, and dry-run non-mutation.

## Limitations and Remaining Governance

A passing structural validation does not constitute CISO Requirement approval, applicability determination, compliance validation, or deployment authorization.

The mechanism cannot determine semantic normative fidelity, approve an interpretation, establish that a source applies, validate a parameter assignment's organizational authority, define safeguards/evidence, or decide whether evidence is sufficient. It depends on the already validated source boundary and the checked-in source snapshot/slice. It has no Requirement Catalog, database, signatures, trusted approver authentication, approval workflow, impact-analysis engine, or execution integration.

Still unresolved are production Requirement ID syntax; final schema design/versioning; owner and delegated approver roles; approval capture/authentication and effective-date mechanics; parameter owner/source/scope/value; assessment-specific authority-versus-benchmark role and applicability rules; safeguard expectations; evidence-validation criteria; change-impact policy; and any deterministic comparison semantics. This increment deliberately does not implement them.

## CISO Implementation Checkpoint Decision

| Decision field | Record |
|---|---|
| Authority | DDS CISO |
| Decision | **APPROVED FOR NON-OPERATIONAL IMPLEMENTATION CHECKPOINT** |
| Additional conditions | None |
| Scope | The five SAR-CODEX-070 implementation artifacts listed in the Files section above |
| Workflow reference | SAR-CODEX-070 |
| Decision provenance | Explicit CISO approval in the SAR-CODEX-070 review conversation |
| Decision date | **UNRESOLVED - no explicit date was included in the approval record** |

This disposition authorizes a controlled repository checkpoint of the reviewed implementation only. It does not authorize production Requirement identifier syntax or catalog population, approval of the SI-12(3) Requirement, parameter assignment, applicability determination, safeguard/evidence evaluation, findings, risk scoring or acceptance, deployment authorization, or assessment execution.

The implementation checkpoint approval is distinct from both the earlier SI-12(3) **source-boundary fidelity** approval and any future human approval of the SI-12(3) SAR Requirement. The example remains `PROPOSED`, `NOT_APPROVED`, and `NON_EXECUTABLE`; no Requirement approval record is created by this checkpoint decision.
