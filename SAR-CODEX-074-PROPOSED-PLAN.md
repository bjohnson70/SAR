# SAR-CODEX-074 Proposed Plan

**STATUS: PROPOSED - NOT AUTHORIZED TO EXECUTE**

This plan follows the SAR-CODEX-073 non-operational registry contract increment. It is a proposal only and grants no authority to create a production registry, issue identities/versions, approve Requirements, or enable assessment execution.

## Objectives

- Select and document the technology-neutral registry system-of-record boundary.
- Implement persistence and transactional-or-equivalent registration against SAR-CODEX-073 contracts.
- Provide deterministic identity/version allocation, idempotency, and safe concurrency handling.
- Persist append-only lifecycle events and immutable content references without conflating registration with approval or eligibility.
- Provide import/export, recovery, reconciliation, and audit capabilities.

## Dependencies

- DDS CISO disposition on production logical-ID syntax and uniqueness namespace/issuer model.
- DDS CISO disposition on whether the SAR-CODEX-073 RFC 8785/SHA-256 profile is suitable for production and whether its exact envelope fields are approved.
- Named registry authority/operator and authorized organization/delegation model.
- Approved lifecycle event authority, event retention, withdrawal/supersession effects, and source currentness/effective-time rules.
- Approved storage/deployment and operational security, records-retention, recovery, availability, and audit requirements.
- Approved migration authority and SI-12(3) migration procedure; migration remains separate from Requirement approval.

## Implementation Tasks

1. Confirm the reviewed v1 schema/profile and resolve any CISO decisions before production persistence.
2. Specify registry API or repository contract, authorization boundary, idempotency semantics, atomicity guarantees, concurrency/conflict handling, and operational error model.
3. Select a deployment/storage implementation only after comparing it against technology-neutral guarantees; no database/cloud option is presumed.
4. Implement transactional-or-equivalent identity and sequential version registration with unique constraints, append-only event writes, and immutable content references.
5. Implement safe retry, partial-failure recovery, backup/restore, import/export, and reconciliation without silently merging or rewriting records.
6. Integrate authenticated identity/delegation checks for operations that require them; keep the registry custodian distinct from human Requirement approval authority.
7. Add lifecycle projections that never infer approval/currentness from newest version and never enable assessment execution.
8. Develop an independently authorized migration process for provisional examples; preserve source provenance and all unresolved/non-executable boundaries.

## Security Constraints

- Allocation and registration are not authorization to use or approve a Requirement.
- Human approval evidence must bind verified human identity/authority, exact identity/version, and exact content digest; the persistence service cannot self-assert approval.
- Source-fidelity validation, Requirement approval, parameter authorization, source authority/benchmark role, applicability, and execution eligibility remain separate.
- Enforce unique identity/version keys, immutable prior content, referential integrity, append-only history, idempotent retry, concurrency control, and import collision quarantine.
- Do not add a concrete storage technology unless selected and reviewed under approved deployment decisions.
- No production Requirement may be promoted or executable under this plan by default.

## Acceptance Criteria

- Concurrent registration produces no duplicate logical IDs or `(logical ID, version)` keys.
- Replaying the same idempotency key/request returns the same result; a changed payload using that key is rejected and audited.
- Failed/partial writes cannot expose an issued record with missing content or lifecycle history.
- Existing versions/events cannot be mutated or removed through supported operations.
- Every new reference resolves, content digests verify under the approved profile, and lifecycle history reconciles deterministically.
- Import/export preserves identity, exact version, content bytes/digest, source/Candidate Boundary provenance, and history; collisions are quarantined.
- No registration path can set `APPROVED`, assign parameters, create applicability, or enable assessment execution.
- Recovery, rollback detection, backup restoration, and audit export are tested before operational use.

## Test Strategy

- Unit tests for allocation uniqueness, monotonic version sequences, immutable writes, exact content digest, event order, and idempotency.
- Concurrency/property tests with simultaneous identity/version requests and forced collision simulation.
- Fault-injection tests across transaction boundaries, content storage, event persistence, retries, and acknowledgments.
- Import/export round-trip and collision/quarantine tests across contract/schema versions.
- Security tests for unauthorized principal/delegation, forged/misbound approval evidence, event mutation, rollback, and administrator separation.
- Migration rehearsal with synthetic data first; any SI-12(3) migration remains non-operational until separately authorized.
- Recovery/restore tests and independent reconciliation checks.

## Estimated Complexity

**High.** Transactional identity/version allocation, tamper-resistant append-only history, identity/delegation integration, failure recovery, and portable migration span data, security, operational controls, and audit. A limited prototype may be medium complexity but would not satisfy production acceptance criteria.

## Decisions Requiring CISO Authorization

- Exact production UUID representation and global versus issuer-qualified uniqueness domain.
- Registry authority, participating organizations, named operator, and delegation scope.
- Whether RFC 8785/JCS with the SAR-CODEX-073 field boundary and SHA-256 profile is accepted for production use.
- Lifecycle vocabulary, event authorization, effective/current semantics, and supersession/withdrawal effects.
- Storage/deployment technology, retention, recovery objectives, audit controls, and operational risk ownership.
- Import/export trust and cross-organization identity adoption/collision policy.
- Authority and procedure for migrating any existing example into a production registry.
- Any production Requirement approval, parameter assignment, applicability, or execution eligibility remains a separate human-governed decision.

**STOP POINT:** SAR-CODEX-074 is proposed only. Do not begin implementation until separately authorized.
