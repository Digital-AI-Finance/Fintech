# L01 Slides: Fintech Foundations

<!-- Parent: ../AGENTS.md -->

## Content Summary

Six LaTeX Beamer slide variants presenting Lecture 1: Fintech Foundations and Overview. The lecture arc spans from **WHY** (disruption tension and 2008 crisis context) through **WHAT** (definition and historical evolution) to **HOW** (collaboration models, value chain unbundling) and **WHERE** (embedded finance) and **SO WHAT** (strategic implications).

All variants share a common narrative but differ in scope, structure, and figure inclusion:

- **Full/Overview/Deepdive** variants depend on shared preamble for theme, colors, and macros
- **Core/Mini10/Mini5** variants are self-contained with inline preambles

## File Inventory

| File | Frames | Structure | Dependencies | Purpose |
|------|--------|-----------|--------------|---------|
| `L01_full.tex` | 31 | 10-role arc with depth | `\input{../../../_shared/preamble.tex}` | Flagship presentation: complete narrative with all 12 figures |
| `L01_overview.tex` | ~20 | Three-zone structure | `\input{../../../_shared/preamble.tex}` | Condensed overview for breadth-focused audiences |
| `L01_deepdive.tex` | ~25 | Main content + appendix | `\input{../../../_shared/preamble.tex}` | Analytical deep dive with additional detail and appendix frames |
| `L01_core.tex` | 10 | 5-frame WHY-WHAT-HOW-WHERE-SO-WHAT core | None (self-contained) | Essential 10-frame arc, self-contained, portable |
| `L01_mini10.tex` | 11 | Full narrative arc (incl. title) | None; inline TikZ | 11-frame version with narrative arc but no external figures (inline diagrams) |
| `L01_mini5.tex` | 6 | 5-slide teaser (incl. title) | None (self-contained) | Quick teaser: WHY > WHAT > HOW > WHERE > SO WHAT, perfect for workshops or introductions |

## Frame-by-Frame Breakdown

### L01_full.tex (31 Frames)

**Opening (Frames 1–4: WHY)**
1. Title Page
2. Opening Cartoon (disruption tension: "The revolution started in a garage, not a boardroom")
3. Learning Objectives (Bloom's: Understand → Apply → Analyze → Evaluate)
4. Welcome / Bridge to Course

**Part I: What is Fintech? (Frames 5–10: WHAT)**
5. Definition and Scope
6. Evolution Timeline (Figure 01: S-curve from 1950s to 2020s)
7. Historical Phases (electronic banking → digital banking → embedded finance)
8. Characteristics of Fintech (speed, agility, customer-centricity, technology-native)
9. Fintech Ecosystem Overview (Figure 04: service categories)
10. Transition to Crisis

**Part II: The Crisis Catalyst (Frames 11–13: WHY deeper)**
11. 2008 Financial Crisis Timeline (Figure 05: market collapse and recovery)
12. Loss of Trust in Incumbents
13. Technology Opportunity Window

**Part III: Disruption of Value Chain (Frames 14–17: HOW)**
14. Traditional Banking Value Chain (unified model)
15. Value Chain Disruption (Figure 02: unbundling into payment, lending, wealth, insurance)
16. Fintech Segmentation by Service (overview of specialization)
17. Examples: PayPal (payments), LendingClub (lending), Robinhood (wealth)

**Part IV: Collaboration Models (Frames 18–21: HOW deeper)**
18. Partnership Framework (Figure 03: matrix of collaboration types)
19. Partnership Models (startup + incumbent: licensing, acquisition, API integration, white-label)
20. Bank-Fintech Partnership Flow (Figure 07: relationship dynamics)
21. Case Study: Partnership Success and Failure

**Part V: Investment and Growth (Frames 22–24: WHERE)**
22. Fintech Investment Trends (Figure 06: funding growth 2010–2020)
23. Market Size and Projections
24. Regional Fintech Hubs (Silicon Valley, London, Singapore, etc.)

**Part VI: Embedded Finance (Frames 25–28: WHERE deeper)**
25. What is Embedded Finance? (fintech features embedded in non-financial platforms)
26. Embedded Finance Architecture (Figure 08: API + integration model)
27. Use Cases: Buy Now Pay Later (BNPL), payroll, marketplace lending
28. Platform Economics

**Part VII: Competitive Comparison and Takeaway (Frames 29–31: SO WHAT)**
29. Incumbent Banks vs. Fintech Startups (Figure 09: metrics comparison)
30. Key Concepts Summary (Figure 10: taxonomy or quadrant chart)
31. Closing Cartoon (XKCD-style reflection) + Final Takeaway

---

### L01_overview.tex (~20 Frames)

Alternative structure with three-zone organization:

**Zone 1: Foundation (Frames 1–6)**
- Title, objectives, definitions, and opening cartoon

**Zone 2: Disruption (Frames 7–16)**
- Crisis catalyst, value chain unbundling, collaboration models

**Zone 3: Future (Frames 17–20)**
- Embedded finance, competitive landscape, closing takeaway

Includes subset of figures (typically 6–8 key visuals).

---

### L01_deepdive.tex (~25 Frames)

Analytical variant with main content + appendix:

**Main Content (Frames 1–22)**
- Full narrative arc similar to `L01_full.tex` but with more analytical depth and fewer figures

**Appendix (Frames 23–25)**
- Advanced topics: regulatory landscape, technology stack evolution, emerging fintech categories

---

### L01_core.tex (10 Frames)

**Essential 10-frame arc** (self-contained, no dependencies):

1. Title
2. Opening: Why Fintech Emerged (crisis + technology)
3. What is Fintech? (definition + scope)
4. Historical Evolution (3–4 key phases)
5. Value Chain Disruption (unbundling overview)
6. Collaboration Models (partnership types)
7. Embedded Finance (concept + architecture)
8. Competitive Advantage (incumbent vs. startup)
9. Key Takeaways (quadrant or summary)
10. Closing / Questions

**Inline diagrams** use TikZ (no external figures); all preamble content embedded.

---

### L01_mini10.tex (11 Frames including Title)

**Narrative arc in 11 frames** (self-contained):

1. Title Page
2. Opening Cartoon (inline TikZ stick figures)
3. What is Fintech?
4. Historical Evolution (S-curve sketch, inline TikZ or text)
5. Crisis Catalyst (2008 impact)
6. Value Chain Disruption (simple flow diagram, TikZ)
7. Collaboration Models (matrix, simplified text or TikZ)
8. Embedded Finance (concept + example)
9. Competitive Landscape
10. Key Concepts
11. Closing Takeaway + Questions

All graphics are **inline TikZ** — no external PDF figures. Designed for portability and quick delivery.

---

### L01_mini5.tex (6 Frames including Title)

**5-slide teaser arc** (self-contained, minimal):

1. Title Page
2. Why Fintech? (crisis + opportunity)
3. What & How (definition + collaboration models)
4. Where (embedded finance)
5. So What? (competitive implications)
6. Questions / Contact

**Ultra-minimal design** — mostly text with inline TikZ highlights. Perfect for:
- Pre-lecture teasers
- Workshop introductions
- Elevator pitch presentations

---

## Compilation Instructions

### Full/Overview/Deepdive Variants

Require `_shared/preamble.tex`:

```bash
cd slides/
pdflatex L01_full.tex
pdflatex L01_full.tex  # Run twice for overlays and references
```

**Prerequisites:**
- `_shared/preamble.tex` must be present in parent directory
- All figure PDFs in `figures/*/chart.pdf` or `cartoon.pdf` must exist
- LaTeX packages: `beamer`, `tikz`, `pgfplots`, `booktabs`, `multicol`

### Core/Mini10/Mini5 Variants

Self-contained (no external dependencies):

```bash
cd slides/
pdflatex L01_core.tex
pdflatex L01_mini10.tex
pdflatex L01_mini5.tex
```

**Prerequisites:**
- Standard LaTeX packages (embedded in preamble)
- No external figures required

---

## Theme and Color Configuration

All variants use:
- **Beamer Theme:** `Madrid`
- **Color Theme:** `whale` (with customizations)
- **Primary Color:** `mlteal` (#0D7377)
- **Accent Colors:** `mlpurple` (#9467BD), `mlblue` (#1F77B4), `mlred` (#D62728), etc.

**Color palette** is consistent across all slide files and matches the chart color scheme from `_shared/chart_styles.py`.

---

## Learning Objectives (Frame 3 in Full Variant)

By the end of this lecture, students will be able to:

1. **Describe** the defining characteristics of fintech and trace its historical evolution from early electronic banking to modern embedded finance. *(Understand)*
2. **Explain** how the 2008 financial crisis acted as a catalyst for fintech innovation by eroding trust in traditional institutions. *(Understand)*
3. **Classify** the major collaboration models between traditional financial institutions and fintech companies. *(Apply)*
4. **Compare** the competitive advantages and disadvantages of incumbent banks vs. fintech startups across key service dimensions. *(Analyze)*
5. **Evaluate** which collaboration model best fits a given strategic scenario. *(Evaluate)*

**Bloom's levels covered:** Understand, Apply, Analyze, Evaluate

---

## AI Agent Instructions

### For Updating Slide Content

**When editing learning objectives, frame content, or speaker notes:**

1. **Maintain the narrative arc:** WHY (disruption) → WHAT (definition/evolution) → HOW (collaboration/value chain) → WHERE (embedded finance) → SO WHAT (implications)

2. **Update all variants consistently:**
   - If you change a learning objective in `L01_full.tex`, also update it in the other full/overview/deepdive variants
   - Core/mini5/mini10 may have condensed versions of same content

3. **Assessment alignment:**
   - Quiz and exercise assessments directly reference learning objectives
   - If objectives change, coordinate with quiz/exercise maintainers

4. **Figure references:**
   - Always use relative paths: `figures/NN_label/chart.pdf`
   - Verify figure exists before compiling
   - Mini variants can skip figures and use inline TikZ diagrams instead

5. **Speaker notes:**
   - Use `\note{}` within frames to add speaker guidance
   - Notes should reinforce pedagogical intent, not repeat slide text

### For Managing Variants

**When deciding which variant to use or modify:**

- **L01_full.tex** for comprehensive courses, recorded lectures, or archival
- **L01_overview.tex** for breadth-focused classes or introductory audiences
- **L01_deepdive.tex** for analytical courses or research seminars
- **L01_core.tex** for self-contained, portable core material (15–20 min presentation)
- **L01_mini10.tex** for workshop opening or 20–25 min intensive session
- **L01_mini5.tex** for teaser, introduction, or 10–15 min elevator pitch

### For Preamble Maintenance

**When updating `_shared/preamble.tex`:**

1. All full/overview/deepdive variants will inherit the changes
2. Document your changes clearly so other lectures can follow the same pattern
3. Avoid breaking existing figure/frame references
4. Test compilation with at least one variant before committing

### For Typography and Styling

**Consistent conventions across all variants:**

- **Emphasis:** Use `\textbf{}` for strong emphasis, `\textit{}` for definitions
- **Colors:** Use predefined color names (`mlpurple`, `mlblue`, etc.) for consistency
- **Bottom notes:** Use `\bottomnote{}` for pedagogical guidance tied to assessment
- **Frame transitions:** Use overlays (`\uncover<>{}`, `\only<>{}`) sparingly; prefer clear frame sequences

---

## Dependencies

| Dependency | Location | Purpose |
|------------|----------|---------|
| Shared preamble | `_shared/preamble.tex` | Theme, colors, macros (for full/overview/deepdive only) |
| Figure PDFs | `figures/*/chart.pdf`, `figures/*/cartoon.pdf` | Included via `\includegraphics` (full/overview/deepdive only) |
| Parent AGENTS.md | `../AGENTS.md` | High-level lecture documentation |

---

## Metadata

| Field | Value |
|-------|-------|
| **Lecture** | L01 (Fintech Foundations and Overview) |
| **Audience** | MSc Financial Technology, Spring 2026 |
| **Total Variants** | 6 (3 dependent, 3 self-contained) |
| **Total Frames** | 31 (full), 20 (overview), 25 (deepdive), 10 (core), 11 (mini10), 6 (mini5) |
| **Narrative Arc** | WHY > WHAT > HOW > WHERE > SO WHAT |
| **Figures** | 12 (in full/overview/deepdive variants; inline TikZ in core/mini) |

---

**Last Updated:** 2026-02-26
**Maintainer:** FinTech Lecture Series Team
