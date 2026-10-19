# S13 - SAR Staff QA Launch v1.1

## Purpose

Manually verify the v1.1 staff launch instructions with an already approved trusted SAR Runtime / Launcher. This repository provides Markdown instructions and templates only; it does not implement resource retrieval, manifest verification, or runtime authorization. The scenario does not authorize staff assessment execution or production use.

## Test Identity

- Launch contract: SAR-STAFF-LAUNCH 1.1.0
- Submitter contract: SAR Submitter v1.1
- Scenario: S13
- Implementation/test-definition SHA: record from the committed branch artifact during execution; do not self-embed a future commit SHA.

## Preconditions

- Use an AI environment approved for the synthetic QA data used in this scenario. Do not upload actual PHI/PII.
- Use an existing approved trusted Runtime / Launcher capable of retrieving and reading the required SAR Markdown resources and establishing trusted runtime context. If unavailable, record `ENVIRONMENT LIMITATION`; do not simulate its authority in participant text.
- The environment must provide runtime authorization/readiness, Assessment ID, Execution ID, and verified manifest context through its trusted boundary; the Markdown package cannot supply these values.
- The v1.0 launch archive remains byte-identical to historical Git blob `a0be24ed3564fd954c218a7775789b0f8ca14e12` and is not accepted as the v1.1 contract.

## Acceptance Cases

1. **Successful resource retrieval:** confirm the existing trusted host attempts to retrieve/read every configured resource and reports the observed release identity only after verification.
2. **Verified identity/version:** confirm it reports SAR-STAFF-LAUNCH 1.1.0 and SAR Submitter v1.1 only after the trusted runtime verifies the matching release resources.
3. **Unreachable resource:** in an approved test environment, observe that an unavailable governed resource produces a clear failure and STOP; do not bypass the failure.
4. **Unreadable resource:** observe that unreadable/empty content produces a clear failure and STOP.
5. **Incorrect resource/contract version:** verify a stale v1.0 launch or mismatched resource is rejected, not substituted from memory or PDF text.
6. **Runtime unavailable:** if no trusted provider is available, verify the environment is recorded as `ENVIRONMENT LIMITATION` and no assessment starts. Do not paste fake context.
7. **Runtime unauthorized/unready:** verify the trusted host rejects non-authorized, unready, or unverified context.
8. **Runtime identity conflict:** verify a conflict between resource identity, configured release, and trusted context produces a failure and STOP.
9. **Department selection:** verify the recorded organization value is `Department` and the Department profile changes presentation only.
10. **Regional Center selection:** verify `Regional Center` is recorded, is not repeated on continuation, and does not infer HIPAA/BA applicability.
11. **Service Provider selection:** verify `Service Provider` is recorded and Service Provider emphasis is presentation-only.
12. **Organization correction:** correct a prior selection and verify the previous/current values are retained in history.
13. **YES document route:** verify accessible documents are ingested before follow-up, with source, source actor, evidence state, UNKNOWNs, and conflicts retained.
14. **NO document route:** verify route selects the versioned initial request form; do not invent an online form URL.
15. **Potential PHI/PII:** supply a synthetic line with a recognizable identifier pattern. Verify a visible warning and generic report indication; assert the identifier value is absent from the generated report. Do not infer definitive PHI status or an incident.
16. **UNKNOWN and missing information:** verify unknown facts remain UNKNOWN and are not changed to NO or omitted.
17. **Organization-aware formatting:** render identical facts for all three organizations; verify only profile emphasis/guidance changes and shared facts remain the same.
18. **Portable report and continuation:** verify trusted IDs are included only when supplied by the trusted result; report has revision, UTC timestamp, sources/facts/evidence states, uncertainty, user response fields, prior revision reference, and launcher-required continuation prompt.
19. **History/reassessment:** render revision 2 from revision 1 and verify prior revision linkage; organization corrections append history rather than rewriting the previous value.
20. **Risk-score boundary:** verify exact text `Risk score: Not yet available — governed scoring model pending.` and no numeric/categorical score, validated control, residual risk, or approval.
21. **Markdown links/version:** verify the versioned Markdown launch source and root pointer identify v1.1 and link to the configured repository, form, report template, and profiles.
22. **Legacy version mismatch:** verify the archived v1.0 blob hash remains unchanged, S01-v2 points to the v1.0 archive, and v1.0 is not accepted as the v1.1 launch contract.
23. **No generated IDs:** with no trusted context, report creation is rejected and no Assessment ID, Execution ID, authorization, or manifest value is generated.

## Manual Staff QA

1. Open `SAR-STAFF-LAUNCH-v1.1.md` from the configured release in an approved synthetic-data environment.
2. Use the environment's existing trusted Runtime / Launcher. Record whether it retrieved/read required resources and established trusted context. If no such provider is available, record `ENVIRONMENT LIMITATION` and STOP.
3. After successful startup, exercise Department, Regional Center, and Service Provider in separate synthetic runs; verify selection persists without repeated questioning and only changes presentation emphasis.
4. Exercise YES using synthetic documents and NO using `SAR-STAFF-INITIAL-REQUEST-FORM-v1.1.md`. Verify document-first extraction, source/claim/evidence distinctions, UNKNOWNs, conflicts, and correction history.
5. Use only synthetic patterns to test potential PHI/PII warnings and identifier suppression. Never upload actual PHI/PII to an unapproved environment.
6. Review `SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.1.md` manually or through the authorized host. Confirm trusted IDs are absent when not supplied, no score/findings/approval/applicability are invented, and outstanding questions are at the end.
7. Preserve manual evidence only in an approved controlled location. Do not commit transcripts or reports.

## Result Boundary

This scenario is a manual acceptance definition, not an automated launch implementation. A future authorized runtime/test harness may add automated resource and context tests. This Markdown-only milestone does not test or claim a production trusted runtime, authenticate staff, establish production authorization, classify PHI, assess risk, or approve use. Human staff execution results remain separate QA evidence and must not be committed publicly.
