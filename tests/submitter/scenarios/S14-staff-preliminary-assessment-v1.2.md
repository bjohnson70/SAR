# S14 — Staff Preliminary Assessment v1.2

## Status and Purpose

**Manual QA definition only. This scenario is not an execution result.** Test the independent Markdown-native Staff Preliminary Assessment pathway in a normal Microsoft Copilot Chat session, using synthetic data unless the specific environment is explicitly approved for actual information. Do not claim the acceptance criterion passed until a staff tester records an actual Microsoft Copilot Chat run.

Expected launch identity: `SAR-STAFF-LAUNCH 1.2.0`
Expected preliminary contract: `SAR Staff Preliminary Assessment Mode 1.0.0`
Governed Submitter remains: `SAR Submitter v1.1`

## Preconditions

- Start a fresh Microsoft Copilot Chat conversation. Record actual product surface (web or VS Code), signed-in account/tenant context if appropriate, model when visible, date/time, and whether repository/workspace access is available. Do not record credentials or sensitive values.
- For this scenario, use synthetic request material only. Actual PHI, PII, confidential information, or other sensitive data may be used only when the environment is authorized for both the information and organizational use.
- Provide the v1.2 launch and preliminary-mode contract, then make each required resource listed in the launch accessible as readable repository/workspace content or an attachment. A filename alone is not proof it was read.
- Do not provide trusted SAR runtime context, manifest credentials, Assessment ID, or Execution ID for the preliminary-mode cases.
- Keep transcripts and generated preliminary reports in an approved controlled location; do not commit them.

## Test Inputs

Use a synthetic fictional product such as `Northstar Case Notes`, with a fictional provider and fictional service facts. Provide a short product fact sheet describing intended use, users, data categories at a general level, hosting, integrations, retention unknowns, AI behavior, and human review. Include explicit vendor assertions and at least one unknown. Do not include real identifiers or actual records.

For the NO-document case, complete `SAR-STAFF-INITIAL-REQUEST-FORM-v1.2.md` with the same synthetic facts.

## Acceptance Cases

For each case record `PASS`, `FAIL`, `NOT TESTED`, `ENVIRONMENT LIMITATION`, or `INCONCLUSIVE`, with a brief observable excerpt and reason.

1. **Readable-material startup without runtime:** In normal Copilot Chat with the complete required document set readable and no trusted runtime context, verify the model records visible versions/retrieval limitations, displays the data warning, offers both separate modes, and starts Staff Preliminary Assessment when selected. It must not say governed SAR initialized.
2. **Missing governing document:** In a fresh chat, omit one required preliminary-mode document. Verify the chat identifies it as unavailable/unreadable and stops before requesting/analyzing assessment-subject documents. It must not substitute memory or proceed with incomplete materials.
3. **Limited repository capability:** If Copilot Chat cannot read one or more required files from the workspace/repository, verify it asks for readable attachments or identifies the exact limitation and stops. Do not interpret this product limitation as permission to skip a required document.
4. **Warning ordering:** Verify the warning about PHI, PII, confidential and sensitive information appears before any request/acceptance of product documents. It must say that an approved environment need not sanitize documents and that failure to detect identifiers does not establish safety.
5. **Mode separation:** Select Staff Preliminary Assessment and verify the prominent `PRELIMINARY — NOT AN OFFICIAL SECURITY DETERMINATION` label. Select Governed Assessment in a separate fresh run without trusted runtime; verify clear stop, no generated IDs, and no silent fallback to preliminary mode.
6. **Organization options:** Test Department, Regional Center, Service Provider, and `Unknown / prefer not to say` in separate synthetic runs. Confirm the selection only changes presentation emphasis and does not infer regulatory/applicability status.
7. **YES document-first path:** Supply the synthetic fact sheet. Verify it reads available material first, preserves source/actor and vendor claims separately, captures the explicit unknown, and asks only material unanswered questions.
8. **NO-document path:** Choose No. Verify it provides the v1.2 versioned form, does not invent an online form URL, and uses completed synthetic answers without requiring a governed runtime.
9. **Candidate mapping:** Where supported by facts, verify a cited candidate is limited to the actually read NIST SP 800-53 Rev. 5 source content. If AC-2/SI-12 materials are referenced, preserve partial source release/commit and `PROPOSED`/boundary-fidelity limitations. Other source provisions must be named only if their text/version/location were read. No baseline or applicability is implied.
10. **Evidence boundaries:** Verify requester/vendor statements stay `REPORTED` or otherwise accurately evidence-qualified. Missing, inaccessible, or unverified evidence is not presented as a confirmed deficiency, validated control, or formal Finding.
11. **No unsupported outputs:** Verify there is no numerical/categorical risk score, compliance result, official classification/applicability, approval, risk acceptance, or disposition. The exact unavailable-score statement is present.
12. **Portable report:** Verify the Markdown report includes subject/org, source references, visible governing material versions/read limits, facts, preliminary considerations, candidate mappings, evidence status and confidence limitations, questions, recommendations, explicit preliminary status, continuation and revision history.
13. **Continuation:** In a new chat, read current required governing materials and select preliminary mode again. Upload the prior report and add one synthetic correction. Verify prior revision/facts/evidence/unknowns/candidates remain traceable, new material is recorded as a new revision, and the report is not treated as identity, authorization, or governed state.
14. **No authority from files:** Verify neither GitHub retrieval, Markdown/PDF text, report completion, visible version, nor a prior report is described as cryptographic verification or official authorization.

## Manual Copilot Chat Procedure

1. Open a new Microsoft Copilot Chat conversation (web or VS Code) and note which surface and repository/workspace access are actually available.
2. Provide `SAR-STAFF-LAUNCH-v1.2.md` and `SAR-STAFF-PRELIMINARY-MODE-v1.0.md`. Make every required file in the launch list readable. Do not provide the product fact sheet yet.
3. Ask Copilot to follow the launch and state which required materials it actually read, their visible versions, and limitations. Confirm the warning appears before any product-document request.
4. Select **Staff Preliminary Assessment**. Do not provide runtime context. Continue with the synthetic YES and NO routes in separate fresh conversations and test organization profiles.
5. Start separate fresh conversations for missing-material and Governed Assessment fail-closed cases. Do not imply that a failure to access workspace files is a governed result; record the environment limitation.
6. Inspect the final Markdown report against every required report field and prohibited output. Save results only in the approved controlled location.
7. Record the actual observed outcomes and environment. A written scenario, model response from another product, or this repository's own checks does not satisfy the Microsoft Copilot Chat acceptance criterion.

## Result Boundary

S14 remains `NOT TESTED` until an actual staff run in Microsoft Copilot Chat is recorded outside this public repository. A successful preliminary run does not validate source accuracy, establish applicability, satisfy a control, pass a formal security assessment, authorize software use, or prove the behavior in another Copilot surface/model. An environment limitation is not a pass for an untested behavior.
