---
schema_version: 2
catalog_status: ready
id: cgss
name: China General Social Survey (CGSS)
aka:
- CGSS
- 中国综合社会调查
- China General Social Survey
- 中国社会综合调查
- 人大CGSS
provider: National Survey Research Center at Renmin University of China (NSRC, National Survey Research Center at Renmin University
  of China)
china_related: true
domains:
- sociology
- public
- labor
- health
- governance
- development
- demography
unit_of_observation: Individuals (Adults 18+) - Years (repeated cross-section, non-trace panel)
structure: repeated-cross-section
geo_granularity:
- personal
- village/community
- County
- city
- province
geography: All 31 provinces/municipalities/autonomous regions in mainland China (including urban and rural areas)
time_span:
  start: 2003
  end: ongoing
  last_confirmed_release: 2021
  coverage_note: More than 13 rounds from 2003 to 2021 have been confirmed; the questionnaire module and opening progress
    are irregular
  last_checked: '2026-07-10'
frequency:
- annual-or-biennial
sample_size: Approximately 10,000–12,000 respondents (18+) per round
key_variables:
- Social attitudes (happiness/sense of fairness/trust/political attitudes/values)
- Social class and mobility (subjective status/objective income/education/occupation)
- Labor market (employment/income/working hours/occupation)
- Education and training
- Health (self-evaluation/mental health)
- Family and Marriage (Marriage/Maternity/Residential Arrangements)
- Social participation (political participation/social organizations/voluntary activities)
- Urban-rural gap (hukou/urban-rural residence)
- environmental attitude
- Internet use and media exposure
research_fit:
  best_for:
  - Nationally replicated cross-section of adult social attitudes, trust in government, sense of fairness, subjective class,
    and values
  choose_over:
  - Prioritize CGSS over CFPS/CHFS when nationally repeated cross-sections of adult attitudes and values are the primary outcome
  - When you need to track causal changes for the same person or family, give priority to panels such as CFPS/CHARLS.
  not_good_for:
  - personal tracking
  - children teenagers
  - corporate research
  - Not checking for long-term trends in continuity of questionnaires across waves
  needs_join_for:
  - Policy and regional macro variables need to be joined by province/city/county and year; fine geographical codes may be
    limited
  variation_available:
  - Multiple rounds of repeated sections
  - Age-Period-Cohort Differences
  - Regional policy differences
good_for:
- Changes in social attitudes and values—the changing trends and determinants of the Chinese public’s sense of happiness,
  fairness, and trust
- Social stratification and intergenerational mobility - the relationship between subjective class identity and objective
  income/education/occupational status
- Urban-rural gap - the continuing impact of the household registration system on income, education, and political participation
  (repeated cross-section covers 20 years of changes)
- Political Attitudes and Government Trust - The Chinese public’s trust in governments/institutions at all levels and its
  relationship with public policies
- Environmental awareness – public attitudes towards pollution, climate change and determinants of pro-environmental behavior
- The Internet and Social Change—The Impact of Digital Divide and Social Media Use on Political Participation and Social Trust
identification:
- OLS/Logit (section)
- Age-period-cohort (APC) decomposition
- DID (policy/regional differences - using repeated sections to make composite panels)
- IV (regional/policy exogenous shocks)
linkable_keys:
- Provincial code
- City code
- County code (authorization required)
- Can be joined with macro data at the regional level
access_routes:
- route: RUC CSSD CGSS data space
  access_status: available-with-application
  direct_url: https://cssd.ruc.edu.cn/dataspace/cgss
  requirements: Register on CSSD, complete real-name verification and the data-use agreement. Public files and restricted files have different permissions; restricted files require approval.
  steps:
  - Start at the CGSS data space linked through RUC's official CSSD launch announcement.
  - Register and complete the platform's identity and agreement steps; select the required wave and questionnaire.
  - Download public files under the platform's conditions; apply separately for restricted files rather than assuming all waves or fields are covered.
  deliverable: Wave-specific public data and questionnaire files. The visible catalog includes CGSS2018 and CGSS2021 data labelled SPSS and Stata 14+, with PDF questionnaires; catalog .tab names are not a verified downloaded archive format.
  cost: free
  last_checked: '2026-10-26'
  caveat: The legacy CNSDA endpoint http://cnsda.ruc.edu.cn/ failed DNS in GitHub Actions and returned an empty response in the browser on this date. Use the officially linked CSSD route; this check did not create an account or download microdata.
access:
  url: https://cssd.ruc.edu.cn/dataspace/cgss
  cost: free
  license: Academic research only, registration + signing of agreement required
  format:
  - dta
  - csv
  - sav(SPSS)
  api: false
  how_to_get: Open the RUC CSSD CGSS data space, register and complete real-name verification and the data-use agreement, then select the wave. Public files are downloadable under those conditions; restricted files require an additional application and approval. The current route is not the legacy CNSDA endpoint.
caveats: CGSS is a repeated cross-section rather than a panel - different samples are interviewed in each round and cannot
  track changes in the same person. The questionnaire was revised on a large scale after 2010, and some variables were discontinued
  across rounds. Some sensitive topics (such as politically sensitive issues) may be removed to comply with censorship requirements.
  The representativeness of rural samples was weak in the early stage.
quality:
  profile_status: verified
  access_status: verified
  paper_use_status: verified
  last_audited: '2026-07-10'
used_by:
- cite: 'Wang, Zhou & Wan (2025), The Impact of Robots on Unemployment Duration: Evidence from the Chinese General Social
    Survey'
  journal: CER
  year: 2025
  dataset_role: Labor unemployment duration results; joined with robot exposure
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v89y2025ics1043951x24001949.html
  data_note: Use CGSS data to study the impact of industrial robot penetration on the duration of worker unemployment—low-skilled
    workers are more affected
- cite: 'Yang & Zhang (2024), Social Capital Meets Guanxi: Social Networks and Income Inequality in China'
  journal: CER
  year: 2024
  dataset_role: Social networks, social capital, and income outcomes
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v83y2024ics1043951x23001797.html
  data_note: Use the social network and social capital variables of CGSS to study the impact of 'guanxi' (guanxi) on income
    inequality - social networks strengthen the intergenerational transmission of income advantages
- cite: 'Mu (2022), Perceived Relative Income, Fairness, and the Role of Government: Evidence from a Randomized Survey Experiment
    in China'
  journal: CER
  year: 2022
  dataset_role: Sense of fairness, relative income and government role attitudes; survey experimental results
  evidence_type: abstract
  evidence_url: https://ideas.repec.org/a/eee/chieco/v73y2022ics1043951x22000426.html
  data_note: Using CGSS data + randomized experimental methods, we study the impact of subjective relative income on fairness
    perceptions and government redistribution preferences.
- cite: 'Jiang & Yin (2025), Delinking Social Identity From Rural-Urban Stereotypes: The Labor Market Effects of Abolishing Agricultural Hukou in China'
  doi: https://doi.org/10.1111/jors.70032
  journal: JRS
  year: 2025
  dataset_role: CGSS nationally representative survey data — rural stayer and migrant labor market outcomes
  evidence_type: data-section
  evidence_url: https://onlinelibrary.wiley.com/doi/10.1111/jors.70032
  data_note: Uses CGSS repeated cross-sections combined with CFPS for validation in a staggered DiD across 89 cities where agricultural hukou was abolished (2010-2015). Finds ~17% annual earnings increase for rural stayers, no income gains for rural-urban migrants, and higher nonemployment risk for urban incumbents. CGSS provides broad social attitudes and labor market measures complementing CFPS income data.
- cite: 'Chen Chen (2025), Long-Run Impacts of Fertility Restriction Policy on China''s Gender Gap in Career Advancement'
  doi: https://doi.org/10.1016/j.labeco.2025.102782
  journal: Labour Economics
  year: 2025
  dataset_role: CGSS 12 waves (2003-2021); repeated cross-section for career advancement and gender gap outcomes
  evidence_type: data-section
  evidence_url: https://www.sciencedirect.com/science/article/abs/pii/S092753712500106X
  data_note: >-
    Uses CGSS 12 waves (2003-2021) as the primary individual-level data source, combined with Census-based provincial fertility data. Cohort triple-difference (DDD) exploiting staggered provincial implementation of China's "Later, Longer, Fewer" (LLF) campaign in the 1970s. Finds LLF reduced the gender gap in managerial positions by ~20% and administrative rank by ~18%. Mechanism — women pursued more college education, increased labor input, and relied less on offspring for old-age support. Effects stronger in state sector (~25%) and non-white-collar, non-female-dominated industries.
provenance:
- source: http://cgss.ruc.edu.cn/info/1014/1041.htm (official CSSD launch announcement, 2026-08-27) and https://cssd.ruc.edu.cn/dataspace/cgss (browser-read 2026-10-26)
  field_scope:
  - Official platform link and registration, real-name verification, agreement and file-specific approval conditions
  - Visible CGSS2018/2021 catalog entries, format labels and questionnaires; no authenticated microdata delivery tested
  - Replacement of the current acquisition start, not a change to survey identity, paper-use evidence or release coverage
  added: '2026-10-26'
  confidence: high
  verified: true
- source: CGSS official site http://cgss.ruc.edu.cn and CNSDA platform http://cnsda.ruc.edu.cn (supports survey design, waves, variable coverage, and access conditions)
  added: '2026-07-08'
  confidence: high
  verified: true
related_datasets:
- cfps
- chns
- charls
---

## Positioning in one sentence
CGSS is China’s longest-running comprehensive social attitude survey with the widest coverage—approximately 12,000 people per year since 2003,
Covering "soft" variables such as social attitudes, class, political participation, and values,
It is the core data source for studying **China's social changes, public attitudes and values**.
Unlike CFPS/CHARLS which is biased towards economic variables (income/health/cognition), the unique value of CGSS is
"What people think about society" - happiness, fairness, trust, political attitudes, etc.

## Research questions suitable for answering/Typical identification strategies
- **"What do the Chinese public think of
- **Social stratification and subjective class identity**: How does objective income/education map to subjective class identity? Is there an expanding trend in "middle-class anxiety" or "lower-class identification"?
- **Political Economy of Government Trust**: Differences in trust levels at different levels of government (central/provincial/city/county) and their relationship with the quality of public services.
- **Not suitable for use**: Research that requires individual panels to track causal effects (CGSS is a repeated cross-section, not a panel), child/adolescent issues (only 18+), enterprise/industry level research.
- **Causal identification techniques for repeated cross-sections**: Multiple rounds of CGSS can be combined into a "synthetic panel" by province/city/year, and DID can be used to estimate the impact of provincial policy changes on public attitudes.

## Key variables/modules
- **Core attitude module**: happiness, life satisfaction, social justice, interpersonal trust, government trust (levels)
- **Class and Mobility Module**: Subjective socioeconomic status, parental education/occupation, personal education/income/occupation
- **Political Participation Module**: voting, community participation, social organizations, petitioning
- **Labor force module**: Employment status (employer/employee/self-employed/farmer), income, working hours, occupation
- **Health Module**: Self-assessed health, mental health (short version of GHQ)
- **Internet module** (newly added in recent years): Internet frequency, social media use, information sources

## How to get
1. Open the [official CSSD CGSS data space](https://cssd.ruc.edu.cn/dataspace/cgss), register and complete real-name verification and the data-use agreement.
2. Select the wave and its questionnaire. The catalog distinguishes public files from files requiring separate approval; public-file access is not a grant to every restricted field.
3. Download the permitted files and inspect the supplied format, questionnaire and identifiers. The browser check confirmed the catalog and instructions, not an authenticated download. The old CNSDA URL is retained in provenance as a historical route, not the recommended starting point.

## Connections to other data
- **CFPS/CHARLS**: The core variables of the CGSS covering attitudes and values are the weaknesses of the CFPS/CHARLS - the two complement each other. "Province/Year" can be used for cross-validation at the macro level.
- **Statistical Yearbook**: Use "province code/year" to connect provincial GDP/finance/public services and other indicators to construct policy impact variables.
- **and CHNS/CHFS**: both are large-scale social surveys and can be cross-validated on common variables such as income and education.

## Remarks / Pitfalls
- **Not the panel! ** This is the most fundamental difference between CGSS and CFPS/CHARLS - resampling is done in each round and individual changes cannot be tracked. When making causal inferences, a composite panel method or identification limited to the regional level is required.
- **Major changes to the questionnaire in 2010**: After 2010, the CGSS was connected with the ISSP (International Social Survey Project), and the questionnaire structure was significantly adjusted - the inter-temporal comparison before/after 2010 needs to check the continuity variable by variable.
- **Review of Sensitive Issues**: Politically sensitive issues may be removed or have their wording changed in some years, so please pay attention when doing time series analysis.
