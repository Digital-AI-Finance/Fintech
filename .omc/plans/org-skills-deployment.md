# Work Plan: Organization-Wide Course-Creator Skills Deployment

## 1. Context

### 1.1 Original Request

Add the course-creator skill system (8 pipeline skills + 3 triad skills) to the EXISTING `digital-ai-finance/digital-ai-finance-organization-manager` repository, create an install script for org-wide distribution, expand the GitHub Pages documentation site with detailed pages covering the entire course-creator system, and update the README.

### 1.2 Existing Repository

**Repo:** `digital-ai-finance/digital-ai-finance-organization-manager` (PRIVATE, already exists)
**GitHub Pages:** Live at `https://digital-ai-finance.github.io/digital-ai-finance-organization-manager/`
**Pages source:** `main` branch, `/docs` path, status: built, public: true

Current structure:
```
.github/workflows/
.gitignore
LICENSE
README.md
docs/
  index.html          # Existing docs page (dark-theme, Inter font, sophisticated)
org_manager/
  __init__.py
  analyzers/
  cache.py
  cli.py
  github_client.py
  report_generator.py
  templates/
  tools/
requirements.txt
screenshot.png
screenshot_dark.png
scripts/
  add_claude_gitignore.py
  add_copyright.py
  catalog_charts.py
  check_beamer_compliance.py
  generate_docs.py
  remove_claude_files.py
  search_claude_references.py
setup.py
templates/
  template_beamer_final.tex
tests/
```

### 1.3 Existing Design System (from docs/index.html)

The existing documentation page uses a specific design system that ALL new pages MUST match:
- **Font:** Inter (Google Fonts CDN)
- **Primary accent:** `#3b82f6` (blue)
- **Secondary accent:** `#8b5cf6` (purple)
- **Background:** Dark mode default, CSS custom properties for theme switching
- **Layout:** Sidebar + main content area
- **Components:** Cards with subtle borders, code blocks with syntax highlighting, search, theme toggle (dark/light)
- **Approach:** Pure static HTML/CSS/JS, no build tools

**CRITICAL:** The executor MUST read the actual `docs/index.html` from the cloned repo before writing ANY new page, to extract exact CSS variables, class names, and layout patterns. The new pages must be visually indistinguishable from the existing page.

### 1.4 Skill Files Inventory

**8 course-creator pipeline skills** (in `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/`):

| File | Lines | Role |
|------|-------|------|
| `course-creator.md` | 891 | Parent orchestrator, manifest schema, 7-stage pipeline |
| `course-creator-slides.md` | 278 | Stage 1: LaTeX Beamer .tex generation |
| `course-creator-charts.md` | 180 | Stage 2: Chart scripts + PDF compilation |
| `course-creator-galleries.md` | 491 | Stage 3: PDF-to-PNG gallery pages |
| `course-creator-lectures.md` | 695 | Stage 4: HTML lecture pages |
| `course-creator-quizzes.md` | 329 | Stage 5: Quiz HTML pages |
| `course-creator-projects.md` | 613 | Stage 6: Project track pages |
| `course-creator-deploy.md` | 301 | Stage 7: GitHub Pages deployment |

**3 triad skills** (in `C:/Users/OsterriederJRO/.claude/skills/omc-learned/` -- parent directory, NOT inside course-creator):

| File | Lines | Role |
|------|-------|------|
| `beamer-slide-creator.md` | 1736 | Beamer slide architecture, chart types, section frameworks |
| `full-lecture-generator.md` | 900 | Full ~30-slide lecture generation with 10-role arc |
| `mini-lecture-generator.md` | 583 | 5-slide teaser and 10-slide standalone mini-lectures |

**Total:** 11 skill files, ~6,997 lines

### 1.5 Organization Context

- **Digital-AI-Finance:** 21+ public repos with GitHub Pages (academic courses)
- **Reference site:** `https://digital-ai-finance.github.io/Blockchain/` (12 lectures, 60 PDFs)
- All repos use GitHub Pages for hosting course websites

---

## 2. Work Objectives

### 2.1 Core Objective

Make the course-creator skill system distributable from the org-manager repo so that any contributor across the digital-ai-finance organization can install the skills with a single command and use them immediately in Claude Code.

### 2.2 Deliverables

| # | Deliverable | Description |
|---|-------------|-------------|
| D1 | `skills/` directory in repo | All 11 skill .md files organized in the repo |
| D2 | Install script | `scripts/install_skills.py` that copies skills to `~/.claude/skills/omc-learned/` |
| D3 | Docs: Overview page | `docs/skills/index.html` -- system overview + architecture diagram |
| D4 | Docs: Setup page | `docs/skills/setup.html` -- installation and prerequisites |
| D5 | Docs: Manifest reference | `docs/skills/manifest.html` -- complete YAML manifest spec |
| D6 | Docs: Pipeline page | `docs/skills/pipeline.html` -- all 7 stages explained |
| D7 | Docs: Examples page | `docs/skills/examples.html` -- reference sites + usage examples |
| D8 | Updated docs/index.html | Add "Skills" section/link to existing landing page |
| D9 | Updated README.md | Add skills section with quick-start |

### 2.3 Definition of Done

- All 11 skill files present in `skills/` directory and byte-identical to source
- Install script runs on Windows (Python 3.8+), copies all skills correctly
- All 5 new docs pages render correctly, match existing dark-theme design system exactly
- All internal links work (no 404s)
- Existing docs/index.html updated with navigation to new skills section
- README.md updated with skills overview
- GitHub Pages builds successfully after push

---

## 3. Must Have / Must NOT Have

### Must Have

- All 11 skill files copied verbatim (zero content modification)
- Install script with `--dry-run` flag for safety
- Install script works on Windows with forward-slash paths (pathlib.Path)
- Docs pages use IDENTICAL CSS variables, font (Inter), and layout as existing `docs/index.html`
- Dark mode support on all new pages (matching existing toggle)
- Sidebar navigation on all new pages (matching existing pattern)
- Mobile-responsive layout
- Architecture diagram (CSS/SVG, no external images)
- Manifest field reference table
- Pipeline stage dependency visualization
- Links to Blockchain reference site as working example
- `.nojekyll` in docs/ (if not already present)

### Must NOT Have

- No modification of ANY existing skill file content
- No npm, webpack, or any build tools
- No external CSS frameworks (Bootstrap, Tailwind, etc.)
- No changes to existing `org_manager/` Python package
- No changes to existing `scripts/` files (only ADD new install_skills.py)
- No breaking changes to existing `docs/index.html` (additive only)
- No server-side rendering
- No JavaScript frameworks (React, Vue, etc.)
- No deletion of any existing file

---

## 4. Updated Repository File Structure

After implementation, the repo will have these additions (marked NEW) and modifications (marked MODIFIED):

```
digital-ai-finance-organization-manager/
  .github/workflows/          # (existing, unchanged)
  .gitignore                  # (existing, unchanged)
  LICENSE                     # (existing, unchanged)
  README.md                   # MODIFIED: add skills section at bottom
  docs/
    index.html                # MODIFIED: add skills navigation link + card
    skills/                   # NEW directory
      index.html              # NEW: Skills overview + architecture diagram
      setup.html              # NEW: Installation + prerequisites
      manifest.html           # NEW: YAML manifest reference
      pipeline.html           # NEW: 7-stage pipeline explanation
      examples.html           # NEW: Reference sites + usage examples
  org_manager/                # (existing, entirely unchanged)
  requirements.txt            # (existing, unchanged)
  screenshot.png              # (existing, unchanged)
  screenshot_dark.png         # (existing, unchanged)
  scripts/
    add_claude_gitignore.py   # (existing, unchanged)
    add_copyright.py          # (existing, unchanged)
    catalog_charts.py         # (existing, unchanged)
    check_beamer_compliance.py # (existing, unchanged)
    generate_docs.py          # (existing, unchanged)
    install_skills.py         # NEW: Skill installer script
    remove_claude_files.py    # (existing, unchanged)
    search_claude_references.py # (existing, unchanged)
  setup.py                    # (existing, unchanged)
  skills/                     # NEW directory
    course-creator/
      course-creator.md       # NEW: verbatim copy from source
      course-creator-slides.md
      course-creator-charts.md
      course-creator-galleries.md
      course-creator-lectures.md
      course-creator-quizzes.md
      course-creator-projects.md
      course-creator-deploy.md
    beamer-slide-creator.md   # NEW: verbatim copy from source
    full-lecture-generator.md  # NEW: verbatim copy from source
    mini-lecture-generator.md  # NEW: verbatim copy from source
  templates/                  # (existing, unchanged)
  tests/                      # (existing, unchanged)
```

**Change summary:** 17 new files created (11 skills + 1 install script + 5 docs pages), 2 existing files surgically modified, 0 existing files deleted, 0 existing directories modified.

---

## 5. New/Modified Files Specifications

### 5.1 `skills/` directory (11 files) -- Verbatim Copies

**Action:** Copy verbatim from source locations. No content changes.

| Source Path | Destination in Repo |
|-------------|---------------------|
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator.md` | `skills/course-creator/course-creator.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-slides.md` | `skills/course-creator/course-creator-slides.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-charts.md` | `skills/course-creator/course-creator-charts.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-galleries.md` | `skills/course-creator/course-creator-galleries.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-lectures.md` | `skills/course-creator/course-creator-lectures.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-quizzes.md` | `skills/course-creator/course-creator-quizzes.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-projects.md` | `skills/course-creator/course-creator-projects.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-deploy.md` | `skills/course-creator/course-creator-deploy.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/beamer-slide-creator.md` | `skills/beamer-slide-creator.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/full-lecture-generator.md` | `skills/full-lecture-generator.md` |
| `C:/Users/OsterriederJRO/.claude/skills/omc-learned/mini-lecture-generator.md` | `skills/mini-lecture-generator.md` |

**Acceptance criterion:** Files are byte-identical to source. Verify with SHA-256.

### 5.2 `scripts/install_skills.py` -- New File

**Specification:**
- Python 3.8+ compatible
- Uses `pathlib.Path` exclusively for all path operations
- Detects home directory via `Path.home()` (cross-platform)
- Target: `~/.claude/skills/omc-learned/`
- Creates target directories if they do not exist
- Copies all 11 skill files preserving directory structure:
  - `skills/course-creator/*.md` -> `~/.claude/skills/omc-learned/course-creator/`
  - `skills/*.md` (triad, at top level) -> `~/.claude/skills/omc-learned/`
- CLI flags via `argparse`:
  - `--dry-run`: Show what would be copied without copying
  - `--force`: Overwrite existing files (default: skip if target exists and is byte-identical)
  - `--verbose`: Print each file copy operation
  - `--target DIR`: Override target directory (default: `~/.claude/skills/omc-learned/`)
- Uses `shutil.copy2` to preserve metadata
- Verifies copied files match source via `hashlib.sha256` comparison
- Output: Summary (N copied, N skipped, N errors)
- Exit code 0 on success, 1 on any failure

**Example usage:**
```bash
python scripts/install_skills.py              # Install, skip if identical
python scripts/install_skills.py --dry-run    # Preview only
python scripts/install_skills.py --force      # Overwrite all
python scripts/install_skills.py --verbose    # Detailed output
```

### 5.3 `docs/skills/index.html` -- Overview Page

**PREREQUISITE:** Executor MUST first read `docs/index.html` from the cloned repo to extract exact CSS.

**Content sections:**
1. **Hero banner:** "Course Creator Skills" title, tagline about manifest-driven course generation
2. **What is it:** 2-3 paragraphs explaining the system
3. **Architecture diagram:** Pure CSS/SVG box diagram showing:
   - `course.yaml` manifest at top
   - Arrow to course-creator orchestrator
   - 7 stages in vertical pipeline with arrows
   - Triad skills branching off Stage 1
   - Output: GitHub Pages website at bottom
4. **Skill inventory table:** All 11 skills with name, description, line count
5. **Key features list:** Manifest-driven, 7-stage pipeline, 6 PDF variants, chart auto-derivation, dual-tier quizzes, pure static output, Windows compatible
6. **Quick links:** Cards to Setup, Manifest Reference, Pipeline, Examples

**Design:** Match `docs/index.html` dark theme, Inter font, CSS variables exactly.

### 5.4 `docs/skills/setup.html` -- Setup Page

**Content sections:**
1. Prerequisites table (pdflatex, python3, matplotlib, numpy, pdftoppm/magick, gh CLI)
2. Installation steps (clone repo, run script, verify)
3. Manual installation alternative
4. Verification checklist
5. Updating skills (pull + re-run with `--force`)
6. Troubleshooting (common issues)

### 5.5 `docs/skills/manifest.html` -- Manifest Reference

**Content sections:**
1. Introduction (what the manifest is, where it lives)
2. Complete YAML example (from course-creator.md lines 70-175)
3. Field reference table (all fields -- course identity, modules, lectures, projects, quizzes, theme)
4. Validation rules (5 hard errors, 6 soft warnings)
5. Design tokens (core colors, section tag colors, module group colors)
6. Badge background derivation algorithm
7. Chart auto-derivation algorithm with chart type reference table

### 5.6 `docs/skills/pipeline.html` -- Pipeline Page

**Content sections:**
1. Pipeline overview diagram (CSS/SVG, 7 stages with arrows and dependencies)
2. Per-stage detail sections (7 sections), each with: inputs, process summary, outputs, quality gates, how to run individually
3. Stage dependency table
4. Error recovery (state file format, recovery scenarios, forcing re-runs)
5. Aggregate quality report example
6. Output directory structure (complete tree)

### 5.7 `docs/skills/examples.html` -- Examples Page

**Content sections:**
1. Blockchain reference implementation (link to live site, stats: 12 lectures, 72 PDFs, 144 charts)
2. Quick start (minimal 3-lecture course.yaml, step-by-step commands)
3. Running individual stages (command examples for each)
4. Customization (override chart types, quiz distributions, theme colors)
5. Organization repos using the system

### 5.8 `docs/index.html` -- SURGICAL Modification

**CRITICAL:** Do NOT rewrite the page. Read the current file first, then make minimal additions:
- Add "Skills" entry to the sidebar navigation (matching existing nav item pattern)
- Add a "Course Creator Skills" card in the main content area (matching existing card component)
- Link to `skills/index.html`

### 5.9 `README.md` -- SURGICAL Modification

**CRITICAL:** Do NOT rewrite the file. Read the current file first, then append:
- `## Course Creator Skills` section with: 1-paragraph description, skill table (11 rows), install command, documentation link, Blockchain reference link

---

## 6. GitHub Pages Site Map

```
docs/
  index.html                    # Landing page (MODIFIED: add skills link)
  skills/
    index.html                  # Overview + architecture diagram
    setup.html                  # Installation + prerequisites
    manifest.html               # YAML manifest reference
    pipeline.html               # 7-stage pipeline explanation
    examples.html               # Reference sites + usage examples
```

### Navigation Structure (All skills/*.html pages)

**Top nav bar:** Matching existing docs nav pattern
**Breadcrumb:** Home > Skills > [Current Page]
**Sidebar:** Section-level navigation within current page
**Previous/Next:** Bottom navigation between skills pages

### Inter-Page Link Matrix

| From | To | Link Text |
|------|----|-----------|
| `docs/index.html` | `docs/skills/index.html` | "Course Creator Skills" |
| `docs/skills/index.html` | `docs/skills/setup.html` | "Get Started" |
| `docs/skills/index.html` | `docs/skills/manifest.html` | "Manifest Reference" |
| `docs/skills/index.html` | `docs/skills/pipeline.html` | "Pipeline Stages" |
| `docs/skills/index.html` | `docs/skills/examples.html` | "Examples" |
| `docs/skills/setup.html` | `docs/skills/manifest.html` | "Next: Manifest Reference" |
| `docs/skills/manifest.html` | `docs/skills/pipeline.html` | "Next: Pipeline" |
| `docs/skills/pipeline.html` | `docs/skills/examples.html` | "Next: Examples" |
| `docs/skills/examples.html` | External | Blockchain reference site |
| All skills pages | `docs/index.html` | "Home" |
| All skills pages | `docs/skills/index.html` | "Skills" breadcrumb |

---

## 7. Install Script Detailed Specification

### `scripts/install_skills.py`

```
Purpose: Copy course-creator skills from repo to user's Claude Code skills directory.

Input: skills/ directory relative to script location (auto-detected via __file__)
Output: Files in ~/.claude/skills/omc-learned/

Arguments:
  --dry-run     Show what would be copied without copying
  --force       Overwrite even if target exists and differs
  --verbose     Print detailed per-file output
  --target DIR  Override target directory (default: ~/.claude/skills/omc-learned/)

Flow:
  1. Determine repo root = Path(__file__).resolve().parent.parent
  2. Determine source = repo_root / "skills"
  3. Determine target = Path.home() / ".claude" / "skills" / "omc-learned"
  4. Scan source for all .md files recursively
  5. For each .md file:
     a. Compute relative path from skills/ root
     b. Compute target path = target / relative_path
     c. If --dry-run: print "Would copy {src} -> {dst}", continue
     d. Create target parent directory if needed (mkdir -p)
     e. If target exists:
        - Compute SHA-256 of both files
        - If identical: print "Skip (identical): {relative_path}", continue
        - If differs and not --force: print "Skip (exists, differs): {relative_path}", continue
        - If differs and --force: proceed to copy
     f. Copy with shutil.copy2
     g. Verify: recompute SHA-256 of target, compare to source
     h. Print status line
  6. Print summary: "Installed: N copied, N skipped (identical), N skipped (exists), N errors"
  7. Exit 0 if zero errors, 1 otherwise

Error handling:
  - PermissionError: Print warning, count as error, continue
  - Missing source: Print error, count as error, continue
  - Target dir creation failure: Print error, exit 1
```

File mapping (repo -> user home):
```
skills/course-creator/course-creator.md       -> ~/.claude/skills/omc-learned/course-creator/course-creator.md
skills/course-creator/course-creator-slides.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-slides.md
skills/course-creator/course-creator-charts.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-charts.md
skills/course-creator/course-creator-galleries.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-galleries.md
skills/course-creator/course-creator-lectures.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-lectures.md
skills/course-creator/course-creator-quizzes.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-quizzes.md
skills/course-creator/course-creator-projects.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-projects.md
skills/course-creator/course-creator-deploy.md -> ~/.claude/skills/omc-learned/course-creator/course-creator-deploy.md
skills/beamer-slide-creator.md                 -> ~/.claude/skills/omc-learned/beamer-slide-creator.md
skills/full-lecture-generator.md               -> ~/.claude/skills/omc-learned/full-lecture-generator.md
skills/mini-lecture-generator.md               -> ~/.claude/skills/omc-learned/mini-lecture-generator.md
```

---

## 8. Detailed TODOs

### Phase A: Repository Structure (skill files + install script)

#### TODO-A1: Copy skill files into repo
**Action:** Create `skills/course-creator/` directory in the repo. Copy all 11 skill files verbatim.
**Source paths (absolute):**
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-slides.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-charts.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-galleries.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-lectures.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-quizzes.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-projects.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/course-creator/course-creator-deploy.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/beamer-slide-creator.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/full-lecture-generator.md`
- `C:/Users/OsterriederJRO/.claude/skills/omc-learned/mini-lecture-generator.md`
**Destination:** `skills/` directory in the cloned repo, preserving subdirectory structure
**Acceptance:**
- [ ] 11 .md files present in `skills/` (8 in `skills/course-creator/`, 3 at `skills/` root)
- [ ] Files are byte-identical to source (verify with diff or SHA-256)

#### TODO-A2: Create `scripts/install_skills.py`
**Action:** Implement per specification in Section 7.
**Requirements:**
- `pathlib.Path` for all paths
- `argparse` for CLI
- `hashlib.sha256` for comparison
- `shutil.copy2` for copying
- Flags: `--dry-run`, `--force`, `--verbose`, `--target`
- Print summary at end
- Exit code 0/1
**Acceptance:**
- [ ] Script runs on Windows Python 3.8+ without errors
- [ ] `--dry-run` lists all 11 files without copying
- [ ] Default run copies all 11 files to correct locations
- [ ] Re-run skips all 11 as identical
- [ ] `--force` re-run overwrites all 11

### Phase B: Documentation Pages

**CRITICAL DESIGN CONSTRAINT:** Every executor working on docs pages MUST first read the existing `docs/index.html` from the cloned repo. Extract exact CSS custom properties, class names, component patterns, Inter font loading, and dark mode mechanism. ALL new pages must use this identical design system. Do NOT use a different CSS approach.

**CSS STRATEGY:** Create a shared `docs/skills/styles.css` file extracted from the existing `docs/index.html` CSS. All 5 new pages link to this one shared stylesheet. This prevents CSS drift between pages built by parallel executors.

#### TODO-B1: Create `docs/skills/index.html` (Overview)
**Action:** Create the skills overview page.
**Prerequisite:** Read `docs/index.html` to extract design system.
**Content:** Hero, "What is it" section, CSS/SVG architecture diagram, skill inventory table, key features, quick-link cards
**Acceptance:**
- [ ] Page renders with identical visual style to `docs/index.html`
- [ ] Architecture diagram is pure CSS/SVG (no external images)
- [ ] Skill inventory table lists all 11 skills
- [ ] All 4 quick-link cards work
- [ ] Dark mode toggle works
- [ ] Mobile responsive

#### TODO-B2: Create `docs/skills/setup.html` (Installation)
**Action:** Create the setup/installation page.
**Prerequisite:** Read `docs/index.html` to extract design system.
**Content:** Prerequisites table, 3-step installation, manual alternative, verification, updating, troubleshooting
**Acceptance:**
- [ ] Prerequisites table lists all dependencies with check/install commands
- [ ] Code blocks with copy-ready commands
- [ ] Dark mode works, style matches index

#### TODO-B3: Create `docs/skills/manifest.html` (Manifest Reference)
**Action:** Create the manifest reference page.
**Prerequisite:** Read `docs/index.html` to extract design system.
**Content:** Introduction, complete YAML example, field reference table (all fields), validation rules (5 hard + 6 soft), design tokens, chart auto-derivation
**Acceptance:**
- [ ] Complete YAML example rendered with syntax highlighting
- [ ] Field reference table has every field from Section 1.4 spec (30+ fields)
- [ ] Validation rules: 5 hard errors, 6 soft warnings, all listed
- [ ] Chart type reference table: 10 types
- [ ] Dark mode works

#### TODO-B4: Create `docs/skills/pipeline.html` (Pipeline)
**Action:** Create the pipeline documentation page.
**Prerequisite:** Read `docs/index.html` to extract design system.
**Content:** Pipeline diagram, 7 stage detail sections, dependency table, error recovery, quality report example, output directory tree
**Acceptance:**
- [ ] CSS/SVG pipeline diagram shows all 7 stages with arrows
- [ ] Each stage has: inputs, process, outputs, quality gates
- [ ] Dependency table is accurate
- [ ] State file JSON example included
- [ ] Output directory tree complete

#### TODO-B5: Create `docs/skills/examples.html` (Examples)
**Action:** Create the examples page.
**Prerequisite:** Read `docs/index.html` to extract design system.
**Content:** Blockchain reference (link + stats), quick start manifest, step-by-step commands, individual stage commands, customization guide
**Acceptance:**
- [ ] Blockchain link: `https://digital-ai-finance.github.io/Blockchain/`
- [ ] Minimal course.yaml is valid YAML
- [ ] All commands are correct
- [ ] Dark mode works

#### TODO-B6: Modify `docs/index.html` (Add skills navigation)
**Action:** Surgically add skills content to existing page.
**Prerequisite:** Read the CURRENT `docs/index.html` content first.
**Changes (additive ONLY):**
- Add "Skills" entry to sidebar navigation (match existing nav pattern exactly)
- Add "Course Creator Skills" card in main content (match existing card pattern)
- Link card to `skills/index.html`
**CONSTRAINT:** Do NOT rewrite the page. Identify exact insertion points. Change only what is needed.
**Acceptance:**
- [ ] Existing content byte-for-byte unchanged except for insertions
- [ ] New "Skills" nav entry visible in sidebar
- [ ] New card links to `skills/index.html`
- [ ] Page still renders correctly

### Phase C: README Update

#### TODO-C1: Update README.md
**Action:** Surgically append skills section to existing README.
**Prerequisite:** Read the CURRENT `README.md` content first.
**Changes (additive ONLY):**
- Append `## Course Creator Skills` section with: description paragraph, skill table (11 rows: name, purpose, stage), install command, documentation link, Blockchain reference link
**CONSTRAINT:** Do NOT rewrite existing content.
**Acceptance:**
- [ ] Existing README content preserved exactly
- [ ] New section renders correctly on GitHub
- [ ] Documentation link points to GH Pages skills overview

### Phase D: Verification

#### TODO-D1: Verify all links work
**Action:** Check every inter-page link across all docs pages.
**Checks:**
- All 5 skills pages link to each other correctly
- `docs/index.html` links to `skills/index.html`
- External link to Blockchain reference site
- README links to GH Pages
**Acceptance:** Zero broken links

#### TODO-D2: Verify GitHub Pages builds
**Action:** Push changes and verify GH Pages deployment.
**Checks:**
- All files are under `docs/` (GH Pages source path)
- Pages site builds without errors
- New pages accessible at expected URLs
**Acceptance:** Site live at `https://digital-ai-finance.github.io/digital-ai-finance-organization-manager/skills/`

#### TODO-D0: Ensure `.nojekyll` exists
**Action:** Create `docs/.nojekyll` if it doesn't already exist in the repo.
**Acceptance:**
- [ ] `docs/.nojekyll` file exists (empty file, prevents Jekyll processing)

#### TODO-D3: Verify install script
**Action:** Test the install script end-to-end.
**Checks:**
- `python scripts/install_skills.py --dry-run` lists all 11 files
- `python scripts/install_skills.py --verbose` copies all 11 files
- Re-run without `--force` skips all as identical
**Acceptance:** All three runs produce expected output

---

## 9. Task Flow and Dependencies

```
Phase A (repo structure)          Phase B (docs)                   Phase C
  |                                 |                                |
  A1 (copy skills) ----+           B1 (overview)   ----+           C1 (README)
  A2 (install script) -+           B2 (setup)      ----+            |
                        |           B3 (manifest)   ----+            |
                        |           B4 (pipeline)   ----+            |
                        |           B5 (examples)   ----+            |
                        |                               |            |
                        +---------- B6 (modify index) --+            |
                                                        |            |
                                    Phase D (verify)    +------------+
                                      |
                                      D1 (link check)
                                      D2 (GH Pages)
                                      D3 (install test)
```

**Parallelizable groups:**
- **Group 1 (all parallel):** A1, A2, B1, B2, B3, B4, B5, C1
  - These are all independent: skill copies, install script, 5 new docs pages, README update
  - NOTE: B1-B5 all share the same prerequisite of reading `docs/index.html` first
- **Group 2 (after B1-B5 complete):** B6
  - Must wait to know the final URL structure of new pages
- **Group 3 (after everything):** D1, D2, D3

**Estimated concurrency:** 5-6 parallel executors for Group 1.

---

## 10. Commit Strategy

| # | Contents | Message |
|---|----------|---------|
| 1 | All 11 skill files in `skills/` | "Add 11 course-creator skill files for org-wide distribution" |
| 2 | `scripts/install_skills.py` | "Add install_skills.py for automated skill installation" |
| 3 | 5 new docs pages in `docs/skills/` | "Add course-creator documentation site (5 pages)" |
| 4 | Modified `docs/index.html` + `README.md` | "Add skills navigation to docs landing page and README" |

---

## 11. Success Criteria

| # | Criterion | Verification Method |
|---|-----------|---------------------|
| S1 | 11 skill files in `skills/` | `find skills/ -name "*.md" \| wc -l` returns 11 |
| S2 | Install script works | `python scripts/install_skills.py --dry-run` lists 11 files |
| S3 | 5 docs pages match existing design | Visual comparison in browser; dark mode toggle works |
| S4 | Zero broken internal links | Crawl all href attributes, verify no 404s |
| S5 | `docs/index.html` has skills navigation | "Skills" link visible in sidebar |
| S6 | `README.md` has skills section | Section visible on GitHub |
| S7 | GH Pages builds | Pages status shows "built" |
| S8 | Existing functionality unchanged | No changes to `org_manager/`, `tests/`, existing `scripts/` |

---

## 12. Risk Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| CSS mismatch between new and existing docs pages | Pages look inconsistent, unprofessional | MANDATORY: read existing `docs/index.html` FIRST, extract exact CSS. All executors building docs MUST start by reading this file. |
| Install script path issues on Windows | Script fails for users | Use `pathlib.Path` exclusively. Test with both forward and back slashes. Use `Path.home()` not `os.environ`. |
| GH Pages 404 on new pages | Documentation inaccessible | All pages under `docs/` (configured GH Pages source). Use relative links only. |
| Skill files modified during copy | Skills behave differently | SHA-256 verification in install script. Byte-identical copies in repo. |
| Existing `docs/index.html` has unexpected structure | B6 modification fails | B6 MUST read the actual file first, identify exact insertion points, use Edit tool for surgical changes. |
| Dark mode CSS vars differ between pages | Visual glitch in theme toggle | Extract CSS custom properties from existing page; reuse identically in all new pages. |
| GH Pages caches stale version | Users see old content | Include cache-busting meta tags where possible. Document "hard refresh" in troubleshooting. |
| Triad skill file locations differ from expected | Install script puts files in wrong place | Triad skills are at `skills/` root (NOT in `skills/course-creator/`), mapping to `~/.claude/skills/omc-learned/` root. Verify file listing before/after. |
