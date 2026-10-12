# SAR Requirement Registry Contract and Canonical Content Profile

**SAR-CODEX-073 | NON-OPERATIONAL IMPLEMENTATION CONTRACT**

> **CONTRACT AND VALIDATOR ONLY - NO REGISTRY, ALLOCATOR, APPROVAL WORKFLOW, OR ASSESSMENT EXECUTION**

This document describes the versioned structural contract in `schemas/sar-requirement-registry.schema.json`, the read-only validator in `tools/validate_requirement_registry.py`, and its synthetic fixture. It is not a production registry, identity convention, approval policy, parameter assignment, applicability rule, or execution interface. All identities and source references in the fixture are fabricated test values.

## 1. Governance Boundary

The implementation preserves the approved SAR-CODEX-071/072 boundaries:

- Logical identity is separate from immutable version, source provenance, integrity, lifecycle history, approval, applicability, and execution eligibility.
- Allocation or version registration would establish only registry identity/version existence. It would not authorize use, establish source fidelity, provide human review, approve the Requirement, select source authority versus benchmark role, assign parameters, establish applicability, or permit execution.
- Lifecycle events are an append-only audit contract. `APPROVAL_EVIDENCE_REFERENCED` records a reference only; it does not mean evidence was authenticated or authority verified, and it does not change a version to approved.
- The schema intentionally has no `APPROVED`, `PROMOTED`, `CURRENT`, `EFFECTIVE`, or execution-enabled state. It does not model applicability or parameter assignments.
- An assessment must separately pin the exact Requirement identity/version/content digest and separately governed inputs. No assessment resolver is implemented.

This contract does not weaken the trusted-identity, exact-version, human-decision, or independently governed eligibility principles. Mechanical validation cannot prove identity, authorization, source fidelity, semantic correctness, or approval.

## 2. Versioned Record Contract

The registry snapshot has `registry_contract_version: 1.0.0` and `snapshot_context: NON_OPERATIONAL_FIXTURE`. Four record kinds each carry `record_schema_version: 1.0.0`:

| Record | Key / reference | Mutability contract | Validation boundary |
|---|---|---|---|
| Logical Requirement identity | `(issuer_namespace, logical_id)`; unique within the snapshot. | Identity is stable and never edited/recycled. A new alias may be represented only through a later contract/event design. | Format, duplicate-key and `IDENTITY_REGISTERED` reference checks; no proof that issuer is authorized or conceptually unique. |
| Immutable Requirement version | `(issuer_namespace, logical_id, version_id)`; unique; positive sequential per identity beginning at 1. | Issued fields are immutable. New content gets another version. `based_on_version`, when present, must exist earlier under the same identity. | Version sequence, identity and content-reference resolution, registration event and envelope identity checks; no approval/currentness inference. |
| Content reference | `content_reference_id`; one embedded canonical content envelope and digest in the portable fixture contract; optional immutable storage locator is outside the digest. | Content envelope, digest, and reference record are immutable for a registered version. Locator replacement is not implemented here and must not mutate the envelope or digest. | Envelope schema, RFC 8785 canonical bytes, SHA-256 recomputation and exact version/digest linkage. |
| Lifecycle event | `event_id`; one-based contiguous `sequence`; `previous_event_id` links the ordered append-only event list. | Prior events must remain an identical prefix. A correction or new decision is a new event, never an overwrite. | Event schema, unique event ID, sequence/chain, target references, registration order, permitted event type and acyclic supersession checks. |

Identity syntax is deliberately only a non-empty string in schema. `fixture-logical-requirement-001` is not production syntax. Issuer namespace and cross-organization uniqueness semantics remain subject to separate CISO decisions. The version integer is a non-operational contract choice for this implementation; it is not a production identifier or allocation service.

The `RequirementRegistryPort` in the Python validator is a typing `Protocol`, not an adapter or service. It has no database, network, allocator, or persistence implementation. Its write methods require an opaque out-of-band authorization context, and its read/export methods require an access context; implementations must authenticate/authorize those contexts through a trusted integration and must not treat `actor_reference` text in a record as proof of identity or delegation. Implementations would have to provide the approved uniqueness, atomic-or-equivalent change, concurrency, idempotency, referential integrity, authorization, append-only history, recovery, portability, and reconciliation guarantees for their operating context. No particular database, cloud, API host, or object store is required.

## 3. Canonical Content Envelope v1

### Included fields

The `SAR-REQ-CONTENT-JCS-SHA256` profile v1 envelope is the exact JSON object accepted by the content-envelope schema. Its included fields are:

| Field | Included values |
|---|---|
| `profile_id`, `profile_version` | Literal profile identifier and `1.0.0`. |
| `identity` | Issuer namespace, opaque logical ID, and immutable positive integer version ID. |
| `normative_content` | Controlled statement, semantic role, normative strength, scope, conditions, exceptions, qualifiers, and parameter dependency references/usage. |
| `source_bindings` | Source Catalog identity, exact source version/revision, artifact reference, source object/provision, ordered part references, source relationships, and exact validated Candidate Boundary ID/revision and decision reference. |

The envelope stores references, not copies of source documents. The parameter dependency represents the source-defined dependency and use in the Requirement. It contains no organization-assigned parameter value, assignment record, assignment authority, or parameter approval.

### Excluded fields

The following are not part of the canonical envelope and do not affect its digest:

- Lifecycle/currentness/effective projections, state fields, and lifecycle events.
- Approval decisions, approval evidence packages, signatures, actor authentication, delegation checks, and approval timestamps.
- Assessment-specific source-authority/benchmark role, applicability, assessment execution eligibility, evidence, findings, or risk decisions.
- Organization-specific parameter values/assignments and their authorization records.
- Storage locators, replication locations, access timestamps, verification timestamps, mutable display labels, and other administrative metadata.

The `content_reference_id`, digest value, and lifecycle/approval records are also outside the envelope, avoiding self-reference. The immutable version record points to the content reference; the approval-evidence reference event binds its own exact `approval_content_digest` to that target. Relocating stored bytes must not change the envelope or digest; this contract does not implement relocation or mutable reference updates.

A correction to an included normative, parameter-dependency, source-binding, identity, version, or profile field changes the envelope and therefore requires a new digest and a new immutable version under future governed revision policy. A correction to an excluded event/admin field must not change the content digest; it is represented as a separate append-only event. Version migration and compatibility behavior beyond profile v1 remain open for production design.

## 4. Canonicalization and Digest

The implementation uses the RFC 8785 JSON Canonicalization Scheme (JCS) implementation `rfc8785==0.1.4`; SHA-256 is applied to the canonical UTF-8 bytes. The record stores `digest_algorithm: sha-256` and 64 lowercase hexadecimal digits in `digest_value`. This is a versioned non-operational implementation profile for review, not a claim that SAR-CODEX-072 finalized a production algorithm/profile.

Profile rules:

1. Parse JSON as UTF-8 and reject duplicate object member names before a dictionary can discard them. Reject non-JSON constants such as NaN/Infinity.
2. Validate the envelope against the exact versioned schema before canonicalization. The schema uses strings, booleans only where explicitly allowed, arrays, and safe integer version IDs; floating-point domain values are not represented in the envelope.
3. Serialize object members and JSON primitives according to RFC 8785. Preserve array order exactly; producers must provide stable order for source parts, dependencies, and bindings.
4. Do not apply NFC/NFD or other Unicode normalization. JCS-required escaping is applied by the canonicalizer, while Unicode scalar sequences remain distinct. Invalid Unicode is rejected by the canonicalizer.
5. Compute SHA-256 over the resulting canonical bytes and compare the complete lowercase digest before accepting the content reference.

A digest provides content-integrity comparison only. It is not a digital signature, authenticated identity, authority/delegation decision, proof of source fidelity, or human approval. The registry contract does not sign content or authenticate actors.

## 5. Lifecycle and Append-Only Validation

The bundle is a complete non-operational snapshot. Lifecycle events use a deterministic contiguous sequence and previous-event link. Registration events must match exactly one identity/version record and precede events that target that version. Duplicate identities, versions, content references, event IDs, broken links, non-contiguous per-identity version sequences, and dangling references are rejected.

Allowed event kinds in this contract are registration, review recorded, approval evidence referenced, review required, withdrawal, supersession, and administrative correction. There is intentionally no event kind that approves/promotes a Requirement or enables assessment execution. An approval evidence reference must name an evidence reference and the exact content digest of its target version; validation only checks this linkage, not the evidence itself or the authority behind it.

Withdrawal and supersession are terminal version lifecycle outcomes for this contract. Supersession names one or more existing successor versions and is checked for self-links and graph cycles. State transitions are deterministic projections for integrity checking only; they do not implement operational lifecycle policy or affect content digests.

`validate_append_only(previous, candidate)` requires every previously recorded identity, version, and content-reference object to remain present and unchanged, and the old event list to remain an unchanged prefix. New records/events may extend the snapshot only if the complete candidate snapshot passes all schema, digest, uniqueness, referential-integrity, sequencing, and lifecycle checks. This validates a proposed snapshot; it does not persist or authorize it.

## 6. SI-12(3) Migration Mapping

The source example remains unchanged at `requirements/examples/si-12-3.proposed.yaml`. No production ID, version, approval, digest, parameter assignment, applicability, or execution status was changed.

| Existing example field | Future contract mapping | Preserved migration state |
|---|---|---|
| `identity.logical_id: EXAMPLE-REQ-0001` | Logical identity record only after an approved production ID convention and authorized migration. | Treat current value as example placeholder/legacy alias, never import as production identity. |
| `identity.version: EXAMPLE-VERSION-1` | Immutable version record under future sequential version contract. | Placeholder is not a version number; do not silently translate or promote it. |
| Source family `nist-sp800-53-rev5`, release `5.2.0`, pinned revision `78650f02ad9321bb7b817846f8fbd4f2bcd620de`, source object/part and `required` relation | One or more source bindings with exact Source Catalog, source-object, part, relationship, and artifact references. | Preserve pinned source provenance; source-native identifiers do not become SAR identity; do not copy source documents. |
| Candidate Boundary `cbr-nist-sp800-53-rev5-si-12-3-smt`, `VALIDATED`, decision reference | Candidate Boundary binding with exact revision and boundary decision reference. | Preserve as source-fidelity validation only; not Requirement approval. |
| Controlled representation and `si-12.3_prm_1` dependency | Normative content and parameter-dependency reference in a new immutable envelope. | Preserve proposal text/dependency; assignment remains absent/unresolved. |
| `PROPOSED`, `NOT_APPROVED`, history | Non-operational lifecycle events. | Preserve proposed/unapproved state; no synthetic approval event. |
| Unresolved applicability/source role and `NON_EXECUTABLE` boundary | Outside the identity/version registry content and records; referenced by a future separate assessment contract if authorized. | Remain unresolved, not determined, and non-executable. |

A future migration requires an authorized plan, production identifier/version decisions, source and Candidate Boundary re-resolution, mapping/version rules, immutable input/output snapshots, integrity verification, and row-level reconciliation. Registration is not approval; migration must not create applicability or execution eligibility. No migration is performed by SAR-CODEX-073.

## 7. Run and Assumptions

Install the declared Python dependencies with `python -m pip install -r requirements.txt`. Validate the included fixture with `python tools/validate_requirement_registry.py`. Run registry tests with `python -m unittest discover -s tests/requirements -p 'test_validate_requirement_registry.py' -v`; run all existing Requirement tests with `python -m unittest discover -s tests/requirements -v`.

Assumptions for this non-operational increment:

- JSON Schema Draft 2020-12 remains the schema convention already used by the Requirement tool.
- Registry snapshots are complete JSON exports; array order in the event log is authoritative and immutable.
- UUID syntax, production issuer namespaces, persistence, authentication/authorization mechanisms, approval workflow, canonicalization compatibility beyond profile v1, and deployment/storage technologies remain unresolved.
- The synthetic namespace/IDs/source references and actor references exist only for tests and assert no real authority or source facts.
