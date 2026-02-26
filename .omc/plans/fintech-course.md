# Work Plan: MSc Fintech Course Generation

## Context

### Original Request
Generate a complete MSc-level Fintech course using the course-creator skill system. The course spans 5 days (20 hours total) with 7 lectures of approximately 2h15m each (~15h45m total lecture time), targeting Finance/Business MSc students with strong finance backgrounds but limited technical/coding skills.

### Interview Summary
- **Format:** 5 days x 4 hours = 20 hours total
- **Lectures:** 7 lectures of ~2h15m each (~15h45m total lecture time)
- **Remaining time:** ~4h15m distributed as hands-on workshops (2h15m), final review (45m), and breaks (1h15m)
- **Language:** English
- **Assessment:** Quizzes only (standard + advanced per lecture, auto-generated). No project tracks.
- **Chart style:** Conceptual diagrams only (process flows, architecture diagrams, comparison matrices, conceptual models). NO real market data charts.
- **Audience:** Finance/Business MSc students (strong finance, limited coding)
- **Repository:** NEW repo "Fintech" on `digital-ai-finance` GitHub org
- **Stage 6 (projects):** SKIP entirely -- quizzes only

### Research Findings
- Course-creator skill system is fully installed at `~/.claude/skills/omc-learned/course-creator/`
- 7-stage pipeline: slides -> charts -> galleries -> lectures -> quizzes -> (skip projects) -> deploy
- Each lecture produces 6 PDF variants: mini5, mini10, core, overview, deepdive, full
- Quizzes: 20 standard MCQ + 20 advanced MCQ per lecture (Bloom's taxonomy distribution)
- Chart auto-derivation from topic keywords; conceptual-only constraint means no real market data

---

## Work Objectives

### Core Objective
Produce a complete, deployable Fintech course website with 7 lectures, 14 quiz pages (`L{NN}_quiz.html` + `L{NN}_quiz_advanced.html`), 7 gallery pages (`L{NN}_gallery.html`), 7 lecture HTML pages, an index page (no Projects nav), and all supporting PDF/PNG assets, deployed to `https://digital-ai-finance.github.io/Fintech/`.

### Deliverables
1. `course.yaml` manifest file (single source of truth)
2. 42 LaTeX `.tex` files (7 lectures x 6 variants each)
3. ~84 conceptual chart scripts + PDFs (12 per lecture)
4. 42 compiled PDFs (7 lectures x 6 variants)
5. PNG galleries for all PDF variants
6. 7 HTML lecture pages
7. 14 HTML quiz pages (7 standard + 7 advanced)
8. 1 HTML index page
9. GitHub Pages deployment at `digital-ai-finance.github.io/Fintech/`

### Definition of Done
- All 7 stages of the course-creator pipeline complete (Stage 6 skipped)
- Site is live at the GitHub Pages URL
- All navigation links work (no 404s)
- All PDFs downloadable
- All quizzes functional (answer checking works)
- All galleries render thumbnails correctly

---

## Guardrails

### Must Have
- All 7 lectures with complete content
- Conceptual diagrams ONLY (no real market data, no live API calls in chart scripts)
- MSc-level rigor appropriate for finance/business students
- English language throughout
- Bloom's taxonomy distribution in quizzes
- 6 PDF variants per lecture (mini5, mini10, core, overview, deepdive, full)
- Dual-tier quizzes per lecture (standard + advanced)

### Must NOT Have
- Project tracks (Stage 6 skipped entirely)
- Coding exercises or programming assignments
- Real market data charts or live data dependencies
- External CSS files (all inline per course-creator spec)
- LaTeX compilation in CI/CD (all local)
- Content requiring coding skills from students

---

## Day Schedule (5 Days x 4 Hours)

### Day 1: Introduction to Fintech (4 hours)
| Time | Activity | Duration |
|------|----------|----------|
| 09:00-11:15 | **Lecture 1:** Fintech Foundations and Overview | 2h 15min |
| 11:15-11:30 | Break | 15min |
| 11:30-13:00 | **Lecture 2:** Fintech Ecosystem (first half) | 1h 30min |

### Day 2: Ecosystem and Payments (4 hours)
| Time | Activity | Duration |
|------|----------|----------|
| 09:00-10:00 | **Lecture 2:** Fintech Ecosystem (completion) | 1h |
| 10:00-10:15 | Break | 15min |
| 10:15-12:15 | **Lecture 3:** Payments and Fintech | 2h |
| 12:15-13:00 | **Workshop A:** Payment Systems Case Analysis | 45min |

### Day 3: Regulation and Personal Finance (4 hours)
| Time | Activity | Duration |
|------|----------|----------|
| 09:00-11:15 | **Lecture 4:** Fintech Security and Regulation -- RegTech | 2h 15min |
| 11:15-11:30 | Break | 15min |
| 11:30-13:00 | **Lecture 5:** Personal Finance and Wealth Management (first half) | 1h 30min |

### Day 4: Wealth Management and Insurtech (4 hours)
| Time | Activity | Duration |
|------|----------|----------|
| 09:00-10:00 | **Lecture 5:** Personal Finance and Wealth Management (completion) | 1h |
| 10:00-10:15 | Break | 15min |
| 10:15-12:15 | **Lecture 6:** Insurtech | 2h |
| 12:15-13:00 | **Workshop B:** Robo-Advisor Portfolio Construction Exercise | 45min |

### Day 5: Technology and Synthesis (4 hours)
| Time | Activity | Duration |
|------|----------|----------|
| 09:00-11:15 | **Lecture 7:** The Technology of FinTech | 2h 15min |
| 11:15-11:30 | Break | 15min |
| 11:30-12:15 | **Workshop C:** Fintech Startup Evaluation | 45min |
| 12:15-13:00 | **Final Review and Course Wrap-Up** | 45min |

**Total lecture time:** ~15h45m (avg ~2h15m per lecture) | **Total workshop time:** 2h15m | **Final review:** 45m | **Breaks:** 1h15m

---

## Workshop Specifications

### Workshop A: Payment Systems Case Analysis (Day 2, 45 min)
- **Learning Objective:** Students evaluate real-world payment ecosystems by analyzing the cost structures, stakeholder relationships, and regulatory frameworks of different payment methods.
- **Activity:** Teams of 3-4 receive printed case dossiers comparing three payment scenarios: (1) a traditional credit card cross-border transaction, (2) a mobile payment (M-Pesa or WeChat Pay), and (3) a BNPL (Buy Now Pay Later) transaction. Each team maps the stakeholder chain, estimates merchant costs, and identifies regulatory gaps. Teams present findings in a structured 3-minute summary.
- **Materials:** Printed case dossiers (3 per team), worksheet with stakeholder mapping template, cost comparison matrix handout
- **Duration:** 45 minutes (15 min reading + analysis, 20 min team work, 10 min presentations)

### Workshop B: Robo-Advisor Portfolio Construction Exercise (Day 4, 45 min)
- **Learning Objective:** Students apply wealth management principles by designing a model portfolio allocation using a simplified robo-advisor decision framework (no coding required).
- **Activity:** Each student receives a client profile (age, risk tolerance, investment horizon, financial goals) and a menu of 8 asset classes with expected return/risk characteristics. Using a provided decision matrix worksheet, students construct a portfolio allocation, calculate expected portfolio metrics by hand, and justify their choices. A peer review round follows where students critique each other's allocations.
- **Materials:** Client profile cards (4 different profiles), asset class fact sheets, portfolio construction worksheet, expected return/risk lookup table
- **Duration:** 45 minutes (10 min individual work, 15 min portfolio construction, 10 min peer review, 10 min discussion)

### Workshop C: Fintech Startup Evaluation (Day 5, 45 min)
- **Learning Objective:** Students synthesize course concepts by evaluating a fintech startup across multiple dimensions: technology, regulation, market fit, and risk.
- **Activity:** Teams receive a 2-page startup brief for a fictional fintech company (integrating themes from all 7 lectures: payments, regtech, wealth management, insurtech, and underlying technology). Teams use a structured evaluation rubric to score the startup across 6 dimensions: (1) problem-solution fit, (2) regulatory readiness, (3) technology stack soundness, (4) competitive positioning, (5) risk profile, (6) scalability. Teams present a 2-minute investment recommendation (invest / pass / conditional).
- **Materials:** Startup brief handout, evaluation rubric worksheet, scoring guide
- **Duration:** 45 minutes (10 min reading, 20 min team evaluation, 15 min presentations)

---

## Complete `course.yaml` Manifest

The executor MUST create this file verbatim at `D:/Joerg/Research/slides/Fintech/course.yaml`:

```yaml
# === COURSE IDENTITY ===
course:
  name: "Financial Technology (FinTech)"
  short_name: "Fintech"
  institution: "University of Zurich"
  department: "Department of Finance"
  level: "MSc"
  semester: "Spring 2026"
  instructor:
    name: "Joerg Osterrieder"
    email: "joerg.osterrieder@uzh.ch"
  repo:
    org: "digital-ai-finance"
    name: "Fintech"
    visibility: "public"

# === MODULE STRUCTURE ===
modules:
  - id: "foundations"
    name: "Foundations"
    color: "#2CA02C"
    lectures: [1, 2]

  - id: "financial-services"
    name: "Financial Services"
    color: "#FF7F0E"
    lectures: [3, 5]

  - id: "regulation-insurance"
    name: "Regulation and Insurance"
    color: "#D62728"
    lectures: [4, 6]

  - id: "technology"
    name: "Technology"
    color: "#3333B2"
    lectures: [7]

# === LECTURES ===
lectures:
  - number: 1
    title: "Fintech Foundations and Overview"
    subtitle: "Understanding the Revolution in Financial Services"
    topics:
      - "Definitions and evolution of fintech"
      - "The great recession as a catalyst for fintech innovation"
      - "Importance and impact of fintech in the financial industry"
      - "Collaboration vs. competition between traditional financial institutions and fintech"
      - "Key trends and innovations in fintech"
    prerequisites: []
    figures:
      domain_focus: "finance"
      required_types:
        - "time_series"
        - "flowchart"
        - "comparison_bar"

  - number: 2
    title: "Fintech Ecosystem"
    subtitle: "Growth, Social Impact, and Behavioral Dimensions"
    topics:
      - "Fintech growth drivers and economic benefits"
      - "Fintech and social impact: financial inclusion"
      - "Trust in fintech platforms and services"
      - "Risk aversion and fintech adoption barriers"
      - "Choice architecture and nudging in financial products"
    prerequisites: [1]
    figures:
      domain_focus: "finance"
      required_types:
        - "diagram"
        - "concept_illustration"
        - "comparison_bar"

  - number: 3
    title: "Payments and Fintech"
    subtitle: "From Cash to Digital: The Transformation of Money Movement"
    topics:
      - "History of payment methods from barter to digital"
      - "Current global trends in payment methods"
      - "Complexity of the payment process and settlement layers"
      - "Cost burden for merchants across payment types"
      - "International credit card regulation and interchange fees"
      - "Future of payment networks and real-time settlement"
    prerequisites: [1]
    figures:
      domain_focus: "finance"
      required_types:
        - "time_series"
        - "flowchart"
        - "comparison_bar"

  - number: 4
    title: "Fintech Security and Regulation -- RegTech"
    subtitle: "Navigating Compliance in the Digital Finance Era"
    topics:
      - "Perspectives on financial regulation: innovation vs. consumer protection"
      - "Anti-money laundering (AML) and know your customer (KYC) solutions"
      - "US fintech regulatory landscape"
      - "Global fintech regulation: EU, UK, Singapore, and emerging markets"
      - "RegTech: technology-driven regulatory compliance"
      - "Looking forward: regulatory sandboxes and embedded compliance"
    prerequisites: [1, 2]
    figures:
      domain_focus: "finance"
      required_types:
        - "flowchart"
        - "diagram"
        - "comparison_bar"

  - number: 5
    title: "Personal Finance and Wealth Management"
    subtitle: "How Technology Is Democratizing Investment"
    topics:
      - "Robo-advisors and automated investment platforms"
      - "Personal finance management tools and budgeting apps"
      - "Impact of AI and machine learning on wealth management"
      - "Case studies of fintech solutions in wealth management"
      - "Fee structures: traditional vs. robo-advisory"
    prerequisites: [1, 2]
    figures:
      domain_focus: "finance"
      required_types:
        - "comparison_bar"
        - "flowchart"
        - "diagram"

  - number: 6
    title: "Insurtech"
    subtitle: "Technology-Driven Innovation in Insurance"
    topics:
      - "Innovations in insurance through technology"
      - "Digital insurance platforms and distribution models"
      - "Underwriting and claims processing automation"
      - "Case studies of insurtech startups"
      - "Parametric insurance and smart contracts in insurance"
    prerequisites: [1, 2]
    figures:
      domain_focus: "finance"
      required_types:
        - "flowchart"
        - "comparison_bar"
        - "diagram"

  - number: 7
    title: "The Technology of FinTech"
    subtitle: "The Digital Infrastructure Powering Financial Innovation"
    topics:
      - "Identity, privacy, and anonymity in digital finance"
      - "Blockchain and encryption fundamentals"
      - "Big data and analytics in financial services"
      - "AI, decision support systems, and automation"
      - "Smartphones and customer-facing technology"
      - "Cloud computing and API-driven financial services"
    prerequisites: [1, 2, 3, 4, 5, 6]
    figures:
      domain_focus: "finance"
      required_types:
        - "diagram"
        - "flowchart"
        - "concept_illustration"

# === PROJECT TRACKS ===
# INTENTIONALLY EMPTY: This course uses quizzes only, no projects.
projects: []

# === QUIZ CONFIGURATION ===
quizzes:
  standard:
    count: 20
    bloom_distribution:
      understand: 4
      apply: 8
      analyze: 6
      evaluate: 2
  advanced:
    count: 20
    bloom_distribution:
      apply: 4
      analyze: 8
      evaluate: 6
      create: 2

# === VISUAL THEME ===
theme:
  nav_color: "#1a1a4e"
  hero_gradient_start: "#0D7377"
  hero_gradient_end: "#14BDEB"
  accent_color: "#FF7F0E"
  font_family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
```

---

## Per-Lecture Content Outlines

### Lecture 1: Fintech Foundations and Overview

**Title:** Fintech Foundations and Overview
**Subtitle:** Understanding the Revolution in Financial Services

**Sections:**
1. **What Is Fintech?** -- Definitions across academia, industry, and regulators; scope of fintech (payments, lending, insurance, wealth management, capital markets)
2. **Historical Evolution** -- Pre-digital financial innovation; ATMs and electronic trading as early fintech; the internet era and online banking
3. **The Great Recession Catalyst** -- 2008 financial crisis as trust inflection point; regulatory response creating space for startups; consumer demand shift
4. **Importance and Industry Impact** -- Market size and growth trajectory; disruption of traditional banking value chains; new entrants vs. incumbents
5. **Collaboration Models** -- Bank-fintech partnerships; white-label infrastructure; open banking and API ecosystems; acquisition vs. organic development
6. **Key Trends and Innovations** -- Embedded finance; neobanks; decentralized finance overview; super-apps; sustainability-focused fintech

**Suggested Conceptual Diagrams:**
1. **Timeline diagram** -- Evolution of fintech from 1950s (credit cards) through 2020s (DeFi, embedded finance)
2. **Flowchart** -- Traditional banking value chain vs. fintech-disrupted value chain
3. **Comparison matrix** -- Fintech collaboration models: partnership, acquisition, white-label, open banking

**Quiz Focus Areas:**
- Standard: Fintech definitions, historical milestones, impact on traditional banking, collaboration model types, key innovation categories
- Advanced: Evaluate which collaboration model best suits a given scenario; analyze the causal links between the 2008 crisis and fintech growth; synthesize arguments for/against bank-fintech partnerships

---

### Lecture 2: Fintech Ecosystem

**Title:** Fintech Ecosystem
**Subtitle:** Growth, Social Impact, and Behavioral Dimensions

**Sections:**
1. **Fintech Growth Drivers** -- Venture capital investment trends; technology cost reduction; smartphone penetration; generational shift in banking preferences
2. **Economic Benefits** -- Cost reduction through automation; improved credit access; faster time-to-market for financial products
3. **Financial Inclusion** -- Unbanked and underbanked populations; mobile money in developing economies (M-Pesa case); microfinance platforms
4. **Trust in Fintech** -- Consumer trust frameworks; transparency vs. traditional banking opacity; data privacy concerns; brand trust vs. technology trust
5. **Risk Aversion and Adoption** -- Behavioral finance perspective; technology adoption lifecycle; demographic variation in fintech adoption
6. **Choice Architecture** -- Nudging in financial products; default settings in savings apps; framing effects in investment platforms; ethical considerations

**Suggested Conceptual Diagrams:**
1. **Ecosystem diagram** -- Fintech ecosystem map showing key players: startups, incumbents, regulators, investors, consumers, technology providers
2. **Concept illustration** -- Technology adoption lifecycle applied to fintech services
3. **Comparison bar chart** -- Trust factors: traditional banks vs. fintech platforms vs. big tech financial services

**Quiz Focus Areas:**
- Standard: Growth drivers, financial inclusion mechanisms, trust factors, nudging concepts, adoption barriers
- Advanced: Evaluate ethical implications of choice architecture in financial apps; analyze trade-offs between financial inclusion and consumer protection; synthesize a strategy for building fintech trust in a low-trust market

---

### Lecture 3: Payments and Fintech

**Title:** Payments and Fintech
**Subtitle:** From Cash to Digital: The Transformation of Money Movement

**Sections:**
1. **History of Payments** -- Barter, commodity money, coinage, paper money, checks, wire transfers, credit cards, digital wallets
2. **Global Payment Trends** -- Cash vs. card vs. mobile by region; real-time payment systems (UPI India, PIX Brazil, FedNow US); cross-border payment corridors
3. **Payment Process Complexity** -- Four-party model (issuer, acquirer, network, merchant); authorization, clearing, settlement lifecycle; batch vs. real-time processing
4. **Merchant Cost Burden** -- Interchange fees; payment facilitator model; cost comparison across payment types; impact on small vs. large merchants
5. **Regulation of Credit and Payments** -- Durbin Amendment; PSD2 in Europe; interchange fee caps; open banking mandates
6. **Future of Payments** -- Central bank digital currencies (CBDCs); stablecoins; instant settlement networks; embedded payments; invisible payments

**Suggested Conceptual Diagrams:**
1. **Timeline** -- History of payment methods from barter (3000 BCE) to CBDCs (2020s)
2. **Flowchart** -- Four-party payment model: cardholder -> issuer -> network -> acquirer -> merchant (with authorization, clearing, settlement flows)
3. **Comparison bar chart** -- Merchant cost per transaction across payment types: cash, debit, credit, mobile wallet, BNPL

**Quiz Focus Areas:**
- Standard: Payment history milestones, four-party model roles, interchange fee mechanics, global payment trends, CBDC basics
- Advanced: Analyze the impact of PSD2 on European payment competition; evaluate whether CBDCs will displace commercial bank deposits; synthesize a payment strategy for a merchant entering three different markets

---

### Lecture 4: Fintech Security and Regulation -- RegTech

**Title:** Fintech Security and Regulation -- RegTech
**Subtitle:** Navigating Compliance in the Digital Finance Era

**Sections:**
1. **Regulatory Perspectives** -- Innovation-friendly vs. precautionary approaches; regulatory objectives (stability, consumer protection, competition, innovation); the regulatory trilemma
2. **AML and KYC** -- Money laundering stages (placement, layering, integration); KYC process flow; digital identity verification; transaction monitoring systems
3. **US Fintech Regulation** -- Federal vs. state regulatory patchwork; OCC fintech charter; SEC and CFTC jurisdiction over digital assets; Consumer Financial Protection Bureau (CFPB)
4. **Global Regulatory Landscape** -- EU MiCA regulation; UK FCA regulatory sandbox; Singapore MAS licensing framework; regulatory arbitrage and forum shopping
5. **RegTech Solutions** -- Automated compliance monitoring; natural language processing for regulatory change; real-time transaction surveillance; regulatory reporting automation
6. **Looking Forward** -- Regulatory sandboxes worldwide; embedded compliance (compliance-as-a-service); suptech (supervisory technology); harmonization efforts

**Suggested Conceptual Diagrams:**
1. **Flowchart** -- KYC/AML compliance process: customer onboarding -> identity verification -> risk assessment -> ongoing monitoring -> suspicious activity reporting
2. **Architecture diagram** -- RegTech technology stack: data layer, analytics layer, reporting layer, integration layer
3. **Comparison matrix** -- Global regulatory approaches by jurisdiction (US, EU, UK, Singapore): licensing, sandbox, crypto regulation, open banking mandate

**Quiz Focus Areas:**
- Standard: AML stages, KYC process steps, US regulatory bodies, key global regulations (MiCA, PSD2), RegTech capabilities
- Advanced: Evaluate trade-offs between regulatory innovation sandboxes and consumer protection; analyze how regulatory arbitrage affects global fintech competition; design a compliance framework for a fintech operating in three jurisdictions

---

### Lecture 5: Personal Finance and Wealth Management

**Title:** Personal Finance and Wealth Management
**Subtitle:** How Technology Is Democratizing Investment

**Sections:**
1. **Robo-Advisors** -- Definition and operating model; algorithmic portfolio construction; MPT and risk profiling; major platforms (Betterment, Wealthfront, Nutmeg)
2. **Personal Finance Tools** -- Budgeting and expense tracking apps; account aggregation; financial goal planning; behavioral nudges in savings
3. **AI in Wealth Management** -- Machine learning for asset allocation; sentiment analysis for market signals; personalized financial advice; chatbot advisory
4. **Case Studies** -- Betterment (US robo-advisory pioneer); Revolut (neobank with wealth features); Ant Group (comprehensive financial platform); Scalable Capital (European robo-advisor)
5. **Fee Structure Comparison** -- Traditional advisor fees (AUM-based); robo-advisor fee models; hybrid advisory pricing; total cost of ownership analysis
6. **Democratization of Investment** -- Fractional shares; micro-investing; social trading; impact investing platforms; access to alternative assets

**Suggested Conceptual Diagrams:**
1. **Comparison bar chart** -- Fee structures: traditional advisor (1-2% AUM) vs. robo-advisor (0.25-0.50%) vs. DIY (0%) with service level comparison
2. **Flowchart** -- Robo-advisor process: risk questionnaire -> profile classification -> portfolio construction -> automatic rebalancing -> tax-loss harvesting
3. **Architecture diagram** -- AI-driven wealth management platform: data ingestion, ML models, portfolio engine, client interface, compliance layer

**Quiz Focus Areas:**
- Standard: Robo-advisor mechanics, MPT basics, fee comparison, personal finance tool features, AI applications in wealth management
- Advanced: Evaluate whether robo-advisors can fully replace human advisors for HNW clients; analyze the behavioral economics of micro-investing platforms; design an ideal hybrid advisory model

---

### Lecture 6: Insurtech

**Title:** Insurtech
**Subtitle:** Technology-Driven Innovation in Insurance

**Sections:**
1. **Insurance Industry Overview** -- Traditional insurance value chain; pain points (complexity, slow claims, opaque pricing); ripe areas for disruption
2. **Digital Insurance Platforms** -- Direct-to-consumer models; comparison platforms; on-demand and usage-based insurance; peer-to-peer insurance
3. **Underwriting Automation** -- Data-driven risk assessment; telematics and IoT-based pricing; AI underwriting models; real-time risk scoring
4. **Claims Processing** -- Automated claims triage; computer vision for damage assessment; fraud detection algorithms; straight-through processing
5. **Insurtech Case Studies** -- Lemonade (AI-first insurance); Root Insurance (telematics auto); Oscar Health (health tech insurance); Parametric insurance examples (flight delay, crop insurance)
6. **Parametric Insurance and Smart Contracts** -- Trigger-based payouts; blockchain-enabled insurance contracts; weather derivatives; removing the claims process entirely

**Suggested Conceptual Diagrams:**
1. **Flowchart** -- Traditional insurance claims process vs. automated insurtech claims process (side-by-side)
2. **Comparison bar chart** -- Insurance value chain disruption: traditional vs. insurtech across distribution, underwriting, claims, and customer service
3. **Architecture diagram** -- IoT-enabled insurtech platform: sensors -> data pipeline -> risk engine -> pricing model -> policy management -> claims automation

**Quiz Focus Areas:**
- Standard: Traditional insurance pain points, digital platform models, telematics pricing, automated claims features, parametric insurance triggers
- Advanced: Evaluate the viability of peer-to-peer insurance models at scale; analyze how IoT data changes the fundamental nature of insurance underwriting; design a parametric insurance product for a specific risk scenario

---

### Lecture 7: The Technology of FinTech

**Title:** The Technology of FinTech
**Subtitle:** The Digital Infrastructure Powering Financial Innovation

**Sections:**
1. **Digital Identity** -- Authentication methods (passwords, biometrics, MFA); self-sovereign identity; privacy-preserving techniques (zero-knowledge proofs overview); GDPR and identity
2. **Blockchain and Encryption** -- Cryptographic primitives (hashing, public-key encryption); distributed ledger concepts; smart contracts at a high level; permissioned vs. permissionless blockchains; use cases in trade finance and settlement
3. **Big Data and Analytics** -- Data sources in financial services; credit scoring with alternative data; real-time analytics; data governance and ethics
4. **AI, DSS, and Automation** -- Machine learning applications (fraud detection, credit risk, chatbots); decision support systems; robotic process automation (RPA); explainability and bias in financial AI
5. **Smartphones and Customer Technology** -- Mobile-first banking design; biometric authentication; push notifications and engagement; super-apps; embedded finance via mobile
6. **Cloud and APIs** -- Banking-as-a-service (BaaS); API economy in financial services; cloud infrastructure for fintech; microservices architecture; security in cloud-native finance

**Suggested Conceptual Diagrams:**
1. **Architecture diagram** -- Fintech technology stack: infrastructure layer (cloud, APIs), data layer (big data, analytics), intelligence layer (AI/ML), application layer (mobile, web), security layer (identity, encryption)
2. **Flowchart** -- Blockchain transaction lifecycle: initiation -> validation -> consensus -> block addition -> confirmation
3. **Concept illustration** -- AI applications in fintech mapped to the customer journey: onboarding (KYC/identity) -> engagement (personalization) -> transactions (fraud detection) -> advisory (robo-advice) -> compliance (RegTech)

**Quiz Focus Areas:**
- Standard: Authentication methods, blockchain basics, big data applications, AI use cases in finance, API concepts, cloud benefits
- Advanced: Evaluate privacy trade-offs between centralized identity and self-sovereign identity; analyze how explainability requirements constrain AI model selection in finance; synthesize a technology architecture for a new neobank

---

## Theme and Branding

### Color Scheme

| Element | Color | Hex Code |
|---------|-------|----------|
| Navigation bar | Dark navy | `#1a1a4e` |
| Hero gradient start | Teal | `#0D7377` |
| Hero gradient end | Light blue | `#14BDEB` |
| Accent | Orange | `#FF7F0E` |
| Module: Foundations | Green | `#2CA02C` |
| Module: Financial Services | Orange | `#FF7F0E` |
| Module: Regulation and Insurance | Red | `#D62728` |
| Module: Technology | Blue | `#3333B2` |

### Design Rationale
The teal-to-blue gradient conveys technology and trust, differentiating this Fintech course from the blockchain course (which uses purple-to-blue). The four-module color scheme follows the established course-creator convention. Orange accents draw attention to key interactive elements (buttons, links).

### Module-Lecture Assignment

| Module | Color | Lectures |
|--------|-------|----------|
| Foundations (green) | `#2CA02C` | L01 (Foundations), L02 (Ecosystem) |
| Financial Services (orange) | `#FF7F0E` | L03 (Payments), L05 (Wealth Management) |
| Regulation and Insurance (red) | `#D62728` | L04 (RegTech), L06 (Insurtech) |
| Technology (blue) | `#3333B2` | L07 (Technology) |

---

## Execution Plan: Task Flow

### Prerequisites Check (before any generation)

**Task 0: Verify Dependencies**
- [ ] Verify `pdflatex --version` returns a valid TeX distribution
- [ ] Verify `python --version` returns Python 3.x
- [ ] Verify `python -c "import matplotlib; import numpy"` succeeds
- [ ] Verify `pdftoppm -v` or `magick --version` for PDF-to-PNG conversion
- [ ] Verify `gh auth status` returns authenticated
- [ ] Verify skill files exist at `~/.claude/skills/omc-learned/course-creator/`

**Acceptance:** All 6 dependency checks pass. If any fail, report with install instructions and stop.

---

### Task 1: Create `course.yaml` Manifest

**Action:** Write the complete `course.yaml` file (provided above in this plan) to `D:/Joerg/Research/slides/Fintech/course.yaml`.

**Acceptance Criteria:**
- [ ] File exists at `D:/Joerg/Research/slides/Fintech/course.yaml`
- [ ] YAML parses without syntax errors
- [ ] All 7 lectures present with sequential numbering 1-7
- [ ] All 4 modules present with correct lecture assignments
- [ ] Every lecture number appears in exactly one module
- [ ] Prerequisites are valid (reference only lower-numbered lectures)
- [ ] `projects: []` (empty, confirming no project tracks)
- [ ] Quiz configuration matches spec (20 standard, 20 advanced per lecture)

---

### Task 2: Run Stage 1 -- Slide Generation (course-creator:slides)

**Action:** For each of the 7 lectures, generate:
- Master content plan
- `L{NN}_full.tex` (~30 slides) via full-lecture-generator
- `L{NN}_overview.tex` (~25-30 slides) via beamer-slide-creator
- `L{NN}_deepdive.tex` (~15-20 slides) via beamer-slide-creator
- `L{NN}_core.tex` (~10 slides) extracted from full
- `L{NN}_mini10.tex` (10 slides) via mini-lecture-generator
- `L{NN}_mini5.tex` (5 slides) via mini-lecture-generator
- Quiz `.tex` files (standard)
- Exercise `.tex` files

Also generate `_shared/preamble.tex` with Fintech-specific metadata.

**CRITICAL CONSTRAINTS for content generation:**
- All charts must be conceptual diagrams (process flows, architecture diagrams, comparison matrices, conceptual models)
- NO real market data, NO live data references, NO stock prices, NO cryptocurrency prices
- Target audience: MSc finance/business students -- assume strong financial literacy, explain technology concepts
- All figure references use `\includegraphics` pointing to `figures/` directory (chart scripts generated in Stage 2)

**Parallelism:** Lectures 1, 3 can run in parallel (both have only prerequisite []). Lectures 2, 4, 5, 6 depend on L1. Lecture 7 depends on all previous.

**Suggested execution order:**
1. L01 (no prerequisites) -- generates first, establishes style
2. L02, L03 in parallel (L02 depends on L01; L03 depends on L01)
3. L04, L05, L06 in parallel (all depend on L01 + L02)
4. L07 last (depends on all)

**Acceptance Criteria:**
- [ ] 42 `.tex` files exist (7 lectures x 6 variants)
- [ ] Frame counts within expected ranges per variant
- [ ] Self-contained preamble in mini5, mini10, core (no `\input` commands)
- [ ] Shared preamble reference in full, overview, deepdive
- [ ] No `chart.py` scripts generated (only `\includegraphics` references)
- [ ] 7 quiz `.tex` files (standard) generated
- [ ] 7 exercise `.tex` files generated
- [ ] All content is conceptual (no real market data in any slide)

---

### Task 3: Run Stage 2 -- Charts and Compilation (course-creator:charts)

**Action:**
1. Generate `_shared/chart_styles.py` with Fintech theme colors (using the teal/blue palette)
2. For each lecture, run chart auto-derivation to determine chart specifications
3. Generate `chart.py` scripts for all conceptual diagrams (12 per lecture = ~84 total)
4. Execute all `chart.py` scripts to produce `chart.pdf` files
5. Compile all `.tex` files to `.pdf` using `pdflatex` (two passes)

**CRITICAL CONSTRAINTS for chart generation:**
- ALL charts must be conceptual: process flows, architecture diagrams, comparison matrices, conceptual models
- Use matplotlib for bar charts, comparison charts, and data visualizations with SYNTHETIC/ILLUSTRATIVE data only
- Use matplotlib with annotation-heavy approaches for flowcharts and architecture diagrams
- NO real market data. Use clearly labeled illustrative/conceptual data (e.g., "Illustrative cost comparison")
- Opening and closing cartoons use `plt.xkcd()` style
- All chart scripts use `np.random.seed(42)` where randomness is needed
- All chart scripts import from `_shared/chart_styles.py`
- `figsize=(10,6)` for all charts
- No `plt.show()` calls

**Acceptance Criteria:**
- [ ] `_shared/chart_styles.py` exists with Fintech theme colors
- [ ] ~84 `chart.py` scripts generated (12 per lecture)
- [ ] All `chart.py` scripts produce `chart.pdf` (exit code 0)
- [ ] All 42 `.tex` files compile to `.pdf` without errors
- [ ] Zero missing PDFs
- [ ] All charts are conceptual (visual inspection of a sample)
- [ ] CHART_METADATA dict present in every chart.py
- [ ] V4_COLORS palette used consistently

---

### Task 4: Run Stage 3 -- Galleries (course-creator:galleries)

**Action:**
1. Convert all 42 PDFs to PNGs using `pdftoppm` (or ImageMagick fallback)
2. Place PNGs in `website/galleries/images/L{NN}/{variant}/slide_{PP}.png`
3. Generate 7 gallery HTML pages (`website/galleries/L{NN}_gallery.html`) with 5 variant tabs
   - **Note:** Gallery shows 5 tabs (mini5, mini10, core, extended, full). The deepdive variant is NOT shown in the gallery but IS included in downloads. This is by design per `course-creator-galleries.md`.

**Acceptance Criteria:**
- [ ] PNG files exist for all 42 PDF variants
- [ ] PNG count matches PDF page count for each variant
- [ ] 7 gallery HTML pages generated
- [ ] All 5 tabs functional in each gallery page (deepdive excluded by design; available only as PDF download)
- [ ] Lightbox opens and navigates correctly
- [ ] Download buttons link to correct PDFs
- [ ] No broken image references

---

### Task 5: Run Stage 4 -- Lecture HTML Pages (course-creator:lectures)

**Action:**
1. Parse each full-variant `.tex` file to extract content
2. Map frames to the 8-section framework (WHY, WHAT, CASE, HOW, RISK, WHERE, IMPACT, SOWHAT)
3. Convert LaTeX content to HTML using the conversion rules
4. Copy chart PNGs to `website/charts/L{NN}/`
5. Generate 7 HTML lecture pages (`website/lectures/L{NN}.html`)

**Acceptance Criteria:**
- [ ] 7 lecture HTML pages exist
- [ ] All 8 sections present in each HTML page
- [ ] No raw LaTeX commands in HTML output
- [ ] All `<img>` src paths resolve to existing files
- [ ] KaTeX CDN included for formula rendering
- [ ] Sidebar navigation matches section IDs
- [ ] Download links point to correct PDF paths
- [ ] Scroll-tracking JavaScript functional

---

### Task 6: Run Stage 5 -- Quizzes (course-creator:quizzes)

**Action:**
1. Parse standard quiz `.tex` files from Stage 1 and convert to interactive HTML
2. Generate 7 advanced quiz HTML pages (20 questions each, higher Bloom's level)
3. Each quiz page has inline CSS, ANSWERS JavaScript object, and checkAnswers() function

**Quiz Content Constraints:**
- Questions must be appropriate for MSc finance/business students
- Standard quizzes: understand(4) + apply(8) + analyze(6) + evaluate(2) = 20
- Advanced quizzes: apply(4) + analyze(8) + evaluate(6) + create(2) = 20
- No coding-related questions
- All questions test conceptual understanding, not technical implementation
- Advanced quiz questions must NOT duplicate standard quiz questions

**Acceptance Criteria:**
- [ ] 14 quiz HTML pages: `L{NN}_quiz.html` (standard) and `L{NN}_quiz_advanced.html` (advanced) -- filenames must match deploy skill links
- [ ] Each quiz contains exactly 20 question blocks
- [ ] Bloom's distribution matches configuration
- [ ] ANSWERS object has keys "1" through "20" with non-empty explanations
- [ ] checkAnswers() function present and correct
- [ ] Standard and advanced quizzes have zero duplicate questions
- [ ] Nav bar links are correct relative paths
- [ ] No JavaScript console errors

---

### Task 7: SKIP Stage 6 -- Projects (NOT APPLICABLE)

**Action:** No action. Projects are not part of this course. The `projects: []` in the manifest confirms this.

---

### Task 8: Run Stage 7 -- Deploy (course-creator:deploy)

**Action:**
1. Copy all 42 PDFs to `website/downloads/`
2. Copy chart PNGs to `website/charts/L{NN}/`
3. Generate `website/index.html` with:
   - Hero banner with "Financial Technology (FinTech)" title, teal-to-blue gradient
   - 4 module sections with color-coded badges
   - 7 lecture cards with links to lecture pages, galleries, quizzes, downloads
   - No projects section (empty projects array)
   - Omit the "Projects" nav link from the index page since `projects: []` is empty. The deploy skill template includes a Projects nav link by default; remove it for this course.
   - Footer with generation info
4. Generate `.github/workflows/deploy.yml`
5. Create GitHub repo: `gh repo create digital-ai-finance/Fintech --public`
6. Push all website files to main branch
7. Configure GitHub Pages
8. Verify deployment is live

**Acceptance Criteria:**
- [ ] `website/index.html` generated with all lecture cards
- [ ] 42 PDFs in `website/downloads/`
- [ ] Chart PNGs in `website/charts/`
- [ ] `.github/workflows/deploy.yml` exists (static deploy only, no LaTeX)
- [ ] GitHub repo `digital-ai-finance/Fintech` exists and is public
- [ ] GitHub Pages configured on main branch
- [ ] Site is live at `https://digital-ai-finance.github.io/Fintech/`
- [ ] All navigation links work (no 404s)
- [ ] No "Projects" nav link in index page (projects: [] is empty)
- [ ] All PDF downloads accessible
- [ ] Responsive layout at 1400px, 1000px, 800px breakpoints

---

## Commit Strategy

| Commit | After Task | Message |
|--------|------------|---------|
| 1 | Task 1 | `feat: add course.yaml manifest for MSc Fintech course (7 lectures, 4 modules)` |
| 2 | Task 2 (per lecture batch) | `feat: generate LaTeX slides for lectures L01-L03` |
| 3 | Task 2 (remaining) | `feat: generate LaTeX slides for lectures L04-L07` |
| 4 | Task 3 | `feat: generate chart scripts and compile all PDFs` |
| 5 | Task 4 | `feat: generate PNG galleries for all lecture variants` |
| 6 | Task 5 | `feat: generate HTML lecture pages (7 lectures)` |
| 7 | Task 6 | `feat: generate quiz pages (14 quizzes: 7 standard + 7 advanced)` |
| 8 | Task 8 | `feat: generate index page and deploy to GitHub Pages` |

Note: Commits are local until Stage 7 (deploy) pushes everything to GitHub.

---

## Success Criteria

### Quantitative
- [ ] 42 `.tex` files generated (7 x 6 variants)
- [ ] 42 `.pdf` files compiled
- [ ] ~84 chart scripts generated and executed
- [ ] 7 gallery HTML pages with PNGs for all variants
- [ ] 7 lecture HTML pages with 8 sections each
- [ ] 14 quiz HTML pages with 20 questions each (280 total questions)
- [ ] 1 index HTML page
- [ ] Site live at `digital-ai-finance.github.io/Fintech/`

### Qualitative
- [ ] Content appropriate for MSc finance/business students
- [ ] No coding exercises or programming requirements
- [ ] All charts are conceptual (no real market data)
- [ ] Consistent visual theme across all pages
- [ ] Professional academic quality

### Final Verification
- [ ] Run full link check on deployed site
- [ ] Spot-check 3 quizzes for answer correctness
- [ ] Spot-check 3 lectures for LaTeX-to-HTML fidelity
- [ ] Verify all 6 PDF variants downloadable for at least 2 lectures

---

## Expected Output Directory Structure

```
D:/Joerg/Research/slides/Fintech/
  course.yaml
  _shared/
    preamble.tex
    chart_styles.py
  lectures/
    L01_fintech_foundations/
      slides/
        L01_mini5.tex    + L01_mini5.pdf
        L01_mini10.tex   + L01_mini10.pdf
        L01_core.tex     + L01_core.pdf
        L01_overview.tex + L01_overview.pdf
        L01_deepdive.tex + L01_deepdive.pdf
        L01_full.tex     + L01_full.pdf
      figures/
        01_fintech_evolution_timeline/chart.py + chart.pdf
        02_banking_value_chain_flow/chart.py + chart.pdf
        ... (12 figures total)
      quizzes/
        L01_quiz_standard.tex + L01_quiz_standard.pdf
        L01_quiz_advanced.tex + L01_quiz_advanced.pdf
      exercises/
        L01_exercises.tex + L01_exercises.pdf
    L02_fintech_ecosystem/
      ...
    L03_payments_and_fintech/
      ...
    L04_regtech/
      ...
    L05_wealth_management/
      ...
    L06_insurtech/
      ...
    L07_technology_of_fintech/
      ...
  website/
    index.html
    lectures/
      L01.html ... L07.html
    quizzes/
      L01_quiz.html, L01_quiz_advanced.html ... L07_quiz.html, L07_quiz_advanced.html
    galleries/
      L01_gallery.html ... L07_gallery.html
      images/
        L01/ (mini5/, mini10/, core/, extended/, full/)
        ...
    downloads/
      L01_mini5.pdf ... L07_full.pdf (42 PDFs total)
    charts/
      L01/ ... L07/ (chart PNGs)
  .github/
    workflows/
      deploy.yml
```

---

## Notes for Executor

1. **Conceptual charts constraint is paramount.** Every chart.py must produce a conceptual diagram. If chart auto-derivation suggests a time_series type, use illustrative/synthetic data with clear labels like "Illustrative Growth Trend" rather than real market data.

2. **Audience calibration.** These are finance/business MSc students who understand DCF, portfolio theory, risk management, and financial regulation. They do NOT know how to code. All slides should explain technology at a conceptual level, using analogies to familiar finance concepts where possible.

3. **Stage 6 is SKIPPED.** Do not generate project pages. The `projects: []` in the manifest handles this cleanly. The index page should not include a projects section.

4. **Quiz quality matters.** The 280 questions (140 standard + 140 advanced) are the primary assessment tool. Each question must have one unambiguously correct answer and a clear explanation. No trick questions.

5. **Lecture split across days.** Lectures 2 and 5 are split across two days. The slide content does not need to reflect this split -- the instructor handles the pacing. The course.yaml does not encode day scheduling.

6. **The manifest theme uses teal-to-blue gradient** (`#0D7377` to `#14BDEB`) for the hero banner, differentiating from the blockchain course. Ensure the index page and all HTML pages use this gradient, not the default purple-to-blue.

7. **Authoritative HTML filenames (CRITICAL -- must align with deploy skill links).** The deploy skill (`course-creator-deploy.md` lines 174-176) defines the canonical URLs that the index page links to. All generated HTML files MUST use these exact names:
   - **Quizzes:** `quizzes/L{NN}_quiz.html` (standard) and `quizzes/L{NN}_quiz_advanced.html` (advanced)
   - **Galleries:** `galleries/L{NN}_gallery.html`
   - **Lectures:** `lectures/L{NN}.html` (unchanged)
   - If the galleries skill (`course-creator-galleries.md`) generates `L{NN}.html`, rename to `L{NN}_gallery.html` to match deploy links. If the quizzes skill generates `L{NN}_standard.html`, rename to `L{NN}_quiz.html`. The deploy skill filenames are authoritative.

8. **Gallery shows 5 tabs; deepdive excluded by design.** Gallery pages display 5 variant tabs: mini5, mini10, core, extended, full. The deepdive variant is NOT shown in the gallery but IS included in `website/downloads/` as a PDF download. This is by design per `course-creator-galleries.md` (line 9: "5 variant tabs (mini5, mini10, core, extended, full)").
