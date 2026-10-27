---
schema_version: 3
catalog_status: ready
id: ceps
name: China Education Panel Survey (CEPS)
aka:
- CEPS
- 中国教育追踪调查
- China Education Panel Survey
provider: National Survey Research Center (NSRC), Renmin University of China
china_related: true
domains:
- education
- labor
- development
- public
- migration
- urban-rural
data_pathway:
  mode: direct
  origin: ready-made
  target_artifact: Separate student, parent, teacher and principal files for the national 2013-2014 baseline and 2014-2015 follow-up, plus a distinct 2012 pilot data file and questionnaires. The pilot is not a third national-panel wave.
  availability: partially-reproducible
  ordinary_researcher_feasible: true
  summary: >-
    RUC's CSSD CEPS public space catalogs three releases: the 2012 pilot,
    the 2013-2014 national baseline and the 2014-2015 follow-up. Their file
    lists and public labels are visible without login. The separately
    listed restricted-data space names later follow-ups and sub-provincial
    geography but exposes no file inventory in the unauthenticated view.
    CNSDA remains a dated official archive source; the PKU 2014 baseline
    mirror is a separate deposit, not an equivalent all-wave or all-respondent release.
  barrier: CSSD's launch instructions require real-name verification and the data-use agreement for public downloads, with separate approval for restricted files. Catalog visibility and public labels do not establish this reviewer's download authorization. Finer geography and later waves must not inherit the public releases' permissions.
  last_checked: '2026-10-27'

unit_of_observation: Student-year, parent-year, teacher-year, school-administrator-year, with class and school context files
structure: Longitudinal school-based panel with multiple respondent types
geo_granularity:
- student
- family
- class
- school
- county/district (sample PSU; exact public identifiers require checking the release)
geography: National mainland China sample drawn from 28 county-level units (counties, districts, or county-level cities), 112 schools, and 438 classes at baseline
time_span:
  start: 2013-09
  end: 2015-07
  last_confirmed_release: 2015
  coverage_note: These start/end dates describe the confirmed public national panel, 2013-2014 baseline and 2014-2015 follow-up. CSSD's third public release is a separate 2012 pilot, not another post-2015 panel wave. The restricted-data space names 2015-2016, 2017, 2019 and 2024 follow-ups, but their files and granted access were not verified. CSSD's 2026 publication/version dates are platform-release dates, not survey years.
  last_checked: '2026-10-27'
frequency:
- annual follow-up
sample_size: Baseline approximately 19,487 students in 438 classrooms and 112 schools; the CNSDA 2014-2015 release lists 10,750 student and parent records, 791 teacher records, and 304 school-administrator records for that release. Separately, CSSD's 2012 pilot file metadata reports 2,330 observations and 625 variables; this is not the national baseline sample or proof of cross-wave linkage.
key_variables:
- Student cognitive and noncognitive assessments
- Student demographics, family background, hukou and migration-related measures
- Parent education, occupation, household resources, and parent-child relationships
- Class composition, friendship and peer relationships, teacher-student interaction, and school context
- Teacher characteristics, evaluations, workload and attitudes
- School facilities, enrollment, staffing and administration

research_fit:
  best_for:
  - Peer composition, classroom interaction, school resources, and adolescent human-capital outcomes
  - Urban-rural, migrant-status, and local school-context comparisons when the approved geography and weights support them
  - Linking individual education outcomes to school, class, and county/district context rather than treating the survey as a county economic panel
  choose_over:
  - Prefer CEPS over a general household survey when the question needs students, parents, teachers, classmates, and school administrators observed around the same classrooms.
  - Prefer CFPS or CHFS when the question needs broader household or financial coverage, annual local economic outcomes, or a longer adult panel.
  not_good_for:
  - A dense city-year or county-year economic panel; only 28 county-level sample units are selected at baseline.
  - National administrative school outcomes, complete school rosters, or unrestricted fine-grained spatial exposure.
  - Treating classroom-derived peer shares as a ready-made national statistic; those variables must be reconstructed from respondent files and paper-specific inclusion rules.
  needs_join_for:
  - Local labor markets, housing, weather, land, or policy exposure require a separately sourced geography-year dataset and an approved, stable CEPS geography key.
  - Cross-wave comparisons require the survey's identifier and attrition documentation; do not assume every respondent file is a balanced panel.
  variation_available:
  - Classroom peer composition and school-context differences observed in the survey
  - Urban-rural and migrant-status heterogeneity in education and family outcomes
  topics:
  - education
  - peer effects
  - school quality
  - human capital
  - urban-rural inequality
  - migrant children
  - social capital
  - local public services

good_for:
- School and classroom peer effects
- Student cognitive and noncognitive development
- Family, school, and community channels of education inequality
- Urban-rural and migrant-background comparisons in lower-secondary education
identification:
- Multilevel or fixed-effects comparisons within school/class context
- Paper-specific random classroom assignment or peer-composition designs where assignment and sample restrictions are documented
- Panel comparisons across the confirmed baseline and follow-up waves
linkable_keys:
- Respondent identifiers within each wave and respondent type
- Student-parent, student-teacher, class, and school identifiers where supplied
- Wave/cohort and documented county/district identifiers when approved

joins:
  - target: cfps
    relation: complement
    keys:
    - Age/cohort and documented region, with no assumption of person-level matching
    - Survey year and urban-rural or hukou definitions
    method: Use CEPS for school and peer context and CFPS for broader household or adult outcomes; compare harmonized definitions rather than attempting individual linkage.
    evidence_status: plausible
  - target: china-stat-yearbook
    relation: complement
    keys:
    - Approved county/district code or documented sample-PSU crosswalk
    - Reference year
    method: Add province/city or other public local context only after verifying that the released CEPS geography key is stable and permitted. The official CEPS pages establish the 28-PSU design but do not release a universal public crosswalk in the checked materials; a coarser join may be the only lawful option.
    evidence_status: plausible

access_routes:
  - route: RUC CSSD CEPS public data space (current primary route)
    access_status: available-with-registration-and-terms
    direct_url: https://cssd.ruc.edu.cn/dataspace/ceps1
    requirements: Follow CSSD's registration, real-name verification, public-license/data-use agreement and citation conditions; select the exact release and language.
    steps:
    - Start at the official CEPS data space https://cssd.ruc.edu.cn/dataspace/ceps and choose its public-data subspace.
    - Select the 2012 pilot, national baseline or first follow-up as a distinct release; inspect the file list and documentation before requesting downloads.
    - Complete the platform's identity and agreement steps. Obtain only files permitted for the account; a public label does not grant restricted geography or later-wave access.
    - Read the user manual, sampling and cross-wave documentation, then verify identifiers and the delivered formats before constructing a panel.
    deliverable: Cataloged public files comprise the pilot ceps2012.dta with 14 questionnaire documents; baseline cepsw1{parent,principal,student,teacher}{CN,EN}.dta with 19 documents; and follow-up cepsw2{parent,principal,student,teacher}{CN,EN}.dta with 13 documents, including the two-wave variable crosswalk. These are observed file labels, not downloaded and inspected deliveries.
    cost: registration
    last_checked: '2026-10-27'
    caveat: The unauthenticated catalog lists all 63 files as public. File detail and search surfaces can use .dta and ingested .tab labels for the same named product; verify the actual export. No account, identity submission, license acceptance, preview behind acceptance, or microdata download was performed in this review.
  - route: RUC CSSD CEPS restricted-data information
    access_status: needs-verification
    direct_url: https://cssd.ruc.edu.cn/dataspace/ceps2
    requirements: The platform requires a separate application and approval for restricted data; CEPS-specific eligibility, file permissions and actual delivery are not established by the public description.
    steps:
    - Read the restricted-data description and identify the exact year or sub-provincial geography needed.
    - Consult the current CSSD application instructions and the CEPS contact linked from its parent space (nsrc@ruc.edu.cn) to establish the target product, eligibility and review procedure.
    - Apply through the provider's authorized process only once those conditions are known; do not plan a later-wave panel or spatial merge on the public listing alone.
    deliverable: The public description names sub-provincial geographic information and follow-ups labelled 2015-2016 school year, 2017, 2019 and 2024. No file names, respondent inventories or approved delivery were verified for this route.
    cost: by-application
    last_checked: '2026-10-27'
    caveat: The unauthenticated restricted subspace returned zero search results while displaying its product description. This does not prove that restricted files are absent, visible after login, generally approved or downloadable; those alternatives remain unresolved.
  - route: CNSDA official CEPS catalog
    access_status: available-with-login
    direct_url: https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
    requirements: Free registration/login; follow the catalog's data-use and citation terms.
    steps:
    - Register or log in to CNSDA.
    - Open the CEPS 2014-2015 follow-up project and read the data-use notes and documentation.
    - Download the permitted questionnaire, codebook, and respondent files; record the exact release and language before analysis.
    deliverable: CNSDA lists Chinese and English questionnaires, a data-use manual, a two-wave variable crosswalk, and Stata respondent files for students, parents, teachers, and school administrators.
    cost: free
    last_checked: '2026-09-27'
    caveat: Historical official archive observation from 2026-09-27, not newly revalidated here. Its notice says it will no longer add data, retains daily maintenance and directs additional-data requests to the newer RUC platform. Use CSSD as the current primary start; do not conflate CNSDA's inventory or permissions with CSSD's.
  - route: RUC CEPS project documentation
    access_status: documentation-only
    direct_url: https://ceps.ruc.edu.cn/xmjs/xmgk.htm
    requirements: Use the project documentation to confirm design and current release links.
    steps:
    - Read the project overview and sampling documentation.
    - Follow the current data-release instructions to the authorized archive.
    deliverable: Survey design, baseline scope, questionnaires, and release notices.
    cost: free
    last_checked: '2026-08-12'
    caveat: The producer documentation is not proof of microdata download rights. The supplied official launch-announcement URL https://ceps.ruc.edu.cn/info/1006/1058.htm failed browser certificate-authority validation on 2026-10-27; no warning was bypassed. The CSSD platform's own announcement and catalogs were independently readable.
  - route: PKU Open Research Data Platform 2014 baseline mirror
    access_status: available-with-login
    direct_url: https://doi.org/10.18170/DVN/KURJUU
    requirements: Dataverse account/login; cite the deposit and inspect its file-level metadata.
    steps:
    - Open the DOI deposit and review version, file list, and terms.
    - Download the questionnaire and files labelled as 2014 CEPS baseline data.
    - Treat the deposit as a mirror/subset unless it is independently shown to equal the official release.
    deliverable: The checked deposit lists a student questionnaire, SPSS student file, and a processed tabular student file; it does not establish complete multi-respondent or unrestricted geographic coverage.
    cost: free
    last_checked: '2026-08-12'
    caveat: This is a public research-data deposit by a named depositor, not proof that all official CEPS waves, identifiers, weights, or geographies are present.

access:
  url: https://cssd.ruc.edu.cn/dataspace/ceps1
  cost: registration
  license: CSSD platform public license/data-use agreement and attribution for public files; restricted files require separate approval. Historical CNSDA and PKU deposits retain their own terms and identities.
  format:
  - dta
  - sav
  - pdf
  - xlsx
  - xls
  - doc
  - tab (platform-ingested labels; actual download/export not tested)
  api: false
  how_to_get: Start at the CSSD CEPS public space, select the distinct pilot, baseline or 2014-2015 follow-up, and complete the platform's registration, real-name and agreement requirements before obtaining permitted files. Later-wave and finer-geography requests are separate restricted applications, not an extension of public access. Read the manual and cross-wave table before joining respondent files; cite CNSDA history and the PKU baseline mirror separately.
caveats: CEPS is school-based rather than a general local-economy panel. The baseline design is nationally representative at its stated sampling level, but the 28 county-level PSUs are not a census of Chinese counties. Student, parent, teacher and administrator files have different units and identifiers. A paper's classroom-level peer share, civil-servant-family indicator, or other constructed measure is a derived variable, not a raw CEPS field. Fine geography, weights, attrition, and the availability of later waves must be checked in the exact release used.

quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-09-27'

used_by:
  - cite: 'Li & Wu (2026), Parental Social Capital Spillovers in Children''s Noncognitive Skills Formation: Evidence from Random Classroom Assignment in China'
    doi: https://doi.org/10.1016/j.chieco.2026.102748
    journal: CER
    year: 2026
    dataset_role: Main student, family, class, teacher and school-context evidence for peer-parent social-capital spillovers
    evidence_type: publisher_page_and_crossref
    evidence_url: https://www.sciencedirect.com/science/article/pii/S1043951X26000982
    data_note: The publisher page identifies the 2013-2014 CEPS baseline and its random classroom-assignment setting. The paper studies class exposure to children of civil-servant families, noncognitive skills, friendship networks and teacher-student relationships. The paper use supports the baseline CEPS role; it does not imply that its classroom-derived exposure variable or analysis file is a separate downloadable dataset.

provenance:
  - source: CSSD launch announcement https://cssd.ruc.edu.cn/news/11 and official CEPS spaces https://cssd.ruc.edu.cn/dataspace/ceps, https://cssd.ruc.edu.cn/dataspace/ceps1 and https://cssd.ruc.edu.cn/dataspace/ceps2 (browser-read 2026-10-27)
    field_scope:
    - Public-release count resolved to the 2012 pilot and two national-panel school-year releases, not a third post-2015 public wave
    - Current official acquisition start, general real-name/agreement conditions and separate restricted-data approval
    - Later-year/geography description only; restricted space showed no unauthenticated file inventory
    added: '2026-10-27'
    confidence: high
    verified: true
  - source: CSSD pilot https://cssd.ruc.edu.cn/dataset/143?versionNo=1.0, baseline https://cssd.ruc.edu.cn/dataset/144?versionNo=1.0, follow-up https://cssd.ruc.edu.cn/dataset/145?versionNo=1.1 and pilot file https://cssd.ruc.edu.cn/file/149?datasetVersionId=50 (browser-read 2026-10-27)
    field_scope:
    - Exact public file inventories and permission labels at the listed versions; follow-up includes two-wave variable crosswalk
    - Pilot file metadata reports 2330 observations and 625 variables, distinct from national-panel sample claims
    - Public-license acceptance gate observed, not accepted; no authenticated download or restricted-file inspection
    added: '2026-10-27'
    confidence: high
    verified: true
  - source: RUC CEPS project overview https://ceps.ruc.edu.cn/xmjs/xmgk.htm
    field_scope:
    - producer
    - baseline design
    - national scope
    - project identity
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: CNSDA CEPS 2014-2015 catalog https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
    field_scope:
    - follow-up wave
    - respondent files
    - variable counts
    - sample counts
    - access route
    - questionnaires and documentation
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: Current CNSDA CEPS 2014-2015 catalog recheck https://www.cnsda.org/index.php?id=61662993&r=projects%2Fview
    field_scope:
    - current catalog availability and registration entry point
    - 28-PSU, 112-school, 438-class sampling description
    - current 20-item catalog inventory, including questionnaires, manual, cross-wave table, and four respondent-file types
    - notice that additional-data requests are directed to RUC's newer social-science data platform
    added: '2026-09-27'
    confidence: high
    verified: true
  - source: PKU Open Research Data Platform deposit https://doi.org/10.18170/DVN/KURJUU
    field_scope:
    - public baseline mirror
    - file formats
    - deposit metadata
    - file-level terms
    added: '2026-08-12'
    confidence: high
    verified: true
  - source: China Economic Review article page https://www.sciencedirect.com/science/article/pii/S1043951X26000982 and Crossref DOI metadata https://doi.org/10.1016/j.chieco.2026.102748
    field_scope:
    - Li and Wu authorship
    - 2026 publication
    - actual CEPS baseline use
    - classroom and outcome roles
    added: '2026-08-12'
    confidence: high
    verified: true

related_datasets:
  - id: cfps
    relation: complement
  - id: cgss
    relation: complement
---

## Positioning in one sentence

CEPS is a nationally sampled, school-based longitudinal survey that places students, parents, teachers, and school administrators around the same lower-secondary classrooms. It is especially useful when a research question needs peer composition and school context together; it is not a substitute for a dense county-year economic panel, and the public route must be distinguished from each paper's derived classroom file.

## Select rules

- Prioritize CEPS when the outcome is adolescent learning or noncognitive development and the mechanism runs through classmates, families, teachers, or school resources.
- Use the official CSSD public-data space as the current primary route. Its three releases include the separate 2012 pilot, not a third national-panel wave. Retain CNSDA as historical official archive evidence and the PKU DOI deposit as a separately cited baseline mirror. Check the exact wave, file language, weights, attrition documentation, and geography fields before constructing a panel.
- Switch to CFPS or CHFS when the question needs broad household, adult, asset, labor-market, or annual local-economic coverage. Do not infer a county-level policy effect merely because CEPS sampled counties.

## Get recipe

1. Start at the [official CSSD CEPS public space](https://cssd.ruc.edu.cn/dataspace/ceps1), select the intended release, and follow registration, real-name verification and agreement requirements. The three public datasets are identified below.
2. Read the data-use manual and two-wave variable crosswalk before downloading respondent files. Public labels establish catalog permissions, not approval already granted to this reviewer or unrestricted local geography.
3. Download only the permitted student, parent, teacher, and administrator files for the target wave, preserving their original file names and identifiers.
4. Build classroom or peer variables from the respondent files only after documenting inclusion rules. A paper's cleaned peer share is a constructed analysis variable, not an official CEPS download.
5. For local joins, confirm the approved county/district key and the reference year; if fine geography is absent, use a documented coarser match or stop.

### What the three public releases actually contain

The unauthenticated CSSD file lists, checked on 2026-10-27, identify these releases. All listed files carry the public-file marker; actual downloads and license acceptance were not performed.

| Official release | Visible data products | Accompanying files and identity boundary |
| --- | --- | --- |
| [2012 pilot, v1.0](https://cssd.ruc.edu.cn/dataset/143?versionNo=1.0) | One file labelled `ceps2012.dta`; its metadata reports 2,330 observations and 625 variables. | 14 student, parent and teacher questionnaire documents. Separate pilot, not a third observation of the national baseline students; the catalog does not establish linkage to the later panel. |
| [2013-2014 national baseline, v1.0](https://cssd.ruc.edu.cn/dataset/144?versionNo=1.0) | Eight Stata-labelled files: `cepsw1parent`, `cepsw1principal`, `cepsw1student`, `cepsw1teacher`, each in `CN` and `EN` versions. | 19 documents covering questionnaires, user manuals, sampling, fieldwork and the cognitive-test report. These respondent products are not interchangeable with a student-only mirror. |
| [2014-2015 follow-up, v1.1](https://cssd.ruc.edu.cn/dataset/145?versionNo=1.1) | Eight Stata-labelled files with the same four respondent stems under `cepsw2`, each in `CN` and `EN` versions. | 13 documents, including `两轮调查变量对照表.xls`, the usage/fieldwork manuals and questionnaires. This is the confirmed public follow-up, not proof of another open national-panel wave. |

The [separate restricted-data space](https://cssd.ruc.edu.cn/dataspace/ceps2) describes sub-provincial geography and follow-ups labelled 2015-2016, 2017, 2019 and 2024. Its unauthenticated view lists no files. Establish the exact respondent products and application conditions with CSSD/CEPS before relying on those years; neither the three-release announcement nor a login page establishes their availability to a particular researcher. The public national-panel dates and `last_confirmed_release: 2015` therefore remain unchanged. CSSD's 2026 version timestamps do not extend the survey's observation period.

## Connections and Limitations

The survey's strength is its nested school/class/respondent structure. The practical risk is assuming that a student file alone contains the parent, teacher, school, weights, or geography components needed for a paper. The 28 baseline PSUs support national survey inference at the design's stated level but do not support arbitrary county rankings. The 2014-2015 CNSDA release and the PKU baseline mirror have different samples and file inventories; never merge them without checking identifiers and attrition.

## Decision sufficiency check

For a question about how classmates' family background affects student outcomes, choose the national CEPS baseline/follow-up, start at CSSD for the relevant student/parent/teacher/principal files, reconstruct the classroom measure, and treat any local policy or weather variable as a separately sourced join. Do not add the 2012 pilot as another follow-up or assume that an application mention grants post-2015 data. For a question about annual city housing prices or county economic growth, choose CHFS/CFPS or an official local panel instead. The existing `ready` status remains a judgment about the documented public releases and lawful acquisition start, not account approval, unrestricted geography or paper-file reproducibility.
