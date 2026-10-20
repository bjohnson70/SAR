# S15 — KISS Staff Experience

## Status

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
| H | Facts are insufficient for a complete assessment. | Produce a useful PROVISIONAL report with stated assumptions, UNKNOWNs, evidence/source coverage limitations, open questions, candidate safeguards, and no score/findings/approval. | Covered by report instructions and provisional handling. | NOT TESTED |

## Execution Procedure

1. Open a new Microsoft Copilot Chat session. Test the surface intended for staff use; do not infer behavior in other Copilot products or models.
2. Run A and B using only `SAR-STAFF-START.md`. Record the first response and question order.
3. Run C with a synthetic proposal; run D with no documentation and synthetic answers.
4. For E and F, use a test network/corpus where a reference is unavailable or demonstrably partial; observe the stated limitation and continued useful analysis.
5. Run G and H in separate sessions. Verify no unsupported determination is produced and incomplete facts yield a useful provisional report.
6. Record each observed result as `PASS`, `FAIL`, `NOT TESTED`, `ENVIRONMENT LIMITATION`, or `INCONCLUSIVE`, with a brief excerpt/reference in controlled evidence. Update the table only after an actual run.

A pass in this scenario does not establish legal applicability, validate a control, complete source coverage, grant authorization, or demonstrate compatibility in an untested Copilot surface. Keep S15 evidence out of the public repository unless its content is approved for publication.
