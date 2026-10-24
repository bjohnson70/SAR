# SRAT Preliminary Scoring Decision Record

**Tracking:** SAR-CODEX-078-SRAT-02

**Status:** OPEN — CISO authorization not recorded

**Reference:** [Profile v1.0 and workbook provenance](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md)

## Scope Decision Recorded

The requester replaced the original fourteen-factor GenAI scope with the supplied `DDS_SRAT_v1r5_Default_High.xlsx` ten-variable model and chose to document its numeric rules as source-reported only. All other document-first, privacy, nine-section, QA, and feature-branch publication requirements remain. This implementation direction is **not CISO scoring authorization**.

The original request's 14–70 possible total versus 8–40 bands cannot be resolved from this workbook: that is a different, unavailable reference. Do not attribute those anchors/thresholds to DDS v1r5 or invent a crosswalk.

## Actual Workbook Inconsistencies

1. **Total 26 has no band.** Ten category values of 1–3 yield totals 10–30. `RAT SCORECARD!A33` defines Low <=10, Low Medium 11–15, Medium 16–20, Medium High 21–25, High >26. Within valid integer totals, 10 and 11–25 and 27–30 are covered, but 26 is not. **Recommendation (PROPOSED ONLY):** if these five bands are retained, change High to **>=26**, explicitly restrict totals to valid ten-category integer inputs, and test boundaries 10, 11, 15, 16, 20, 21, 25, 26, 27, 30. Do not use this correction before approval; do not collapse five bands to three without a separate decision.
2. **Descriptive anchors and formulas are different methods.** I's formula can produce Medium for a partial Yes set that does not fit its policy-only description. II's narrative names three compliance items but its formula counts six, including CCPA and accessibility. III's scorecard uses TLS 1.2, worksheet question TLS 1.3; fully encrypted PHI can receive formula Low rather than descriptive Medium. V's secure-development narrative is not the same as its five formula questions. VI's descriptive Medium/High overlap and its formula counts eight topics. VII's mutually exclusive no-transfer/transfer questions prevent a coherent all-Yes Low, while the descriptive Low permits no transfer. VIII and IX also count questions rather than directly testing every descriptive condition. Do not silently choose formula or description as authoritative.
3. **Unknowns and input validity.** The scoring sheet deliberately defaults blanks/errors/zero to High. This is different from SAR's preliminary rule that missing evidence is not a deficiency. Yes-count formulas also convert non-Yes nonblank text to zero; range guards do not fully enforce integer/enumerated responses. Shared formulas are normal workbook encoding, not missing logic. **Recommendation:** retain UNKNOWN outside numeric scoring until a supported input policy and validation rules are approved.
4. **N/A and non-GenAI mismatch.** Scorecard C30 says non-GenAI is N/A/Low (1), but X's D20 requires B14/B19 and returns 3 when blank; no non-GenAI branch is present there. Removing X would change the denominator. Other law-, DDS-, AI-, cloud-, or database-specific questions also lack a general N/A rule.
5. **X relies on different referenced artifacts.** Narrative anchors cite SIMM 5305-F Part I; D20 uses a SIMM 5310-C PTA/PIA completion answer and PIA risk level. GenAI B3:B10 questions do not feed the score. Its No/CDT text is a source statement, not authority to impose that process on every organization.

## Decisions Requiring CISO Authorization

| ID | Decision needed | Recommendation (not approved) | Interim preliminary behavior |
|---|---|---|---|
| CISO-01 | Confirm source identity/version, authority, ownership, currentness and publication permissions; ten-variable model versus separate fourteen-factor reference | Confirm the exact workbook hash and approved reference/version; obtain the other scale only if still needed | Attribute workbook as supplied, not authenticated/approved; do not publish workbook bytes |
| CISO-02 | Choose descriptive anchors versus worksheet formulas; resolve overlapping/missing definitions and TLS minimum | Reconcile each variable, input and source location into one versioned rule set; explicitly resolve VI overlap and VII incompatible Yes conditions | Unique descriptive matches only as provisional nonnumeric bands; conflicts/partial matches UNRESOLVED |
| CISO-03 | Approve missing-information, invalid-input and intermediate-value rules | Keep unknown distinct from an adverse answer; require valid enumerations and integer category outputs; no 1–5 interpolation | No numeric default HIGH; missingness remains visible |
| CISO-04 | Approve N/A and software/organization-specific scope rules | One general profile with conditional X; define treatment of irrelevant subquestions, denominator and totals before numeric use | Retain ten rows, N/A has no numeric value; no scaling or denominator adjustment |
| CISO-05 | Correct total 26 gap, establish valid total range and any mapping to three overall bands | High >=26 is the smallest proposed correction if retaining five bands; validate all boundaries; do not presume a three-band crosswalk | Publish no assigned SAR total or numeric overall band |
| CISO-06 | Confirm weighting/aggregation, dependency/double-counting treatment and any overrides | Make equal weighting explicit only if the ten-score sum is adopted; calibrate against representative cases and harms | Existing qualitative likelihood/impact matrix; highest defensible material scenario, not factor average |
| CISO-07 | Resolve X's SIMM 5305-F versus 5310-C basis and non-GenAI formula discrepancy; supported substitutions for non-State entities | Require supported source-specific organizational scope; define any equivalent privacy/AI review separately | No automatic SIMM/DGS/CDT obligation or new gate; assess underlying facts qualitatively |
| CISO-08 | Authorize release of a finalized numeric methodology and its approval record | Record decision maker/authority, date, effective scope, profile version, resolved rules and calibration/test evidence | Working guidance is not CISO-approved; live behavior tests remain NOT TESTED until executed |

## Until Decisions Are Approved

Use [the launcher](SAR-STAFF-START.md) and [report template](SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.3.md) immediately with supplied documents. Follow the profile's provisional evidence/match rules and explain unresolved factor bands without delaying a defensible qualitative assessment. Historical numeric results remain attributed history. A signed vendor review is neither SAR's assessment nor scoring authorization.

An eventual approved decision must supersede this record explicitly, preserve the previous profile/report basis, and update the profile, launcher reference, template, and regression expectations together. Static repository checks are not live Copilot QA, validated safeguards, compliance certification, or software approval.
