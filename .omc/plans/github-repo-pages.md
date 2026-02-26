# Plan: GitHub Repository with GitHub Pages for Fintech Course

**Plan ID:** github-repo-pages
**Created:** 2026-02-26
**Status:** READY

---

## Context

### Original Request
Set up a full GitHub repository named "Fintech" under the `Digital-AI-Finance` organization, with GitHub Pages serving the course website. Follow the established pattern from the Blockchain reference repository.

### Research Findings

**Reference model (Blockchain repo):**
- Default branch: `master`
- Pages source: `master` branch, `/docs` path (NOT GitHub Actions)
- Repo root contains: source files, build scripts, .omc/, AGENTS.md, docs/
- docs/ contains: index.html, charts/, gallery/, lectures/, quiz/, slides/, assets/
- .gitignore excludes: LaTeX aux files, __pycache__, .DS_Store, CLAUDE.md, .claude/
- .gitignore does NOT exclude: .omc/, AGENTS.md (both are committed)
- Visibility: private (but Fintech course.yaml says public)

**Current Fintech project:**
- Location: `D:/Joerg/Research/slides/Fintech/`
- NOT a git repo yet
- Total size: ~30 MB (website ~23 MB, mostly PDFs)
- Website directory: `website/` with index.html, lectures/, galleries/, quizzes/, downloads/, charts/
- Source: 12 .tex files, 25 chart .py files, compiled PDFs in both lectures/ and website/downloads/
- 15 AGENTS.md files throughout hierarchy
- Malformed directory: `website/{lectures,quizzes,galleries` (contains only images/L01/, likely a glob expansion artifact -- empty/negligible)

**GitHub auth:**
- Authenticated as `josterri` via GITHUB_TOKEN
- Full scopes including admin:org, repo, workflow
- Repo `Digital-AI-Finance/Fintech` does NOT yet exist

### Key Decisions Made

1. **Deployment method: Branch-based from /docs** (match Blockchain reference)
   - Rename `website/` to `docs/`
   - Pages source: master branch, /docs path
   - No GitHub Actions needed

2. **Index page: Keep existing editorial-style index.html**
   - Our polished Crimson Pro + Source Sans design stays
   - Matches all other Fintech HTML pages
   - Do NOT apply deploy skill's compact GitHub-style CSS

3. **Repo contents: Full project** (match Blockchain pattern)
   - LaTeX source, Python charts, compiled PDFs, website/docs, course.yaml
   - Include AGENTS.md files (Blockchain does this)
   - Include .omc/ directory (Blockchain does this)

4. **Default branch: master** (match Blockchain reference)

5. **Visibility: public** (per course.yaml)

6. **README.md: Yes, create one** (Blockchain has one; standard practice)

---

## Work Objectives

### Core Objective
Create the `Digital-AI-Finance/Fintech` GitHub repository with the full course project and enable GitHub Pages serving from `docs/`.

### Deliverables
1. `.gitignore` file at project root
2. `website/` renamed to `docs/`
3. Malformed directory `{lectures,quizzes,galleries` removed
4. `README.md` at project root
5. Git repository initialized with `master` as default branch
6. Remote repository created at `Digital-AI-Finance/Fintech` (public)
7. Initial commit pushed
8. GitHub Pages enabled and serving from `master` branch `/docs` path
9. Site verified live at `https://digital-ai-finance.github.io/Fintech/`

### Definition of Done
- `gh repo view Digital-AI-Finance/Fintech` returns valid repo info
- `gh api repos/Digital-AI-Finance/Fintech/pages` returns source: master, /docs
- `curl -s -o /dev/null -w "%{http_code}" https://digital-ai-finance.github.io/Fintech/` returns 200 (may take 1-2 minutes after enabling)
- All project files present in repo (tex, py, pdf, html, yaml, md)
- No LaTeX aux files, no __pycache__, no .claude/ in the repo

---

## Guardrails

### MUST Have
- Match Blockchain repo pattern: master branch, /docs path for Pages
- Keep existing editorial-style index.html unchanged
- Include ALL source files (tex, py, pdf) in repo
- .gitignore must exclude LaTeX build artifacts and Python cache
- Repository must be public (per course.yaml)
- Default branch must be `master` (not `main`)

### MUST NOT
- Do NOT use GitHub Actions for Pages deployment
- Do NOT modify index.html content or styling
- Do NOT modify any .tex, .py, or .pdf files
- Do NOT create a separate gh-pages branch
- Do NOT include .claude/ directory in repo
- Do NOT include CLAUDE.md in repo
- Do NOT delete or modify the malformed directory before verifying its contents are negligible (it contains only images/L01/ which appears empty or near-empty)

---

## Task Flow

```
Task 1 (cleanup)
    |
    v
Task 2 (.gitignore)
    |
    v
Task 3 (rename website/ to docs/)
    |
    v
Task 4 (README.md)
    |
    v
Task 5 (git init + initial commit)
    |
    v
Task 6 (create remote repo)
    |
    v
Task 7 (push to remote)
    |
    v
Task 8 (enable GitHub Pages)
    |
    v
Task 9 (verify)
```

All tasks are sequential -- each depends on the previous.

---

## Detailed Tasks

### Task 1: Clean Up Malformed Directory

**What:** Remove the `{lectures,quizzes,galleries` directory from `website/` (before rename).

**Steps:**
1. Verify contents: `ls -R "D:/Joerg/Research/slides/Fintech/website/{lectures,quizzes,galleries/"`
2. Confirm it contains only `images/L01/` with negligible or no files
3. Remove it: `rm -rf "D:/Joerg/Research/slides/Fintech/website/{lectures,quizzes,galleries"`
4. Verify removal: `ls "D:/Joerg/Research/slides/Fintech/website/"` should no longer show it

**Acceptance criteria:**
- Directory is gone
- No other files were affected

---

### Task 2: Create .gitignore

**What:** Create `.gitignore` at `D:/Joerg/Research/slides/Fintech/.gitignore`

**Content** (matches Blockchain pattern with additions):
```
# LaTeX auxiliary files
*.aux
*.log
*.nav
*.out
*.snm
*.toc
*.vrb
*.synctex.gz
*.fls
*.fdb_latexmk
*.bbl
*.blg
*.idx
*.ilg
*.ind

# Python
__pycache__/
*.pyc
*.pyo

# Claude Code
CLAUDE.md
.claude/

# OS files
.DS_Store
Thumbs.db
desktop.ini

# Windows device names
nul
NUL
```

**Note:** .omc/ and AGENTS.md are NOT excluded (matches Blockchain pattern).

**Acceptance criteria:**
- File exists at `D:/Joerg/Research/slides/Fintech/.gitignore`
- Content matches specification above
- Blockchain pattern is followed (CLAUDE.md excluded, AGENTS.md included, .omc/ included)

---

### Task 3: Rename website/ to docs/

**What:** Rename the website directory so GitHub Pages can serve from /docs.

**Steps:**
1. Verify no existing `docs/` directory: `ls "D:/Joerg/Research/slides/Fintech/docs" 2>/dev/null`
2. Rename: `mv "D:/Joerg/Research/slides/Fintech/website" "D:/Joerg/Research/slides/Fintech/docs"`
3. Verify: `ls "D:/Joerg/Research/slides/Fintech/docs/index.html"` exists
4. Verify all subdirectories moved: charts/, downloads/, galleries/, lectures/, quizzes/ present under docs/

**Acceptance criteria:**
- `D:/Joerg/Research/slides/Fintech/docs/index.html` exists
- `D:/Joerg/Research/slides/Fintech/website/` does NOT exist
- All content intact (charts, downloads, galleries, lectures, quizzes, index.html)

---

### Task 4: Create README.md

**What:** Create a standard README at `D:/Joerg/Research/slides/Fintech/README.md`

**Content:**
```markdown
# Financial Technology (FinTech)

MSc Course -- Spring 2026
University of Zurich, Department of Finance

**Instructor:** Prof. Joerg Osterrieder

## Course Website

[https://digital-ai-finance.github.io/Fintech/](https://digital-ai-finance.github.io/Fintech/)

## Repository Structure

- `lectures/` -- LaTeX source, figures, and compiled PDF slides
- `docs/` -- Course website (served via GitHub Pages)
- `_shared/` -- Shared LaTeX preambles and Python chart styles
- `course.yaml` -- Course configuration
```

**Acceptance criteria:**
- File exists at `D:/Joerg/Research/slides/Fintech/README.md`
- Contains course title, instructor, link to Pages site, structure overview

---

### Task 5: Initialize Git Repository

**What:** Initialize git repo with `master` as default branch.

**Steps:**
1. `cd "D:/Joerg/Research/slides/Fintech" && git init -b master`
2. `git add -A`
3. Review staged files: `git status` -- confirm no .claude/, no CLAUDE.md, no LaTeX aux files
4. `git commit -m "Initial commit: Fintech course project with website"`
5. Verify: `git log --oneline` shows one commit

**Acceptance criteria:**
- Git repo initialized at `D:/Joerg/Research/slides/Fintech/`
- Default branch is `master`
- Initial commit exists
- No excluded files (per .gitignore) in the commit

---

### Task 6: Create Remote Repository

**What:** Create `Digital-AI-Finance/Fintech` on GitHub.

**Command:**
```bash
gh repo create Digital-AI-Finance/Fintech --public --description "Financial Technology (FinTech) - MSc Course, University of Zurich" --source "D:/Joerg/Research/slides/Fintech" --remote origin
```

**Acceptance criteria:**
- `gh repo view Digital-AI-Finance/Fintech` returns valid JSON
- Repo is public
- Remote `origin` is configured in local git

---

### Task 7: Push to Remote

**What:** Push master branch to origin.

**Steps:**
1. `git push -u origin master`
2. Verify: `gh repo view Digital-AI-Finance/Fintech --json defaultBranchRef` shows master

**Acceptance criteria:**
- `git push` succeeds with no errors
- Remote has all files
- `gh api repos/Digital-AI-Finance/Fintech/contents --jq '.[].name'` shows expected directories (docs/, lectures/, _shared/, etc.)

---

### Task 8: Enable GitHub Pages

**What:** Configure GitHub Pages to serve from master branch, /docs path.

**Command:**
```bash
gh api repos/Digital-AI-Finance/Fintech/pages -X POST -f "source[branch]=master" -f "source[path]=/docs"
```

**If Pages already auto-enabled (unlikely), update:**
```bash
gh api repos/Digital-AI-Finance/Fintech/pages -X PUT -f "source[branch]=master" -f "source[path]=/docs"
```

**Acceptance criteria:**
- `gh api repos/Digital-AI-Finance/Fintech/pages --jq '.source'` returns `{"branch":"master","path":"/docs"}`
- No errors from API call

---

### Task 9: Verify Deployment

**What:** Confirm the site is live and serving correctly.

**Steps:**
1. Wait 30 seconds for GitHub Pages build
2. Check Pages status: `gh api repos/Digital-AI-Finance/Fintech/pages --jq '.status'`
3. Attempt to reach the site: `curl -s -o /dev/null -w "%{http_code}" https://digital-ai-finance.github.io/Fintech/`
4. If 404, wait another 60 seconds and retry (Pages can take up to 2 minutes)
5. Verify final URL: `gh api repos/Digital-AI-Finance/Fintech/pages --jq '.html_url'`

**Acceptance criteria:**
- Pages status is "built" (not "errored")
- HTTP response from `https://digital-ai-finance.github.io/Fintech/` is 200
- Page content is the editorial-style Fintech landing page

---

## Commit Strategy

Single initial commit containing the full project:

```
Initial commit: Fintech course project with website

Includes:
- LaTeX lecture sources (L01, L02)
- Python chart generators
- Compiled PDF slides and downloads
- Course website (docs/) with GitHub Pages
- Course configuration (course.yaml)
```

---

## Success Criteria

| Criterion | Verification Command |
|-----------|---------------------|
| Repo exists | `gh repo view Digital-AI-Finance/Fintech --json name` |
| Repo is public | `gh repo view Digital-AI-Finance/Fintech --json visibility` |
| Default branch is master | `gh repo view Digital-AI-Finance/Fintech --json defaultBranchRef` |
| Pages enabled from /docs | `gh api repos/Digital-AI-Finance/Fintech/pages --jq '.source'` |
| Site returns 200 | `curl -s -o /dev/null -w "%{http_code}" https://digital-ai-finance.github.io/Fintech/` |
| No excluded files in repo | `gh api repos/Digital-AI-Finance/Fintech/contents/.claude 2>&1` should 404 |
| docs/index.html exists | `gh api repos/Digital-AI-Finance/Fintech/contents/docs/index.html --jq '.name'` |
| PDFs accessible | `gh api repos/Digital-AI-Finance/Fintech/contents/docs/downloads --jq '.[].name'` shows PDFs |

---

## Risk Notes

- **PDF sizes:** The downloads/ directory has ~4.5 MB of PDFs and lectures/ has more. Total repo ~30 MB. Well within GitHub limits (no LFS needed).
- **Pages build time:** May take 1-2 minutes after enabling. Task 9 includes retry logic.
- **Malformed directory name:** The `{lectures,quizzes,galleries` directory uses shell special characters in its name. Must use proper quoting when removing it.
- **Visibility mismatch:** Blockchain is private, but course.yaml says public for Fintech. We follow course.yaml (public).
- **AGENTS.md files:** 15 AGENTS.md files will be committed (matches Blockchain pattern). These are documentation for AI agents, not sensitive.
