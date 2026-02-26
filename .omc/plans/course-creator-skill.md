# Course-Creator Skill -- Implementation Plan (v2, Revised)

## Context

### Original Request
Create a modular "course-creator" skill system that orchestrates existing beamer/lecture skills to produce complete academic courses hosted on GitHub Pages. The system follows the proven pattern of the Blockchain course at https://digital-ai-finance.github.io/Blockchain/.

### Interview Summary
Two rounds of deep interview established:
- Parent orchestrator + 7 sub-skills + `course-creator:all` meta-runner architecture
- `course-creator:all` is a mode of the parent orchestrator `course-creator.md`, NOT a separate file
- Manifest-first approach (YAML input, no interactive wizard)
- 6 PDF files per lecture across 5 named variants: mini5, mini10, core, overview (extended part 1), deepdive (extended part 2), full
- Top-down content generation from a master plan
- Faithful minimal LaTeX-to-HTML conversion (direct mapping, not AI-enriched)
- Pure static HTML/CSS/JS matching the Blockchain reference exactly
- Full GitHub deployment automation via `gh` CLI and GitHub Actions
- Windows path compatibility required (forward slashes in generated paths)

### Research Findings
- Three existing OMC-learned skills form the "lecture-generation triad":
  - `beamer-slide-creator.md` (1736 lines) -- universal foundation with 3-zone architecture, 15+ layouts, TikZ blueprints, chart architecture
  - `mini-lecture-generator.md` (583 lines) -- 5-slide teaser and 10-slide standalone arcs, self-contained preamble, inline TikZ/pgfplots
  - `full-lecture-generator.md` (900 lines) -- 30-slide expansion, external Python charts, shared preamble, companion quiz + exercise files
- `academic-beamer-slides` agent (620 lines) -- batch mode, pattern inference, auto-fix quality system
- `beamer_validation/` tool suite -- 8 Python checkers (slide refs, figure existence, notation, undefined terms, URLs, DOIs, citations, BibTeX)
- HTML templates extracted from Blockchain reference: index page, lecture page, quiz page, gallery page
- Complete CSS extracted from Blockchain reference (inline `<style>` blocks per page, no external CSS files)
- Gallery PNG path pattern: `slides-png/L{NN}_{variant}/slide_01.png`

### Revision Notes (v2)
This revision addresses 8 critical issues and 8 minor issues from the Critic + Architect review:
- C1: Section tag colors corrected to match Blockchain reference exactly
- C2: Core variant uses frame-index-based selection (no tagging system)
- C3: `section_framework` scoped to extended variant only
- C4: Gallery PNGs moved inside `website/` tree
- C5: Complete CSS from Blockchain reference included as inline `<style>` blocks
- C6: Stage 1 = .tex source only; Stage 2 = all chart.py + .pdf
- C7: GitHub Actions = simple static deploy; LaTeX compilation is local
- C8: Downloads directory populated locally in Stage 7
- A1: Extended variant = 2 files (overview + deepdive), total 6 PDF files per lecture
- A2: `figures/` directory name used everywhere (not `charts/` for figure scripts)
- A3: Design tokens confirmed from reference

---

## Work Objectives

### Core Objective
Build a complete, production-ready skill system at `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/` that takes a YAML manifest and produces a fully deployed academic course website with slides, HTML lectures, quizzes, galleries, and projects.

### Deliverables
1. **8 skill files**: 1 orchestrator + 7 sub-skills (course-creator:all is a mode of the orchestrator)
2. **Manifest schema specification** embedded in orchestrator skill
3. **HTML/CSS/JS templates** embedded in relevant sub-skills as inline `<style>` blocks per page type
4. **GitHub Actions workflow template** (simple static deploy) embedded in the deploy sub-skill
5. **Quality gate definitions** per stage

### Definition of Done
- Running `course-creator:all` with a valid YAML manifest produces a complete course website
- Each sub-skill can run independently (e.g., `course-creator:slides` to regenerate only slides)
- Output matches the Blockchain reference site's visual design exactly (verified by inline CSS)
- All 6 PDF files compile without errors for every lecture
- GitHub Actions workflow deploys pre-built static assets (no LaTeX in CI)
- Zero manual HTML authoring required after manifest creation

---

## Must Have / Must NOT Have

### Must Have (Guardrails)
- YAML manifest drives everything -- no hardcoded course content
- Each sub-skill is a standalone `.md` file with clear triggers, inputs, and outputs
- Orchestrator calls existing triad skills by reference, does not duplicate their logic
- HTML conversion is faithful and minimal (LaTeX frame content maps directly to HTML sections)
- All 6 PDF files use the same master content plan (top-down derivation)
- Pure static output -- no build tools, no frameworks, no server-side rendering
- Inline `<style>` blocks per HTML page (matching Blockchain reference pattern, NO external CSS files)
- Module color coding system (green/orange/red/blue for up to 4 modules)
- 8-section lecture page template (WHY/WHAT/CASE/HOW/RISK/WHERE/IMPACT/SOWHAT) with correct colors from reference
- Dual-tier quizzes: standard (20 MCQ) + advanced (20 MCQ) per lecture
- KaTeX via CDN `<script>` tag for formula rendering in lecture HTML pages
- All deployable assets (HTML, PNGs, PDFs) live under `website/` tree
- `figures/` directory name for chart/figure scripts (matching full-lecture-generator convention)
- Windows path compatibility: use forward slashes in all generated paths

### Must NOT Have
- Interactive wizard or CLI prompts during generation
- React, Vue, Next.js, or any JavaScript framework
- External CSS frameworks (Bootstrap, Tailwind) or external `.css` files
- AI-enriched HTML content beyond what the LaTeX source contains
- Hardcoded topic names, lecture counts, or domain assumptions in the skill files
- Duplication of beamer-slide-creator, mini-lecture-generator, or full-lecture-generator logic
- Any dependency on MCP servers or external APIs beyond `gh` CLI
- LaTeX compilation in GitHub Actions CI (compilation is local only)

---

## Manifest Format Specification

### Course Manifest Schema (`course.yaml`)

```yaml
# === COURSE IDENTITY ===
course:
  name: "Blockchain Technology and Decentralized Finance"
  short_name: "Blockchain"           # Used in URLs and directory names
  institution: "University of Zurich"
  department: "Department of Finance"
  level: "BSc"                       # BSc | MSc | PhD
  semester: "Spring 2026"
  instructor:
    name: "Joerg Osterrieder"
    email: "joerg.osterrieder@uzh.ch"
  repo:
    org: "digital-ai-finance"        # GitHub org or username
    name: "Blockchain"               # Repo name (created if missing)
    visibility: "public"             # public | private

# === MODULE STRUCTURE ===
modules:
  - id: "foundations"
    name: "Foundations"
    color: "#2CA02C"                 # Module badge color (green)
    lectures: [1, 2, 3]             # Lecture numbers in this module

  - id: "technology"
    name: "Technology"
    color: "#FF7F0E"                 # orange
    lectures: [4, 5, 6]

  - id: "applications"
    name: "Applications"
    color: "#D62728"                 # red
    lectures: [7, 8, 9]

  - id: "frontiers"
    name: "Frontiers"
    color: "#3333B2"                 # blue
    lectures: [10, 11, 12]

# === LECTURES ===
lectures:
  - number: 1
    title: "What Is Blockchain?"
    subtitle: "From Ledgers to Distributed Trust"
    topics:
      - "History of ledgers and double-entry bookkeeping"
      - "The trust problem in digital transactions"
      - "Hash functions and Merkle trees"
      - "Blocks, chains, and immutability"
      - "Consensus without a central authority"
    prerequisites: []
    figures:
      domain_focus: "finance"        # Guides chart data generation
      required_types:                # Optional override; otherwise auto-derived
        - "time_series"
        - "flowchart"
        - "comparison_bar"

  - number: 2
    title: "Cryptographic Foundations"
    subtitle: "The Math That Makes It Work"
    topics:
      - "Symmetric vs asymmetric encryption"
      - "Digital signatures and verification"
      - "Hash functions: SHA-256 in practice"
      - "Public-key infrastructure"
    prerequisites: [1]

  # ... (all lectures follow same pattern)

# === PROJECT TRACKS ===
projects:
  - id: "defi-dashboard"
    title: "DeFi Dashboard"
    description: "Build a real-time dashboard tracking DeFi protocol metrics"
    difficulty: "Intermediate"
    lectures_required: [4, 5, 6, 7]
    deliverables:
      - "Working web dashboard"
      - "Data pipeline documentation"
      - "5-minute presentation"

  - id: "smart-contract-audit"
    title: "Smart Contract Security Audit"
    description: "Audit a deployed smart contract for common vulnerabilities"
    difficulty: "Advanced"
    lectures_required: [5, 6, 8, 9]
    deliverables:
      - "Audit report (PDF)"
      - "Test suite"
      - "Remediation recommendations"

# === QUIZ CONFIGURATION ===
quizzes:
  standard:
    count: 20                        # MCQ per lecture
    bloom_distribution:
      understand: 4
      apply: 8
      analyze: 6
      evaluate: 2
  advanced:
    count: 20
    bloom_distribution:
      apply: 4
      analyze: 8
      evaluate: 6
      create: 2

# === VISUAL THEME ===
theme:
  nav_color: "#1a1a4e"              # Dark navy navigation bar
  hero_gradient_start: "#3333B2"    # Hero section gradient
  hero_gradient_end: "#0066CC"
  accent_color: "#FF7F0E"
  font_family: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
```

### Chart Auto-Derivation Algorithm

When a lecture's `figures` field is omitted or has no `required_types`, the system auto-derives chart types:

```
Algorithm: chart_auto_derive(lecture, course_level)
  Input: lecture.topics, course.level
  Output: list of {type, description} chart specs

  1. Count = 10 (base for full variant) + 2 (opening/closing cartoon)
  2. For each topic in lecture.topics:
     a. If topic contains "comparison" or "vs" -> add "comparison_bar"
     b. If topic contains "timeline" or "history" -> add "time_series"
     c. If topic contains "flow" or "process" or "lifecycle" -> add "flowchart"
     d. If topic contains "architecture" or "structure" -> add "diagram"
     e. Otherwise -> add "concept_illustration"
  3. Fill remaining slots up to Count with:
     - 1 "overview_diagram" (always)
     - 1 "summary_table" (always)
     - Remaining: alternate "concept_illustration" and "data_visualization"
  4. Assign figure numbering: 01_, 02_, ..., {Count}_
  5. Opening cartoon = figure 11, Closing cartoon = figure {Count}
```

### Manifest Validation Rules
- Every lecture number in `modules[].lectures` must exist in `lectures[]`
- Every lecture number must appear in exactly one module
- `prerequisites` must reference lecture numbers that exist and have a lower number
- Module colors should be distinct (warn if two modules share the same hex)
- At least 1 module and 1 lecture required
- Maximum 20 lectures per course (practical limit for generation time)

---

## Design Tokens (Blockchain Reference)

### Confirmed Color System

| Token | Value | Usage |
|-------|-------|-------|
| Primary | `#3333B2` | Headings, accents, active states |
| Link | `#0066CC` | All hyperlinks, action buttons |
| Nav Background | `#1a1a4e` | Top navigation bar |
| Page Background | `#f6f8fa` | Body background |
| Border | `#e1e4e8` | Card borders, dividers |
| Text Primary | `#24292e` | Body text |
| Text Muted | `#586069` | Captions, metadata |
| Hero Gradient | `#3333B2 -> #0066CC` | Hero banner |

### Section Tag Colors (8 Sections)

| Section | Tag Background | Tag Text | Left Border |
|---------|---------------|----------|-------------|
| WHY | `#d4edda` | `#155724` | `#2CA02C` |
| WHAT | `#e8e8f5` | `#3333B2` | `#3333B2` |
| CASE | `#ffecd2` | `#b45309` | `#FF7F0E` |
| HOW | `#e0f0ff` | `#0052a3` | `#0066CC` |
| RISK | `#f8d7da` | `#721c24` | `#D62728` |
| WHERE | `#d1ecf1` | `#0c5460` | `#17a2b8` |
| IMPACT | `#fff3cd` | `#856404` | `#F7931A` |
| SOWHAT | `#f0d6ff` | `#5b21b6` | `#9b59b6` |

### Module Group Colors

| Group | Badge Background | Badge Text | Section Head BG | Border Left |
|-------|-----------------|------------|-----------------|-------------|
| g1 (Foundations) | `#d4edda` | `#2CA02C` | `#2CA02C` | `#2CA02C` |
| g2 (Platforms) | `#ffecd2` | `#FF7F0E` | `#FF7F0E` | `#FF7F0E` |
| g3 (Applications) | `#f8d7da` | `#D62728` | `#D62728` | `#D62728` |
| g4 (Advanced) | `#e8e8f5` | `#3333B2` | `#3333B2` | `#3333B2` |

### Callout Box Colors

| Variant | Background | Border Left | Text Color |
|---------|-----------|-------------|------------|
| callout-blue | `#e0f0ff` | `#0066CC` | `#003d80` |
| callout-purple | `#f0ecff` | `#3333B2` | `#221166` |
| callout-orange | `#fff3e0` | `#FF7F0E` | `#7a3e00` |
| callout-green | `#e8f5e9` | `#2CA02C` | `#1a5c1a` |
| callout-red | `#fde8e8` | `#D62728` | `#7a0000` |
| callout-yellow | `#fffbe6` | `#F7931A` | `#7a4a00` |

---

## File Structure

### Skill Directory Layout

```
C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/
  course-creator.md              # Parent orchestrator (triggers, routing, manifest parsing)
                                 # Also handles course-creator:all mode
  course-creator-slides.md       # Stage 1: Generate LaTeX Beamer .tex source files
  course-creator-charts.md       # Stage 2: Generate Python chart scripts + compile to PDF
  course-creator-galleries.md    # Stage 3: PDF-to-PNG slide galleries (BEFORE lectures)
  course-creator-lectures.md     # Stage 4: Convert LaTeX to HTML lecture pages
  course-creator-quizzes.md      # Stage 5: Generate dual-tier quizzes
  course-creator-projects.md     # Stage 6: Generate project track pages
  course-creator-deploy.md       # Stage 7: Index page, repo setup, deploy
```

### Generated Course Output Directory

```
{course_short_name}/                          # e.g., Blockchain/
  course.yaml                                  # Original manifest (copied)
  _shared/
    preamble.tex                               # Shared LaTeX preamble
    chart_styles.py                            # Shared matplotlib styles

  lectures/
    L01_what_is_blockchain/
      slides/
        L01_mini5.tex                          # 5-slide teaser
        L01_mini5.pdf
        L01_mini10.tex                         # 10-slide standalone
        L01_mini10.pdf
        L01_core.tex                           # ~10 key slides (frame-index extraction)
        L01_core.pdf
        L01_overview.tex                       # Extended part 1: accessible, visual (~25-30 slides)
        L01_overview.pdf
        L01_deepdive.tex                       # Extended part 2: mathematical detail (~15-20 slides)
        L01_deepdive.pdf
        L01_full.tex                           # ~30 slides + quiz + exercises
        L01_full.pdf
      figures/
        01_concept_overview/
          chart.py
          chart.pdf
        02_hash_function_demo/
          chart.py
          chart.pdf
        ...
        11_opening_cartoon/
          cartoon.py
          cartoon.pdf
        22_closing_cartoon/
          cartoon.py
          cartoon.pdf
      quizzes/
        L01_quiz_standard.tex                  # 20 MCQ standard
        L01_quiz_standard.pdf
        L01_quiz_advanced.tex                  # 20 MCQ advanced
        L01_quiz_advanced.pdf
      exercises/
        L01_exercises.tex
        L01_exercises.pdf

    L02_cryptographic_foundations/
      ...  (same structure)

  website/
    index.html                                 # Course landing page (inline CSS)
    lectures/
      L01.html                                 # Lecture page (inline CSS, 8-section layout)
      L02.html
      ...
    quizzes/
      L01_standard.html                        # Standard quiz page (inline CSS)
      L01_advanced.html                        # Advanced quiz page (inline CSS)
      L02_standard.html
      ...
    galleries/
      L01.html                                 # Gallery page with tabs (inline CSS+JS)
      L02.html
      ...
      images/                                  # All gallery PNGs under website/
        L01/
          mini5/
            slide_01.png ... slide_06.png
          mini10/
            slide_01.png ... slide_11.png
          core/
            slide_01.png ... slide_11.png
          extended/
            slide_01.png ... slide_30.png
          full/
            slide_01.png ... slide_32.png
        L02/
          ...
    projects/
      defi-dashboard.html                      # Project track page
      smart-contract-audit.html
      ...
    downloads/                                 # PDF copies for web download
      L01_mini5.pdf
      L01_mini10.pdf
      L01_core.pdf
      L01_overview.pdf                         # Extended overview part
      L01_deepdive.pdf                         # Extended deepdive part
      L01_full.pdf
      L02_mini5.pdf
      ...
    charts/                                    # Chart PNGs for lecture HTML embedding
      L01/
        01_concept_overview.png
        02_hash_function_demo.png
        ...
      L02/
        ...

  .github/
    workflows/
      deploy.yml                               # Simple static site deployment
```

---

## Stage Execution Order

**IMPORTANT: Stage ordering has been corrected to ensure dependencies are met.**

```
Stage 1: course-creator:slides    -- Generate .tex source files + master content plans
Stage 2: course-creator:charts    -- Generate chart.py scripts + compile to chart.pdf
        (Then: compile all .tex to .pdf locally using pdflatex)
Stage 3: course-creator:galleries -- Convert PDFs to PNGs (needed before Stage 4 for TikZ replacement)
Stage 4: course-creator:lectures  -- Convert LaTeX to HTML lecture pages (uses gallery PNGs for TikZ)
Stage 5: course-creator:quizzes   -- Generate dual-tier quiz HTML pages
Stage 6: course-creator:projects  -- Generate project track pages
Stage 7: course-creator:deploy    -- Generate index.html, copy downloads, setup repo, deploy
```

---

## Per-Stage Implementation

---

### STAGE 1: course-creator:slides

**Purpose:** Generate all LaTeX Beamer `.tex` source files and master content plans for every lecture. This stage produces ONLY `.tex` files and content plans -- NO chart generation, NO PDF compilation.

**Inputs:**
- `course.yaml` manifest (parsed by orchestrator, passed as structured data)
- Lecture-generation triad skills (referenced, not duplicated)

**Process:**

1. **Master Content Plan Generation** (per lecture)
   For each lecture in the manifest, generate a master content plan document:
   ```
   Lecture {N}: {title}
   Core tension: [one sentence with "but" or a question]
   Topics: [from manifest]

   Slide-by-slide spec:
     Slide 1: [role, layout, content summary, figure ref, bottomnote]
     Slide 2: ...
     ...

   Notation table:
     | Symbol | Meaning | Where Used |

   Figure allocation:
     | Figure | Type | Section | Description |

   Domain applications:
     | Application | Section | Worked example? |
   ```

2. **Variant Derivation** (top-down from master plan)

   | Variant | Files Produced | Generation Method |
   |---------|---------------|-------------------|
   | `full` (~30 slides) | `L{NN}_full.tex` | Invoke `full-lecture-generator` with master plan, topics. Uses fixed 10-role arc: WHY>FEEL>WHAT>CASE>HOW>RISK>WHERE>IMPACT>SOWHAT>ACT. |
   | `overview` (~25-30 slides) | `L{NN}_overview.tex` | Invoke `beamer-slide-creator` with INTRO/CORE/CLOSING zones. Accessible, visual, problem-first. |
   | `deepdive` (~15-20 slides) | `L{NN}_deepdive.tex` | Invoke `beamer-slide-creator` with MAIN BODY + `\appendix`. Mathematical detail, proofs, advanced topics. |
   | `mini10` (10 slides) | `L{NN}_mini10.tex` | Invoke `mini-lecture-generator` 10-slide arc. |
   | `mini5` (5 slides) | `L{NN}_mini5.tex` | Invoke `mini-lecture-generator` 5-slide arc. |
   | `core` (~10 slides) | `L{NN}_core.tex` | Frame-index extraction from full variant (see algorithm below). |

   **Note on `section_framework`:** The `section_framework` field from the manifest applies ONLY to the `overview` and `deepdive` variants (generated via `beamer-slide-creator`). The `full` variant ALWAYS uses the fixed 10-role arc from `full-lecture-generator` regardless of any `section_framework` setting. The `section_framework` field should NOT appear in the `full-lecture-generator` prompt template.

3. **Core Variant Extraction Algorithm** (frame-index-based selection)

   ```
   Algorithm: extract_core_variant(full_tex_content)
     Input: L{NN}_full.tex (the full ~30-slide variant)
     Output: L{NN}_core.tex (~10 slides)

     1. Parse all \begin{frame}...\end{frame} blocks, assign index 1..N
     2. Map frame indices to the 8 arc sections using the full-lecture-generator
        10-role arc (frame ranges are fixed by the arc):
          WHY:    frames 1-4     -> select frame 1
          WHAT:   frames 6-9     -> select frame 6
          CASE:   frames 10-13   -> select frame 10
          HOW:    frames 14-17   -> select frame 14
          RISK:   frames 18-20   -> select frame 18
          WHERE:  frames 21-23   -> select frame 21
          IMPACT: frames 24-25   -> select frame 24
          SOWHAT: frames 26-28   -> select frame 26
     3. Take the FIRST frame from each of the 8 arc sections (8 frames)
     4. Add the title frame (frame 0) and the key takeaways frame (last frame)
     5. Total: 10 frames = title + 8 section-first + takeaways
     6. Wrap in a self-contained preamble (copy from mini10 pattern)
     7. Write to L{NN}_core.tex
   ```

4. **Generation Order** (per lecture)
   ```
   a. Generate master content plan (sequential -- sets the tone for everything)
   b. Generate full variant via full-lecture-generator (establishes canonical content)
   c. Generate overview + deepdive via beamer-slide-creator (two separate .tex files)
   d. Extract core variant from full (frame-index selection, no AI generation needed)
   e. Generate mini10 via mini-lecture-generator (10-slide arc from master plan)
   f. Generate mini5 via mini-lecture-generator (5-slide arc from master plan)
   ```

5. **Cross-Lecture Parallelism**
   - Lectures with no prerequisites can be generated in parallel
   - Lectures with prerequisites must wait for prerequisite master plans
   - Within a single lecture, steps b and e/f are independent (can parallelize)

6. **Skill Integration Prompts**

   **For full-lecture-generator:**
   ```
   Generate a full lecture (~30 slides) for:
   Title: {lecture.title}
   Subtitle: {lecture.subtitle}
   Course: {course.name} ({course.level})
   Instructor: {course.instructor.name}
   Topics to cover: {lecture.topics}
   Prerequisites covered in previous lectures: {resolved_prerequisites}
   Domain focus for figures: {lecture.figures.domain_focus}
   Audience level: {course.level}
   Shared preamble path: ../_shared/preamble.tex
   Figure output directory: figures/

   Follow the full-lecture-generator skill specification exactly.
   Use the fixed 10-role arc (WHY>FEEL>WHAT>CASE>HOW>RISK>WHERE>IMPACT>SOWHAT>ACT).
   Generate companion quiz and exercise files.
   DO NOT generate chart.py scripts -- figure scripts are handled in Stage 2.
   Include \includegraphics references to figures/ paths for where charts will go.
   ```

   **For mini-lecture-generator (10-slide):**
   ```
   Generate a 10-slide standalone mini-lecture for:
   Title: {lecture.title}
   Core tension: {master_plan.core_tension}
   Key topics (select 5 most important): {lecture.topics}
   Audience level: {course.level}

   Follow the mini-lecture-generator skill specification exactly.
   Use self-contained preamble (inline TikZ/pgfplots only).
   Use the 10-slide WHY>FEEL>WHAT>CASE>HOW>RISK>WHERE>IMPACT>SOWHAT>ACT arc.
   ```

   **For mini-lecture-generator (5-slide):**
   ```
   Generate a 5-slide teaser mini-lecture for:
   Title: {lecture.title}
   Core tension: {master_plan.core_tension}
   Key topics (select 3 most important): {lecture.topics}

   Follow the mini-lecture-generator 5-slide teaser arc.
   Use self-contained preamble.
   Use the WHY>WHAT>HOW>WHERE>SOWHAT arc.
   ```

   **For beamer-slide-creator (overview file):**
   ```
   Generate the OVERVIEW file (~25-30 slides) of an extended lecture:
   Title: {lecture.title}
   Topics: {lecture.topics}
   Audience level: {course.level}
   Section framework: {lecture.section_framework | default: "PMSP"}

   This is the accessible, visual, problem-first overview.
   Use beamer-slide-creator three-zone architecture: INTRO/CORE/CLOSING.
   Shared preamble path: ../_shared/preamble.tex
   Figure output directory: figures/
   Output file: L{NN}_overview.tex

   DO NOT generate chart.py scripts -- figure scripts are handled in Stage 2.
   ```

   **For beamer-slide-creator (deepdive file):**
   ```
   Generate the DEEPDIVE file (~15-20 slides) of an extended lecture:
   Title: {lecture.title} -- Mathematical Deep Dive
   Topics: {lecture.topics} (advanced/mathematical aspects)
   Audience level: {course.level}

   This is the mathematical detail / proofs / advanced topics appendix.
   Use beamer-slide-creator MAIN BODY + \appendix structure.
   Use \section* for deepdive sections.
   Shared preamble path: ../_shared/preamble.tex
   Figure output directory: figures/
   Output file: L{NN}_deepdive.tex

   DO NOT generate chart.py scripts -- figure scripts are handled in Stage 2.
   ```

**Quality Gates:**
- [ ] All 6 .tex files per lecture are syntactically valid LaTeX
- [ ] Frame counts within expected ranges (mini5: 5-6, mini10: 10-11, core: 10-11, overview: 25-30, deepdive: 15-20, full: 29-33)
- [ ] Self-contained preamble in mini5, mini10, and core (zero `\input` commands)
- [ ] Shared preamble in full, overview, and deepdive (`\input{../_shared/preamble.tex}`)
- [ ] Notation consistent across all variants of the same lecture
- [ ] No chart.py scripts generated in this stage (only \includegraphics references)

**Outputs:**
- 6 `.tex` files per lecture (mini5, mini10, core, overview, deepdive, full)
- Master content plan document per lecture
- `quizzes/` directory with standard quiz .tex (from full-lecture-generator companion)
- `exercises/` directory with exercise .tex

---

### STAGE 2: course-creator:charts

**Purpose:** Generate all Python matplotlib chart scripts and compile them to PDF. This is the ONLY stage that creates chart.py scripts and runs them.

**Inputs:**
- Master content plans from Stage 1
- Figure allocation tables from master plans
- `_shared/chart_styles.py` (generated once per course)

**Process:**

1. **Generate shared chart_styles.py** (once per course)
   ```python
   """Shared chart styles for {course.name}."""

   import matplotlib.pyplot as plt

   V4_COLORS = {
       'MLPURPLE': '#3333B2',
       'MLBLUE': '#0066CC',
       'MLORANGE': '#FF7F0E',
       'MLGREEN': '#2CA02C',
       'MLRED': '#D62728',
       'MLLAVENDER': '#ADADE0',
       'MLGRAY': '#808080',
   }

   def apply_v4_style():
       plt.rcParams.update({
           'font.size': 14, 'axes.labelsize': 14, 'axes.titlesize': 16,
           'xtick.labelsize': 13, 'ytick.labelsize': 13, 'legend.fontsize': 13,
           'figure.figsize': (10, 6), 'figure.dpi': 150,
           'axes.spines.top': False, 'axes.spines.right': False,
       })

   def save_chart(fig, path):
       fig.savefig(path, dpi=300, bbox_inches='tight')
       plt.close(fig)
   ```

2. **Per-lecture figure generation**
   - Mini variants (mini5, mini10, core): Use inline TikZ/pgfplots only. No external chart scripts.
   - Full variant: Follow `full-lecture-generator` chart specification (10+ content charts + 2 cartoons per lecture)
   - Extended variants (overview, deepdive): Charts shared with full variant where applicable; deepdive adds additional diagnostic/analytical charts
   - Cartoon generation uses XKCD-style via `plt.xkcd()` context manager

3. **Figure naming convention** (uses `figures/` directory, matching full-lecture-generator)
   ```
   lectures/L{NN}_{topic}/figures/
     01_{descriptive_name}/chart.py + chart.pdf
     02_{descriptive_name}/chart.py + chart.pdf
     ...
     11_opening_cartoon/cartoon.py + cartoon.pdf
     22_closing_cartoon/cartoon.py + cartoon.pdf
   ```

4. **Compilation**
   ```bash
   cd lectures/L{NN}_{topic}/figures/
   for dir in */; do
     cd "$dir"
     python chart.py 2>/dev/null || python cartoon.py 2>/dev/null
     cd ..
   done
   ```

5. **Then: Compile all .tex to .pdf** (local compilation, after charts are ready)
   ```bash
   cd lectures/L{NN}_{topic}/slides/
   for tex in *.tex; do
     pdflatex -interaction=nonstopmode "$tex"
     pdflatex -interaction=nonstopmode "$tex"   # Second pass for refs
   done
   ```

**Quality Gates:**
- [ ] Every chart.py produces a valid chart.pdf
- [ ] Every chart.py has CHART_METADATA dict
- [ ] Every chart.py imports from `_shared/chart_styles.py` (full/extended variants)
- [ ] Color palette uses only V4_COLORS
- [ ] `figsize` is (10, 6) for all charts
- [ ] `np.random.seed(42)` present where random data is used
- [ ] No `plt.show()` calls (only `plt.savefig`)
- [ ] All 6 .tex files compile to valid .pdf with pdflatex (0 errors)
- [ ] Zero overfull vbox warnings
- [ ] Chart-to-slide ratio >= 1:4 for full and extended variants
- [ ] Opening and closing cartoons present in full and extended variants

**Outputs:**
- chart.py + chart.pdf in each `figures/` subdirectory
- All 6 .pdf files per lecture compiled from .tex

---

### STAGE 3: course-creator:galleries

**Purpose:** Convert PDF slides to PNG images, placing them inside the `website/` tree, and build tabbed gallery pages.

**Inputs:**
- Compiled PDF files from Stage 2 (all 6 files per lecture)
- Gallery HTML/CSS/JS template (inline)

**Process:**

1. **PDF to PNG Conversion** (into `website/galleries/images/`)
   ```bash
   # For each variant of each lecture:
   mkdir -p website/galleries/images/L{NN}/mini5
   pdftoppm -png -r 200 lectures/L{NN}_{topic}/slides/L{NN}_mini5.pdf \
     website/galleries/images/L{NN}/mini5/slide

   # Rename pdftoppm output from slide-01.png to slide_01.png
   for f in website/galleries/images/L{NN}/mini5/slide-*.png; do
     mv "$f" "$(echo $f | sed 's/slide-/slide_/')"
   done

   # Repeat for: mini10, core, overview (as "extended"), deepdive, full
   # Note: "extended" tab in gallery shows overview slides
   mkdir -p website/galleries/images/L{NN}/extended
   pdftoppm -png -r 200 lectures/L{NN}_{topic}/slides/L{NN}_overview.pdf \
     website/galleries/images/L{NN}/extended/slide
   ```

   Fallback if pdftoppm is unavailable:
   ```bash
   magick -density 200 L{NN}_mini5.pdf -quality 90 \
     website/galleries/images/L{NN}/mini5/slide_%02d.png
   ```

2. **Gallery HTML Page** (with 5 variant tabs)

   Each gallery page uses inline `<style>` and `<script>` blocks. Complete template:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,initial-scale=1.0">
   <title>L{NN} Slide Gallery - {course.name}</title>
   <style>
   *{box-sizing:border-box;margin:0;padding:0}
   body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;background:#f6f8fa;color:#24292e;font-size:13px;line-height:1.5}
   a{color:#0066CC;text-decoration:none}
   a:hover{text-decoration:underline}
   .nav{background:#1a1a4e;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:200}
   .nav-title{color:#fff;font-weight:600;font-size:14px}
   .nav-links{display:flex;gap:16px}
   .nav-links a{color:#fff;font-size:11px;opacity:0.8}
   .nav-links a:hover{opacity:1;text-decoration:none}
   .container{max-width:1300px;margin:0 auto;padding:16px 20px}
   .back{display:inline-block;margin-bottom:12px;font-size:12px;color:#586069}
   .back:hover{color:#0066CC;text-decoration:none}
   .page-title{font-size:20px;font-weight:700;color:#24292e;margin-bottom:4px}
   .page-sub{font-size:12px;color:#586069;margin-bottom:20px}
   .tabs{display:flex;gap:0;margin-bottom:0;border-bottom:2px solid #e1e4e8}
   .tab-btn{padding:9px 20px;font-size:12px;font-weight:600;color:#586069;background:none;border:none;cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px;transition:all 0.15s;border-radius:4px 4px 0 0;display:flex;align-items:center;gap:6px}
   .tab-btn:hover{color:#3333B2;background:#f0ecff}
   .tab-btn.active{color:#3333B2;border-bottom-color:#3333B2;background:#f0ecff}
   .tab-badge{font-size:10px;background:#e8e8f5;color:#3333B2;padding:1px 6px;border-radius:10px;font-weight:700}
   .tab-btn.active .tab-badge{background:#3333B2;color:#fff}
   .tab-panel{display:none;padding-top:16px}
   .tab-panel.active{display:block}
   .panel-head{display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:10px}
   .panel-title{font-size:14px;font-weight:700;color:#24292e}
   .panel-desc{font-size:11px;color:#586069;margin-top:2px}
   .dl-btn{display:inline-flex;align-items:center;gap:6px;padding:7px 14px;background:#0066CC;color:#fff;border-radius:4px;font-size:12px;font-weight:600;transition:all 0.15s}
   .dl-btn:hover{background:#0052a3;color:#fff;text-decoration:none;transform:translateY(-1px)}
   .slide-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
   .slide-card{cursor:pointer;border:2px solid #e1e4e8;border-radius:5px;overflow:hidden;background:#fff;transition:all 0.15s;position:relative}
   .slide-card:hover{border-color:#3333B2;box-shadow:0 4px 12px rgba(51,51,178,0.15);transform:translateY(-2px)}
   .slide-card img{width:100%;height:auto;display:block;background:#f0f0f0}
   .slide-card .slide-num{position:absolute;bottom:0;left:0;right:0;background:rgba(26,26,78,0.75);color:#fff;font-size:10px;font-weight:600;padding:3px 7px;text-align:center}
   .slide-card:hover .slide-num{background:rgba(51,51,178,0.9)}
   .slide-placeholder{width:100%;padding-bottom:56.25%;background:linear-gradient(135deg,#e8e8f5 0%,#d0d0ee 100%);position:relative}
   .slide-placeholder-inner{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#3333B2;font-size:11px;font-weight:600;gap:4px}
   .slide-placeholder-num{font-size:18px;font-weight:700;color:#3333B2}
   .lightbox{display:none;position:fixed;inset:0;background:rgba(0,0,0,0.9);z-index:1000;align-items:center;justify-content:center}
   .lightbox.open{display:flex}
   .lightbox-inner{position:relative;max-width:90vw;max-height:90vh;display:flex;flex-direction:column;align-items:center}
   .lightbox-img{max-width:100%;max-height:80vh;object-fit:contain;border-radius:3px;box-shadow:0 8px 40px rgba(0,0,0,0.5)}
   .lightbox-controls{display:flex;align-items:center;gap:16px;margin-top:12px}
   .lb-btn{background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);color:#fff;padding:7px 16px;border-radius:4px;cursor:pointer;font-size:13px;font-weight:600;transition:background 0.15s}
   .lb-btn:hover{background:rgba(255,255,255,0.28)}
   .lb-btn:disabled{opacity:0.3;cursor:default}
   .lb-counter{color:#fff;font-size:12px;min-width:70px;text-align:center;opacity:0.8}
   .lb-close{position:absolute;top:-40px;right:0;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);color:#fff;width:32px;height:32px;border-radius:4px;cursor:pointer;font-size:18px;font-weight:700;display:flex;align-items:center;justify-content:center;transition:background 0.15s}
   .lb-close:hover{background:rgba(255,255,255,0.3)}
   .lb-filename{color:rgba(255,255,255,0.5);font-size:10px;margin-top:6px}
   .foot{text-align:center;padding:20px;font-size:10px;color:#586069;margin-top:16px}
   @media(max-width:1000px){.slide-grid{grid-template-columns:repeat(3,1fr)}}
   @media(max-width:700px){.slide-grid{grid-template-columns:repeat(2,1fr)}.tabs{flex-wrap:wrap}.tab-btn{flex:1;justify-content:center;padding:8px 10px;font-size:11px}.panel-head{flex-direction:column;align-items:flex-start}}
   </style>
   </head>
   <!-- ... body with 5 tabs: mini5, mini10, core, extended, full ... -->
   <!-- Image src paths: images/L{NN}/{variant}/slide_01.png (relative to galleries/) -->
   <!-- Inline <script> with SLIDE_SETS, buildGrid, switchTab, lightbox functions -->
   ```

   **Gallery SLIDE_SETS JavaScript data structure:**
   ```javascript
   var SLIDE_SETS = {
     mini5:    { base: 'images/L{NN}/mini5/',    count: {N}, label: '5-Slide Teaser',     pdf: '../downloads/L{NN}_mini5.pdf' },
     mini10:   { base: 'images/L{NN}/mini10/',   count: {N}, label: '10-Slide Standalone', pdf: '../downloads/L{NN}_mini10.pdf' },
     core:     { base: 'images/L{NN}/core/',     count: {N}, label: 'Core (10 slides)',    pdf: '../downloads/L{NN}_core.pdf' },
     extended: { base: 'images/L{NN}/extended/',  count: {N}, label: 'Extended Overview',   pdf: '../downloads/L{NN}_overview.pdf' },
     full:     { base: 'images/L{NN}/full/',     count: {N}, label: 'Full Lecture',        pdf: '../downloads/L{NN}_full.pdf' }
   };
   ```

   **Complete gallery JavaScript (inline):**
   ```javascript
   var currentSet = 'mini5';
   var currentIndex = 0;

   function padNum(n) { return n < 10 ? '0' + n : '' + n; }

   function buildGrid(setKey) {
     var set = SLIDE_SETS[setKey];
     var grid = document.getElementById('grid-' + setKey);
     var html = '';
     for (var i = 1; i <= set.count; i++) {
       var filename = 'slide_' + padNum(i) + '.png';
       var src = set.base + filename;
       var label = i === 1 ? 'Title slide' : 'Slide ' + (i - 1);
       html += '<div class="slide-card" onclick="openLightbox(\'' + setKey + '\',' + (i-1) + ')">';
       html += '<img src="' + src + '" alt="' + label + '" loading="lazy" onerror="this.parentNode.replaceChild(makePlaceholder(' + i + '),this)">';
       html += '<div class="slide-num">' + label + '</div>';
       html += '</div>';
     }
     grid.innerHTML = html;
   }

   function makePlaceholder(num) {
     var outer = document.createElement('div');
     outer.className = 'slide-placeholder';
     var inner = document.createElement('div');
     inner.className = 'slide-placeholder-inner';
     var numEl = document.createElement('div');
     numEl.className = 'slide-placeholder-num';
     numEl.textContent = padNum(num);
     var lbl = document.createElement('div');
     lbl.textContent = num === 1 ? 'Title Slide' : 'Slide ' + (num - 1);
     inner.appendChild(numEl);
     inner.appendChild(lbl);
     outer.appendChild(inner);
     return outer;
   }

   // Build all grids
   Object.keys(SLIDE_SETS).forEach(function(k) { buildGrid(k); });

   function switchTab(setKey, btn) {
     document.querySelectorAll('.tab-btn').forEach(function(b) { b.classList.remove('active'); b.setAttribute('aria-selected','false'); });
     document.querySelectorAll('.tab-panel').forEach(function(p) { p.classList.remove('active'); });
     btn.classList.add('active');
     btn.setAttribute('aria-selected','true');
     document.getElementById('panel-' + setKey).classList.add('active');
     currentSet = setKey;
   }

   function openLightbox(setKey, index) {
     currentSet = setKey;
     currentIndex = index;
     renderLightbox();
     document.getElementById('lightbox').classList.add('open');
     document.body.style.overflow = 'hidden';
   }

   function renderLightbox() {
     var set = SLIDE_SETS[currentSet];
     var filename = 'slide_' + padNum(currentIndex + 1) + '.png';
     var src = set.base + filename;
     var label = currentIndex === 0 ? 'Title slide' : 'Slide ' + currentIndex;
     document.getElementById('lb-img').src = src;
     document.getElementById('lb-img').alt = label;
     document.getElementById('lb-filename').textContent = set.label + ' \u00B7 ' + label;
     document.getElementById('lb-counter').textContent = (currentIndex + 1) + ' / ' + set.count;
     document.getElementById('lb-prev').disabled = (currentIndex === 0);
     document.getElementById('lb-next').disabled = (currentIndex === set.count - 1);
   }

   function closeLightbox() {
     document.getElementById('lightbox').classList.remove('open');
     document.body.style.overflow = '';
   }

   function lbNav(dir) {
     var next = currentIndex + dir;
     if (next < 0 || next >= SLIDE_SETS[currentSet].count) return;
     currentIndex = next;
     renderLightbox();
   }

   function lbClickOutside(e) {
     if (e.target === document.getElementById('lightbox')) closeLightbox();
   }

   document.addEventListener('keydown', function(e) {
     var lb = document.getElementById('lightbox');
     if (!lb.classList.contains('open')) return;
     if (e.key === 'Escape' || e.key === 'Esc') { closeLightbox(); return; }
     if (e.key === 'ArrowLeft')  { lbNav(-1); return; }
     if (e.key === 'ArrowRight') { lbNav(1);  return; }
   });
   ```

**Quality Gates:**
- [ ] Every PDF has corresponding PNG files in `website/galleries/images/L{NN}/{variant}/`
- [ ] PNG count matches page count of each PDF
- [ ] Gallery HTML loads all thumbnails without 404s
- [ ] All 5 variant tabs present in each gallery page (mini5, mini10, core, extended, full)
- [ ] Lightbox navigation works for all variants
- [ ] Keyboard navigation (arrows, escape) functional

**Outputs:**
- PNG slide images in `website/galleries/images/L{NN}/{variant}/`
- `website/galleries/L{NN}.html` for each lecture

---

### STAGE 4: course-creator:lectures

**Purpose:** Convert LaTeX Beamer frames to HTML lecture pages using the 8-section template with inline CSS.

**Inputs:**
- Compiled `.tex` files from Stage 1 (specifically the `full` variant)
- Master content plans (for section mapping)
- Gallery PNGs from Stage 3 (for TikZ replacement)
- Chart PNGs (copied to `website/charts/` during this stage)

**Process:**

1. **Section Mapping** (LaTeX arc role -> HTML section)

   | Full-Lecture Arc Role | HTML Section ID | Tag CSS Class | Left Border CSS Class |
   |----------------------|-----------------|---------------|----------------------|
   | WHY (frames 1-4) | `why` | `tag-why` (bg:`#d4edda`, color:`#155724`) | `border-why` (border-left:`4px solid #2CA02C`) |
   | WHAT (frames 6-9) | `what` | `tag-what` (bg:`#e8e8f5`, color:`#3333B2`) | `border-what` (border-left:`4px solid #3333B2`) |
   | CASE (frames 10-13) | `case` | `tag-case` (bg:`#ffecd2`, color:`#b45309`) | `border-case` (border-left:`4px solid #FF7F0E`) |
   | HOW (frames 14-17) | `how` | `tag-how` (bg:`#e0f0ff`, color:`#0052a3`) | `border-how` (border-left:`4px solid #0066CC`) |
   | RISK (frames 18-20) | `risk` | `tag-risk` (bg:`#f8d7da`, color:`#721c24`) | `border-risk` (border-left:`4px solid #D62728`) |
   | WHERE (frames 21-23) | `where` | `tag-where` (bg:`#d1ecf1`, color:`#0c5460`) | `border-where` (border-left:`4px solid #17a2b8`) |
   | IMPACT (frames 24-25) | `impact` | `tag-impact` (bg:`#fff3cd`, color:`#856404`) | `border-impact` (border-left:`4px solid #F7931A`) |
   | SO WHAT (frames 26-28) | `sowhat` | `tag-sowhat` (bg:`#f0d6ff`, color:`#5b21b6`) | `border-sowhat` (border-left:`4px solid #9b59b6`) |

2. **LaTeX-to-HTML Conversion Rules** (faithful minimal conversion)

   | LaTeX Element | HTML Output |
   |---------------|-------------|
   | `\begin{frame}[t]{Title}` | `<section id="sectionN" class="content-section border-{section}">` + `<h2>Title</h2>` |
   | `\begin{itemize}\compactlist` | `<ul class="compact-list">` |
   | `\item` | `<li>` |
   | `\textbf{text}` | `<strong>text</strong>` |
   | `\textit{text}` | `<em>text</em>` |
   | `\begin{block}{Title}` | `<div class="callout callout-purple"><strong>Title</strong>` |
   | `\begin{exampleblock}{Title}` | `<div class="callout callout-green"><strong>Title</strong>` |
   | `\begin{alertblock}{Title}` | `<div class="callout callout-red"><strong>Title</strong>` |
   | `$$formula$$` or `\[formula\]` | `<div class="formula">$$formula$$</div>` (rendered by KaTeX) |
   | `$inline$` | `\(inline\)` (rendered by KaTeX) |
   | `\includegraphics{path}` | `<div class="chart-wrap"><img src="../charts/L{NN}/{name}.png" alt="...">` |
   | `\bottomnote{text}` | `<p class="bottom-note">text</p>` |
   | `\begin{columns}[T]` | `<div class="two-col">` |
   | `\begin{tabular}` | `<table class="comp-table">` |
   | `\begin{enumerate}` | `<ol>` |
   | `\textcolor{color}{text}` | `<span style="color:{mapped_color}">text</span>` |
   | `\begin{tikzpicture}` | `<div class="chart-wrap"><img src="../galleries/images/L{NN}/full/slide_{frame_num}.png">` |
   | `\section{Name}` / `% === NAME ===` | Section boundary marker (maps to HTML section) |

3. **HTML Lecture Page Template** (complete inline CSS from Blockchain reference)

   Each lecture page includes the COMPLETE CSS from the reference as an inline `<style>` block:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,initial-scale=1.0">
   <title>L{NN}: {title} - {course.name}</title>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
   <style>
   *{box-sizing:border-box;margin:0;padding:0}
   body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;background:#f6f8fa;color:#24292e;font-size:13px;line-height:1.6}
   a{color:#0066CC;text-decoration:none}
   a:hover{text-decoration:underline}

   /* Nav */
   .nav{background:#1a1a4e;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100}
   .nav-title{color:#fff;font-weight:600;font-size:14px}
   .nav-links{display:flex;gap:16px}
   .nav-links a{color:#fff;font-size:11px;opacity:0.8}
   .nav-links a:hover{opacity:1;text-decoration:none}

   /* Layout */
   .wrap{display:flex;max-width:1400px;margin:0 auto}

   /* Sidebar */
   .side{width:200px;background:#fff;border-right:1px solid #e1e4e8;height:calc(100vh - 38px);overflow-y:auto;position:sticky;top:38px;flex-shrink:0;padding:12px 0}
   .side-head{padding:6px 12px;font-size:10px;font-weight:700;color:#586069;text-transform:uppercase;letter-spacing:0.08em}
   .side-nav{list-style:none;margin-bottom:16px}
   .side-nav li a{display:flex;align-items:center;gap:8px;padding:5px 12px;font-size:11px;color:#586069;border-left:3px solid transparent;transition:all 0.1s}
   .side-nav li a:hover{color:#0066CC;background:#f6f8fa;text-decoration:none;border-left-color:#0066CC}
   .side-nav li a.active{color:#0066CC;border-left-color:#0066CC;background:#f0f6ff;font-weight:600}
   .side-badge{font-size:9px;font-weight:700;padding:1px 5px;border-radius:3px;background:#e8e8f5;color:#3333B2}

   /* Main */
   .main{flex:1;min-width:0;padding:16px 20px}
   .back{display:inline-block;margin-bottom:12px;font-size:12px;color:#586069}
   .back:hover{color:#0066CC;text-decoration:none}

   /* Hero */
   .hero{background:linear-gradient(135deg,#3333B2 0%,#0066CC 100%);color:#fff;padding:20px 24px;border-radius:6px;margin-bottom:20px}
   .hero-eyebrow{font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:0.1em;opacity:0.7;margin-bottom:6px}
   .hero h1{font-size:22px;font-weight:700;margin-bottom:4px}
   .hero-sub{font-size:13px;opacity:0.85;margin-bottom:12px}
   .hero-desc{font-size:12px;opacity:0.75;max-width:700px;line-height:1.5}
   .hero-meta{display:flex;gap:20px;margin-top:14px;padding-top:14px;border-top:1px solid rgba(255,255,255,0.2)}
   .hero-meta span{font-size:11px;opacity:0.8}
   .hero-meta strong{font-weight:700}

   /* Content sections */
   .content-section{background:#fff;border:1px solid #e1e4e8;border-radius:6px;padding:18px 20px;margin-bottom:14px;scroll-margin-top:54px}
   .section-label{display:flex;align-items:center;gap:10px;margin-bottom:14px;padding-bottom:10px;border-bottom:2px solid #e1e4e8}
   .section-tag{font-size:10px;font-weight:700;padding:3px 8px;border-radius:3px;text-transform:uppercase;letter-spacing:0.06em}
   .section-label h2{font-size:15px;font-weight:700;color:#24292e}
   .section-label .section-num{font-size:11px;color:#586069;margin-left:auto}

   /* Section tag colors */
   .tag-why{background:#d4edda;color:#155724}
   .tag-what{background:#e8e8f5;color:#3333B2}
   .tag-case{background:#ffecd2;color:#b45309}
   .tag-how{background:#e0f0ff;color:#0052a3}
   .tag-risk{background:#f8d7da;color:#721c24}
   .tag-where{background:#d1ecf1;color:#0c5460}
   .tag-impact{background:#fff3cd;color:#856404}
   .tag-sowhat{background:#f0d6ff;color:#5b21b6}

   /* Section border colors */
   .border-why{border-left:4px solid #2CA02C}
   .border-what{border-left:4px solid #3333B2}
   .border-case{border-left:4px solid #FF7F0E}
   .border-how{border-left:4px solid #0066CC}
   .border-risk{border-left:4px solid #D62728}
   .border-where{border-left:4px solid #17a2b8}
   .border-impact{border-left:4px solid #F7931A}
   .border-sowhat{border-left:4px solid #9b59b6}

   .content-section p{font-size:12px;line-height:1.7;color:#444;margin-bottom:10px}
   .content-section p:last-child{margin-bottom:0}

   /* Callout boxes */
   .callout{border-radius:4px;padding:10px 14px;margin:12px 0;font-size:12px;line-height:1.6}
   .callout-blue{background:#e0f0ff;border-left:3px solid #0066CC;color:#003d80}
   .callout-purple{background:#f0ecff;border-left:3px solid #3333B2;color:#221166}
   .callout-orange{background:#fff3e0;border-left:3px solid #FF7F0E;color:#7a3e00}
   .callout-green{background:#e8f5e9;border-left:3px solid #2CA02C;color:#1a5c1a}
   .callout-red{background:#fde8e8;border-left:3px solid #D62728;color:#7a0000}
   .callout-yellow{background:#fffbe6;border-left:3px solid #F7931A;color:#7a4a00}
   .callout strong{font-weight:700}

   /* Inline charts */
   .chart-wrap{margin:14px 0;text-align:center;background:#f6f8fa;border:1px solid #e1e4e8;border-radius:4px;padding:8px}
   .chart-wrap img{max-width:100%;height:auto;border-radius:3px}
   .chart-caption{font-size:10px;color:#586069;margin-top:6px;font-style:italic}

   /* Two-column layout */
   .two-col{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:12px 0}
   .two-col-text-chart{display:grid;grid-template-columns:1fr 0.9fr;gap:16px;margin:12px 0;align-items:start}

   /* Table */
   .comp-table{width:100%;border-collapse:collapse;font-size:11px;margin:12px 0}
   .comp-table th{background:#1a1a4e;color:#fff;padding:6px 10px;text-align:left;font-weight:600}
   .comp-table td{padding:6px 10px;border-bottom:1px solid #e1e4e8}
   .comp-table tr:hover td{background:#f6f8fa}
   .comp-table td:first-child{font-weight:600;color:#24292e}
   .check{color:#2CA02C;font-weight:700}
   .cross{color:#D62728;font-weight:700}

   /* Download section */
   .downloads{background:#fff;border:1px solid #e1e4e8;border-radius:6px;padding:18px 20px;margin-bottom:14px}
   .downloads h3{font-size:14px;font-weight:700;margin-bottom:14px;color:#24292e}
   .dl-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
   .dl-btn{display:flex;flex-direction:column;align-items:center;padding:10px 12px;border:1px solid #e1e4e8;border-radius:5px;background:#f6f8fa;color:#24292e;font-size:11px;font-weight:500;transition:all 0.15s;text-align:center}
   .dl-btn:hover{border-color:#0066CC;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,0.08);text-decoration:none;color:#0066CC}
   .dl-btn .dl-icon{font-size:20px;margin-bottom:5px}
   .dl-btn .dl-size{font-size:9px;color:#586069;margin-top:3px}

   /* Action links */
   .action-links{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}
   .action-btn{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:4px;font-size:12px;font-weight:600;transition:all 0.15s}
   .action-btn:hover{text-decoration:none;transform:translateY(-1px)}
   .btn-primary{background:#0066CC;color:#fff}
   .btn-primary:hover{background:#0052a3;color:#fff}
   .btn-secondary{background:#3333B2;color:#fff}
   .btn-secondary:hover{background:#2626a0;color:#fff}
   .btn-outline{border:1px solid #0066CC;color:#0066CC;background:#fff}
   .btn-outline:hover{background:#0066CC;color:#fff}

   /* Footer */
   .foot{text-align:center;padding:16px;font-size:10px;color:#586069;margin-top:8px}

   /* Responsive */
   @media(max-width:900px){
     .wrap{flex-direction:column}
     .side{width:100%;height:auto;max-height:none;position:relative;top:0;border-right:none;border-bottom:1px solid #e1e4e8;padding:8px 0}
     .side-nav{display:flex;flex-wrap:wrap;gap:2px;padding:0 8px}
     .side-nav li a{border-left:none;border-bottom:2px solid transparent;padding:4px 8px}
     .two-col,.two-col-text-chart{grid-template-columns:1fr}
     .dl-grid{grid-template-columns:repeat(2,1fr)}
   }
   @media(max-width:600px){
     .hero h1{font-size:17px}
     .hero-meta{flex-wrap:wrap;gap:10px}
   }
   </style>
   </head>
   <body>
   <!-- ... body content ... -->

   <!-- KaTeX auto-render -->
   <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
   <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
     onload="renderMathInElement(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\(',right:'\\)',display:false}]})"></script>

   <!-- Scroll tracking -->
   <script>
   (function(){
     var sections = document.querySelectorAll('.content-section[id]');
     var links = document.querySelectorAll('.side-nav li a');
     function onScroll(){
       var scrollPos = window.scrollY + 80;
       var current = '';
       sections.forEach(function(s){
         if(s.offsetTop <= scrollPos) current = s.id;
       });
       links.forEach(function(a){
         a.classList.remove('active');
         if(a.getAttribute('href') === '#'+current) a.classList.add('active');
       });
     }
     window.addEventListener('scroll', onScroll, {passive:true});
     onScroll();
   })();
   </script>
   </body>
   </html>
   ```

4. **Download section includes all 6 file variants:**
   ```html
   <div class="downloads" id="downloads">
     <h3>Download Slides &amp; Resources</h3>
     <div class="dl-grid">
       <a class="dl-btn" href="../downloads/L{NN}_mini5.pdf" download>
         <span class="dl-icon">&#128196;</span> 5-Slide Teaser
         <span class="dl-size">Executive summary</span>
       </a>
       <a class="dl-btn" href="../downloads/L{NN}_mini10.pdf" download>
         <span class="dl-icon">&#128196;</span> 10-Slide Standalone
         <span class="dl-size">Self-contained overview</span>
       </a>
       <a class="dl-btn" href="../downloads/L{NN}_core.pdf" download>
         <span class="dl-icon">&#128196;</span> Core Slides
         <span class="dl-size">10-slide summary</span>
       </a>
       <a class="dl-btn" href="../downloads/L{NN}_overview.pdf" download>
         <span class="dl-icon">&#128196;</span> Extended Overview
         <span class="dl-size">Accessible overview</span>
       </a>
       <a class="dl-btn" href="../downloads/L{NN}_deepdive.pdf" download>
         <span class="dl-icon">&#128196;</span> Deep Dive
         <span class="dl-size">Mathematical detail</span>
       </a>
       <a class="dl-btn" href="../downloads/L{NN}_full.pdf" download>
         <span class="dl-icon">&#128196;</span> Full Lecture
         <span class="dl-size">Complete lecture deck</span>
       </a>
     </div>
   </div>
   ```

**Quality Gates:**
- [ ] Every lecture in manifest has a corresponding L{NN}.html
- [ ] All 8 sections present in each HTML file (even if some sections are thin)
- [ ] All `<img>` src paths resolve to existing files in `website/`
- [ ] No raw LaTeX commands remaining in HTML output
- [ ] Sidebar navigation links match section IDs
- [ ] Download links point to files that will exist in `website/downloads/`
- [ ] HTML validates (no unclosed tags)
- [ ] KaTeX CDN scripts included for formula rendering
- [ ] Scroll-tracking JavaScript present and functional

**Outputs:**
- `website/lectures/L{NN}.html` for each lecture
- Chart PNGs copied to `website/charts/L{NN}/`

---

### STAGE 5: course-creator:quizzes

**Purpose:** Generate dual-tier HTML quiz pages for every lecture, with inline CSS.

**Inputs:**
- Quiz .tex files from Stage 1 (companion files from full-lecture-generator)
- Manifest quiz configuration

**Process:**

1. **Standard Quiz** (20 MCQ) -- already generated as companion file by full-lecture-generator in Stage 1. Convert to HTML.

2. **Advanced Quiz** (20 MCQ) -- generate separately with higher Bloom's distribution.

3. **HTML Quiz Page** uses inline `<style>` block matching the Blockchain reference quiz CSS:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,initial-scale=1.0">
   <title>Quiz: L{NN} - {title} ({tier}) - {course.name}</title>
   <style>
   *{box-sizing:border-box;margin:0;padding:0}
   body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;background:#f6f8fa;color:#24292e;font-size:13px;line-height:1.5}
   a{color:#0066CC;text-decoration:none}
   .nav{background:#1a1a4e;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100}
   .nav-title{color:#fff;font-weight:600;font-size:14px}
   .nav-links{display:flex;gap:16px}
   .nav-links a{color:#fff;font-size:11px;opacity:0.8}
   .nav-links a:hover{opacity:1}
   .container{max-width:800px;margin:0 auto;padding:16px}
   h1{font-size:18px;margin-bottom:4px}
   .subtitle{font-size:12px;color:#586069;margin-bottom:16px}
   .back{display:inline-block;margin-bottom:12px;font-size:12px}
   .q-block{background:#fff;border:1px solid #e1e4e8;border-radius:6px;padding:14px;margin-bottom:10px}
   .q-num{font-weight:700;font-size:12px;color:#586069;margin-bottom:4px}
   .q-text{font-size:13px;font-weight:600;margin-bottom:8px}
   .q-options label{display:block;padding:4px 0;cursor:pointer;font-size:12px}
   .q-options input{margin-right:6px}
   .q-feedback{margin-top:6px;font-size:11px;padding:6px 8px;border-radius:4px;display:none}
   .q-feedback.correct{display:block;background:#d4edda;color:#155724}
   .q-feedback.incorrect{display:block;background:#f8d7da;color:#721c24}
   .btn{background:#0066CC;color:#fff;border:none;padding:8px 20px;border-radius:4px;cursor:pointer;font-size:12px;margin-top:12px}
   .btn:hover{background:#0052a3}
   .score-box{background:#fff;border:1px solid #e1e4e8;border-radius:6px;padding:14px;margin-top:12px;text-align:center;font-size:14px;font-weight:600;display:none}
   </style>
   </head>
   <!-- body with ANSWERS inline JS object + checkAnswers() function -->
   ```

4. **Quiz answer-checking JavaScript** (inline):
   ```javascript
   var ANSWERS = {
     "1": {"correct": "B", "explanation": "..."},
     // ... 20 questions
   };
   function checkAnswers() {
     var total = Object.keys(ANSWERS).length, correct = 0;
     for (var qid in ANSWERS) {
       var sel = document.querySelector('input[name="q' + qid + '"]:checked');
       var fb = document.getElementById('fb-' + qid);
       if (!sel) { fb.className = 'q-feedback incorrect'; fb.textContent = 'No answer selected.'; continue; }
       if (sel.value === ANSWERS[qid].correct) {
         fb.className = 'q-feedback correct';
         fb.textContent = 'Correct! ' + ANSWERS[qid].explanation;
         correct++;
       } else {
         fb.className = 'q-feedback incorrect';
         fb.textContent = 'Incorrect. ' + ANSWERS[qid].explanation;
       }
     }
     var box = document.getElementById('score-box');
     box.style.display = 'block';
     box.textContent = 'Score: ' + correct + ' / ' + total + ' (' + Math.round(100*correct/total) + '%)';
   }
   ```

**Quality Gates:**
- [ ] Every lecture has both standard and advanced quiz HTML files
- [ ] Each quiz has exactly 20 questions
- [ ] Bloom's distribution matches manifest specification
- [ ] Every answer has an explanation
- [ ] ANSWERS JSON is valid JavaScript
- [ ] checkAnswers() function produces correct scores

**Outputs:**
- `website/quizzes/L{NN}_standard.html` for each lecture
- `website/quizzes/L{NN}_advanced.html` for each lecture

---

### STAGE 6: course-creator:projects

**Purpose:** Generate project track HTML pages from the manifest, with inline CSS.

(Same as original plan, but using inline `<style>` blocks matching the reference pattern. All CSS is embedded per-page.)

**Quality Gates:**
- [ ] Every project in manifest has a corresponding HTML page
- [ ] All lecture links resolve to existing lecture HTML pages
- [ ] Module colors on lecture pills match the manifest
- [ ] Rubric table has rows for each deliverable

**Outputs:**
- `website/projects/{project_id}.html` for each project

---

### STAGE 7: course-creator:deploy

**Purpose:** Copy PDFs to downloads directory, generate the index page, auto-create GitHub repo, and deploy the pre-built static site.

**Critical: NO LaTeX compilation in CI.** All PDFs, PNGs, and HTML are pre-built locally. The GitHub Actions workflow is a simple static site copy.

**Inputs:**
- Complete `website/` directory from Stages 3-6
- All PDF files from lectures
- Manifest repo configuration

**Process:**

1. **Copy PDFs to downloads directory** (locally, before deployment)
   ```bash
   mkdir -p website/downloads
   for lecture_dir in lectures/L*/slides/; do
     cp "$lecture_dir"/*.pdf website/downloads/ 2>/dev/null
   done
   ```

   Expected files per lecture in `website/downloads/`:
   - `L{NN}_mini5.pdf`
   - `L{NN}_mini10.pdf`
   - `L{NN}_core.pdf`
   - `L{NN}_overview.pdf`
   - `L{NN}_deepdive.pdf`
   - `L{NN}_full.pdf`

2. **Copy chart PNGs to website** (if not already done in Stage 4)
   ```bash
   for lecture_dir in lectures/L*; do
     LNN=$(basename "$lecture_dir" | cut -d_ -f1)
     mkdir -p "website/charts/$LNN"
     for fig_dir in "$lecture_dir"/figures/*/; do
       fig_name=$(basename "$fig_dir")
       if [ -f "$fig_dir/chart.pdf" ]; then
         # Convert chart.pdf to .png for web embedding
         pdftoppm -png -r 200 -singlefile "$fig_dir/chart.pdf" "website/charts/$LNN/$fig_name"
       fi
     done
   done
   ```

3. **Index Page Generation** (inline CSS from Blockchain reference)

   Uses the COMPLETE index page CSS from the Blockchain reference:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width,initial-scale=1.0">
   <title>{course.name} - {course.institution}</title>
   <style>
   *{box-sizing:border-box;margin:0;padding:0}
   body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;background:#f6f8fa;color:#24292e;font-size:12px;line-height:1.4}
   a{color:#0066CC;text-decoration:none}
   .nav{background:#1a1a4e;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:100}
   .nav-title{color:#fff;font-weight:600;font-size:14px}
   .nav-links{display:flex;gap:16px}
   .nav-links a{color:#fff;font-size:11px;opacity:0.8}
   .nav-links a:hover{opacity:1}
   .wrap{display:flex;max-width:1800px;margin:0 auto}
   .side{width:180px;background:#ffffff;border-right:1px solid #e1e4e8;height:calc(100vh - 38px);overflow-y:auto;position:sticky;top:38px;flex-shrink:0}
   .side-head{padding:8px 10px;background:#f6f8fa;border-bottom:1px solid #e1e4e8;font-weight:600;font-size:11px}
   .side details{border-bottom:1px solid #f0f0f0}
   .side summary{padding:6px 10px;font-size:10px;font-weight:600;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center}
   .side summary::-webkit-details-marker{display:none}
   .side summary::after{content:"+";color:#586069;font-size:12px}
   .side details[open] summary::after{content:"-"}
   .side ul{list-style:none;padding:0 0 6px 0}
   .side li a{display:block;padding:4px 10px 4px 18px;color:#586069;font-size:10px}
   .side li a:hover{background:#f6f8fa;color:#0066CC}
   .g1 summary{border-left:3px solid #2CA02C}
   .g2 summary{border-left:3px solid #FF7F0E}
   .g3 summary{border-left:3px solid #D62728}
   .g4 summary{border-left:3px solid #3333B2}
   .main{flex:1;min-width:0;padding:10px}
   .hero{background:linear-gradient(135deg,#3333B2 0%,#0066CC 100%);color:#fff;padding:12px 16px;border-radius:6px;margin-bottom:12px;display:flex;align-items:center;justify-content:space-between}
   .hero-left h1{font-size:18px;font-weight:700}
   .hero-left p{font-size:11px;opacity:0.8;margin-top:2px}
   .hero-stats{display:flex;gap:24px}
   .hero-stats span{text-align:center}
   .hero-stats b{display:block;font-size:20px}
   .hero-stats small{font-size:9px;opacity:0.7}
   .section{margin-bottom:16px}
   .section-head{display:flex;align-items:center;gap:8px;margin-bottom:8px;padding:6px 0;border-bottom:2px solid #e1e4e8}
   .section-head span{width:22px;height:22px;border-radius:4px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:11px;font-weight:700}
   .section-head.s1 span{background:#2CA02C}
   .section-head.s2 span{background:#FF7F0E}
   .section-head.s3 span{background:#D62728}
   .section-head.s4 span{background:#3333B2}
   .section-head h2{font-size:13px;color:#24292e}
   .lgrid{display:grid;grid-template-columns:repeat(6,1fr);gap:6px;margin-bottom:12px}
   .lcard{display:block;background:#fff;border:1px solid #e1e4e8;border-radius:4px;padding:8px 10px;cursor:pointer;transition:all 0.15s}
   .lcard:hover{border-color:#0066CC;box-shadow:0 2px 6px rgba(0,0,0,0.1)}
   .lcard-num{font-size:10px;font-weight:700;padding:2px 5px;border-radius:3px;margin-right:6px}
   .s1 .lcard-num{background:#d4edda;color:#2CA02C}
   .s2 .lcard-num{background:#ffecd2;color:#FF7F0E}
   .s3 .lcard-num{background:#f8d7da;color:#D62728}
   .s4 .lcard-num{background:#e8e8f5;color:#3333B2}
   .lcard-title{font-size:11px;font-weight:500;color:#24292e}
   .lesson-section{margin-bottom:16px;background:#fff;border:1px solid #e1e4e8;border-radius:6px;padding:12px}
   .lesson-head{display:flex;align-items:center;gap:8px;margin-bottom:10px}
   .lesson-num{font-size:11px;font-weight:700;padding:4px 8px;border-radius:4px}
   .l1 .lesson-num{background:#d4edda;color:#2CA02C}
   .l2 .lesson-num{background:#ffecd2;color:#FF7F0E}
   .l3 .lesson-num{background:#f8d7da;color:#D62728}
   .l4 .lesson-num{background:#e8e8f5;color:#3333B2}
   .lesson-title{font-size:13px;font-weight:600;color:#24292e}
   .lesson-link{margin-left:auto;font-size:10px;color:#0066CC;padding:4px 8px;border:1px solid #0066CC;border-radius:4px}
   .lesson-link:hover{background:#0066CC;color:#fff}
   .cgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px}
   .ccard{display:block;background:#f6f8fa;border:1px solid #e1e4e8;border-radius:4px;padding:8px;cursor:pointer;transition:all 0.15s;text-align:center;font-size:10px;font-weight:500;color:#24292e}
   .ccard:hover{border-color:#0066CC;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,0.1)}
   .ccard-icon{font-size:16px;margin-bottom:4px}
   .ccard-label{font-size:9px;color:#586069;margin-top:2px}
   .ccard img{width:100%;height:80px;object-fit:contain;background:#fff;border-radius:3px;margin-bottom:4px}
   .ccard-name{font-size:9px;color:#24292e;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;display:block}
   .foot{text-align:center;padding:12px;font-size:10px;color:#586069;margin-top:12px}
   @media(max-width:1400px){.lgrid{grid-template-columns:repeat(4,1fr)}}
   @media(max-width:1000px){.lgrid{grid-template-columns:repeat(3,1fr)}.side{width:160px}}
   @media(max-width:800px){.wrap{flex-direction:column}.side{width:100%;height:auto;max-height:200px;position:relative;top:0}.lgrid{grid-template-columns:repeat(2,1fr)}}
   </style>
   </head>
   <!-- body structure matches Blockchain reference exactly -->
   ```

4. **GitHub Repository Setup**
   ```bash
   # Check if repo exists
   gh repo view {course.repo.org}/{course.repo.name} 2>/dev/null

   # If not, create it
   gh repo create {course.repo.org}/{course.repo.name} \
     --{course.repo.visibility} \
     --description "{course.name} - {course.institution}"

   # Clone and populate
   git clone https://github.com/{course.repo.org}/{course.repo.name}.git
   cp -r website/* {course.repo.name}/
   cp .github/ {course.repo.name}/.github/ -r

   # Initial commit
   cd {course.repo.name}
   git add -A
   git commit -m "Initial course deployment: {course.name}"
   git push origin main

   # Configure GitHub Pages
   gh api repos/{course.repo.org}/{course.repo.name}/pages \
     -f source='{"branch":"main","path":"/"}' --method POST 2>/dev/null || \
   gh api repos/{course.repo.org}/{course.repo.name}/pages \
     -f source='{"branch":"main","path":"/"}' --method PUT
   ```

5. **GitHub Actions Workflow** (simple static deploy -- NO LaTeX compilation)

   ```yaml
   name: Deploy Course to GitHub Pages

   on:
     push:
       branches: [main]
     workflow_dispatch:

   permissions:
     contents: read
     pages: write
     id-token: write

   concurrency:
     group: "pages"
     cancel-in-progress: false

   jobs:
     deploy:
       environment:
         name: github-pages
         url: ${{ steps.deployment.outputs.page_url }}
       runs-on: ubuntu-latest
       steps:
         - name: Checkout
           uses: actions/checkout@v4

         - name: Setup Pages
           uses: actions/configure-pages@v4

         - name: Upload artifact
           uses: actions/upload-pages-artifact@v3
           with:
             path: '.'

         - name: Deploy to GitHub Pages
           id: deployment
           uses: actions/deploy-pages@v4
   ```

**Quality Gates:**
- [ ] All PDFs copied to `website/downloads/` (6 per lecture)
- [ ] GitHub repo exists and is accessible
- [ ] GitHub Actions workflow runs successfully (simple static deploy)
- [ ] Index page renders with all lecture cards and correct module colors
- [ ] All navigation links work (lectures, quizzes, galleries, projects, downloads)
- [ ] Responsive layout works at 1400px, 1000px, 800px breakpoints
- [ ] All download PDFs are accessible from lecture pages
- [ ] Site is live at `https://{org}.github.io/{repo}/`

**Outputs:**
- `website/index.html`
- `website/downloads/` populated with all PDFs
- `website/charts/` populated with chart PNGs
- `.github/workflows/deploy.yml`
- GitHub repository created, configured, and deployed

---

## Orchestrator Logic

### course-creator.md (Parent Orchestrator)

**Triggers:**
- "create course"
- "new course"
- "course creator"
- "build course"
- "course-creator"
- "deploy course"

**The `course-creator:all` mode** is handled directly by the orchestrator, not a separate file. When triggered, it runs all 7 stages in sequence with quality gates between each stage.

**Orchestration Flow:**

```
Input: course.yaml manifest file path

1. VALIDATE manifest (schema check, cross-reference integrity)
   IF errors: Report and stop
   IF warnings: Report and continue

2. STAGE 1: course-creator:slides
   - Generate .tex source files and master content plans
   - Quality gate: all .tex files syntactically valid

3. STAGE 2: course-creator:charts
   - Generate _shared/chart_styles.py
   - Generate chart.py scripts from master content plans
   - Execute all chart.py scripts -> chart.pdf
   - Compile all .tex -> .pdf with pdflatex (locally)
   - Quality gate: all chart.pdf and slide .pdf files exist

4. STAGE 3: course-creator:galleries
   - Convert PDFs to PNGs into website/galleries/images/
   - Generate gallery HTML pages with 5 variant tabs
   - Quality gate: PNG counts match PDF page counts

5. STAGE 4: course-creator:lectures
   - Parse full variant .tex files
   - Convert to HTML with inline CSS using section mapping
   - Copy chart PNGs to website/charts/
   - Quality gate: all L{NN}.html valid, no raw LaTeX

6. STAGE 5: course-creator:quizzes
   - Convert standard quiz .tex to HTML
   - Generate advanced quiz and convert to HTML
   - Quality gate: 2 quiz HTMLs per lecture, 20 questions each

7. STAGE 6: course-creator:projects
   - Generate project HTML pages with auto-rubric
   - Quality gate: all project HTML files valid

8. STAGE 7: course-creator:deploy
   - Copy PDFs to website/downloads/
   - Generate index.html with inline CSS
   - Create/update GitHub repo
   - Push to main branch
   - Verify live deployment
   - Quality gate: site is live and all links work

REPORT: Summary of all stages with counts and status
```

**Running Individual Stages:**
```
course-creator:slides    -- Regenerate all .tex source files
course-creator:charts    -- Regenerate all charts + compile PDFs
course-creator:galleries -- Regenerate gallery PNGs and pages
course-creator:lectures  -- Regenerate HTML lecture pages
course-creator:quizzes   -- Regenerate quiz HTML pages
course-creator:projects  -- Regenerate project pages
course-creator:deploy    -- Copy downloads, regenerate index, redeploy
course-creator:all       -- Run all 7 stages in sequence (mode of orchestrator)
```

**Error Recovery:**
- Each stage writes completion markers to `.omc/state/course-creator-state.json`
- If a run fails mid-way, re-running `course-creator:all` resumes from the failed stage
- Individual stages can be re-run independently to fix specific issues

---

## Commit Strategy

### For the Skill Files (One-Time)
```
Commit 1: "Add course-creator orchestrator and manifest schema"
  - course-creator/course-creator.md

Commit 2: "Add course-creator slide generation sub-skill"
  - course-creator/course-creator-slides.md

Commit 3: "Add course-creator chart generation sub-skill"
  - course-creator/course-creator-charts.md

Commit 4: "Add course-creator gallery sub-skill"
  - course-creator/course-creator-galleries.md

Commit 5: "Add course-creator HTML lecture conversion sub-skill"
  - course-creator/course-creator-lectures.md

Commit 6: "Add course-creator quiz generation sub-skill"
  - course-creator/course-creator-quizzes.md

Commit 7: "Add course-creator project and deploy sub-skills"
  - course-creator/course-creator-projects.md
  - course-creator/course-creator-deploy.md
```

### For Generated Course Content
```
Commit 1: "Add shared preamble and chart styles for {course.short_name}"
  - _shared/preamble.tex, _shared/chart_styles.py

Commit 2: "Add lecture LaTeX sources (L01-L{NN})"
  - lectures/*/slides/*.tex

Commit 3: "Add figure scripts, chart PDFs, and compiled slide PDFs"
  - lectures/*/figures/**, lectures/*/slides/*.pdf

Commit 4: "Add website gallery PNGs and gallery pages"
  - website/galleries/**

Commit 5: "Add HTML lecture pages and chart images"
  - website/lectures/*.html, website/charts/**

Commit 6: "Add quiz pages (standard + advanced)"
  - website/quizzes/*.html

Commit 7: "Add project pages, index page, and downloads"
  - website/projects/*.html, website/index.html, website/downloads/**

Commit 8: "Add GitHub Actions deployment workflow"
  - .github/workflows/deploy.yml
```

---

## Detailed TODOs

### TODO 1: Create course-creator.md orchestrator
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator.md`
**Acceptance Criteria:**
- Contains complete YAML manifest schema documentation
- Contains manifest validation logic (all rules from "Manifest Validation Rules" section)
- Contains chart auto-derivation algorithm
- Contains orchestration flow with 7-stage sequencing (corrected order)
- Contains `course-creator:all` mode logic (not a separate file)
- Contains error recovery logic with state persistence
- Contains triggers, description, and quality metadata
- References all 7 sub-skills by their IDs
- Does NOT duplicate any logic from the lecture-generation triad
- Documents Windows path compatibility requirements

### TODO 2: Create course-creator-slides.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-slides.md`
**Acceptance Criteria:**
- Contains master content plan generation template
- Contains variant derivation logic for all 6 .tex files (mini5, mini10, core, overview, deepdive, full)
- Documents that `section_framework` applies ONLY to overview/deepdive (beamer-slide-creator), NOT to full (full-lecture-generator)
- Contains exact prompt templates for invoking each triad skill (no chart generation in prompts)
- Contains cross-lecture parallelism rules
- Contains frame-index-based core variant extraction algorithm
- Contains quality gates (frame counts, preamble isolation)
- Uses `figures/` directory name throughout

### TODO 3: Create course-creator-charts.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-charts.md`
**Acceptance Criteria:**
- Contains chart_styles.py generation template
- Contains figure naming convention using `figures/` directory
- Contains cartoon generation specification (XKCD-style)
- Contains per-variant chart rules (inline TikZ for mini, external for full/extended)
- Contains chart auto-derivation algorithm (when manifest omits `figures` field)
- Contains compilation commands for batch chart generation + pdflatex compilation
- Contains quality gates (CHART_METADATA, color palette, figsize, seed, PDF compilation)

### TODO 4: Create course-creator-galleries.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-galleries.md`
**Acceptance Criteria:**
- Contains PDF-to-PNG conversion commands placing PNGs in `website/galleries/images/L{NN}/{variant}/`
- Contains gallery HTML page template with 5 variant tabs (mini5, mini10, core, extended, full)
- Contains complete inline CSS matching Blockchain reference gallery page
- Contains complete inline JavaScript (SLIDE_SETS, buildGrid, switchTab, lightbox, keyboard nav)
- Contains quality gates (PNG count matches pages, all thumbnails load)

### TODO 5: Create course-creator-lectures.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-lectures.md`
**Acceptance Criteria:**
- Contains complete LaTeX-to-HTML conversion rules table
- Contains section mapping with CORRECT colors from Blockchain reference (tag-why, tag-what, etc.)
- Contains COMPLETE inline CSS for lecture pages (all rules from reference)
- Contains KaTeX CDN integration via `<script>` tags
- Contains scroll-tracking JavaScript (IntersectionObserver pattern from reference)
- Contains download section with all 6 PDF variants (including core and overview/deepdive)
- Contains quality gates (all sections present, no raw LaTeX, links resolve)
- TikZ pictures replaced by gallery PNG images from Stage 3

### TODO 6: Create course-creator-quizzes.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-quizzes.md`
**Acceptance Criteria:**
- Contains dual-tier specification (standard + advanced Bloom's distributions)
- Contains LaTeX quiz-to-HTML conversion algorithm
- Contains ANSWERS JavaScript object schema
- Contains COMPLETE inline CSS matching Blockchain reference quiz page
- Contains checkAnswers() JavaScript function
- Contains quality gates (20 questions, Bloom's distribution, valid JS)

### TODO 7: Create course-creator-projects.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-projects.md`
**Acceptance Criteria:**
- Contains project HTML page template with inline CSS
- Contains auto-rubric generation logic
- Contains lecture pill linking logic
- Contains quality gates (all links resolve, rubric complete)

### TODO 8: Create course-creator-deploy.md sub-skill
**File:** `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-deploy.md`
**Acceptance Criteria:**
- Contains PDF copy commands for `website/downloads/` (all 6 variants per lecture)
- Contains chart PNG copy commands for `website/charts/`
- Contains COMPLETE inline CSS for index page matching Blockchain reference
- Contains GitHub repo creation commands (gh CLI)
- Contains GitHub Actions workflow YAML (simple static deploy, NO LaTeX in CI)
- Contains gh-pages configuration commands
- Contains quality gates (site live, all links work, responsive)

---

## Success Criteria

| Criterion | Measurement | Pass Threshold |
|-----------|-------------|----------------|
| **Manifest parsing** | Feed 3 different manifests, all parse correctly | 3/3 |
| **Slide generation** | All 6 .tex files per lecture are syntactically valid | 0 errors across all files |
| **PDF compilation** | All 6 .pdf files compile locally | 0 pdflatex errors |
| **Chart generation** | All chart.py scripts produce valid PDFs | 0 failures |
| **HTML fidelity** | Spot-check lecture HTML against source LaTeX | Content matches, no raw LaTeX visible |
| **Quiz functionality** | Load quiz, answer, check score | Score calculation correct |
| **Gallery rendering** | All 5 variant tabs show correct slide counts | PNG counts match |
| **Deployment** | GitHub Actions runs successfully | Site live at expected URL (simple static deploy) |
| **Visual match** | Compare against Blockchain reference | Inline CSS produces identical look |
| **Download completeness** | All 6 PDF variants accessible per lecture | All download links work |
| **Independence** | Run each sub-skill individually | Each produces correct output |
| **Idempotency** | Run course-creator:all twice | Second run identical |

---

## Risk Mitigations

| Risk | Mitigation |
|------|------------|
| LaTeX compilation failures at scale | Invoke `validate_beamer.py --quick` after each .tex generation; compile locally with build-fixer agent |
| PDF-to-PNG tool not available on Windows | Provide both pdftoppm and ImageMagick commands; detect available tool at runtime |
| `gh` CLI not authenticated | Check `gh auth status` before Stage 7; provide clear error message with auth instructions |
| Cross-lecture notation drift | Generate notation table in master content plan; pass to all variant generators |
| Quiz-slide drift | Generate quiz AFTER finalizing slides (enforced by Stage ordering: 1 before 5) |
| Large course (20 lectures x 6 files = 120 PDFs) | Parallel generation within stages; incremental state tracking for resume |
| Windows path separators | Use forward slashes in all generated paths; avoid backslashes in skill templates |
| Gallery PNGs not ready for lecture HTML | Stage ordering ensures galleries (Stage 3) run before lectures (Stage 4) |

---

## Dependencies

| Dependency | Required By | How to Check |
|------------|-------------|--------------|
| `pdflatex` | Stage 2 (compilation) | `pdflatex --version` |
| `python3` + `matplotlib` + `numpy` | Stage 2 (charts) | `python -c "import matplotlib"` |
| `pdftoppm` or `magick` | Stage 3 (galleries) | `pdftoppm -v` or `magick --version` |
| `gh` CLI (authenticated) | Stage 7 (deploy) | `gh auth status` |
| Existing triad skills | Stage 1 | Check files exist at expected paths |
| `beamer_validation` tools | Quality gates | Check `C:/Users/OsterriederJRO/.claude/tools/beamer_validation/` exists |

---

*Plan generated by Prometheus (v2, revised after Critic + Architect review). Implementation via `/oh-my-claudecode:start-work course-creator-skill`.*
