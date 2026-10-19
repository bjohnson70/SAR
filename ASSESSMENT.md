# SAR Staff QA Launch Pointer v1.1.0

This root file points staff to the versioned SAR staff QA launch package. It is not the governed Submitter contract, a trusted runtime manifest, or assessment authorization.

## Current Staff QA Launch

- Launch instructions: [SAR-STAFF-LAUNCH-v1.1.md](SAR-STAFF-LAUNCH-v1.1.md)
- Portable initial request form for the no-document QA path: [SAR-STAFF-INITIAL-REQUEST-FORM-v1.1.md](SAR-STAFF-INITIAL-REQUEST-FORM-v1.1.md)
- Portable report template: [SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.1.md](SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.1.md)
- Organization presentation profiles: [SAR-STAFF-REPORT-PROFILES-v1.1.md](SAR-STAFF-REPORT-PROFILES-v1.1.md)
- Manual acceptance scenario: [S13-staff-qa-launch-v1.1.md](tests/submitter/scenarios/S13-staff-qa-launch-v1.1.md)

Staff must use an already approved Runtime / Launcher to retrieve and read required materials, verify their correspondence to a trusted runtime manifest, and establish authorization/readiness. This Markdown-only repository package does not implement that launcher. A repository URL, this pointer, or its contents do not themselves initialize SAR. Failure to read or verify required material or obtain trusted runtime context means STOP; no assessment is initialized.

The launch is for controlled staff QA only. It does not provide a production assessment service, scoring model, approval workflow, applicability engine, or execution authorization.

## Version Migration

This v1.1 pointer supersedes the root v1.0 launch for current staff QA distribution. The historical v1.0 S01-v2 launch is preserved byte-for-byte at [tests/submitter/launch/v1.0/ASSESSMENT.md](tests/submitter/launch/v1.0/ASSESSMENT.md); its SHA-1 Git blob identity is `a0be24ed3564fd954c218a7775789b0f8ca14e12`. S01-v2 remains historical and uses that archived launch plus its pinned `SAR Submitter v1.0` contract. S01-v3 and S13 use the v1.1 launch assets and current `SAR Submitter v1.1` contract. Neither version substitutes for trusted runtime context.

This pointer is documentation only and does not start an assessment.
