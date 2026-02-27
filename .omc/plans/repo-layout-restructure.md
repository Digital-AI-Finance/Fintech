# Plan: Restructure Fintech Repo Layout to Match Methods-Algorithms Pattern

**Created:** 2026-02-27
**Status:** READY
**Complexity:** HIGH
**Estimated tasks:** 10 sequential phases, ~120 file operations

---

## Context

### Original Request
"Keep all content. But in terms of layout and structure, please follow e.g. the repo Methods-Algorithms."

### Research Findings
The Methods-Algorithms repo uses a flat layout inside each lecture folder: slides (.tex/.pdf) and chart directories sit directly in the lecture folder, with no nested `slides/` or `figures/` subdirectories. The parent directory is named `slides/` (not `lectures/`), lecture folders use Title_Case naming, and the `docs/` tree uses `quiz/` (singular), `docs/slides/pdf/` for downloads, and `docs/slides/images/` for chart PNGs.

### Key Numbers (verified)
- **13 .tex files** (6 for L01, 6 for L02, 1 shared preamble)
- **24 chart/cartoon .py files** (12 per lecture)
- **9 HTML files** in docs/ (1 index, 2 lecture pages, 2 galleries, 4 quizzes)
- **15 AGENTS.md files** across the tree (4 of which become orphaned and must be handled)
- **6 .tex files use `\input{../../../_shared/preamble.tex}`** (L01: full, overview, deepdive; L02: full, overview, deepdive) -- core, mini5, and mini10 are self-contained
- **66 `\includegraphics{figures/...}` references** across 8 .tex files (30 in L01, 36 in L02)
- **24 `sys.path.insert` calls** in chart.py/cartoon.py referencing `_shared` via 3 parent hops

---

## Work Objectives

### Core Objective
Restructure the Fintech repo directory layout to match the Methods-Algorithms flat-structure pattern, preserving all content and updating every internal reference so LaTeX compilation, Python chart generation, and GitHub Pages all continue working.

### Deliverables
1. Renamed top-level directory: `lectures/` becomes `slides/`
2. Renamed lecture folders: Title_Case naming convention
3. Flattened internal structure: no more nested `slides/` and `figures/` subdirs
4. Restructured `docs/` tree to match M-A pattern
5. All internal references updated (.tex, .py, .html, AGENTS.md)
6. GitHub Pages site functional at same URL
7. `_shared/` retained (actively imported, different purpose from M-A `templates/`)
8. Config file renamed: `course.yaml` becomes `config.yaml`

### Definition of Done
- `pdflatex` compiles all .tex files without errors (those that use `\input` and `\includegraphics`)
- All `chart.py` / `cartoon.py` scripts can import from `_shared/chart_styles.py`
- `docs/index.html` loads correctly at `https://digital-ai-finance.github.io/Fintech/`
- All internal links in HTML files resolve correctly
- No broken relative paths anywhere in the repo
- Clean git commit with all changes

---

## Guardrails

### MUST Have
- Every file that exists today must exist after restructuring (zero content loss)
- All LaTeX `\input{}` paths must resolve correctly
- All LaTeX `\includegraphics{}` paths must resolve correctly
- All Python `sys.path.insert` paths must resolve correctly
- All HTML relative `href` and `src` attributes must resolve correctly
- GitHub Pages must continue serving from `docs/`
- `_shared/` directory retained at repo root

### MUST NOT
- Delete any content files
- Change file contents beyond path references
- Change the `docs/index.html` visual design or CSS
- Rename `_shared/` to `templates/` (different purpose in this repo)
- Break any LaTeX compilation
- Break any Python chart generation
- Move files that M-A doesn't have an analog for into nonexistent locations

---

## Target Structure (After Restructuring)

```
D:/Joerg/Research/slides/Fintech/
├── slides/                                           [was: lectures/]
│   ├── L01_Fintech_Foundations/                       [was: L01_fintech_foundations]
│   │   ├── 01_fintech_evolution_timeline/             [was inside figures/]
│   │   │   ├── chart.py
│   │   │   └── chart.pdf
│   │   ├── 02_banking_value_chain_disruption/         [was inside figures/]
│   │   ├── 03_collaboration_models_matrix/
│   │   ├── 04_fintech_ecosystem_overview/
│   │   ├── 05_great_recession_catalyst/
│   │   ├── 06_fintech_investment_growth/
│   │   ├── 07_bank_fintech_partnership_flow/
│   │   ├── 08_embedded_finance_architecture/
│   │   ├── 09_fintech_impact_comparison/
│   │   ├── 10_key_concepts_summary/
│   │   ├── 11_opening_cartoon/
│   │   ├── 12_closing_cartoon/
│   │   ├── L01_full.tex                               [was inside slides/]
│   │   ├── L01_full.pdf
│   │   ├── L01_overview.tex
│   │   ├── L01_overview.pdf
│   │   ├── L01_deepdive.tex
│   │   ├── L01_deepdive.pdf
│   │   ├── L01_core.tex
│   │   ├── L01_core.pdf
│   │   ├── L01_mini10.tex
│   │   ├── L01_mini10.pdf
│   │   ├── L01_mini5.tex
│   │   ├── L01_mini5.pdf
│   │   ├── L01_*.aux, .log, .nav, .out, .snm, .toc   [LaTeX artifacts]
│   │   └── AGENTS.md
│   ├── L02_Fintech_Ecosystem/                         [was: L02_fintech_ecosystem]
│   │   ├── (same flat pattern as L01)
│   │   └── AGENTS.md
│   └── AGENTS.md
├── docs/
│   ├── index.html                                     [updated links]
│   ├── lectures/                                      [KEPT -- Fintech-specific]
│   │   ├── L01.html
│   │   ├── L02.html
│   │   └── AGENTS.md
│   ├── quiz/                                          [was: quizzes/]
│   │   ├── L01_quiz.html
│   │   ├── L01_quiz_advanced.html
│   │   ├── L02_quiz.html
│   │   ├── L02_quiz_advanced.html
│   │   └── AGENTS.md
│   ├── slides/                                        [NEW structure for web assets]
│   │   ├── pdf/                                       [was: downloads/]
│   │   │   ├── L01_full.pdf ... L02_mini5.pdf
│   │   │   └── AGENTS.md
│   │   └── images/                                    [was: charts/]
│   │       ├── L01_Fintech_Foundations/                [was: L01/]
│   │       │   └── *.png
│   │       └── L02_Fintech_Ecosystem/                 [was: L02/]
│   │           └── *.png
│   ├── galleries/                                     [KEPT -- Fintech-specific]
│   │   ├── L01_gallery.html
│   │   ├── L02_gallery.html
│   │   ├── images/L01/...
│   │   ├── images/L02/...
│   │   └── AGENTS.md
│   └── AGENTS.md
├── _shared/                                           [KEPT -- actively imported]
│   ├── preamble.tex
│   ├── chart_styles.py
│   └── AGENTS.md
├── config.yaml                                        [was: course.yaml]
├── README.md
├── AGENTS.md
└── .omc/
```

---

## Task Flow and Dependencies

```
Phase 0 (Backup branch)
    |
    v
Phase 1 (Scaffold)
    |
    v
Phase 2 (Move chart/figure dirs) ──> Phase 3 (Move .tex/.pdf files)
    |                                      |
    v                                      v
Phase 4 (Update LaTeX \input paths)   Phase 5 (Update LaTeX \includegraphics paths)
    |                                      |
    +──────────── both done ───────────────+
                    |
                    v
            Phase 6 (Update Python sys.path)
                    |
                    v
            Phase 7 (Restructure docs/)
                    |
                    v
            Phase 8 (Update HTML references + rename config)
                    |
                    v
            Phase 9 (Update AGENTS.md files + cleanup + verify)
```

---

## Detailed Tasks

### Phase 0: Create Backup Branch (Rollback Safety)

**Goal:** Create a git backup branch so the entire restructuring can be rolled back if anything goes wrong.

**Actions:**
```
git checkout -b backup-pre-restructure
git checkout -          # return to original branch (main or current)
```

**Rollback procedure:** If anything goes wrong at any phase, run:
```
git checkout backup-pre-restructure
git checkout -b main-restored       # or whatever the working branch was
```
This restores the entire repo to its pre-restructuring state.

**Acceptance Criteria:** Branch `backup-pre-restructure` exists pointing at the current HEAD. Working tree is back on the original branch.

---

### Phase 1: Create Target Directory Scaffold

**Goal:** Create the new directory structure without moving any files yet.

**Actions:**
1. Create `slides/` at repo root
2. Create `slides/L01_Fintech_Foundations/`
3. Create `slides/L02_Fintech_Ecosystem/`
4. Create `docs/quiz/`
5. Create `docs/slides/`
6. Create `docs/slides/pdf/`
7. Create `docs/slides/images/`
8. Create `docs/slides/images/L01_Fintech_Foundations/`
9. Create `docs/slides/images/L02_Fintech_Ecosystem/`

**Acceptance Criteria:** All target directories exist. No files moved yet.

---

### Phase 2: Move Chart/Figure Directories (Flatten)

**Goal:** Move all 24 chart/figure subdirectories from `lectures/LXX_*/figures/NN_name/` up into the lecture folder directly.

**Actions for L01 (12 dirs):**
```
mv lectures/L01_fintech_foundations/figures/01_fintech_evolution_timeline/    slides/L01_Fintech_Foundations/01_fintech_evolution_timeline/
mv lectures/L01_fintech_foundations/figures/02_banking_value_chain_disruption/ slides/L01_Fintech_Foundations/02_banking_value_chain_disruption/
mv lectures/L01_fintech_foundations/figures/03_collaboration_models_matrix/   slides/L01_Fintech_Foundations/03_collaboration_models_matrix/
mv lectures/L01_fintech_foundations/figures/04_fintech_ecosystem_overview/    slides/L01_Fintech_Foundations/04_fintech_ecosystem_overview/
mv lectures/L01_fintech_foundations/figures/05_great_recession_catalyst/      slides/L01_Fintech_Foundations/05_great_recession_catalyst/
mv lectures/L01_fintech_foundations/figures/06_fintech_investment_growth/     slides/L01_Fintech_Foundations/06_fintech_investment_growth/
mv lectures/L01_fintech_foundations/figures/07_bank_fintech_partnership_flow/ slides/L01_Fintech_Foundations/07_bank_fintech_partnership_flow/
mv lectures/L01_fintech_foundations/figures/08_embedded_finance_architecture/ slides/L01_Fintech_Foundations/08_embedded_finance_architecture/
mv lectures/L01_fintech_foundations/figures/09_fintech_impact_comparison/     slides/L01_Fintech_Foundations/09_fintech_impact_comparison/
mv lectures/L01_fintech_foundations/figures/10_key_concepts_summary/          slides/L01_Fintech_Foundations/10_key_concepts_summary/
mv lectures/L01_fintech_foundations/figures/11_opening_cartoon/               slides/L01_Fintech_Foundations/11_opening_cartoon/
mv lectures/L01_fintech_foundations/figures/12_closing_cartoon/               slides/L01_Fintech_Foundations/12_closing_cartoon/
```

**Actions for L02 (12 dirs):**
```
mv lectures/L02_fintech_ecosystem/figures/01_fintech_ecosystem_map/          slides/L02_Fintech_Ecosystem/01_fintech_ecosystem_map/
mv lectures/L02_fintech_ecosystem/figures/02_growth_drivers_dashboard/       slides/L02_Fintech_Ecosystem/02_growth_drivers_dashboard/
mv lectures/L02_fintech_ecosystem/figures/03_financial_inclusion_gap/        slides/L02_Fintech_Ecosystem/03_financial_inclusion_gap/
mv lectures/L02_fintech_ecosystem/figures/04_mpesa_adoption_flow/            slides/L02_Fintech_Ecosystem/04_mpesa_adoption_flow/
mv lectures/L02_fintech_ecosystem/figures/05_trust_framework_comparison/     slides/L02_Fintech_Ecosystem/05_trust_framework_comparison/
mv lectures/L02_fintech_ecosystem/figures/06_technology_adoption_lifecycle/   slides/L02_Fintech_Ecosystem/06_technology_adoption_lifecycle/
mv lectures/L02_fintech_ecosystem/figures/07_adoption_barriers_matrix/       slides/L02_Fintech_Ecosystem/07_adoption_barriers_matrix/
mv lectures/L02_fintech_ecosystem/figures/08_nudging_architecture/           slides/L02_Fintech_Ecosystem/08_nudging_architecture/
mv lectures/L02_fintech_ecosystem/figures/09_choice_architecture_examples/   slides/L02_Fintech_Ecosystem/09_choice_architecture_examples/
mv lectures/L02_fintech_ecosystem/figures/10_ecosystem_stakeholder_impact/   slides/L02_Fintech_Ecosystem/10_ecosystem_stakeholder_impact/
mv lectures/L02_fintech_ecosystem/figures/11_opening_cartoon/                slides/L02_Fintech_Ecosystem/11_opening_cartoon/
mv lectures/L02_fintech_ecosystem/figures/12_closing_cartoon/                slides/L02_Fintech_Ecosystem/12_closing_cartoon/
```

**Acceptance Criteria:** All 24 chart/cartoon directories exist directly inside `slides/L01_Fintech_Foundations/` and `slides/L02_Fintech_Ecosystem/`. The old `figures/` directories contain only their AGENTS.md files.

---

### Phase 3: Move Slide .tex/.pdf Files (Flatten)

**Goal:** Move all .tex, .pdf, and LaTeX artifact files from the nested `slides/` subdir up into the lecture folder directly.

**Actions for L01:**
```
mv lectures/L01_fintech_foundations/slides/L01_full.tex        slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_full.pdf        slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_overview.tex    slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_overview.pdf    slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_deepdive.tex    slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_deepdive.pdf    slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_core.tex        slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_core.pdf        slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_mini10.tex      slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_mini10.pdf      slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_mini5.tex       slides/L01_Fintech_Foundations/
mv lectures/L01_fintech_foundations/slides/L01_mini5.pdf       slides/L01_Fintech_Foundations/
```
Also move all `.aux`, `.log`, `.nav`, `.out`, `.snm`, `.toc` artifacts (or optionally delete them since they are regenerated by pdflatex).

**Actions for L02:** Same pattern.

**Acceptance Criteria:** All .tex and .pdf files sit directly in `slides/L01_Fintech_Foundations/` and `slides/L02_Fintech_Ecosystem/`. The old `slides/` subdirs contain only their AGENTS.md files.

---

### Phase 4: Update LaTeX `\input{}` Paths

**Goal:** Fix the shared preamble import path in the 6 .tex files that use it.

**What changes:**
- **Before (3 hops from nested slides/ to root):** `\input{../../../_shared/preamble.tex}`
- **After (2 hops from flat lecture dir to root):** `\input{../../_shared/preamble.tex}`

**Files to update (6 total):**
| File | Old Path | New Path |
|------|----------|----------|
| `slides/L01_Fintech_Foundations/L01_full.tex` | `\input{../../../_shared/preamble.tex}` | `\input{../../_shared/preamble.tex}` |
| `slides/L01_Fintech_Foundations/L01_overview.tex` | same | same |
| `slides/L01_Fintech_Foundations/L01_deepdive.tex` | same | same |
| `slides/L02_Fintech_Ecosystem/L02_full.tex` | same | same |
| `slides/L02_Fintech_Ecosystem/L02_overview.tex` | same | same |
| `slides/L02_Fintech_Ecosystem/L02_deepdive.tex` | same | same |

**Files NOT changed (self-contained, no `\input`):**
- L01_core.tex, L01_mini5.tex, L01_mini10.tex
- L02_core.tex (has explicit comment: "Self-contained (no \input{} commands)"), L02_mini5.tex, L02_mini10.tex

**Acceptance Criteria:** `grep -r '\\input{' slides/` shows only `../../_shared/preamble.tex` paths. No `../../../` remains. Exactly 6 files contain `\input`.

---

### Phase 5: Update LaTeX `\includegraphics{}` Paths

**Goal:** Fix all chart/figure include paths now that figures are siblings (not in a subfolder).

**What changes:**
- **Before (reference into sibling figures/ dir):** `\includegraphics[...]{figures/01_fintech_evolution_timeline/chart.pdf}`
- **After (reference to sibling dir directly):** `\includegraphics[...]{01_fintech_evolution_timeline/chart.pdf}`

**Transformation rule:** Remove the `figures/` prefix from all `\includegraphics` paths.

**Files to update (8 .tex files, 66 total occurrences):**
- `slides/L01_Fintech_Foundations/L01_full.tex` -- 12 occurrences
- `slides/L01_Fintech_Foundations/L01_overview.tex` -- 9 occurrences
- `slides/L01_Fintech_Foundations/L01_deepdive.tex` -- 4 occurrences
- `slides/L01_Fintech_Foundations/L01_core.tex` -- 5 occurrences
- `slides/L02_Fintech_Ecosystem/L02_full.tex` -- 12 occurrences
- `slides/L02_Fintech_Ecosystem/L02_overview.tex` -- 11 occurrences
- `slides/L02_Fintech_Ecosystem/L02_deepdive.tex` -- 7 occurrences
- `slides/L02_Fintech_Ecosystem/L02_core.tex` -- 6 occurrences

**Acceptance Criteria:** `grep -r 'figures/' slides/*.tex` returns zero matches. All `\includegraphics` paths reference directories that exist as siblings in the same folder.

---

### Phase 6: Update Python `sys.path.insert` in chart.py / cartoon.py

**Goal:** Fix the `_shared` import path in all 24 Python chart/cartoon scripts.

**What changes:**
- Old path has 3 `..` hops; new path has 2 `..` hops.
- **Before:** `os.path.join(os.path.dirname(__file__), '..', '..', '..', '_shared')` -- from `lectures/LXX/figures/NN_name/` to repo root
- **After:** `os.path.join(os.path.dirname(__file__), '..', '..', '_shared')` -- from `slides/LXX/NN_name/` to repo root

**Transformation rule:** Change `'..', '..', '..', '_shared'` to `'..', '..', '_shared'` in all 24 files.

**Files to update:** All 20 `chart.py` + 4 `cartoon.py` files.

**Acceptance Criteria:** `grep -r "parents\[4\]\|'\.\.', '\.\.', '\.\.'," slides/` returns zero matches. A test import from any chart.py directory resolves `_shared/chart_styles.py` correctly.

---

### Phase 7: Restructure docs/ Directory

**Goal:** Reorganize docs/ subdirectories to match M-A pattern while keeping Fintech-specific content.

**Actions:**

7a. **Rename `docs/quizzes/` to `docs/quiz/`:**
```
mv docs/quizzes/L01_quiz.html          docs/quiz/L01_quiz.html
mv docs/quizzes/L01_quiz_advanced.html docs/quiz/L01_quiz_advanced.html
mv docs/quizzes/L02_quiz.html          docs/quiz/L02_quiz.html
mv docs/quizzes/L02_quiz_advanced.html docs/quiz/L02_quiz_advanced.html
mv docs/quizzes/AGENTS.md              docs/quiz/AGENTS.md
```

7b. **Move `docs/downloads/` content to `docs/slides/pdf/`:**
```
mv docs/downloads/L01_full.pdf     docs/slides/pdf/L01_full.pdf
mv docs/downloads/L01_overview.pdf docs/slides/pdf/L01_overview.pdf
mv docs/downloads/L01_deepdive.pdf docs/slides/pdf/L01_deepdive.pdf
mv docs/downloads/L01_core.pdf     docs/slides/pdf/L01_core.pdf
mv docs/downloads/L01_mini10.pdf   docs/slides/pdf/L01_mini10.pdf
mv docs/downloads/L01_mini5.pdf    docs/slides/pdf/L01_mini5.pdf
mv docs/downloads/L02_full.pdf     docs/slides/pdf/L02_full.pdf
(... same for all L02 PDFs)
mv docs/downloads/AGENTS.md        docs/slides/pdf/AGENTS.md
```

7c. **Move `docs/charts/` content to `docs/slides/images/`:**
```
mv docs/charts/L01/*.png  docs/slides/images/L01_Fintech_Foundations/
mv docs/charts/L02/*.png  docs/slides/images/L02_Fintech_Ecosystem/
mv docs/charts/AGENTS.md  docs/slides/images/AGENTS.md
```

7d. **Keep `docs/lectures/` and `docs/galleries/` as-is** (Fintech-specific content not present in M-A; relocating them would break functionality without a clear target).

7e. **Remove empty old directories** after all files are moved:
```
rmdir docs/quizzes docs/downloads docs/charts/L01 docs/charts/L02 docs/charts
```

**Acceptance Criteria:** `docs/quiz/`, `docs/slides/pdf/`, `docs/slides/images/L01_Fintech_Foundations/`, `docs/slides/images/L02_Fintech_Ecosystem/` all exist with their files. Old `docs/quizzes/`, `docs/downloads/`, `docs/charts/` directories are gone.

---

### Phase 8: Update All HTML Relative References

**Goal:** Fix every relative link in all 9 HTML files to point to the new locations.

**8a. `docs/index.html` -- Link updates:**

| Old href/src | New href/src | Count |
|--------------|-------------|-------|
| `quizzes/L01_quiz.html` | `quiz/L01_quiz.html` | 1 |
| `quizzes/L01_quiz_advanced.html` | `quiz/L01_quiz_advanced.html` | 1 |
| `quizzes/L02_quiz.html` | `quiz/L02_quiz.html` | 1 |
| `quizzes/L02_quiz_advanced.html` | `quiz/L02_quiz_advanced.html` | 1 |
| `downloads/L01_full.pdf` | `slides/pdf/L01_full.pdf` | 2 |
| `downloads/L01_overview.pdf` | `slides/pdf/L01_overview.pdf` | 1 |
| `downloads/L01_deepdive.pdf` | `slides/pdf/L01_deepdive.pdf` | 1 |
| `downloads/L01_core.pdf` | `slides/pdf/L01_core.pdf` | 1 |
| `downloads/L01_mini10.pdf` | `slides/pdf/L01_mini10.pdf` | 1 |
| `downloads/L01_mini5.pdf` | `slides/pdf/L01_mini5.pdf` | 1 |
| `downloads/L02_*.pdf` | `slides/pdf/L02_*.pdf` | 6 |
| `lectures/L01.html` | `lectures/L01.html` | NO CHANGE |
| `galleries/L01_gallery.html` | `galleries/L01_gallery.html` | NO CHANGE |

**8b. `docs/lectures/L01.html` and `docs/lectures/L02.html` -- Link updates:**

| Old href/src | New href/src |
|--------------|-------------|
| `../quizzes/L01_quiz.html` | `../quiz/L01_quiz.html` |
| `../quizzes/L01_quiz_advanced.html` | `../quiz/L01_quiz_advanced.html` |
| `../downloads/L01_full.pdf` | `../slides/pdf/L01_full.pdf` |
| `../downloads/L01_overview.pdf` | `../slides/pdf/L01_overview.pdf` |
| `../downloads/L01_deepdive.pdf` | `../slides/pdf/L01_deepdive.pdf` |
| `../downloads/L01_core.pdf` | `../slides/pdf/L01_core.pdf` |
| `../downloads/L01_mini10.pdf` | `../slides/pdf/L01_mini10.pdf` |
| `../downloads/L01_mini5.pdf` | `../slides/pdf/L01_mini5.pdf` |
| `../charts/L01/*.png` | `../slides/images/L01_Fintech_Foundations/*.png` |
| `../galleries/L01_gallery.html` | NO CHANGE |

**8c. `docs/galleries/L01_gallery.html` and `L02_gallery.html` -- Link updates:**

| Old href/src | New href/src |
|--------------|-------------|
| `../quizzes/L01_quiz.html` | `../quiz/L01_quiz.html` |
| `../downloads/L01_*.pdf` | `../slides/pdf/L01_*.pdf` |
| `../index.html` | NO CHANGE |
| `../lectures/L01.html` | NO CHANGE |
| `images/L01/...` | NO CHANGE (gallery images stay in galleries/) |

**8d. `docs/quiz/L01_quiz.html` (and all 3 other quiz files) -- Link updates:**

| Old href/src | New href/src |
|--------------|-------------|
| `../index.html` | NO CHANGE |
| `../lectures/L01.html` | NO CHANGE |
| `../galleries/L01_gallery.html` | NO CHANGE |
| `L01_quiz_advanced.html` | NO CHANGE (sibling link, same dir) |
| `L02_quiz.html` | NO CHANGE (sibling link, same dir) |

Note: Quiz files mostly link to sibling quizzes and `../` paths that don't change. But verify each file.

**8e. Rename `course.yaml` to `config.yaml`:**
```
mv course.yaml config.yaml
```
(No HTML files reference this file, but any build scripts or AGENTS.md that mention it need updating.)

**Acceptance Criteria:** Open `docs/index.html` in a browser; every link works. Spot-check `docs/lectures/L01.html` chart images load. No 404s on any relative link.

---

### Phase 9: Update AGENTS.md Files, Handle Orphans, Cleanup, and Verify

**Goal:** Update all AGENTS.md files to reflect the new paths, handle orphaned AGENTS.md files in now-empty directories, remove empty directories, and run verification.

**9a. Handle 4 orphaned AGENTS.md files:**

After Phases 2 and 3, the old `slides/` and `figures/` subdirectories within each lecture contain only their AGENTS.md files. These must be removed before the directories can be deleted:

| Orphaned File | Action |
|---------------|--------|
| `lectures/L01_fintech_foundations/slides/AGENTS.md` | Delete (content is superseded by the lecture-level AGENTS.md) |
| `lectures/L01_fintech_foundations/figures/AGENTS.md` | Delete (content is superseded by the lecture-level AGENTS.md) |
| `lectures/L02_fintech_ecosystem/slides/AGENTS.md` | Delete (content is superseded by the lecture-level AGENTS.md) |
| `lectures/L02_fintech_ecosystem/figures/AGENTS.md` | Delete (content is superseded by the lecture-level AGENTS.md) |

```
rm lectures/L01_fintech_foundations/slides/AGENTS.md
rm lectures/L01_fintech_foundations/figures/AGENTS.md
rm lectures/L02_fintech_ecosystem/slides/AGENTS.md
rm lectures/L02_fintech_ecosystem/figures/AGENTS.md
```

Any relevant content from these 4 files should be merged into the corresponding lecture-level AGENTS.md (`slides/L01_Fintech_Foundations/AGENTS.md` and `slides/L02_Fintech_Ecosystem/AGENTS.md`) during step 9b, before deletion.

**9b. Update remaining AGENTS.md files (11 files):**
Every AGENTS.md that references old paths needs updating. Key changes:
- `lectures/` -> `slides/`
- `L01_fintech_foundations` -> `L01_Fintech_Foundations`
- `L02_fintech_ecosystem` -> `L02_Fintech_Ecosystem`
- `figures/` prefix removed from internal references
- `slides/` subdir references removed
- `docs/quizzes/` -> `docs/quiz/`
- `docs/downloads/` -> `docs/slides/pdf/`
- `docs/charts/` -> `docs/slides/images/`
- `course.yaml` -> `config.yaml`
- Merge any useful content from the 4 deleted AGENTS.md files into the lecture-level ones

**9c. Update README.md** if it contains directory tree or path references.

**9d. Remove empty old directories:**
```
rmdir lectures/L01_fintech_foundations/slides/
rmdir lectures/L01_fintech_foundations/figures/
rmdir lectures/L01_fintech_foundations/exercises/   (already empty)
rmdir lectures/L01_fintech_foundations/quizzes/     (already empty)
rmdir lectures/L01_fintech_foundations/
rmdir lectures/L02_fintech_ecosystem/slides/
rmdir lectures/L02_fintech_ecosystem/figures/
rmdir lectures/L02_fintech_ecosystem/exercises/
rmdir lectures/L02_fintech_ecosystem/quizzes/
rmdir lectures/L02_fintech_ecosystem/
rmdir lectures/
```

All directories should now be truly empty (AGENTS.md files removed in 9a, content files moved in Phases 2-3).

**9e. Verification checklist:**
1. `ls slides/L01_Fintech_Foundations/` shows .tex, .pdf, and chart dirs all flat
2. `ls slides/L02_Fintech_Ecosystem/` shows same pattern
3. `grep -r 'figures/' slides/**/*.tex` returns 0 matches
4. `grep -r '../../../_shared' slides/**/*.tex` returns 0 matches
5. `grep -r "'..', '..', '..'" slides/**/*.py` returns 0 matches
6. `grep -r 'quizzes/' docs/**/*.html` returns 0 matches
7. `grep -r 'downloads/' docs/**/*.html` returns 0 matches
8. `grep -r 'charts/' docs/**/*.html` returns 0 matches (except possibly AGENTS.md)
9. `ls lectures/` fails (directory should not exist)
10. `ls docs/quizzes/` fails (directory should not exist)
11. `ls docs/downloads/` fails (directory should not exist)
12. `ls docs/charts/` fails (directory should not exist)
13. `cat config.yaml` succeeds (renamed from course.yaml)
14. Verify no orphaned AGENTS.md files remain in deleted directories

**Acceptance Criteria:** All 14 verification checks pass. No orphaned empty directories remain. No orphaned AGENTS.md files remain. All remaining AGENTS.md files reflect current structure.

---

## Commit Strategy

**Single commit** after all phases complete and verified:

```
Restructure repo layout to match Methods-Algorithms pattern

- Rename lectures/ to slides/ with Title_Case folder names
- Flatten internal structure: remove nested slides/ and figures/ subdirs
- Restructure docs/: quizzes/ -> quiz/, downloads/ -> slides/pdf/,
  charts/ -> slides/images/
- Rename course.yaml to config.yaml
- Update all LaTeX \input and \includegraphics paths
- Update all Python sys.path imports
- Update all HTML relative links
- Update all AGENTS.md files
- Remove 4 orphaned AGENTS.md files from deleted subdirs

All content preserved. No files deleted (except orphaned AGENTS.md).
```

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Catastrophic failure mid-restructure | Phase 0 backup branch allows full rollback via `git checkout backup-pre-restructure` |
| Missed `\includegraphics` path | Grep verification in Phase 9 catches any remaining `figures/` references |
| Broken GitHub Pages | `docs/` directory name unchanged; only internal links updated |
| LaTeX won't compile after move | Path changes are mechanical (remove one `../` level); verified by grep |
| Python import fails | sys.path depth change is uniform (-1 parent); verified by grep |
| Gallery images break | Gallery `images/` subdir stays inside `docs/galleries/` unchanged |
| HTML link missed | Phase 8 enumerates every `href` and `src` found by grep in each file |
| AGENTS.md has stale paths | Phase 9b systematically updates all 11 remaining AGENTS.md files |
| rmdir fails on non-empty dir | Phase 9a explicitly handles 4 orphaned AGENTS.md files before rmdir |

---

## Success Criteria

1. **Structure matches M-A pattern:** `slides/LXX_Title_Case/` with flat .tex and chart dirs
2. **Zero content loss:** Every .tex, .py, .pdf, .html, .png file from before exists after
3. **Zero broken references:** All `\input`, `\includegraphics`, `sys.path`, and HTML `href`/`src` resolve
4. **GitHub Pages works:** `docs/index.html` serves correctly with all links functional
5. **Clean git history:** Single descriptive commit
6. **Rollback available:** `backup-pre-restructure` branch preserved until verified successful
