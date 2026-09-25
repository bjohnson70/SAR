# HIPAA Safe Harbor Identifiers

## Purpose

This artifact preserves the federally documented 18 identifier categories used by the HIPAA Safe Harbor de-identification method and gives them stable SAR identities.

These 18 identifiers are SAR's initial governed identifier set. They are not the complete universe of sensitive, personally identifiable, confidential, security-sensitive, authentication, financial, DDS, or other data categories. Future governed sets may coexist without changing this federal set.

## Federal Authority

- **Regulatory authority:** 45 CFR § 164.514(b)(2)
- **Explanatory authority:** U.S. Department of Health and Human Services, Office for Civil Rights, *Guidance Regarding Methods for De-identification of Protected Health Information in Accordance with the Health Insurance Portability and Accountability Act (HIPAA) Privacy Rule*
- **Guidance distinction:** The HHS guidance explains the Safe Harbor and Expert Determination methods; it is not itself the regulation.
- **Federal method addressed here:** Safe Harbor identifier categories.

## Safe Harbor Context

The Safe Harbor categories concern identifiers of:

- the individual;
- relatives of the individual;
- employers of the individual; or
- household members of the individual.

Removing the listed identifiers alone does not automatically satisfy Safe Harbor. The covered entity must also not have actual knowledge that the remaining information could be used, alone or in combination with other information, to identify an individual who is a subject of the information.

Identifier discovery, HIPAA applicability, PHI determination, and de-identification determination remain separate SAR concepts. The presence of an identifier does not automatically establish that information is PHI or that HIPAA applies.

## Governance Boundaries

- The HIPAA Safe Harbor baseline contains exactly 18 identifiers.
- SAR stable IDs do not replace or alter federal terminology.
- Future SAR data categories do not become additional HIPAA identifiers.
- Additional governed sets must not be represented as numbered extensions of this set.
- Future sets require their own identity, authority, provenance, and applicability basis.
- Source content and SAR conversational interpretation remain separate layers.
- Identifier presence does not automatically establish PHI.
- HIPAA applicability is determined separately from identifier discovery.
- This artifact does not create conversational groups, Submitter questions, risk scores, classifications, NIST mappings, control mappings, or approval logic.

## Governed Identifiers

The following preserves the supplied federal A–R order and terminology. The SAR identifiers are stable references for this governed set; they do not replace the federal item letters or source text.

### HIPAA-ID-01

- **Federal item:** A
- **Federal source order:** 1
- **Federal terminology/source text:** Names

### HIPAA-ID-02

- **Federal item:** B
- **Federal source order:** 2
- **Federal terminology/source text:** All geographic subdivisions smaller than a state, including street address, city, county, precinct, ZIP code, and their equivalent geocodes, except for the initial three digits of the ZIP code if, according to the current publicly available data from the Bureau of the Census:
  - (1) The geographic unit formed by combining all ZIP codes with the same three initial digits contains more than 20,000 people; and
  - (2) The initial three digits of a ZIP code for all such geographic units containing 20,000 or fewer people is changed to 000.

### HIPAA-ID-03

- **Federal item:** C
- **Federal source order:** 3
- **Federal terminology/source text:** All elements of dates (except year) for dates that are directly related to an individual, including birth date, admission date, discharge date, death date, and all ages over 89 and all elements of dates (including year) indicative of such age, except that such ages and elements may be aggregated into a single category of age 90 or older.

### HIPAA-ID-04

- **Federal item:** D
- **Federal source order:** 4
- **Federal terminology/source text:** Telephone numbers

### HIPAA-ID-05

- **Federal item:** E
- **Federal source order:** 5
- **Federal terminology/source text:** Fax numbers

### HIPAA-ID-06

- **Federal item:** F
- **Federal source order:** 6
- **Federal terminology/source text:** Email addresses

### HIPAA-ID-07

- **Federal item:** G
- **Federal source order:** 7
- **Federal terminology/source text:** Social security numbers

### HIPAA-ID-08

- **Federal item:** H
- **Federal source order:** 8
- **Federal terminology/source text:** Medical record numbers

### HIPAA-ID-09

- **Federal item:** I
- **Federal source order:** 9
- **Federal terminology/source text:** Health plan beneficiary numbers

### HIPAA-ID-10

- **Federal item:** J
- **Federal source order:** 10
- **Federal terminology/source text:** Account numbers

### HIPAA-ID-11

- **Federal item:** K
- **Federal source order:** 11
- **Federal terminology/source text:** Certificate/license numbers

### HIPAA-ID-12

- **Federal item:** L
- **Federal source order:** 12
- **Federal terminology/source text:** Vehicle identifiers and serial numbers, including license plate numbers

### HIPAA-ID-13

- **Federal item:** M
- **Federal source order:** 13
- **Federal terminology/source text:** Device identifiers and serial numbers
- **HHS explanatory guidance:** In the HIPAA de-identification context, a device identifier associated merely with the model or version of a device is distinguishable from a serial or other number assigned to a specific device that may uniquely identify an individual. The Device Identifier (DI) portion corresponding to the model/version is not the kind of uniquely identifying device identifier addressed by the Safe Harbor prohibition. A Production Identifier (PI), including a serial number or other number corresponding to a specific device, may be identifying and is within the relevant HIPAA device-identifier concept.

### HIPAA-ID-14

- **Federal item:** N
- **Federal source order:** 14
- **Federal terminology/source text:** Web Universal Resource Locators (URLs)

### HIPAA-ID-15

- **Federal item:** O
- **Federal source order:** 15
- **Federal terminology/source text:** Internet Protocol (IP) addresses

### HIPAA-ID-16

- **Federal item:** P
- **Federal source order:** 16
- **Federal terminology/source text:** Biometric identifiers, including finger and voice prints

### HIPAA-ID-17

- **Federal item:** Q
- **Federal source order:** 17
- **Federal terminology/source text:** Full-face photographs and any comparable images

### HIPAA-ID-18

- **Federal item:** R
- **Federal source order:** 18
- **Federal terminology/source text:** Any other unique identifying number, characteristic, or code, except as permitted by paragraph (c) of § 164.514.

## Extensibility

SAR Data Discovery may later contain multiple governed data-element sets:

```text
SAR Data Discovery
    |
    +-- HIPAA Safe Harbor Identifiers
    |
    +-- Future governed identifier/data sets
            |
            +-- authority/provenance specific to that set
```

Future sets must not be presented as additional HIPAA identifiers, alter the HIPAA count, silently merge into this federal set, or inherit HIPAA authority without an applicable basis. They must not be represented as numbered extensions of the HIPAA-ID set.