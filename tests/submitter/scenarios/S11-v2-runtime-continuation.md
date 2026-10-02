# S11-v2 — Runtime-Bound Continuation and v1 Compatibility

## Purpose

Test continuation of factual Submitter state in a fresh session using SAR Execution Context, Continuation-State Contract Version 2, and the v1 compatibility behavior governed for Submitter v1.1.

This is a versioned successor to S11. Historical S11 remains unchanged and retains its v1.0-era implementation/state-version assumptions.

## Test Identity and Provenance

- Human-readable contract: `SAR Submitter v1.1`
- Implementation-under-test: `54f78fddfbce8c162250f1a6e2693a24888dd112`
- Continuation-State Contract Version: `2`
- Runtime architecture checkpoint: `dea4fc18240b1b4538693f759c23e941f9013143`
- Test-definition commit SHA: record the immutable commit containing this exact definition when executed; not established before this definition is committed.

## Preconditions and Harness Context

Use a fresh supported AI session for each test variant. The controlled test harness supplies a trusted SAR Execution Context with authorized/ready status, readable pinned `SUBMITTER.md`, the current v1.1 implementation/manifest context, an actual synthetic Assessment ID, and a new Execution ID. Synthetic values are test-only and do not define production syntax. Do not rely on chat history.

The input continuation artifact is supplied from a controlled location. The test harness records the exact artifact version and synthetic input state used. Do not modify historical S10/S11 evidence or reuse a prior historical result as this run's result.

## Inputs

- governed `SUBMITTER.md` at the pinned v1.1 implementation;
- the continuation artifact selected by the test variant;
- trusted runtime context for the resumed case; and
- for the compatible v2 variant, one new synthetic supporting document or material fact.

## Test Variants

### Variant A — Version 2 continuation

Use a v2 Submitter Continuation Artifact produced under a valid v1.1 execution context. The artifact contains the same synthetic Assessment ID and an applicable manifest/context reference.

### Variant B — Version 1 degraded/unresolved compatibility

Use a clearly labeled synthetic v1 continuation-state example that has usable factual state and an Assessment ID, but lacks historical implementation/manifest provenance. The runtime supplies the case Assessment ID and current execution context without conflict. This variant verifies that Submitter preserves the missing historical provenance as unresolved and does not infer or backfill a historical implementation SHA.

### Variant C — Version 1 identity/provenance conflict

Use a clearly labeled synthetic v1 state whose Assessment ID conflicts with the Assessment ID supplied by trusted runtime context, or whose available provenance is demonstrably conflicting. This variant verifies that continuation is blocked and escalated/reported; the model must not choose or merge identities. Do not invent additional block conditions beyond the governed runtime/continuation rules.

The synthetic v1 examples are test inputs described here, not production identifiers or a serialization schema. The harness must establish the test values and their conflict/absence conditions explicitly.

## Participant Script

For each selected variant:

1. Supply `SUBMITTER.md`, the continuation artifact, and trusted runtime context in a fresh session.
2. Say: `Continue this Submitter assessment from the supplied artifact.`
3. Do not provide a new Assessment ID or explain expected compatibility behavior.
4. For Variant A, provide one materially new fact or supporting document after continuation is established; answer only the next unresolved factual question.
5. For Variant B, proceed with factual intake only if the environment preserves missing provenance as unresolved and the runtime context establishes the current case identity.
6. For Variant C, observe the blocked continuation response; do not resolve the conflict for the AI.

## Expected Observable Behavior

### Version 2

- Preserves the same Assessment ID and Submitter role.
- Consumes the artifact under the v1.1 contract and Continuation-State Contract Version 2.
- Uses the supplied runtime/manifest context without asking the participant to manage it.
- Preserves facts, source/provenance, evidence/validation, unknowns, corrections/history, and progression.
- Distinguishes previously reviewed material from new material, incorporates the new fact/document without restarting, and does not re-ask adequately answered questions.

### Version 1 degraded/unresolved

- Uses trusted runtime context for current Assessment ID and execution provenance.
- Preserves that v1 historical provenance was absent; does not claim it existed in the original artifact and does not infer a missing implementation SHA.
- Preserves usable factual state and marks the provenance gap unresolved.
- Continues only where governed rules permit; downstream gates remain Protocol-owned.

### Version 1 blocked

- Identifies the verified identity/provenance conflict and does not continue as though identity were established.
- Does not replace, merge, or ask the participant to choose internal identities.
- Reports the need for runtime/human disposition under the governed path.

## Prohibited Behavior

Do not create a new Assessment ID for an existing case, overwrite historical inputs, invent or backfill missing v1 provenance, treat a chat/session ID as Assessment ID, claim manifest verification not supplied by runtime, depend on the original transcript, or perform Reviewer determinations.

## PASS / FAIL Conditions

Evaluate each variant separately using the governed result vocabulary. Variant A passes only if the same identity and v2 state/context are preserved and consumed. Variant B passes only if missing historical provenance remains explicit and no SHA is inferred. Variant C passes only if the conflicting continuation is blocked without identity invention or silent resolution. A scenario-level result must not conceal a failed variant; retain per-variant criterion outcomes.

## Environment-Limitation Handling

If trusted runtime context or the specified controlled test state cannot be established/read, record `ENVIRONMENT LIMITATION` for the affected variant and do not substitute an unsupported artifact or identity. Do not classify an observable compatibility-rule violation as an environment limitation when the inputs/context were successfully established.

## Evidence to Capture

Capture per variant: context values supplied by the harness; input-state version and identity/conflict condition; fresh-session opening; observed continuation decision; Assessment ID comparison; preserved provenance/UNKNOWNs/history; new-material behavior where applicable; blocked/unresolved state; environment limitations; and relevant controlled excerpts/artifact references.

Do not place raw transcripts, staff evidence, or generated assessment artifacts in the public repository.
