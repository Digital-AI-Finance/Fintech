# L02 Slides: Six Lecture Variants

<!-- Parent: ../AGENTS.md -->

**LaTeX Beamer presentations for Lecture 2: Fintech Ecosystem**

## Overview

This directory contains six variants of the L02 lecture, each optimized for different teaching contexts, audience sizes, and time constraints. All share the same core content but differ in depth, structure, and standalone capability.

**Shared metadata:**
- **Course:** Financial Technology (MSc), University of Zurich
- **Academic year:** Spring 2026
- **Instructor:** Joerg Osterrieder
- **Lecture theme:** Growth drivers, financial inclusion, behavioral economics, and ethical design

---

## Files Overview

| File | Frames | Type | Audience | Duration | Self-Contained? | Status |
|------|--------|------|----------|----------|-----------------|--------|
| `L02_full.tex` | 31 | Primary | Instructors, full cohort | 90 min | No* | Production |
| `L02_overview.tex` | 26 | Condensed | Time-constrained sessions | 60 min | No* | Production |
| `L02_deepdive.tex` | 17 (+appendix) | Analytical | Deep learners, seminars | 75 min | No* | Production |
| `L02_core.tex` | 10 | Extracted core | Standalone, printed | 30–45 min | Yes | Production |
| `L02_mini10.tex` | 11 | Teaser | Promotional, online sharing | 10–15 min | Yes | Production |
| `L02_mini5.tex` | 6 | Ultra-short arc | Lightning talks, 5-slide pitch | 3–5 min | Yes | Production |
| `L02_full.pdf` | — | Compiled | Display/printing | — | Yes | Auto-generated |
| `L02_overview.pdf` | — | Compiled | Display/printing | — | Yes | Auto-generated |
| `L02_deepdive.pdf` | — | Compiled | Display/printing | — | Yes | Auto-generated |
| `L02_core.pdf` | — | Compiled | Display/printing | — | Yes | Auto-generated |
| `L02_mini10.pdf` | — | Compiled | Display/printing | — | Yes | Auto-generated |
| `L02_mini5.pdf` | — | Compiled | Display/printing | — | Yes | Auto-generated |

*No = Requires `../../../_shared/preamble.tex` for theme, colors, commands
**Yes = Fully self-contained (preamble embedded, no external dependencies)

---

## Detailed Variant Descriptions

### 1. L02_full.tex (31 frames) — Primary Lecture

**Purpose:** Comprehensive lecture for 90-minute session

**Structure:** 10-role narrative arc
- **WHY (3 frames):** Title, opening cartoon, learning objectives
- **FEEL (2 frames):** Personal connection (nudges in your wallet), bridge from L01
- **WHAT (5 frames):** Growth drivers, financial inclusion, case study (M-Pesa)
- **HOW (4 frames):** Trust, behavioral economics foundations
- **WHERE (4 frames):** Technology adoption lifecycle, diffusion, chasm
- **OBSTACLES (3 frames):** Barriers to adoption (access, behavioral, trust)
- **MECHANISMS (2 frames):** Choice architecture, nudging principles
- **DARK SIDE (2 frames):** Dark patterns, ethical boundaries
- **SO WHAT (2 frames):** Implications for startups, regulators, users
- **NEXT (1 frame):** Closing cartoon, call to reflection

**Audience:** Full cohorts (50–150 students), instructors who want detailed narrative

**Dependencies:**
- `../../../_shared/preamble.tex` (Beamer theme, colors, macros)
- `../figures/*/chart.pdf` (12 figures embedded via `\includegraphics`)

**Compilation:**
```bash
pdflatex L02_full.tex && pdflatex L02_full.tex
```

**Key features:**
- Interactive exercises ("Find one nudge in your app")
- Personal reflection moments
- Full color, professional theme
- Appendix available for optional deeper dives

---

### 2. L02_overview.tex (26 frames) — Condensed Overview

**Purpose:** Comprehensive but concise lecture for 60-minute session

**Structure:** Three-zone approach
- **ZONE 1: Growth & Opportunity (8 frames)**
  - What is fintech? Four growth drivers. Why now?
- **ZONE 2: Barriers & Behavioral Economics (10 frames)**
  - Financial inclusion gap. Why don't people adopt? Choice architecture.
- **ZONE 3: Implications & Ethics (8 frames)**
  - Technology adoption lifecycle. Dark patterns. Regulatory implications.

**Audience:** Time-constrained instructors, workshops, webinars

**Dependencies:**
- `../../../_shared/preamble.tex`
- `../figures/*/chart.pdf` (selected figures)

**Compilation:**
```bash
pdflatex L02_overview.tex && pdflatex L02_overview.tex
```

**Key features:**
- Streamlined narrative (less personal narrative, more data)
- Faster pacing
- Emphasis on three core themes
- Printable in 13 slides per page (A4 handouts)

---

### 3. L02_deepdive.tex (17 frames + appendix) — Analytical Deep Dive

**Purpose:** Detailed analytical variant with supplementary material

**Structure:** 17 core frames + optional appendix
- Core lecture covers growth drivers, inclusion barriers, behavioral mechanisms, ethical implications
- Appendix includes:
  - Extended case studies (M-Pesa, India Stack, BigTech fintech)
  - Academic citations (technology adoption, behavioral economics)
  - Regulatory frameworks (GDPR, PSD2, local regulations)
  - Advanced topics (algorithmic bias, inclusive design patterns)

**Audience:** Seminars, advanced students, instructors preparing academic discussions

**Dependencies:**
- `../../../_shared/preamble.tex`
- `../figures/*/chart.pdf` (all figures)

**Compilation:**
```bash
pdflatex L02_deepdive.tex && pdflatex L02_deepdive.tex
```

**Key features:**
- Citation-heavy (academic rigor)
- Appendix for flexible delivery
- Deep-dive boxes for technical discussion
- Suitable for publication or archival

---

### 4. L02_core.tex (10 frames) — Extracted Core

**Purpose:** Self-contained essential content (no external preamble dependency)

**Structure:** Minimal viable lecture
1. Title page
2. Opening cartoon (TikZ-embedded)
3. Learning objectives
4. Growth drivers (2 frames)
5. Financial inclusion (2 frames)
6. Choice architecture and nudging (1 frame)
7. Closing reflection
8. References

**Audience:** Standalone teaching, printed distribution, email sharing

**Dependencies:**
- **NONE** — Fully self-contained
- Preamble embedded in file
- All diagrams and colors defined inline (no external figures)
- Can be compiled on any machine with a standard LaTeX distribution

**Compilation:**
```bash
pdflatex L02_core.tex && pdflatex L02_core.tex
```

**Key features:**
- Zero external dependencies
- Portable (can be emailed, printed, shared)
- Printable in 2 slides per page
- ~15 KB file size (minimal)

---

### 5. L02_mini10.tex (11 frames) — 10-Minute Teaser

**Purpose:** Promotional, promotional, or shareable teaser variant

**Structure:** 11 frames (including title)
1. Title + course logo
2. Opening hook (fintech in 2026)
3. Four growth drivers (visual TikZ diagram)
4. The inclusion gap (compelling statistic)
5. Technology adoption S-curve (classic framework)
6. Behavioral nudges (interactive element)
7. Dark patterns warning (ethical perspective)
8. Case study snapshot (M-Pesa or India Stack)
9. Three implications for you
10. Closing reflection
11. Contact/follow-up

**Audience:** Prospective students, online sharing, webinars, conference presentations

**Dependencies:**
- **NONE** — Fully self-contained
- All content via TikZ/pgfplots (no external PDFs)
- Embedded color definitions
- Portable (single .tex file)

**Compilation:**
```bash
pdflatex L02_mini10.tex && pdflatex L02_mini10.tex
```

**Key features:**
- Rapid pacing (1 minute per frame)
- Visually striking (TikZ diagrams, bright colors)
- Engagement hooks ("Find one nudge in your app")
- Shareable PDF (standalone, no dependencies)

---

### 6. L02_mini5.tex (6 frames) — 5-Slide Arc

**Purpose:** Ultra-short narrative arc for lightning talks

**Structure:** Five-slide pitch (+ title)
- **Slide 1 (Title):** Fintech Ecosystem in 5 minutes
- **Slide 2 (WHY):** Why fintech matters (growth statistics, unbanked population)
- **Slide 3 (WHAT):** What drives adoption (four drivers)
- **Slide 4 (HOW):** How product design shapes decisions (nudging)
- **Slide 5 (WHERE):** Where the ethical line is (nudging vs. dark patterns)
- **Slide 6 (SO WHAT):** What you should do (three takeaways)

**Audience:** 3–5 minute pitches, academic lightning talks, social media snippets

**Dependencies:**
- **NONE** — Fully self-contained
- All diagrams in TikZ (pgfplots, shapes.geometric)
- Embedded color palette
- Minimal fonts (readable at small sizes)

**Compilation:**
```bash
pdflatex L02_mini5.tex && pdflatex L02_mini5.tex
```

**Key features:**
- Extreme brevity (one big idea per slide)
- Memorable narrative arc
- Printable as a single A4 page
- Shareable as a 6-slide deck (1 MB PDF)

---

## Common Elements Across Variants

### Shared Content

All variants cover these core topics:

1. **Growth Drivers** — Regulation, technology, consumer demand, capital availability
2. **Financial Inclusion** — Global gap, barriers (access, behavioral, informational, institutional)
3. **Technology Adoption Lifecycle** — Innovators, early adopters, chasm, early majority, late majority, laggards
4. **Behavioral Economics** — Framing, anchoring, defaults, loss aversion
5. **Choice Architecture** — Decision set design, default effects, nudging
6. **Nudging Mechanisms** — Helpful vs. manipulative (dark patterns)
7. **Ethical Implications** — Protecting vulnerable users while enabling innovation

### Shared Visual Identity

- **Color palette:** V4 palette (mlpurple, mlblue, mlred, mlorange, mlgreen, mlteal, mlcyan, etc.)
- **Typography:** Beamer Madrid theme with teal accent
- **Logos:** University of Zurich + course branding (in preamble)
- **Footer notes:** Consistent use of `\bottomnote{}` for context and citations

---

## Compilation Guide

### Prerequisites

```bash
# macOS/Linux
brew install texlive-full  # or apt-get install texlive-full
# Windows: Install MiKTeX or TeX Live

# Verify pdflatex
which pdflatex
```

### Compile All Variants

```bash
#!/bin/bash
cd /path/to/slides/

for variant in full overview deepdive core mini10 mini5; do
  echo "Compiling L02_${variant}.tex..."
  pdflatex -interaction=nonstopmode "L02_${variant}.tex"
  pdflatex -interaction=nonstopmode "L02_${variant}.tex"  # Second pass for overlays
done

echo "All variants compiled successfully."
```

### Troubleshooting

| Error | Cause | Solution |
|-------|-------|----------|
| `! I can't find file 'preamble.tex'` | Missing `_shared/preamble.tex` (for full/overview/deepdive) | Ensure `../../../_shared/` exists; check path |
| `! I can't find file 'chart.pdf'` | Missing figure files | Run `python3 ../figures/*/chart.py` to regenerate |
| `! Undefined control sequence \mlpurple` | Color not defined (mini variants) | Color embedded in header; check preamble import |
| Blurry/pixelated output | DPI too low | Use `pdflatex -output-directory=build` for better control |

---

## Usage Scenarios

### Scenario 1: First-Time Teaching

Use **L02_full.tex** or **L02_overview.tex**:
1. Compile both before first class
2. Present L02_full in 90 minutes OR split L02_overview across two 30-minute sessions
3. Distribute L02_mini10 or L02_mini5 to students as review material

### Scenario 2: Time-Constrained Session

Use **L02_overview.tex**:
1. Compile 30 minutes before class
2. Present in 50–60 minutes
3. Encourage students to review L02_core as handout

### Scenario 3: Promotion/Outreach

Use **L02_mini10.tex** or **L02_mini5.tex**:
1. Compile and distribute before open day
2. Present at webinar or conference (no setup needed)
3. Share PDF on website or social media

### Scenario 4: Standalone Study

Use **L02_core.tex**:
1. Email or print standalone
2. Students review at their own pace
3. No installation dependencies for readers

---

## Integration with Other Lectures

**Upstream (L01):**
- L01 covers supply-side structure (what is fintech, where did it come from, how do banks and fintechs collaborate)
- L02 bridges with Frame 4: "Bridge from Lecture 1" — explicitly transitions to demand-side analysis

**Downstream (L03+):**
- L02 foundations (behavioral economics, nudging) inform regulatory analysis in L03
- Inclusion barriers established here resurface in L04 (microfinance, SMB lending) and L05 (remittances)

**Cross-course:**
- Behavioral economics content aligns with MSc Economics core
- Regulatory content builds toward advanced regulation course

---

## Maintenance & Updates

### When to Update Slides

| Trigger | Action | Files | Frequency |
|---------|--------|-------|-----------|
| New academic year | Refresh dates, institution logos | All | Annually |
| Data/statistics outdated | Update figures, regenerate PDFs | relevant `../figures/*.py` | Annually |
| Typos or clarifications | Edit .tex, recompile | Affected variants | As discovered |
| New case study or research | Add frames to deepdive/full | L02_deepdive.tex, L02_full.tex | Per semester |
| Color scheme change | Update preamble.tex | All (via preamble) | On brand update |

### Regeneration Workflow

```bash
# Step 1: Update figure data (if needed)
cd ../figures
for dir in 0* 1*; do python "$dir/chart.py" || python "$dir/cartoon.py"; done
cd ../slides

# Step 2: Recompile all variants
./compile_all.sh  # See script above

# Step 3: Verify PDFs
ls -lh *.pdf  # Check file sizes and timestamps
```

---

## Notes for Developers & Instructors

### Variant Choice Heuristic

```
┌─ Do I have 90 minutes?
│  ├─ Yes → use L02_full.tex
│  └─ No → Do I have external figures available?
│     ├─ Yes, 60 min available → L02_overview.tex
│     ├─ Yes, <30 min → L02_mini10.tex
│     └─ No (email/portable needed) → L02_core.tex or L02_mini5.tex
```

### Extending Variants

To add content:
1. **For full/overview/deepdive:** Edit `.tex`, recompile (external figures available)
2. **For core/mini variants:** Edit `.tex`, regenerate TikZ diagrams inline (no external figures)
3. **Always recompile twice** (Beamer needs two passes for overlays and references)

### Accessibility

- All variants use **sans-serif fonts** (Beamer default) for readability
- Color palette is **colorblind-friendly** (verified with Coblis simulator)
- PDFs include **text layer** (searchable, readable by screen readers)
- Consider adding **speaker notes** (`.notes{}`) for instructors with visual impairments

---

## File Maintenance Schedule

**Weekly (before class):**
- Verify all `.pdf` files exist and are up-to-date

**Monthly:**
- Check for typos or broken references in active variant(s)

**Quarterly (seasonal):**
- Refresh data in figures (if using real-time sources)

**Annually (before course starts):**
- Rebuild all figures
- Update course metadata (year, instructor, institution)
- Review and refresh case studies

---

## License & Attribution

All materials created for the Financial Technology course (Spring 2026), University of Zurich.

---

**Last updated:** 2026-02-26
**Maintainer:** Joerg Osterrieder
