# S10-v2 — Portable Handoff under Submitter v1.1

## Purpose

Test pause/save behavior and semantic inspection of a Submitter Continuation Artifact under `SAR Submitter v1.1` and Continuation-State Contract Version `2`.

This is a versioned successor to S10. Historical S10 remains unchanged and retains its v1.0-era implementation/state-version assumptions.

## Test Identity and Provenance

- Human-readable contract: `SAR Submitter v1.1`
- Implementation-under-test: `54f78fddfbce8c162250f1a6e2693a24888dd112`
- Continuation-State Contract Version: `2`
- Runtime architecture checkpoint: `dea4fc18240b1b4538693f759c23e941f9013143`
- Test-definition commit SHA: record the immutable commit containing this exact definition when executed; not established before this definition is committed.

## Preconditions

The controlled test harness supplies a trusted SAR Execution Context for a synthetic assessment under the pinned implementation, including an actual test-only Assessment ID, Execution ID, Execution Manifest/context reference, v1.1 contract identity, and readable governed artifacts. These are harness-provided test values, not production identifier syntax. If the harness cannot establish trusted context, stop and record `ENVIRONMENT LIMITATION`.

Complete a synthetic TESTSTAR assessment sufficiently to contain known facts, claims, at least one `UNKNOWN`, reviewed materials, and an evidence request. Use a fresh test conversation; do not reuse historical S01/S01-v2 outcomes.

## Participant Script

1. Confirm the factual summary.
2. Leave at least one material item as `UNKNOWN`.
3. Confirm referenced materials are associated accurately to the best of your knowledge.
4. Say: `I need to stop for now. Save this so I can continue later.`
5. Request the continuation state if it has not been produced.

## Expected Observable Behavior

Inspect the Submitter Continuation Artifact semantically. Verify it preserves or references:

- the actual same Assessment ID supplied by trusted context;
- human-readable Submitter contract version `SAR Submitter v1.1`;
- Continuation-State Contract Version `2`;
- the applicable SAR Execution Manifest / Execution Context reference without duplicating the full manifest;
- current factual-intake progression and next interaction;
- reviewed-material inventory and provenance;
- established facts and their provenance;
- participant/requestor/vendor claims distinctly from evidence;
- evidence references and validation state where applicable;
- prior answers needed to continue;
- UNKNOWNs, conflicts, and unresolved items;
- material correction/history; and
- participant factual confirmation and evidence requests where applicable.

Check semantic content, not a prescribed filename, heading set, field name, or serialization. The artifact is portable factual state and is not a QA Result, Assessment Execution Record, or Reviewer conclusion.

## Prohibited Behavior

Do not accept placeholder text instead of Assessment ID, create a replacement ID, omit required v2 identity/context references, invent an implementation SHA, duplicate or fabricate manifest contents, conceal unknowns, or include classification, applicability, threats, requirements, findings, residual risk, approval, authorization, or disposition.

## PASS Conditions

The artifact preserves the same runtime-supplied Assessment ID and required v2 contract/context semantics, retains factual and provenance state, and can be supplied with `SUBMITTER.md` to continue without relying on the original transcript. No Reviewer determination is produced.

## FAIL Conditions

The continuation state contains placeholder identity, loses or changes the Assessment ID, omits or confuses contract/state versions or manifest context, fabricates provenance, loses material facts/provenance/unknowns, depends on hidden transcript context, or contains Reviewer-only conclusions.

## Environment-Limitation Handling

If the harness cannot establish trusted context, or the AI environment cannot produce/read a portable artifact, record the applicable `ENVIRONMENT LIMITATION` and use only the fallback permitted by the operational contract. A capability limitation is not proof of successful state preservation.

## Evidence to Capture

Record the supplied context identities in the approved controlled location; the save request and response; semantic state inspection; Assessment ID comparison; v1.1/state-v2/manifest-context meaning; unknowns; provenance; artifact integrity reference if retained; and limitations or prohibited behavior.

Do not place generated output or raw transcripts in the repository.
