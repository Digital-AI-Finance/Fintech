<!-- Generated: 2026-02-26 -->

# Fintech Course Materials

## Purpose

This repository contains complete course materials for **Financial Technology (FinTech)** — an MSc-level 7-lecture course at the University of Zurich, Department of Finance. Taught by Joerg Osterrieder, Spring 2026.

The project generates:
- **6 LaTeX Beamer slide variants** per lecture (full, overview, deepdive, core, mini10, mini5)
- **12+ matplotlib charts** per lecture with consistent V4 color palette
- **Interactive HTML quizzes** with 20 questions per standard/advanced level
- **Slide galleries** (PNG exports for web preview)
- **Complete course website** with downloadable PDFs and visual galleries

## Course Structure

| Module | Lectures | Focus |
|--------|----------|-------|
| **Foundations** | 1, 2 | Fintech ecosystem, growth, social impact, behavioral dimensions |
| **Financial Services** | 3, 5 | Payments, personal finance, wealth management |
| **Regulation & Insurance** | 4, 6 | RegTech, compliance, insurtech |
| **Technology** | 7 | Blockchain, AI, cloud, big data, privacy |

**Course Contact:** joerg.osterrieder@uzh.ch

## Key Files & Directories

| Location | Contents |
|----------|----------|
| `config.yaml` | Master course configuration: metadata, module structure, lecture topics, theme colors |
| `_shared/` | Shared LaTeX preamble and Python chart styling (see [`_shared/AGENTS.md`](./_shared/AGENTS.md)) |
| `slides/` | All lecture content organized by lecture number (see [`slides/AGENTS.md`](./slides/AGENTS.md)) |
| `docs/` | Static course website: HTML pages, PDF downloads, chart galleries, slide galleries |

## Project Architecture

### Lecture Pipeline

Each lecture follows a **3-stage pipeline**:

**Stage 1: Chart Generation**
```
slides/L[N]_*/[N]_*_title/chart.py
  └─> runs matplotlib script
  └─> imports V4_COLORS from _shared/chart_styles.py
  └─> generates chart.pdf (300 dpi)
  └─> manually convert to PNG for website
```

**Stage 2: LaTeX Compilation**
```
slides/L[N]_*/L[N]_variant.tex
  ├─> full, overview, deepdive: \input{../../_shared/preamble.tex}
  ├─> core, mini10, mini5: self-contained preamble (no external imports)
  ├─> \includegraphics{[N]_*/chart.pdf}
  └─> pdflatex (run twice for overlays/navigation)
```

**Stage 3: Web Assets**
```
docs/
  ├─> slides/pdf/L[N]_*.pdf (copied from slides/*)
  ├─> slides/images/L[N]/*.png (PDF→PNG conversion)
  └─> galleries/images/L[N]/* (pdftoimage or similar)
```

### Slide Variants Explained

Each lecture produces **6 distinct PDF variants**:

| Variant | Duration | Purpose | Preamble | Graphics | Use Case |
|---------|----------|---------|----------|----------|----------|
| **full** | 80+ min | 10-role narrative arc | shared | all charts | complete lecture |
| **overview** | 50 min | executive summary | shared | key charts only | intro/refresher |
| **deepdive** | 90+ min | extended analysis | shared | all charts | deeper topics |
| **core** | 30 min | essentials only | self-contained | core charts | review session |
| **mini10** | 10 min | elevator pitch | self-contained | minimal | social media, promotions |
| **mini5** | 5 min | teaser arc | self-contained | no graphics | lead generation |

**Self-contained variants** (core, mini10, mini5) embed their own LaTeX preamble so they compile independently without `../../_shared/preamble.tex`.

### Color Palette

The course uses the **V4 Fintech Palette** (matplotlib + LaTeX):

```
MLTEAL:   #0D7377  (primary, nav, structure)
MLCYAN:   #14BDEB  (hero gradient end, accent)
MLORANGE: #FF7F0E  (accent, bar charts)
MLPURPLE: #9467BD  (secondary highlight)
MLBLUE:   #1F77B4  (data series 1)
MLRED:    #D62728  (data series 2, alerts)
MLGREEN:  #2CA02C  (module 1 indicator)
MLGRAY:   #7F7F7F  (neutral, text)
```

Defined in:
- LaTeX: `_shared/preamble.tex` (lines 36-43)
- Python: `_shared/chart_styles.py` (V4_COLORS dict)

### Website Theme

The course website uses a consistent design system:

- **Navigation**: `#1a1a4e` (dark navy)
- **Hero gradient**: `#0D7377` → `#14BDEB` (teal to cyan)
- **Accent**: `#FF7F0E` (orange)
- **Typography**: System font stack (Segoe UI, Helvetica, Arial, sans-serif)
- **Layout**: Self-contained HTML pages (no external CSS frameworks)

## Working in This Repository

### For Lecture Content Creators

When adding a new lecture:

1. **Create lecture folder:** `slides/L[N]_[Slug]/`
2. **Charts are flat** in the lecture dir (no separate figures/ subdir)
3. **Generate charts:** Run `python [N]_*/chart.py` in the lecture folder
4. **Create slide variants:**
   - `L[N]_full.tex` uses `\input{../../_shared/preamble.tex}`
   - `L[N]_mini5.tex` includes embedded preamble (no imports)
5. **Compile LaTeX:**
   ```bash
   cd slides/L01_Fintech_Foundations
   pdflatex L01_full.tex
   pdflatex L01_full.tex  # run twice for overlays
   ```
6. **Verify:**
   - Check for zero overfull vbox warnings in mini variants
   - Ensure all `\includegraphics` paths resolve correctly

### For Chart Creators

All chart scripts follow a consistent pattern:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

from chart_styles import V4_COLORS, apply_v4_style, save_chart
import matplotlib.pyplot as plt

# Your chart code here, using V4_COLORS['MLTEAL'] etc.

fig, ax = plt.subplots(figsize=(10, 6))
# ... plotting code ...
ax = apply_v4_style(ax, title='Your Title', xlabel='X', ylabel='Y')
save_chart(fig, filename='chart.pdf')
```

**Important:**
- All charts save as **PDF** (300 dpi) in their chart subdirectory
- PNG conversion for website happens separately (manual or automated)
- Fallback color definitions included in case `chart_styles.py` import fails

### For Website Developers

Website structure:

```
docs/
├── slides/pdf/        # PDF links (copy from slides/)
├── slides/images/L[N]/  # PNG versions of charts (one per lecture)
├── galleries/images/  # Slide gallery images by variant
│   └── L[N]/mini5/, mini10/, core/, extended/, full/
└── html files        # Static pages (inline CSS/JS, no frameworks)
```

**HTML pages use KaTeX CDN** for math rendering. No external frameworks required.

## Testing & Verification

Before committing changes:

- **LaTeX compilation:**
  ```bash
  cd slides/L[N]_[Slug]
  pdflatex L[N]_full.tex
  pdflatex L[N]_full.tex
  ```
  Check log for `Overfull \hbox` or `Overfull \vbox` warnings. Mini variants must have zero warnings.

- **Chart generation:**
  ```bash
  cd slides/L[N]_[Slug]/[N]_*
  python chart.py
  ```
  Each script must output `Saved: chart.pdf` without errors.

- **HTML rendering:** Open website pages in a browser; verify math renders correctly via KaTeX.

## Dependencies

### External Tools
- **LaTeX**: `pdflatex` with Beamer, TikZ, pgfplots packages
- **Python 3**: matplotlib, numpy
- **PDF→PNG**: pdftoppm (MiKTeX) or similar tool
- **Web**: KaTeX CDN (for math rendering in HTML)

### Project Dependencies
- `_shared/preamble.tex` — Master LaTeX preamble (Beamer theme, colors, custom commands)
- `_shared/chart_styles.py` — Matplotlib styling (V4_COLORS, apply_v4_style, save_chart)

## Course Metadata

From `config.yaml`:

- **Institution**: University of Zurich, Department of Finance
- **Level**: MSc
- **Semester**: Spring 2026
- **Instructor**: Joerg Osterrieder (joerg.osterrieder@uzh.ch)
- **Repository**: digital-ai-finance/Fintech (public)
- **Assessment**: Quizzes only (no projects)
  - Standard: 20 questions per lecture (Understand, Apply, Analyze, Evaluate)
  - Advanced: 20 questions per lecture (Apply, Analyze, Evaluate, Create)

## For AI Agents

### Common Patterns

- **10-role narrative arc**: Full lectures follow a consistent structure: **WHY** (context) → **FEEL** (relevance) → **WHAT** (definition) → **CASE** (example) → **HOW** (mechanism) → **RISK** (challenges) → **WHERE** (landscape) → **IMPACT** (significance) → **SO WHAT** (takeaway) → **ACT** (next steps)

- **Chart naming**: Figures follow pattern `[N]_[slug]/chart.py` where N is lecture number (zero-padded) and slug is kebab-case descriptor. Charts live flat inside the lecture directory.

- **Self-contained variants**: mini5, mini10, and core variants must include a full LaTeX preamble and never rely on `\input{../../_shared/preamble.tex}`.

- **Graphics imports**: Full/overview/deepdive variants use `\includegraphics{[N]_*/chart.pdf}` with relative paths from the lecture directory.

- **Path patterns for chart imports**: Matplotlib charts use `sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))` to dynamically locate shared resources.

### Testing Requirements

- LaTeX mini variants must compile with **zero overfull box warnings**
- All `\includegraphics` paths must resolve without errors
- Chart scripts must run without ImportError (fallback color definitions provided)
- Website HTML pages must render correctly with math via KaTeX CDN

### Related Documentation

- [`_shared/AGENTS.md`](./_shared/AGENTS.md) — Shared LaTeX preamble and chart styling
- [`slides/AGENTS.md`](./slides/AGENTS.md) — Lecture-specific structure and L01/L02 details
