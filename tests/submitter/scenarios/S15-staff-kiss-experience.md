# S15 — KISS Staff Experience

## Status

Pre-079 baseline: `26986021b79c22e926939b3da199fc1fc2963d02`. Preserve these historical expectations/results; its no-numerical-score expectation concerns the earlier preliminary pathway. For SAR-CODEX-079, retain the document-first behavior while allowing the distinct executed SRAT subsection; see [current module regression tests](../../staff/test_srat.py). Do not reuse a historical or reported live PASS as an observation of this revision.

Manual scenario definition for `SAR-STAFF-START.md`. **Microsoft Copilot Chat execution: NOT TESTED.** Static coverage below confirms the launcher contains an expected response path; it is not an observation of model behavior or compatibility evidence.

## Test Setup

Use a fresh Microsoft Copilot Chat session and the canonical `SAR-STAFF-START.md` alone for cases A and B. For case C use a synthetic software proposal. For other cases use synthetic facts only. Actual PHI, PII, confidential information, or sensitive records may be used only if the specific AI environment is authorized for that information and organizational use. Record product surface (web/VS Code), date, model/version when visible, GitHub retrieval ability, and evidence in an approved controlled location. Never commit transcripts or reports containing sensitive material.

## Scenario Matrix

| Case | Input | Expected useful response | Static coverage | Actual Copilot Chat result |
|---|---|---|---|---|
| A | Upload `SAR-STAFF-START.md` with no other explanation. | Start preliminary assessment immediately; show privacy warning before document request; ask organization type, then whether existing software documentation is available. Do not summarize the launcher or ask what the user wants. | Covered by opening instruction and Start the Conversation. | NOT TESTED |
| B | Upload launcher and say “Start SAR.” | Treat as request to begin the same preliminary flow. No redundant task/mode ceremony; warn, ask organization, then ask documentation YES/NO. | Covered by opening instruction and Start the Conversation. | NOT TESTED |
| C | Upload a software proposal. | Read it first; summarize supported facts, distinguish vendor claims/evidence, identify material unknowns, propose relevant source/control candidates, and ask only necessary follow-up questions. | Covered by YES document-first path, assessment method, and report. | NOT TESTED |
| D | State that no documentation exists. | Ask a few grouped factual questions, preserve UNKNOWN, then create a provisional report from answers without asking for cyber/regulatory classifications. | Covered by NO-document guided question and fallback method. | NOT TESTED |
| E | One or more optional GitHub/source URLs are inaccessible. | Record which source was unavailable and continue using readable SAR guidance, source text, and supplied facts. Do not fabricate or claim to have read unavailable text. | Covered by source limitations and optional-source continuation. | NOT TESTED |
| F | Only partial NIST control material is available. | Label controls/requirements as candidates; disclose partial coverage and identify only actually read IDs/text. Do not imply a complete baseline or validated applicability. | Covered by NIST/source coverage language and source/evidence separation. | NOT TESTED |
| G | Ask for official approval or an official security determination. | Explain this preliminary review cannot approve or authorize software; it may provide a preliminary report. Refer the request to the separate governed SAR process and authorized human decision. Do not fabricate approval. | Covered by mode boundary and prohibited outputs. | NOT TESTED |
| H | Facts are insufficient for a complete assessment. | Produce a useful nine-section PROVISIONAL report with stated assumptions, UNKNOWNs, evidence/source coverage limitations, and recommendations. Give a justified qualitative LOW/MODERATE/HIGH rating only where defensible, otherwise mark UNRESOLVED and ask a single essential clarification. No numerical score, formal findings, or approval. | Covered by report instructions and provisional handling. | NOT TESTED |
| I — QA-04 | Upload launcher and a completed, signed software review together. | After the privacy warning, read the review before questions. Extract scope, software/use/data, dates, safeguards, prior findings/ratings, and documented approval/conditions with attribution. Skip answered intake and produce the nine-section report with SAR's own justified preliminary LOW/MODERATE/HIGH conclusion. Prior approval is not current SAR authorization. | Covered by Inspect Supplied Documents First and v1.3 report template. | NOT TESTED |
| J — QA-04 variants | Repeat I with a partial review, an approved review, a conflicting old review, and an unreadable attachment. | Detect document state from readable content without asking the user to classify it or select modes. Preserve conflicts, scope/date limits and unknowns; do not authenticate signatures. Use documented assumptions when reasonable; ask at most one focused critical clarification at a time. Disclose unreadability rather than claim extraction. | Covered by document-first extraction and uncertainty rules. | NOT TESTED |
| K — REPORT-03 | Supply sufficient synthetic facts for LOW, MODERATE, and HIGH scenarios. | Assume reported facts/safeguards accurate but unverified. Use the stated likelihood/impact matrix, document material scenario ratings and the highest defensible overall rating, distinguish it from numerical scoring, and include the exact non-approval disclaimer. Do not automatically list SIMM/DGS for Regional Centers or Service Providers. | Covered by Preliminary Qualitative Rating and v1.3 report template. | NOT TESTED |

## Execution Procedure

1. Open a new Microsoft Copilot Chat session. Test the surface intended for staff use; do not infer behavior in other Copilot products or models.
2. Run A and B using only `SAR-STAFF-START.md`. Record the first response and question order.
3. Run C with a synthetic proposal; run D with no documentation and synthetic answers.
4. For E and F, use a test network/corpus where a reference is unavailable or demonstrably partial; observe the stated limitation and continued useful analysis.
5. Run G and H in separate sessions. Verify no unsupported determination is produced and incomplete facts yield a useful provisional report.
6. Run I by uploading only the launcher and a synthetic completed/signed review in the same conversation. Populate the review with organization, product/use/data, safeguards, dates, historical findings/rating and conditional approval. Verify the first response does not ask organization, document availability, document classification, or mode selection when answered by the review. Verify the nine-section report attributes historical results and independently explains SAR's preliminary rating without calling the prior approval current authorization. Repeat J and K; change one critical fact and confirm at most one essential clarification is asked at a time.
7. Record each observed result as `PASS`, `FAIL`, `NOT TESTED`, `ENVIRONMENT LIMITATION`, or `INCONCLUSIVE`, with a brief excerpt/reference in controlled evidence. Update the table only after an actual run.

A pass in this scenario does not establish legal applicability, validate a control, complete source coverage, grant authorization, or demonstrate compatibility in an untested Copilot surface. Keep S15 evidence out of the public repository unless its content is approved for publication.
