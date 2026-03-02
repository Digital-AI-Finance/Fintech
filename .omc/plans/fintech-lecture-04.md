# Execution Plan: Lecture 4 -- Fintech Security and Regulation -- RegTech

**Plan ID:** fintech-lecture-04
**Created:** 2026-03-01
**Status:** READY FOR EXECUTION
**Complexity:** HIGH (17 phases, ~50 deliverable files)

---

## Context

### Original Request
Create Lecture 4 (Fintech Security and Regulation -- RegTech) for the MSc-level Financial Technology course at University of Zurich. L01, L02, and L03 are complete and deployed. L04 must follow their exact patterns.

### Research Findings (from codebase exploration)

**Verified L03 patterns (L04 must match):**

| Pattern | L03 Value | L04 Must Match |
|---------|-----------|----------------|
| Full tex frames | 31 | ~31 |
| Overview tex frames | ~28 | ~25-30 |
| Deepdive tex frames | ~17 | ~15-20 |
| Core tex frames | 10 | ~10 |
| Mini10 frames | 10 + title | exactly 10 + title |
| Mini5 frames | 5 + title | exactly 5 + title |
| Chart subdirs | 10 charts + 2 cartoons = 12 | 10 charts + 2 cartoons = 12 |
| Preamble (full/overview/deepdive) | `\input{../../_shared/preamble.tex}` | same |
| Preamble (core/mini10/mini5) | self-contained inline | same |
| Chart imports | `sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))` | same |
| Chart style | `from chart_styles import V4_COLORS, apply_v4_style, save_chart` | same |
| Cartoon style | `with plt.xkcd():` context manager | same |
| Chart output | `chart.pdf` / `cartoon.pdf` per subdir | same |
| Chart figsize | `figsize=(10, 6)` for charts, `figsize=(12, 6)` for cartoons | same |
| Random seed | `np.random.seed(42)` | same |

**Shared infrastructure (confirmed locations):**
- Preamble: `D:/Joerg/Research/slides/Fintech/_shared/preamble.tex`
- Chart styles: `D:/Joerg/Research/slides/Fintech/_shared/chart_styles.py`
- Gallery images structure: `docs/galleries/images/L0X/{mini5,mini10,core,extended,full}/`
- Slide PDFs: `docs/slides/pdf/L0X_*.pdf`
- Chart PNGs: `docs/slides/images/L0X_*/`

**Relative path from L04 dir to _shared:** `../../_shared/` -- match L03 pattern exactly; copy the import line verbatim from L03 chart.py. For LaTeX: `\input{../../_shared/preamble.tex}`. For Python: `sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))`. Both confirmed working in L03 production code.

**index.html L04 card (lines 806-836):** Currently shows "Digital Lending and Credit" as coming-soon. This title is WRONG for L04's actual topic. Must update title to "Fintech Security and Regulation", update description, change status to "available", and convert disabled spans to active links.

---

## Work Objectives

### Core Objective
Produce Lecture 4 (Fintech Security and Regulation -- RegTech) with all 6 LaTeX variants, 12 chart/cartoon scripts, 2 quiz HTML files, 1 lecture HTML page, 1 gallery HTML page, and all supporting assets -- following the exact L01/L02/L03 pattern.

### Deliverables (Complete File Inventory)

**Slides directory: `slides/L04_Fintech_Security_and_Regulation/`** (37 files)
| # | File | Type |
|---|------|------|
| 1 | `L04_full.tex` | LaTeX, ~31 frames, uses `\input{../../_shared/preamble.tex}` |
| 2 | `L04_overview.tex` | LaTeX, ~25-30 frames, uses `\input{../../_shared/preamble.tex}` |
| 3 | `L04_deepdive.tex` | LaTeX, ~15-20 frames, uses `\input{../../_shared/preamble.tex}` |
| 4 | `L04_core.tex` | LaTeX, ~10 frames, self-contained (inline preamble) |
| 5 | `L04_mini10.tex` | LaTeX, exactly 10+title frames, self-contained |
| 6 | `L04_mini5.tex` | LaTeX, exactly 5+title frames, self-contained |
| 7 | `L04_full.pdf` | Compiled PDF |
| 8 | `L04_overview.pdf` | Compiled PDF |
| 9 | `L04_deepdive.pdf` | Compiled PDF |
| 10 | `L04_core.pdf` | Compiled PDF |
| 11 | `L04_mini10.pdf` | Compiled PDF |
| 12 | `L04_mini5.pdf` | Compiled PDF |
| 13 | `01_regulatory_approaches/chart.py` | Python matplotlib |
| 14 | `01_regulatory_approaches/chart.pdf` | Generated chart |
| 15 | `02_aml_compliance_flow/chart.py` | Python matplotlib |
| 16 | `02_aml_compliance_flow/chart.pdf` | Generated chart |
| 17 | `03_kyc_process_flow/chart.py` | Python matplotlib |
| 18 | `03_kyc_process_flow/chart.pdf` | Generated chart |
| 19 | `04_money_laundering_stages/chart.py` | Python matplotlib |
| 20 | `04_money_laundering_stages/chart.pdf` | Generated chart |
| 21 | `05_us_regulatory_patchwork/chart.py` | Python matplotlib |
| 22 | `05_us_regulatory_patchwork/chart.pdf` | Generated chart |
| 23 | `06_global_regulatory_comparison/chart.py` | Python matplotlib |
| 24 | `06_global_regulatory_comparison/chart.pdf` | Generated chart |
| 25 | `07_regtech_stack_architecture/chart.py` | Python matplotlib |
| 26 | `07_regtech_stack_architecture/chart.pdf` | Generated chart |
| 27 | `08_sandbox_adoption_timeline/chart.py` | Python matplotlib |
| 28 | `08_sandbox_adoption_timeline/chart.pdf` | Generated chart |
| 29 | `09_compliance_cost_comparison/chart.py` | Python matplotlib |
| 30 | `09_compliance_cost_comparison/chart.pdf` | Generated chart |
| 31 | `10_regtech_investment_trends/chart.py` | Python matplotlib |
| 32 | `10_regtech_investment_trends/chart.pdf` | Generated chart |
| 33 | `11_opening_cartoon/cartoon.py` | Python matplotlib (xkcd style) |
| 34 | `11_opening_cartoon/cartoon.pdf` | Generated cartoon |
| 35 | `12_closing_cartoon/cartoon.py` | Python matplotlib (xkcd style) |
| 36 | `12_closing_cartoon/cartoon.pdf` | Generated cartoon |
| 37 | `AGENTS.md` | Directory documentation |

**Docs directory additions:** (8+ files)
| # | File | Type |
|---|------|------|
| 38 | `docs/lectures/L04.html` | Lecture page (8 sections) |
| 39 | `docs/galleries/L04_gallery.html` | 5-tab gallery |
| 40 | `docs/galleries/images/L04/mini5/*.png` | Gallery slide PNGs |
| 41 | `docs/galleries/images/L04/mini10/*.png` | Gallery slide PNGs |
| 42 | `docs/galleries/images/L04/core/*.png` | Gallery slide PNGs |
| 43 | `docs/galleries/images/L04/extended/*.png` | Gallery slide PNGs |
| 44 | `docs/galleries/images/L04/full/*.png` | Gallery slide PNGs |
| 45 | `docs/quiz/L04_quiz.html` | Standard quiz (20 questions) |
| 46 | `docs/quiz/L04_quiz_advanced.html` | Advanced quiz (20 questions) |
| 47 | `docs/slides/pdf/L04_full.pdf` | Copy of compiled PDF |
| 48 | `docs/slides/pdf/L04_overview.pdf` | Copy of compiled PDF |
| 49 | `docs/slides/pdf/L04_deepdive.pdf` | Copy of compiled PDF |
| 50 | `docs/slides/pdf/L04_core.pdf` | Copy of compiled PDF |
| 51 | `docs/slides/pdf/L04_mini10.pdf` | Copy of compiled PDF |
| 52 | `docs/slides/pdf/L04_mini5.pdf` | Copy of compiled PDF |
| 53 | `docs/slides/images/L04_Fintech_Security_and_Regulation/*.png` | 12 chart PNGs |

**Modified files:** (1 file)
| # | File | Change |
|---|------|--------|
| 54 | `docs/index.html` | L04 card: `coming-soon` -> `available`, fix title to "Fintech Security and Regulation", add active links + download block |

### Definition of Done
- [ ] All 6 .tex files compile without errors via pdflatex (2 passes each)
- [ ] All 12 chart.py / cartoon.py scripts execute without errors and produce .pdf output
- [ ] All 6 compiled PDFs render correctly (spot-check: title page, charts visible, no missing fonts)
- [ ] Both quiz HTML files load in browser with working JS (check answer, score calculation)
- [ ] L04.html lecture page loads with all 8 sections, sidebar navigation working
- [ ] L04_gallery.html loads with 5 tabs, images visible
- [ ] docs/index.html shows L04 as "Available" with working links, title corrected
- [ ] All `\includegraphics` paths in .tex files resolve correctly
- [ ] Frame counts match spec: full(~31), overview(~25-30), deepdive(~15-20), core(~10), mini10(10+title), mini5(5+title)
- [ ] Quiz Bloom's distribution: standard = understand(4)+apply(8)+analyze(6)+evaluate(2), advanced = apply(4)+analyze(8)+evaluate(6)+create(2)

---

## Guardrails

### MUST Have
- All relative paths match L03 pattern exactly (../../_shared for both LaTeX and Python)
- `\includegraphics` use bare relative paths like `01_regulatory_approaches/chart.pdf` (no `figures/` prefix)
- Self-contained mini variants (mini10, mini5) have NO `\input{}` commands and NO `\includegraphics` -- pure TikZ + text
- Core variant has NO `\input{}` but DOES use `\includegraphics` for charts (self-contained preamble with chart references)
- Full/overview/deepdive variants use `\input{../../_shared/preamble.tex}`
- All chart.py scripts have `CHART_METADATA` dict
- All chart.py scripts have fallback V4_COLORS and helper functions (try/except pattern from L03)
- Cartoons use `with plt.xkcd():` context
- All quiz questions are about regulation/compliance/RegTech content -- NO coding questions
- Subtitle in LaTeX: "Navigating Compliance in the Digital Finance Era"
- Bridge frame references L03 (payment regulation, PSD2, interchange caps -> broader regulatory landscape)
- Forward-look frame previews L05 (Personal Finance and Wealth Management)
- Course progress bar updated to show L01-L03 checked, L04 bold
- index.html L04 card title changed from "Digital Lending and Credit" to "Fintech Security and Regulation"

### MUST NOT Have
- Real market data in charts (all conceptual with `np.random.seed(42)`)
- `\input{}` in core/mini10/mini5 files
- External file dependencies in mini variants (no `\includegraphics`)
- `figures/` prefix in any `\includegraphics` path
- Coding questions in quizzes
- Any broken relative paths
- Missing chart subdirectories

---

## L04 Content Architecture

### Chart Subdirectories (12 total)

| # | Directory | Chart Type | Content | Section |
|---|-----------|-----------|---------|---------|
| 01 | `01_regulatory_approaches` | comparison_bar | Innovation-friendly vs. precautionary approach comparison across dimensions: speed-to-market, consumer protection, innovation rate, compliance cost, systemic risk (illustrative scores by country: US, UK, Singapore, EU, China) | Regulatory Perspectives |
| 02 | `02_aml_compliance_flow` | flowchart | End-to-end AML compliance pipeline: Customer Onboarding -> Identity Verification -> Risk Scoring -> Transaction Monitoring -> Suspicious Activity Reporting -> Case Management -> Regulatory Filing | AML and KYC |
| 03 | `03_kyc_process_flow` | flowchart | KYC lifecycle: Customer Application -> Document Collection -> Identity Verification (manual vs. digital) -> Screening (PEP, sanctions) -> Risk Rating -> Ongoing Monitoring -> Periodic Review | AML and KYC |
| 04 | `04_money_laundering_stages` | flowchart | Three-stage money laundering model: Placement (cash deposits, smurfing, shell companies) -> Layering (complex transactions, cross-border transfers, shell networks) -> Integration (real estate, businesses, luxury goods) with detection difficulty annotations | AML and KYC |
| 05 | `05_us_regulatory_patchwork` | diagram | US fintech regulatory landscape: Federal level (OCC, SEC, CFTC, CFPB, FinCEN, FDIC) and State level (50 state regulators, money transmitter licenses) with jurisdiction overlaps and gaps visualized | US Fintech Regulation |
| 06 | `06_global_regulatory_comparison` | comparison_bar | Multi-jurisdiction comparison matrix: EU (MiCA), UK (FCA sandbox), Singapore (MAS), US (patchwork), Switzerland (FINMA), across dimensions: sandbox availability, crypto framework, open banking mandate, AML rigor, licensing speed | Global Regulatory Landscape |
| 07 | `07_regtech_stack_architecture` | diagram | RegTech technology stack layers: Data Ingestion (APIs, feeds) -> Data Processing (NLP, ML) -> Analytics (pattern detection, risk scoring) -> Reporting (regulatory filings, dashboards) -> Audit (trail, evidence) with specific technologies annotated per layer | RegTech Solutions |
| 08 | `08_sandbox_adoption_timeline` | time_series | Timeline of regulatory sandbox launches worldwide: UK FCA (2016), Singapore MAS (2016), Australia ASIC (2017), Hong Kong HKMA (2017), EU (various 2018-2020), US state-level (2018-2023), with cumulative count overlay | Looking Forward |
| 09 | `09_compliance_cost_comparison` | comparison_bar | Compliance cost as percentage of revenue for different firm sizes and types: large bank, mid-size bank, fintech startup, neobank, crypto exchange -- showing how compliance burden disproportionately affects smaller firms | RegTech Solutions |
| 10 | `10_regtech_investment_trends` | time_series | RegTech and SupTech investment trends (illustrative 2015-2025): global investment volume, number of deals, average deal size, with key regulatory milestones annotated (MiCA proposal, GDPR enforcement, FCA sandbox launch) | Looking Forward |
| 11 | `11_opening_cartoon` | cartoon (xkcd) | Compliance officer at desk buried under a mountain of paper regulations, with a tiny robot on the desk saying "I can read all of those in 3 seconds." Caption: "The compliance department's new hire." | Opening |
| 12 | `12_closing_cartoon` | cartoon (xkcd) | Two regulators: one human with a magnifying glass examining a single transaction, one AI on multiple screens monitoring millions of transactions simultaneously. The human says "I found a suspicious pattern!" The AI says "I found 47,000." Caption: "SupTech vs. Traditional Supervision" | Closing |

### Narrative Arc (Full Variant, ~31 frames)

| Frame(s) | Arc Role | Content | Charts Used |
|----------|----------|---------|-------------|
| 1 | Title | Title page | -- |
| 2 | Opening | Opening cartoon: "The Compliance Department's New Hire" | 11_opening_cartoon |
| 3 | Objectives | Learning objectives (5 items, Bloom's tagged) | -- |
| 4 | Bridge | Bridge from L03: payment regulation (PSD2, interchange caps) was a taste -- now the full regulatory landscape | 01_regulatory_approaches |
| 5 | FEEL | Personal connection: "Your bank knows more about you than your doctor -- is that protection or surveillance?" | -- |
| 6-9 | WHAT | Regulatory Perspectives: innovation vs. precaution, regulatory objectives (stability, consumer protection, competition, innovation), the regulatory trilemma, global approach comparison | 01, 06 |
| 10-13 | CASE | AML and KYC: money laundering stages, KYC process flow, digital identity verification, transaction monitoring systems | 02, 03, 04 |
| 14-17 | HOW | US Fintech Regulation: federal vs. state patchwork, OCC charter, SEC/CFTC jurisdiction, CFPB role | 05 |
| 18-20 | RISK | Global Regulatory Landscape: MiCA, FCA sandbox, MAS licensing, regulatory arbitrage, forum shopping dangers | 06 |
| 21-23 | WHERE | RegTech Solutions: automated compliance, NLP for regulatory change, real-time surveillance, reporting automation | 07, 09 |
| 24-25 | IMPACT | Looking Forward: sandboxes worldwide, embedded compliance, SupTech, harmonization | 08, 10 |
| 26-27 | SO WHAT | Synthesis: Regulatory Design Evaluation Framework -- 5 questions for assessing any fintech regulatory regime | -- |
| 28 | ACT | Forward look: L05 preview (Personal Finance and Wealth Management) + reflection prompt + course progress bar | -- |
| 29 | Closing | Closing cartoon: "SupTech vs. Traditional Supervision" | 12_closing_cartoon |
| 30 | Takeaways | Key takeaways (7 items) | -- |
| 31 | Summary | Summary + key vocabulary + next lecture | -- |

### Quiz Content Focus

**Standard Quiz (20 questions):**
- Understand (4): What are the three stages of money laundering, what is KYC, what is MiCA, what is a regulatory sandbox
- Apply (8): Identify which US regulator oversees a given fintech scenario, classify a transaction as suspicious based on AML indicators, apply KYC requirements to a customer onboarding scenario, match RegTech capabilities to compliance needs, apply regulatory sandbox rules to a startup scenario, identify which MAS license category a fintech needs, apply PEP screening to a customer profile, match global regulation to jurisdiction
- Analyze (6): Compare innovation-friendly vs. precautionary approaches with evidence, analyze why regulatory arbitrage occurs, break down the compliance cost burden by firm size, analyze the RegTech technology stack components, compare EU MiCA vs. US patchwork approach, analyze digital identity verification advantages/disadvantages
- Evaluate (2): Assess the effectiveness of regulatory sandboxes in promoting innovation, evaluate whether harmonized global regulation is achievable

**Advanced Quiz (20 questions):**
- Apply (4): Apply AML framework to a complex cross-border scenario, design a KYC process for a neobank, apply MiCA classification to a novel token, implement a risk-based approach to transaction monitoring
- Analyze (8): Analyze regulatory arbitrage incentives across jurisdictions, decompose RegTech NLP pipeline for regulatory change detection, compare sandbox outcomes across UK/Singapore/Australia, analyze SupTech adoption barriers, examine CFPB enforcement patterns, break down digital identity verification technologies, analyze compliance cost scaling for startups vs. incumbents, compare AML effectiveness across jurisdictions
- Evaluate (6): Evaluate tradeoffs between sandbox innovation and consumer protection, critique US regulatory patchwork vs. EU unified approach, assess the feasibility of global regulatory harmonization, evaluate AI-powered AML vs. rules-based approaches, assess embedded compliance viability, evaluate privacy implications of comprehensive KYC
- Create (2): Design a multi-jurisdiction compliance framework for a global fintech, propose a SupTech architecture for a central bank

---

## Task Flow and Dependencies

```
Phase 1 (Scaffold) ────> Phase 2-7 (LaTeX, parallel-safe)
                    ├──> Phase 8 (Charts, parallel with LaTeX writing)
                    │
Phase 8 ──────────> Phase 9 (Execute charts)
                    │
Phase 2-5 + Phase 9 > Phase 10 (Compile full/overview/deepdive/core -- need charts)
Phase 6-7 ────────> Phase 10 (Compile mini10/mini5 -- no chart dependency)
                    │
Phase 10 ─────────> Phase 11 (Quizzes, parallel)
                ├──> Phase 12 (Lecture HTML, parallel)
                ├──> Phase 13 (Gallery HTML + PNGs)
                ├──> Phase 14 (Copy PDFs + chart PNGs to docs/)
                │
Phase 11-14 ──────> Phase 15 (Update index.html)
                ├──> Phase 16 (Create AGENTS.md)
                │
Phase 15-16 ──────> Phase 17 (Commit and push)
```

**Parallelization opportunities:**
- Phases 2-7 (all 6 LaTeX files) can be written in parallel
- Phase 8 (chart scripts) can be written in parallel with phases 2-7
- Phase 9 (execute charts) requires phase 8 complete
- Phase 10 (compile) requires phases 2-7 AND phase 9
- Phases 11, 12 can run in parallel after phase 10
- Phase 13 requires phase 10 (needs compiled PDFs for screenshot conversion)
- Phase 14 requires phases 9 + 10

---

## Detailed TODOs

### Phase 1: Create Directory Scaffold

**Create 19 directories:**
```
slides/L04_Fintech_Security_and_Regulation/
slides/L04_Fintech_Security_and_Regulation/01_regulatory_approaches/
slides/L04_Fintech_Security_and_Regulation/02_aml_compliance_flow/
slides/L04_Fintech_Security_and_Regulation/03_kyc_process_flow/
slides/L04_Fintech_Security_and_Regulation/04_money_laundering_stages/
slides/L04_Fintech_Security_and_Regulation/05_us_regulatory_patchwork/
slides/L04_Fintech_Security_and_Regulation/06_global_regulatory_comparison/
slides/L04_Fintech_Security_and_Regulation/07_regtech_stack_architecture/
slides/L04_Fintech_Security_and_Regulation/08_sandbox_adoption_timeline/
slides/L04_Fintech_Security_and_Regulation/09_compliance_cost_comparison/
slides/L04_Fintech_Security_and_Regulation/10_regtech_investment_trends/
slides/L04_Fintech_Security_and_Regulation/11_opening_cartoon/
slides/L04_Fintech_Security_and_Regulation/12_closing_cartoon/
docs/galleries/images/L04/mini5/
docs/galleries/images/L04/mini10/
docs/galleries/images/L04/core/
docs/galleries/images/L04/extended/
docs/galleries/images/L04/full/
docs/slides/images/L04_Fintech_Security_and_Regulation/
```

**Acceptance criteria:**
- All 12 chart subdirectories exist under `slides/L04_Fintech_Security_and_Regulation/`
- All 5 gallery image subdirectories exist under `docs/galleries/images/L04/`
- `docs/slides/images/L04_Fintech_Security_and_Regulation/` exists

---

### Phase 2: Generate L04_full.tex (Flagship)

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/L04_full.tex`

**Structure (match L03_full.tex exactly):**
```
% L04_full.tex -- Lecture 4: Fintech Security and Regulation (Full Variant)
% Frames: 31 | Charts: 12 \includegraphics | Arc: 10-role
% Generated for: Financial Technology (FinTech) -- MSc Course, Spring 2026
\input{../../_shared/preamble.tex}

\subtitle{Navigating Compliance in the Digital Finance Era}

\begin{document}
... 31 frames ...
\end{document}
```

**Frame inventory (31 frames, 12 `\includegraphics`):**

| Frame | Title | Content | Chart |
|-------|-------|---------|-------|
| 1 | Title Page | `\titlepage` | -- |
| 2 | Opening Cartoon | "The Compliance Department's New Hire" | `11_opening_cartoon/cartoon.pdf` |
| 3 | Learning Objectives | 5 objectives, Bloom's tagged | -- |
| 4 | Bridge from L03 | L03 payment regulation (PSD2, interchange caps) was specific -- now the broader landscape | `01_regulatory_approaches/chart.pdf` |
| 5 | The Surveillance Paradox | Personal: "Your bank knows more about you than your doctor -- protection or surveillance?" | -- |
| 6 | Innovation-Friendly vs. Precautionary Approaches | Two philosophical poles: UK/Singapore (sandbox-first, fail-fast) vs. EU/China (rule-first, prevent-harm) | -- |
| 7 | Regulatory Objectives | Four goals: financial stability, consumer protection, competition, innovation -- and why they conflict | `01_regulatory_approaches/chart.pdf` |
| 8 | The Regulatory Trilemma | You can optimize for 2 of 3: innovation speed, consumer safety, financial stability | -- |
| 9 | Global Regulatory Spectrum | Where each major jurisdiction sits on the innovation-caution spectrum | `06_global_regulatory_comparison/chart.pdf` |
| 10 | The Three Stages of Money Laundering | Placement, layering, integration with examples and detection difficulty | `04_money_laundering_stages/chart.pdf` |
| 11 | Know Your Customer (KYC) | Full KYC lifecycle: application -> verification -> screening -> rating -> monitoring | `03_kyc_process_flow/chart.pdf` |
| 12 | Digital Identity Verification | eKYC technologies: biometrics, document AI, liveness detection, digital identity wallets | -- |
| 13 | Transaction Monitoring and SAR Filing | End-to-end AML compliance pipeline | `02_aml_compliance_flow/chart.pdf` |
| 14 | US Fintech Regulation: The Federal Layer | OCC, SEC, CFTC, CFPB, FinCEN -- who regulates what | `05_us_regulatory_patchwork/chart.pdf` |
| 15 | US Fintech Regulation: The State Layer | 50-state patchwork, money transmitter licenses, the OCC fintech charter debate | -- |
| 16 | SEC vs. CFTC: The Digital Asset Divide | Howey test, commodity vs. security, enforcement actions | -- |
| 17 | CFPB and Consumer Protection | Fintech-specific enforcement, buy-now-pay-later scrutiny, data privacy | -- |
| 18 | EU MiCA Regulation | Markets in Crypto-Assets: classification, licensing, stablecoin requirements | `06_global_regulatory_comparison/chart.pdf` |
| 19 | UK FCA Regulatory Sandbox | How sandboxes work, cohort structure, graduation rates, outcomes | -- |
| 20 | Singapore MAS Framework | MAS licensing tiers, Payment Services Act, fintech festivals, global partnerships | -- |
| 21 | RegTech: Automated Compliance | Technology stack: data ingestion, ML processing, analytics, reporting, audit | `07_regtech_stack_architecture/chart.pdf` |
| 22 | NLP for Regulatory Change Management | How NLP parses regulatory updates, maps obligations, alerts compliance teams | -- |
| 23 | The Compliance Cost Burden | Why compliance costs hit small firms hardest -- and how RegTech can level the field | `09_compliance_cost_comparison/chart.pdf` |
| 24 | Regulatory Sandboxes Worldwide | Timeline of sandbox launches, design variations, success metrics | `08_sandbox_adoption_timeline/chart.pdf` |
| 25 | SupTech: The Regulator's AI | How central banks and supervisors use technology: market surveillance, stress testing, reporting analytics | -- |
| 26 | Embedded Compliance and Harmonization | Compliance-as-a-service, API-first regulation, global harmonization efforts | `10_regtech_investment_trends/chart.pdf` |
| 27 | A Regulatory Evaluation Framework | 5 questions: Does it protect consumers? Foster innovation? Maintain stability? Scale globally? Adapt to change? | -- |
| 28 | What Comes Next | L05 preview (Personal Finance and Wealth Management) + reflection prompt + course progress bar | -- |
| 29 | Closing Cartoon | "SupTech vs. Traditional Supervision" | `12_closing_cartoon/cartoon.pdf` |
| 30 | Key Takeaways | 7 key points | -- |
| 31 | Summary and Key Vocabulary | Summary paragraph + 10 vocabulary terms + next lecture | -- |

**Critical patterns to replicate:**
- Header comment: `% L04_full.tex -- Lecture 4: Fintech Security and Regulation (Full Variant)`
- `\input{../../_shared/preamble.tex}` on line 4
- `\subtitle{Navigating Compliance in the Digital Finance Era}`
- `\bottomnote{...}` on every frame
- `\textcolor{mlpurple}{...}` for emphasis
- `\textcolor{mlred}{...}` for risks/warnings
- `\begin{columns}[T]` layout for chart+text frames (50/47 split like L03)
- `\includegraphics[width=\textwidth]{01_regulatory_approaches/chart.pdf}` (bare relative paths)
- `\begin{exampleblock}`, `\begin{alertblock}`, `\begin{block}` usage
- Course progress bar in frame 28 (L01 + L02 + L03 checked, L04 bold)
- Bottom note of final frame: reference to L05

**Acceptance criteria:**
- Exactly 31 `\begin{frame}` blocks
- At least 12 `\includegraphics` commands (some charts reused across frames; count should match frame inventory)
- All `\includegraphics` paths use bare relative format (no `figures/` prefix)
- `\input{../../_shared/preamble.tex}` present
- Every frame has a `\bottomnote{}`
- Bridge frame references L03
- Forward-look frame previews L05

---

### Phase 3: Generate L04_overview.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/L04_overview.tex`

**Pattern (from L03_overview.tex):**
```
% L04_overview.tex -- Lecture 4: Fintech Security and Regulation (Overview Variant)
% Frames: ~27 | Charts: subset of 12 | Architecture: INTRO/CORE/CLOSING
\input{../../_shared/preamble.tex}
\subtitle{Navigating Compliance in the Digital Finance Era}
```

**Structure:** ~25-30 frames. Three-zone architecture (INTRO / CORE / CLOSING). Uses a subset of the 12 charts (approximately 8-10). Includes section commands (`\section{Introduction}`, etc.).

**Acceptance criteria:**
- 25-30 `\begin{frame}` blocks
- Uses `\input{../../_shared/preamble.tex}`
- Has `\section{}` commands for zone organization
- Includes opening and closing cartoons
- Uses subset of charts via `\includegraphics`
- All paths bare relative

---

### Phase 4: Generate L04_deepdive.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/L04_deepdive.tex`

**Pattern (from L03_deepdive.tex):**
```
% L04_deepdive.tex -- Lecture 4: Fintech Security and Regulation (Deep Dive Variant)
% Frame count: ~12 main body + ~5 appendix = ~17 total
% Architecture: MAIN BODY + \appendix
\input{../../_shared/preamble.tex}
\subtitle{Navigating Compliance in the Digital Finance Era --- Deep Dive}
```

**Focus areas for deep dive:**
- AML enforcement effectiveness: comparing rules-based vs. ML-based transaction monitoring
- Regulatory arbitrage game theory: why firms forum-shop and how regulators respond
- MiCA deep analysis: token classification framework, stablecoin reserve requirements, DeFi implications
- SupTech architecture: how central banks deploy ML for market surveillance and stress testing
- Cross-jurisdiction compliance: building a multi-regulatory compliance engine
- Privacy vs. surveillance: GDPR tension with AML/KYC obligations

**Acceptance criteria:**
- 15-20 `\begin{frame}` blocks total
- Has `\appendix` section with supplementary analytical frames
- Advanced learning objectives targeting Analyze/Evaluate/Create Bloom's levels
- Uses `\input{../../_shared/preamble.tex}`
- Includes subset of charts

---

### Phase 5: Extract L04_core.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/L04_core.tex`

**Pattern (from L03_core.tex -- SELF-CONTAINED):**
```
% L04_core.tex -- Fintech Security and Regulation
% Core Slides (10 frames)
% Self-contained (no \input{} commands)
% Compile: pdflatex L04_core.tex (twice for overlays)

\documentclass[aspectratio=169, 11pt]{beamer}
\usetheme{Madrid}
\usecolortheme{whale}
\usepackage{tikz,pgfplots,booktabs,multicol,amsmath,graphicx}
...
% Full inline color definitions (mlpurple, mlblue, mlred, mlorange, mlgreen, mlgray, mlteal, mlcyan)
% Full beamer color settings
% \bottomnote command definition
% \graphicspath{{}}
% Metadata (title, subtitle, author, institute, date)
```

**Content:** Extract the 10 most essential frames from L04_full covering: bridge from L03, regulatory approaches comparison, money laundering stages, KYC process, US regulatory patchwork, global regulatory comparison (MiCA focus), RegTech stack, compliance cost burden, regulatory evaluation framework, key takeaways.

**Critical:** Uses `\includegraphics` for charts (unlike mini variants). Has `\graphicspath{{}}` and can reference chart subdirectories.

**Acceptance criteria:**
- Exactly 10 `\begin{frame}` blocks
- NO `\input{}` commands anywhere
- Full inline preamble (documentclass, usepackage, colors, beamer settings, bottomnote command)
- Has `\graphicspath{{}}`
- Can include `\includegraphics` for charts
- Compiles standalone without any external dependencies

---

### Phase 6: Generate L04_mini10.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/L04_mini10.tex`

**Pattern (from L03_mini10.tex -- SELF-CONTAINED, NO \includegraphics):**
```
% L04_mini10.tex -- Fintech Security and Regulation
% 10-Slide Arc: WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT
% Self-contained (no \input{} commands, no \includegraphics)
```

**Arc:** WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT
- Title frame (not counted in the 10)
- Frame 1 (WHY): TikZ comic -- compliance officer drowning in stacked regulation documents, with a small drone hovering above labeled "RegTech"
- Frame 2 (FEEL): Text prompt -- "How many compliance rules does your bank follow? (Hint: thousands)"
- Frame 3 (WHAT): Table -- regulatory approaches comparison (innovation-friendly vs. precautionary) across 5 jurisdictions
- Frame 4 (CASE): TikZ diagram -- money laundering three-stage flow (placement -> layering -> integration)
- Frame 5 (HOW): TikZ flow -- KYC process lifecycle (application -> verification -> screening -> monitoring)
- Frame 6 (RISK): TikZ comic -- fintech startup looking at a map of US with 50 different license requirements
- Frame 7 (WHERE): pgfplots bar chart -- global regulatory comparison (sandbox availability, crypto framework, AML rigor by country, illustrative)
- Frame 8 (IMPACT): TikZ diagram -- RegTech technology stack (data -> processing -> analytics -> reporting)
- Frame 9 (SO WHAT): Evaluation checklist -- 5 questions for any regulatory framework
- Frame 10 (ACT): Activity + next lecture preview (L05: Personal Finance and Wealth Management)

**Critical:** All visuals are pure TikZ/pgfplots inline. NO `\includegraphics`. NO external file dependencies.

**Acceptance criteria:**
- Title frame + exactly 10 content frames
- NO `\input{}` commands
- NO `\includegraphics` commands
- All diagrams drawn inline with TikZ or pgfplots
- Full inline preamble
- Arc labels in bottomnotes: "Slide X/10 -- ARC_ROLE | ..."
- Compiles completely standalone

---

### Phase 7: Generate L04_mini5.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/L04_mini5.tex`

**Pattern (from L03_mini5.tex -- SELF-CONTAINED, NO \includegraphics):**
```
% L04_mini5.tex -- Fintech Security and Regulation
% 5-Slide Teaser Arc: WHY > WHAT > HOW > WHERE > SO WHAT
% Self-contained (no \input{} commands, no \includegraphics)
```

**Arc:** WHY > WHAT > HOW > WHERE > SO WHAT
- Title frame (not counted in the 5)
- Slide 1 (WHY): TikZ comic -- balance scale with "Innovation" on one side and "Regulation" on the other, slightly tipping
- Slide 2 (WHAT): Table comparing regulatory approaches: US (patchwork), EU (MiCA), UK (sandbox), Singapore (licensing tiers)
- Slide 3 (HOW): TikZ diagram -- money laundering stages simplified (placement -> layering -> integration)
- Slide 4 (WHERE): pgfplots bar chart -- illustrative compliance costs by firm type (large bank, fintech, neobank, crypto exchange)
- Slide 5 (SO WHAT): Evaluation framework for regulatory regimes + RegTech promise

**Acceptance criteria:**
- Title frame + exactly 5 content frames
- NO `\input{}` commands
- NO `\includegraphics` commands
- All visuals inline TikZ/pgfplots
- Arc labels in bottomnotes: "Slide X/5 -- ARC_ROLE | ..."
- Compiles completely standalone

---

### Phase 8: Generate 12 Chart Scripts

**For each of the 10 chart scripts (`chart.py`):**

**Template pattern (from L03 01_payment_history_timeline/chart.py):**
```python
"""
Figure XX: [Title]
[Description]
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

try:
    from chart_styles import V4_COLORS, apply_v4_style, save_chart
except ImportError:
    V4_COLORS = {
        'MLPURPLE': '#9467BD', 'MLBLUE': '#1F77B4', 'MLRED': '#D62728',
        'MLORANGE': '#FF7F0E', 'MLGREEN': '#2CA02C', 'MLGRAY': '#7F7F7F',
        'MLTEAL': '#0D7377', 'MLCYAN': '#14BDEB', 'MLYELLOW': '#BCBD22',
        'MLPINK': '#E377C2', 'MLBROWN': '#8C564B',
    }
    def apply_v4_style(ax, title='', xlabel='', ylabel=''):
        ...
    def save_chart(fig, filename='chart.pdf', dpi=300):
        ...

CHART_METADATA = {
    'title': '...',
    'type': '...',
    'section': '...',
    'lecture_number': 4,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
np.random.seed(42)
# ... chart code ...

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
```

**For each of the 2 cartoon scripts (`cartoon.py`):**

**Template pattern (from L03 11_opening_cartoon/cartoon.py):**
```python
"""
Figure XX: [Title]
[Description]
"""
# ... same imports and fallback ...

CHART_METADATA = {
    'title': '...',
    'type': 'cartoon',
    'section': 'Opening'/'Closing',
    'lecture_number': 4,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    # ... cartoon code ...

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
```

**Chart-specific content guide:**

| # | Script | Key visualization elements |
|---|--------|---------------------------|
| 01 | `01_regulatory_approaches/chart.py` | Grouped bar chart: 5 countries x 5 dimensions (innovation speed, consumer protection, etc.), color-coded by dimension |
| 02 | `02_aml_compliance_flow/chart.py` | Horizontal flowchart with boxes and arrows: 7-stage AML pipeline, color-coded by phase (onboarding=blue, monitoring=orange, reporting=red) |
| 03 | `03_kyc_process_flow/chart.py` | Vertical flowchart: KYC lifecycle stages with branching for manual vs. digital paths, timing annotations |
| 04 | `04_money_laundering_stages/chart.py` | Three-column diagram: placement, layering, integration with example methods and detection difficulty heat coloring |
| 05 | `05_us_regulatory_patchwork/chart.py` | Organizational diagram: two tiers (federal, state) with agency boxes, jurisdiction lines, and overlap indicators |
| 06 | `06_global_regulatory_comparison/chart.py` | Heat-map style comparison matrix: 6 jurisdictions x 5 regulatory dimensions, scored 1-5 with color gradient |
| 07 | `07_regtech_stack_architecture/chart.py` | Layered architecture diagram: 5 horizontal layers stacked vertically with technology labels and data flow arrows |
| 08 | `08_sandbox_adoption_timeline/chart.py` | Timeline with event markers: sandbox launches 2016-2025, with cumulative count line overlay |
| 09 | `09_compliance_cost_comparison/chart.py` | Horizontal bar chart: 5 firm types showing compliance cost as % of revenue, sorted by burden |
| 10 | `10_regtech_investment_trends/chart.py` | Dual-axis time series: bar chart for investment volume + line for deal count, with annotated regulatory milestones |
| 11 | `11_opening_cartoon/cartoon.py` | XKCD-style: stick figure at desk with paper mountain, small robot on desk |
| 12 | `12_closing_cartoon/cartoon.py` | XKCD-style: human with magnifying glass vs. AI with multiple screens, speech bubbles |

**Acceptance criteria per script:**
- Imports match L03 pattern exactly (sys.path.insert, matplotlib.use('Agg'), try/except)
- Has CHART_METADATA dict with lecture_number: 4
- Uses `np.random.seed(42)` for any random data
- Charts use `figsize=(10, 6)`, cartoons use `figsize=(12, 6)`
- Output path uses `os.path.join(os.path.dirname(__file__), 'chart.pdf')` or `'cartoon.pdf'`
- All data is conceptual/illustrative (no real market data)
- Executes without errors and produces valid PDF

---

### Phase 9: Execute All Chart Scripts

**Commands (run from project root):**
```bash
cd D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation
for dir in 01_* 02_* 03_* 04_* 05_* 06_* 07_* 08_* 09_* 10_*; do
    python "$dir/chart.py"
done
python 11_opening_cartoon/cartoon.py
python 12_closing_cartoon/cartoon.py
```

**Acceptance criteria:**
- All 12 scripts exit with code 0
- Each produces a .pdf file in its subdirectory
- Each .pdf file is > 0 bytes
- Output includes "Saved: ..." for each

---

### Phase 10: Compile All 6 .tex Files

**Commands (run from `slides/L04_Fintech_Security_and_Regulation/`):**
```bash
# Full, Overview, Deepdive (depend on _shared/preamble.tex AND chart PDFs)
pdflatex L04_full.tex && pdflatex L04_full.tex
pdflatex L04_overview.tex && pdflatex L04_overview.tex
pdflatex L04_deepdive.tex && pdflatex L04_deepdive.tex

# Core (depends on chart PDFs but not preamble)
pdflatex L04_core.tex && pdflatex L04_core.tex

# Mini10, Mini5 (no external dependencies)
pdflatex L04_mini10.tex && pdflatex L04_mini10.tex
pdflatex L04_mini5.tex && pdflatex L04_mini5.tex
```

**Acceptance criteria:**
- All 6 produce .pdf files
- No fatal LaTeX errors (warnings about overful hbox are acceptable)
- Each PDF has correct number of pages (frames + 0-1 for title)
- Charts are visible in full/overview/deepdive/core PDFs

---

### Phase 11: Generate Quiz HTML Files

**File 1:** `D:/Joerg/Research/slides/Fintech/docs/quiz/L04_quiz.html`
**File 2:** `D:/Joerg/Research/slides/Fintech/docs/quiz/L04_quiz_advanced.html`

**Pattern (from L03_quiz.html):**
- Full inline CSS with same `:root` variables (--nav-bg, --hero-from, etc.)
- Navbar with links to: index.html, L04.html, L04_gallery.html, L04_quiz.html, L04_quiz_advanced.html
- Hero section with gradient background
- 20 questions, each with:
  - Question number and Bloom's level badge
  - 4 answer options (radio buttons)
  - "Check Answer" button
  - Correct/incorrect feedback with explanation
- Score tracker at bottom
- All inline JS (no external scripts)

**Standard quiz Bloom's distribution:**
| Level | Count | Color Variable |
|-------|-------|----------------|
| Understand | 4 | --bloom-u (#2CA02C) |
| Apply | 8 | --bloom-ap (#1F77B4) |
| Analyze | 6 | --bloom-an (#FF7F0E) |
| Evaluate | 2 | --bloom-ev (#D62728) |

**Advanced quiz Bloom's distribution:**
| Level | Count | Color Variable |
|-------|-------|----------------|
| Apply | 4 | --bloom-ap (#1F77B4) |
| Analyze | 8 | --bloom-an (#FF7F0E) |
| Evaluate | 6 | --bloom-ev (#D62728) |
| Create | 2 | --bloom-cr (#9467BD) |

**Topic coverage (both quizzes combined):**
- Regulatory approaches: innovation-friendly vs. precautionary
- The regulatory trilemma
- Money laundering stages (placement, layering, integration)
- KYC process and digital identity verification
- Transaction monitoring and SAR filing
- US regulatory patchwork (OCC, SEC, CFTC, CFPB, FinCEN)
- OCC fintech charter and its controversies
- SEC vs. CFTC jurisdiction over digital assets
- EU MiCA regulation framework
- UK FCA regulatory sandbox design and outcomes
- Singapore MAS licensing framework
- Regulatory arbitrage and forum shopping
- RegTech technology stack components
- NLP for regulatory change management
- Compliance cost burden by firm size
- SupTech and supervisory technology
- Regulatory sandboxes worldwide
- Embedded compliance and compliance-as-a-service
- NO coding questions

**Acceptance criteria:**
- Each file has exactly 20 question blocks
- Bloom's distribution matches spec
- All questions relate to L04 regulation/compliance/RegTech topics
- No coding/programming questions
- Inline CSS/JS (no external dependencies)
- Navbar links are correct for L04
- Score calculation works (manual browser test)

---

### Phase 12: Generate L04.html Lecture Page

**File:** `D:/Joerg/Research/slides/Fintech/docs/lectures/L04.html`

**Pattern (from L03.html):**
- Same CSS design system (Crimson Pro + Source Sans 3 fonts, same :root variables)
- KaTeX for math rendering
- Sticky navbar with L04-specific links
- Hero section: L04 title, subtitle, description
- Sidebar navigation (8 sections)
- 8 content sections covering all L04 topics:
  1. Overview (bridge from L03, course context)
  2. Regulatory Perspectives (innovation vs. precaution, trilemma)
  3. AML and KYC (money laundering stages, KYC lifecycle, digital identity)
  4. US Fintech Regulation (federal vs. state, OCC charter, SEC/CFTC, CFPB)
  5. Global Regulatory Landscape (MiCA, FCA sandbox, MAS, regulatory arbitrage)
  6. RegTech Solutions (automated compliance, NLP, real-time surveillance, reporting)
  7. Looking Forward (sandboxes, embedded compliance, SupTech, harmonization)
  8. Key Takeaways and Vocabulary
- Each section: ~300-500 words, educational prose, key terms bolded
- Info boxes, callout boxes, alert boxes matching L03 style
- Footer

**Acceptance criteria:**
- HTML validates (no unclosed tags)
- 8 sidebar navigation links work
- All internal links functional
- Navbar links correct for L04
- Content covers all 6 L04 topics comprehensively
- No placeholder text

---

### Phase 13: Generate L04_gallery.html + Gallery PNGs

**File:** `D:/Joerg/Research/slides/Fintech/docs/galleries/L04_gallery.html`

**Pattern (from L03_gallery.html):**
- 5 tabs: Mini 5, Mini 10, Core, Extended (overview), Full
- Each tab shows slide images as a scrollable gallery
- Tab switching via inline JS
- Same CSS design system

**PNG generation (pdftoppm at 200 DPI):**
```bash
# Convert each PDF variant to PNGs for gallery
pdftoppm -png -r 200 L04_mini5.pdf docs/galleries/images/L04/mini5/slide
pdftoppm -png -r 200 L04_mini10.pdf docs/galleries/images/L04/mini10/slide
pdftoppm -png -r 200 L04_core.pdf docs/galleries/images/L04/core/slide
pdftoppm -png -r 200 L04_overview.pdf docs/galleries/images/L04/extended/slide
pdftoppm -png -r 200 L04_full.pdf docs/galleries/images/L04/full/slide
```

**Gallery image naming:**
- mini5: `slide-1.png` through `slide-6.png` (no zero-padding, 5+title = 6 pages)
- mini10: `slide-01.png` through `slide-11.png` (zero-padded, 10+title = 11 pages)
- core: `slide-01.png` through `slide-10.png` (zero-padded)
- extended: `slide-01.png` through `slide-XX.png` (zero-padded, ~28 pages)
- full: `slide-01.png` through `slide-31.png` (zero-padded)

**Acceptance criteria:**
- Gallery HTML has 5 working tabs
- PNG images exist in all 5 subdirectories
- Tab switching shows correct images
- Images are legible at gallery size

---

### Phase 14: Copy PDFs and Chart PNGs to docs/

**PDF copies:**
```bash
cp slides/L04_Fintech_Security_and_Regulation/L04_full.pdf docs/slides/pdf/
cp slides/L04_Fintech_Security_and_Regulation/L04_overview.pdf docs/slides/pdf/
cp slides/L04_Fintech_Security_and_Regulation/L04_deepdive.pdf docs/slides/pdf/
cp slides/L04_Fintech_Security_and_Regulation/L04_core.pdf docs/slides/pdf/
cp slides/L04_Fintech_Security_and_Regulation/L04_mini10.pdf docs/slides/pdf/
cp slides/L04_Fintech_Security_and_Regulation/L04_mini5.pdf docs/slides/pdf/
```

**Chart PNG conversions (for docs/slides/images/):**
Convert each chart.pdf/cartoon.pdf to .png and copy to `docs/slides/images/L04_Fintech_Security_and_Regulation/`:
```
regulatory_approaches.png
aml_compliance_flow.png
kyc_process_flow.png
money_laundering_stages.png
us_regulatory_patchwork.png
global_regulatory_comparison.png
regtech_stack_architecture.png
sandbox_adoption_timeline.png
compliance_cost_comparison.png
regtech_investment_trends.png
opening_cartoon.png
closing_cartoon.png
```

**Acceptance criteria:**
- 6 PDFs in `docs/slides/pdf/` matching names `L04_*.pdf`
- 12 PNGs in `docs/slides/images/L04_Fintech_Security_and_Regulation/`
- All files > 0 bytes

---

### Phase 15: Update docs/index.html

**File:** `D:/Joerg/Research/slides/Fintech/docs/index.html`

**Changes required:**

1. **L04 lecture card (lines ~806-836):** Change from `coming-soon` to `available` with active links and CORRECTED title.

Replace the entire L04 card block:
- `class="lecture-card coming-soon"` -> `class="lecture-card available"`
- `class="status-badge coming-soon"` -> `class="status-badge available"`
- `Coming Soon` -> `Available`
- Title: change from "Digital Lending and Credit" to "Fintech Security and Regulation"
- Description: update to "Regulatory approaches, AML/KYC compliance, US and global regulation, RegTech solutions, and supervisory technology."
- Replace all `<span class="link-pill disabled">` with `<a href="..." class="link-pill ...">` (matching L03 pattern exactly -- same SVG icons)
- Links:
  - Lecture: `lectures/L04.html`
  - Gallery: `galleries/L04_gallery.html`
  - Quiz: `quiz/L04_quiz.html`
  - Advanced Quiz: `quiz/L04_quiz_advanced.html`
  - Download PDF: `slides/pdf/L04_full.pdf`

2. **Downloads section (after L03 block, ~line 1041):** Add L04 download block:
```html
<!-- L04 Downloads -->
<div class="download-block">
  <p class="download-block-label">Lecture 04 — Fintech Security and Regulation</p>
  <div class="download-pills">
    <a href="slides/pdf/L04_full.pdf" class="dl-pill">
      <svg viewBox="0 0 13 13" fill="currentColor" aria-hidden="true"><path d="M6.5 1a.5.5 0 01.5.5v5.79l1.65-1.65a.5.5 0 01.7.7l-2.5 2.5a.5.5 0 01-.7 0l-2.5-2.5a.5.5 0 11.7-.7L6 7.29V1.5a.5.5 0 01.5-.5zM1 10a.5.5 0 011 0v.5h9V10a.5.5 0 011 0v.5a1 1 0 01-1 1H2a1 1 0 01-1-1V10z"/></svg>
      L04 Full <span class="dl-variant">full</span>
    </a>
    <a href="slides/pdf/L04_overview.pdf" class="dl-pill">
      <svg viewBox="0 0 13 13" fill="currentColor" aria-hidden="true"><path d="M6.5 1a.5.5 0 01.5.5v5.79l1.65-1.65a.5.5 0 01.7.7l-2.5 2.5a.5.5 0 01-.7 0l-2.5-2.5a.5.5 0 11.7-.7L6 7.29V1.5a.5.5 0 01.5-.5zM1 10a.5.5 0 011 0v.5h9V10a.5.5 0 011 0v.5a1 1 0 01-1 1H2a1 1 0 01-1-1V10z"/></svg>
      L04 Overview <span class="dl-variant">overview</span>
    </a>
    <a href="slides/pdf/L04_deepdive.pdf" class="dl-pill">
      <svg viewBox="0 0 13 13" fill="currentColor" aria-hidden="true"><path d="M6.5 1a.5.5 0 01.5.5v5.79l1.65-1.65a.5.5 0 01.7.7l-2.5 2.5a.5.5 0 01-.7 0l-2.5-2.5a.5.5 0 11.7-.7L6 7.29V1.5a.5.5 0 01.5-.5zM1 10a.5.5 0 011 0v.5h9V10a.5.5 0 011 0v.5a1 1 0 01-1 1H2a1 1 0 01-1-1V10z"/></svg>
      L04 Deep Dive <span class="dl-variant">deepdive</span>
    </a>
    <a href="slides/pdf/L04_core.pdf" class="dl-pill">
      <svg viewBox="0 0 13 13" fill="currentColor" aria-hidden="true"><path d="M6.5 1a.5.5 0 01.5.5v5.79l1.65-1.65a.5.5 0 01.7.7l-2.5 2.5a.5.5 0 01-.7 0l-2.5-2.5a.5.5 0 11.7-.7L6 7.29V1.5a.5.5 0 01.5-.5zM1 10a.5.5 0 011 0v.5h9V10a.5.5 0 011 0v.5a1 1 0 01-1 1H2a1 1 0 01-1-1V10z"/></svg>
      L04 Core <span class="dl-variant">core</span>
    </a>
    <a href="slides/pdf/L04_mini10.pdf" class="dl-pill">
      <svg viewBox="0 0 13 13" fill="currentColor" aria-hidden="true"><path d="M6.5 1a.5.5 0 01.5.5v5.79l1.65-1.65a.5.5 0 01.7.7l-2.5 2.5a.5.5 0 01-.7 0l-2.5-2.5a.5.5 0 11.7-.7L6 7.29V1.5a.5.5 0 01.5-.5zM1 10a.5.5 0 011 0v.5h9V10a.5.5 0 011 0v.5a1 1 0 01-1 1H2a1 1 0 01-1-1V10z"/></svg>
      L04 Mini 10 <span class="dl-variant">mini10</span>
    </a>
    <a href="slides/pdf/L04_mini5.pdf" class="dl-pill">
      <svg viewBox="0 0 13 13" fill="currentColor" aria-hidden="true"><path d="M6.5 1a.5.5 0 01.5.5v5.79l1.65-1.65a.5.5 0 01.7.7l-2.5 2.5a.5.5 0 01-.7 0l-2.5-2.5a.5.5 0 11.7-.7L6 7.29V1.5a.5.5 0 01.5-.5zM1 10a.5.5 0 011 0v.5h9V10a.5.5 0 011 0v.5a1 1 0 01-1 1H2a1 1 0 01-1-1V10z"/></svg>
      L04 Mini 5 <span class="dl-variant">mini5</span>
    </a>
  </div>
</div>
```

**Acceptance criteria:**
- L04 card shows "Available" status badge
- L04 card title reads "Fintech Security and Regulation" (NOT "Digital Lending and Credit")
- All 5 link pills are clickable `<a>` tags (not disabled `<span>`)
- Links point to correct L04 URLs
- Download block appears after L03 block with all 6 variants
- SVG icons match L03 pattern exactly
- HTML structure matches L03 card exactly

---

### Phase 16: Create AGENTS.md for L04

**File:** `D:/Joerg/Research/slides/Fintech/slides/L04_Fintech_Security_and_Regulation/AGENTS.md`

**Pattern (from L03 AGENTS.md):**
- Header: `# L04: Fintech Security and Regulation`
- Parent reference: `<!-- Parent: ../AGENTS.md -->`
- Overview section with core themes
- Directory structure (all 12 chart dirs + 6 tex + 6 pdf + AGENTS.md)
- Key files table
- Variants guide (For Instructors / For Self-Study / For Outreach)
- Graphics & Figures (12 total: 10 charts + 2 cartoons with descriptions)
- Generation & Compilation instructions
- Instructional Goals (5 learning objectives, Bloom's tagged)
- Integration Points (links from L03, links to L05)
- File Maintenance notes
- Notes for Developers

**Core themes for overview:**
- Regulatory approaches: innovation-friendly vs. precautionary
- AML/KYC: compliance processes and digital identity
- US regulatory patchwork: federal and state jurisdictions
- Global regulatory frameworks: MiCA, FCA sandbox, MAS licensing
- RegTech solutions: automated compliance, NLP, real-time surveillance
- Future: sandboxes, SupTech, embedded compliance, harmonization

**Acceptance criteria:**
- Matches L03 AGENTS.md structure section-by-section
- All 12 chart directories listed with descriptions
- All 6 variants listed with frame counts
- Correct lecture number (4) throughout
- References L03 (previous) and L05 (next) correctly

---

### Phase 17: Commit and Push

**Commit strategy:**
```
git add slides/L04_Fintech_Security_and_Regulation/
git add docs/lectures/L04.html
git add docs/galleries/L04_gallery.html
git add docs/galleries/images/L04/
git add docs/quiz/L04_quiz.html
git add docs/quiz/L04_quiz_advanced.html
git add docs/slides/pdf/L04_*.pdf
git add docs/slides/images/L04_Fintech_Security_and_Regulation/
git add docs/index.html

git commit -m "Add L04: Fintech Security and Regulation -- RegTech

Complete lecture materials including:
- 6 LaTeX variants (full, overview, deepdive, core, mini10, mini5)
- 12 matplotlib charts (10 analytical + 2 XKCD cartoons)
- Standard and advanced quizzes (20 questions each)
- Lecture page, gallery page, and gallery images
- docs/index.html updated: L04 available with download pills, title corrected"

git push
```

**Acceptance criteria:**
- All new files tracked
- No untracked L04 files left behind
- Commit message describes scope
- Push succeeds

---

## Success Criteria (Final Verification Checklist)

| # | Check | Method |
|---|-------|--------|
| 1 | 12 chart subdirectories exist | `ls slides/L04_Fintech_Security_and_Regulation/` |
| 2 | 12 chart/cartoon PDFs generated | `ls slides/L04_Fintech_Security_and_Regulation/*/chart.pdf slides/L04_Fintech_Security_and_Regulation/*/cartoon.pdf` |
| 3 | 6 compiled slide PDFs exist | `ls slides/L04_Fintech_Security_and_Regulation/L04_*.pdf` |
| 4 | Frame counts correct | Open each PDF, count slides |
| 5 | No LaTeX compilation errors | Check .log files for `Fatal error` |
| 6 | All \includegraphics resolve | No "File not found" in .log |
| 7 | 6 PDFs copied to docs/slides/pdf/ | `ls docs/slides/pdf/L04_*.pdf` |
| 8 | 12 chart PNGs in docs/slides/images/ | `ls docs/slides/images/L04_Fintech_Security_and_Regulation/` |
| 9 | Gallery images in 5 subdirs | `ls docs/galleries/images/L04/` |
| 10 | L04_quiz.html has 20 questions | Count question blocks |
| 11 | L04_quiz_advanced.html has 20 questions | Count question blocks |
| 12 | L04.html has 8 sections | Count section headers |
| 13 | L04_gallery.html has 5 tabs | Check tab elements |
| 14 | index.html shows L04 as Available | Check class attribute |
| 15 | index.html L04 title is "Fintech Security and Regulation" | Not "Digital Lending and Credit" |
| 16 | index.html has L04 download block | Search for "L04" in downloads section |
| 17 | AGENTS.md present and complete | Read file, check all sections |
| 18 | No `\input{}` in core/mini10/mini5 | grep for \input in those files |
| 19 | No `\includegraphics` in mini10/mini5 | grep for \includegraphics in those files |
| 20 | All quiz questions are non-coding | Manual review |
| 21 | Bloom's distribution correct | Count badges by level |

---

## Execution Notes

**Recommended agent assignments:**
- Phase 1 (scaffold): executor-low (simple mkdir)
- Phases 2-7 (LaTeX): executor-high (complex content generation, one per file)
- Phase 8 (charts): executor (12 parallel chart scripts)
- Phase 9 (execute charts): executor-low (run scripts)
- Phase 10 (compile): executor-low (run pdflatex)
- Phase 11 (quizzes): executor (HTML generation, 2 files)
- Phase 12 (lecture HTML): executor (complex HTML)
- Phase 13 (gallery): executor (HTML + pdftoppm)
- Phase 14 (copy): executor-low (file copies)
- Phase 15 (index.html): executor (surgical HTML edit)
- Phase 16 (AGENTS.md): writer (documentation)
- Phase 17 (commit): executor-low (git operations)

**Known index.html discrepancy:** The L05 card in index.html currently shows "Regulation and Compliance" which is an outdated/incorrect title. L04's forward-look frame correctly references L05 as "Personal Finance and Wealth Management" per the course plan (config.yaml). Do NOT change the L04 forward-look text to match the incorrect L05 card -- that will be fixed when L05 is built.

**Critical reference files for executors:**
- L03_full.tex: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_full.tex`
- L03_core.tex: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_core.tex`
- L03_mini10.tex: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_mini10.tex`
- L03_mini5.tex: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_mini5.tex`
- L03 chart.py example: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/01_payment_history_timeline/chart.py`
- L03 cartoon.py example: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/11_opening_cartoon/cartoon.py`
- L03_quiz.html: `D:/Joerg/Research/slides/Fintech/docs/quiz/L03_quiz.html`
- L03.html: `D:/Joerg/Research/slides/Fintech/docs/lectures/L03.html`
- L03_gallery.html: `D:/Joerg/Research/slides/Fintech/docs/galleries/L03_gallery.html`
- index.html: `D:/Joerg/Research/slides/Fintech/docs/index.html` (lines 806-836 for L04 card, lines 1012-1041 for L03 download block to copy pattern)
- L03 AGENTS.md: `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/AGENTS.md`
- _shared/preamble.tex: `D:/Joerg/Research/slides/Fintech/_shared/preamble.tex`
- _shared/chart_styles.py: `D:/Joerg/Research/slides/Fintech/_shared/chart_styles.py`
