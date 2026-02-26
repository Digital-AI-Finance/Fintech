# L02 Figures: 12 Charts and Cartoons

<!-- Parent: ../AGENTS.md -->

**Matplotlib Python generation scripts and compiled PDFs for Lecture 2 visualizations**

## Overview

This directory contains 12 custom visualizations for the L02 lecture (Fintech Ecosystem). Each figure includes:

- **Python generation script** (`chart.py` or `cartoon.py`) — Generates the visualization from scratch
- **Compiled PDF** (`chart.pdf` or `cartoon.pdf`) — Ready to embed in LaTeX slides
- **Metadata** — Embedded in script as CHART_METADATA (title, type, section, lecture_number)

All scripts use matplotlib with optional fallback color definitions and are designed for **regeneration** (not manual editing of PDFs).

---

## Files Overview

| # | Directory | Type | Python Script | Output | Used In |
|---|-----------|------|---------------|--------|---------|
| 1 | `01_fintech_ecosystem_map` | Diagram | `chart.py` | `chart.pdf` | L02_full, L02_overview, L02_deepdive |
| 2 | `02_growth_drivers_dashboard` | Dashboard | `chart.py` | `chart.pdf` | L02_full, L02_overview |
| 3 | `03_financial_inclusion_gap` | Bar chart | `chart.py` | `chart.pdf` | L02_full, L02_deepdive |
| 4 | `04_mpesa_adoption_flow` | Flow diagram | `chart.py` | `chart.pdf` | L02_full, L02_deepdive |
| 5 | `05_trust_framework_comparison` | Radar/bubble | `chart.py` | `chart.pdf` | L02_full, L02_overview |
| 6 | `06_technology_adoption_lifecycle` | S-curve | `chart.py` | `chart.pdf` | L02_full, L02_overview |
| 7 | `07_adoption_barriers_matrix` | Heatmap | `chart.py` | `chart.pdf` | L02_full, L02_deepdive |
| 8 | `08_nudging_architecture` | Conceptual diagram | `chart.py` | `chart.pdf` | L02_full, L02_overview |
| 9 | `09_choice_architecture_examples` | Comparison | `chart.py` | `chart.pdf` | L02_full |
| 10 | `10_ecosystem_stakeholder_impact` | Network/matrix | `chart.py` | `chart.pdf` | L02_full, L02_overview |
| 11 | `11_opening_cartoon` | XKCD illustration | `cartoon.py` | `cartoon.pdf` | L02_full, L02_overview, L02_deepdive |
| 12 | `12_closing_cartoon` | XKCD illustration | `cartoon.py` | `cartoon.pdf` | L02_full, L02_deepdive |

---

## Detailed Figure Descriptions

### 1. Fintech Ecosystem Map (01_fintech_ecosystem_map)

**Purpose:** Contextualize fintech within a broader ecosystem

**Type:** Circular network diagram (hub-and-spoke)

**Visual structure:**
- **Central hub:** "Fintech Services" (teal box)
- **Inner ring (6 nodes):** Startups, Banks, BigTech, Regulators, Investors, Tech Providers
- **Outer ring (4 segments):** Banked Consumers, Unbanked Consumers, SMBs, Enterprises
- **Arrows:** Hub → Inner (solid), Outer → Inner (dashed)

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Fintech Ecosystem Map',
    'type': 'ecosystem_diagram',
    'section': 'The Fintech Ecosystem',
    'lecture_number': 2,
}
```

**Data sources:** Conceptual (no external data); colors from V4_COLORS palette

**Use cases:**
- Frame 4 (Bridge from L01) — Establish the ecosystem context
- Discussion prompt: "Which ring affects fintech adoption most?"

---

### 2. Growth Drivers Dashboard (02_growth_drivers_dashboard)

**Purpose:** Visualize the four interdependent drivers of fintech growth

**Type:** Multi-panel dashboard (2×2 grid or quadrant)

**Visual structure:**
- **Four quadrants:**
  - Regulation (e.g., open banking directives, sandbox initiatives)
  - Technology (e.g., mobile, AI, blockchain maturity)
  - Consumer demand (e.g., user preference for digital, younger demographics)
  - Capital availability (e.g., VC funding, IPO exits, institutional interest)
- **Central overlap:** Where all four drivers converge = **Fintech growth**
- **Color coding:** Each driver in distinct color; intersection in mixed color

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Growth Drivers Dashboard',
    'type': 'dashboard',
    'section': 'Growth Drivers',
    'lecture_number': 2,
}
```

**Data sources:** Illustrative data (e.g., regulatory timeline, funding trends); can be updated annually

**Use cases:**
- Frame 5–6 (What drives fintech?) — Main teaching visual
- Exercise: "Which driver is strongest in your country?"

---

### 3. Financial Inclusion Gap (03_financial_inclusion_gap)

**Purpose:** Quantify the gap between global banked and unbanked populations

**Type:** Stacked bar chart or population pyramid

**Visual structure:**
- **X-axis:** Region (Sub-Saharan Africa, South Asia, East Asia, Latin America, OECD, etc.)
- **Y-axis:** Adult population (millions) or percentage
- **Stacked bars:** Banked (green) vs. Unbanked (orange)
- **Overlay:** % unbanked per region

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Financial Inclusion Gap by Region',
    'type': 'bar_chart',
    'section': 'Financial Inclusion',
    'lecture_number': 2,
}
```

**Data sources:** World Bank data (frequency: refreshed annually); sources cited in caption

**Use cases:**
- Frame 9–10 (The Inclusion Gap) — Motivate the problem
- Exercise: "Which regions have the highest unbanked populations?"

---

### 4. M-Pesa Adoption Flow (04_mpesa_adoption_flow)

**Purpose:** Case study of technology adoption in action (Kenya, East Africa)

**Type:** Flow diagram or timeline

**Visual structure:**
- **Left to right:** Pre-adoption → Awareness → Trial → Adoption → Regular use → Ecosystem expansion
- **Stages:**
  1. **Pre-2007:** SMS-based transfer requests (no mobile money)
  2. **2007:** M-Pesa launch (Safaricom); early adopters
  3. **2008–2010:** Rapid expansion; small retailers adopt
  4. **2010–2015:** Ecosystem deepens (savings, insurance, credit)
  5. **2015+:** Regional expansion (Tanzania, Uganda, DRC, India); fintech partnerships
- **User flow:** Farmer → Agent → Recipient → Ecosystem participant

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'M-Pesa: Adoption Journey',
    'type': 'flow_diagram',
    'section': 'Case Study',
    'lecture_number': 2,
}
```

**Data sources:** M-Pesa reports, Safaricom investor relations, academic case studies; illustrative milestones

**Use cases:**
- Frame 11–12 (Case Study: M-Pesa) — Real-world adoption narrative
- Exercise: "Map your financial service adoption using M-Pesa as model"

---

### 5. Trust Framework Comparison (05_trust_framework_comparison)

**Purpose:** Compare trust dimensions across traditional banks, fintechs, and BigTech platforms

**Type:** Radar chart (multi-dimensional) or bubble chart (2D with size encoding)

**Visual structure:**
- **Dimensions:**
  - Regulatory backing (is it licensed?)
  - History/longevity (how long has it existed?)
  - Transparency (are terms clear?)
  - Security (encryption, fraud protection)
  - Accessibility (easy to use, 24/7 service)
  - Social proof (how many users, reviews)
- **Three entities:** Traditional Bank (blue), Fintech Startup (purple), BigTech Platform (orange)
- **Radar plot:** Each entity as a polygon; larger area = higher overall trust

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Trust Framework Comparison',
    'type': 'radar_chart',
    'section': 'Behavioral Barriers',
    'lecture_number': 2,
}
```

**Data sources:** Illustrative (based on typical trust surveys); can be calibrated with real survey data

**Use cases:**
- Frame 15–16 (Trust as a Barrier) — Highlight why adoption stalls
- Discussion: "Which dimension matters most to you?"

---

### 6. Technology Adoption Lifecycle (06_technology_adoption_lifecycle)

**Purpose:** Introduce the classic technology diffusion model (Rogers, 1962)

**Type:** S-curve (cumulative adoption) + normal distribution overlay

**Visual structure:**
- **S-curve:** Cumulative % of population adopting technology over time
- **Segments labeled on curve:**
  - Innovators (2.5%) — Risk-takers, try first
  - Early adopters (13.5%) — Opinion leaders
  - Early majority (34%) — Pragmatists
  - Late majority (34%) — Skeptics
  - Laggards (16%) — Resistant
- **Chasm:** Gap between early adopters and early majority (dashed vertical line)
- **Real-world examples:** Fintech apps that crossed (Venmo, N26) vs. stalled (Google Pay in some markets)

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Technology Adoption Lifecycle',
    'type': 's_curve',
    'section': 'Adoption Barriers',
    'lecture_number': 2,
}
```

**Data sources:** Rogers (1962) "Diffusion of Innovations"; Christensen (1997) "The Innovator's Dilemma"

**Use cases:**
- Frame 17–18 (Crossing the Chasm) — Key framework for predicting fintech success
- Exercise: "Where is your favorite fintech app on this curve?"

---

### 7. Adoption Barriers Matrix (07_adoption_barriers_matrix)

**Purpose:** Systematize barriers into four categories (access, behavioral, informational, institutional)

**Type:** 2×2 matrix heatmap (or 4-cell taxonomy)

**Visual structure:**
- **Rows:** Internal vs. External barriers
- **Columns:** Individual vs. Systemic barriers
- **Four cells:**
  1. **Access barriers (external, systemic):** No smartphone, no electricity, no ID
  2. **Behavioral barriers (internal, individual):** Distrust, habit, loss aversion
  3. **Informational barriers (external, individual):** Don't know the product exists, don't understand it
  4. **Institutional barriers (external, systemic):** Regulatory restrictions, no agent network, poor interoperability
- **Color intensity:** Red (severe barrier) → Yellow (moderate) → Green (manageable)
- **Examples:** Specific barriers plotted as dots/labels in each cell

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Adoption Barriers Matrix',
    'type': 'heatmap',
    'section': 'Obstacles to Adoption',
    'lecture_number': 2,
}
```

**Data sources:** Conceptual taxonomy; examples from fintech research and case studies

**Use cases:**
- Frame 19–20 (Obstacles to Adoption) — Organize why inclusion remains incomplete
- Workshop: "For your fintech product, which barriers are hardest to overcome?"

---

### 8. Nudging Architecture (08_nudging_architecture)

**Purpose:** Decompose the anatomy of a "nudge" (choice architecture design element)

**Type:** Conceptual diagram (flow or nested boxes)

**Visual structure:**
- **Top level:** The nudge (e.g., "Round-up savings feature")
- **Decomposed into:**
  - **Choice set:** What options are available? (save $1.50, save $5, skip saving)
  - **Default:** Which option is pre-selected? (save $1.50 is default)
  - **Framing:** How is it presented? ("Save effortlessly" vs. "We'll take your money")
  - **Anchor:** Is there a reference point? (comparison to historical average spending)
  - **Feedback:** How is outcome communicated? (visual progress bar, monthly summary)
- **Outcome:** Behavior change (increase in savings rate)

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Nudging Architecture',
    'type': 'conceptual_diagram',
    'section': 'Behavioral Mechanisms',
    'lecture_number': 2,
}
```

**Data sources:** Thaler & Sunstein (2008) "Nudge"; Dinner et al. (2011) "Partitioning Default Effects"

**Use cases:**
- Frame 21 (How Nudges Work) — Teach students the anatomy of design choices
- Exercise: "Identify each component in your banking app's savings feature"

---

### 9. Choice Architecture Examples (09_choice_architecture_examples)

**Purpose:** Show real-world fintech nudges (good and bad)

**Type:** Side-by-side comparison or grid of screenshots/mockups

**Visual structure:**
- **Left column (Good nudges):**
  - Rounding-up savings (Acorns, Chime)
  - Financial literacy tips on dashboard
  - Goal-based account segmentation
  - Spending categories with traffic-light alerts
- **Right column (Dark patterns):**
  - Hidden auto-renewal (subscription traps)
  - Confusing opt-out menus (hard to cancel)
  - Fake scarcity ("Only 3 spots left!")
  - Misleading APR displays
- **Each example:** Screenshot/mockup + brief label + assessment ("Helpful nudge" vs. "Dark pattern")

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Choice Architecture: Helpful Nudges vs. Dark Patterns',
    'type': 'comparison_grid',
    'section': 'Dark Side of Nudging',
    'lecture_number': 2,
}
```

**Data sources:** Screenshots from real fintech apps (anonymized); design pattern research (Nielsen Norman Group, IAB)

**Use cases:**
- Frame 22–23 (The Dark Side) — Highlight ethical boundaries
- Debate: "Where is the line between nudging and manipulation?"

---

### 10. Ecosystem Stakeholder Impact (10_ecosystem_stakeholder_impact)

**Purpose:** Analyze value creation and distribution across stakeholder groups

**Type:** Matrix or network diagram (stakeholders × impact dimensions)

**Visual structure:**
- **Stakeholders (rows):** Banks, Fintech startups, BigTech platforms, Regulators, Consumers, Investors
- **Impact dimensions (columns):** Financial inclusion, Innovation, Risk, Profit, Social welfare
- **Cell contents:** Color-coded impact (green = positive, red = negative, yellow = mixed)
- **Alternative: Network view** with nodes (stakeholder groups) and edges (value flows); edge thickness indicates magnitude

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Ecosystem Stakeholder Impact Matrix',
    'type': 'impact_matrix',
    'section': 'Implications',
    'lecture_number': 2,
}
```

**Data sources:** Conceptual (based on industry research, regulatory filings, academic case studies)

**Use cases:**
- Frame 25 (Implications for Each Stakeholder) — Summarize trade-offs
- Capstone exercise: "Design a fintech product that maximizes value for all stakeholders"

---

### 11. Opening Cartoon (11_opening_cartoon)

**Purpose:** Engage students with a memorable visual metaphor at lecture start

**Type:** XKCD-style hand-drawn illustration

**Visual scene:**
- **Left side:** Farmer in field with mobile phone in hand, holding "Transfer Complete" screen, signal bars visible
  - Speech bubble: *"Who needs a branch? I have three bars of signal."*
- **Right side:** Traditional bank building with "CLOSED" sign on door
  - Bird on roof speech bubble: *"Even I have a mobile wallet."*
- **Ground line:** Flat horizon (savanna-style landscape)
- **Color:** Minimal color palette, hand-drawn aesthetic (plt.xkcd() style)

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Opening Cartoon: Mobile Banking Revolution',
    'type': 'cartoon',
    'section': 'Opening',
    'lecture_number': 2,
}
```

**Data sources:** Illustrative (inspired by true narratives of mobile banking in developing economies)

**Use cases:**
- Frame 2 (Opening Cartoon) — Hook attention, establish lecture theme
- Quote: *"The most important bank branch in history fits in your pocket."*

---

### 12. Closing Cartoon (12_closing_cartoon)

**Purpose:** Reflect on ethical implications and leave a memorable closing image

**Type:** XKCD-style hand-drawn illustration

**Visual scene:** (Varies by lecture focus, typical options)

**Option A (Nudging ethics):**
- **Left side:** Designer at desk sketching a "Save" button with happy expression
- **Right side:** Same designer, sad expression, looking at user data showing 80% of users fell into dark pattern trap
- **Caption:** *"Intent vs. Impact"* or *"The designer's dilemma"*

**Option B (Inclusion vs. protection):**
- **Left:** Person excluded from banking system (no phone, no ID)
- **Right:** Person protected by over-regulation (access exists but limited by compliance)
- **Caption:** *"Balancing act: Include without exploiting"*

**Option C (Future of fintech):**
- **Left:** Fintech startup (lightning-fast, risky)
- **Right:** Traditional bank (slow but solid)
- **Center:** Merged entity (fast + safe)
- **Caption:** *"Convergence: The future is hybrid"*

**Python metadata:**
```python
CHART_METADATA = {
    'title': 'Closing Cartoon: [Theme variant]',
    'type': 'cartoon',
    'section': 'Closing',
    'lecture_number': 2,
}
```

**Data sources:** Illustrative (no external data)

**Use cases:**
- Final frame (Closing Reflection) — Leave students with a thought-provoking image
- Pair with reflection prompt: "What's your take-away from this lecture?"

---

## Generation & Dependencies

### Python Requirements

```bash
pip install matplotlib numpy
```

### Directory Structure for Import

All scripts use:
```python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared'))
```

This assumes:
```
L02_fintech_ecosystem/
├── figures/
│   ├── 01_fintech_ecosystem_map/
│   │   └── chart.py
│   └── ... (11 more subdirs)
└── ../../_shared/
    └── chart_styles.py
```

### Fallback Mechanism

Each script has a **try-except** pattern:

```python
try:
    from chart_styles import V4_COLORS, apply_v4_style, save_chart
except ImportError:
    # Fallback: embedded definitions
    V4_COLORS = { 'MLPURPLE': '#9467BD', ... }
    def apply_v4_style(ax, ...): ...
    def save_chart(fig, ...): ...
```

This ensures **graphs compile even if `chart_styles.py` is missing**.

### Regeneration Workflow

```bash
#!/bin/bash
cd /path/to/L02_fintech_ecosystem/figures

# Generate all charts (01–10)
for dir in 0{1..9}_* 10_*; do
    echo "Generating $dir..."
    python "$dir/chart.py"
done

# Generate cartoons (11–12)
for dir in 1{1..2}_*; do
    echo "Generating $dir..."
    python "$dir/cartoon.py"
done

echo "All figures regenerated."
```

### Verification

```bash
# Check all PDFs exist and are recent
ls -lh **/chart.pdf **/cartoon.pdf | grep -E "2026-02"
```

---

## Customization & Updates

### Updating Figure Data

To refresh a figure (e.g., latest fintech funding statistics):

1. **Open the script:** `02_growth_drivers_dashboard/chart.py`
2. **Locate the data section** (usually ~20–50 lines from start):
   ```python
   # Data: Funding by year (billions USD)
   years = [2019, 2020, 2021, 2022, 2023, 2024]
   funding = [135, 172, 231, 156, 92, 110]
   ```
3. **Update values** based on latest sources
4. **Regenerate:** `python chart.py`
5. **Check output:** `ls -lh chart.pdf` (should have recent timestamp)

### Changing Colors

To modify the color palette globally:

1. **Edit `_shared/chart_styles.py`:**
   ```python
   V4_COLORS = {
       'MLPURPLE': '#9467BD',  # Change this
       ...
   }
   ```
2. **Regenerate all figures:**
   ```bash
   for dir in *_*; do python "$dir/chart.py"; done
   ```

### Adding New Figures

To add a new visualization (e.g., figure 13):

1. **Create directory:** `mkdir 13_new_topic`
2. **Create script:** `13_new_topic/chart.py` (copy template from existing chart)
3. **Add metadata:**
   ```python
   CHART_METADATA = {
       'title': 'New Topic Chart',
       'type': 'bar_chart',
       'section': 'New Section',
       'lecture_number': 2,
   }
   ```
4. **Generate:** `python 13_new_topic/chart.py`
5. **Test:** `ls -lh 13_new_topic/chart.pdf`
6. **Update parent AGENTS.md** (this file) and slides

---

## Styling & Accessibility

### Color Palette

All figures use the **V4 color palette** (verified colorblind-friendly):

| Name | Hex | RGB | Use Case |
|------|-----|-----|----------|
| MLPURPLE | #9467BD | (148, 103, 189) | Primary accent |
| MLBLUE | #1F77B4 | (31, 119, 180) | Data series 1 |
| MLRED | #D62728 | (214, 39, 40) | Alerts, negatives |
| MLORANGE | #FF7F0E | (255, 127, 14) | Data series 2 |
| MLGREEN | #2CA02C | (44, 160, 44) | Success, positives |
| MLTEAL | #0D7377 | (13, 115, 119) | Teal accent |
| MLCYAN | #14BDEB | (20, 189, 235) | Highlights |
| MLGRAY | #7F7F7F | (127, 127, 127) | Neutral, axes |

**Verification:** All colors tested with [Coblis](https://www.color-blindness.com/coblis-color-blindness-simulator/) color blindness simulator.

### Font & Typography

- **Sans-serif fonts** (matplotlib default, DejaVu Sans)
- **Font sizes:** 14pt (titles) → 11pt (labels) → 9pt (ticks)
- **Font weight:** Bold for titles, regular for data labels
- **Color contrast:** All text checked for WCAG AA compliance (4.5:1 minimum)

### Accessibility Features

- **Text descriptions** in file names (e.g., `03_financial_inclusion_gap`)
- **CHART_METADATA** in each script (title, type, section, lecture_number)
- **Alt text ready:** For web use, include caption from CHART_METADATA['title']
- **Searchable PDFs:** Generated with text layer (embedded fonts)

---

## Integration with LaTeX

### Embedding Figures

In any LaTeX slide file, include figures:

```latex
\includegraphics[width=0.8\textwidth]{figures/01_fintech_ecosystem_map/chart.pdf}
```

### Sizing & Aspect Ratios

All PDFs maintain **consistent aspect ratio** (10:6 or 12:8 for most charts):

- **Width:** 1000–1200 px
- **Height:** 600–800 px
- **DPI:** 300 (publication-quality)

---

## Maintenance Schedule

| Task | Frequency | Owner | Checklist |
|------|-----------|-------|-----------|
| Verify PDFs exist | Before each lecture | Instructor | `ls -lh **/chart.pdf` |
| Update data (if real-time sources) | Quarterly | Data team | Edit `*/chart.py`, regenerate |
| Refresh color scheme | Annually | Brand team | Update `_shared/chart_styles.py`, regenerate all |
| Add new figures | Per semester | Instructor + dev | Create directory, script, test, update AGENTS.md |
| Archive old variants | Annually | Admin | Move outdated figures to `_archive/` |

---

## License & Attribution

All figures created for the Financial Technology course, University of Zurich, Spring 2026.

**Data sources cited in each script's metadata and comments.**

---

**Last updated:** 2026-02-26
**Maintainer:** Joerg Osterrieder
