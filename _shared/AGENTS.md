<!-- Parent: ../AGENTS.md -->
<!-- Generated: 2026-02-26 -->

# Shared Assets: LaTeX Preamble & Chart Styling

## Purpose

This directory contains **shared, reusable assets** used by all 7 lectures in the Fintech course. All lectures import from these files to maintain visual and thematic consistency across the course.

## Files

### `preamble.tex`

The master **LaTeX Beamer preamble** — imported by all full, overview, and deepdive lecture variants.

**Status**: Single source of truth for:
- Beamer theme (Madrid) and color theme (whale)
- LaTeX packages (TikZ, pgfplots, amsmath, hyperref, etc.)
- V4 Fintech color palette (8 colors)
- Custom commands (`\bottomnote`, footnotes, etc.)
- Navigation bars, title formatting, slide layouts

**How lectures use it:**
```latex
% In slides/L[N]_[Slug]/L[N]_full.tex:
\input{../../_shared/preamble.tex}

\subtitle{Understanding the Revolution in Financial Services}

\begin{document}
% ... slide content ...
\end{document}
```

**Color Definitions** (lines 34-50 of preamble.tex):
```latex
\definecolor{MLPURPLE}{HTML}{9467BD}
\definecolor{MLBLUE}{HTML}{1F77B4}
\definecolor{MLRED}{HTML}{D62728}
\definecolor{MLORANGE}{HTML}{FF7F0E}
\definecolor{MLGREEN}{HTML}{2CA02C}
\definecolor{MLGRAY}{HTML}{7F7F7F}
\definecolor{MLTEAL}{HTML}{0D7377}
\definecolor{MLCYAN}{HTML}{14BDEB}

% Lowercase aliases for use in \textcolor{}
\colorlet{mlpurple}{MLPURPLE}
\colorlet{mlblue}{MLBLUE}
% ... etc ...
```

**Key Packages**:
- `\usepackage{tikz}` + `\usetikzlibrary{arrows.meta, positioning, shapes.geometric, calc, decorations.pathmorphing}`
- `\usepackage{pgfplots}` with `\pgfplotsset{compat=1.18}`
- `\usepackage{booktabs}` for tables
- `\usepackage{multicol}` for multi-column layouts
- `\usepackage{amsmath}` for math mode

**Custom Commands**:
- `\bottomnote{text}` — Adds a note bar at the bottom of a slide (typically for learning objectives, metadata, or discussion prompts)

**Modifying the preamble:**
- Only edit `preamble.tex` if you need to change something that affects **all lectures**
- For lecture-specific customizations, define commands in the lecture's `.tex` file instead
- Always test with multiple lecture variants (full and mini5) after editing

---

### `chart_styles.py`

The master **matplotlib styling module** — imported by all chart scripts to ensure visual consistency.

**Status**: Single source of truth for:
- V4 Fintech color palette (8 colors + 2 extended colors)
- Color cycle order
- Plot aesthetics (fonts, spines, grid, DPI)
- PDF export settings

**How chart scripts use it:**
```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))

from chart_styles import V4_COLORS, apply_v4_style, save_chart

# Use colors in plotting
plt.bar(x, y, color=V4_COLORS['MLTEAL'])

# Apply styling
ax = apply_v4_style(ax, title='My Chart', xlabel='X', ylabel='Y')

# Save as PDF
save_chart(fig, filename='chart.pdf')
```

**V4_COLORS Dictionary**:
```python
V4_COLORS = {
    'MLPURPLE': '#9467BD',   # secondary highlight
    'MLBLUE': '#1F77B4',     # data series 1
    'MLRED': '#D62728',      # data series 2, alerts
    'MLORANGE': '#FF7F0E',   # accent, bar charts (module Financial Services)
    'MLGREEN': '#2CA02C',    # module Foundations indicator
    'MLGRAY': '#7F7F7F',     # neutral, muted text
    'MLTEAL': '#0D7377',     # primary color, structure, nav
    'MLCYAN': '#14BDEB',     # hero gradient end, light accent
    'MLYELLOW': '#BCBD22',   # extended palette
    'MLPINK': '#E377C2',     # extended palette
    'MLBROWN': '#8C564B',    # extended palette
}
```

**COLOR_CYCLE** (ordered list for multi-series charts):
```python
[MLTEAL, MLORANGE, MLPURPLE, MLRED, MLBLUE, MLGREEN, MLCYAN, MLYELLOW, MLPINK]
```

**`apply_v4_style(ax, title='', xlabel='', ylabel='')` Function**:
Applies consistent styling to a matplotlib axes object:
- Bold title (14pt, dark gray #333333)
- Axis labels (11pt, medium gray #555555)
- Removes top and right spines (clean look)
- Gray spines (#CCCCCC)
- Gray tick labels (#555555)
- White background

**`save_chart(fig, filename='chart.pdf', dpi=300)` Function**:
- Applies tight layout
- Saves as PDF with white background
- Uses 300 dpi for print quality
- Prints "Saved: {filename}" to stdout
- Closes the figure to free memory

**Fallback Implementation**:
Chart scripts include fallback color and styling definitions (lines 19-40) in case `chart_styles.py` cannot be imported. This ensures robustness if a chart script runs in isolation or if the import path is incorrect.

```python
try:
    from chart_styles import V4_COLORS, apply_v4_style, save_chart
except ImportError:
    # Define colors and functions locally
    V4_COLORS = { ... }
    def apply_v4_style(ax, ...): ...
    def save_chart(fig, ...): ...
```

**Modifying chart_styles.py**:
- Only edit if you need to change colors or styling for **all charts**
- Changes here affect all 7 lectures immediately
- Always test by running a sample chart script after editing
- Document color purpose comments for future maintainers

---

## Integration Points

### LaTeX + Matplotlib Colors

The same color palette is used in both systems, enabling seamless visual integration:

| Element | LaTeX | Matplotlib | Use |
|---------|-------|------------|-----|
| Primary structure | `\mlpurple` | `V4_COLORS['MLPURPLE']` | titles, emphasis |
| Navigation | `\mlteal` | `V4_COLORS['MLTEAL']` | nav bars, primary accents |
| Accent | `\mlorange` | `V4_COLORS['MLORANGE']` | highlights, bar charts |
| Charts (series 1) | `\mlblue` | `V4_COLORS['MLBLUE']` | line plots, data |
| Charts (series 2) | `\mlred` | `V4_COLORS['MLRED']` | line plots, alerts |

### Chart Script Patterns

All 7 lectures follow this pattern for chart generation:

```
slides/L[N]_[Topic]/
├── [N]_01_[descriptor]/
│   ├── chart.py          ← Script that imports from _shared
│   └── chart.pdf         ← Output (committed to repo)
├── [N]_02_[descriptor]/
│   ├── chart.py
│   └── chart.pdf
├── ...
├── L[N]_full.tex         ← Imports ../../_shared/preamble.tex
├── L[N]_mini5.tex        ← Self-contained (no imports)
└── ...
```

**Key convention**: Chart scripts always use the path pattern:
```python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '_shared'))
```

This allows chart scripts to run from any lecture directory without modification.

---

## Best Practices

### When Adding a New Color

1. Add to `V4_COLORS` in `chart_styles.py`
2. Add corresponding `\definecolor{}` and `\colorlet{}` to `preamble.tex`
3. Document purpose in both files
4. Test in at least one full lecture and one mini5 variant

### When Modifying LaTeX Preamble

- Test with: `pdflatex slides/L01_Fintech_Foundations/L01_full.tex` and `pdflatex slides/L01_Fintech_Foundations/L01_mini5.tex`
- Verify zero overfull box warnings in mini variants
- Document changes in commit message

### When Modifying Chart Styling

- Test by running: `python slides/L01_Fintech_Foundations/01_*/chart.py`
- Verify PDF output looks correct
- Check that fallback color definitions match the main module
- Run at least 3 different chart types (bar, line, scatter)

---

## For AI Agents

### Working in This Directory

- Never modify colors or styles without understanding their use across all lectures
- Always test changes with real chart scripts and LaTeX compilations
- Document the purpose of any new color or command you add
- Maintain backward compatibility: don't rename or remove colors/functions

### Dependencies

- `preamble.tex` is used by all lectures that employ `\input{../../_shared/preamble.tex}`
- `chart_styles.py` is used by all chart scripts in `slides/L[N]_*/[N]_*/`
- Changes here have immediate impact on 7 lectures + 80+ chart scripts

### Testing Checklist

- [ ] LaTeX preamble changes: Test full and mini5 variants of L01
- [ ] Color additions: Test in matplotlib and LaTeX separately
- [ ] Function changes to chart_styles.py: Run at least 3 sample chart scripts
- [ ] Commit changes with clear documentation of intent

### Related Documentation

- Parent: `../AGENTS.md` — Course overview and architecture
- Sibling: `../slides/AGENTS.md` — Lecture-specific structure
