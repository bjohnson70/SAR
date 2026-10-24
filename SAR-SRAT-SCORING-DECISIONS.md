# SRAT Scoring Decision Record

**Tracking:** SAR-CODEX-079; preserves SAR-CODEX-078-SRAT-02 history

**Status:** Architectural direction supplied as CISO-approved; targeted methodology decisions remain OPEN

**Reference:** [Profile v1.0 and workbook provenance](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md)

## Historical 078 Scope Decision

The requester replaced the original fourteen-factor GenAI scope with the supplied `DDS_SRAT_v1r5_Default_High.xlsx` ten-variable model and chose to document its numeric rules as source-reported only. All other document-first, privacy, nine-section, QA, and feature-branch publication requirements remain. This implementation direction is **not CISO scoring authorization**.

The original request's 14–70 possible total versus 8–40 bands cannot be resolved from this workbook: that is a different, unavailable reference. Do not attribute those anchors/thresholds to DDS v1r5 or invent a crosswalk.

### SAR-CODEX-079 Direction — Superseding the 078 Interim Numeric Restriction

The current task supplies **CISO-approved architectural direction** to implement DDS SRAT v1r5 independently, with worksheet-specific raw formulas, mandatory default-HIGH effective scores and evidence-supported reductions. That direction supersedes 078's prohibition on assigned SRAT numbers and its descriptive-match-only interim procedure. It does not approve the proposed score-26 correction, N/A reduced-scope classification, a NIST crosswalk or changes to SAR's qualitative conclusions. No additional institutional signature, authorization date or legal authority is invented.

The [module](tools/srat.py) uses methodology `DDS-SRAT` / `v1r5`, implementation `1.0.0`. The [profile](SAR-SRAT-PRELIMINARY-SCORING-PROFILE-v1.0.md) now documents the independent procedure and the [report renderer](tools/sar_report.py) keeps methodology results separate. Historical S16 remains pinned to 078; its no-numbers expectations are not current module requirements.

## Actual Workbook Inconsistencies

1. **Total 26 has no band.** Ten category values of 1–3 yield totals 10–30. `RAT SCORECARD!A33` defines Low <=10, Low Medium 11–15, Medium 16–20, Medium High 21–25, High >26. Within valid integer totals, 10 and 11–25 and 27–30 are covered, but 26 is not. **Recommendation (PROPOSED ONLY):** if these five bands are retained, change High to **>=26**, explicitly restrict totals to valid ten-category integer inputs, and test boundaries 10, 11, 15, 16, 20, 21, 25, 26, 27, 30. Do not use this correction before approval; do not collapse five bands to three without a separate decision.
2. **Descriptive anchors and formulas are different methods.** I's formula can produce Medium for a partial Yes set that does not fit its policy-only description. II's narrative names three compliance items but its formula counts six, including CCPA and accessibility. III's scorecard uses TLS 1.2, worksheet question TLS 1.3; fully encrypted PHI can receive formula Low rather than descriptive Medium. V's secure-development narrative is not the same as its five formula questions. VI's descriptive Medium/High overlap and its formula counts eight topics. VII's mutually exclusive no-transfer/transfer questions prevent a coherent all-Yes Low, while the descriptive Low permits no transfer. VIII and IX also count questions rather than directly testing every descriptive condition. Do not silently choose formula or description as authoritative.
3. **Unknowns and input validity.** The scoring sheet deliberately defaults blanks/errors/zero to High. Yes-count formulas also convert non-Yes nonblank text to zero; range guards do not fully enforce integer/enumerated responses. Shared formulas are normal workbook encoding, not missing logic. Under 079 the module preserves raw formula behavior but never allows Unknown/N/A/arbitrary responses, incomplete assessment or missing validated evidence to lower effective risk. SRAT HIGH due to incomplete assurance is not a confirmed deficiency and does not alter SAR qualitative unknown handling.
4. **N/A and non-GenAI mismatch.** Scorecard C30 says non-GenAI is N/A/Low (1), but X's D20 requires B14/B19 and returns 3 when blank; no non-GenAI branch is present there. Removing X would change the denominator. Other law-, DDS-, AI-, cloud-, or database-specific questions also lack a general N/A rule.
5. **X relies on different referenced artifacts.** Narrative anchors cite SIMM 5305-F Part I; D20 uses a SIMM 5310-C PTA/PIA completion answer and PIA risk level. GenAI B3:B10 questions do not feed the score. Its No/CDT text is a source statement, not authority to impose that process on every organization.

## Decision Disposition and Remaining CISO Authorization

| ID | Decision needed | Recommendation (not approved) | Interim preliminary behavior |
|---|---|---|---|
| CISO-01 | Source authority, ownership, currentness and publication permissions | 079 identifies the ten-variable workbook as approved reference; independently establish canonical provenance and workbook publication permission | Pin the recorded hash; do not commit workbook bytes or claim institutional authentication |
| CISO-02 | Reconcile narrative/formula differences and TLS requirements | 079 directs use of worksheet formulas, not descriptive substitutions. Any correction to those formulas requires a versioned decision | Raw logic retains III/VII/X discrepancies; evidence gates do not rewrite it |
| CISO-03 | Evidence sufficiency, verification authority and input exceptions | Default-HIGH and integer 1/2/3 are required by 079. Operationally define authorized verifiers, review scope and any permitted per-question exception | Every required answer needs validated, located evidence and a dated reviewer justification before effective reduction; Unknown/N/A cannot lower it |
| CISO-04 | N/A reduced-scope aggregation/classification and exclusion authority | Approve a justified reduced-scope calculation/classification policy and reviewer authority; do not silently rescale | Approved N/A excluded from the sum; count/list disclosed; affected overall classification PROVISIONAL without a band |
| CISO-05 | Correct total 26 gap | High >=26 remains the smallest proposed correction if retaining five bands; **PROPOSED ONLY**, not implemented | Total 26 is UNCLASSIFIED/provisional; invalid totals never LOW; no three-band crosswalk |
| CISO-06 | Future weighting, dependency/double-counting treatment and overrides | 079 retains the source's sum for all ten applicable variables (10–30, initial 30); any changed weighting/override needs a new version | Sum effective integers, no averaging or composite score across methodologies; NIST/qualitative results independent |
| CISO-07 | X's SIMM 5305-F versus 5310-C basis and non-State organizational substitutions | Define supported equivalents and scope-specific exemptions if desired | X raw uses B14/B19; contextual B3:B10 completion/evidence gates effective reductions. No automatic SIMM/DGS/CDT obligation |
| CISO-08 | Operational release/authorization records, trusted evidence integration and final-artifact process | Preserve supplied 079 authority; record production roles, review evidence, effective scope and actual live QA before broader deployment | Standard-library module and synthetic tests are not trusted runtime execution, validated software approval or a live Copilot PASS; PDF only on reviewer request |

## Implemented Calculation Policy and Differences From Workbook

Use [the launcher](SAR-STAFF-START.md) and [report template](SAR-STAFF-ASSESSMENT-REPORT-TEMPLATE-v1.3.md) immediately. Keep all ten rows and outstanding gaps. A numerical result is displayed only when the independent module actually ran; otherwise disclose NOT EXECUTED and proceed with the qualitative report.

- Raw D-cell formulas and all-ten source bands are preserved; source total 26 remains unclassified. Cached workbook values are not test oracles; no Excel recalculation has been claimed.
- **Additional effective-score assurance:** all required responses, validated evidence with source/location/verifier/date, Assessed status, reviewer/date and reduction justification are required. X's contextual B3:B10 completion is required even though those cells do not affect raw D20. Worksheet dropdowns permit Unknown/N/A and arbitrary nonblank inputs can feed formulas; none can produce an effective reduction here. Integer-only outputs are enforced.
- **Explicit applicability difference:** non-GenAI X is not automatically 1 (descriptive anchor) or automatically excluded. Pending N/A stays 3; reviewer-approved N/A with basis/date and established no-GenAI scope excludes X, with provisional reduced-scope classification. Any approved N/A exclusion affects only SRAT, never NIST controls or privacy applicability.
- **Aggregation policy:** sum effective values for applicable categories; excluded values are `None`, not zero. Show applicable count/list. With exclusions do not apply ten-variable bands or choose a normalization denominator. With zero applicable categories, total is undefined and requires review, not LOW.
- **Boundaries:** unknown SRAT assurance may yield HIGH while SAR qualitative risk remains LOW/MODERATE. There is no automatic mathematical crosswalk, combined score or NIST mutation.

Evidence status is a trusted-caller assertion, not cryptographically established by the library. Reusing a reference does not establish sufficient verification for a different scope. Operational authorization and artifact storage remain outside this bounded module.

An eventual approved decision must supersede this record explicitly, preserve the previous profile/report basis, and update the profile, launcher reference, template, and regression expectations together. Static repository checks are not live Copilot QA, validated safeguards, compliance certification, or software approval.

## Automated Verification — 2026-10-23

Executed on the 079 implementation before publication, with synthetic assessment data only:

| Command / check | Observed result |
|---|---|
| `python -m unittest discover -s tests\staff -v`, with `SAR_SRAT_WORKBOOK` pointing to the supplied local workbook | **33 passed**: 20 calculation/report tests, 9 document/link tests, 4 local workbook-source checks; no skips |
| `python -m unittest discover -s tests\requirements -v` | **20 passed**, preserving existing requirement/governance regressions |
| Binary source truth tables | All **516** Yes/No combinations across I–IX checked; X PIA branch, context completion and missing/invalid input cases separately covered |
| Local workbook-source checks | Exact SHA-256, all variable input/score mappings, shared response formulas, category branch thresholds, X source expressions, total formula and original threshold legend verified |
| Qualitative rubric preservation | Exact launcher rubric text compared against baseline `26986021b79c22e926939b3da199fc1fc2963d02`; unchanged |
| Python syntax compilation | All three implementation modules compiled successfully in memory |

Cases A–F and I are covered by calculation/evidence/applicability tests; G by independent input/result preservation; H by generated nine-section Markdown with separate method subsections; J by existing regressions plus document-first/static checks. A generated report without an executed SRAT result is also tested and explicitly says NOT EXECUTED.

These are actual library executions and source/document checks, **not Excel recalculation, independent validation of any real evidence, production integration or live Microsoft Copilot Chat QA**. Live behavior for this revision remains NOT TESTED. The workbook stays local and is not a repository dependency; optional source tests skip explicitly when its path is not provided.
