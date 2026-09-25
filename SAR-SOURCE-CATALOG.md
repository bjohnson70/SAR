# SAR Source Catalog

## Purpose

This document defines the conceptual model for identifying, registering, versioning, validating, and maintaining authoritative and reference sources used by Software Assessment and Review (SAR).

The Source Catalog is not merely a bibliography. It is a controlled registry that enables SAR to determine:

- what source exists;
- who publishes or maintains it;
- what kind of authority or reference source it represents;
- where the canonical source is located;
- which version or revision is current;
- which version or revision SAR actually used;
- when SAR last verified the source;
- whether the source has changed;
- whether a change may affect SAR logic or existing assessments;
- whether machine-readable source material exists; and
- how a source relates to later mappings without itself asserting applicability.

This document does not create a machine-readable registry schema, source ID convention, automated synchronization, control catalog, applicability rules, or requirement mappings.

## Governing Principle

> SAR must know both what the current authoritative source is and exactly what version of that source supported a particular assessment.

These are different concepts. A source may change after an assessment is completed. A later source revision must not silently rewrite the historical basis of an earlier SAR assessment. Likewise, an old assessment must not cause SAR to assume an obsolete source remains current for a new assessment.

## Source Catalog and Applicability

The Source Catalog identifies and describes sources. It does not, by itself, establish that a source applies to a particular SAR.

```text
Control Source
    !=
Applicability Basis
```

Registering a source means that SAR knows about the source. It does not mean that the source applies to every assessment. Actual applicability must be established later through supported applicability logic.

## Source Categories

The catalog should support conceptual categories broad enough to represent:

- laws;
- regulations;
- authoritative government guidance;
- security and privacy frameworks;
- standards;
- State policies;
- departmental policies;
- contractual provisions;
- Business Associate Agreements and other governing agreements;
- cloud requirements;
- AI requirements or guidance;
- technical standards;
- machine-readable control catalogs;
- organizational procedures;
- authoritative training or reference material; and
- other approved reference or benchmark sources.

These are conceptual categories, not an exhaustive legal inventory or a statement of applicability.

## Initial Known Source Families

The following are source families or candidate sources already known to the SAR architecture and may later be registered in the catalog:

- NIST SP 800-53 Rev. 5;
- NIST OSCAL content associated with applicable NIST control material;
- HIPAA;
- HITECH;
- applicable Business Associate Agreements or governing agreements;
- California State security and privacy requirements;
- California State IT requirements;
- California cloud provisions;
- California State AI requirements or guidance;
- DDS policies and standards;
- the authoritative source for the DDS 19 data-element concept; and
- other contractual or organizational requirements identified through assessment.

These are source families or candidate sources only. This document does not populate detailed requirements or invent citations, URLs, revision dates, effective dates, control numbers, statutory sections, or document metadata. It does not assert that any source applies to Regional Centers, Business Associates, vendors, or every SAR.

### HIPAA Safe Harbor Identifier Authority

For the initial SAR HIPAA Safe Harbor identifier reference, preserve two distinguishable source authorities:

**Regulatory authority**

- authority: 45 CFR § 164.514(b)(2);
- source role: federal regulatory authority;
- relationship to SAR artifact: supports [HIPAA-IDENTIFIERS.md](HIPAA-IDENTIFIERS.md);
- status: registered source authority, not a universal applicability determination.

**Explanatory guidance**

- publisher: U.S. Department of Health and Human Services, Office for Civil Rights;
- title: *Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule*;
- source role: authoritative explanatory guidance;
- relationship to SAR artifact: explains the Safe Harbor identifier categories preserved in [HIPAA-IDENTIFIERS.md](HIPAA-IDENTIFIERS.md);
- relationship to regulation: explanatory guidance for 45 CFR § 164.514(b)(2), not the regulation itself.

No publication date, revision, version, canonical URL, immutable retrieval reference, source owner, or applicability conclusion is asserted here because none is established by the registered repository evidence. Registration does not establish that HIPAA applies to every SAR or that identifier presence establishes PHI.

## Source Identity

SAR should eventually retain the following conceptual information for each catalog source where available and relevant:

- stable SAR source identifier;
- source title;
- source family;
- source type or category;
- publisher or issuing authority;
- canonical source location;
- authoritative versus reference or benchmark status;
- jurisdictional or organizational scope where useful;
- version;
- revision;
- publication date;
- effective date;
- expiration date where applicable;
- status;
- machine-readable availability;
- source format;
- SAR source owner or custodian;
- date first registered;
- date last verified;
- next review date or review cadence;
- notes;
- supersedes;
- superseded by; and
- related sources.

This list is conceptual. It is not a final database schema, and every field is not required for every source.

## Stable SAR Source Identifier

SAR should use a stable internal SAR Source ID. The internal identifier must remain stable even if a publisher changes a URL, publishes a new revision, slightly changes a document title, or supersedes the source.

The model distinguishes a source family's stable SAR identity from the identity of a specific version or revision where appropriate:

```text
Source Family
    ->
Source Version / Revision
    ->
Immutable Version Reference
```

This document does not define identifier syntax or invent actual IDs.

## Source Provenance

Every registered source should preserve enough provenance to answer:

- Who issued it?
- Where was it obtained?
- Is that location authoritative?
- What version or revision was obtained?
- When was it obtained or verified?
- Was it human-readable, machine-readable, or both?
- Has its authenticity or currentness been validated?
- What immutable reference identifies the exact material used?

Where appropriate, SAR distinguishes the canonical or current location from the immutable, version-specific reference used by SAR. A canonical location helps identify current material; an immutable reference preserves reproducibility for the exact material used.

## Source Behaviors

### Versioned / Static Sources

Versioned or static sources may include published policy documents, PDFs, contractual provisions, formal guidance, departmental standards, and published revisions.

SAR should periodically check these sources against the authoritative publisher to determine whether they have been revised, replaced, superseded, withdrawn, expired, or otherwise materially changed. Review cadence should eventually be risk- and source-appropriate; this document does not prescribe a universal frequency.

### Maintained / Dynamic Sources

Maintained or dynamic sources may include machine-readable repositories, OSCAL content repositories, authoritative structured catalogs, and other continuously maintained upstream sources.

These sources must not be treated as static PDFs requiring only periodic rereading. SAR should eventually preserve the specific release, version, tag, commit, digest, or other immutable upstream identifier actually consumed. "Latest" is not sufficient provenance.

## Current Source Versus Assessment Source

### Current Source Version

The current source version is the version presently recognized by SAR as current.

### Assessment Source Version

The assessment source version is the exact source version used to support a specific assessment.

These values may legitimately differ:

```text
Assessment completed using Source Version A
                    |
                    v
           Decision preserved
                    |
Source later becomes Version B
                    |
                    v
          B becomes current
                    |
                    v
Existing assessment does not silently become based on B
```

A later source version may trigger impact analysis or reassessment, but it must not rewrite assessment history.

## Periodic Source Review

Authoritative and reference sources cannot generally be assumed to remain current indefinitely. For non-dynamic or versioned sources, SAR should support periodic verification against the authoritative publisher.

Conceptual review metadata includes:

- last verified date;
- verified by and verification method;
- review cadence;
- next review date where applicable;
- currentness status;
- change detected; and
- change-review status.

This document does not define operational scheduling mechanics or arbitrary annual, quarterly, or other universal review frequencies.

## Source Currentness Status

Conceptual source-currentness states include:

- Current / Verified;
- Review Due;
- Change Detected;
- Superseded;
- Withdrawn;
- Expired where applicable; and
- Currentness Unknown.

These are conceptual states only, not an executable enumeration or schema. Currentness Unknown must not silently become Current.

## Source Change Detection

A detected source change must not automatically alter assessment logic. SAR uses this conceptual dependency model:

```text
Source Change Detected
    ->
Source Change Validated
    ->
Materiality Analysis
    ->
Affected Mapping / Rule Identification
    ->
Affected Assessment Identification
    ->
Reassessment Determination
    ->
Traceable Update where required
```

This is a dependency model, not a workflow implementation.

## Materiality

Source-change materiality concerns whether a change affects SAR assessment reasoning or expectations. A new publication date, formatting change, URL move, metadata correction, or editorial revision may not necessarily change SAR requirements.

A substantive requirement change may affect classification logic, applicability logic, control expectations, evidence expectations, findings, risk treatment, residual-risk conclusions, future assessments, or existing assessments.

SAR must not infer materiality merely because a source version changed. Materiality should eventually be determined through traceable comparison and authorized review. This document does not define detailed materiality scoring.

## Impact Analysis

The Source Catalog should eventually support answering:

- What changed?
- Which SAR mappings reference the changed source?
- Which rules depend on those mappings?
- Which control expectations may be affected?
- Which assessments used the prior version?
- Which assessments remain valid?
- Which assessments require review or reassessment?
- Who reviewed the impact?
- What decision was made?
- What source or version replaced the prior source?

This document does not implement impact analysis.

## Historical Preservation

SAR must preserve historical source provenance. It must not overwrite the fact that an assessment relied on an earlier version merely because a newer version exists.

Historical records should eventually preserve source identity; version or revision; immutable reference; assessment usage; dates; relevant mappings; subsequent supersession; and impact or reassessment decisions where applicable. This supports auditability and reconstruction of prior decisions.

## Machine-Readable Sources

Machine-readable sources are important to future SAR implementation. The catalog should eventually identify:

- whether machine-readable content exists;
- its format;
- authoritative repository or location;
- release, version, tag, commit, or digest;
- date synchronized;
- validation status; and
- relationship to human-readable authoritative material.

OSCAL is an important example. This document does not build an OSCAL integration or assume a live upstream repository should be consumed without version pinning. A reproducible SAR assessment should be capable of identifying the exact machine-readable content used.

## Source Integrity

SAR should prefer authoritative publishers and repositories over unofficial copies. Where a working copy, cached copy, or transformed representation is used, SAR should preserve linkage to the authoritative source and the version from which it was derived.

Future implementation may use hashes or digests, signed releases, repository commit identifiers, release identifiers, version metadata, or controlled local copies. This document does not prescribe a specific integrity mechanism.

## Source Relationships

Catalog sources may have relationships such as:

- supersedes;
- superseded by;
- implements;
- supplements;
- references;
- interprets;
- contractualizes or incorporates where appropriate;
- machine-readable representation of;
- human-readable representation of; and
- related to.

This document does not create final relationship enumerations or infer legal hierarchy solely from these relationships.

## Authority Versus Reference / Benchmark

SAR distinguishes sources that provide an applicable authority from sources used as a reference, benchmark, or control-equivalency source. A source can exist in the catalog even when it is not independently applicable to a particular assessment.

For example, a State security or cloud provision may serve as an applicable requirement where an independent applicability basis exists, or as a benchmark or reference for a safeguard. The Source Catalog does not decide which role applies to a specific SAR; that determination belongs to later applicability logic.

## HIPAA CE / BA Terminology

Within SAR, **CE** means HIPAA Covered Entity where used in this context and **BA** means HIPAA Business Associate. BA does not mean State contractor. HIPAA relationships, contractual or agreement relationships, State or DDS applicability, and system, data, or environment risk remain separate dimensions.

The presence of HIPAA, HITECH, a BAA, State provisions, or contractual sources in the Source Catalog does not itself establish applicability. This document makes no new legal conclusions.

## Source Ownership / Stewardship

Registered sources should eventually have an identified SAR source owner or custodian responsible for the currency and validation of SAR's registered representation. This role is not necessarily the publisher.

```text
Publisher / Issuing Authority
    = entity that creates or officially maintains the source

SAR Source Owner / Custodian
    = person, role, or organizational function responsible for maintaining
      SAR's registered representation of that source
```

This document does not assign specific DDS staff or units.

## Source Review Versus Assessment Re-evaluation

### Source Review

Source review determines whether SAR's registered source remains current and accurately represented.

### Assessment Re-evaluation

Assessment re-evaluation determines whether a source change or other material change affects an existing SAR conclusion.

A source review does not automatically require reassessment, and a new source version does not automatically invalidate an existing assessment. Conversely, a material source change must not be ignored merely because an assessment was previously completed.

## Source Traceability

SAR supports the following conceptual source trace:

```text
Authoritative Publisher
    ->
Canonical Source
    ->
Source Family
    ->
Specific Version / Revision
    ->
Immutable Reference
    ->
SAR Catalog Entry
    ->
Mapping / Rule
    ->
Applicability Basis
    ->
Control Expectation
    ->
Assessment
    ->
Decision
```

Not every source uses every layer. This source trace complements the existing Evidence Chain and Decision Trace; it does not replace them.

## Relationship to Existing SAR Documents

[PRACTITIONER-DISCOVERY.md](PRACTITIONER-DISCOVERY.md) discovers AS-IS practitioner knowledge and process.

[SAR-ARCHITECTURE.md](SAR-ARCHITECTURE.md) defines the conceptual SAR risk architecture and governing principles.

[SAR-INFORMATION-MODEL.md](SAR-INFORMATION-MODEL.md) defines what information SAR must represent.

[SAR-INTAKE-MODEL.md](SAR-INTAKE-MODEL.md) defines how facts are collected.

[SAR-DECISION-LOGIC.md](SAR-DECISION-LOGIC.md) defines how supported facts become traceable assessment conclusions.

This document defines how authoritative and reference sources are identified, versioned, verified, maintained, and historically preserved. Future mapping and rules artifacts will connect catalog sources to specific requirements, applicability logic, safeguards, and controls.

## Future Work

The following are identified for later work and are not built by this document:

- machine-readable source registry schema;
- source ID convention;
- automated source-currentness checking;
- source synchronization;
- source hashing or digest validation;
- change comparison or diffing;
- materiality rules;
- source-to-requirement extraction;
- authoritative requirement catalog;
- applicability and authority matrix;
- control catalog;
- NIST SP 800-53 Rev. 5 mapping;
- OSCAL ingestion;
- HIPAA and HITECH mapping;
- BAA mapping;
- California State and DDS mapping;
- cloud mapping;
- AI requirement mapping;
- authoritative DDS 19-data-element mapping;
- affected-assessment analysis;
- reassessment workflow;
- notification and scheduling; and
- source governance roles.

## Design Constraints

This source-catalog model maintains the following boundaries:

- Source registration does not establish applicability.
- Control source remains separate from applicability basis.
- Current source version remains separate from assessment source version.
- Historical source versions are preserved.
- New versions do not silently rewrite prior assessments.
- Old assessments do not cause obsolete sources to be used for new work.
- Non-dynamic sources support periodic currentness review.
- Dynamic and machine-readable sources support immutable version references.
- "Latest" is not treated as sufficient provenance.
- Currentness Unknown does not become Current.
- Source change does not automatically mean material change.
- Material source changes can trigger impact analysis.
- Source review is distinct from assessment re-evaluation.
- Authoritative sources are distinguished from reference or benchmark use.
- Publisher is distinct from SAR source owner or custodian.
- HIPAA BA is not treated as State contractor.
- No source's presence in the catalog establishes legal applicability.
- No actual NIST controls or regulatory mappings are created.
- No invented citations, URLs, dates, revisions, or legal conclusions are introduced.
- No executable schema, synchronization mechanism, or rules engine is prematurely created.