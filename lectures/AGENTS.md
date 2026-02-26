<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-02-26 -->

# Lectures: Structure and Content

## Purpose

This directory contains all 7 lecture materials for the Financial Technology (FinTech) MSc course at the University of Zurich, taught by Joerg Osterrieder, Spring 2026.

Each lecture folder is self-contained, with:
- **6 slide variants** (full, overview, deepdive, core, mini10, mini5) as LaTeX PDFs
- **10-12 matplotlib charts** (generated from Python scripts)
- **2 cartoons** (opening and closing, XKCD style)
- **AGENTS.md** documentation for the lecture

**Current status:**
- L01, L02: Fully implemented
- L03-L07: Planned (metadata defined in `../course.yaml`)

---

## Implemented Lectures

### L01: Fintech Foundations and Overview

**Location:** `./L01_fintech_foundations/`

**Scope:** Introduces what fintech is, its historical evolution from electronic banking to embedded finance, the 2008 financial crisis as a catalyst, and the emerging collaboration models between traditional banks and fintech startups.

**Key topics:**
- Definition and characteristics of fintech
- Historical S-curve evolution (1950s → 2020s)
- Banking value chain disruption
- Partnership models (acquisition, partnership, licensing, API, white-label)
- Competitive advantages (speed/cost vs. scale/trust)
- Embedded finance architecture

**Narrative arc:** WHY (disruption tension) → WHAT (definition + evolution) → HOW (collaboration models) → WHERE (embedded finance) → SO WHAT (strategic implications)

**Frames:** 31 (full) | 27 (overview) | 15 (deepdive) | 10 (core) | 11 (mini10) | 6 (mini5)

**Figures:** 10 charts + 2 cartoons
1. Fintech evolution timeline (S-curve, 1950s–2020s)
2. Banking value chain disruption (unbundling)
3. Collaboration models matrix (4 types)
4. Fintech ecosystem overview (service categories)
5. Great recession as catalyst (timeline + impact)
6. Fintech investment growth (funding trends)
7. Bank-fintech partnership flow (relationship channels)
8. Embedded finance architecture (API diagram)
9. Fintech impact comparison (incumbent vs. startup)
10. Key concepts summary (taxonomy)
11. Opening cartoon (disruption tension)
12. Closing cartoon (reflection/takeaway)

**Dependencies:**
- Shared preamble: `../_shared/preamble.tex`
- Shared chart styles: `../_shared/chart_styles.py`

**See:** [`L01_fintech_foundations/AGENTS.md`](./L01_fintech_foundations/AGENTS.md)

---

### L02: Fintech Ecosystem

**Location:** `./L02_fintech_ecosystem/`

**Scope:** Shifts from supply-side strategy (L01) to demand-side behavior. Examines the fintech ecosystem through growth drivers, financial inclusion barriers, technology adoption patterns, and behavioral design mechanisms (choice architecture, nudging).

**Key topics:**
- Four drivers of fintech growth: regulation, technology, consumer demand, capital
- Financial inclusion: access barriers, capability gaps, behavioral factors, trust dimensions
- Technology adoption lifecycle (crossing the chasm)
- Choice architecture and nudging mechanisms
- Ethics of behavioral design (helpful vs. manipulative patterns)
- Trust in fintech vs. traditional banks vs. BigTech

**Narrative arc:** WHY (context) → FEEL (relevance) → WHAT (growth drivers + inclusion barriers) → HOW (adoption mechanisms) → WHERE (ecosystem landscape) → OBSTACLES (barriers) → MECHANISMS (nudging) → DARK SIDE (ethics) → SO WHAT (takeaway) → NEXT (action)

**Frames:** 31 (full) | 26 (overview) | 17 (deepdive) | 10 (core) | 11 (mini10) | 6 (mini5)

**Figures:** 10 charts + 2 cartoons
1. Fintech ecosystem map (hub + inner ring + outer ring)
2. Growth drivers dashboard (4 interconnected drivers)
3. Financial inclusion gap (banked vs. unbanked)
4. M-Pesa adoption flow (Kenya case study)
5. Trust framework comparison (banks vs. fintech vs. BigTech)
6. Technology adoption lifecycle (S-curve with chasm)
7. Adoption barriers matrix (access, capability, behavioral, institutional)
8. Nudging architecture (choice set, defaults, frames, anchors)
9. Choice architecture examples (real-world nudges and dark patterns)
10. Ecosystem stakeholder impact (value matrix)
11. Opening cartoon (mobile phone vs. bank branch)
12. Closing cartoon (reflection on behavioral design ethics)

**Lecture 2 Prerequisite:** L01 (students should understand fintech fundamentals before analyzing demand-side behavior)

**Dependencies:**
- Shared preamble: `../_shared/preamble.tex`
- Shared chart styles: `../_shared/chart_styles.py`
- L01 concepts (fintech definition, ecosystem structure)

**See:** [`L02_fintech_ecosystem/AGENTS.md`](./L02_fintech_ecosystem/AGENTS.md)

---

## Planned Lectures

### L03: Payments and Fintech

**Location:** `./L03_payments_fintech/` (not yet created)

**Status:** Metadata defined in `../course.yaml`

**Planned scope:** History of payment methods, global trends, payment process complexity, merchant cost burden, credit card regulation, future of settlement networks.

**Key topics:**
- History from barter to digital
- Current global trends
- Settlement layer complexity
- Interchange fees and regulation
- Real-time payment networks

**Figures:** Time series (payment trends), flowcharts (settlement), comparison bars (costs)

**Prerequisite:** L01

---

### L04: Fintech Security and Regulation (RegTech)

**Location:** `./L04_regtech_security/` (not yet created)

**Status:** Metadata defined in `../course.yaml`

**Planned scope:** Financial regulation perspectives, AML/KYC solutions, US fintech regulation, global regulatory landscape (EU, UK, Singapore), RegTech, regulatory sandboxes.

**Key topics:**
- Regulation vs. innovation tension
- AML/KYC frameworks
- Global regulatory variation
- Technology-driven compliance (RegTech)
- Embedded compliance and sandboxes

**Figures:** Flowcharts (regulatory flows), diagrams (KYC process), comparison bars (regional frameworks)

**Prerequisites:** L01, L02

---

### L05: Personal Finance and Wealth Management

**Location:** `./L05_personal_finance_wealth/` (not yet created)

**Status:** Metadata defined in `../course.yaml`

**Planned scope:** Robo-advisors, personal finance tools, AI/ML in wealth management, fintech case studies, fee structures (traditional vs. robo-advisory).

**Key topics:**
- Automated investment platforms
- Personal finance management apps
- AI and machine learning applications
- Fee structures and cost comparison
- Case studies of fintech wealth managers

**Figures:** Comparison bars (fees), flowcharts (robo-advisor logic), diagrams (platform architecture)

**Prerequisites:** L01, L02

---

### L06: Insurtech

**Location:** `./L06_insurtech/` (not yet created)

**Status:** Metadata defined in `../course.yaml`

**Planned scope:** Insurance innovation through technology, digital platforms, underwriting and claims automation, insurtech case studies, parametric insurance, smart contracts in insurance.

**Key topics:**
- Digital insurance distribution
- Underwriting automation
- Claims processing innovation
- Parametric insurance
- Blockchain in insurance contracts

**Figures:** Flowcharts (claims process), diagrams (underwriting architecture), comparison bars (market adoption)

**Prerequisites:** L01, L02

---

### L07: The Technology of FinTech

**Location:** `./L07_technology_fintech/` (not yet created)

**Status:** Metadata defined in `../course.yaml`

**Planned scope:** Foundational technologies underpinning fintech: identity, privacy, blockchain, encryption, big data, analytics, AI, decision support, smartphones, cloud computing, APIs.

**Key topics:**
- Identity and privacy in digital finance
- Blockchain and cryptography fundamentals
- Big data and analytics
- Artificial intelligence and automation
- Cloud infrastructure and APIs

**Figures:** Diagrams (architecture), flowcharts (data pipelines), concept illustrations (blockchain)

**Prerequisites:** L01-L06

---

## Directory Structure

```
lectures/
├── AGENTS.md                          ← You are here
├── L01_fintech_foundations/
│   ├── AGENTS.md
│   ├── slides/
│   │   ├── AGENTS.md
│   │   ├── L01_full.tex
│   │   ├── L01_overview.tex
│   │   ├── L01_deepdive.tex
│   │   ├── L01_core.tex
│   │   ├── L01_mini10.tex
│   │   ├── L01_mini5.tex
│   │   └── *.pdf (compiled variants)
│   ├── figures/
│   │   ├── AGENTS.md
│   │   ├── 01_fintech_evolution_timeline/
│   │   │   ├── chart.py
│   │   │   └── chart.pdf
│   │   ├── 02_banking_value_chain_disruption/
│   │   │   ├── chart.py
│   │   │   └── chart.pdf
│   │   ├── ... (8 more chart dirs)
│   │   ├── 11_opening_cartoon/
│   │   │   ├── cartoon.py
│   │   │   └── cartoon.pdf
│   │   └── 12_closing_cartoon/
│   │       ├── cartoon.py
│   │       └── cartoon.pdf
│   ├── exercises/
│   └── quizzes/
│
├── L02_fintech_ecosystem/
│   ├── AGENTS.md
│   ├── slides/
│   │   ├── AGENTS.md
│   │   ├── L02_full.tex
│   │   ├── ... (5 more variants)
│   │   └── *.pdf (compiled variants)
│   ├── figures/
│   │   ├── AGENTS.md
│   │   ├── 01_fintech_ecosystem_map/
│   │   │   ├── chart.py
│   │   │   └── chart.pdf
│   │   ├── ... (8 more chart dirs)
│   │   └── 12_closing_cartoon/
│   │       ├── cartoon.py
│   │       └── cartoon.pdf
│   ├── exercises/
│   └── quizzes/
│
├── L03_payments_fintech/              ← Planned
├── L04_regtech_security/              ← Planned
├── L05_personal_finance_wealth/       ← Planned
├── L06_insurtech/                     ← Planned
└── L07_technology_fintech/            ← Planned
```

---

## Creation Workflow for New Lectures

When creating L03 and beyond, follow this structure:

### 1. Create folder
```bash
mkdir L0N_[slug]
cd L0N_[slug]
```

### 2. Create subdirectories
```bash
mkdir slides figures exercises quizzes
```

### 3. Create slide variants

Each lecture needs 6 variants:

- **L0N_full.tex** (80+ min): Full narrative arc with 10 roles (WHY, FEEL, WHAT, CASE, HOW, RISK, WHERE, IMPACT, SO WHAT, ACT)
- **L0N_overview.tex** (50 min): Three-zone overview structure
- **L0N_deepdive.tex** (90+ min): Extended analysis with appendix
- **L0N_core.tex** (30 min): Self-contained, 10-frame core (no external imports)
- **L0N_mini10.tex** (10 min): Self-contained teaser (11 frames total with title)
- **L0N_mini5.tex** (5 min): Self-contained ultra-short arc (6 frames: WHY, WHAT, HOW, WHERE, SO WHAT)

**Full/overview/deepdive templates:**
```latex
\input{../../../_shared/preamble.tex}

\title{Lecture N: [Title]}
\subtitle{[Subtitle]}

\begin{document}

% --- Frame 1: Title ---
\begin{frame}
  \titlepage
\end{frame}

% ... more frames ...

\end{document}
```

**Self-contained templates (core/mini):**
```latex
\documentclass[aspectratio=169, 11pt]{beamer}
\usetheme{Madrid}
\usecolortheme{whale}

% Embedded preamble (copy from _shared/preamble.tex)
\usepackage{...}
\definecolor{mlpurple}{HTML}{9467BD}
% ... all color and package definitions ...

\title{Lecture N: [Title]}
\subtitle{[Subtitle]}

\begin{document}
% ... frames ...
\end{document}
```

### 4. Create figures

Each figure subdirectory:
```
figures/
├── 01_[descriptor]/
│   ├── chart.py
│   └── chart.pdf  ← Generated
├── ... (9 more charts)
├── 11_opening_cartoon/
│   ├── cartoon.py
│   └── cartoon.pdf ← Generated
└── 12_closing_cartoon/
    ├── cartoon.py
    └── cartoon.pdf ← Generated
```

**Chart template:**
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

from chart_styles import V4_COLORS, apply_v4_style, save_chart
import matplotlib.pyplot as plt
import numpy as np

# Your chart code here
fig, ax = plt.subplots(figsize=(10, 6))
# ... plotting ...
ax = apply_v4_style(ax, title='Title', xlabel='X', ylabel='Y')
save_chart(fig, filename='chart.pdf')
```

### 5. Create AGENTS.md

Create `L0N_[slug]/AGENTS.md` following the structure of L01 or L02 AGENTS files.

### 6. Create slides/AGENTS.md

Document the slide variants in `L0N_[slug]/slides/AGENTS.md`.

### 7. Create figures/AGENTS.md

Document the charts in `L0N_[slug]/figures/AGENTS.md`.

---

## Compilation Workflow

### Full/Overview/Deepdive Variants

**Requires:** `../_shared/preamble.tex`

```bash
cd L0N_[slug]/slides
pdflatex L0N_full.tex
pdflatex L0N_full.tex  # Run twice for overlays
pdflatex L0N_overview.tex
pdflatex L0N_overview.tex
pdflatex L0N_deepdive.tex
pdflatex L0N_deepdive.tex
```

### Core/Mini Variants

**Self-contained:** No external dependencies

```bash
cd L0N_[slug]/slides
pdflatex L0N_core.tex
pdflatex L0N_core.tex
pdflatex L0N_mini10.tex
pdflatex L0N_mini10.tex
pdflatex L0N_mini5.tex
pdflatex L0N_mini5.tex
```

### Figures

```bash
cd L0N_[slug]/figures
for dir in 0*/; do python "$dir/chart.py"; done
for dir in 1*/; do python "$dir/cartoon.py"; done
```

---

## Course Prerequisites

Based on `../course.yaml`:

| Lecture | Prerequisites |
|---------|---------------|
| L01 | None |
| L02 | L01 |
| L03 | L01 |
| L04 | L01, L02 |
| L05 | L01, L02 |
| L06 | L01, L02 |
| L07 | L01, L02, L03, L04, L05, L06 |

---

## Assessment Integration

Each lecture includes:

- **Learning objectives** mapped to Bloom's levels: Understand, Apply, Analyze, Evaluate
- **Quiz questions** (20 standard + 20 advanced per lecture) aligned to objectives
- **Exercises** (if present in `exercises/`) for hands-on learning
- **Case studies** referenced in slides and assessments

**Quiz levels per lecture:**

| Level | Standard Count | Advanced Count | Bloom's Levels |
|-------|---|---|---|
| Standard | 20 | - | Understand (4), Apply (8), Analyze (6), Evaluate (2) |
| Advanced | - | 20 | Apply (4), Analyze (8), Evaluate (6), Create (2) |

---

## Website Integration

PDFs and assets from lectures are published to the website:

- **downloads/**: All 6 variants per lecture (e.g., `L01_full.pdf`, `L01_mini5.pdf`)
- **charts/L[N]/**: PNG exports of all figures (PDF→PNG conversion)
- **galleries/images/L[N]/**: Slide gallery previews by variant (mini5, mini10, core, extended, full)

---

## Maintenance Notes

### For Lecture Creators

- Update frame counts in AGENTS.md headers if content changes
- Regenerate charts when data sources are updated
- Ensure mini variants have **zero overfull vbox warnings** on compilation
- Test all 6 variants before committing

### For AI Agents

**Common patterns across all lectures:**
- 10-role narrative arc for full variants (WHY, FEEL, WHAT, CASE, HOW, RISK, WHERE, IMPACT, SO WHAT, ACT)
- Self-contained variants (core, mini10, mini5) embed their own preamble
- All charts use matplotlib with fallback color definitions
- Chart scripts import from `../_shared/chart_styles.py` with `sys.path.insert(0, ...)`
- Opening and closing cartoons use XKCD style (`with plt.xkcd():`)

**Testing before commit:**
- [ ] All 6 LaTeX variants compile without errors
- [ ] Mini variants have zero overfull box warnings
- [ ] All chart.py scripts run and generate PDFs
- [ ] All \includegraphics paths resolve correctly
- [ ] Learning objectives match quiz question levels
- [ ] AGENTS.md metadata is accurate

---

## Dependencies

- **Parent:** `../AGENTS.md` (course overview)
- **Siblings:**
  - `../_shared/preamble.tex` — Master LaTeX preamble (used by full/overview/deepdive variants)
  - `../_shared/chart_styles.py` — Matplotlib styling (used by all chart scripts)
  - `../course.yaml` — Course metadata (lecture titles, topics, prerequisites)

---

## Quick Links

- **Course Overview:** `../AGENTS.md`
- **Shared Assets:** `../_shared/AGENTS.md`
- **Website:** `../docs/AGENTS.md`
- **L01 Details:** `./L01_fintech_foundations/AGENTS.md`
- **L02 Details:** `./L02_fintech_ecosystem/AGENTS.md`

---

**Last Updated:** 2026-02-26

**Maintainer:** Joerg Osterrieder, University of Zurich, Department of Finance
