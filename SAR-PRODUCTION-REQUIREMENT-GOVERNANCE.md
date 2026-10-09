# Production SAR Requirement Governance

**SAR-CODEX-071 | APPROVED GOVERNANCE DESIGN**

> **APPROVED - GOVERNANCE DESIGN ONLY - NOT AN OPERATIONAL WORKFLOW**

This document records the DDS CISO's approval of the SAR production Requirement governance design, subject to the three binding clarifications in the decision register. It defines governance direction, not an operational workflow or implementation. It creates no Requirement, Requirement approval event, schema change, applicability decision, parameter assignment, assessment rule, or execution authority. Implementation choices expressly identified as unresolved remain open.

## 1. Purpose and Authority Boundary

Design a trustworthy production path from a human-validated Candidate Requirement Boundary to a governed SAR Requirement. The focus is authorization and provenance, not assessment implementation.

Preserve the following distinct decisions and objects:

```text
Source Content
    != Candidate Requirement Boundary
    != SAR Requirement
    != Assessment Applicability
    != Safeguard / Evidence Evaluation
    != Human Risk Acceptance
```

The SAR-CODEX-068 DDS CISO decision approved only SI-12(3) boundary fidelity to the pinned NIST source. SAR-CODEX-069 approved five Requirement-governance design principles only. SAR-CODEX-070 approved a non-operational repository implementation checkpoint only. None approves the SI-12(3) Requirement, an applicability basis, an implementation or evidence expectation, compliance, risk acceptance, deployment, or assessment execution.

The SAR-CODEX-070 checkpoint record states `APPROVED FOR NON-OPERATIONAL IMPLEMENTATION CHECKPOINT`, with no additional conditions and scope limited to five implementation artifacts. Its decision date is unresolved because no explicit date was supplied. That checkpoint is not production deployment approval and is not authenticated Requirement approval evidence by itself.

The SAR-CODEX-071 design decision is recorded in Section 14. It does not approve SI-12(3) or any other Requirement, assign a parameter, establish applicability, or authorize assessment execution.

## 2. Existing Approved Governance

### Existing approved principles

- Source, Candidate Requirement Boundary, Requirement, Applicability Basis, Control/Safeguard, Evidence, Finding, and Risk Decision are distinct.
- Only a human-validated Candidate Requirement Boundary may be the basis for a governed SAR Requirement.
- Requirement governance approval, when separately performed, establishes normative representation and source provenance only. It does not establish assessment applicability or downstream assessment conclusions.
- A Requirement may retain unresolved organization-defined parameters; evaluation depending on an unassigned parameter must remain blocked.
- Promotion design requires source/boundary provenance, normative fidelity review, controlled identity/version, human Requirement review and approval, and change/supersession history.
- Human authorization is required for Requirement approval. AI output, structural validation, repository contribution, or an automated readiness result cannot substitute for the human decision.
- Historical versions and decisions must remain traceable and must not be silently rewritten.
- Approval authority must be configurable for each authorized organization and may include formally delegated approvers under recorded authority and scope.
- Approval evidence must be identity-backed and verified, and bound to the exact Requirement identity, immutable version, content integrity, and authorized human decision.
- Assessment execution eligibility is governed independently from Requirement approval, applicability, currentness, source authority, and parameter resolution.

These principles derive from SAR-CODEX-068/069/070 and the SAR-CODEX-071 approved design. The clarifications above are binding design requirements. They do not settle production ID syntax, specific delegated approver assignments, identity proofing technology, signature mechanisms, exact lifecycle vocabulary, or workflow implementation.

### Provisional implementation, not production policy

The committed `schemas/sar-requirement-record.schema.json`, `tools/validate_requirement.py`, example, tests, and `SAR-REQUIREMENT-IMPLEMENTATION.md` are provisional SAR-CODEX-070 implementation artifacts. The schema's `0.1-provisional` label, `EXAMPLE-REQ-0001`, `EXAMPLE-VERSION-1`, lifecycle strings, readiness output labels, and approval-record shape are implementation choices for review. They are not approved production identifier syntax, a trusted identity system, an operational Requirement Catalog, or an authentication/authorization service.

## 3. Current Implementation Baseline

The repository has no populated operational Requirement Catalog and no production Requirement ID convention or trusted approval service. The current Requirement schema validates record structure and cross-checks the pinned source manifest, candidate set, and local source slice. It does not authenticate a decision maker, verify delegation, prove signature integrity, establish semantic correctness, or create a governed state transition.

The SI-12(3) example remains `NON_OPERATIONAL_EXAMPLE`, `PROPOSED`, `NOT_APPROVED`, and `NON_EXECUTABLE`. It references Candidate Boundary `cbr-nist-sp800-53-rev5-si-12-3-smt` in state `VALIDATED`, NIST SP 800-53 Rev. 5 OSCAL release `5.2.0`, pinned upstream revision `78650f02ad9321bb7b817846f8fbd4f2bcd620de`, source object `si-12.3`, part `si-12.3_smt`, parameter `si-12.3_prm_1`, and parent relationship `si-12.3 --required--> #si-12`. Its applicability is `UNRESOLVED / GOVERNED RULE NOT YET POPULATED` and its assessment-specific source role is `NOT_DETERMINED`.

The approved source-boundary decision is not Requirement approval. The provisional approval-record fields do not themselves establish authenticated authority; a test fixture with a synthetic approver is not evidence of a real decision.

## 4. Identity Alternatives and Approved Design

| Strategy | Benefits | Risks / limitations |
|---|---|---|
| Opaque SAR-managed logical ID | Independent of publisher numbering and wording; stable across source revisions; works for multiple Requirements from one provision, and Requirements related to multiple sources; machine-friendly. | Requires an authorized allocator/registry and duplicate prevention; less human-readable without linked source metadata. |
| Source-derived ID | Immediately recognizable and easy to inspect. | Couples identity to publisher numbering and source family; can collide across source families/versions; problematic for split/merge, multiple Requirements from one provision, multiple-source Requirements, or replacement sources. |
| Composite source/Requirement ID | Embeds source context and may be readable. | Can become unstable when source bindings change; can imply one source per Requirement; grows awkward after split/merge or multi-source provenance; embeds an unsettled grammar. |

### Approved governance design direction

Adopt an **opaque SAR-managed logical Requirement ID**, independent of NIST numbering or any source key, and a separate immutable version identity. Human-readable source labels and citations remain separate fields. A logical identity should remain stable through source updates when the conceptual Requirement continues; a materially different, split, or merged Requirement receives new logical identity/relationship as an approved succession decision.

This approach supports global uniqueness through an authorized central allocator and uniqueness constraint; duplicate prevention must be enforced atomically. It permits multiple Requirements from one source provision and Requirements related to multiple sources without encoding a single-source assumption in the ID. A source replacement or withdrawal changes provenance/currentness and may trigger a new version or successor, but does not recycle or rewrite the logical ID. The ID is machine-stable; human readability comes from separately displayed source/title/provision metadata. Identity is immutable once issued.

For adoption by multiple authorized organizations, the governance layer must provide one global allocation authority/registry or centrally registered issuer namespaces with collision checks across participating namespaces. A local sequence with no shared uniqueness control is insufficient. This design principle does not require embedding an organization or source identifier into the logical ID itself.

For implementation discussion only, a random UUID-sized identifier is one possible allocation format. This is not an adopted format. Do not use `EXAMPLE-REQ-0001`, a NIST control number, or a Candidate Boundary ID as a production Requirement ID.

**Versioning design:** treat `(logical_requirement_id, version)` as the stable lookup pair; assign a monotonically increasing revision number within the logical identity (for example, `1`, `2`) after version syntax is separately governed. Each version is immutable and binds the exact source/candidate revisions and normative representation. A content digest may additionally bind bytes but must not replace logical ID/version or source references. Do not assume SemVer semantics unless separately approved.

**Uniqueness and allocation:** a future authorized Requirement Registry or allocation service must atomically reject duplicate logical IDs and duplicate `(logical ID, version)` pairs. Allocation authority belongs to a designated SAR governance custodian/service role under a CISO-approved delegation. This repository increment does not allocate IDs or build that registry.

## 5. Versioning and Supersession

### Approved governance design direction

- First proposed Requirement record starts at version 1 only after its logical identity is authorized; proposal versions must also be immutable once referenced or reviewed.
- Normative text, semantic role, scope, conditions, exceptions, source-part binding, parameter dependency set, or source-role representation change creates a new immutable Requirement version and a new human review/approval decision before that version is usable as approved content.
- A source revision never silently rewrites an existing Requirement. Pin and compare the new source; record materiality review. If source binding changes, create a new Requirement version even if a reviewer concludes the obligation is substantively unchanged, so the exact source basis remains reproducible. Reapproval is required when normative meaning, scope, parameter dependency, or approval conditions change; CISO should decide whether source-binding-only revisions also require reapproval.
- A Candidate Boundary correction/revision requires its own human boundary validation. A Requirement version may not point back to a superseded or unvalidated boundary as its current approved basis.
- Newly assigned/changed parameter values belong in separately versioned assignment records. They do not rewrite the source definition. A new Requirement version is needed only if the normative dependency itself changes, not merely because a valid assignment changes.
- Provenance correction that changes what source, candidate, part, or digest was actually reviewed requires a new version or a reapproval event according to materiality; never overwrite the old binding. Pure clerical metadata correction that does not change meaning or identity may be an append-only governance correction event, preserving the original value and correction rationale.
- Approval-record corrections are append-only events linked to the original record. A change to approver, authority, exact version, decision scope, or decision provenance is material and requires a new authenticated decision or explicit revocation/replacement. It must not be silently edited.
- Supersession links old and replacement logical IDs/versions. A superseded version remains retrievable for historical assessments. Withdrawal/revocation should preserve the prior version and state the reason, authority, effective point if governed, and affected downstream content.

**Metadata-only design direction:** do not issue a new normative Requirement version for a non-semantic correction to descriptive metadata that does not affect source binding, interpretation, identity, authority, or use. Record it as an append-only governance event. If a purported metadata correction affects any of those bindings, treat it as material and review/reapprove. Exact materiality criteria remain unresolved and require separate governance decisions.

## 6. Human Approval Authority

The following is a role proposal; none of these roles is assigned by this document.

| Role | Proposed authority boundary |
|---|---|
| Requirement author/content owner | May draft a proposal, maintain provenance, and request review. May not approve their own Requirement. |
| Source-validation reviewer | May verify source version, transcription, candidate boundary, and source links within a defined delegation. This is not Requirement approval. |
| Technical/semantic reviewer | May review normative representation, scope, dependencies, parameters, and change impact; records recommendation or return. May not approve unless separately delegated. |
| Independent approver | Reviews the exact version and evidence; may approve or reject only under recorded, active delegation. Recommended to be independent of author and primary technical reviewer. |
| DDS CISO | Recommended approval authority for initial production Requirement governance decisions until a delegation matrix is explicitly approved. The CISO may delegate within recorded scope; the delegator's own authority must itself be authenticated. |
| Registry/content custodian | May allocate IDs, enforce uniqueness, archive approved records, and carry out an authorized state update. Must not originate or invent an approval decision. |
| AI agent, implementation service, repository contributor | May perform mechanical checks or prepare a proposal. Has no Requirement approval authority by virtue of authorship, access, or validator result. |

### Approved governance design direction

Do not hardcode DDS CISO as the sole approver. Make approval authority configurable for each authorized organization and allow formally delegated approvers under recorded scope, effective/expiration dates, and revocation. DDS may designate the CISO as its initial primary approver. The role model must distinguish author, source-fidelity reviewer, technical reviewer, approval recommender, authorized Requirement approver, and assessment-specific risk decision authority. No actor receives approval authority solely through repository contribution, application access, AI output, or self-declaration.

Require separation of duties in production: the author cannot be sole reviewer or approver; the person validating source fidelity cannot alone approve Requirement governance. An exception, if allowed, must be explicitly approved by the configured authorized authority with rationale and audit record. Conflicts of interest must be declared; conflicted personnel recuse or an unconflicted authority is appointed.

Delegation should be recorded in an authoritative delegation register with delegator identity/authority, delegate identity, scope (source families, Requirement classes, or actions), start/end timestamp, restrictions, revocation mechanism, and evidence reference. Expired or revoked delegation cannot authorize a new approval. The exact assignment, quorum, role names, and exception policy remain unresolved governance decisions.

Approval of a Requirement remains distinct from later assessment-specific human risk acceptance, residual-risk disposition, or deployment authorization. Those decisions require their own authority and evidence.

## 7. Approval Authentication and Evidence

### Minimum approval record recommendation

A production Requirement approval event should bind at minimum:

- authenticated approver principal and display identity;
- authority/delegation reference, scope, validity period, and authorization check result;
- exact logical Requirement ID and immutable version;
- decision (`APPROVE`, `REJECT`, or `RETURN`), explicit scope, rationale, conditions, and decision timestamp in UTC with timezone (`Z`);
- integrity binding to the exact reviewed Requirement artifact (canonical content digest or immutable repository blob/commit identity), source/candidate identities and versions, and referenced source artifacts;
- approval evidence location, authentication/signature method, workflow event/transaction ID, and verifier result;
- append-only history links to prior review, correction, revocation, replacement, or supersession events.

Boundary fidelity approval and Requirement approval use distinct decision scopes, identity/version targets, and records. A Git commit author, chat statement, Markdown line, schema pass, or self-declared role alone is not authenticated approval. Structural validation proves only defined structural properties; it neither authenticates the actor nor authorizes the decision.

**Binding approved clarification:** approval evidence must be verified, identity-backed evidence of an authorized human decision, bound to the exact logical Requirement identity, immutable version, and integrity-verified content reviewed. A record that lacks any of these bindings does not establish Requirement approval. The authentication mechanism, canonicalization, signature format, trust roots, timestamping, and verification service remain implementation decisions.

### Mechanism comparison

| Mechanism | Strengths | Risks / prerequisites |
|---|---|---|
| A. Controlled repository approval | Fits repository-based development; PR review can bind a decision to a diff/commit and preserve discussion/audit events. | Only trustworthy if organizational identity is authenticated, branch protections and required reviewers are configured, role/delegation is checked, audit history retained, and the exact reviewed artifact is bound. A commit author or Markdown claim alone is insufficient. Current repository configuration has not been verified as meeting these controls. |
| B. Signed structured decision record | Portable and cryptographically verifiable; can bind Requirement identity/version, artifact digest, scope, approver, and timestamp. | Requires canonicalization, signature format, key issuance/protection/rotation/revocation, trust roots, verifier, and secure timestamp policy. A signature proves key use, not that the key holder had current authority unless delegation is separately checked. |
| C. Trusted workflow / identity-backed approval service | Can enforce authenticated identity, delegation, separation of duties, expiry, required fields, immutable audit events, and controlled release. | Requires an approved service, identity integration, security/recovery controls, audit retention, and a governed relationship between workflow events and repository artifacts. |

### Approved governance design direction

For initial repository development, use mechanism A **only after** repository administrators verify authenticated organizational accounts, protected `main`, required authorized reviewer rules, delegation lookup, and retained platform audit events. Bind approval to a digest or immutable blob/commit of the exact reviewed Requirement version and source/boundary references. Store a structured decision record or immutable workflow reference; do not treat prose alone as evidence. If those controls cannot be demonstrated, do not claim authenticated CISO approval in-repository.

For production, recommend mechanism C as the authoritative decision service and a signed structured record (B) as the portable, verifiable evidence package. The service must authenticate the approver and current delegation and bind the approval to exact canonical Requirement bytes/version. Canonicalization, signature algorithm, trust roots, trusted timestamp, retention, revocation, and repository sync are unresolved design details, not implemented here.

Avoid self-referential hashing: the artifact digest must cover the immutable Requirement content/version payload, excluding the approval event that references that digest, or use an immutable blob identity. Define canonicalization before relying on a byte digest across serializers.

## 8. Promotion State Machine

### Recommended production states (approved governance design direction)

Keep Requirement lifecycle separate from source currentness, parameter assignment, applicability, and assessment execution eligibility. Recommended Requirement lifecycle labels are:

`PROPOSED -> UNDER_REVIEW -> APPROVED`

Return/rejection paths: `UNDER_REVIEW -> RETURNED` or `REJECTED`; a returned item may be corrected and resubmitted as a new immutable version or proposal revision. Approved versions may transition to `REVIEW_REQUIRED`, `SUPERSEDED`, `WITHDRAWN`, or `REVOKED` through a separately authorized event. Exact terminal labels and transition semantics require CISO approval. Do not reuse Candidate Boundary status `VALIDATED` as a Requirement lifecycle state.

| Transition | Authorized actor | Preconditions and evidence | Recorded result / failure path |
|---|---|---|---|
| Source-fidelity review: Candidate Boundary `PROPOSED` -> `VALIDATED` (separate candidate lifecycle) | Authorized source-validation reviewer under future delegation | Exact pinned source; complete normative parts, parameters, relationships, and source provenance; review evidence and boundary rationale. | Record candidate validation decision and exact source/candidate version. Return/reject the candidate on discrepancy. This is not a Requirement lifecycle state or Requirement approval. |
| Candidate `VALIDATED` -> Requirement `PROPOSED` | Authorized content author | Exact pinned source/boundary refs; source-fidelity approval scope; unique authorized logical ID/version; parameter dependencies and unknowns represented; proposal artifact digest. | Create immutable proposal/history event. Missing or inconsistent provenance blocks creation; return to source/boundary review if the candidate is ineligible. |
| `PROPOSED` -> `UNDER_REVIEW` | Requirement owner/workflow coordinator | Required representation fields and structural checks pass; source and candidate resolve; reviewers assigned with conflicts declared. | Record review-start event and exact artifact version. Structural pass is not review or approval. Incomplete input remains proposed or is returned. |
| `UNDER_REVIEW` -> `RETURNED` / `REJECTED` | Authorized reviewer; rejection authority as delegated | Review records issues or rationale against exact ID/version and digest. | Append review decision. Correction produces a new immutable version/revision; rejection does not delete prior records. |
| `UNDER_REVIEW` -> `APPROVED` | Authenticated CISO or currently delegated independent approver | Source/boundary fidelity verified; normative meaning/scope reviewed; parameter dependencies explicit; provenance complete; authority/delegation active; integrity binding verified; no unresolved blocker outside permitted scope. | Authenticated approval record with decision, authority, exact ID/version/digest, scope, rationale, UTC time, evidence and workflow references. Failure means no state transition; return/defer/reject explicitly. |
| `APPROVED` -> `REVIEW_REQUIRED` | Authorized Requirement custodian or workflow on validated trigger; no semantic approval implied | Source, authority, delegation, parameter policy, or provenance issue detected; exact prior version preserved. | Mark new governance event requiring review; prevent new use according to separately approved eligibility policy. Do not rewrite prior approval. |
| `APPROVED` -> `SUPERSEDED` / `WITHDRAWN` / `REVOKED` | CISO or currently delegated authority; revocation may also be triggered by verified key/delegation compromise under approved procedure | Reason, replacement or withdrawal basis, impact analysis, exact affected versions, and decision evidence. | Append signed/authenticated status event and successor/revocation references; retain historical records and alert dependent workflows. |

**Promotion-readiness is not promotion authorization.** A validator can identify missing fields and report blockers. Only an authenticated human decision by an authorized approver can authorize `APPROVED`. Neither an approved Requirement nor a readiness result establishes system applicability, executable assessment eligibility, or risk acceptance.

Assessment execution eligibility is a distinct determination and must be governed independently from Requirement approval, applicability, currentness, source authority, and parameter resolution. Those dimensions must not be inferred from one another; an approved Requirement may remain ineligible for a particular assessment. Any eligibility decision and its prerequisites require separate governance. No eligibility state machine or rule is implemented here.

## 9. Parameter Governance Boundary

The handling below is an **approved governance design direction**. It is consistent with, but does not expand, the previously approved principle that a Requirement may retain unresolved parameters and parameter-dependent evaluation must be blocked.

Keep these as independent records/interfaces:

1. **Requirement normative approval:** approves source-bound obligation representation and explicitly retained parameter dependency; parameter may remain unresolved if CISO policy permits.
2. **Parameter assignment:** separate authorized assignment record for `si-12.3_prm_1`, with owner/authority, governing source or decision, value, scope, version/effective interval, approval evidence, and history. This task assigns nothing.
3. **Assessment applicability:** assessment-specific target/basis/rule/result and source role; not inherited from Requirement approval or assignment.
4. **Assessment evaluation:** may consume only authorized Requirement version, applicable determination, and required parameter assignment/version plus separately approved expectation/evidence/rules.

Until these interfaces are approved, an unresolved parameter remains explicit and any dependent evaluation stays blocked. Do not default, infer, or copy a value across scopes. Parameter assignment itself does not establish applicability or implementation.

## 10. Change Control and Revocation

### Approved governance design direction

- **Incorrect source transcription:** mark affected source/boundary/Requirement use for review; verify the pinned authority; revalidate the Candidate Boundary if its content or scope changes; create a new Requirement version and reapprove if an approved representation was affected.
- **Updated authoritative source:** pin and compare new source; determine materiality through human review; create new source-bound version where the binding changes; reapprove when meaning, scope, dependency, or applicable decision changes. Never propagate automatically.
- **Changed Requirement wording or parameter dependency:** issue a new immutable version, preserve old version, rerun source-fidelity and Requirement review, and require fresh approval before use.
- **Provenance correction:** append correction event. If it changes what artifact/version was reviewed or integrity binding, suspend eligibility pending re-review and reapproval; do not silently fix metadata.
- **Compromised approval evidence:** revoke/suspend the affected approval through an authenticated authorized event, preserve the compromised record, identify the potentially affected versions and downstream consumers, notify designated owners, and initiate impact review. Do not automatically create findings or reassessments.
- **Expired/revoked delegation:** deny new approvals by that delegation. Preserve prior decisions; review approvals made during the affected interval based on verified facts and approved policy. Do not retroactively invalidate by assumption.
- **Withdrawn source:** record source currentness/withdrawal separately; identify dependent Requirements and approvals; decide whether they remain historical, need review, or need replacement. Do not delete.
- **Superseded Requirement:** preserve prior versions and link the successor; new use must resolve to an approved current version under a future eligibility rule. Historical assessments continue to reference the old version they used.
- **Older assessments:** retain source version, Requirement ID/version, content digest, parameter assignment, applicability/rule versions, approval reference, and evaluation inputs. Deterministic replay uses those pinned historical artifacts, never current/latest content. Any re-evaluation is a new event; no retroactive findings or automatic reassessment are created here.

Change detection, impact analysis, notifications, re-evaluation eligibility, and deterministic replay require future governed services and schemas. This design defines no automatic invalidation behavior or new findings.

## 11. Governance Threat and Failure Analysis

Controls below express approved design directions; they do not assign risk scores or claim existing deployment controls.

| Failure mode | Preventive control | Detective control | Audit evidence |
|---|---|---|---|
| Fabricated approval record | Require trusted workflow/signature or verified platform approval; reject free-text-only claims. | Verify signature/workflow event against trust source and artifact digest. | Signed decision, workflow event ID, verification result, reviewed content digest. |
| Self-declared approver authority | Resolve identity and delegation from an authoritative register; never trust a role field supplied in the record alone. | Recheck delegation scope and validity at decision time and periodically. | Identity principal, delegation record/version, authorization check and timestamp. |
| Approval of one version reused for another | Bind decision to logical ID, immutable version and content digest. | Compare approved digest and identity/version to the exact proposed/consumed artifact. | Approval payload plus immutable content blob/digest and verifier result. |
| Source content changed without versioning | Pin source commit/version and prohibit mutable “latest” references as the only basis. | Compare pinned content and manifest; detect mismatch or changed digest. | Source manifest, immutable revision, integrity result, change-review event. |
| Superseded Requirement treated as current | Require eligibility lookup by ID/version and explicit currentness/supersession links before use. | Detect consumption of superseded/withdrawn/revoked versions in resolver or review. | Resolution input/output, state/version snapshot, alert and authorized exception if any. |
| Invalid delegation accepted | Central delegation record with scope, dates, revocation and identity binding. | Validate active delegation during approval verification; alert on expired/revoked authority. | Delegation artifact/version and validation evidence at approval timestamp. |
| Parameter value inserted without authorization | Keep assignments separate; schema requires authority/scope/version/decision reference for assigned state. | Compare assignment provenance against authorized parameter governance source and scope. | Assignment record, approval evidence, scope/version check, change history. |
| AI-generated Requirement promoted without human review | Require source-validated boundary plus explicit human-reviewed state and authenticated human approval; validator cannot set it. | Audit provenance and identity of reviewer/approver; detect automated or missing actor evidence. | Extraction provenance, human review record, authenticated approval event. |
| Approved Requirement treated as automatically applicable | Keep applicability separate and require a target-specific basis/rule for assessment use. | Check assessment trace for applicability record and target; flag absence as unresolved. | Applicability target/basis/rule/version and explicit status/rationale. |
| Historical assessment becomes unreproducible | Pin immutable source/Requirement/parameter/rule versions and retain referenced artifacts. | Periodic replay/retrieval checks and dependency inventory; report unavailable historical inputs. | Snapshot manifest, digests/blob IDs, version references, replay outcome and gaps. |

## 12. Implementation Implications

This approved design does not authorize implementation changes. Subject to the remaining governance decisions and a separately authorized implementation increment, likely future changes include:

- **Requirement JSON Schema:** separate stable logical ID/version; proposed state/currentness state; source and candidate refs; typed parameter assignment refs; approval record vs boundary-validation reference; supersession; history; integrity binding and record context.
- **Requirement validator:** cross-reference identity/version, source/candidate, parameter and relationship records; enforce state/decision consistency; detect self/invalid supersession; verify digest and authorized signer/delegation via trusted interfaces; emit diagnostics/readiness without promotion.
- **Approval records:** structured, authenticated, immutable decisions bound to exact Requirement version and digest, with delegation checks and revocation/supersession links.
- **Requirement Catalog:** controlled registry with atomic ID allocation, uniqueness, version preservation, currentness and change links. None exists today.
- **Tests:** adversarial authorization, mismatch, replay, delegation expiry/revocation, signature/digest, supersession, parameter scope, and historical-readiness tests, using synthetic records only.
- **Repository permissions:** protected branches, required reviewers, authenticated organization identities, CODEOWNERS or equivalent, audit-log retention, access controls, and release/tag policy. Current repository settings must be verified; this document does not assert they are configured.
- **Trusted workflow:** production identity provider, MFA/strong authentication as approved, delegation service, trusted timestamp, signed decision event, key lifecycle, revocation, audit export, and repository/catalog integration.
- **Execution eligibility:** downstream resolver must require an approved exact Requirement version and independently governed applicability and parameter prerequisites. No resolver is implemented here.

### Minimum viable governance after remaining decisions

Before production use, the minimum governance prerequisite is an approved ID/version convention; an assigned Requirement owner and approval authority/delegation; separation-of-duties rules; source/boundary review checklist; authenticated decision record bound to the exact version; explicit return/reject/revoke handling; and a documented route for unresolved parameter/applicability states. These are governance artifacts, not automatic platform features.

### Production hardening

Production hardening additionally requires an identity-backed approval service or equivalently controlled mechanism, signed/verified decision evidence, trusted timestamps and key lifecycle, a controlled Requirement Registry with atomic uniqueness enforcement, immutable audit retention, downstream eligibility enforcement, notification/impact analysis, and historical replay verification. None is present or approved as deployed in the current repository.

### Recommended implementation order after remaining decisions

1. Approve exact identity/version semantics, lifecycle names, role/delegation policy, and approval evidence/authentication model.
2. Verify or establish protected repository review controls for initial development; define decision-record and content-digest canonicalization.
3. Revise the provisional schema and validator under a new authorized implementation increment; add authenticated workflow verification rather than trusting a self-asserted approval field.
4. Implement a governed registry/approval record store with immutable history, then test promotion and revocation paths using synthetic identities and records.
5. Separately govern parameter assignment and applicability; only later consider safeguard/evidence mappings and assessment execution eligibility.

## 13. Open Decisions

- Exact opaque ID encoding and allocation authority; random UUID, UUIDv7, or another identifier strategy.
- Version representation, increment rules, and which provenance-only changes require new versions.
- Lifecycle state names, state transitions, currentness interaction, and meanings of withdrawal vs revocation.
- DDS initial primary-approver designation and named delegated roles; delegation register owner, expiry, limits, quorum, separation-of-duties exceptions, and conflict handling.
- Initial repository approval controls and proof of authenticated role; whether those controls can be established in this repository.
- Canonicalization and integrity binding for Requirement versions; digest/signature format, trusted timestamp and key/trust-root lifecycle.
- Production trusted approval service, audit retention, revocation integration, and repository/Catalog synchronization.
- Source currentness and materiality review ownership and downstream eligibility behavior.
- Parameter assignment authority and scope; assessment-specific source role and applicability basis remain separately unresolved.

## 14. CISO Decision Register

### SAR-CODEX-071 disposition

| Register field | Recorded disposition |
|---|---|
| Decision authority | DDS CISO |
| Decision | `APPROVED - GOVERNANCE DESIGN` |
| Additional conditions | None |
| Decision provenance | Explicit CISO disposition in the SAR-CODEX-071 conversation. |
| Decision date | Unresolved; the approval record does not explicitly establish a date. |

### Binding clarifications

| Clarification | Approved requirement |
|---|---|
| Organizational approval authority | Approval authority is configurable for each authorized organization and includes formally delegated approvers under recorded authority, scope, and validity. Specific assignments and delegation implementation remain unresolved. |
| Approval evidence | Verified identity-backed evidence must bind the authorized human decision to the exact Requirement identity, immutable version, and content integrity. Authentication, signature, canonicalization, and verification mechanisms remain unresolved. |
| Assessment execution eligibility | Eligibility is independently governed from Requirement approval, applicability, currentness, source authority, and parameter resolution. No eligibility logic or decision is established here. |

### Governance design decisions

The following design directions are approved at the governance-design level. This approval does not resolve the implementation details or open decisions listed in Section 13.

| Decision | Approved design direction | Alternatives not selected as design direction | Rationale / remaining boundary |
|---|---|---|---|
| Logical ID | Use an opaque SAR-managed logical Requirement ID, separate from source keys. | Source-derived or composite ID. | Stable identity supports changing source bindings; encoding, allocator, registry, and issuance remain unresolved. |
| Versioning | Keep immutable per-logical-ID versions with append-only metadata/decision events and explicit succession. | Content hash as sole version; mutable current record. | Preserves the exact reviewed content; version syntax, revision triggers, and storage remain unresolved. |
| Approval authority | Use configurable organizational authority, including formally delegated approvers, with separation of duties and recorded authority. | Fixed universal approver; self-approval. | Exact roles, assignments, delegation register, exception policy, and conflict controls remain unresolved. |
| Approval evidence | Require verified identity-backed human approval evidence bound to exact Requirement identity, immutable version, and content integrity. | Repository prose or self-asserted role alone. | Approval mechanism, canonicalization, signatures, trust lifecycle, and audit implementation remain unresolved. |
| Promotion/revocation | Require authorized human decision for approval and preserve review, revocation, and succession history. | Automated promotion on readiness; mutable status without history. | Exact lifecycle labels, transitions, and implementation remain unresolved; this design grants no approval to any Requirement. |
| Change control | Preserve immutable versions for material changes and append-only events for non-semantic corrections. | Silent mutation; automatic source propagation. | Materiality criteria, reapproval triggers, and owner roles remain unresolved. |
| Assessment execution eligibility | Govern eligibility independently from Requirement approval, applicability, currentness, source authority, and parameter resolution. | Treat Requirement approval as sufficient for execution. | Eligibility criteria, authority, resolver, and operational logic remain unresolved. |

## 15. Scope and Review Limitations

This document records an approved governance design only. It does not create a production ID, Requirement, Requirement approval event, delegation record, signature, registry, applicability determination, parameter assignment, safeguard/evidence rule, finding, or assessment. It does not modify the provisional SAR-CODEX-070 schema, validator, example, tests, or approved SAR governance documents.

The exact production ID syntax, delegated approver assignments, authentication service, canonical artifact hashing, lifecycle policy, revocation workflow, impact analysis, source role, applicability basis, parameter assignment, and assessment eligibility implementation remain unresolved. The SAR-CODEX-071 CISO approval is limited to the governance design and binding clarifications recorded in Section 14; it is not approval of SI-12(3), a parameter value, applicability, or assessment execution.
