# AGENTS.md — PDF Downloads

<!-- Parent: ../../AGENTS.md -->

## Directory Overview

The **slides/pdf/** directory contains compiled PDF files in 6 variants per lecture, ready for download and offline viewing. These PDFs are derived from source materials in the slides directory and mirror the slide variants available in the gallery (mini5, mini10, core, deepdive, overview, full). All PDFs are static files—no processing, no server logic required.

### Purpose

Provide learners with offline-accessible lecture content in multiple granularities, from quick reference (mini5) to comprehensive (full). PDFs enable printing, annotation, and reading on devices without internet access.

### Key Features

- 6 PDF variants per lecture: full, overview, deepdive, core, mini10, mini5
- Static files, no processing required
- Direct download links from course website
- Consistent naming convention for easy identification
- Correspond to slide gallery variants (mini5, mini10, core, extended, full)
- Ready for print and digital annotation

## Files & Structure

### File Naming Convention

```
L{lecture_num}_{variant}.pdf
```

where:
- `{lecture_num}`: 01, 02, 03, ... (zero-padded)
- `{variant}`: full, overview, deepdive, core, mini10, mini5

### L01 PDFs (6 variants)

| Filename | Slides | Use Case | Audience |
|----------|--------|----------|----------|
| `L01_full.pdf` | 31 slides | Complete reference | All learners, archival |
| `L01_overview.pdf` | ~15–18 slides | High-level summary | Busy professionals, executives |
| `L01_deepdive.pdf` | ~22–27 slides | Comprehensive deep dive | Researchers, subject experts |
| `L01_core.pdf` | ~10 slides | Essential concepts only | Time-constrained learners |
| `L01_mini10.pdf` | ~11 slides | Core overview | Quick review before exam |
| `L01_mini5.pdf` | 6 slides | Ultra-quick summary | 5-minute reference |

### L02 PDFs (6 variants)

| Filename | Slides | Use Case | Audience |
|----------|--------|----------|----------|
| `L02_full.pdf` | 31 slides | Complete reference | All learners, archival |
| `L02_overview.pdf` | ~15–18 slides | High-level summary | Busy professionals, executives |
| `L02_deepdive.pdf` | ~22–27 slides | Comprehensive deep dive | Researchers, subject experts |
| `L02_core.pdf` | ~10 slides | Essential concepts only | Time-constrained learners |
| `L02_mini10.pdf` | ~11 slides | Core overview | Quick review before exam |
| `L02_mini5.pdf` | 6 slides | Ultra-quick summary | 5-minute reference |

**Current Status**: L01 and L02 PDFs exist (12 total files). Additional lectures (L03, L04, ...) will follow the same pattern.

## PDF Variant Details

### mini5 (6 slides)

**Purpose**: Executive summary, 5-minute read, highly condensed

**Contents**:
- Title/intro slide
- 4 key concept slides (distilled to most essential points)
- Closing/summary slide

**Use**: Quick reference, meeting prep, email attachment

**Source**: Extracted from full slide deck (typically slides 1, 3, 5, 7, 9, 11 or similar curated selection)

### mini10 (11 slides)

**Purpose**: Overview version, quick study guide, ~10-minute read

**Contents**:
- Title slide
- 8–9 content slides (major concepts, key diagrams)
- Closing/summary slide

**Use**: Class preparation, quick review before quiz, sharing with stakeholders

**Source**: Gallery's mini10 variant (corresponding PNG sequence)

### core (10 slides)

**Purpose**: Core curriculum, essential knowledge, recommended for most learners

**Contents**:
- Title slide
- 8 essential concept slides
- Closing slide

**Use**: Primary study material for core learners, exam prep (if exam covers core material)

**Source**: Gallery's core variant (corresponding PNG sequence)

### overview (~15–18 slides)

**Purpose**: Structured introduction, breadth before depth, professional summary

**Contents**:
- Title/intro slides
- 12–16 slides covering major concepts at medium depth
- Closing/summary

**Use**: Briefing new learners, stakeholder presentations, curriculum mapping

**Source**: Subset of full slide deck (approximately 50% of full)

### deepdive (~22–27 slides)

**Purpose**: Comprehensive exploration, all major content, but not quite complete

**Contents**:
- Title slides
- 20–25 detailed slides with examples, case studies, data
- Closing/references

**Use**: In-depth study, research, expert reference, teaching material

**Source**: Extended variant plus selected slides from full (approximately 80% of full)

### full (31 slides)

**Purpose**: Complete deck, everything included, archival reference

**Contents**:
- Opening slides (title, agenda, intro)
- All content sections with examples and details
- Appendix, references, extended resources
- Closing slides

**Use**: Complete reference, instructor use, publication, detailed research

**Source**: Entire compiled slide deck from source materials

## Relationship to Gallery Variants

The slides/pdf directory PDFs correspond to the gallery image variants:

| Download Variant | Gallery Variant | Relationship |
|------------------|-----------------|--------------|
| mini5 | mini5 | Same slides, PDF instead of HTML+PNG |
| mini10 | mini10 | Same slides, PDF instead of HTML+PNG |
| core | core | Same slides, PDF instead of HTML+PNG |
| overview | (extended + curated) | Similar scope, tailored subset |
| deepdive | extended | Approximately extended variant |
| full | full | Exact same slides as full gallery |

**Note**: Gallery mini5 uses single-digit image naming, but PDF variants use consistent naming (mini5.pdf is always the 6-slide version).

## Compilation & Maintenance

### Source Materials

PDFs are compiled from source materials in:
- `D:/Joerg/Research/slides/Fintech/slides/L01_Fintech_Foundations/` (L01 source)
- `D:/Joerg/Research/slides/Fintech/slides/L02_Fintech_Ecosystem/` (L02 source)

### Compilation Process

**Typical workflow** (not automated, manual update required):

1. **Compile LaTeX variants** from source slide deck via pdflatex
2. **Name files** according to convention (L01_mini5.pdf, L01_mini10.pdf, etc.)
3. **Move to slides/pdf/** directory
4. **Test downloads** (verify file integrity, test open in PDF readers)

**Tools** (if re-compiling):
- pdflatex: Primary tool (LaTeX → PDF)
- PDF Merger (if combining multiple files): pdftk, ghostscript, or online tools

### Version Tracking

**Current**: No formal version tracking. PDFs are static and updated as needed.

**Recommendation**: If versioning becomes important, add date stamp or version number to README or metadata.

### Updating a Variant

1. **Update source slide deck** (if content changes)
2. **Re-compile PDF** from source (pdflatex in slides/L0N_[Slug]/)
3. **Replace file** in slides/pdf/ directory
4. **Test download** (verify file opens, content is correct)
5. **Update AGENTS.md** this file if slide count changes

## Download Integration with Website

### HTML Links

Lectures and other pages link to downloads like:

```html
<a href="slides/pdf/L01_mini5.pdf" download>Download mini5 PDF</a>
<a href="slides/pdf/L01_full.pdf" download>Download Full PDF</a>
```

The `download` attribute prompts browser to download instead of opening in viewer.

### Directory Structure in HTML

From website root, downloads are accessed at:
```
/slides/pdf/L01_full.pdf
/slides/pdf/L02_overview.pdf
etc.
```

### Static Serving

No server-side processing. Files are served as-is by any static HTTP server:
- Apache, Nginx, Node.js http-server, Python SimpleHTTPServer
- GitHub Pages, Netlify, AWS S3 (static site hosting)

## Common Tasks

### Adding a New Lecture's PDFs

1. **Compile 6 PDF variants** from source materials (pdflatex in slides/L03_*/directory)
2. **Name files**: L03_full.pdf, L03_overview.pdf, L03_deepdive.pdf, L03_core.pdf, L03_mini10.pdf, L03_mini5.pdf
3. **Move to slides/pdf/** directory
4. **Test downloads** (click link, verify opens in PDF reader)
5. **Update index.html** or lecture pages to include download links
6. **Update AGENTS.md** (this file) if variant details differ

### Re-compiling an Existing Variant

1. **Update source .tex file** (if content changed)
2. **Run pdflatex** in the lecture directory (twice for overlays)
3. **Save** with exact filename (L01_mini5.pdf, etc.)
4. **Replace file** in slides/pdf/ directory
5. **Verify file integrity** (download and open in PDF reader)

**Checklist**:
- [ ] File name matches convention (L0{N}_{variant}.pdf)
- [ ] File size reasonable (not 0 bytes, not suspiciously large)
- [ ] PDF opens without errors
- [ ] Content matches expected variant (check slide count)
- [ ] Text is readable (no encoding issues)

### Optimizing PDF File Sizes

If PDFs are too large, use:

**GhostScript** (command-line, effective):
```bash
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
  -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf
```

**PDF Compression Tools**:
- Smallpdf.com (online, easy)
- ilovepdf.com (online, free)
- PDF Compressor (desktop tool)

**Target**: Keep individual PDFs under 10 MB for reasonable download times (aim for 2–5 MB if possible).

### Updating Download Links on Website

If variant names or structure changes, update HTML links:

```html
<!-- Old -->
<a href="slides/pdf/L01_mini.pdf" download>Download Mini</a>

<!-- New -->
<a href="slides/pdf/L01_mini5.pdf" download>Download mini5 (6 slides)</a>
```

Ensure href matches actual filename in slides/pdf/ directory.

## Testing Checklist

- [ ] All 12 files present (L01 × 6, L02 × 6)
- [ ] File names follow convention (L0{N}_{variant}.pdf)
- [ ] Files are not empty (size > 100 KB)
- [ ] PDFs open in standard readers (Adobe Reader, browser, Preview)
- [ ] Text is readable (no corruption, proper encoding)
- [ ] Slide counts match variant descriptions (mini5 ≈ 6 slides, full ≈ 31)
- [ ] Download links work from website (no 404 errors)
- [ ] File sizes are reasonable (< 10 MB per file)
- [ ] Metadata is correct (title, author, creation date if relevant)

## AI Agent Instructions

### Content / Publishing

- **Focus**: PDF correctness, variant completeness, content accuracy
- **Key tasks**: Verify slide counts, test PDF opens, check content matches lecture
- **DO**: Compare PDF content to gallery/lecture. Verify slide counts. Test file integrity.
- **AVOID**: Manually creating PDFs—use source slide deck export feature.

### DevOps / Deployment

- **Focus**: File integrity, download speed, CDN optimization
- **Key tasks**: Test downloads, check file sizes, verify HTTP headers
- **DO**: Test download links from website. Monitor file sizes. Check cache headers.
- **AVOID**: Hosting PDFs on third-party services—keep them in slides/pdf/ directory.

### General Maintenance

- **Focus**: File organization, version tracking, update workflows
- **Key tasks**: Organize files, maintain naming convention, document updates
- **DO**: Keep files named consistently. Update AGENTS.md when variants change.
- **AVOID**: Duplicating or versioning files—replace old variants when updating.

## Related Documentation

- **Parent**: `../../AGENTS.md` — Overview of entire website
- **Lectures**: `../../lectures/AGENTS.md` — Lecture content (source material)
- **Galleries**: `../../galleries/AGENTS.md` — Slide galleries (corresponding PNG variants)
- **Charts**: `../images/AGENTS.md` — Chart images (may be embedded in PDFs)
- **Source Materials**: `D:/Joerg/Research/slides/Fintech/slides/` — Original slide decks
