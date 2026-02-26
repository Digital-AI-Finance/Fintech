# L02: Fintech Ecosystem

<!-- Parent: ../AGENTS.md -->

**Lecture 2 of the Financial Technology MSc course (Spring 2026)**

## Overview

This lecture examines the fintech ecosystem through **demand-side** and **behavioral** lenses. After establishing what fintech is and how supply-side players collaborate (L01), L02 investigates who fintech serves, why adoption varies, and how product design shapes financial decisions.

**Core themes:**
- Four drivers of fintech growth (regulation, technology, consumer demand, capital availability)
- Financial inclusion barriers (access, capability, behavioral, trust)
- Technology adoption lifecycle and crossing the chasm
- Choice architecture and nudging mechanisms
- Ethics of behavioral design (helpful vs. manipulative)

**Bloom's levels covered:** Understand, Apply, Analyze, Evaluate

**Key frames:** 31 (full) | 26 (overview) | 17 (deepdive) | 10 (core) | 11 (mini10) | 6 (mini5)

**Narrative structure:** 10-role arc (WHY → FEEL → WHAT → HOW → WHERE → OBSTACLES → MECHANISMS → DARK SIDE → SO WHAT → NEXT)

---

## Directory Structure

```
L02_fintech_ecosystem/
├── AGENTS.md (this file)
├── slides/
│   ├── AGENTS.md
│   ├── L02_full.tex         (31 frames, full narrative)
│   ├── L02_overview.tex     (26 frames, three-zone structure)
│   ├── L02_deepdive.tex     (17 frames + appendix)
│   ├── L02_core.tex         (10 frames, self-contained core)
│   ├── L02_mini10.tex       (11 frames, self-contained teaser)
│   ├── L02_mini5.tex        (6 frames, 5-slide arc)
│   ├── L02_full.pdf
│   ├── L02_overview.pdf
│   ├── L02_deepdive.pdf
│   ├── L02_core.pdf
│   ├── L02_mini10.pdf
│   └── L02_mini5.pdf
├── figures/
│   ├── AGENTS.md
│   ├── 01_fintech_ecosystem_map/
│   ├── 02_growth_drivers_dashboard/
│   ├── 03_financial_inclusion_gap/
│   ├── 04_mpesa_adoption_flow/
│   ├── 05_trust_framework_comparison/
│   ├── 06_technology_adoption_lifecycle/
│   ├── 07_adoption_barriers_matrix/
│   ├── 08_nudging_architecture/
│   ├── 09_choice_architecture_examples/
│   ├── 10_ecosystem_stakeholder_impact/
│   ├── 11_opening_cartoon/
│   └── 12_closing_cartoon/
├── exercises/ (may be empty—exercises referenced in docs/)
└── quizzes/ (may be empty—quiz source in docs/)
```

---

## Key Files

| File | Purpose | Audience | Status |
|------|---------|----------|--------|
| `slides/L02_full.tex` | Primary lecture deck (31 frames) | Instructors, students | Production |
| `slides/L02_overview.tex` | Condensed overview (26 frames) | Quick reference | Production |
| `slides/L02_deepdive.tex` | Analytical variant with appendix (17 frames) | Deep learners | Production |
| `slides/L02_core.tex` | Extracted 10-frame core (self-contained) | Standalone teaching | Production |
| `slides/L02_mini10.tex` | 11-frame teaser with TikZ diagrams | Promotional | Production |
| `slides/L02_mini5.tex` | 5-slide arc (WHY > WHAT > HOW > WHERE > SO WHAT) | Lightning talks | Production |
| `figures/*/chart.py` | Python generation scripts (matplotlib) | Regeneration | Production |
| `figures/*/chart.pdf` | Compiled charts (10 + 2 cartoons = 12 total) | Embedded in slides | Production |

---

## Variants Guide

### For Instructors
- **L02_full.tex** — Use this in 90-minute sessions. Covers all 10 narrative roles with personal exercises, bridging from L01, and closure.
- **L02_overview.tex** — Use this in 60-minute sessions. Three-zone structure emphasizes growth drivers, inclusion barriers, and behavioral mechanisms.

### For Self-Study
- **L02_core.tex** — Self-contained, printable. Covers only the 10 essential frames (no dependency on preamble).
- **L02_deepdive.tex** — Deep dive with appendix for additional analysis and references.

### For Outreach/Promotion
- **L02_mini5.tex** — Ultra-short 5-slide teaser arc. No external dependencies (pure TikZ).
- **L02_mini10.tex** — Slightly expanded 11-frame version. Self-contained with inline TikZ diagrams.

---

## Graphics & Figures (12 Total)

All 12 figures live in `figures/` subdirectories. Each includes a Python script (`chart.py` or `cartoon.py`) and compiled PDF.

### Charts (10 analytical figures)

1. **01_fintech_ecosystem_map** — Central hub + inner ring (players) + outer ring (customer segments)
2. **02_growth_drivers_dashboard** — Four drivers interconnected (regulation, technology, demand, capital)
3. **03_financial_inclusion_gap** — Global unbanked vs. banked populations and access barriers
4. **04_mpesa_adoption_flow** — M-Pesa as adoption case study (Kenya, unbanked to active user)
5. **05_trust_framework_comparison** — Trust dimensions across traditional banks, fintech, BigTech
6. **06_technology_adoption_lifecycle** — S-curve (innovators → early adopters → chasm → early majority)
7. **07_adoption_barriers_matrix** — 2x2 matrix of access barriers (structural, behavioral, informational, institutional)
8. **08_nudging_architecture** — Decision architecture with choice set, defaults, frames, anchors
9. **09_choice_architecture_examples** — Real-world nudging examples (rounding-up savings, dark patterns)
10. **10_ecosystem_stakeholder_impact** — Stakeholder value matrix (banks, consumers, regulators, platforms)

### Cartoons (2 XKCD-style illustrations)

11. **11_opening_cartoon** — Farmer with mobile phone, bank with "CLOSED" sign. Metaphor: mobile banking as universal access.
12. **12_closing_cartoon** — (Purpose varies by lecture variant; supports reflection on behavioral design ethics)

---

## Generation & Compilation

### Slides
All `.tex` files compile with `pdflatex` (run twice for overlays):
```bash
pdflatex L02_full.tex && pdflatex L02_full.tex
```

**Dependencies:**
- **Full/Overview/DeepDive variants** require `../../../_shared/preamble.tex` (colors, theme, metadata)
- **Core/Mini5/Mini10 variants** are self-contained (preamble embedded)

### Figures
Regenerate all charts:
```bash
cd figures
for dir in 0*/; do python "$dir/chart.py"; done
for dir in 1*/; do python "$dir/cartoon.py"; done
```

**Dependencies:**
- All scripts import `_shared/chart_styles.py` (V4_COLORS, apply_v4_style, save_chart)
- Fallback color definitions and functions embedded if import fails
- Output: `chart.pdf` or `cartoon.pdf` in each subdirectory

---

## Instructional Goals

Students will be able to:

1. **Identify** the four drivers of fintech growth and explain their interdependence (Understand)
2. **Explain** why financial inclusion remains incomplete despite technological progress, distinguishing access, capability, behavioral, and trust barriers (Understand)
3. **Apply** the technology adoption lifecycle to predict which fintech products will cross the chasm and which will stall (Apply)
4. **Analyze** how choice architecture and nudging mechanisms shape financial decisions for good and for ill (Analyze)
5. **Evaluate** the ethical boundary between helpful nudging and manipulative dark patterns in financial product design (Evaluate)

---

## Integration Points

**Links from L01:**
- Lecture 1 covers supply-side strategy (what fintech is, origins, bank-fintech collaboration)
- L02 shifts perspective to demand side (who benefits, why adoption varies, how design shapes behavior)

**Links to L03/Later lectures:**
- Understanding behavioral economics and choice architecture enables deeper analysis of regulatory frameworks (L03)
- Inclusion barriers inform discussions of remittances, microfinance, and emerging-market fintech (L04+)

**Assessments:**
- Quiz questions cover growth drivers, adoption barriers, and ethical evaluation of design choices
- Exercises ask students to identify nudges in their own financial apps and debate design tradeoffs
- Workshops (in `exercises/`) simulate product design decisions under inclusion-protection constraints

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

- **Variants use `\input{../../../_shared/preamble.tex}`** — These depend on a global preamble (Beamer theme, colors, commands). Ensure the path exists.
- **Mini variants are self-contained** — No external dependencies; can be compiled in isolation or emailed as standalone PDFs.
- **All figures use matplotlib with fallback color definitions** — If `_shared/chart_styles.py` is unavailable, charts still compile using embedded V4_COLORS and helper functions.
- **XKCD cartoons use `with plt.xkcd():`** — This is a matplotlib style context; no external libraries needed.

---

## License & Attribution

All materials created for the Financial Technology course, University of Zurich, Spring 2026.

---

**Last updated:** 2026-02-26
**Maintainer:** Joerg Osterrieder
