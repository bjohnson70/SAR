# HIPAA Safe Harbor Identifiers — Governed Conversational Interpretation

## Purpose

This artifact defines the governed interpretation layer for the federal HIPAA Safe Harbor identifiers preserved in `HIPAA-IDENTIFIERS.md`.

It is not the federal regulation, HHS/OCR guidance, a replacement for `HIPAA-IDENTIFIERS.md`, a HIPAA applicability determination, a PHI determination, a de-identification determination, a risk assessment, a control mapping, or a Reviewer decision.

## Governance Status

Federal source terminology, authoritative federal explanation, SAR-governed interpretation, and participant response remain separate. Every record maps to exactly one existing `HIPAA-ID-01` through `HIPAA-ID-18`. No new HIPAA identifier is created.

Interpretation status vocabulary:

- `SOURCE_EXPLICIT` — Directly stated in the federal source terminology or regulation.
- `AUTHORITATIVE_GUIDANCE` — Explicitly explained by HHS/OCR guidance.
- `SAR_APPROVED_INTERPRETATION` — An explicitly approved SAR presentation decision, such as a group assignment supplied for this artifact.
- `SAR_INTERPRETATION_REQUIRED` — Participant-facing wording, examples, or boundaries require further SAR governance.
- `NONE_APPROVED` — No approved explanation, example, or boundary is available for use.

No element currently has `GOVERNED` participant-facing wording. The six presentation groups are:

```text
PROPOSED — HUMAN REVIEW REQUIRED
```

## Authority and Provenance

- **Regulatory authority:** 45 CFR § 164.514(b)(2), the Safe Harbor implementation specification.
- **Explanatory authority:** U.S. Department of Health and Human Services, Office for Civil Rights, *Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule*.
- **Source-preservation artifact:** `HIPAA-IDENTIFIERS.md`.

The HHS guidance explains the regulation; it is not the regulation. Identifier discovery does not determine HIPAA applicability, PHI status, or de-identification status.

## Element Interpretation Records

Each record preserves the federal source terminology and identifies the current interpretation status. No unsupported participant examples are approved.

### HIPAA-ID-01

- **Federal item:** A
- **Federal terminology:** Names
- **SAR presentation group:** Names, Contact, and Geographic Information
- **Authoritative explanation:** HHS explains names associated with the individual, relatives, employers, and household members.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** HUMAN GOVERNANCE REQUIRED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve participant-facing wording without broadening the federal category.

### HIPAA-ID-02

- **Federal item:** B
- **Federal terminology:** All geographic subdivisions smaller than a state, including street address, city, county, precinct, ZIP code, and equivalent geocodes, subject to the stated three-digit ZIP exception.
- **SAR presentation group:** Names, Contact, and Geographic Information
- **Authoritative explanation:** HHS explains the first-three-digit ZIP rule, population condition, restricted ZIP treatment, current Census data, and ZCTAs.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Preserve subdivisions smaller than a state, listed geographic categories, the ZIP exception, population condition, `000` treatment, and current-data basis. Do not reduce this to address alone.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve concise wording that preserves the federal exception.

### HIPAA-ID-03

- **Federal item:** C
- **Federal terminology:** All elements of dates (except year) directly related to an individual, including listed dates and ages over 89, with the stated age aggregation.
- **SAR presentation group:** Dates and Health-Record Identifiers
- **Authoritative explanation:** HHS explains that day, month, and more-specific-than-year dates are restricted and ages over 89 are treated as 90 or older.
- **Approved examples:** HHS example: January 1, 2009 versus 2009. No additional participant examples approved.
- **Boundary / do not confuse with:** Preserve the year exception, age-over-89 treatment, age-90-or-older aggregation, and date-of-test/health-care context.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve wording that does not reduce this to birth date.

### HIPAA-ID-04

- **Federal item:** D
- **Federal terminology:** Telephone numbers
- **SAR presentation group:** Names, Contact, and Geographic Information
- **Authoritative explanation:** HHS references personal phone numbers in PHI-context discussion.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** HUMAN GOVERNANCE REQUIRED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve ordinary-language wording.

### HIPAA-ID-05

- **Federal item:** E
- **Federal terminology:** Fax numbers
- **SAR presentation group:** Names, Contact, and Geographic Information
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** NONE APPROVED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording and boundaries.

### HIPAA-ID-06

- **Federal item:** F
- **Federal terminology:** Email addresses
- **SAR presentation group:** Names, Contact, and Geographic Information
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** NONE APPROVED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording and boundaries.

### HIPAA-ID-07

- **Federal item:** G
- **Federal terminology:** Social security numbers
- **SAR presentation group:** Account and License Identifiers
- **Authoritative explanation:** HHS states that parts or derivatives, such as the last four digits, do not satisfy Safe Harbor.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Do not broaden to authentication or financial categories.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve participant-facing wording.

### HIPAA-ID-08

- **Federal item:** H
- **Federal terminology:** Medical record numbers
- **SAR presentation group:** Dates and Health-Record Identifiers
- **Authoritative explanation:** HHS uses medical records, laboratory reports, and hospital bills in PHI-context examples.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Do not broaden to all information in a medical record.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve wording and boundaries.

### HIPAA-ID-09

- **Federal item:** I
- **Federal terminology:** Health plan beneficiary numbers
- **SAR presentation group:** Dates and Health-Record Identifiers
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** NONE APPROVED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording and boundaries.

### HIPAA-ID-10

- **Federal item:** J
- **Federal terminology:** Account numbers
- **SAR presentation group:** Account and License Identifiers
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Do not broaden to credentials, usernames, passwords, or financial information without separate governance.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve wording that does not broaden account numbers.

### HIPAA-ID-11

- **Federal item:** K
- **Federal terminology:** Certificate/license numbers
- **SAR presentation group:** Account and License Identifiers
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Do not label generally as credentials or authorization information.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording.

### HIPAA-ID-12

- **Federal item:** L
- **Federal terminology:** Vehicle identifiers and serial numbers, including license plate numbers
- **SAR presentation group:** Vehicle, Device, Web, and Network Identifiers
- **Authoritative explanation:** License plate numbers are explicit in the federal terminology.
- **Approved examples:** License plate numbers — SOURCE_EXPLICIT. No additional examples approved.
- **Boundary / do not confuse with:** Do not broaden to all vehicle information.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording.

### HIPAA-ID-13

- **Federal item:** M
- **Federal terminology:** Device identifiers and serial numbers
- **SAR presentation group:** Vehicle, Device, Web, and Network Identifiers
- **Authoritative explanation:** The federal category is explicit. Detailed DI/PI wording in the source artifact was not independently located during research.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Detailed model/version versus specific-device interpretation requires authoritative verification.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Verify the exact HHS passage before promoting DI/PI wording or examples.

### HIPAA-ID-14

- **Federal item:** N
- **Federal terminology:** Web Universal Resource Locators (URLs)
- **SAR presentation group:** Vehicle, Device, Web, and Network Identifiers
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** NONE APPROVED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording.

### HIPAA-ID-15

- **Federal item:** O
- **Federal terminology:** Internet Protocol (IP) addresses
- **SAR presentation group:** Vehicle, Device, Web, and Network Identifiers
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** NONE APPROVED
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve participant-facing wording.

### HIPAA-ID-16

- **Federal item:** P
- **Federal terminology:** Biometric identifiers, including finger and voice prints
- **SAR presentation group:** Biometric and Image Information
- **Authoritative explanation:** Finger and voice prints are explicit federal examples.
- **Approved examples:** Finger prints; voice prints — SOURCE_EXPLICIT.
- **Boundary / do not confuse with:** Do not add other biometric examples without governance.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve wording and any additional examples.

### HIPAA-ID-17

- **Federal item:** Q
- **Federal terminology:** Full-face photographs and any comparable images
- **SAR presentation group:** Biometric and Image Information
- **Authoritative explanation:** NO ADDITIONAL AUTHORITATIVE INTERPRETATION FOUND
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** “Comparable images” requires governed clarification.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT
- **Unresolved interpretation work:** Approve wording and examples.

### HIPAA-ID-18

- **Federal item:** R
- **Federal terminology:** Any other unique identifying number, characteristic, or code, except as permitted by paragraph (c) of § 164.514.
- **SAR presentation group:** Other Unique Identifying Information
- **Authoritative explanation:** HHS explains unlisted unique features, including clinical trial record numbers, insecure codes, record barcodes, and distinctive characteristics such as a unique occupation. HHS also explains the § 164.514(c) re-identification-code exception.
- **Approved examples:** NONE APPROVED
- **Boundary / do not confuse with:** Do not turn this into other sensitive information, other credentials, other account information, or a catch-all for future SAR data sets.
- **Interpretation status:** SAR_INTERPRETATION_REQUIRED
- **Provenance classification:** SOURCE_EXPLICIT; AUTHORITATIVE_GUIDANCE
- **Unresolved interpretation work:** Approve a dedicated residual-category question and boundary wording.

## Presentation Groups

These are SAR presentation mechanisms, not federal HIPAA categories. They do not alter the federal 18 and do not determine HIPAA applicability or PHI status.

```text
PROPOSED — HUMAN REVIEW REQUIRED
```

### Group 1 — Names, Contact, and Geographic Information

- **Members:** HIPAA-ID-01, HIPAA-ID-02, HIPAA-ID-04, HIPAA-ID-05, HIPAA-ID-06
- **Rationale:** Direct names, contact, and geographic categories.
- **Authoritative support:** Federal terms; HHS provides names/phone context and detailed ZIP guidance.
- **SAR interpretation required:** Participant wording.
- **Remaining ambiguity:** HIPAA-ID-02 must retain its geographic and ZIP exceptions.

### Group 2 — Dates and Health-Record Identifiers

- **Members:** HIPAA-ID-03, HIPAA-ID-08, HIPAA-ID-09
- **Rationale:** Dates and medical/benefit record identifiers.
- **Authoritative support:** Federal terms; HHS provides date and medical-record context.
- **SAR interpretation required:** Participant wording.
- **Remaining ambiguity:** HIPAA-ID-09 has little additional HHS explanation.

### Group 3 — Account and License Identifiers

- **Members:** HIPAA-ID-07, HIPAA-ID-10, HIPAA-ID-11
- **Rationale:** Explicit account-number and certificate/license-number categories.
- **Authoritative support:** Federal terms only.
- **SAR interpretation required:** Group label and participant wording.
- **Remaining ambiguity:** Do not call these credentials or authorization information without further governance.

### Group 4 — Vehicle, Device, Web, and Network Identifiers

- **Members:** HIPAA-ID-12, HIPAA-ID-13, HIPAA-ID-14, HIPAA-ID-15
- **Rationale:** Vehicle, device, URL, and IP categories.
- **Authoritative support:** Federal terms.
- **SAR interpretation required:** Participant wording.
- **Remaining ambiguity:** HIPAA-ID-13 needs verified DI/PI guidance before detailed examples.

### Group 5 — Biometric and Image Information

- **Members:** HIPAA-ID-16, HIPAA-ID-17
- **Rationale:** Biometric and image categories.
- **Authoritative support:** Federal terms; finger and voice prints are explicit examples.
- **SAR interpretation required:** “Comparable images” and additional examples.
- **Remaining ambiguity:** Do not expand beyond approved source material.

### Group 6 — Other Unique Identifying Information

- **Members:** HIPAA-ID-18
- **Rationale:** Residual category with distinct HHS guidance and the § 164.514(c) exception.
- **Authoritative support:** Federal text and HHS guidance.
- **SAR interpretation required:** Dedicated question and careful boundary.
- **Remaining ambiguity:** It must not become a catch-all for every sensitive-data category.

## Group-Level Response Semantics

Future SUBMITTER.md use may ask a group-level question and allow:

- `YES`;
- `NO`;
- `UNKNOWN`; and
- `EXAMPLES`, only when approved examples exist.

`YES` expands to the individual identifiers in the current group.

`NO` becomes participant-reported `NO` for the group’s members only after explicit confirmation that all displayed members may be recorded as `NO`.

`UNKNOWN` preserves the group as unresolved. It is not converted to `NO`.

`EXAMPLES` displays only governed approved examples. The AI must never invent examples.

## Element-Level Response Semantics

When a group expands:

- show every governed identifier in the current group;
- allow numbered selections;
- allow comma-separated selections;
- allow natural-language responses;
- allow `ALL`;
- allow `NONE`; and
- allow `UNKNOWN`.

`ALL` and `NONE` apply only to the currently displayed group. Omission is never evidence of absence.

## Deterministic Omitted-Selection Rule

If the displayed elements are `1, 2, 3, 4` and the participant selects `1, 3`, record:

```text
1 = selected / YES
3 = selected / YES
2 = unresolved pending confirmation
4 = unresolved pending confirmation
```

Then ask:

> Can I record 2 and 4 as No?

- `YES`: record participant-reported `NO` for 2 and 4.
- `NO`: allow correction or additional selections.
- `UNKNOWN`: retain unresolved state.

Never derive `NO` from omission.

## Response and Provenance Model

Future response records should preserve, at minimum:

- `identifier_id` or `presentation_group_id`;
- `participant_response`;
- `source_actor`;
- response date/session where available;
- supporting reference where available;
- validation state; and
- unresolved reason where applicable.

Keep these separate:

```text
Participant Response = UNRESOLVED
Reviewer/SAR Treatment = POTENTIALLY PRESENT
```

This interpretation artifact does not perform Reviewer treatment.

## Corrections and Continuation

Future Submitter artifacts should:

- preserve prior responses;
- allow participant corrections;
- record the current response;
- retain lightweight correction/activity history;
- preserve participant/session provenance where available;
- avoid re-asking adequately resolved items; and
- continue unresolved items across people and AI models.

A full event-sourcing system is not required for the initial design.

## Future Governed Data Sets

The interpretation pattern may later be reused for separately governed sets such as:

- financial/payment;
- authentication/security-sensitive;
- confidential business;
- DDS/state-specific; and
- AI-specific information.

Those sets require their own authority and provenance. They must not modify the HIPAA 18 or inherit HIPAA authority merely because they are used in the same SAR assessment.

## Source References

- eCFR, 45 CFR § 164.514: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-E/section-164.514
- HHS/OCR, *Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the HIPAA Privacy Rule*: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
- HHS/OCR full guidance PDF: https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/understanding/coveredentities/De-identification/hhs_deid_guidance.pdf

These links are source references only. This artifact does not replace the regulatory text or HHS guidance, and it does not perform legal or applicability analysis.

## Research Status

The federal sources provide strong support for the 18 categories and several boundaries, but human governance is still required for final participant-facing wording, examples, group labels, device clarification, and residual-category handling.
