# L03: Payments and Fintech

<!-- Parent: ../AGENTS.md -->

**Lecture 3 of the Financial Technology MSc course (Spring 2026)**

## Overview

This lecture examines payments and fintech through the lens of **infrastructure design** and **behavioral economics in motion**. After establishing what fintech is (L01) and how adoption varies (L02), L03 investigates the largest fintech vertical: the systems, economics, and regulation of money movement itself.

**Core themes:**
- History of payment methods: from barter to CBDCs
- The four-party model and authorization-clearing-settlement lifecycle
- Merchant economics: fees, costs, and regulation
- Real-time payment systems and their role in financial inclusion
- Cross-border payment complexity and remittance challenges
- Central bank digital currencies and stablecoins as infrastructure

**Bloom's levels covered:** Understand, Apply, Analyze, Evaluate

**Key frames:** 31 (full) | 28 (overview) | 17 (deepdive) | 10 (core) | 11 (mini10) | 6 (mini5)

**Narrative structure:** 10-role arc (WHY → FEEL → WHAT → CASE → HOW → RISK → WHERE → IMPACT → SO WHAT → ACT)

---

## Directory Structure

```
L03_Payments_and_Fintech/
├── AGENTS.md (this file)
├── L03_full.tex         (31 frames, full narrative)
├── L03_overview.tex     (28 frames, three-zone structure)
├── L03_deepdive.tex     (17 frames + appendix)
├── L03_core.tex         (10 frames, self-contained core)
├── L03_mini10.tex       (11 frames, self-contained teaser)
├── L03_mini5.tex        (6 frames, 5-slide arc)
├── L03_full.pdf
├── L03_overview.pdf
├── L03_deepdive.pdf
├── L03_core.pdf
├── L03_mini10.pdf
├── L03_mini5.pdf
├── 01_payment_history_timeline/
├── 02_global_payment_trends/
├── 03_four_party_payment_model/
├── 04_payment_lifecycle_flow/
├── 05_merchant_cost_comparison/
├── 06_interchange_fee_structure/
├── 07_realtime_payment_adoption/
├── 08_cross_border_payment_flows/
├── 09_cbdc_design_comparison/
├── 10_payment_innovation_timeline/
├── 11_opening_cartoon/
└── 12_closing_cartoon/
```

---

## Key Files

| File | Purpose | Audience | Status |
|------|---------|----------|--------|
| `L03_full.tex` | Primary lecture deck (31 frames) | Instructors, students | Production |
| `L03_overview.tex` | Condensed overview (28 frames) | Quick reference | Production |
| `L03_deepdive.tex` | Analytical variant with appendix (17 frames) | Deep learners | Production |
| `L03_core.tex` | Extracted 10-frame core (self-contained) | Standalone teaching | Production |
| `L03_mini10.tex` | 11-frame teaser with TikZ diagrams | Promotional | Production |
| `L03_mini5.tex` | 5-slide arc (WHY > WHAT > HOW > WHERE > SO WHAT) | Lightning talks | Production |
| `*/chart.py` | Python generation scripts (matplotlib) | Regeneration | Production |
| `*/chart.pdf` | Compiled charts (10 + 2 cartoons = 12 total) | Embedded in slides | Production |

---

## Variants Guide

### For Instructors
- **L03_full.tex** — Use this in 90-minute sessions. Covers all 10 narrative roles with payment system mechanics, regulatory context, and closure.
- **L03_overview.tex** — Use this in 60-minute sessions. Three-zone structure emphasizes payment history, four-party model, and merchant economics.

### For Self-Study
- **L03_core.tex** — Self-contained, printable. Covers only the 10 essential frames (no dependency on preamble).
- **L03_deepdive.tex** — Deep dive with appendix for additional regulatory analysis and technical details.

### For Outreach/Promotion
- **L03_mini5.tex** — Ultra-short 5-slide teaser arc. No external dependencies (pure TikZ).
- **L03_mini10.tex** — Slightly expanded 11-frame version. Self-contained with inline TikZ diagrams.

---

## Graphics & Figures (12 Total)

All 12 figures live in chart subdirectories (flat in lecture dir). Each includes a Python script (`chart.py` or `cartoon.py`) and compiled PDF.

### Charts (10 analytical figures)

1. **01_payment_history_timeline** — Annotated timeline from barter (3000 BCE) through coinage, checks, wire transfers, credit cards, mobile wallets, CBDCs
2. **02_global_payment_trends** — Regional payment method preferences (card, mobile, cash, real-time) across developed and developing markets
3. **03_four_party_payment_model** — Cardholder, merchant, issuing bank, acquiring bank, card network relationships
4. **04_payment_lifecycle_flow** — Authorization → Clearing → Settlement workflow with timing and data flows
5. **05_merchant_cost_comparison** — Cost per $100 transacted across payment types (cash, check, card, mobile, ACH, real-time)
6. **06_interchange_fee_structure** — Merchant fee breakdown showing how interchange is distributed between network, issuer, acquirer
7. **07_realtime_payment_adoption** — UPI (India), PIX (Brazil), FedNow (US) volume and user growth comparison
8. **08_cross_border_payment_flows** — Correspondent banking chains, SWIFT, and cost structure for international remittances
9. **09_cbdc_design_comparison** — Design matrix showing offline capability, privacy, tiered access, and rate-bearing features
10. **10_payment_innovation_timeline** — Four disruption waves: cards, digital wallets, real-time rails, embedded payments

### Cartoons (2 XKCD-style illustrations)

11. **11_opening_cartoon** — Swedish cashier refusing cash payment: "Sorry, we don't accept that." Metaphor: cash obsolescence vs. legal tender.
12. **12_closing_cartoon** — (Purpose varies by lecture variant; supports reflection on payment system design and regulation)

---

## Generation & Compilation

### Slides
All `.tex` files compile with `pdflatex` (run twice for overlays):
```bash
pdflatex L03_full.tex && pdflatex L03_full.tex
```

**Dependencies:**
- **Full/Overview/DeepDive variants** require `../../_shared/preamble.tex` (colors, theme, metadata)
- **Core/Mini5/Mini10 variants** are self-contained (preamble embedded)

### Figures
Regenerate all charts from within the lecture directory:
```bash
cd slides/L03_Payments_and_Fintech
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

1. **Describe** the evolution of payment systems from barter to digital rails and real-time networks, explaining the forces driving each transition (Understand)
2. **Explain** the four-party payment model and the authorization, clearing, and settlement lifecycle for card and ACH transactions (Understand)
3. **Apply** a cost-analysis framework to compare merchant fees across payment types and evaluate the impact of interchange regulation (Apply)
4. **Analyze** how cross-border payment complexity and remittance costs affect financial inclusion in developing economies (Analyze)
5. **Evaluate** the design trade-offs in central bank digital currencies and stablecoins as future payment infrastructure (Evaluate)

---

## Integration Points

**Links from L01:**
- Lecture 1 covers fintech as a supply-side disruption across value chain
- L03 applies that lens to the largest fintech vertical (payments)

**Links from L02:**
- Lecture 2 explored behavioral design, choice architecture, and nudging
- L03 shows how payment UI design (tap-to-pay, rounding-up) embodies those principles in practice

**Links to L04/Later lectures:**
- Payment regulation (Durbin, PSD2) connects to broader regulatory frameworks (L04)
- KYC/AML in real-time payment networks bridges to RegTech (L04)
- Cross-border payments inform discussions of emerging-market fintech (future lectures)

**Assessments:**
- Quiz questions cover payment evolution, four-party model mechanics, merchant cost analysis, and CBDC design evaluation
- Exercises ask students to calculate merchant fees under different regulatory scenarios and design a payment rail
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

**When updating, generating, or debugging L03 slide decks:**

1. **Understand the variant system:**
   - `L03_full.tex`, `L03_overview.tex`, `L03_deepdive.tex` all use `\input{../../_shared/preamble.tex}` — centralizes theme, colors, and shared commands
   - `L03_core.tex`, `L03_mini10.tex`, `L03_mini5.tex` are self-contained — include all preamble, color definitions, and custom commands inline

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
   - Core/mini5/mini10: Self-contained; compile with `pdflatex L03_*.tex` directly
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
   - Charts use `CHART_METADATA` dictionary with keys: `title`, `type`, `section` (History/Four-Party/Merchant Economics/Regulation/Cross-Border/CBDC), `lecture_number`

2. **Chart types in L03:**
   - **Time series** (01 evolution timeline, 10 innovation timeline): Annotated timelines with milestones
   - **Diagram** (03 four-party model, 04 lifecycle flow, 06 interchange, 08 cross-border): Network or structural layout
   - **Comparison chart** (02 global trends, 05 merchant costs, 07 realtime adoption, 09 CBDC design): Bars, heatmaps, or matrices

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
   - Timeline milestones (when did X payment innovation emerge?)
   - Four-party model mechanics (which party bears the risk in a chargeback?)
   - Merchant cost analysis (how does interchange regulation affect small merchants?)
   - Cross-border corridors (what causes high remittance fees to developing countries?)
   - CBDC design (which design choice offers privacy while enabling CBDCs?)

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
| **Lecture** | L03 (Payments and Fintech) |
| **Subtitle** | From Cash to Digital: The Transformation of Money Movement |
| **Audience** | MSc Financial Technology, Spring 2026 |
| **Frames** | 31 (full) / 28 (overview) / 17 (deepdive) / 10 (core) / 11 (mini10) / 6 (mini5) |
| **Figures** | 12 (10 charts + 2 cartoons) |
| **Narrative Arc** | WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT |
| **Assessment** | Quizzes (Bloom's: Understand, Apply, Analyze, Evaluate) |
| **Prerequisite** | L01 (Fintech Foundations) |

---

## License & Attribution

All materials created for the Financial Technology course, University of Zurich, Spring 2026.

---

**Last updated:** 2026-03-01
**Maintainer:** Joerg Osterrieder
