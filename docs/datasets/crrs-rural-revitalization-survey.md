---
schema_version: 3
catalog_status: ready
id: crrs-rural-revitalization-survey
name: China Rural Revitalization Survey (CRRS 中国乡村振兴综合调查)
aka:
- CRRS
- 中国乡村振兴综合调查
- China Rural Revitalization Survey
- CASS RDI CRRS
provider: >-
  中国社会科学院农村发展研究所 (Institute of Rural Development, Chinese
  Academy of Social Sciences, RDI-CASS). Verified from the official RDI site
  rdi.cssn.cn (home, 调查数据 column and release notes, all fetched/read
  2026-08-15).
china_related: true
domains:
- agriculture
- rural development
- household
- public
- poverty
- rural revitalization

data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: >-
    Approved remote use of CRRS2020 and CRRS2022 village/household/member
    microdata, questionnaires, weights and coding information on the RDI
    cloud desktop. The official 2025-04-29 release note closes the former
    email-request channel: microdata stay in the controlled environment,
    and research results may be exported to the approved email only after
    administrator review. This is not a downloadable raw-data delivery.
  availability: ready-made
  ordinary_researcher_feasible: true
  summary: >-
    CRRS is a biennial national rural tracking survey by CASS RDI. Baseline
    2020: 10 provinces (Guangdong, Zhejiang, Shandong, Anhui, Henan,
    Heilongjiang, Guizhou, Sichuan, Shaanxi, Ningxia), 50 counties, 150
    townships, 300 villages, 300 village questionnaires + 3,700+ household
    questionnaires + 15,000+ household-member records. 2022 second wave
    (village tracking 100%, household tracking 81%); 2024 third wave added
    Liaoning, Shanxi, Hunan and Inner Mongolia (472 village + 5,800+ household
    questionnaires, 23,000+ members). Second-wave data release announced
    2025-04-29; a fourth wave was in preparation as of 2026-07 (official news).
  barrier: >-
    Domestic applicants only under the published rules; identity/institution
    review, a research plan, limited cloud accounts and a monthly lottery
    when demand exceeds capacity. Unsuccessful applicants roll forward
    within the application year. Only reviewed results leave the cloud.
    The published application endpoint was not logged into or tested in
    this review; consult the official note/contact for current operation.
  last_checked: '2026-10-26'

unit_of_observation: >-
  Three linked levels: village questionnaire, household questionnaire, and
  individual household-member records; panel tracking of baseline sample
  across waves
structure: panel (tracking survey; biennial waves 2020/2022/2024, fourth wave in preparation 2026)
geo_granularity:
- county (50 counties/districts at baseline), township (150), village (300)
geography: >-
  China; baseline 10 provinces across four regions (east/central/west/
  northeast): Guangdong, Zhejiang, Shandong, Anhui, Henan, Heilongjiang,
  Guizhou, Sichuan, Shaanxi, Ningxia; third wave (2024) added Liaoning,
  Shanxi, Hunan, Inner Mongolia
time_span:
  start: '2020'
  end: '2024'
  last_confirmed_release: '2025-04-29: CRRS2020 and CRRS2022 open for approved cloud use'
  coverage_note: >-
    Waves: 2020 baseline, 2022 second, 2024 third (completed per the
    2025-04-29 note); fourth-wave preparation news dated 2026-07 on the
    official site. The re-read release note grants cloud use of 2020/2022,
    not a 2024 release or downloadable microdata.
  last_checked: '2026-10-26'
frequency:
- biennial
sample_size: >-
  Baseline 2020: 300 villages, 3,700+ households, 15,000+ members. Third
  wave 2024: 472 village questionnaires, 5,800+ household questionnaires,
  23,000+ members (official release note, read 2026-08-15).
key_variables:
- Village-level questionnaire (village economy, organization, infrastructure)
- Household questionnaire (production, income, consumption, assets, land)
- Household-member records (demographics, education, employment, health)
- Tracking outcomes across waves (village tracking 100%, household 81% in 2022)
- 2020 example village collective-property-reform status, villagers' public
  participation, migration-for-work, household income, demographics and
  village context (paper-specific use; verify source variables in the approved
  delivery)

research_fit:
  best_for:
  - Rural China household/village panel research (released 2020/2022) on production,
    income, consumption and rural revitalization policies, with village-level
    context
  - Research fitting the CASS RDI rural survey family and approved domestic cloud-desktop use
  choose_over:
  - Choose CRRS over other rural household surveys when village+household
    linked design, released 2020/2022 waves, and CASS RDI provenance fit.
  - For nationally representative rural-urban household panels with long
    history use cfps/chip; CRRS is rural-focused and younger.
  not_good_for:
  - Urban households (rural sample)
  - Pre-2020 rural panel history
  - Full-population representativeness (10-province baseline, expanded to 14
    in 2024)
  needs_join_for:
  - County-level administrative/market context from china-stat-yearbook or
    county statistics
  - Policy exposure timing (belongs to the variation side of the design)
  variation_available:
  - Longitudinal tracking across released 2020/2022; 2024 fieldwork completion does not establish its release
  - Cross-county/cross-province variation (10 baseline provinces; 14 by 2024)
  topics:
  - rural revitalization
  - agriculture
  - rural households
  - village economy
  - rural development

good_for:
- rural household panel research
- village-level rural development
- rural revitalization policy evaluation
identification:
- panel tracking comparisons
- cross-sectional regional variation
linkable_keys:
- Village ID, household ID, member ID (tracking designed)
- County/province identifiers (normalization needed for external joins)

joins:
- target: china-stat-yearbook
  relation: complement
  keys:
  - county/province + year
  method: join county-level context with name/code normalization; verify geography fields in the delivered data
  evidence_status: plausible

access_routes:
- route: RDI cloud-desktop application (official release instructions)
  access_status: by-application
  direct_url: http://rdi.cssn.cn/dcsj/202504/t20250429_5871894.shtml
  requirements:
  - Domestic applicant eligible under the official note; overseas applicants are not currently included
  - Platform registration, identity and institutional documentation reviewed by the provider
  - Research plan after account allocation; personal non-commercial account and reviewed result exports
  steps:
  - Read the official second-wave note and follow its cloud-platform address and user manual; consult crrs_rdi@cass.org.cn if the endpoint or certificate is unavailable.
  - Register and submit the required identity/institution materials through the provider's process, not to this repository.
  - Await review and cloud-account allocation; oversubscribed approved applications enter the first-working-day monthly lottery, with annual reapplication required.
  - Submit the requested research plan after allocation, work on the two released waves inside the cloud, and request review before exporting research results.
  deliverable: Controlled cloud access to CRRS2020/2022 village/household/member data, questionnaires, weights and coding information; reviewed result exports, not a raw-file download
  cost: by-application
  last_checked: '2026-10-26'
  caveat: The former email data-request route was explicitly closed on 2025-04-29. The current note does not specify fees. This review read the official instructions without submitting identity documents, opening an account or verifying the cloud endpoint's current service availability.

access:
  url: http://rdi.cssn.cn/dcsj/202504/t20250429_5871894.shtml
  cost: by-application
  license: Personal non-commercial approved cloud use; no account sharing; result export requires review and published research must acknowledge the project
  format:
  - microdata files (exact formats unread)
  api: false
  how_to_get: Follow the official 2025-04-29 cloud-desktop instructions for domestic identity review, account allocation and research-plan submission. Work with CRRS2020/2022 in the controlled environment and export only reviewed results. The historical email microdata-request channel is closed.
caveats:
- The public 2025 paper verifies a 2020 use case and route, not that all
  variables, fields or sample counts recur in another CRRS wave; inspect the
  selected approved delivery and its questionnaire/codebook.
- The 2022-10-24 使用说明 mentions slightly different baseline village counts (156 in one passage vs 300 in the 2025 note); the 2025-04-29 release note is used as the primary source and the discrepancy is retained as unresolved.
- The 2025 note opens 2020/2022 to controlled use; 2024 collection and 2026 fieldwork preparation do not establish release of those later waves. The old email route described in the 2025 paper is historical and does not override the newer official procedure.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-28'

used_by:
- cite: >-
    Li & Gao (2025), The Impact of the Reform of Rural Collective Property
    Rights System on Villagers' Public Participation: An Empirical Study Based
    on CRRS 2020 Data
  doi: https://doi.org/10.1371/journal.pone.0316899
  journal: PLOS ONE
  year: 2025
  dataset_role: >-
    Linked 2020 village-committee and villager questionnaires used for a rural
    governance analysis; village variables are matched to villager records.
  evidence_type: publisher_full_text
  evidence_url: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0316899&type=printable
  data_note: >-
    The public full text states that the analysis uses de-identified 2020 CRRS
    data from CASS RDI. It describes 284 village-committee questionnaires and
    7,451 villager questionnaires after the authors' cleaning, and says that
    the village-level reform question was matched to villager records. Its data
    availability statement directs institutional applicants to the RDI page,
    the data-use form and the listed contact emails, with a reply within one
    week. This verifies a concrete 2020 use and route, not release of the
    authors' matched and cleaned analysis file.

provenance:
- source: http://rdi.cssn.cn/dcsj/202504/t20250429_5871894.shtml (official second-wave release note, browser re-read 2026-10-26 despite GitHub HEAD 403)
  field_scope:
  - Current 2020/2022 cloud-only use and closure of the former email-request channel
  - Domestic eligibility, identity review, research plan, account-capacity lottery and controlled result exports
  - Application instructions verified, not cloud service availability, approved credentials or raw-data delivery
  added: '2026-10-26'
  confidence: high
  verified: true
- source: http://rdi.cssn.cn/dcsj/ (调查数据 column, fetched+read 2026-08-15)
  field_scope:
  - data column exists
  - release notes and use notes listed
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://rdi.cssn.cn/dcsj/202504/t20250429_5871894.shtml (关于公布第二期中国乡村振兴综合调查数据的说明（试行）, fetched+read 2026-08-15)
  field_scope:
  - biennial tracking design; three waves completed
  - baseline 2020: 10 provinces, 50 counties, 150 townships, 300 villages, 300 village + 3,700+ household questionnaires, 15,000+ members
  - 2022 wave: village tracking 100%, household 81%
  - 2024 third wave: +4 provinces (Liaoning, Shanxi, Hunan, Inner Mongolia), 472 village + 5,800+ household questionnaires, 23,000+ members
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://rdi.cssn.cn/dcsj/202306/t20230607_5643271.shtml (中国乡村振兴综合调查数据使用说明, fetched+read 2026-08-15)
  field_scope:
  - application procedure (form + confidentiality agreement + ID scan, email, ~1 week review)
  - questionnaire attachments
  added: '2026-08-15'
  confidence: high
  verified: true
- source: http://rdi.cssn.cn/ (home, prior-run cache 200 + news; fourth-wave prep news 2026-07)
  field_scope:
  - fourth wave in preparation (2026-07 news)
  added: '2026-08-15'
  confidence: med
  verified: false
- source: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0316899&type=printable (publisher full text, read 2026-09-28)
  field_scope:
  - actual 2020 CRRS use in Li & Gao (2025)
  - linked village-committee and villager-questionnaire use and paper-specific analytic counts
  - examples of 2020 variables used in the article
  - institutional application, RDI-page, form, email and one-week response boundary stated in the data-availability statement
  - distinction between CRRS delivery and the authors' cleaned/matched analysis file
  added: '2026-09-28'
  confidence: high
  verified: true

related_datasets:
- id: cfps
  relation: complement
- id: chip
  relation: complement
- id: china-stat-yearbook
  relation: complement
---

## Positioning in one sentence

CRRS is CASS RDI's rural tracking survey of villages, households and members. The current documented route is approved domestic cloud use of the 2020/2022 waves, with reviewed result exports rather than raw-data downloads; a public article verifies a linked village-villager 2020 use case. Later fieldwork expanded coverage but does not itself establish another released wave.

## Select rules

- Prioritize CRRS for released 2020/2022 rural household/village research when the linked design fits and controlled domestic cloud use is feasible.
- Switch to cfps/chip for nationally representative, longer-history household panels; CRRS is rural-only and young.
- Not for urban samples or pre-2020 history.

## Get recipe

1. Read the [official second-wave instructions](http://rdi.cssn.cn/dcsj/202504/t20250429_5871894.shtml), which supersede the older email procedure. Follow the provider's platform link and manual; ask the listed project contact about an unavailable service or certificate rather than bypassing warnings.
2. Domestic applicants complete identity/institution review and await cloud-account allocation, potentially by the monthly lottery, then submit the requested research plan.
3. Analyze the 2020/2022 waves in the cloud. Research results require administrator review before email export; the instructions do not offer downloadable raw microdata. No identity documents or application were submitted in this review.

## Connections and Limitations

Village-household-member linkage is designed within waves and across waves (tracking). The published 2020 example verifies a village-variable to villager-record match, but its cleaned 284-village/7,451-person sample is not itself the delivered dataset. County-level geography should be normalized before joining external data. One unresolved discrepancy between the 2022 and 2025 official notes on baseline village counts is retained. Confirm the target wave's currently distributable files on the official column before relying on a specific wave.

## Decision sufficiency check

A domestic researcher can assess the 2020/2022 linked village-household product and begin the documented cloud application, allowing for eligibility, capacity and result-export review. A design requiring unrestricted local microdata or overseas access cannot assume this route will work. Within approved access, inspect questionnaires, identifiers, weights and geography before an external merge; the paper's cleaned matched sample is not a released CRRS file.
