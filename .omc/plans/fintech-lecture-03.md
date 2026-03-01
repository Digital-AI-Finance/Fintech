# Execution Plan: Lecture 3 -- Payments and Fintech

**Plan ID:** fintech-lecture-03
**Created:** 2026-03-01
**Status:** READY FOR EXECUTION
**Complexity:** HIGH (17 phases, ~50 deliverable files)

---

## Context

### Original Request
Create Lecture 3 (Payments and Fintech) for the MSc-level Financial Technology course at University of Zurich. L01 and L02 are complete and deployed. L03 must follow their exact patterns.

### Research Findings (from codebase exploration)

**Verified L02 patterns (L03 must match):**

| Pattern | L02 Value | L03 Must Match |
|---------|-----------|----------------|
| Full tex frames | 31 | ~31 |
| Overview tex frames | ~27 | ~25-30 |
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

**Relative path from L03 dir to _shared:** `../../_shared/` -- match L02 pattern exactly; copy the import line verbatim from L02 chart.py. For LaTeX: `\input{../../_shared/preamble.tex}`. For Python: `sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))`. Both confirmed working in L02 production code.

---

## Work Objectives

### Core Objective
Produce Lecture 3 (Payments and Fintech) with all 6 LaTeX variants, 12 chart/cartoon scripts, 2 quiz HTML files, 1 lecture HTML page, 1 gallery HTML page, and all supporting assets -- following the exact L01/L02 pattern.

### Deliverables (Complete File Inventory)

**Slides directory: `slides/L03_Payments_and_Fintech/`** (37 files)
| # | File | Type |
|---|------|------|
| 1 | `L03_full.tex` | LaTeX, ~31 frames, uses `\input{../../_shared/preamble.tex}` |
| 2 | `L03_overview.tex` | LaTeX, ~25-30 frames, uses `\input{../../_shared/preamble.tex}` |
| 3 | `L03_deepdive.tex` | LaTeX, ~15-20 frames, uses `\input{../../_shared/preamble.tex}` |
| 4 | `L03_core.tex` | LaTeX, ~10 frames, self-contained (inline preamble) |
| 5 | `L03_mini10.tex` | LaTeX, exactly 10+title frames, self-contained |
| 6 | `L03_mini5.tex` | LaTeX, exactly 5+title frames, self-contained |
| 7 | `L03_full.pdf` | Compiled PDF |
| 8 | `L03_overview.pdf` | Compiled PDF |
| 9 | `L03_deepdive.pdf` | Compiled PDF |
| 10 | `L03_core.pdf` | Compiled PDF |
| 11 | `L03_mini10.pdf` | Compiled PDF |
| 12 | `L03_mini5.pdf` | Compiled PDF |
| 13 | `01_payment_history_timeline/chart.py` | Python matplotlib |
| 14 | `01_payment_history_timeline/chart.pdf` | Generated chart |
| 15 | `02_global_payment_trends/chart.py` | Python matplotlib |
| 16 | `02_global_payment_trends/chart.pdf` | Generated chart |
| 17 | `03_four_party_payment_model/chart.py` | Python matplotlib |
| 18 | `03_four_party_payment_model/chart.pdf` | Generated chart |
| 19 | `04_payment_lifecycle_flow/chart.py` | Python matplotlib |
| 20 | `04_payment_lifecycle_flow/chart.pdf` | Generated chart |
| 21 | `05_merchant_cost_comparison/chart.py` | Python matplotlib |
| 22 | `05_merchant_cost_comparison/chart.pdf` | Generated chart |
| 23 | `06_interchange_fee_structure/chart.py` | Python matplotlib |
| 24 | `06_interchange_fee_structure/chart.pdf` | Generated chart |
| 25 | `07_realtime_payment_adoption/chart.py` | Python matplotlib |
| 26 | `07_realtime_payment_adoption/chart.pdf` | Generated chart |
| 27 | `08_cross_border_payment_flows/chart.py` | Python matplotlib |
| 28 | `08_cross_border_payment_flows/chart.pdf` | Generated chart |
| 29 | `09_cbdc_design_comparison/chart.py` | Python matplotlib |
| 30 | `09_cbdc_design_comparison/chart.pdf` | Generated chart |
| 31 | `10_payment_innovation_timeline/chart.py` | Python matplotlib |
| 32 | `10_payment_innovation_timeline/chart.pdf` | Generated chart |
| 33 | `11_opening_cartoon/cartoon.py` | Python matplotlib (xkcd style) |
| 34 | `11_opening_cartoon/cartoon.pdf` | Generated cartoon |
| 35 | `12_closing_cartoon/cartoon.py` | Python matplotlib (xkcd style) |
| 36 | `12_closing_cartoon/cartoon.pdf` | Generated cartoon |
| 37 | `AGENTS.md` | Directory documentation |

**Docs directory additions:** (8+ files)
| # | File | Type |
|---|------|------|
| 38 | `docs/lectures/L03.html` | Lecture page (8 sections) |
| 39 | `docs/galleries/L03_gallery.html` | 5-tab gallery |
| 40 | `docs/galleries/images/L03/mini5/*.png` | Gallery slide PNGs |
| 41 | `docs/galleries/images/L03/mini10/*.png` | Gallery slide PNGs |
| 42 | `docs/galleries/images/L03/core/*.png` | Gallery slide PNGs |
| 43 | `docs/galleries/images/L03/extended/*.png` | Gallery slide PNGs |
| 44 | `docs/galleries/images/L03/full/*.png` | Gallery slide PNGs |
| 45 | `docs/quiz/L03_quiz.html` | Standard quiz (20 questions) |
| 46 | `docs/quiz/L03_quiz_advanced.html` | Advanced quiz (20 questions) |
| 47 | `docs/slides/pdf/L03_full.pdf` | Copy of compiled PDF |
| 48 | `docs/slides/pdf/L03_overview.pdf` | Copy of compiled PDF |
| 49 | `docs/slides/pdf/L03_deepdive.pdf` | Copy of compiled PDF |
| 50 | `docs/slides/pdf/L03_core.pdf` | Copy of compiled PDF |
| 51 | `docs/slides/pdf/L03_mini10.pdf` | Copy of compiled PDF |
| 52 | `docs/slides/pdf/L03_mini5.pdf` | Copy of compiled PDF |
| 53 | `docs/slides/images/L03_Payments_and_Fintech/*.png` | 12 chart PNGs |

**Modified files:** (1 file)
| # | File | Change |
|---|------|--------|
| 54 | `docs/index.html` | L03 card: `coming-soon` -> `available`, add active links + download block |

### Definition of Done
- [ ] All 6 .tex files compile without errors via pdflatex (2 passes each)
- [ ] All 12 chart.py / cartoon.py scripts execute without errors and produce .pdf output
- [ ] All 6 compiled PDFs render correctly (spot-check: title page, charts visible, no missing fonts)
- [ ] Both quiz HTML files load in browser with working JS (check answer, score calculation)
- [ ] L03.html lecture page loads with all 8 sections, sidebar navigation working
- [ ] L03_gallery.html loads with 5 tabs, images visible
- [ ] docs/index.html shows L03 as "Available" with working links
- [ ] All `\includegraphics` paths in .tex files resolve correctly
- [ ] Frame counts match spec: full(~31), overview(~25-30), deepdive(~15-20), core(~10), mini10(10+title), mini5(5+title)
- [ ] Quiz Bloom's distribution: standard = understand(4)+apply(8)+analyze(6)+evaluate(2), advanced = apply(4)+analyze(8)+evaluate(6)+create(2)

---

## Guardrails

### MUST Have
- All relative paths match L02 pattern exactly (../../_shared for both LaTeX and Python)
- `\includegraphics` use bare relative paths like `01_payment_history_timeline/chart.pdf` (no `figures/` prefix)
- Self-contained variants (core, mini10, mini5) have NO `\input{}` commands and NO `\includegraphics` -- pure TikZ + text
- Full/overview/deepdive variants use `\input{../../_shared/preamble.tex}`
- All chart.py scripts have `CHART_METADATA` dict
- All chart.py scripts have fallback V4_COLORS and helper functions (try/except pattern from L02)
- Cartoons use `with plt.xkcd():` context
- All quiz questions are about payments/fintech content -- NO coding questions
- Subtitle in LaTeX: "From Cash to Digital: The Transformation of Money Movement"
- Bridge frame references L02 (behavioral economics, choice architecture)
- Forward-look frame previews L04 (Fintech Security and Regulation -- RegTech)
- Course progress bar updated to show L03 checked

### MUST NOT Have
- Real market data in charts (all conceptual with `np.random.seed(42)`)
- `\input{}` in core/mini10/mini5 files
- External file dependencies in mini variants (no `\includegraphics`)
- `figures/` prefix in any `\includegraphics` path
- Coding questions in quizzes
- Any broken relative paths
- Missing chart subdirectories

---

## L03 Content Architecture

### Chart Subdirectories (12 total)

| # | Directory | Chart Type | Content | Section |
|---|-----------|-----------|---------|---------|
| 01 | `01_payment_history_timeline` | time_series | Timeline from barter (3000 BCE) through coinage, paper, checks, cards, digital wallets, CBDCs | History of Payments |
| 02 | `02_global_payment_trends` | comparison_bar | Cash vs. card vs. mobile payment share by region (US, EU, China, India, Africa) | Global Payment Trends |
| 03 | `03_four_party_payment_model` | flowchart | Cardholder -> Issuer -> Network -> Acquirer -> Merchant with fee flows | Payment Process Complexity |
| 04 | `04_payment_lifecycle_flow` | flowchart | Authorization -> Clearing -> Settlement lifecycle with timing annotations | Payment Process Complexity |
| 05 | `05_merchant_cost_comparison` | comparison_bar | Cost per $100 transaction: cash, debit, credit, mobile, crypto | Merchant Cost Burden |
| 06 | `06_interchange_fee_structure` | flowchart/diagram | Fee flow diagram: who pays whom in a card transaction (interchange, assessment, processing) | Regulation of Credit and Payments |
| 07 | `07_realtime_payment_adoption` | comparison_bar | Real-time payment volume by country (UPI, PIX, FedNow, Faster Payments, SEPA Instant) | Global Payment Trends |
| 08 | `08_cross_border_payment_flows` | flowchart | Correspondent banking chain: originator -> sending bank -> correspondent(s) -> receiving bank -> beneficiary | Payment Process Complexity |
| 09 | `09_cbdc_design_comparison` | comparison_bar/matrix | Retail vs. wholesale CBDC design dimensions: privacy, programmability, intermediation, offline capability | Future of Payments |
| 10 | `10_payment_innovation_timeline` | time_series | Payment disruption waves: 1950s cards -> 1990s internet -> 2010s mobile -> 2020s embedded/invisible | Future of Payments |
| 11 | `11_opening_cartoon` | cartoon (xkcd) | Person paying with phone, cashier confused by physical cash. Caption: "Sorry, we don't accept... whatever that is." | Opening |
| 12 | `12_closing_cartoon` | cartoon (xkcd) | Two ATMs talking, one saying "Remember when we were the future?" | Closing |

### Narrative Arc (Full Variant, ~31 frames)

| Frame(s) | Arc Role | Content | Charts Used |
|----------|----------|---------|-------------|
| 1 | Title | Title page | -- |
| 2 | Opening | Opening cartoon | 11_opening_cartoon |
| 3 | Objectives | Learning objectives (5 items, Bloom's tagged) | -- |
| 4 | Bridge | Bridge from L02 (behavioral lens -> payment design) | 01_payment_history_timeline |
| 5 | FEEL | Personal connection: "Why does paying by card feel different from cash?" | -- |
| 6-9 | WHAT | History of Payments + Global Payment Trends | 01, 02, 07 |
| 10-13 | CASE | Payment Process Complexity (four-party model, lifecycle, cross-border) | 03, 04, 08 |
| 14-17 | HOW | Merchant Cost Burden (interchange, facilitator model, cost comparison) | 05, 06 |
| 18-20 | RISK | Regulation and risks (Durbin, PSD2, interchange caps, open banking mandates) | -- |
| 21-23 | WHERE | Evidence at scale (real-time payment adoption globally, cross-border corridors) | 07, 02 |
| 24-25 | IMPACT | Future of Payments (CBDCs, stablecoins, embedded, invisible) | 09, 10 |
| 26-27 | SO WHAT | Synthesis: Payment Design Evaluation Framework | -- |
| 28 | ACT | Forward look: L04 preview + reflection prompt | -- |
| 29 | Closing | Closing cartoon | 12_closing_cartoon |
| 30 | Takeaways | Key takeaways (7 items) | -- |
| 31 | Summary | Summary + key vocabulary + next lecture | -- |

### Quiz Content Focus

**Standard Quiz (20 questions):**
- Understand (4): Payment history milestones, basic four-party model roles, what interchange fees are, what a CBDC is
- Apply (8): Identify fee flow in a transaction, classify payment types by settlement speed, apply four-party model to a scenario, match regulation to jurisdiction, calculate merchant cost burden
- Analyze (6): Compare real-time payment systems across countries, analyze why cash persists in some markets, break down cross-border payment friction, analyze interchange regulation impact
- Evaluate (2): Assess CBDC design tradeoffs, evaluate PSD2 impact on competition

**Advanced Quiz (20 questions):**
- Apply (4): Apply correspondent banking model to a scenario, calculate total payment processing cost, apply regulation to a new market
- Analyze (8): Analyze PSD2 impact on incumbent banks, decompose merchant fee structure, compare CBDC approaches across central banks, analyze network effects in payment systems
- Evaluate (6): Evaluate CBDC effects on commercial bank deposits and monetary transmission, critique interchange fee regulation effectiveness, assess stablecoin risks vs. traditional payment rails
- Create (2): Design a payment strategy for a multi-market fintech, propose a CBDC framework balancing privacy and compliance

---

## Task Flow and Dependencies

```
Phase 1 (Scaffold) ────> Phase 2-7 (LaTeX, parallel-safe)
                    ├──> Phase 8 (Charts, parallel with LaTeX writing)
                    │
Phase 8 ──────────> Phase 9 (Execute charts)
                    │
Phase 2 + Phase 9 ─> Phase 10 (Compile full/overview/deepdive -- need charts)
Phase 3-7 ────────> Phase 10 (Compile core/mini10/mini5 -- no chart dependency)
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
slides/L03_Payments_and_Fintech/
slides/L03_Payments_and_Fintech/01_payment_history_timeline/
slides/L03_Payments_and_Fintech/02_global_payment_trends/
slides/L03_Payments_and_Fintech/03_four_party_payment_model/
slides/L03_Payments_and_Fintech/04_payment_lifecycle_flow/
slides/L03_Payments_and_Fintech/05_merchant_cost_comparison/
slides/L03_Payments_and_Fintech/06_interchange_fee_structure/
slides/L03_Payments_and_Fintech/07_realtime_payment_adoption/
slides/L03_Payments_and_Fintech/08_cross_border_payment_flows/
slides/L03_Payments_and_Fintech/09_cbdc_design_comparison/
slides/L03_Payments_and_Fintech/10_payment_innovation_timeline/
slides/L03_Payments_and_Fintech/11_opening_cartoon/
slides/L03_Payments_and_Fintech/12_closing_cartoon/
docs/galleries/images/L03/mini5/
docs/galleries/images/L03/mini10/
docs/galleries/images/L03/core/
docs/galleries/images/L03/extended/
docs/galleries/images/L03/full/
docs/slides/images/L03_Payments_and_Fintech/
```

**Acceptance criteria:**
- All 12 chart subdirectories exist under `slides/L03_Payments_and_Fintech/`
- All 5 gallery image subdirectories exist under `docs/galleries/images/L03/`
- `docs/slides/images/L03_Payments_and_Fintech/` exists

---

### Phase 2: Generate L03_full.tex (Flagship)

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_full.tex`

**Structure (match L02_full.tex exactly):**
```
% L03_full.tex -- Lecture 3: Payments and Fintech (Full Variant)
% Frames: 31 | Charts: 12 \includegraphics | Arc: 10-role
% Generated for: Financial Technology (FinTech) -- MSc Course, Spring 2026
\input{../../_shared/preamble.tex}

\subtitle{From Cash to Digital: The Transformation of Money Movement}

\begin{document}
... 31 frames ...
\end{document}
```

**Frame inventory (31 frames, 12 `\includegraphics`):**

| Frame | Title | Content | Chart |
|-------|-------|---------|-------|
| 1 | Title Page | `\titlepage` | -- |
| 2 | Opening Cartoon | "Sorry, We Don't Accept That" | `11_opening_cartoon/cartoon.pdf` |
| 3 | Learning Objectives | 5 objectives, Bloom's tagged | -- |
| 4 | Bridge from L02 | L02 behavioral lens -> payment design as choice architecture | `01_payment_history_timeline/chart.pdf` |
| 5 | The Pain of Paying | Personal: cash vs. card feels different -- behavioral economics of payment pain | -- |
| 6 | A Brief History of Payments | Barter -> coinage -> paper -> checks -> wire -> cards -> digital | -- |
| 7 | The Global Payment Landscape | Cash vs. card vs. mobile by region | `02_global_payment_trends/chart.pdf` |
| 8 | The Rise of Real-Time Payments | UPI, PIX, FedNow, Faster Payments, SEPA Instant | `07_realtime_payment_adoption/chart.pdf` |
| 9 | Why Cash Persists | Anonymity, reliability, no fees, cultural inertia | -- |
| 10 | The Four-Party Payment Model | Issuer, acquirer, network, merchant relationships | `03_four_party_payment_model/chart.pdf` |
| 11 | Authorization, Clearing, Settlement | Lifecycle with timing | `04_payment_lifecycle_flow/chart.pdf` |
| 12 | Batch vs. Real-Time Processing | Why settlement still takes days in most systems | -- |
| 13 | Cross-Border Payment Complexity | Correspondent banking chain | `08_cross_border_payment_flows/chart.pdf` |
| 14 | The Merchant Cost Burden | Cost comparison across payment types | `05_merchant_cost_comparison/chart.pdf` |
| 15 | Interchange Fees Explained | Who pays whom in a card transaction | `06_interchange_fee_structure/chart.pdf` |
| 16 | Payment Facilitators and Aggregators | Stripe/Square model -- how they simplified merchant onboarding | -- |
| 17 | Small vs. Large Merchant Economics | Disproportionate fee impact on small businesses | -- |
| 18 | The Durbin Amendment | US debit interchange regulation -- intended and unintended consequences | -- |
| 19 | PSD2 and Open Banking | European payment regulation -- strong customer authentication, account access | -- |
| 20 | Global Interchange Regulation | Interchange caps across jurisdictions, open banking mandates | -- |
| 21 | Real-Time Payment Systems Compared | Deep dive: UPI (India), PIX (Brazil), FedNow (US) | `07_realtime_payment_adoption/chart.pdf` |
| 22 | Cross-Border Payment Corridors | Remittance flows, SWIFT vs. alternatives | -- |
| 23 | The Cost of Sending Money Abroad | Average remittance cost by corridor, UN SDG target | -- |
| 24 | Central Bank Digital Currencies | Retail vs. wholesale, design dimensions | `09_cbdc_design_comparison/chart.pdf` |
| 25 | Stablecoins and Payment Rails | USDC/USDT as payment infrastructure, regulatory response | -- |
| 26 | Embedded and Invisible Payments | Buy buttons, in-app payments, IoT payments, payment waves | `10_payment_innovation_timeline/chart.pdf` |
| 27 | A Payment Evaluation Framework | 5 questions: speed, cost, inclusion, security, privacy | -- |
| 28 | What Comes Next | L04 preview + reflection prompt + course progress bar | -- |
| 29 | Closing Cartoon | "Remember When We Were the Future?" | `12_closing_cartoon/cartoon.pdf` |
| 30 | Key Takeaways | 7 key points | -- |
| 31 | Summary and Key Vocabulary | Summary paragraph + 10 vocabulary terms + next lecture | -- |

**Critical patterns to replicate:**
- Header comment: `% L03_full.tex -- Lecture 3: Payments and Fintech (Full Variant)`
- `\input{../../_shared/preamble.tex}` on line 4
- `\subtitle{From Cash to Digital: The Transformation of Money Movement}`
- `\bottomnote{...}` on every frame
- `\textcolor{mlpurple}{...}` for emphasis
- `\textcolor{mlred}{...}` for risks/warnings
- `\begin{columns}[T]` layout for chart+text frames (50/47 split like L02)
- `\includegraphics[width=\textwidth]{01_payment_history_timeline/chart.pdf}` (bare relative paths)
- `\begin{exampleblock}`, `\begin{alertblock}`, `\begin{block}` usage
- Course progress bar in frame 28 (L01 + L02 checked, L03 bold)
- Bottom note of final frame: reference to L04

**Acceptance criteria:**
- Exactly 31 `\begin{frame}` blocks
- Exactly 12 `\includegraphics` commands
- All `\includegraphics` paths use bare relative format (no `figures/` prefix)
- `\input{../../_shared/preamble.tex}` present
- Every frame has a `\bottomnote{}`
- Bridge frame references L02
- Forward-look frame previews L04

---

### Phase 3: Generate L03_overview.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_overview.tex`

**Pattern (from L02_overview.tex):**
```
% L03_overview.tex -- Lecture 3: Payments and Fintech (Overview Variant)
% Frames: ~27 | Charts: subset of 12 | Architecture: INTRO/CORE/CLOSING
\input{../../_shared/preamble.tex}
\subtitle{From Cash to Digital: The Transformation of Money Movement}
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

### Phase 4: Generate L03_deepdive.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_deepdive.tex`

**Pattern (from L02_deepdive.tex):**
```
% L03_deepdive.tex -- Lecture 3: Payments and Fintech (Deep Dive Variant)
% Frame count: ~12 main body + ~5 appendix = ~17 total
% Architecture: MAIN BODY + \appendix
\input{../../_shared/preamble.tex}
\subtitle{From Cash to Digital: The Transformation of Money Movement --- Deep Dive}
```

**Focus areas for deep dive:**
- Interchange fee economics (game-theoretic analysis)
- CBDC monetary policy implications (disintermediation risk)
- Cross-border payment reform (SWIFT alternatives, blockchain settlement)
- Real-time gross settlement system design
- Payment fraud and security architecture

**Acceptance criteria:**
- 15-20 `\begin{frame}` blocks total
- Has `\appendix` section with supplementary analytical frames
- Advanced learning objectives targeting Analyze/Evaluate/Create Bloom's levels
- Uses `\input{../../_shared/preamble.tex}`
- Includes subset of charts

---

### Phase 5: Extract L03_core.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_core.tex`

**Pattern (from L02_core.tex -- SELF-CONTAINED):**
```
% L03_core.tex -- Payments and Fintech
% Core Slides (10 frames)
% Self-contained (no \input{} commands)
% Compile: pdflatex L03_core.tex (twice for overlays)

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

**Content:** Extract the 10 most essential frames from L03_full covering: bridge, four-party model, interchange fees, global trends, real-time payments, merchant costs, regulation overview, CBDC basics, evaluation framework, key takeaways.

**Critical:** Uses `\includegraphics` for charts (unlike mini variants). Has `\graphicspath{{}}` and can reference chart subdirectories.

**Acceptance criteria:**
- Exactly 10 `\begin{frame}` blocks
- NO `\input{}` commands anywhere
- Full inline preamble (documentclass, usepackage, colors, beamer settings, bottomnote command)
- Has `\graphicspath{{}}`
- Can include `\includegraphics` for charts
- Compiles standalone without any external dependencies

---

### Phase 6: Generate L03_mini10.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_mini10.tex`

**Pattern (from L02_mini10.tex -- SELF-CONTAINED, NO \includegraphics):**
```
% L02_mini10.tex -- Fintech Ecosystem
% 10-Slide Arc: WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT
% Self-contained (no \input{} commands, no \includegraphics)
```

**Arc:** WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT
- Title frame (not counted in the 10)
- Frame 1 (WHY): TikZ comic -- person tapping phone at merchant, cash register gathering dust
- Frame 2 (FEEL): Text prompt -- "Check your last 10 transactions"
- Frame 3 (WHAT): Table -- payment types comparison (cash, card, mobile, crypto)
- Frame 4 (CASE): TikZ diagram -- four-party payment model
- Frame 5 (HOW): TikZ flow -- authorization -> clearing -> settlement lifecycle
- Frame 6 (RISK): TikZ comic -- merchant looking at fee breakdown
- Frame 7 (WHERE): pgfplots bar chart -- real-time payment adoption by country (illustrative)
- Frame 8 (IMPACT): TikZ quadrant -- speed vs. cost of payment types
- Frame 9 (SO WHAT): Evaluation checklist -- 5 questions for any payment system
- Frame 10 (ACT): Activity + next lecture preview

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

### Phase 7: Generate L03_mini5.tex

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/L03_mini5.tex`

**Pattern (from L02_mini5.tex -- SELF-CONTAINED, NO \includegraphics):**
```
% L03_mini5.tex -- Payments and Fintech
% 5-Slide Teaser Arc: WHY > WHAT > HOW > WHERE > SO WHAT
% Self-contained (no \input{} commands, no \includegraphics)
```

**Arc:** WHY > WHAT > HOW > WHERE > SO WHAT
- Title frame (not counted in the 5)
- Slide 1 (WHY): TikZ comic -- evolution from barter to tap-to-pay
- Slide 2 (WHAT): Table comparing payment methods (cash, card, mobile, CBDC)
- Slide 3 (HOW): TikZ diagram -- four-party model simplified
- Slide 4 (WHERE): pgfplots bar chart -- illustrative merchant costs by payment type
- Slide 5 (SO WHAT): Evaluation framework for payment systems

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

**Template pattern (from L02 01_fintech_ecosystem_map/chart.py):**
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
    'lecture_number': 3,
}

fig, ax = plt.subplots(1, 1, figsize=(10, 6))
np.random.seed(42)
# ... chart code ...

output_path = os.path.join(os.path.dirname(__file__), 'chart.pdf')
save_chart(fig, output_path)
```

**For each of the 2 cartoon scripts (`cartoon.py`):**

**Template pattern (from L02 11_opening_cartoon/cartoon.py):**
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
    'lecture_number': 3,
}

with plt.xkcd():
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    # ... cartoon code ...

output_path = os.path.join(os.path.dirname(__file__), 'cartoon.pdf')
save_chart(fig, output_path)
```

**Important:** The cartoon save_chart fallback uses `filename='cartoon.pdf'` in the default, but the actual call uses `output_path` variable. Match L02 exactly.

**Acceptance criteria per script:**
- Imports match L02 pattern exactly (sys.path.insert, matplotlib.use('Agg'), try/except)
- Has CHART_METADATA dict with lecture_number: 3
- Uses `np.random.seed(42)` for any random data
- Charts use `figsize=(10, 6)`, cartoons use `figsize=(12, 6)`
- Output path uses `os.path.join(os.path.dirname(__file__), 'chart.pdf')` or `'cartoon.pdf'`
- All data is conceptual/illustrative (no real market data)
- Executes without errors and produces valid PDF

---

### Phase 9: Execute All Chart Scripts

**Commands (run from project root):**
```bash
cd D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech
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

**Commands (run from `slides/L03_Payments_and_Fintech/`):**
```bash
# Full, Overview, Deepdive (depend on _shared/preamble.tex AND chart PDFs)
pdflatex L03_full.tex && pdflatex L03_full.tex
pdflatex L03_overview.tex && pdflatex L03_overview.tex
pdflatex L03_deepdive.tex && pdflatex L03_deepdive.tex

# Core (depends on chart PDFs but not preamble)
pdflatex L03_core.tex && pdflatex L03_core.tex

# Mini10, Mini5 (no external dependencies)
pdflatex L03_mini10.tex && pdflatex L03_mini10.tex
pdflatex L03_mini5.tex && pdflatex L03_mini5.tex
```

**Acceptance criteria:**
- All 6 produce .pdf files
- No fatal LaTeX errors (warnings about overful hbox are acceptable)
- Each PDF has correct number of pages (frames + 0-1 for title)
- Charts are visible in full/overview/deepdive/core PDFs

---

### Phase 11: Generate Quiz HTML Files

**File 1:** `D:/Joerg/Research/slides/Fintech/docs/quiz/L03_quiz.html`
**File 2:** `D:/Joerg/Research/slides/Fintech/docs/quiz/L03_quiz_advanced.html`

**Pattern (from L02_quiz.html):**
- Full inline CSS with same `:root` variables (--nav-bg, --hero-from, etc.)
- Navbar with links to: index.html, L03.html, L03_gallery.html, L03_quiz.html, L03_quiz_advanced.html
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
- Payment history and evolution
- Four-party model roles and relationships
- Interchange fee mechanics and regulation
- Authorization/clearing/settlement lifecycle
- Cash vs. digital payment tradeoffs
- Real-time payment systems (UPI, PIX, FedNow)
- Cross-border payment friction and corridors
- Merchant cost burden across payment types
- Durbin Amendment and PSD2 key provisions
- CBDC design dimensions and implications
- Stablecoins as payment infrastructure
- Embedded and invisible payments
- NO coding questions

**Acceptance criteria:**
- Each file has exactly 20 question blocks
- Bloom's distribution matches spec
- All questions relate to L03 payment topics
- No coding/programming questions
- Inline CSS/JS (no external dependencies)
- Navbar links are correct for L03
- Score calculation works (manual browser test)

---

### Phase 12: Generate L03.html Lecture Page

**File:** `D:/Joerg/Research/slides/Fintech/docs/lectures/L03.html`

**Pattern (from L02.html):**
- Same CSS design system (Crimson Pro + Source Sans 3 fonts, same :root variables)
- KaTeX for math rendering
- Sticky navbar with L03-specific links
- Hero section: L03 title, subtitle, description
- Sidebar navigation (8 sections)
- 8 content sections covering all L03 topics:
  1. History of Payments
  2. Global Payment Trends
  3. Payment Process Complexity
  4. Merchant Cost Burden
  5. Regulation of Payments
  6. Future of Payments (CBDCs, Stablecoins)
  7. Payment Design Framework (synthesis)
  8. Key Vocabulary and Summary
- Each section: ~300-500 words, educational prose, key terms bolded
- Info boxes, callout boxes, alert boxes matching L02 style
- Footer

**Acceptance criteria:**
- HTML validates (no unclosed tags)
- 8 sidebar navigation links work
- All internal links functional
- Navbar links correct for L03
- Content covers all 6 L03 topics comprehensively
- No placeholder text

---

### Phase 13: Generate L03_gallery.html + Gallery PNGs

**File:** `D:/Joerg/Research/slides/Fintech/docs/galleries/L03_gallery.html`

**Pattern (from L02_gallery.html):**
- 5 tabs: Mini 5, Mini 10, Core, Extended (overview), Full
- Each tab shows slide images as a scrollable gallery
- Tab switching via inline JS
- Same CSS design system

**PNG generation (pdftoppm or equivalent):**
```bash
# Convert each PDF variant to PNGs for gallery
pdftoppm -png -r 150 L03_mini5.pdf docs/galleries/images/L03/mini5/slide
pdftoppm -png -r 150 L03_mini10.pdf docs/galleries/images/L03/mini10/slide
pdftoppm -png -r 150 L03_core.pdf docs/galleries/images/L03/core/slide
pdftoppm -png -r 150 L03_overview.pdf docs/galleries/images/L03/extended/slide
pdftoppm -png -r 150 L03_full.pdf docs/galleries/images/L03/full/slide
```

**Acceptance criteria:**
- Gallery HTML has 5 working tabs
- PNG images exist in all 5 subdirectories
- Tab switching shows correct images
- Images are legible at gallery size

---

### Phase 14: Copy PDFs and Chart PNGs to docs/

**PDF copies:**
```bash
cp slides/L03_Payments_and_Fintech/L03_full.pdf docs/slides/pdf/
cp slides/L03_Payments_and_Fintech/L03_overview.pdf docs/slides/pdf/
cp slides/L03_Payments_and_Fintech/L03_deepdive.pdf docs/slides/pdf/
cp slides/L03_Payments_and_Fintech/L03_core.pdf docs/slides/pdf/
cp slides/L03_Payments_and_Fintech/L03_mini10.pdf docs/slides/pdf/
cp slides/L03_Payments_and_Fintech/L03_mini5.pdf docs/slides/pdf/
```

**Chart PNG conversions (for docs/slides/images/):**
Convert each chart.pdf/cartoon.pdf to .png and copy to `docs/slides/images/L03_Payments_and_Fintech/`:
```
payment_history_timeline.png
global_payment_trends.png
four_party_payment_model.png
payment_lifecycle_flow.png
merchant_cost_comparison.png
interchange_fee_structure.png
realtime_payment_adoption.png
cross_border_payment_flows.png
cbdc_design_comparison.png
payment_innovation_timeline.png
opening_cartoon.png
closing_cartoon.png
```

**Acceptance criteria:**
- 6 PDFs in `docs/slides/pdf/` matching names `L03_*.pdf`
- 12 PNGs in `docs/slides/images/L03_Payments_and_Fintech/`
- All files > 0 bytes

---

### Phase 15: Update docs/index.html

**File:** `D:/Joerg/Research/slides/Fintech/docs/index.html`

**Changes required:**

1. **L03 lecture card (lines ~774-804):** Change from `coming-soon` to `available` with active links.

Replace the entire L03 card block:
- `class="lecture-card coming-soon"` -> `class="lecture-card available"`
- `class="status-badge coming-soon"` -> `class="status-badge available"`
- `Coming Soon` -> `Available`
- Title: update to "Payments and Fintech" (currently "Payments and Digital Money")
- Description: update to match L03 content
- Replace all `<span class="link-pill disabled">` with `<a href="..." class="link-pill ...">` (matching L02 pattern exactly -- same SVG icons)

2. **Downloads section (after L02 block, ~line 1010):** Add L03 download block:
```html
<!-- L03 Downloads -->
<div class="download-block">
  <p class="download-block-label">Lecture 03 -- Payments and Fintech</p>
  <div class="download-pills">
    <a href="slides/pdf/L03_full.pdf" class="dl-pill">...L03 Full...</a>
    <a href="slides/pdf/L03_overview.pdf" class="dl-pill">...L03 Overview...</a>
    <a href="slides/pdf/L03_deepdive.pdf" class="dl-pill">...L03 Deep Dive...</a>
    <a href="slides/pdf/L03_core.pdf" class="dl-pill">...L03 Core...</a>
    <a href="slides/pdf/L03_mini10.pdf" class="dl-pill">...L03 Mini 10...</a>
    <a href="slides/pdf/L03_mini5.pdf" class="dl-pill">...L03 Mini 5...</a>
  </div>
</div>
```

**Acceptance criteria:**
- L03 card shows "Available" status badge
- All 5 link pills are clickable `<a>` tags (not disabled `<span>`)
- Links point to correct L03 URLs:
  - Lecture: `lectures/L03.html`
  - Gallery: `galleries/L03_gallery.html`
  - Quiz: `quiz/L03_quiz.html`
  - Advanced Quiz: `quiz/L03_quiz_advanced.html`
  - Download PDF: `slides/pdf/L03_full.pdf`
- Download block appears after L02 block with all 6 variants
- SVG icons match L02 pattern exactly
- HTML structure matches L02 card exactly

---

### Phase 16: Create AGENTS.md for L03

**File:** `D:/Joerg/Research/slides/Fintech/slides/L03_Payments_and_Fintech/AGENTS.md`

**Pattern (from L02 AGENTS.md):**
- Header: `# L03: Payments and Fintech`
- Parent reference: `<!-- Parent: ../AGENTS.md -->`
- Overview section with core themes
- Directory structure (all 12 chart dirs + 6 tex + 6 pdf + AGENTS.md)
- Key files table
- Variants guide (For Instructors / For Self-Study / For Outreach)
- Graphics & Figures (12 total: 10 charts + 2 cartoons with descriptions)
- Generation & Compilation instructions
- Instructional Goals (5 learning objectives, Bloom's tagged)
- Integration Points (links from L02, links to L04)
- File Maintenance notes
- Notes for Developers

**Acceptance criteria:**
- Matches L02 AGENTS.md structure section-by-section
- All 12 chart directories listed with descriptions
- All 6 variants listed with frame counts
- Correct lecture number (3) throughout
- References L02 (previous) and L04 (next) correctly

---

### Phase 17: Commit and Push

**Commit strategy:**
```
git add slides/L03_Payments_and_Fintech/
git add docs/lectures/L03.html
git add docs/galleries/L03_gallery.html
git add docs/galleries/images/L03/
git add docs/quiz/L03_quiz.html
git add docs/quiz/L03_quiz_advanced.html
git add docs/slides/pdf/L03_*.pdf
git add docs/slides/images/L03_Payments_and_Fintech/
git add docs/index.html

git commit -m "Add L03: Payments and Fintech

Complete lecture materials including:
- 6 LaTeX variants (full, overview, deepdive, core, mini10, mini5)
- 12 matplotlib charts (10 analytical + 2 XKCD cartoons)
- Standard and advanced quizzes (20 questions each)
- Lecture page, gallery page, and gallery images
- docs/index.html updated: L03 available with download pills"

git push
```

**Acceptance criteria:**
- All new files tracked
- No untracked L03 files left behind
- Commit message describes scope
- Push succeeds

---

## Success Criteria (Final Verification Checklist)

| # | Check | Method |
|---|-------|--------|
| 1 | 12 chart subdirectories exist | `ls slides/L03_Payments_and_Fintech/` |
| 2 | 12 chart/cartoon PDFs generated | `ls slides/L03_Payments_and_Fintech/*/chart.pdf slides/L03_Payments_and_Fintech/*/cartoon.pdf` |
| 3 | 6 compiled slide PDFs exist | `ls slides/L03_Payments_and_Fintech/L03_*.pdf` |
| 4 | Frame counts correct | Open each PDF, count slides |
| 5 | No LaTeX compilation errors | Check .log files for `Fatal error` |
| 6 | All \includegraphics resolve | No "File not found" in .log |
| 7 | 6 PDFs copied to docs/slides/pdf/ | `ls docs/slides/pdf/L03_*.pdf` |
| 8 | 12 chart PNGs in docs/slides/images/ | `ls docs/slides/images/L03_Payments_and_Fintech/` |
| 9 | Gallery images in 5 subdirs | `ls docs/galleries/images/L03/` |
| 10 | L03_quiz.html has 20 questions | Count question blocks |
| 11 | L03_quiz_advanced.html has 20 questions | Count question blocks |
| 12 | L03.html has 8 sections | Count section headers |
| 13 | L03_gallery.html has 5 tabs | Check tab elements |
| 14 | index.html shows L03 as Available | Check class attribute |
| 15 | index.html has L03 download block | Search for "L03" in downloads section |
| 16 | AGENTS.md present and complete | Read file, check all sections |
| 17 | No `\input{}` in core/mini10/mini5 | grep for \input in those files |
| 18 | No `\includegraphics` in mini10/mini5 | grep for \includegraphics in those files |
| 19 | All quiz questions are non-coding | Manual review |
| 20 | Bloom's distribution correct | Count badges by level |

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

**Critical reference files for executors:**
- L02_full.tex: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/L02_full.tex`
- L02_core.tex: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/L02_core.tex`
- L02_mini10.tex: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/L02_mini10.tex`
- L02_mini5.tex: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/L02_mini5.tex`
- L02 chart.py example: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/01_fintech_ecosystem_map/chart.py`
- L02 cartoon.py example: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/11_opening_cartoon/cartoon.py`
- L02_quiz.html: `D:/Joerg/Research/slides/Fintech/docs/quiz/L02_quiz.html`
- L02.html: `D:/Joerg/Research/slides/Fintech/docs/lectures/L02.html`
- L02_gallery.html: `D:/Joerg/Research/slides/Fintech/docs/galleries/L02_gallery.html`
- index.html: `D:/Joerg/Research/slides/Fintech/docs/index.html` (lines 774-804 for L03 card, lines 981-1010 for L02 download block to copy pattern)
- L02 AGENTS.md: `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/AGENTS.md`
- _shared/preamble.tex: `D:/Joerg/Research/slides/Fintech/_shared/preamble.tex`
- _shared/chart_styles.py: `D:/Joerg/Research/slides/Fintech/_shared/chart_styles.py`
