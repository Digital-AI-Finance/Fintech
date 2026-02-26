# L01 Figures: Charts and Cartoons

<!-- Parent: ../AGENTS.md -->

## Content Summary

Twelve chart and cartoon figures supporting L01: Fintech Foundations and Overview. Each subdirectory contains one Python script (`chart.py` or `cartoon.py`) that generates a high-quality PDF visualization for inclusion in slide decks. All scripts use a standardized structure with fallback imports, metadata dictionaries, and consistent color palettes.

**Sections represented:**
- **WHY** — Crisis catalyst, disruption tension (Figures 05, 11, 12)
- **WHAT** — Definition, evolution, ecosystem (Figures 01, 04)
- **HOW** — Value chain, collaboration models, partnerships (Figures 02, 03, 07)
- **WHERE** — Investment, embedded finance architecture (Figures 06, 08, 09)
- **SO WHAT** — Competitive comparison, key concepts (Figures 09, 10)

## Directory Structure

```
figures/
├── AGENTS.md                                (this file)
├── 01_fintech_evolution_timeline/
│   ├── chart.py                             (Python: S-curve timeline with milestones)
│   └── chart.pdf                            (Generated PDF)
├── 02_banking_value_chain_disruption/
│   ├── chart.py                             (Python: traditional bank vs. fintech unbundling)
│   └── chart.pdf                            (Generated PDF)
├── 03_collaboration_models_matrix/
│   ├── chart.py                             (Python: partnership models comparison matrix)
│   └── chart.pdf                            (Generated PDF)
├── 04_fintech_ecosystem_overview/
│   ├── chart.py                             (Python: fintech service categories)
│   └── chart.pdf                            (Generated PDF)
├── 05_great_recession_catalyst/
│   ├── chart.py                             (Python: 2008 crisis timeline + impact)
│   └── chart.pdf                            (Generated PDF)
├── 06_fintech_investment_growth/
│   ├── chart.py                             (Python: funding trends 2010–2020+)
│   └── chart.pdf                            (Generated PDF)
├── 07_bank_fintech_partnership_flow/
│   ├── chart.py                             (Python: relationship dynamics and flows)
│   └── chart.pdf                            (Generated PDF)
├── 08_embedded_finance_architecture/
│   ├── chart.py                             (Python: API integration architecture)
│   └── chart.pdf                            (Generated PDF)
├── 09_fintech_impact_comparison/
│   ├── chart.py                             (Python: incumbent vs. startup metrics)
│   └── chart.pdf                            (Generated PDF)
├── 10_key_concepts_summary/
│   ├── chart.py                             (Python: taxonomy or quadrant chart)
│   └── chart.pdf                            (Generated PDF)
├── 11_opening_cartoon/
│   ├── cartoon.py                           (Python: XKCD-style disruption tension)
│   └── cartoon.pdf                          (Generated PDF)
└── 12_closing_cartoon/
    ├── cartoon.py                           (Python: XKCD-style reflection/takeaway)
    └── cartoon.pdf                          (Generated PDF)
```

## Figure Catalog

### Figure 01: Fintech Evolution Timeline

**Type:** Time series with annotated milestones
**Section:** WHAT
**Chart type:** S-curve with labeled inflection points
**Content:**
- Timeline from 1950s to 2020s
- Key milestones: electronic banking (1950s–70s), ATMs, online banking, mobile banking, API-first fintech, embedded finance
- S-curve visualization showing adoption acceleration
- Annotations for major technology shifts (internet, smartphones, cloud)

**Script:** `01_fintech_evolution_timeline/chart.py`
**Generated:** `01_fintech_evolution_timeline/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Fintech Evolution Timeline', 'type': 'time_series', 'section': 'WHAT', 'lecture_number': 1 }`

---

### Figure 02: Banking Value Chain Disruption

**Type:** Flowchart / organizational diagram
**Section:** HOW
**Chart type:** Top-down unbundling diagram
**Content:**
- Top row: One large purple box labeled "TRADITIONAL BANK" with integrated functions
- Bottom rows: Five separate fintech disruptor boxes
  - Payments (PayPal, Stripe)
  - Lending (LendingClub, Prosper)
  - Wealth Management (Robinhood, Betterment)
  - Insurance (Lemonade, Insurify)
  - Infrastructure (Plaid, Avaloq)
- Downward arrows showing disruption vectors

**Script:** `02_banking_value_chain_disruption/chart.py`
**Generated:** `02_banking_value_chain_disruption/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Banking Value Chain Disruption', 'type': 'flowchart', 'section': 'HOW', 'lecture_number': 1 }`

---

### Figure 03: Collaboration Models Matrix

**Type:** Grouped horizontal bar chart / matrix
**Section:** HOW
**Chart type:** Comparison matrix across 5 dimensions
**Content:**
- Four collaboration models: Partnership, Acquisition, White-Label, Open Banking
- Five dimensions (1–5 scale):
  1. Control (who decides direction)
  2. Speed-to-Market (time to launch)
  3. Cost Efficiency (relative cost)
  4. Innovation Potential (experimental freedom)
  5. Risk Level (financial/operational risk)
- Color-coded bars for each model across all dimensions

**Script:** `03_collaboration_models_matrix/chart.py`
**Generated:** `03_collaboration_models_matrix/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Collaboration Models Comparison', 'type': 'comparison_bar', 'section': 'HOW', 'lecture_number': 1 }`

---

### Figure 04: Fintech Ecosystem Overview

**Type:** Categorical diagram
**Section:** WHAT
**Chart type:** Service category wheel or matrix
**Content:**
- Central core: "Financial Services Ecosystem"
- Radial segments or quadrants:
  - Payments & Money Transfer
  - Lending & Credit
  - Investment & Wealth Management
  - Insurance & Risk Management
  - Infrastructure & Data (horizontal/vertical fintech)
- Examples within each category
- Overlap zones showing hybrid/embedded use cases

**Script:** `04_fintech_ecosystem_overview/chart.py`
**Generated:** `04_fintech_ecosystem_overview/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Fintech Ecosystem Overview', 'type': 'categorical', 'section': 'WHAT', 'lecture_number': 1 }`

---

### Figure 05: Great Recession Catalyst

**Type:** Timeline with dual-axis chart
**Section:** WHY
**Chart type:** Historical timeline + market impact
**Content:**
- Timeline from 2007–2012 with major crisis events:
  - Aug 2007: Subprime mortgage crisis begins
  - Sep 2008: Lehman Brothers collapse
  - Oct 2008: Market bottom (S&P 500 lowest point)
  - 2009: TARP, Fed intervention, gradual recovery
- Dual-axis visualization:
  - Left: Market index (stock market, housing) showing crash and recovery
  - Right: Trust in financial institutions (declining) and fintech funding (rising)
- Annotations showing opportunity window for fintech

**Script:** `05_great_recession_catalyst/chart.py`
**Generated:** `05_great_recession_catalyst/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Great Recession as Fintech Catalyst', 'type': 'timeline', 'section': 'WHY', 'lecture_number': 1 }`

---

### Figure 06: Fintech Investment Growth

**Type:** Time series with trend
**Section:** WHERE
**Chart type:** Area or line chart with annual funding
**Content:**
- Timespan: 2010–2020+ (annual data)
- Trend: Global fintech investment rising from ~$1B/year (2010) to $30B+/year (2020)
- Breakdown by category (optional):
  - Payments (largest)
  - Lending
  - Wealth
  - Infrastructure
  - InsurTech
  - Other
- Annotations for inflection points (2015 platform maturity, 2020 pandemic acceleration)

**Script:** `06_fintech_investment_growth/chart.py`
**Generated:** `06_fintech_investment_growth/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Fintech Investment Growth', 'type': 'time_series', 'section': 'WHERE', 'lecture_number': 1 }`

---

### Figure 07: Bank-Fintech Partnership Flow

**Type:** Flow diagram / Sankey
**Section:** HOW
**Chart type:** Relationship dynamics diagram
**Content:**
- Left side: Banks (incumbent financial institutions)
- Right side: Fintech companies (startups)
- Center: Multiple relationship types (flows)
  - API access (Bank → Fintech)
  - White-label solutions (Fintech → Bank)
  - Acquisition (Bank acquires Fintech)
  - Partnership/Joint Ventures (bidirectional)
  - Technology licensing
- Thickness of arrows proportional to frequency/strategic importance

**Script:** `07_bank_fintech_partnership_flow/chart.py`
**Generated:** `07_bank_fintech_partnership_flow/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Bank-Fintech Partnership Flow', 'type': 'sankey', 'section': 'HOW', 'lecture_number': 1 }`

---

### Figure 08: Embedded Finance Architecture

**Type:** Technical architecture diagram
**Section:** WHERE
**Chart type:** API integration stack
**Content:**
- Three layers:
  - **Top layer (Consumer interface):** Non-financial platform (e-commerce, marketplace, social media, saas product)
  - **Middle layer (Integration):** API layer with middleware, security, authorization
  - **Bottom layer (Backend services):** Payments, lending, insurance, settlement infrastructure
- Arrows showing data/transaction flow
- Examples: "Buy Now Pay Later" flow, embedded lending, marketplace insurance
- Highlighting API-first architecture enabling embedded finance

**Script:** `08_embedded_finance_architecture/chart.py`
**Generated:** `08_embedded_finance_architecture/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Embedded Finance Architecture', 'type': 'architecture', 'section': 'WHERE', 'lecture_number': 1 }`

---

### Figure 09: Fintech Impact Comparison

**Type:** Radar or bar comparison chart
**Section:** SO WHAT
**Chart type:** Multi-dimensional comparison
**Content:**
- Two entities: Incumbent Banks vs. Fintech Startups
- Six dimensions (spider/radar or grouped bars):
  1. Cost per transaction
  2. Time to market
  3. Customer acquisition cost
  4. Regulatory burden
  5. Technology agility
  6. Trust/Brand equity
- Color-coded comparison (e.g., teal for banks, orange for fintech)
- Shows strengths and weaknesses of each model

**Script:** `09_fintech_impact_comparison/chart.py`
**Generated:** `09_fintech_impact_comparison/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Incumbent vs. Fintech: Competitive Comparison', 'type': 'radar', 'section': 'SO WHAT', 'lecture_number': 1 }`

---

### Figure 10: Key Concepts Summary

**Type:** Quadrant or taxonomy chart
**Section:** SO WHAT
**Chart type:** Strategic matrix or concept map
**Content:**
- Option A (quadrant):
  - X-axis: Asset-Light ↔ Asset-Heavy
  - Y-axis: Regulated ↔ Unregulated (or: Digital-Native ↔ Legacy)
  - Four quadrants showing different fintech types, incumbents, hybrids
- Option B (taxonomy tree):
  - Root: "Financial Technology"
  - Branches: Horizontal Fintech (infrastructure, data) vs. Vertical Fintech (service-specific)
  - Sub-branches: Payments, Lending, Wealth, Insurance, etc.
- Labels and examples in each quadrant/node

**Script:** `10_key_concepts_summary/chart.py`
**Generated:** `10_key_concepts_summary/chart.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Metadata:** `{ 'title': 'Key Concepts Summary', 'type': 'quadrant', 'section': 'SO WHAT', 'lecture_number': 1 }`

---

### Figure 11: Opening Cartoon

**Type:** XKCD-style cartoon
**Section:** WHY
**Chart type:** Comic illustration
**Content:**
- Two characters: A banker (suit, serious expression) and a fintech founder (casual, laptop)
- Setting: Left side (traditional boardroom), right side (garage/startup space)
- Speech bubbles:
  - Banker (left): "This took us 5 years and a regulatory team."
  - Founder (right): "We built this in a weekend. No branch offices needed."
- Caption (bottom): "The revolution started in a garage, not a boardroom."
- Visual contrast: Traditional office vs. startup workspace, age vs. youth, formality vs. casual

**Script:** `11_opening_cartoon/cartoon.py`
**Generated:** `11_opening_cartoon/cartoon.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Style:** Matplotlib `plt.xkcd()` or hand-drawn aesthetic with stick figures, simple shapes, and caption text
**Metadata:** `{ 'title': 'Opening Cartoon: Fintech Disruption', 'type': 'cartoon_opening', 'section': 'WHY', 'lecture_number': 1 }`

---

### Figure 12: Closing Cartoon

**Type:** XKCD-style cartoon
**Section:** SO WHAT
**Chart type:** Comic illustration
**Content:**
- Single or dual character scene reflecting on the lecture themes
- Possible interpretations:
  - Option A: A bank executive and fintech founder shaking hands (partnership, convergence)
  - Option B: A customer with multiple payment/service app icons floating around them (ecosystem integration)
  - Option C: A timeline showing past (traditional banking), present (fintech boom), future (embedded finance)
- Speech bubble or caption emphasizing key takeaway: "The future is embedded finance—seamlessly woven into every platform."
- Visual cue: Checkmark, thumbs-up, or lightbulb for positive conclusion

**Script:** `12_closing_cartoon/cartoon.py`
**Generated:** `12_closing_cartoon/cartoon.pdf`
**Output:** High-quality PDF, 10×6 inch figure (300 dpi)

**Style:** Matplotlib `plt.xkcd()` or hand-drawn aesthetic with stick figures, simple shapes, and caption text
**Metadata:** `{ 'title': 'Closing Cartoon: Fintech Future', 'type': 'cartoon_closing', 'section': 'SO WHAT', 'lecture_number': 1 }`

---

## Standard Chart Structure

All Python scripts follow this pattern:

```python
"""
Figure NN: [Title]
[One-line description]
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# ... other imports ...

try:
    from chart_styles import V4_COLORS, apply_v4_style, save_chart
except ImportError:
    # Fallback definitions for V4_COLORS, apply_v4_style, save_chart
    V4_COLORS = { ... }
    def apply_v4_style(...): ...
    def save_chart(...): ...

CHART_METADATA = {
    'title': '[Figure Title]',
    'type': '[Chart Type]',
    'section': '[WHY|WHAT|HOW|WHERE|SO WHAT]',
    'lecture_number': 1,
}

# ... figure-specific code ...
save_chart(fig, filename='chart.pdf', dpi=300)
```

### Key Components

1. **Docstring:** One-line description of the figure content and visual approach
2. **Imports:**
   - Standard: `sys`, `os`, `matplotlib`, `matplotlib.pyplot`
   - Figure-specific: `numpy`, `patches`, `FancyBboxPatch`, etc.
3. **sys.path.insert():** Always adds `_shared` to path for chart_styles import
4. **matplotlib.use('Agg'):** Headless rendering (no display backend needed)
5. **Try/Except:** Imports from chart_styles with fallback definitions
6. **CHART_METADATA:** Dictionary with title, type, section, and lecture_number
7. **Figure code:** matplotlib-based visualization
8. **save_chart():** Saves as PDF with 300 dpi, tight layout, white background

---

## Color Palette

All figures use the **V4 Color Palette** from `_shared/chart_styles.py`:

| Name | Hex | RGB | Use Case |
|------|-----|-----|----------|
| MLPURPLE | #9467BD | (148, 103, 189) | Primary/emphasis |
| MLBLUE | #1F77B4 | (31, 119, 180) | Secondary/data |
| MLRED | #D62728 | (214, 39, 40) | Alert/negative |
| MLORANGE | #FF7F0E | (255, 127, 14) | Accent/fintech |
| MLGREEN | #2CA02C | (44, 160, 44) | Positive/growth |
| MLGRAY | #7F7F7F | (127, 127, 127) | Neutral/background |
| MLTEAL | #0D7377 | (13, 115, 119) | Tertiary/corporate |
| MLCYAN | #14BDEB | (20, 189, 235) | Highlight/accent |
| MLYELLOW | #BCBD22 | (188, 189, 34) | Caution/emphasis |
| MLPINK | #E377C2 | (227, 119, 194) | Accent/alternative |
| MLBROWN | #8C564B | (140, 86, 75) | Historic/legacy |

---

## Regenerating Figures

To regenerate any figure:

```bash
cd figures/NN_label/
python chart.py
# or
python cartoon.py
```

This creates/overwrites `chart.pdf` (or `cartoon.pdf`) in the same directory.

### Prerequisites

- Python 3.7+
- matplotlib, numpy, pandas (as needed by individual scripts)
- `_shared/chart_styles.py` accessible via sys.path (fallback definitions provided if missing)

### Testing Individual Figures

```bash
# Navigate to figure directory
cd figures/01_fintech_evolution_timeline/

# Run script
python chart.py

# Check output
ls -la chart.pdf  # Verify PDF created
```

All scripts are designed to be standalone and executable.

---

## Integration with Slides

All figures are referenced in slide decks using relative paths:

```latex
\includegraphics[width=0.85\textwidth]{figures/01_fintech_evolution_timeline/chart.pdf}
```

**Path resolution:**
- From `slides/L01_full.tex`: `figures/NN_label/chart.pdf` (relative to figures/ directory)
- PDF must exist before compilation
- PDFs are generated on-demand by running the Python scripts

---

## Dependencies

| Dependency | Location | Purpose |
|------------|----------|---------|
| Shared chart styles | `_shared/chart_styles.py` | Color palette, helper functions (with fallbacks) |
| Parent AGENTS.md | `../AGENTS.md` | High-level lecture documentation |

---

## Metadata

| Field | Value |
|-------|-------|
| **Lecture** | L01 (Fintech Foundations and Overview) |
| **Total Figures** | 12 |
| **Charts** | 10 (`chart.py`) |
| **Cartoons** | 2 (`cartoon.py`) |
| **Sections covered** | WHY, WHAT, HOW, WHERE, SO WHAT |
| **Output format** | PDF (300 dpi) |
| **Color palette** | V4 (11 colors) |

---

## AI Agent Instructions

### For Updating Figure Content

**When editing chart data, labels, or styling:**

1. **Locate the correct subdirectory** — Find the figure by number and name in the catalog above
2. **Edit the Python script** — Modify `NN_label/chart.py` or `cartoon.py`
3. **Test regeneration:**
   ```bash
   cd figures/NN_label/
   python chart.py
   ```
4. **Verify PDF quality** — Check the generated PDF in a PDF viewer for rendering issues
5. **Verify slide integration** — Re-compile the relevant slide file to ensure `\includegraphics` resolves correctly

### For Adding New Figures

**When creating a new figure:**

1. **Create a new subdirectory** with format `NN_descriptive_label/`
2. **Create the Python script** following the standard structure above
3. **Include CHART_METADATA** with appropriate title, type, section, and lecture_number
4. **Add try/except import** for chart_styles with fallback definitions
5. **Use V4_COLORS** for consistent palette
6. **Call save_chart()** at the end to output PDF
7. **Document the figure** in this AGENTS.md file using the catalog format
8. **Reference in slides** using `\includegraphics{figures/NN_label/chart.pdf}`

### For Maintaining Color Consistency

**When using colors across figures:**

1. **Always import from chart_styles** — Ensures consistency across all lectures
2. **Fallback to hardcoded V4_COLORS** — Allows standalone execution
3. **Use named colors** (MLPURPLE, MLBLUE, etc.) rather than hex values in code
4. **Never override colors** — Let the shared palette define visual identity

### For Debugging Chart Issues

**When a figure fails to generate:**

1. **Check Python path** — Verify sys.path.insert points correctly to `_shared/`
2. **Check matplotlib backend** — Ensure `matplotlib.use('Agg')` for headless rendering
3. **Check imports** — Verify all required libraries (numpy, pandas, etc.) are installed
4. **Check file paths** — Verify relative paths to `_shared/chart_styles.py` are correct
5. **Run in isolation** — Test script directly in its own directory
6. **Check PDF output** — Verify chart.pdf is created and readable

### For Slide Deck Updates

**When slides reference a figure:**

1. **Verify figure PDF exists** before compiling slides
2. **Check path is relative** from slide file location
3. **Check width parameter** in `\includegraphics[width=...]`
4. **Test PDF integration** by viewing the slide PDF after compilation
5. **Update figure** if slide content changes (e.g., if axis labels need updating)

---

**Last Updated:** 2026-02-26
**Maintainer:** FinTech Lecture Series Team
