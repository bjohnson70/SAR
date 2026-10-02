# SAR Repository-Native Execution Architecture

## Status and Authority

**ARCHITECTURE PROPOSAL - DESIGN ONLY; NOT AN OPERATIONAL CONTRACT OR APPROVED EXECUTION MODE**

This document proposes a low-friction repository-native SAR interaction in supported AI chat environments. It complements `SAR-RUNTIME-INTERFACE.md`, `SUBMITTER.md`, `ASSESSMENT-PROTOCOL.md`, and `SAR-EXECUTION-RECORD.md`; it does not amend or supersede them. Existing contracts remain authoritative until separately reviewed and approved.

No repository-native execution mode is authorized by this proposal. In particular, the current Runtime Interface and Submitter require trusted SAR Execution Context before valid Submitter startup. An ordinary repository URL and participant attachments do not satisfy that requirement. Any graded-provenance mode described below requires explicit governance changes before use. This document does not implement the mode, alter S01-v3, run an assessment, define a machine-readable schema, create decision rules, or approve a risk result.

The design goal is: **Give SAR what you know, point the AI at SAR, and receive a governed assessment for human decision.** The participant should not operate SAR's internal roles, records, versions, or assessment machinery.

## Reference Execution Pattern

The inspected `CPAtoCybersecurity/ai_risk_assessment_tool` demonstrates a useful packaging and interaction pattern:

- canonical system instructions define the workflow;
- separate Markdown knowledge files contain methodology, checklist, threat library, reference material, and output template;
- platform-specific deployment instructions install the same canonical content into a preconfigured agent/project;
- the configured agent follows a named sequence, accepts partial answers, and records open questions; and
- a fixed output template encourages consistent reports.

For example, its M365 Agent Builder deployment instructions tell the administrator to paste `core/instructions.md` into the agent instructions and upload the five `core/knowledge/` files. The instructions describe a staged intake/analysis/output process; the knowledge files and template supply supporting content. A user can then start a conversation with the configured agent and provide a system description and documents with relatively little process knowledge.

**Important limitation:** the inspected material does not establish that an arbitrary ordinary chat securely bootstraps from a repository URL alone. The low-friction chat experience relies on a configured platform agent/project whose canonical instructions and knowledge have already been installed. Platform setup and refresh are administrator/deployment work. The core instructions also prescribe some starter questions; thus its observed pattern is not proof of universal zero-question or zero-configuration behavior. This design adopts its single-source-of-truth packaging, orchestration, document-first aspiration, concise workflow, and stable report shape, not its risk tiers, scoring, control conclusions, threat semantics, or approval language.

## Target User Experience

The target ordinary-user interaction is one natural opening message containing available system/software materials and the SAR repository URL. Where the host supports repository access, a repository-native entry artifact directs the AI through governed content. The AI then:

1. reads accessible assessment materials and the SAR entry specification;
2. extracts source-linked facts, claims, evidence references, conflicts, and unknowns;
3. asks only material unanswered factual questions, in small conversational groups;
4. progresses through governed assessment stages without asking the user to choose internal roles;
5. runs only those determinations whose governed rules and inputs are available; and
6. produces a concise assessment report with traceable provenance, limitations, unresolved matters, and any required human decision.

The user is not asked to supply Assessment ID, Execution ID, Git SHA, manifest, continuation version, role selection, rule selection, applicability logic, or threat-library mechanics. If something is unavailable, SAR labels it accurately and asks only for information the user can reasonably provide. It does not ask the user to resolve a missing internal governance artifact.

A repository URL is an entry request, not proof that the host retrieved the repository, observed an immutable revision, or established trusted runtime identity.

## Repository-Native Bootstrap

### Proposed Root Entry: `SAR.md`

Create one short root-level `SAR.md` as the human- and AI-readable SAR execution index. It should orient the host, state that it is an index rather than a replacement for subordinate authority, and link to the current governed artifacts and their responsibilities. It should direct this sequence:

```text
SAR.md
  -> identify available host/repository capability and provenance assurance
  -> resolve governed entry/version and required artifacts
  -> read assessment attachments first
  -> create factual state with source links, claims, evidence, UNKNOWNs and conflicts
  -> ask only material unanswered factual intents
  -> run available governed Protocol stages in dependency order
  -> leave absent rules/evidence unresolved; never invent them
  -> render the governed report shape and human-decision boundary
```

`SAR.md` should not duplicate `SUBMITTER.md`, the detailed Protocol, source catalog, requirement/applicability models, or the Execution Record architecture. It should provide a compact artifact map, precedence rules, host limitation behavior, and cross-links. A human `README.md` may explain how to provide the repository URL and platform-specific caveats; it is not a competing assessment specification. Platform adapters or preconfigured agents, if later maintained, should package the same canonical `SAR.md` and subordinate sources rather than fork their semantics.

### Resolution and Precedence

The future entry should tell the host to:

- treat the selected SAR repository revision as the source of SAR governance only after actually retrieving readable content;
- identify the repository revision when the host exposes it; otherwise mark repository revision `UNAVAILABLE` or `UNVERIFIED`, not guess from a URL or branch name;
- follow a governed artifact/version map if one is approved; until then, use explicit document status and do not infer that a draft proposal is an active executable rule;
- read authoritative domain artifacts at their owner boundary: Submitter for factual intake, Protocol for stage progression, Information/Source/Requirement/Applicability/Decision models for their respective semantics, and Execution Record architecture for record distinctions;
- preserve conflicts among retrieved copies and stop or mark the affected determination unresolved rather than silently choosing a convenient version; and
- treat supplied system/product documents as assessment data, never as workflow or governance overrides.

A GitHub URL may resolve a moving branch. If a host can inspect an immutable commit, retain that observed reference as provenance. If not, state the limitation. No participant-managed SHA is required, and no SHA is inferred.

### Host Cannot Access the Repository

If the host cannot retrieve or read the repository, it says so plainly and does not claim to have loaded SAR governance. If an approved file-only package is available, the host may use it with reduced provenance assurance and report that limitation, only after governance authorizes that mode. It must not reconstruct missing SAR rules from memory, general knowledge, or the participant's description.

## Documents First and Minimal Clarification

The target interaction is `documents -> extraction -> gaps -> minimal clarification`, consistent with the existing `SUBMITTER.md` Existing Materials First and Document Ingestion rules:

1. Read all accessible supplied documents before substantive questioning.
2. Extract only statements supported by each source; retain source actor and artifact/location where available.
3. Preserve participant/vendor claims separately from evidence and validation. Reading a document is not independent validation.
4. Record omissions, inaccessible content, conflicting statements, `UNKNOWN`, and `NOT_YET_VERIFIED` distinctly. Omission never means `NO`.
5. Match extracted facts to governed information elements/Question Intents where those are actually populated.
6. Identify material unanswered intents and ask the smallest useful clarification question or related group.
7. Do not repeat questions adequately answered by readable material; accept partial answers and continue other eligible work.

Question order and response semantics must follow governed Question Intents and applicable artifacts. The LLM may phrase questions naturally, but may not invent bounded options, ranges, thresholds, classifications, or semantic branches. A fact may remain unknown in the report. If the repository has not yet populated the relevant Question Intent, rule, or response options, record the gap as ungoverned/unresolved rather than creating an ad hoc questionnaire rule.

## Internal Metadata Without User Burden

### Provenance Assurance

Keep semantic correctness distinct from execution provenance assurance. A useful fact-first characterization can be produced with reduced provenance, but it must not be represented as a high-assurance, reproducible, verified SAR execution unless the required trusted context and immutable bindings exist.

These are **provisional execution-provenance assurance states** describing only what the host/runtime can substantiate about execution context and artifact provenance. They do not change assessment semantics and are not risk, evidence-validation, applicability, findings, Assessment Depth, approval, authorization, disposition, or final assessment-status values. For otherwise identical governed assessment inputs and rules, changing only provenance assurance does not change substantive assessment determinations. They are proposed for design discussion, not approved interface fields:

- **Repository-observed:** host retrieved SAR content and can identify the actual repository revision/artifacts it observed; this does not authenticate the host, establish manifest verification, or issue persistent identities.
- **Package-observed:** host read user-supplied SAR files; exact source revision/content authenticity may be unverified unless an approved distribution binding is available.
- **Runtime-verified:** a future governed runtime supplied verified identity, manifest, artifact bindings, and context through its trusted interface.
- **Unavailable / unresolved:** material provenance could not be observed or conflicts; retain the gap.

The labels indicate provenance assurance only, not assessment quality or product risk. Governance must decide whether these states become official interface/result values and what operations each permits. They do not silently relax current contracts.

### Assessment Identity

Assessment ID identifies a persistent assessment across sessions/executions; it is not a chat identifier. When trusted runtime supplies it, the AI consumes it without exposing it as a user task. When no trusted persistent identity exists, this proposal permits no invented or model-issued identifier. If separately approved, the assessment may be labeled exactly `SESSION-LOCAL / UNVERIFIED ASSESSMENT IDENTITY` for the current conversation/draft, without a generated token or claim of persistence. The report must state that it is not a verified persistent SAR identity and cannot establish continuity across sessions. A later runtime may bind it to a persistent case only through a governed process that preserves the change/history.

This is a proposed amendment to current identity requirements, not an interpretation already authorized by `SAR-RUNTIME-INTERFACE.md` or `SUBMITTER.md`. Until approval, those current artifacts continue to require runtime-supplied Assessment ID for valid execution.

### Execution Identity

Use runtime-supplied Execution ID when available. In ordinary chat without one, do not synthesize an Execution ID or repurpose a chat/session identifier as one. Mark execution identity `UNAVAILABLE / UNVERIFIED`; the host conversation/session may be recorded as contextual provenance only if actually available and explicitly not an Execution ID. This too requires approval before use in an operational mode.

### Metadata Capture

Track contract identity, source/rule versions, protocol identity, repository revision, artifact provenance, continuation version, and execution context only to the extent observed. Distinguish `UNAVAILABLE`, `UNVERIFIED`, `UNRESOLVED`, and `NOT APPLICABLE` where the owning schema governs them. Do not ask the participant to type internal metadata. A source-derived assessment fact and a host-observed provenance value have different trust status.

## Reconciliation with `SAR-RUNTIME-INTERFACE.md`

The current interface is explicit: SAR Execution Context is trusted runtime context; valid context precedes operational role startup; context is not inferred from conversation, participant claims, filenames, model memory, or moving branches; Runtime / Launcher establishes authorization/readiness, manifest/artifact correspondence, and identities; Submitter consumes valid context; and missing/invalid context means do not claim valid SAR initialization. `SUBMITTER.md` repeats this entry-point requirement. S01-v3 expressly tests under trusted synthetic harness context and requires `ENVIRONMENT LIMITATION` when it cannot be established.

That boundary is appropriate for **high-assurance execution provenance**, but it is too strong for the requested **repository-native ordinary-chat characterization path** if the intention is to do no more than produce a useful, clearly limited draft from observed repository rules and supplied facts. It cannot be relaxed implicitly.

If SAR adopts repository-native execution with graded provenance, a future governed revision must identify and revise at least:

- `SAR-RUNTIME-INTERFACE.md`: the definition of context as necessarily trusted runtime context before every operational role; statements that the context is never inferred from repository/chat inputs; the valid-context-only startup rule; the unconditional Runtime / Launcher ownership model; and identity interfaces that require runtime-supplied IDs. Preserve trusted runtime as the highest-assurance path and define which lower-assurance operations are permitted.
- `SUBMITTER.md`: statements that receiving `SUBMITTER.md` alone does not establish valid execution, Runtime must supply context before startup, Start/Continue is permitted only with explicitly authorized/ready trusted context, and identity-dependent state must stop when Assessment ID is unavailable. Any repository-native mode must have explicit assurance labels and output limitations rather than silently weakening those rules.
- `ASSESSMENT-PROTOCOL.md`: stage-entry identity/provenance gate and orchestration behavior must distinguish which determinations can be produced from repository/package-observed inputs and which require authenticated/persistent identity, verified sources/evidence, approved rules, or human review. The protocol's no-invented-governance and deterministic-rule invariants remain unchanged.
- `SAR-EXECUTION-RECORD.md`: manifest and immutable event/snapshot provenance must remain the high-assurance record basis. Any session-local draft or lower-assurance execution reference must not be mislabeled an Assessment Execution Record or QA Result; its record relationship and assurance attributes require governance.
- `tests/submitter/README.md` and acceptance tests: create a separate repository-native host-capability scenario; do not rewrite S01-v3's trusted-harness precondition or historical result. Define how reduced provenance, inaccessible repository, and unpopulated rules are evaluated.

### Trustworthy Semantics vs High-Assurance Provenance

**Required for trustworthy assessment semantics:** use the correct governed content that is actually available; respect precedence and role boundaries; cite/trace facts to their source; preserve claims/evidence/validation distinctions and unknowns; apply only explicit rules; surface missing or conflicting governance; never invent outcomes; and leave final authorized decisions to humans.

**Required for high-assurance execution provenance:** trusted runtime authorization/readiness, immutable manifest and artifact bindings, verified artifact correspondence, persistent Assessment ID, distinct Execution ID, reproducible input snapshots/events, and controlled evidence/results under approved access and retention governance.

The first set can support a constrained conversational draft under a future approved lower-assurance mode. It does not automatically satisfy the second set or authorize current operational execution.

## S01-v3 Reconciliation

Keep committed S01-v3 unchanged as the high-assurance trusted-harness startup test. It tests Submitter v1.1 behavior after trusted synthetic context has been established; it is not a repository-native ordinary-chat test.

Add a separately governed scenario for repository-native execution, preferably a new scenario ID rather than replacing S01-v3. It should test repository retrieval/entry traversal, host-capability disclosure, document-first extraction, limited clarification, explicit assurance labeling, absence of model-generated IDs, deterministic use of available rules, unresolved behavior for missing rules, and a report with a human disposition boundary. It must include repository-inaccessible and file-only variants where relevant. The new test should not demand high-assurance provenance from a host that cannot provide it, nor allow lower assurance to masquerade as trusted context. Preserve S01-v2 and S01-v3 histories and results unchanged.

## `ASSESSMENT.md` Disposition

At the current baseline, root `ASSESSMENT.md` is a historical S01-v2 QA launch/bootstrap artifact. It identifies Submitter v1.0 and carries old S01-v2 startup material. It is neither the operational launcher nor an assessment-instance result. It must not be silently reinterpreted as the new repository-native entry point or used as a generic report template.

**Recommendation:** reserve root `SAR.md` for the repository-native SAR entry/index. Preserve root `ASSESSMENT.md` as a historical QA launch artifact until a separate migration is approved; then archive it under a clearly versioned test-launch path while preserving exact bytes/history and updating references. Reserve generated assessment output for a distinct name such as `SAR-Assessment-<governed case reference>.md` or a controlled assessment record reference, with its final naming/identity schema separately governed. Do not use one shared root `ASSESSMENT.md` both to explain launch and to represent a case result.

S01-v3 currently explicitly includes the existing `ASSESSMENT.md` as a launch artifact. Any future replacement/migration must update its test package through governance, not remove or reinterpret that requirement ad hoc.

## Automated Internal Role Progression

Expose one SAR workflow to the user; do not ask the user to choose Submitter, Reviewer, or Protocol. A future orchestrator can internally route through governed stages:

```text
Bootstrap / capability assessment
  -> characterize from supplied materials
  -> clarify material factual gaps
  -> factual state and confirmation
  -> governed classification / inherent-risk evaluation, where rules exist
  -> applicability and Assessment Depth, where rules exist
  -> threat and requirement resolution, where catalogs/rules exist
  -> evidence evaluation and validation handoff
  -> findings/gaps under governed criteria
  -> residual-risk analysis where governed
  -> human disposition boundary
  -> report
```

Progression is automatic only where an approved stage contract and gate define the transition. The LLM may coordinate prompts, extract candidates, and explain state; it may not decide that an unevaluated gate is satisfied or invent a rule. If a stage is unsupported by populated governance, mark it `NOT GOVERNED`, `UNRESOLVED`, or the owner-approved equivalent and continue only into independent permitted work. Human review/validation and final decisions remain visibly distinct activities.

## Human Decision Boundary

A report may be prepared automatically from available facts and governed results, but must label its assurance and status. It can include factual characterization, registered source/requirement references, evidence status, governed intermediate determinations, candidate or reviewed findings according to authority, unresolved questions, and residual-risk analysis only where an approved method exists.

The report must not imply that a complete-looking document is an approval. It reserves final risk acceptance, authorization, exceptions, and disposition to the authorized human decision-maker where required. Show the exact unresolved gates, required decision role, decision scope, and rationale fields without pre-filling a decision. A blank, pending, or `HUMAN DECISION REQUIRED` state is not approval.

## Consistency Model

The repository, not model discretion, must determine assessment semantics. Greater consistency than a loosely configured chat prompt requires:

- one canonical root index and explicit authority/preference rules;
- versioned, populated Question Intents with allowed responses, dependencies, UNKNOWN semantics, and priority;
- stable execution order and stage inputs/outputs, while allowing evidence-driven return paths;
- registered sources with exact versions and semantic roles;
- explicit applicability rules/bases and independent authority paths;
- a versioned Threat Library with governed triggers, not freeform threat invention;
- validated requirement records and source citations;
- explicit evidence expectations, validation roles/states, and claim/evidence/validation distinctions;
- hard gates with specified outcomes and route behavior;
- deterministic rule tables/mappings for machine-determinable results, with input/output trace; and
- a report schema/template that renders known, unknown, unresolved, candidate, validated, and human-decided information distinctly.

Identical normalized facts and identical governed versions should yield identical machine-determinable intermediate results. LLM-generated facts remain candidates with provenance until accepted through the governed validation path. Missing catalogs/rules are represented as gaps, not filled by model general knowledge. SAR currently has extensive conceptual models but no populated Question Intent Registry, complete source-bound requirement corpus, active Assessment Depth rules, populated Threat Library, full evidence mappings, or approved result/report schema. Repository bootstrap alone cannot supply this missing executable governance. These are prerequisites to claiming comprehensive deterministic assessments.

## High-Level SAR Assessment Report

The canonical report should be concise in its opening and traceable in its detail. Proposed sections:

1. **Assessment Identity and Provenance:** assurance state; case identity as verified, session-local/unverified, or unavailable; observed SAR revision/artifacts; source/rule/protocol versions; and explicit provenance gaps.
2. **Executive Summary and Status:** scope, principal supported conclusions, unresolved limitations, and whether human decision is required. Never present an ungoverned risk score or imply approval.
3. **System / Software Characterization:** purpose, product, deployment, users, integrations, and key factual scope.
4. **Data / Information Types:** factual descriptions, data subjects/flows, source links, UNKNOWNs, and classifications only if governed and established.
5. **Environment / Connectivity:** hosting, location, access, dependencies, interfaces, and gaps.
6. **Classification and Inherent Risk:** only governed determinations, with rule/version and rationale; otherwise explicit `UNRESOLVED / NOT GOVERNED`.
7. **Assessment Depth:** governed outcome and rule provenance when present; otherwise unresolved.
8. **Authorities, Applicability, and Requirements:** separate candidate/reference/applicable roles, bases, citations, versions, and unresolved interpretation.
9. **Threat Considerations:** governed patterns/triggers and linked facts; distinguish candidates and reviewer validation.
10. **Safeguards / Controls and Evidence:** requirement-to-safeguard links, evidence scope, claim/evidence/validation state, and missing/inaccessible evidence.
11. **Findings / Gaps:** only findings supported by governed criteria/authorized review; otherwise label candidate or unresolved.
12. **Residual Risk:** method/version and conclusion only when governed; never calculate an invented score.
13. **Unresolved Items and Gates:** material unknowns, conflicts, unpopulated governance, evidence requests, and next actions.
14. **Required Human Decisions:** decision authority, exact scope/state considered, required rationale/conditions, and pending/recorded outcome.
15. **Assessment Trace and Sources:** links from conclusions to facts, evidence, validation, requirement, authority/source/version/citation, and rule.

The report is a view over assessment state/history, not a replacement for the detailed record or controlled evidence. Its schema, status vocabulary, identity binding, storage, access, and publication rules require separate approval.

## Host-Capability Model

One semantic workflow should operate with different, explicit provenance assurance. These levels are capability descriptions for proposed governance, not currently approved authorization classes.

| Level | Available capability | Permitted result under this proposal | Provenance and limitations |
|---|---|---|---|
| **1 - Repository-aware chat** | Host can retrieve SAR repository content and user attachments. | Bootstrap from `SAR.md`, read linked governance, perform document-first characterization and only governed stages supported by retrieved content. | Record repository/artifact revisions only when observed; otherwise unverified. No trusted persistent Assessment ID/Execution ID or manifest is implied. Current contracts still require trusted context; this mode needs approval before operational use. |
| **2 - File-only chat** | Host cannot retrieve GitHub; SAR files are supplied as an approved package plus assessment documents. | Same governed workflow from readable supplied files, with unavailable governance marked; repository access absence is explicit. | Package source/revision authenticity is unverified unless an approved distribution binding exists. No inferred SHA, persistent identity, or runtime verification. Requires approval as a lower-assurance mode. |
| **3 - Trusted runtime** | Future runtime supplies verified SAR Execution Context, identities, manifest/artifact bindings, and persistent state. | Same user-facing semantic workflow, with supported continuation and stronger execution provenance. | Highest assurance under the authorized mechanism; verification claims remain limited to properties actually established. This is the current Runtime Interface target, not a presently demonstrated staff QA capability. |

Moving from Level 1/2 to Level 3 improves identity, provenance, persistence, and reproducibility; it must not change factual semantics, UNKNOWN handling, rule definitions, role boundaries, or report meaning. If host capability drops during an execution, disclose the change, retain affected provenance as unavailable, and do not claim that the remainder has Level 3 assurance.

## Reference / Current SAR / Proposed SAR

| Capability | Reference Risk Tool | Current SAR | Proposed SAR |
|---|---|---|---|
| User startup effort | Low once a platform agent/project is configured; setup is not just a repository URL in arbitrary chat. | Manual contract/bootstrap and, for S01-v3, trusted harness precondition. | Attach available materials and provide SAR URL to a repository-aware host; fallback honestly to an approved package or trusted runtime. |
| Repository bootstrap | Canonical `core/instructions.md` plus separately uploaded knowledge files; platform deployment guides configure them. | Governance spread across root Markdown files; no canonical repository-native orchestration entry. | Root `SAR.md` indexes authoritative documents; report actual observed revision or limitation. |
| Document ingestion | Instructions prescribe intake; capable host can use attached/knowledge files. | `SUBMITTER.md` explicitly reads supplied materials before questioning. | Preserve document-first extraction, source links, claim/evidence distinctions, and minimal material clarification. |
| Clarification burden | Structured intake with partial answers/open questions, but it also prescribes starter questions and checklist steps. | Adaptive factual questioning is governed conceptually; Question Intent Registry is not populated. | Ask only material unanswered governed intents; show UNKNOWN/unpopulated-intent gaps instead of a long static questionnaire. |
| Deterministic workflow | Fixed stages and configuration prompt make the agent's process repeatable. | Assessment Protocol proposes deterministic stages/gates but is not an operational engine/ruleset. | Automatic stage orchestration; execute only populated versioned rules and leave other outputs unresolved. |
| Source breadth | Curated AI risk references/checklist and threat resources. | Broad SAR architecture covering security, privacy, legal/contractual authority and technology context; implementation catalogs remain incomplete. | Resolve registered source families and versions, preserve authority roles/citations, and expose coverage gaps. |
| Applicability | Reference framework mappings and tier-driven control review. | Separate applicability model and future rules; no populated universal determination engine. | Apply only approved source-specific applicability rules; do not infer from source presence. |
| Evidence handling | Template/checklist captures responses and assumptions; depth depends on configured agent and user review. | `Claim != Evidence != Validation != Finding`; validation authority and provenance are explicit. | Link assertions, source evidence, scope, validation state, and expectation; unresolved when unsupported. |
| Threat model | STRIDE/AI threat library and risk-tier heuristics are built into its own methodology. | Threat Library architecture proposed; no patterns/triggers populated in reviewed SAR Protocol. | Select only governed patterns from explicit triggers; no model-invented threat catalog. |
| Traceability | References and checklist IDs support citations, but no SAR Assessment Trace architecture equivalent was established in the excerpts reviewed. | Bidirectional Assessment Trace, source/version and evidence relationships are modeled. | Render trace paths from fact through source/rule/evidence to conclusion and human decision. |
| Final report | Stable template with risk ratings, recommendations, checklist and approval fields. | Final Assessment report is conceptual; no approved report schema. | Concise governed report with assurance, unresolved states, trace, and human decision boundary; no ungoverned scoring. |
| Human decision boundary | Template includes approval/sign-off and recommendation language. | Consequential decisions remain with authorized human authority. | Produce decision-ready work; reserve acceptance/authorization/disposition for authorized humans. |
| Provenance assurance | Preconfigured knowledge/version maintenance is described; execution manifest and persistent runtime identity were not established in reviewed materials. | Trusted context/manifest architecture is explicit; S01-v3 requires trusted harness. | Grade assurance honestly across repository, package, and runtime hosts; do not equate repository access with authenticated execution. |

## Minimum Future Governance Changes

No existing artifact is changed by this proposal. If approved, the minimum follow-on changes should be sequenced:

1. **Define and govern `SAR.md`:** root index, precedence, loading map, host limitation disclosure, and no-override rule; update root README to point users and AI hosts to it.
2. **Approve provenance assurance modes:** amend `SAR-RUNTIME-INTERFACE.md` only after explicit decision on whether lower-assurance repository/package execution is permitted, its limits, and status semantics. Preserve trusted runtime as the high-assurance mode.
3. **Align Submitter:** revise `SUBMITTER.md` startup and identity requirements to express approved modes while preserving document-first behavior, unknowns, provenance labels, and authority boundaries.
4. **Make Protocol executable in bounded scope:** define/populate required Question Intents, stage contracts, deterministic rules, applicable source/requirement mappings, evidence expectations, threat triggers, and gate outcomes. Mark unpopulated areas explicitly; avoid a broad speculative rules rewrite.
5. **Preserve acceptance lineage:** leave S01-v3 as the high-assurance scenario. Add a distinct repository-native scenario and explicit host/revision/provenance variants; do not retroactively alter committed test definitions/results.
6. **Define report contract and legacy migration:** approve a report schema/status vocabulary and separate launch entry from output naming; archive `ASSESSMENT.md` only via a byte-preserving, reference-updating migration.
7. **Align record architecture:** define how assurance state, observed repository/package revision, session-local identity, absent execution identity, immutable execution records, and controlled evidence references relate without collapsing assessment state, execution records, and QA results.

A staged proof should first establish repository-aware bootstrap and fact-only report behavior with no unsupported downstream conclusions. Later increments can activate individual governed Protocol stages as rules and catalogs are approved. This is governance sequencing, not permission to execute under the current contracts.

## Unresolved Decisions

- Whether repository-native Level 1 and file-only Level 2 may be operational SAR execution modes, or only clearly labeled preparation/draft modes.
- Who approves a repository revision as a SAR release and how a repository URL maps to a governed version when the default branch moves.
- Whether `SESSION-LOCAL / UNVERIFIED ASSESSMENT IDENTITY` is acceptable as a report label and what persistence/continuation it permits.
- Whether an absent Execution ID blocks only high-assurance record creation or all current `Assessment Execution Record` semantics.
- What source/rule/status vocabulary may be emitted where no formal schema is approved.
- Which portions of the Assessment Protocol can be deterministic at first release given currently unpopulated registries/catalogs/rules.
- How factual preparation output transitions into a governed assessment record and who validates evidence/finding candidates.
- Report format, identity/naming, storage, privacy, retention, and publication control.
- Migration timing and historical location for root `ASSESSMENT.md` while preserving S01-v3's current input requirement.
- Supported host capabilities and how repository/tool access and observed revision are exposed reliably to an AI host.

Until these questions are governed, current Runtime Interface, Submitter contract, Protocol status, and committed acceptance criteria remain in force. This document proposes a direction; it does not make repository URL plus attachments a valid execution under today's high-assurance contract.
