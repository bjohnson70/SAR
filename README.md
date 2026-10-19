# SAR Staff QA Launch

This repository contains SAR governance documents and a **Markdown-only staff QA launch package**. It does not contain a production launcher, trusted runtime, online form, scoring engine, or assessment service.

## Staff Launch v1.1.0

- [Current launch pointer](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/ASSESSMENT.md)
- [Versioned launch instructions](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/SAR-STAFF-LAUNCH-v1.1.md)
- [Initial request form for the NO-document QA path](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/SAR-STAFF-INITIAL-REQUEST-FORM-v1.1.md)
- [Portable Markdown assessment report template](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.1.md)
- [Organization presentation profiles](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/SAR-STAFF-REPORT-PROFILES-v1.1.md)
- [Manual S13 launch acceptance scenario](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/tests/submitter/scenarios/S13-staff-qa-launch-v1.1.md)

## Staff QA Steps

1. Use only an AI environment approved for the information you plan to share. Do not submit actual PHI or sensitive personal information in an unapproved environment.
2. Use an already approved SAR Runtime / Launcher to retrieve and read the configured Markdown resources and establish trusted execution context. This repository provides instructions only; it cannot initialize runtime authorization itself.
3. If a required resource is unavailable, unreadable, mismatched, or trusted runtime context is unavailable, stop. Report that no assessment initialized. A URL, branch, Markdown file, or successful GitHub read is not runtime authorization.
4. After verified startup, choose Department, Regional Center, or Service Provider. This changes report emphasis only; it does not determine applicability.
5. Answer the documentation YES/NO question. YES follows document-first intake. NO uses the versioned Markdown initial request form; no online form URL is provided.
6. Prepare the portable report from the Markdown template. Preserve source/fact/evidence states and unknowns, use the organization presentation profile, and state that governed scoring is pending. Do not imply approval, applicability, validated controls, residual risk, or execution.
7. Save the report and answers as portable Markdown input for a future authorized SAR session. Its continuation instructions do not provide authorization or create identities.

The repository-root `ASSESSMENT.md` is a v1.1 launch pointer. The historical v1.0 S01-v2 launch is byte-preserved at [tests/submitter/launch/v1.0/ASSESSMENT.md](https://github.com/bjohnson70/SAR/blob/sar-codex-074-staff-qa-launch/tests/submitter/launch/v1.0/ASSESSMENT.md); S01-v2 continues to use that archive. S01-v3 and S13 use the v1.1 Markdown launch source. This branch adds no executable launcher or automated S13 code tests; the S13 scenario is a manual acceptance definition.
