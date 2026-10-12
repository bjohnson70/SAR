# SAR Requirement Identity, Version, and Registry Design

**SAR-CODEX-072 | APPROVED DESIGN RECOMMENDATIONS WITH THREE CLARIFICATIONS**

> **DESIGN APPROVED - IMPLEMENTATION SPECIFICATION PENDING - OPERATIONAL EXECUTION NOT AUTHORIZED**

This document records the DDS CISO's approval of the SAR Requirement Identity and Version Registry design recommendations, subject to the three binding clarifications below and in Section 15. Approval covers design direction only. It does not select every technology, resolve detailed implementation specifications, implement a registry, or approve an individual Requirement. It creates no production Requirement identity, version, digest, registry record, approval evidence, or operational authority.

## 1. Purpose and Scope

Define a reviewable, portable design for a future governed SAR Requirement Registry. The registry would maintain stable logical Requirement identity, immutable content versions, source and Candidate Requirement Boundary provenance, integrity metadata, lifecycle history, supersession relationships, and references to verified approval evidence.

The registry is not the Source Catalog, an assessment record store, an applicability engine, an approval workflow, or a copy of source documents. It must preserve the distinctions:

```text
Source Catalog / Source Version
    != Candidate Requirement Boundary
    != Requirement Logical Identity
    != Immutable Requirement Version
    != Content Digest
    != Lifecycle State
    != Approval Decision
    != Applicability Determination
    != Assessment Execution Eligibility
```

This increment is design-only. It does not implement an allocator, registry, canonicalization, digest/signature procedure, approval workflow, source update, Requirement record, parameter assignment, applicability determination, or assessment execution logic. It does not change the provisional SI-12(3) example or assign it a production Requirement ID.

Decision labels used throughout:

- **APPROVED — DESIGN DIRECTION:** a design principle approved in SAR-CODEX-071 or SAR-CODEX-072; it is not an operational capability.
- **PENDING — IMPLEMENTATION SPECIFICATION:** a detailed format, profile, data contract, technology, or procedure requiring specification and separate review.
- **NOT AUTHORIZED — OPERATIONAL EXECUTION:** no registry, allocator, hashing/signing, approval workflow, Requirement promotion, or assessment execution is authorized by this design approval.

## 2. Approved Governance Inherited from SAR-CODEX-071

**APPROVED — DESIGN DIRECTION:** SAR uses an opaque SAR-managed logical Requirement identity independent of source keys, with a separate immutable version identity. Identity remains stable while a conceptual Requirement continues; materially different, split, or merged Requirements require explicit succession identity and relationships. A source provision may produce multiple Requirements and one Requirement may refer to multiple source provisions.

**APPROVED — DESIGN DIRECTION:** Requirement versions and decisions remain historically traceable and are not silently rewritten. Requirement approval is distinct from Candidate Boundary validation, source currentness, applicability, parameter assignment, assessment eligibility, risk acceptance, and deployment authorization.

**APPROVED — DESIGN DIRECTION:** Approval authority is configurable for each authorized organization and can include formally delegated approvers under recorded authority and scope. Approval evidence must be verified and identity-backed, evidencing an authorized human decision and binding it to the exact Requirement identity, immutable version, and content integrity.

**APPROVED — DESIGN DIRECTION:** Assessment execution eligibility is governed independently from Requirement approval, applicability, currentness, source authority, and parameter resolution. No new eligibility rule is proposed as operational behavior here.

SAR-CODEX-071 did not approve production identifier syntax, a version encoding, registry authority/storage, canonicalization, hash algorithm, allocation mechanism, lifecycle vocabulary, import rules, or a registry implementation. The design options in this document are not extensions of the CISO approval.

### SAR-CODEX-072 CISO disposition and clarifications

The DDS CISO approved the Requirement Identity and Version Registry design recommendations with no additional conditions. The exact disposition provenance and unresolved date are recorded in Section 15. The three clarifications are binding design constraints:

1. **Technology-neutral registry:** require registry guarantees, not a particular database, cloud service, API hosting platform, or storage technology. A transactional relational database, authenticated API, and immutable object storage are options only. A repository-backed design may be considered if it demonstrates the same guarantees for its intended context.
2. **Explicit canonical content boundary:** define and review the immutable Requirement content field set, identity/version binding, source/provenance and parameter dependencies, schema/profile, normalization/serialization, digest algorithm identifier, exclusions, metadata corrections, and migration compatibility before implementing hashing. Lifecycle, approval, or unrelated administrative changes must not silently alter a content digest.
3. **Identity is not authorization:** allocation and version registration do not authorize a Requirement for use. Source-fidelity validation, human review, authenticated approval, effective/current lifecycle, source authority/benchmark role, parameter assignment, applicability, and assessment execution eligibility are distinct steps. A registered version can remain proposed, unapproved, unresolved, and non-executable; newest is not automatically approved or current.

## 3. Existing Implementation Baseline

### Approved governance versus implementation

- The Requirement Model is conceptual: it calls for stable internal identity, source traceability, version awareness, and historical preservation but does not define a production identifier grammar or registry.
- SAR-CODEX-069 approved opaque logical identity plus separate immutable version as governance design. SAR-CODEX-071 reaffirmed that direction and added the binding approval authority/evidence and execution eligibility clarifications.
- SAR-CODEX-070's schema, validator, example, and tests are provisional implementation artifacts. `0.1-provisional`, `EXAMPLE-REQ-0001`, `EXAMPLE-VERSION-1`, enumerated lifecycle values, and its approval-record shape are not production conventions.
- The Source Catalog is the separate authority for source-family/source-version identity and preserves current-source versus assessment-source-version distinctions. Registering a source does not establish applicability.
- Candidate Boundary identity is distinct from Requirement identity. A human-validated boundary is necessary provenance for a governed Requirement; validation of the boundary is not Requirement approval.
- The Deterministic Content Model asks for stable logical references and immutable versions, but explicitly does not select a general serialization, database, API, or executable ruleset.

### Provisional schema and validator

The checked-in JSON Schema (`schemas/sar-requirement-record.schema.json`) uses `identity.logical_id` and `identity.version` as required nonempty strings. It has separate `lifecycle`, `source_provenance`, `normative_content`, `governance`, `applicability`, `execution_boundary`, and `history` fields. The provisional history is an array of typed events, while supersession references are embedded in lifecycle data. There is no registry-wide uniqueness constraint, immutable object store, canonical content projection, digest field, transactional allocation service, or cross-record referential integrity store in this implementation.

`tools/validate_requirement.py` validates the local record against the schema and supplied source manifest, candidate set, and source slice. It checks source/candidate/part/parameter/relationship consistency and some local identity/history consistency. It is deterministic and read-only; it cannot authenticate actors, verify delegation, establish global uniqueness, prove content integrity, or create an authorized transition. The focused tests use the existing non-operational example and synthetic in-memory approval data only.

### Existing field conventions

The provisional example separates `identity.logical_id` from `identity.version`; pins source catalog identity, release, upstream revision, artifact path, source object and parts; refers to a validated Candidate Boundary and source relationships; represents normative text separately from parameter dependencies; and keeps lifecycle, approval, applicability, execution boundary, and history distinct. Those are useful design inputs, not approved production field names or complete registry records.

The current example has the opaque-looking placeholders `EXAMPLE-REQ-0001` and `EXAMPLE-VERSION-1`, source `nist-sp800-53-rev5`, release `5.2.0`, pinned revision `78650f02ad9321bb7b817846f8fbd4f2bcd620de`, source object `si-12.3`, part `si-12.3_smt`, Candidate Boundary `cbr-nist-sp800-53-rev5-si-12-3-smt`, unresolved parameter `si-12.3_prm_1`, proposed lifecycle, unresolved applicability, and non-executable state. The example IDs/version string remain explicitly provisional.

## 4. Logical Requirement Identity

### Identity properties

**APPROVED — DESIGN DIRECTION:** The logical ID is a stable SAR-managed opaque identity, not a source-derived key. It must not encode or be derived from NIST control IDs, OSCAL IDs, Candidate Boundary IDs, source-document versions, Requirement approval status, or assessment-specific applicability. It identifies the continuing conceptual Requirement, not a claim that its content is approved, current, applicable, or executable.

Source cardinality is many-to-many: a source provision can support zero, one, or many Requirement identities; a Requirement can be bound to one or many source provisions and source families. Replacing, correcting, withdrawing, or re-releasing a source changes versioned provenance and may prompt a new Requirement version or explicit succession; it does not rewrite or recycle the logical identity when the conceptual Requirement continues. A split or merge produces new logical identities and explicit successor relationships rather than overloading one identifier.

### Identifier alternatives

| Alternative | Benefits | Costs and risks | Assessment |
|---|---|---|---|
| Source-derived or composite human-readable key | Immediately recognizable; easy to inspect without a registry lookup. | Couples identity to publisher numbering, source family, or version; can collide across sources; unstable under source moves, revision, split/merge, or multi-source provenance. May imply a false one-source/one-Requirement relationship. | Not recommended; conflicts with the approved opaque identity principle. Put citations and labels in separate metadata. |
| Central sequential integer or prefixed sequence | Compact, ordered, simple to validate; collision-free with one serial allocator. | Reveals registry volume/order; requires online central allocation; merge/import namespaces are difficult; IDs may be mistaken for semantic rank; format migration and offline drafting are awkward. | Viable only within a single controlled registry; less suitable as a portable cross-organization identity. |
| Random UUIDv4 | Globally portable, opaque, widely supported, no source coupling, and can be generated offline. | Random generation does not authorize registration; collisions, though extremely improbable, still require a registry uniqueness check. No temporal ordering; human-hostile. | Strong candidate where opacity and offline generation matter; registration remains centrally governed. |
| Time-ordered UUIDv7 | Portable, broadly unique, sortable, supports distributed generation and registry reconciliation. | Encodes approximate creation time; node clocks and disorder complicate ordering; sortable values can disclose activity timing. Generated identity still does not establish authorization. | Useful distributed option if time disclosure and clock behavior are accepted; do not treat sort order as version or authority. |
| Issuer namespace plus locally allocated identifier | Supports organizations allocating offline within assigned namespaces and independent local registries. | Requires globally governed namespace allocation, issuer lifecycle, collision checks, and durable issuer identity; migrations and exports must preserve issuer qualification. | Potential federation strategy, but needs explicit governance and namespace registry. |

**APPROVED — DESIGN DIRECTION:** Use an opaque SAR-managed logical ID, independent of source numbering, with controlled registration and uniqueness. Identity remains stable across versions and does not convey authorization.

**PENDING — IMPLEMENTATION SPECIFICATION:** UUIDv4 with a lowercase hyphenated string is one candidate representation, not a required format. Exact UUID representation, uniqueness domain, issuer/namespace model, and offline registration policy remain open. Any implementation must detect collisions and establish authorized registration; UUID generation itself does not do so.

### Uniqueness domain and portability

**APPROVED — DESIGN DIRECTION:** Registration must enforce uniqueness within its governed authority domain and support portable identity references. **PENDING — IMPLEMENTATION SPECIFICATION:** One global SAR authority or a globally governed issuer-qualified namespace are alternative ways to establish cross-organization uniqueness; the design does not select between them. A UUID's statistical uniqueness does not remove the need to check registration and authorization.

Exports preserve the original issuer-qualified ID and never rewrite identity silently. A receiving SAR registry verifies issuer and origin evidence, checks its uniqueness domain, and records an import/adoption event. For a foreign ID whose authority or content cannot be verified, retain it as an external reference or quarantine it; assign a new local SAR identity only through an explicit, authorized adoption/mapping event. Preserve both identifiers and their relationship. Never infer that two differently issued records are the same Requirement from similar wording or source citations alone.

**PENDING — IMPLEMENTATION SPECIFICATION:** Whether “SAR-managed” means one global DDS/SAR namespace, an issuer-qualified federation, or a single registry operated for participating organizations. Import/export acceptance, namespace custodianship, and registry migration authority depend on that choice.

## 5. Immutable Version Strategy

### Version alternatives and recommendation

| Strategy | Benefits | Limitations |
|---|---|---|
| Sequential per-logical-ID version number | Easy to reference, order, and explain; independent of serialization and hash implementation; supports corrections with preserved history. | Requires an authoritative allocator and concurrency control per identity; sequence does not prove content integrity or approval. |
| Content-addressed version ID | Naturally changes with content and detects byte/content changes; deduplicates identical content. | Does not express succession or issuance order; same content may have different governance/provenance; canonicalization is prerequisite; hashes cannot prove authorization or approval; content changes become awkward to reference before materialization. |
| Hybrid sequential version plus digest | Human-stable version key and separate integrity check; supports exact historic references and content verification. | More fields and a requirement to govern both sequence allocation and digest profile; digest must not be mistaken for authority or approval. |

**APPROVED — DESIGN DIRECTION:** Keep Requirement logical identity separate from immutable versions; sequential per-identity versioning is the recommended initial direction, with a separate content-integrity reference. Preserve each issued version historically and control supersession explicitly. A digest is not a version ID and neither registration nor sequence order authorizes use.

**PENDING — IMPLEMENTATION SPECIFICATION:** A positive sequential integer per logical Requirement, serialized as a decimal string, is the recommended version format candidate. Exact wire representation, issuer qualification, draft revision handling, sequence/gap policy, and the digest profile remain unsettled. The hybrid version-plus-digest design is approved as direction, not as a final encoding.

### Draft revisions and issuance

A proposal before registry issuance is a mutable work area only if its mutable nature is explicit; each reviewable draft snapshot should be preserved by a proposal ID, draft revision, actor/time, and content reference. Draft revisions are not production Requirement versions and confer no approval. Once submitted for registry issuance, the registry freezes the exact content snapshot and allocates the next unused version number atomically. Issued versions are immutable regardless of lifecycle state.

The initial issued proposal version is `1` for a newly registered logical ID, but is not approved merely by being issued. Every later issued normative representation gets the next unused version number and begins in a non-approved proposal/review state. Gaps caused by failed or abandoned transactions may be avoided by allocating inside the same transaction as durable version insertion; once an identifier/version has been durably issued it is never reused, even if withdrawn or rejected.

A returned draft can be revised without changing an already issued version; when re-submitted as a distinct immutable snapshot it receives a new issued version under the approved revision policy. A rejected or withdrawn version remains retrievable. “Newest” means largest issued sequence only; it does not mean current, effective, approved, applicable, or eligible.

### Change, concurrent versions, and succession

A material change to normative text/meaning, semantic role, scope, conditions, exceptions, source-part binding, parameter dependency, or other immutable representation content requires a new issued version and fresh review/approval before that version may be approved. Source-only revisions are retained as distinct provenance; whether every provenance-only change requires a new version or reapproval must follow the still-open materiality policy. Non-semantic administrative corrections that do not change identity, interpretation, authority, source binding, or use are append-only correction events; if a correction alters immutable content, issue a new version instead of editing prior bytes.

Concurrent proposals based on the same prior version are permitted as drafts. At issuance, a transaction serializes the per-identity sequence. The registry records `based_on_version` and detects stale bases. A stale proposal must be rebased/reviewed or issued as an explicit branch under future policy; sequence allocation alone must not silently choose the winner. Multiple versions can coexist as proposals or historical records. Effective selection requires an authorized lifecycle/event decision and its own resolution rules; there is no implied single approved “latest” pointer.

### Six distinct concepts

| Concept | Meaning | Mutability / relation |
|---|---|---|
| Requirement logical ID | Stable identity of the continuing conceptual Requirement. | Immutable after registration; source-independent. |
| Requirement version ID | Registry-issued ordinal identifying one immutable version under one logical ID. | Immutable, unique within logical ID, never reused. |
| Content digest | Algorithm-qualified integrity fingerprint of the canonical immutable content envelope. | Recomputed/verified from bytes; not authority, sequence, or approval. |
| Lifecycle state | Current projection of authorized lifecycle events for an identity/version. | Derived from append-only events; not part of normative content digest. |
| Approval decision | A distinct human decision with verified evidence for exact identity/version/content digest and authority. | Separate immutable evidence/event; not a mutable content field. |
| Source version | Exact upstream source release/revision/artifact used as provenance. | Source Catalog identity/version reference; not Requirement version or ID. |

## 6. Minimum Viable Governed Registry Data Model

The registry stores Requirement-owned content and typed references. It must not duplicate complete source documents: source material remains governed by the Source Catalog and its immutable artifacts. External approval evidence remains in its authoritative evidence/workflow system; the registry stores verifiable references and verification results, not an unauthenticated assertion that approval exists.

**APPROVED — DESIGN DIRECTION:** The registry must represent identity, immutable version, source/provenance and Candidate Boundary bindings, immutable content/integrity references, lifecycle events, supersession, verified approval evidence references, and durable history. These are conceptual record responsibilities, not approved field names or a schema.

**PENDING — IMPLEMENTATION SPECIFICATION:** The following minimum conceptual record inventory and candidate fields are design inputs for a later data contract. Exact required/optional fields, keys, and validation rules need specification and review. “Required” describes the proposal, not an operational schema.

| Record | Required fields | Optional fields | Uniqueness and referential integrity | Mutability | Responsible authority | Validation boundary |
|---|---|---|---|---|---|---|
| Requirement identity | `issuer_namespace`; opaque `logical_id`; creation/allocation event reference; issued-at time; creating authorized principal/service; identity status projection. | Owner/custodian references; external-ID aliases; display label. | Unique `(issuer_namespace, logical_id)`; allocation event must resolve; issuer namespace must be recognized. | ID and issuer immutable; ownership/status changes are events. | Registry authority for allocation; content custodian for metadata proposals. | Registry checks syntax, issuer authority, uniqueness and actor permission; it cannot decide semantic sameness. |
| Requirement version | Issuer + logical ID + sequential `version_id`; immutable content object reference; content schema/model version; canonicalization profile ID; digest algorithm and value; issue event; creator; optional `based_on_version`. | Human-readable title, change summary, declared materiality category, source snapshot labels. | Unique `(issuer_namespace, logical_id, version_id)`; identity and content references resolve; predecessor/base reference must exist if set. | Immutable after issuance; corrections issue a new version or append-only correction event as governed. | Registry controls issuance; content owner submits; human approver decides approval separately. | Structural validation, required source/candidate link resolution and digest recomputation; not semantic approval. |
| Source/provenance binding | Binding ID; Requirement version reference; source catalog identity and exact source version/revision; immutable artifact reference/digest if available; source object/provision and ordered part references; typed source relationships; provenance of selection. | Citation/display title, retrieval time, authority/reference role when governed, multiple source bindings, notes. | Unique binding ID; Requirement version and Source Catalog/version/object references resolve; no source-ID-as-Requirement-ID constraint. | Immutable with version; later binding is new version or append-only correction/change event. | Source owner validates source reference; Requirement content owner maintains binding. | Mechanical reference and pinned-source comparison; human source-fidelity validation remains separate. |
| Candidate Boundary relationship | Requirement version; Candidate Boundary ID and exact immutable candidate revision/snapshot; validation status; boundary decision scope; decision evidence reference. | Rationale for multiple boundaries or relationship kind (derived from, refines, combines) if governed. | Relationship key unique per version/boundary/revision; Candidate Boundary and validation decision resolve. | Immutable per issued version; changed candidate reference is new version/change event. | Candidate Boundary governance authority validates boundary; Requirement owner links it. | Confirms existence/status/reference; does not repeat or elevate boundary approval into Requirement approval. |
| Immutable content reference | Stable object locator/reference; media type; immutable storage version/object generation; byte length; serialization/content model version. | Replicas, retention class, retrieval metadata. | Object reference unique within storage authority; referenced bytes must remain retrievable; version points to one exact object. | Write-once; retention/replication metadata changes only through separately recorded storage events. | Registry/content custodian and storage operator under access policy. | Read-after-write, object version, byte length, canonicalization and digest recomputation. |
| Integrity metadata | Digest algorithm identifier; digest value; canonicalization profile/version; covered field-set/profile; verification event reference and result. | Secondary digest, signature/evidence references, verifier implementation version. | Unique integrity tuple per content object/profile/algorithm; digest must match recomputation; verification event resolves. | Original digest metadata immutable; later verification is an append-only event. | Registry integrity service; independent verifier role for high-assurance checks. | Proves bytes match declared digest under declared profile only; not authenticity, semantic correctness, identity authentication, authority, or approval. |
| Lifecycle event | Unique event ID; identity/version target; event type; occurred/recorded timestamps; actor principal; authority/delegation reference; reason/scope; prior event/base; evidence reference where required. | Effective interval, comments, impact references, supersession edge, system correlation/idempotency key. | Unique event ID; target version resolves; event predecessor and evidence references resolve; allowed transition validated against approved rules. | Append-only; corrections are new events referencing corrected event. | Authorized lifecycle actor; registry enforces permission and event integrity. | Schema/state-machine consistency is mechanical; authority, intent, and any exception require verified human/workflow evidence. |
| Supersession relationship | Relationship ID; predecessor Requirement/version; successor Requirement/version(s); relationship type; authorizing event; rationale; effective semantics if governed. | Source-change/materiality reference; impact-analysis references. | Unique directed edge; both endpoints resolve; no self-edge or cycles; supports one-to-many split and many-to-one merge. | Append-only; reversal/correction is another authorized relationship/event. | Authorized Requirement governance authority. | Graph checks detect structural cycle; humans govern whether succession meaning is correct and its effect. |
| Approval evidence reference | Approval evidence ID/reference; exact issuer/logical ID/version; exact content digest; decision and scope; authorized human principal; authority/delegation reference; verification status/result; event/time reference. | Signature/evidence package locator, workflow transaction, rationale/conditions, verification implementation. | Exact identity/version/digest tuple must equal the target version; evidence ID unique; authority/delegation and actor resolve in trusted governance source. | Reference and verified evidence snapshot append-only; revocation or correction is a new event, never overwrite. | Authorized organizational approver/workflow; registry verifier validates linkage, not human intent. | Must verify human identity, active scoped authority/delegation, exact digest and decision evidence per SAR-CODEX-071. A registry field alone is insufficient. |
| Audit/history trail | Event sequence/IDs; immutable event payload references; actor/time; before/after references; correlation/idempotency key; integrity/retention checkpoint references. | Export/import, replication, backup, reconciliation and administrative-correction events. | Event IDs unique; sequence/checkpoint rules resolve; every mutable projection is derivable from retained events. | Append-only; no destructive edits; redaction, if legally required, must preserve an auditable tombstone and governed reason. | Registry operator and independent audit/records custodian. | Reconciliation, chain/checkpoint verification, retention and retrieval tests; does not itself prove every recorded actor was authorized. |

### Registry boundaries

- The registry owns Requirement logical identities, issued versions, Requirement content bytes or immutable references, typed provenance links, integrity metadata, lifecycle history, and verified approval references.
- The Source Catalog owns source identities, source versions, source currentness, canonical/immutable source references, and source artifact provenance. Registry records reference those objects; they do not copy full catalogs or PDFs.
- Candidate Boundary governance owns candidate identity/revision and source-fidelity decisions. A Requirement version references exact candidate revisions and evidence.
- Assessment records own which exact Requirement version, source version, applicability determination, parameter assignment, and other assessment inputs were used. A registry “current” projection must never rewrite an assessment snapshot.
- Registry validation is layered: schema/format validation; uniqueness and reference integrity; digest verification; source/candidate mechanical consistency; approval evidence verification through trusted interfaces; and human semantic/source/governance decisions. A structural pass is not approval.

## 7. Content Integrity and Canonicalization

### Alternatives

| Approach | Advantages | Limitations |
|---|---|---|
| Hash raw serialized JSON/YAML bytes | Simple and preserves exact file bytes. | Whitespace, key order, line endings, and equivalent serializers change the digest; YAML parser behavior and aliases complicate cross-runtime reproducibility. |
| Hash a canonical JSON representation | Stable across property order/whitespace when all implementations share a profile; well-supported standards exist. | Requires a precisely versioned profile and typed input restrictions; canonicalization does not establish semantic equivalence. |
| Hash normalized domain text or selected fields | Can ignore irrelevant formatting and metadata. | “Equivalent” normalization is hard to define; risks deleting meaningful distinctions or omitting a binding field. Must be explicit and versioned. |

**APPROVED — DESIGN DIRECTION:** Content integrity uses a deterministic canonical representation and an algorithm-qualified cryptographic digest separate from identity, version, lifecycle, and approval. Evaluate RFC 8785 JCS and SHA-256 as candidate choices; neither the exact profile nor the final algorithm is selected.

**PENDING — IMPLEMENTATION SPECIFICATION:** The immutable content field boundary below is an explicit candidate for review. It must be agreed and versioned before hashing is implemented. The digest must not change due solely to lifecycle or unrelated administrative events.

| Digest boundary category | Candidate inclusion/exclusion rule |
|---|---|
| Normative Requirement content | Include the controlled normative representation and all governed meaning-bearing fields: semantic role, scope, conditions, exceptions, qualifiers, and other normative constraints. The final field names and exact set require review. |
| Parameter dependencies | Include source parameter identity/reference and the Requirement's dependency/usage representation and unresolved dependency state. Do not include an organization-specific parameter assignment or its mutable authorization record in this Requirement-content digest; assignment is separately governed. |
| Source/provenance binding | Include source catalog identity, exact source version/revision and immutable artifact reference, source object/provision, ordered source-part references, source relationships, and exact Candidate Boundary identity/revision plus validation-decision reference. The precise reference/digest fields require specification. |
| Identity/version binding | Bind the logical ID and immutable version ID in a defined digest envelope, so a copied digest cannot be reused for another version. Exact envelope shape remains pending. |
| Schema/profile | Include or unambiguously bind the content-model/schema version and canonicalization profile identifier used to interpret the bytes. Compatibility and profile migration rules remain pending. |
| Excluded lifecycle metadata | Exclude lifecycle state, currentness/effective projections, transition events, and supersession projection. Changes to these do not alter the content digest. |
| Excluded approval data | Exclude approval records, signatures, workflow events, identity/delegation verification results, and approval timestamps. Approval evidence separately references the exact version and digest. |
| Excluded mutable administration | Exclude mutable owner assignments, display labels, storage locations, operational timestamps, access/verification status, and unrelated administrative corrections unless explicitly incorporated into a separately reviewed immutable content profile. |

For metadata corrections, a change to an included immutable field requires a new content snapshot and digest, with version/review treatment determined by approved change policy; never overwrite old bytes. A correction solely to excluded administrative metadata is an append-only event and must not change the content digest. Schema/profile migration must preserve old verification rules and historical digests; re-canonicalization or changed field boundaries require an explicit compatibility/migration record and must not silently replace prior values.

The exact field set, parameter/provenance subfields, identity/version envelope, Unicode/data-type rules, serializer behavior, exclusions, correction handling, and migration compatibility are **PENDING — IMPLEMENTATION SPECIFICATION** and require separate review before hash implementation.

Candidate deterministic serialization details for later review: UTF-8; reject duplicate JSON object member names; preserve Unicode scalar sequences without silent NFC/NFD normalization; reject invalid Unicode; restrict numbers to safe integers or schema-constrained decimal strings; disallow NaN, infinity, and ambiguous coercions; preserve meaningful array order and sort only semantically unordered collections. Do not normalize source text, citations, or normative punctuation as a hashing convenience. These are proposed profile details, not final rules.

Bind the canonicalization profile ID, digest algorithm identifier, and schema/content-model version to the integrity record. A schema upgrade does not rewrite old content: retain its original profile and verifier; migration creates a new immutable version only when content representation changes under governed change control. Verify imported content by parsing under the declared strict profile, recomputing the digest, and comparing it with the exported digest before registry admission.

**PENDING — IMPLEMENTATION SPECIFICATION:** Retain SHA-256 and an algorithm-qualified value such as `sha-256:<lowercase-hex>` as candidates for separate selection. Algorithm identifier, output encoding, agility, and historical verification policy remain open; no digest is generated here.

### Integrity is not approval

- **Hash integrity** detects whether the covered canonical content differs from the bytes/projection used to compute the digest, assuming the algorithm and implementation are sound.
- **Digital signature** can show that a signing key signed a payload, subject to key custody and verification. It does not alone show the key holder was the authorized approver or that the decision was human-authorized.
- **Authentication** verifies the human principal through an approved identity mechanism.
- **Authorization** verifies that principal's active organizational role/delegation and decision scope at decision time.
- **Human approval** is the explicit authorized decision with rationale/scope and verifiable evidence for the exact identity, version, and content digest.

A digest alone proves none of authentication, authorization, signature provenance, semantic correctness, or human approval. Approval evidence must bind the exact digest and identity/version under SAR-CODEX-071. This increment implements no hash or signature.

## 8. Allocation and Concurrency

### Required transaction semantics

Identity generation and registration authority are separate. A locally generated UUID is only a candidate token until an authorized registry transaction allocates/registers it. The allocator must check the caller's organizational authority; an identifier's uniqueness does not authorize its content or approval.

**APPROVED — DESIGN DIRECTION:** Registration must provide unique identity/version registration, atomic or equivalently controlled updates, concurrency protection, idempotent retries, referential integrity, authenticated and authorized changes, append-only governance events, durable history, integrity verification, recovery/reconciliation, and portable export/import. No specific database, cloud service, API host, or storage technology is required solely because it appears in this design. A repository-backed approach is eligible if it demonstrates the same guarantees for its intended operating context.

**PENDING — IMPLEMENTATION SPECIFICATION:** A central transactional database-backed service is one implementation candidate. If selected, identity creation/allocation event/namespace check/idempotency result should commit atomically; version issuance should serialize per-identity sequencing and durably bind content, integrity metadata, and issuance event. Enforce the selected uniqueness keys. Collision handling rejects/quarantines rather than merging records automatically.

**PENDING — IMPLEMENTATION SPECIFICATION:** For a service-based implementation, use an idempotency key scoped to authenticated principal/operation. Repeating an identical request should return the original committed identity/version result; reusing the key with a different payload should be rejected and audited. After timeout or partial failure, clients should resolve the idempotency key before retrying. A failed pre-commit transaction must not issue a version; a committed transaction with lost acknowledgment must be safely retrievable. Durable event/content writes need an outbox or equivalent recoverable protocol so committed references cannot silently point to missing bytes. Recovery/reconciliation should detect orphaned objects and dangling references and quarantine them rather than silently repairing semantic data. These are service-pattern examples, not required technologies.

### Allocation alternatives

| Mechanism | Concurrency and collision handling | Offline/distributed behavior | Failure and authority concerns |
|---|---|---|---|
| A. Repository-controlled allocation | Serialized through protected branch merge and a uniqueness check over all registered records; concurrent PRs must recheck against latest main at merge. Merge conflict or duplicate must reject, not renumber silently. | Drafts can be prepared offline; production issuance needs an online authorized merge/registry gate. | Git history is useful audit provenance but branch permissions, merge policy, and identity/delegation are not inherently a transaction or trusted approval service. Concurrent/large registry files become contentious. |
| B. Database-backed transactional allocation | Unique indexes, transaction isolation, per-identity sequence lock/CAS, and idempotency provide atomic registration and version issuance. | Online central service required initially; offline work remains draft/proposal with no production ID. | Requires highly available service, access controls, backups, recovery, audit export, and proven authorization integration. A DB administrator must not be able to forge approval evidence. |
| C. Distributed unique IDs with governed registration | UUIDv4/v7 generation makes accidental collision extremely unlikely; central registration still checks uniqueness and authority. | Best offline and multi-site availability; registration can reconcile later. | Generated ID does not establish namespace ownership, authorized creation, semantic identity, or approval. Collision/import conflict needs quarantine; clocks (v7), entropy, issuer governance, and reconciliation matter. |

**APPROVED — DESIGN DIRECTION:** Whichever mechanism is chosen must satisfy the registry guarantees above and separate identity allocation/version registration from authority to use or approve a Requirement. A successful allocation or version registration is not authorization for the Requirement. A newest version is not automatically approved or current.

**PENDING — IMPLEMENTATION SPECIFICATION:** Mechanism B (database-backed transactional allocation) is a candidate initial implementation; A (repository-controlled allocation) and C (distributed unique IDs with governed registration) remain alternatives. Offline authoring may produce non-authoritative drafts; whether offline production identity registration is supported remains open. A protected repository may be used in production only if it demonstrably satisfies the required guarantees for that context; it is not rejected categorically.

**PENDING — IMPLEMENTATION SPECIFICATION:** Registry operator/authority and delegation, hosting/storage platform, availability/recovery objectives, namespace model, whether distributed/offline issuance will ever be allowed, and repository/database source-of-truth relationship.

### Retry, conflict, and reconciliation rules

- Duplicate ID under same issuer: reject transaction, raise security/consistency alert, preserve request evidence, and retry only with a fresh authorized allocation.
- Concurrent versions from one base: serialize sequence assignment; detect stale base and require explicit rebase/review or governed branch handling.
- Retry with same idempotency key and same payload: return same committed result; different payload: reject and audit.
- Partial persistence: keep state pending/quarantined until immutable content, digest, identity/version row, and issuance event reconcile; never advertise an incomplete version as issued.
- Registry restore/migration: compare event log, indexes, object store, checkpoints, and exports; pause writes if reconciliation cannot establish a single consistent state.
- Unauthorized identifier creation: quarantine as external/unregistered data; do not import it as an authorized SAR identity or treat possession of the UUID as delegation.

## 9. Lifecycle, Events, and Supersession

### Event-sourced history and projections

**APPROVED — DESIGN DIRECTION:** Preserve lifecycle and governance history as append-only events; do not mutate historical Requirement content or let lifecycle changes alter its content digest. Registry state must remain distinct from human approval, parameter authorization, applicability, and assessment execution eligibility.

**PENDING — IMPLEMENTATION SPECIFICATION:** Event-sourced storage, projection/rebuild mechanics, event vocabulary, and correction encoding are options for later specification. A read projection, if used, should identify its event cutoff and be reconstructable from durable history. Corrections append a new event rather than silently editing prior history.

Illustrative event categories (not an approved enumeration): identity registered; draft submitted; version issued; review started/returned/completed; approval reference verified; approval refused/revoked; version marked review-required; version withdrawn; version superseded; successor linked; currentness reviewed; administrative correction; import/adoption; integrity check; and registry recovery/reconciliation. Approval events require verified identity-backed evidence and exact content digest. Review, currentness, approval, and execution eligibility remain distinct event dimensions.

Lifecycle state vocabulary, event schema, valid transition matrix, effective-time semantics, correction authority, event signing/retention, and proof of append-only behavior are **PENDING — IMPLEMENTATION SPECIFICATION**. A database's ordinary mutable row is not an append-only audit trail without access controls, retention, tamper evidence, and independent audit.

### Version and temporal meanings

- **Current version:** a registry projection selected under an explicitly governed currentness policy; it is not necessarily the greatest version number and does not imply approval.
- **Effective version:** a version whose authorized effective-time decision applies at a specified time and scope. No effective-date policy is inferred here.
- **Approved version:** exact version with verified identity-backed approval evidence, active authority/delegation at decision time, matching content digest, and no superseding/revocation event that the governing policy says changes its use. Approval is not applicability or execution eligibility.
- **Superseded version:** version with an authorized, directed succession event naming successor(s); it remains immutable and available to historical consumers.
- **Withdrawn version:** preserved version whose authorized event records withdrawal and reason; withdrawal is not deletion and need not imply a replacement.
- **Historical assessment version:** exact identity/version/digest recorded in the assessment's immutable input snapshot, regardless of later currentness, approval, or supersession changes. Re-evaluation is a new assessment event, not a retroactive mutation.

No version is automatically approved/effective because it is newest, and no registry status alone authorizes execution. An assessment resolver would have to apply separately governed eligibility requirements and pin the exact resolved state/event snapshot.

**APPROVED — DESIGN DIRECTION:** Keep these steps distinct and ordered by their own governance, not by identifier creation:

1. Logical ID allocation.
2. Immutable version registration.
3. Source-fidelity validation.
4. Human Requirement review.
5. Authenticated Requirement approval.
6. Effective/current lifecycle determination.
7. Source authority or benchmark role determination.
8. Parameter assignment authorization.
9. Assessment-specific applicability determination.
10. Assessment execution eligibility determination.

Completing an earlier step does not imply a later one. A registered version can remain proposed, unapproved, unresolved, and non-executable.

### Supersession graph

Represent succession as explicit directed relationships between exact versions, with an event authorizing the relation. Allow one predecessor to have multiple successors (split) and multiple predecessors to converge on one successor (merge). Enforce no self-reference and no directed cycles. Do not infer supersession from version order, similar wording, a new source version, or a changed title. A corrected or reversed succession is a new authorized event that explains prior impact; do not erase the original edge. Whether a version can be superseded without an approved successor, and how conflicting effective branches resolve, require separate governance decisions.

## 10. SI-12(3) Provisional Example Migration Mapping

No production identity/version is assigned by this table. The existing file remains unchanged and non-operational.

| Existing provisional example field/value | Proposed registry mapping | Migration treatment |
|---|---|---|
| `identity.logical_id: EXAMPLE-REQ-0001` | Placeholder `logical_id` slot on an identity record. | Do not import as a production ID; preserve only as legacy/example alias in a migration audit if needed. Allocate no replacement in this design. |
| `identity.version: EXAMPLE-VERSION-1` | Placeholder version reference. | Not a production sequence. A future authorized migration creates a new registered identity/version and records the example-to-record migration provenance without overwriting the example. |
| `record_schema_version: 0.1-provisional` | Source-record format/schema metadata. | Retain as origin format in migration evidence; translate fields under a versioned migration map and validate losslessly. |
| Source identity `nist-sp800-53-rev5`, source release `5.2.0`, pinned revision `78650f02ad9321bb7b817846f8fbd4f2bcd620de`, artifact path | One or more source/provenance bindings referencing Source Catalog source/version/artifact. | Verify each reference against the committed manifest and exact source slice; do not copy the full NIST catalog into the Requirement Registry. |
| Source object `si-12.3`, normative part `si-12.3_smt`, parent `required` relation to `#si-12` | Source provision/ordered part/relationship references. | Preserve source-native IDs and source graph as provenance, not SAR Requirement identity. |
| Candidate Boundary `cbr-nist-sp800-53-rev5-si-12-3-smt`, `VALIDATED`, decision reference | Candidate Boundary relation to exact candidate revision and boundary-fidelity decision. | Resolve and preserve validated boundary and pinned provenance; do not treat its decision as Requirement approval. |
| Controlled representation | Immutable Requirement content candidate. | Re-review against exact boundary and source before any authorized version issuance; migration does not promote it. |
| Parameter dependency `si-12.3_prm_1`, `UNRESOLVED` | Normative parameter dependency reference/state in immutable content. | Preserve unresolved state exactly; no parameter assignment or guessed value. |
| Lifecycle `PROPOSED`; approval `NOT_APPROVED` | Lifecycle events/projection and absence of approval evidence. | Preserve as proposed/non-approved; create no approval event and do not infer approval from registry import. |
| Applicability `UNRESOLVED / GOVERNED RULE NOT YET POPULATED`; source role `NOT_DETERMINED` | Separate assessment applicability/source-role records, not Requirement registry identity/version fields. | Preserve unresolved as example metadata or migration note; create no applicability record/determination. |
| Execution `NON_EXECUTABLE`; dependent parameter evaluation blocked | Execution eligibility boundary outside identity/version registry. | Preserve non-executable example scope; introduce no execution logic. |
| Existing two history references | Source-boundary validation reference and proposal-origin event references. | Translate dates/references as provenance only; add no Requirement approval evidence. |

**PENDING — IMPLEMENTATION SPECIFICATION:** Future migration requires an authorized schema/identity convention, confirmed identity allocator, source/Candidate Boundary resolution, explicit mapping version, immutable input/output snapshots, row-by-row validation, digest generation under a reviewed profile, and an auditable migration event. Any imported record must initially remain proposed/unapproved and preserve unresolved parameter/applicability/non-executable state. A distinct authorized human review and approval would be required to change that status. Migration is not authorized by this design approval; do not change or “upgrade” the checked-in example in this increment.

## 11. Security and Failure Analysis

No risk scores or thresholds are assigned.

| Failure mode | Prevention | Detection | Recovery | Audit evidence |
|---|---|---|---|---|
| 1. Duplicate logical IDs | Unique constraint on issuer-qualified logical ID; allocate only through authorized transaction; never trust format uniqueness alone. | Constraint violation, periodic full-registry duplicate scan, reconciliation across imports/replicas. | Reject/quarantine conflicting registration; preserve both source packages; authorized namespace reconciliation and explicit crosswalk, never silent merge. | Allocation request/idempotency key, issuer/authority check, constraint result, reconciliation event. |
| 2. Version overwrite | Write-once immutable content object; unique version key; prohibit update/delete on issued bytes; append correction/new version. | Compare stored digest/object generation against issuance record; immutable-storage audit and periodic retrieval verification. | Restore exact bytes from trusted replica/backup; quarantine registry if integrity cannot be restored; issue correction as new version after review. | Original event/digest, storage object version, access log, restore/reconciliation evidence. |
| 3. Unauthorized registration | Authenticate principal and verify scoped current delegation for allocation and content submission; separate allocation from Requirement approval. | Alert on unknown issuer, role/delegation failure, anomalous registration, or missing allocation event. | Quarantine identity/version, revoke access, preserve evidence, investigate; only authorized decision can adopt, reject, or revoke. | Principal, identity provider result, delegation snapshot/version, request, authorization decision, incident/correction events. |
| 4. Concurrent allocation collision | Database uniqueness and transaction isolation; idempotency keys; serial per-identity version allocation. | Unique-index conflict, duplicate-key alarms, stale-base checks, concurrent request telemetry. | Roll back losing transaction; return same result for idempotent retry or generate new identity; review conflicting content rather than merge. | Transaction IDs, idempotency key, base version, retry/conflict record and resulting allocation event. |
| 5. Digest mismatch | Strict canonicalization profile, algorithm identifier, immutable bytes, recomputation before approval/import/use. | Verify at write, read, export/import, periodic integrity sweep; compare digest and canonicalization/schema version. | Quarantine affected object and dependent approval references; restore verified copy or issue corrected version; never “fix” digest metadata in place. | Expected/observed digest, algorithms/profile, verifier software/version, time, object reference, incident and recovery events. |
| 6. Source-provenance substitution | Bind exact source catalog identity/version/revision/artifact and source parts to immutable Requirement content; validate refs against trusted Source Catalog. | Re-resolve pinned references and compare source/candidate snapshot; detect changed path, revision, part set, or digest. | Mark affected versions for governed review; retain old source links; create new provenance/version and re-review where required. | Source/candidate IDs and revisions, source integrity evidence, comparison, reviewer decision, affected-version list. |
| 7. Forged lifecycle event | Authenticate actor, enforce delegated action scope, protect event store/write paths, separate custodian from decision authority; bind event to target/digest. | Verify event signature/identity/delegation; detect sequence gaps, invalid transitions, duplicate IDs, or unexpected administrative writes. | Freeze projection, preserve suspect events, rebuild from verified history/checkpoint, revoke compromised credentials, append authorized correction. | Raw event, identity/delegation verification, sequence/checkpoint, access logs, correction and recovery records. |
| 8. Supersession cycle | Validate directed graph transactionally for self-edges and cycles; require authorized succession event and resolved endpoints. | Periodic graph integrity check and resolver cycle detection; reject incomplete/conflicting edges. | Quarantine invalid edge/projection; preserve historical event; append authorized correction/reversal and recompute projections. | Edge endpoints, graph snapshot, validator output, authorizing authority/evidence, remediation events. |
| 9. Lost historical version | Immutable/versioned object retention, replicated backup, tested restore, assessment references pin exact version/digest. | Scheduled inventory and restore/retrieval test; detect dangling references and missing object versions. | Restore from verified immutable backup/export; if unavailable, mark history unreproducible and block claims of replay; never reconstruct silently from latest. | Retention policy/version, backup/checkpoint manifests, restore result, missing-object incident, affected assessments. |
| 10. Imported Requirement ID collision | Issuer-qualified identity, verified origin/export manifest, uniqueness check, explicit external-ID crosswalk. | Import preflight compares issuer/id/version/digest and existing registry ownership/content. | Quarantine import; establish whether same origin, duplicate export, or conflicting claim; map only with authorized event; do not silently rekey. | Origin signature/manifest, import request, collision report, crosswalk/adoption decision and authority. |
| 11. Approval evidence attached to wrong version | Evidence record must include issuer/logical ID/version and exact digest; verifier compares all fields to immutable target before linking. | Approval verification and resolver reject mismatched identity/version/digest; periodic linkage audit. | Remove from active projection via append-only correction; preserve evidence and mislink event; obtain correct decision/evidence before approval use. | Evidence package/workflow ref, target tuple, verifier result, correction event, new decision if any. |
| 12. Registry corruption or rollback | Least privilege, immutable audit/event storage, transaction logs, independent backups/checkpoints, separation of administration and approval, tested recovery. | Compare replicated/checkpointed event sequence and hashes; monitor unexpected rollback, gaps, altered projections, or replica divergence. | Halt writes, preserve forensic snapshot, restore from verified checkpoint/log, reconcile every version/reference, require authorized recovery signoff before resuming. | Checkpoint manifests, replication/backup logs, incident timeline, integrity tests, reconciliation and recovery approval. |

## 12. Minimum Viable Implementation Architecture

**APPROVED — DESIGN DIRECTION:** The minimum registry architecture is capability-based and technology-neutral. It must provide:

1. Controlled creation and unique registration of opaque logical identities and immutable versions.
2. Atomic or equivalently controlled writes, concurrency protection, idempotent retries, and safe conflict/partial-failure handling.
3. Referential integrity among Requirement versions, source/provenance bindings, Candidate Boundary revisions, lifecycle events, supersession relationships, and approval evidence references.
4. Immutable content preservation and integrity verification under a separately reviewed canonical content boundary/profile.
5. Authenticated and authorized changes, with identity allocation/version registration kept separate from source fidelity, review, human approval, lifecycle effectiveness, parameter authorization, applicability, and execution eligibility.
6. Append-only governance events, durable historical retrieval, recovery/reconciliation, and portable export/import without implicit approval.

**PENDING — IMPLEMENTATION SPECIFICATION:** A transactional relational database, authenticated API, and immutable object storage are possible implementation options, not mandatory technologies. Other storage/service patterns, including repository-backed implementation, may be considered if they demonstrably provide the same guarantees for the intended operating context. Hosting, database, cloud provider, API platform, and storage technology remain unselected.

Any implementation must keep source documents in the Source Catalog/source artifact system rather than duplicating complete documents in the Requirement Registry. Approval evidence must be verifiable and bound to the exact identity/version/content digest; a mutable `approved: true` field is insufficient. Export/import verification must not create approval or execution eligibility implicitly. Assessment-specific use remains a distinct resolution using exact versions and inputs.

**PENDING — IMPLEMENTATION SPECIFICATION:** Operator, trust boundaries, identity/delegation integration, retention/recovery objectives, segregation of duties, system-of-record contract, and any repository mirror remain to be specified.

## 13. Future Production Hardening

Future hardening may include multi-region high availability; namespaced federation; offline draft clients; authorized distributed UUID generation with central registration; independently verifiable signed export manifests; key rotation/revocation and trusted timestamps; immutable/WORM audit retention; tamper-evident event checkpoints; change-impact indexing; source currentness notification; historical assessment dependency queries; disaster-recovery exercises; import quarantine and external identity crosswalks; privacy-preserving audit access; schema/canonicalization migration tooling; and independent conformance/reproducibility tests across runtimes.

Hardening must not collapse registry state into assessment execution authority. A registry can establish the existence and integrity of a version and link verified approval evidence; it cannot alone establish source applicability, parameter resolution, expected safeguards, evidence sufficiency, or eligibility for a particular assessment.

**PENDING — IMPLEMENTATION SPECIFICATION:** Production service levels, resilience, audit retention, geographic replication, external federation, regulated records, and signing/trusted-time controls require separate specification and review, including assignment of operational risk ownership.

## 14. Open Implementation Decisions

The approved design directions are recorded in Section 15. The following detailed specifications remain pending; their implementation options are not selected merely because they appear here:

- Identifier syntax/version (UUIDv4 proposal), issuer namespace and uniqueness domain, global versus federated registry authority, and offline behavior.
- Version wire format, draft revision model, sequence allocation/retirement semantics, branch/rebase policy, and treatment of source-binding-only changes.
- Registry operator, system of record, database/content store technology, transaction/availability model, API and access-control contract.
- Canonical content envelope, strict JSON parsing rules, RFC 8785 profile details, Unicode handling, numeric constraints, array/set treatment, and schema/model version binding.
- Digest algorithm (SHA-256 proposal), qualified encoding, algorithm migration and historical verification support.
- Lifecycle event type vocabulary, state projection, effective-time/currentness rules, event immutability/tamper-evidence and correction authority.
- Supersession semantics for splits/merges, branches, withdrawal without replacement, conflicting successors, and effective intervals.
- Source and Candidate Boundary revision identity formats/resolution and standards for immutable artifact references.
- Approval evidence service/format, identity proofing, delegation lookup, verifier trust roots, and binding/verifying signatures or workflow events to exact content digest.
- Import/export trust, issuer preservation, adoption/crosswalk authority, collision resolution, and migration of legacy examples.
- Migration governance, schema evolution and canonicalization-profile compatibility, retention, backup, restore, reconciliation, and operational audit responsibilities.

## 15. CISO Decision Register

### SAR-CODEX-072 disposition

| Decision field | Recorded disposition |
|---|---|
| Workflow | SAR-CODEX-072 |
| Authority | DDS CISO |
| Decision | **APPROVED — DESIGN RECOMMENDATIONS WITH THREE CLARIFICATIONS** |
| Additional conditions | None |
| Provenance | Explicit DDS CISO disposition in the SAR-CODEX-072 review conversation. |
| Decision date | Unresolved; no explicit date is present in the authoritative approval record. The commit date is not the approval date. |
| Scope | Requirement Identity and Version Registry design recommendations only. No individual Requirement approval and no implementation authorization. |

### Binding clarifications

| Clarification | Approved binding direction |
|---|---|
| A. Technology-neutral registry | Require unique registration; immutable versions; atomic or equivalently controlled registration; concurrency protection; idempotent retries; referential integrity; authenticated and authorized changes; append-only governance events; durable history; integrity verification; recovery/reconciliation; and export/import portability. Do not require a particular database, cloud service, API hosting platform, or storage technology solely because it appeared in this design. Transactional relational storage, authenticated APIs, immutable object storage, and repository-backed approaches are options; repository-backed designs must demonstrate equivalent guarantees for their intended context. |
| B. Explicit canonical content boundary | Define and review the exact immutable Requirement content field set before implementing hashing: normative fields; parameter dependency fields; source/provenance bindings; identity/version treatment; schema/profile version; Unicode/data-type normalization; deterministic serialization; digest algorithm identifier; lifecycle, approval, and mutable administration exclusions; metadata-correction handling; and migration/compatibility rules. RFC 8785 canonical JSON and algorithm-qualified SHA-256 remain recommendations to evaluate, not final selections. Unrelated lifecycle or administrative events must not silently change a content digest. A digest is not a signature, approval, authorization, or evidence of source fidelity. |
| C. Identity is not authorization | Separate logical ID allocation, immutable version registration, source-fidelity validation, human Requirement review, authenticated Requirement approval, effective/current lifecycle determination, source authority/benchmark role, parameter assignment authorization, assessment-specific applicability, and assessment execution eligibility. Registration does not authorize use; newest does not automatically become approved or current. A registered version may remain proposed, unapproved, unresolved, and non-executable. |

The approval covers the design recommendations subject to these clarifications. Detailed implementation specifications remain pending, and operational execution is not authorized.

### Design decision register

Technical selections below remain pending unless specifically identified as approved design direction. Original alternatives and rationale are retained. No row creates a production identity, version, digest, approval, or implementation permission.

| Decision | Recommended option | Alternatives considered | Reasoning | Operational consequences | Dependencies | Decision status |
|---|---|---|---|---|---|---|
| Production identifier syntax | **PENDING — IMPLEMENTATION SPECIFICATION:** lowercase canonical UUIDv4 is one candidate, with issuer qualification if federation is selected. | UUIDv7; central sequence/prefix; source-derived/composite identifier; other opaque random ID. | Portable and source-independent; no timestamp/source meaning; collision can be checked. | IDs are not human-readable; UUID generation does not authorize registration. | UUID grammar, namespace model, allocator, uniqueness domain, authorization. | **PENDING — IMPLEMENTATION SPECIFICATION** |
| Logical ID uniqueness scope | **APPROVED — DESIGN DIRECTION:** uniqueness is controlled within an authorized registration domain; exact global/federated scope remains pending. | One global DDS namespace; globally registered issuer namespaces; per-organization local uniqueness only. | One authority is simple; issuer qualification may support federation without silent collision. | Cross-organization import requires issuer verification and collision handling; local uniqueness alone is insufficient for federation. | Registry operator, issuer/namespace authority, migration/import policy. | **PENDING — IMPLEMENTATION SPECIFICATION** |
| Immutable version format | **APPROVED — DESIGN DIRECTION:** separate immutable sequential versions per logical ID and separate content-integrity reference. Exact positive integer/string representation remains pending. | UUID version; content hash as sole version; date/release label; mutable `latest`. | Readable succession and stable historical reference while digest independently checks integrity. | Requires controlled per-ID sequencing; gap/reuse and draft revision policies remain pending; digest never replaces version. | Transaction or equivalent control, content envelope/digest profile, rebase/succession rules. | **APPROVED — DESIGN DIRECTION; PENDING — IMPLEMENTATION SPECIFICATION** |
| Registry authority | **APPROVED — DESIGN DIRECTION:** identity/version changes require authenticated and authorized authority, distinct from human Requirement approval. Named custodian/operator remains pending. | Repository maintainers; per-organization registries; federated issuer custodians. | Separates administrative registration from approval; preserves delegated organizational authority. | Operator can allocate/store but cannot approve content merely by operating the registry. | Named operator/custodian, delegation policy, identity source, service governance. | **PENDING — IMPLEMENTATION SPECIFICATION** |
| Registry storage approach | **APPROVED — DESIGN DIRECTION:** technology-neutral guarantees in Clarification A; no storage technology is mandated. | Transactional relational store plus object storage; repository-backed store; document store; distributed ledger. | Guarantee-based design avoids premature technology coupling while retaining uniqueness, history, and recovery requirements. | Selected platform must demonstrate all required guarantees for its operating context. | Hosting/operator, transaction/equivalence evidence, retention/availability requirements. | **PENDING — IMPLEMENTATION SPECIFICATION** |
| Canonicalization standard | **APPROVED — DESIGN DIRECTION:** define and review the exact immutable content boundary before hashing; evaluate RFC 8785 JCS. | Raw byte hash; custom sorted-key JSON; canonical CBOR; normalize-and-hash domain fields. | Deterministic cross-runtime representation is needed; explicit field boundary prevents unrelated metadata affecting digest. | Requires reviewed field set, schema/profile, Unicode/numeric policy, exclusions, and conformance vectors. | Content schema, field projection, Unicode/data-type rules, compatibility and migration tests. | **APPROVED — DESIGN DIRECTION; PENDING — IMPLEMENTATION SPECIFICATION** |
| Digest algorithm | **PENDING — IMPLEMENTATION SPECIFICATION:** retain algorithm-qualified SHA-256 as a candidate, not a selected algorithm. | SHA-512; SHA-3; BLAKE2/3; multiple digests; storage-native object checksum only. | Widely implemented and independently recomputable; algorithm must not be confused with identity/signature. | Requires agility and historical verification support. | Canonical boundary/profile, algorithm policy, export/import verification and migration policy. | **PENDING — IMPLEMENTATION SPECIFICATION** |
| Allocation and concurrency | **APPROVED — DESIGN DIRECTION:** authorized, unique, atomic-or-equivalent registration; concurrency protection, idempotency, retry/recovery, and reconciliation are required. | Protected-repository serialization; transactional database; distributed UUID generation plus governed registration; leased sequence blocks. | Required guarantees are stable across technologies and separate registration from approval. | Selected mechanism must provide evidence of equivalent guarantees; no automatic approval. | Registry authority, auth/delegation, transaction/equivalent controls, retry/reconciliation protocol. | **APPROVED — DESIGN DIRECTION; PENDING — IMPLEMENTATION SPECIFICATION** |
| Lifecycle event representation | **APPROVED — DESIGN DIRECTION:** append-only governance events and durable history; lifecycle remains separate from immutable normative content and digest. | Mutable status row; Git history; signed event log; event sourcing with snapshots. | Preserves history and prevents lifecycle events changing normative content integrity. | Exact event model, projections, retention, and authority checks remain to be specified. | Lifecycle vocabulary, storage/tamper controls, actor/authority model, effective-time semantics. | **APPROVED — DESIGN DIRECTION; PENDING — IMPLEMENTATION SPECIFICATION** |
| Import/export identity rules | **APPROVED — DESIGN DIRECTION:** support portable export/import with identity and history preserved; imports do not implicitly authorize or approve. | Always re-key on import; trust any globally unique UUID; merge equal content IDs; repository-only imports. | Preserves provenance; content equality does not prove same governance identity. | Collision resolution, issuer trust, and adoption/crosswalk remain to be specified. | Namespace policy, trust/evidence format, import authority and audit process. | **APPROVED — DESIGN DIRECTION; PENDING — IMPLEMENTATION SPECIFICATION** |
| Migration strategy | **APPROVED — DESIGN DIRECTION:** preserve the provisional example and all unresolved/unapproved states; no automatic registration or promotion. | In-place mutation of YAML examples; bulk auto-registration; discard placeholders; manual recreation without mapping. | Maintains provenance and prevents confusing examples with production identities. | Migration remains unauthorized until separately specified and authorized; no SI-12(3) approval. | Schema/ID/version conventions, verified source/boundary snapshot, migration authority and procedure. | **PENDING — IMPLEMENTATION SPECIFICATION; NOT AUTHORIZED — OPERATIONAL EXECUTION** |

## 16. Recommended Implementation Sequence

All steps require their own authorization; this list is not permission to begin them.

1. Treat the SAR-CODEX-072 disposition and clarifications as approved design direction; obtain any separate authorization required to begin implementation specification.
2. Specify the logical data contract, exact record responsibilities, uniqueness/reference rules, issuer scope, and identity/version wire formats without allocating production IDs.
3. Define and review the canonical immutable field set, exclusions, normalization/serialization profile, schema compatibility, digest identifier, metadata correction behavior, and cross-runtime test vectors before implementing hashing.
4. Compare registry technologies against the approved guarantees; specify authorization/delegation, atomic-or-equivalent writes, concurrency, idempotency, retry/recovery, import/export, event history, and audit retention independent of platform.
5. Implement the schema and validators as a separately authorized increment; test uniqueness, concurrent allocation, stale proposal rebase, immutability, provenance substitution, digest/import mismatch, event forgery, supersession DAG, backup/restore, and historical retrieval with synthetic records.
6. Conduct security/privacy/records review, access-control and separation-of-duties verification, disaster-recovery exercises, and independent import/export interoperability tests.
7. Migrate the SI-12(3) example only under a separately approved migration plan. Preserve its validated boundary and pinned source provenance; keep the Requirement proposed/unapproved, `si-12.3_prm_1` unresolved, applicability unresolved, and execution non-executable until each is independently governed.
8. Populate no production Requirement or assessment eligibility until distinct human Requirement approval and all separately governed applicability, currentness/source-authority, parameter, and execution prerequisites are satisfied.

## Validation and Scope Record

This document records the SAR-CODEX-072 approved design recommendations and three binding clarifications. It does not create a production Requirement ID or version, registry or allocator record, digest or signature, individual Requirement approval, parameter assignment, applicability determination, or assessment execution logic. The provisional SI-12(3) example and all existing schemas, validators, tests, source artifacts, and governance documents remain unchanged.

The design approval does not approve SI-12(3), select every implementation detail, or authorize operational execution. Detailed specifications remain pending and implementation requires separate authorization. **STOP POINT: await CISO authorization before operational implementation or SAR-CODEX-073.**
