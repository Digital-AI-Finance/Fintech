# L04: Fintech Security and Regulation

<!-- Parent: ../AGENTS.md -->

**Lecture 4 of the Financial Technology MSc course (Spring 2026)**

## Overview

This lecture examines fintech security and regulation through the lens of **compliance architecture** and **regulatory design**. After establishing payment systems (L03), L04 investigates the regulatory frameworks, compliance processes, and technology solutions that govern financial services in the digital age.

**Core themes:**
- Regulatory approaches: innovation-friendly vs. precautionary frameworks
- The regulatory trilemma: innovation, consumer protection, and stability
- AML/KYC: compliance processes and digital identity verification
- US regulatory patchwork: federal and state jurisdictions
- Global regulatory frameworks: EU MiCA, UK FCA sandbox, Singapore MAS
- RegTech solutions: automated compliance, NLP, real-time surveillance
- Future: regulatory sandboxes, SupTech, embedded compliance, harmonization

**Bloom's levels covered:** Understand, Apply, Analyze, Evaluate

**Key frames:** 31 (full) | 27 (overview) | 19 (deepdive) | 10 (core) | 11 (mini10) | 6 (mini5)

**Narrative structure:** 10-role arc (WHY → FEEL → WHAT → CASE → HOW → RISK → WHERE → IMPACT → SO WHAT → ACT)

---

## Directory Structure

```
L04_Fintech_Security_and_Regulation/
├── AGENTS.md (this file)
├── L04_full.tex         (31 frames, full narrative)
├── L04_overview.tex     (27 frames, three-zone structure)
├── L04_deepdive.tex     (19 frames + appendix)
├── L04_core.tex         (10 frames, self-contained core)
├── L04_mini10.tex       (11 frames, self-contained teaser)
├── L04_mini5.tex        (6 frames, 5-slide arc)
├── L04_full.pdf
├── L04_overview.pdf
├── L04_deepdive.pdf
├── L04_core.pdf
├── L04_mini10.pdf
├── L04_mini5.pdf
├── 01_regulatory_approaches/
├── 02_aml_compliance_flow/
├── 03_kyc_process_flow/
├── 04_money_laundering_stages/
├── 05_us_regulatory_patchwork/
├── 06_global_regulatory_comparison/
├── 07_regtech_stack_architecture/
├── 08_sandbox_adoption_timeline/
├── 09_compliance_cost_comparison/
├── 10_regtech_investment_trends/
├── 11_opening_cartoon/
└── 12_closing_cartoon/
```

---

## Key Files

| File | Purpose | Audience | Status |
|------|---------|----------|--------|
| `L04_full.tex` | Primary lecture deck (31 frames) | Instructors, students | Production |
| `L04_overview.tex` | Condensed overview (27 frames) | Quick reference | Production |
| `L04_deepdive.tex` | Analytical variant with appendix (19 frames) | Deep learners | Production |
| `L04_core.tex` | Extracted 10-frame core (self-contained) | Standalone teaching | Production |
| `L04_mini10.tex` | 11-frame teaser with TikZ diagrams | Promotional | Production |
| `L04_mini5.tex` | 5-slide arc (WHY > WHAT > HOW > WHERE > SO WHAT) | Lightning talks | Production |
| `*/chart.py` | Python generation scripts (matplotlib) | Regeneration | Production |
| `*/chart.pdf` | Compiled charts (10 + 2 cartoons = 12 total) | Embedded in slides | Production |

---

## Variants Guide

### For Instructors
- **L04_full.tex** — Use this in 90-minute sessions. Covers all 10 narrative roles with regulatory approaches, AML/KYC processes, compliance architecture, and closure.
- **L04_overview.tex** — Use this in 60-minute sessions. Three-zone structure emphasizes regulatory frameworks, compliance processes, and RegTech solutions.

### For Self-Study
- **L04_core.tex** — Self-contained, printable. Covers only the 10 essential frames (no dependency on preamble).
- **L04_deepdive.tex** — Deep dive with appendix for additional technical details on RegTech, global frameworks, and policy analysis.

### For Outreach/Promotion
- **L04_mini5.tex** — Ultra-short 5-slide teaser arc. No external dependencies (pure TikZ).
- **L04_mini10.tex** — Slightly expanded 11-frame version. Self-contained with inline TikZ diagrams.

---

## Graphics & Figures (12 Total)

All 12 figures live in chart subdirectories (flat in lecture dir). Each includes a Python script (`chart.py` or `cartoon.py`) and compiled PDF.

### Charts (10 analytical figures)

1. **01_regulatory_approaches** — Comparison matrix of regulatory approaches from innovation-friendly (regulatory arbitrage, light-touch rules) to precautionary (sandbox, enhanced scrutiny, ban)
2. **02_aml_compliance_flow** — End-to-end AML pipeline showing risk assessment, transaction monitoring, suspicious activity reporting (SAR), and investigation workflow
3. **03_kyc_process_flow** — KYC lifecycle with customer onboarding, identity verification, manual vs. digital paths (document collection, video KYC, biometric verification)
4. **04_money_laundering_stages** — Three stages of money laundering (placement, layering, integration) with examples and detection challenges
5. **05_us_regulatory_patchwork** — US regulatory landscape showing federal agencies (Fed, OCC, FDIC, SEC, CFTC) and state regulators, overlapping jurisdictions, and charter options
6. **06_global_regulatory_comparison** — Multi-jurisdiction comparison matrix (EU MiCA, UK FCA, Singapore MAS, Hong Kong, Japan) on crypto, stablecoins, and digital assets
7. **07_regtech_stack_architecture** — RegTech technology stack showing layers: data sources (transactions, documents, third-party), processing (NLP, anomaly detection), and outputs (monitoring, reporting, compliance)
8. **08_sandbox_adoption_timeline** — Regulatory sandbox launches worldwide 2016-2025 showing key milestones (FCA 2015, Singapore 2016, Hong Kong 2017, etc.) and adoption by region
9. **09_compliance_cost_comparison** — Compliance cost burden per $1B AUM by firm type (mega-bank, mid-tier, startup, small fintech) showing infrastructure vs. staffing costs
10. **10_regtech_investment_trends** — RegTech investment trends 2015-2025 showing funding volume, deal count, and top investment categories (ID verification, AML/sanctions, KYC automation)

### Cartoons (2 XKCD-style illustrations)

11. **11_opening_cartoon** — Compliance officer at overflowing desk surrounded by regulatory documents with RegTech robot entering: "You called?" Metaphor: compliance burden and automation promise.
12. **12_closing_cartoon** — SupTech (supervisory technology) scene with AI analyzing regulator's dashboard vs. traditional supervision: automated vs. manual oversight comparison.

---

## Generation & Compilation

### Slides
All `.tex` files compile with `pdflatex` (run twice for overlays):
```bash
pdflatex L04_full.tex && pdflatex L04_full.tex
```

**Dependencies:**
- **Full/Overview/DeepDive variants** require `../../_shared/preamble.tex` (colors, theme, metadata)
- **Core/Mini5/Mini10 variants** are self-contained (preamble embedded)

### Figures
Regenerate all charts from within the lecture directory:
```bash
cd slides/L04_Fintech_Security_and_Regulation
for dir in 0*/; do python "$dir/chart.py"; done
for dir in 1*/; do python "$dir/cartoon.py"; done
```

**Dependencies:**
- All scripts import `../../_shared/chart_styles.py` (V4_COLORS, apply_v4_style, save_chart)
- Fallback color definitions and functions embedded if import fails
- Output: `chart.pdf` or `cartoon.pdf` in each subdirectory

---

## Instructional Goals

Students will be able to:

1. **Describe** regulatory approaches from innovation-friendly to precautionary frameworks, including the regulatory trilemma between innovation, consumer protection, and financial stability (Understand)
2. **Explain** AML/KYC processes, digital identity verification methods, and how compliance systems detect and prevent money laundering (Understand)
3. **Apply** a cost-analysis framework to compare compliance burden across jurisdictions and firm types, evaluating trade-offs in regulatory approaches (Apply)
4. **Analyze** the US regulatory patchwork and global regulatory frameworks (MiCA, FCA, MAS), identifying regulatory arbitrage opportunities and harmonization challenges (Analyze)
5. **Evaluate** RegTech solutions and sandboxes as mechanisms for balancing innovation and compliance, assessing the viability of SupTech and embedded compliance (Evaluate)

---

## Integration Points

**Links from L01:**
- Lecture 1 covers fintech as a supply-side disruption across value chain
- L04 applies that lens to regulatory disruption through RegTech and digital compliance

**Links from L02:**
- Lecture 2 explored behavioral design and choice architecture
- L04 shows how compliance systems use behavioral nudges (e.g., friction in identity verification) to drive compliance

**Links from L03:**
- Lecture 3 examined payment systems and their regulation (Durbin Amendment, PSD2)
- L04 expands to holistic regulatory landscape covering payments, cryptocurrencies, and digital assets

**Links to L05/Later lectures:**
- Regulatory frameworks for wealth management (L05) build on SupTech and embedded compliance concepts from L04
- Global regulatory harmonization efforts inform discussions of cross-border fintech in emerging markets

**Assessments:**
- Quiz questions cover regulatory approaches, AML/KYC mechanics, US regulatory structure, global frameworks, and RegTech applications
- Exercises ask students to design a compliance program for a fintech startup, analyze regulatory arbitrage, and evaluate sandbox effectiveness
- Quiz content lives in `docs/quiz/`

---

## File Maintenance

**Update frequency:**
- Slides: Updated annually for Spring semester
- Figures: Regenerated yearly (data sources refreshed in chart.py metadata)
- AGENTS.md: Updated when variants or subdirectories added/removed

**Regeneration triggers:**
- Color scheme changes → rebuild all figures
- New data or research cited → update specific chart.py + regenerate
- Preamble updates → recompile all variants
- Content additions → update frame counts in headers

---

## Notes for Developers

- **Variants use `\input{../../_shared/preamble.tex}`** — These depend on a global preamble (Beamer theme, colors, commands). Ensure the path exists.
- **Mini variants are self-contained** — No external dependencies; can be compiled in isolation or emailed as standalone PDFs.
- **All figures use matplotlib with fallback color definitions** — If `../../_shared/chart_styles.py` is unavailable, charts still compile using embedded V4_COLORS and helper functions.
- **XKCD cartoons use `with plt.xkcd():`** — This is a matplotlib style context; no external libraries needed.

---

## AI Agent Instructions

### For Slides (LaTeX) Work

**When updating, generating, or debugging L04 slide decks:**

1. **Understand the variant system:**
   - `L04_full.tex`, `L04_overview.tex`, `L04_deepdive.tex` all use `\input{../../_shared/preamble.tex}` — centralizes theme, colors, and shared commands
   - `L04_core.tex`, `L04_mini10.tex`, `L04_mini5.tex` are self-contained — include all preamble, color definitions, and custom commands inline

2. **Frame structure convention:**
   - Frames are grouped by narrative role (WHY, FEEL, WHAT, CASE, HOW, RISK, WHERE, IMPACT, SO WHAT, ACT)
   - Comments mark role boundaries and frame indices
   - Use `\bottomnote{}` for pedagogical guidance on assessments

3. **Figure inclusion:**
   - All figures are in `[N]_*/chart.pdf` or `cartoon.pdf` (generated by Python scripts, flat in lecture dir)
   - Use `\includegraphics[width=...]` with PDF paths relative to the lecture directory
   - Full/overview/deepdive variants include all 12 figures; core/mini variants may embed inline TikZ instead

4. **Compilation:**
   - Full/overview/deepdive: Requires `_shared/preamble.tex` via `\input{../../_shared/preamble.tex}`
   - Core/mini5/mini10: Self-contained; compile with `pdflatex L04_*.tex` directly
   - All use `beamer` document class, `Madrid` theme, `whale` color theme

5. **Assessment alignment:**
   - Learning objectives (Frame 3) map to Bloom's levels: Understand, Apply, Analyze, Evaluate
   - Quiz and exercise assessments reference these objectives
   - Update objectives if changing learning goals

### For Figures (Python) Work

**When updating, generating, or debugging charts and cartoons:**

1. **Standard chart structure:**
   - Each subdirectory contains one Python script (`chart.py` or `cartoon.py`) and one generated PDF
   - All scripts import from `_shared/chart_styles.py` via `sys.path.insert(0, ...)`
   - Charts use `CHART_METADATA` dictionary with keys: `title`, `type`, `section` (Regulatory Approaches/AML-KYC/Compliance Architecture/RegTech/Global Frameworks/Sandboxes), `lecture_number`

2. **Chart types in L04:**
   - **Time series** (08 sandbox timeline, 10 investment trends): Annotated timelines with milestones
   - **Diagram** (02 AML flow, 03 KYC flow, 04 money laundering, 07 RegTech stack): Network or structural layout
   - **Comparison chart** (01 regulatory approaches, 05 US patchwork, 06 global comparison, 09 cost comparison): Heatmaps, matrices, or bar charts

3. **Color palette:**
   - Use `V4_COLORS` from `_shared/chart_styles.py`: `MLPURPLE`, `MLBLUE`, `MLRED`, `MLORANGE`, `MLGREEN`, `MLGRAY`, `MLTEAL`, `MLCYAN`, `MLYELLOW`, `MLPINK`, `MLBROWN`
   - Falls back to hardcoded hex if import fails

4. **Function imports:**
   - `apply_v4_style(ax, title='', xlabel='', ylabel='')` — formats axes (removes top/right spines, sets colors)
   - `save_chart(fig, filename='chart.pdf', dpi=300)` — saves as PDF with standard DPI

5. **Execution:**
   - Run: `python chart.py` or `python cartoon.py` in the subdirectory
   - Generates `chart.pdf` or `cartoon.pdf` in the same location
   - All scripts use `matplotlib.use('Agg')` for headless rendering

6. **Fallback handling:**
   - All scripts include try/except around chart_styles import
   - Hardcoded V4_COLORS dict and standalone function definitions ensure script runs even if import fails
   - Good for testing and debugging in isolation

### For Quizzes

**When authoring or updating assessments:**

1. **Quiz alignment:**
   - Question types should map to Bloom's levels from objectives: Understand, Apply, Analyze, Evaluate
   - Main quiz content lives in the `docs/quiz/` folder
   - Use terminology consistently with slides

2. **Assessment scenarios:**
   - Regulatory approaches (when should innovation-friendly vs. precautionary approach be used?)
   - AML/KYC processes (what are the steps to verify customer identity?)
   - Regulatory frameworks (how do MiCA, FCA, and MAS approaches differ?)
   - US regulatory structure (which agencies regulate which fintech activities?)
   - RegTech solutions (how do NLP and anomaly detection improve compliance?)
   - Compliance costs (how does firm size affect regulatory burden?)
   - Sandbox effectiveness (can regulatory sandboxes balance innovation and protection?)

---

## Dependencies

- **Parent:** `../AGENTS.md` (slides directory documentation)
- **Shared preamble:** `../../_shared/preamble.tex` (theme, colors, macros for full/overview/deepdive variants)
- **Shared chart styles:** `../../_shared/chart_styles.py` (color palette and formatting functions)
- **Dependencies within subdirectories:**
  - Each chart subdirectory is independent; can regenerate any chart.pdf by running its chart.py

---

## Metadata

| Field | Value |
|-------|-------|
| **Lecture** | L04 (Fintech Security and Regulation) |
| **Subtitle** | Navigating Compliance in the Digital Finance Era |
| **Audience** | MSc Financial Technology, Spring 2026 |
| **Frames** | 31 (full) / 27 (overview) / 19 (deepdive) / 10 (core) / 11 (mini10) / 6 (mini5) |
| **Figures** | 12 (10 charts + 2 cartoons) |
| **Narrative Arc** | WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT |
| **Assessment** | Quizzes (Bloom's: Understand, Apply, Analyze, Evaluate) |
| **Prerequisites** | L01 (Fintech Foundations), L02 (Fintech Ecosystem), L03 (Payments and Fintech) |

---

## License & Attribution

All materials created for the Financial Technology course, University of Zurich, Spring 2026.

---

**Last updated:** 2026-03-02
**Maintainer:** Joerg Osterrieder
