# AGENTS.md — Fintech Course Website

<!-- Parent: ../AGENTS.md -->

## Directory Overview

The **docs/** directory contains a self-contained, no-build-tools course website serving as the public-facing delivery platform for the Financial Technology (FinTech) lecture series. All pages are static HTML with inline CSS and JavaScript—no frameworks, no dependencies. The design system is consistent across all pages: navigation #1a1a4e, hero gradient #0D7377 → #14BDEB, accent #FF7F0E, and fonts Crimson Pro (display) + Source Sans 3 (body).

### Purpose

Host interactive lecture content, slide galleries with lightbox navigation, quizzes with Bloom's taxonomy labeling, and PDF downloads. Designed to be hosted on any static HTTP server without any build steps or external dependencies.

### Key Features

- Self-contained HTML pages with inline CSS/JS (no external dependencies except CDN fonts/KaTeX)
- Responsive design for mobile and desktop viewing
- Design system consistency: color variables, typography hierarchy, spacing scales
- Chart PNG images embedded via `<img>` tags for rapid loading
- Interactive elements: lightbox galleries, MCQ quizzes with instant feedback, progress tracking
- Accessibility: semantic HTML, ARIA labels, keyboard navigation

## Directory Structure

```
docs/
├── index.html                    # Course landing page
├── AGENTS.md                     # This file
├── lectures/
│   ├── AGENTS.md
│   ├── L01.html                 # Lecture 1: Fintech Foundations
│   └── L02.html                 # Lecture 2: Fintech Ecosystem
├── galleries/
│   ├── AGENTS.md
│   ├── L01_gallery.html          # L01 slide gallery with lightbox
│   ├── L02_gallery.html          # L02 slide gallery with lightbox
│   └── images/
│       ├── L01/
│       │   ├── mini5/            # 6 slides (executive summary)
│       │   ├── mini10/           # 11 slides (overview)
│       │   ├── core/             # 10 slides (core concepts)
│       │   ├── extended/         # 27 slides (all content)
│       │   └── full/             # 31 slides (with appendix)
│       └── L02/
│           ├── mini5/
│           ├── mini10/
│           ├── core/
│           ├── extended/
│           └── full/
├── quiz/
│   ├── AGENTS.md
│   ├── L01_quiz.html             # Standard MCQ quiz (20 questions)
│   ├── L01_quiz_advanced.html     # Advanced quiz (20 questions)
│   ├── L02_quiz.html
│   └── L02_quiz_advanced.html
└── slides/
    ├── pdf/
    │   ├── AGENTS.md
    │   ├── L01_full.pdf              # 6 PDF variants per lecture
    │   ├── L01_overview.pdf
    │   ├── L01_deepdive.pdf
    │   ├── L01_core.pdf
    │   ├── L01_mini10.pdf
    │   ├── L01_mini5.pdf
    │   ├── L02_full.pdf
    │   ├── L02_overview.pdf
    │   ├── L02_deepdive.pdf
    │   ├── L02_core.pdf
    │   ├── L02_mini10.pdf
    │   └── L02_mini5.pdf
    └── images/
        ├── AGENTS.md
        ├── L01/                      # 12 chart PNGs per lecture
        │   ├── fintech_evolution_timeline.png
        │   ├── banking_value_chain_disruption.png
        │   ├── fintech_investment_growth.png
        │   ├── key_concepts_summary.png
        │   └── ... (12 total)
        └── L02/
            ├── fintech_ecosystem_map.png
            ├── growth_drivers_dashboard.png
            ├── financial_inclusion_gap.png
            └── ... (12 total)
```

## Key Files

| File | Purpose | Size | Technology |
|------|---------|------|-----------|
| `index.html` | Landing page with lecture cards, navigation, hero section | ~3.5 KB | Semantic HTML + CSS Grid |
| `lectures/L01.html` | L01 content with 8 sections, scroll tracking, KaTeX math | ~2200+ lines | Responsive design, KaTeX CDN |
| `lectures/L02.html` | L02 content with 8 sections, scroll tracking, KaTeX math | ~2200+ lines | Responsive design, KaTeX CDN |
| `galleries/L01_gallery.html` | 5-tab gallery with 31 slides max, lightbox navigation | ~1800 lines | Lazy loading, lightbox JS |
| `galleries/L02_gallery.html` | 5-tab gallery with 31 slides max, lightbox navigation | ~1800 lines | Lazy loading, lightbox JS |
| `quiz/L01_quiz.html` | 20 MCQ questions with Bloom's taxonomy badges | ~1600 lines | Inline JS for instant feedback |
| `quiz/L01_quiz_advanced.html` | 20 advanced MCQ questions with Bloom's badges | ~1600 lines | Inline JS for instant feedback |
| `quiz/L02_quiz.html` | 20 MCQ questions with Bloom's taxonomy badges | ~1600 lines | Inline JS for instant feedback |
| `quiz/L02_quiz_advanced.html` | 20 advanced MCQ questions with Bloom's badges | ~1600 lines | Inline JS for instant feedback |

## Design System

### Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Navigation Background | `#1a1a4e` | Nav bar, dark backgrounds |
| Hero From | `#0D7377` | Gradient start, primary buttons |
| Hero To | `#14BDEB` | Gradient end, highlights |
| Accent | `#FF7F0E` | CTA buttons, important highlights |
| Accent Light | `#FFB347` | Hover state for accents |
| Module Green | `#2CA02C` | Success state, completion indicators |
| Text (ink) | `#1a1d23` | Primary text |
| Text (muted) | `#4a5568` | Secondary text |
| Text (subtle) | `#718096` | Tertiary text |
| Border | `#e2e8f0` | Card borders, dividers |
| Surface | `#ffffff` | Card backgrounds |
| Surface Soft | `#f8fafc` | Light backgrounds |

### Typography

| Role | Font | Sizes |
|------|------|-------|
| Display (headings) | Crimson Pro 600–700 weight | h1: 2.6rem, h2: 1.8rem, h3: 1.3rem |
| Body (paragraphs, UI) | Source Sans 3 400–500 weight | Body: 1rem, Small: 0.85rem |
| Monospace (code) | JetBrains Mono 400–500 weight | Code: 0.9rem |

### Spacing & Layout

| Property | Value |
|----------|-------|
| Max content width | 1120px (index), 860px (lectures) |
| Nav height | 56px (sticky) |
| Sidebar width (responsive) | 240px on desktop, full width on mobile |
| Section padding | 40px top/bottom, 24px left/right |
| Card radius | 10px (standard), 16px (large) |

### Semantic CSS Variables

All CSS variables defined in `:root` scope. See `index.html` or `lectures/L01.html` for full reference. Used throughout for consistency and easy theme updates.

## Subdirectories

### `lectures/`

Self-contained HTML pages (~2200+ lines each) for lecture content delivery. Each lecture page includes:
- Hero section with gradient background
- 8 narrative content sections (e.g., Overview, Key Concepts, Evolution Timeline, etc.)
- 12 inline chart PNG images
- KaTeX math rendering for formulas
- Sticky scroll tracking sidebar with active section highlighting
- Fully responsive design (mobile-first approach)

### `galleries/`

Interactive slide gallery pages with 5 viewing modes (mini5, mini10, core, extended, full) and lightbox navigation. Images are organized by lecture and variant in the `images/` subdirectory. Galleries support lazy loading and keyboard navigation.

### `quiz/`

Interactive MCQ quizzes with 20 questions per page (standard and advanced variants per lecture). Features include:
- Bloom's taxonomy badges (Understand, Apply, Analyze, Evaluate, Create)
- Color-coded difficulty indicators
- Instant feedback on answer submission
- Automatic score calculation
- Progress tracking

### `slides/pdf/`

PDF files compiled from source materials. Each lecture has 6 variants (full, overview, deepdive, core, mini10, mini5) sourced from the slides/ directory in the parent tree.

### `slides/images/`

PNG images converted from chart PDFs in the source tree (slides/L01_Fintech_Foundations/ and slides/L02_Fintech_Ecosystem/). Images are organized by lecture (L01/, L02/) and referenced as `<img src="slides/images/L01/chart-name.png">` in HTML pages.

## Building & Deployment

### No Build Required

All pages are static HTML files. No build step, no transpilation, no bundling.

**To serve locally:**

```bash
# Python 3
cd docs/
python -m http.server 8000

# Node.js http-server
npx http-server -p 8000

# Nginx
server {
  listen 80;
  root /path/to/website;
  try_files $uri $uri/ =404;
}
```

**To deploy:**

Copy the entire `docs/` directory to any static hosting (GitHub Pages, Netlify, AWS S3, traditional HTTP server). No server-side processing required.

### External Dependencies

All external resources use CDN delivery:

| Resource | URL | Reason |
|----------|-----|--------|
| Google Fonts (Crimson Pro, Source Sans 3, JetBrains Mono) | `fonts.googleapis.com` | Typography |
| KaTeX | `cdn.jsdelivr.net/npm/katex` | Math rendering in lectures |

## Common Tasks

### Adding a New Lecture

1. **Create lecture HTML** at `lectures/L03.html` (copy from L01.html or L02.html as template)
2. **Update design system** (color variables, layout) to match existing pages
3. **Add 12 chart PNG images** to `slides/images/L03/`
4. **Create gallery page** at `galleries/L03_gallery.html` with images organized in `galleries/images/L03/`
5. **Create quiz pages** at `quiz/L03_quiz.html` and `L03_quiz_advanced.html`
6. **Compile PDFs** (6 variants) to `slides/pdf/L03_*.pdf`
7. **Update `index.html`** to link to new lecture

### Updating Design Tokens

All color, typography, and spacing values are defined as CSS variables in `:root {}`. Update once to affect all pages:

1. Open `index.html` or `lectures/L01.html`
2. Edit `:root { --variable-name: new-value; }`
3. Changes cascade to all linked pages

### Adding a Quiz Question

Open `quiz/L01_quiz.html` and locate the `ANSWERS` JavaScript object. Add a new entry:

```javascript
ANSWERS = {
  q1: { correct: 'a', bloom: 'Understand', ... },
  q20: { correct: 'd', bloom: 'Evaluate', ... },
  q21: { correct: 'c', bloom: 'Create', ... }  // New question
}
```

Then add corresponding HTML question card in the quiz-container.

### Updating Chart Images

1. Replace the PNG file in `slides/images/L01/` or `slides/images/L02/`
2. No HTML changes needed—image `<src>` paths remain the same
3. Browser cache may show old image; use cache buster if needed

## Subdirectory AGENTS.md Files

See dedicated documentation:

- **`lectures/AGENTS.md`** — Lecture HTML pages structure, content sections, KaTeX integration, responsive design
- **`galleries/AGENTS.md`** — Gallery HTML, lightbox navigation, image organization, lazy loading
- **`quiz/AGENTS.md`** — Quiz HTML, question data structure, Bloom's taxonomy, scoring logic
- **`slides/pdf/AGENTS.md`** — PDF variants, compilation process, version tracking
- **`slides/images/AGENTS.md`** — Image sources, conversion from PDFs, organization by lecture

## AI Agent Instructions

### Designer / Frontend Developer

- **Scope**: Visual consistency, responsive design, accessibility
- **Key files**: `index.html`, `lectures/L01.html`, `galleries/L01_gallery.html`
- **Focus**: CSS Grid/Flexbox layouts, color contrast, mobile-first design, semantic HTML
- **DO**: Match existing color palette and typography. Test on mobile (375px), tablet (768px), desktop (1120px+)
- **AVOID**: External UI frameworks (Bootstrap, Tailwind)—inline CSS only. Inline all CSS, no separate stylesheets.

### Content / QA

- **Scope**: Quiz questions, lecture content accuracy, chart labeling
- **Key files**: `quiz/L01_quiz.html`, `lectures/L01.html`, `slides/images/L01/`
- **Focus**: Bloom's taxonomy accuracy, question clarity, math rendering (KaTeX), image alt text
- **DO**: Verify quiz answers against lecture content. Test KaTeX rendering on both desktop and mobile.
- **AVOID**: Changing page structure or CSS—keep content updates isolated to HTML body content.

### DevOps / Hosting

- **Scope**: Deployment, static site serving, CDN optimization
- **Key files**: All `.html` files, external CDN references
- **Focus**: HTTP caching headers, gzip compression, image optimization, CDN performance
- **DO**: Test local serving with Python/Node.js. Verify all external CDN resources load. Check cache headers.
- **AVOID**: Server-side processing—this is a static site. No database, no backends.

### Full-Stack / General Maintenance

- **Scope**: Cross-cutting updates (e.g., rebranding, nav structure changes)
- **Key files**: All `.html` files, design system variables
- **Focus**: CSS variable consistency, internal link validation, accessibility compliance
- **DO**: Edit `:root` CSS variables once to update theme globally. Verify all lecture links work.
- **AVOID**: Copy-pasting changes across files—use batch edits or template inheritance mindset.

## Testing Checklist

- [ ] All internal links resolve (lectures/, galleries/, quiz/, slides/pdf/)
- [ ] Chart images load (no 404s) for all lectures
- [ ] KaTeX math renders correctly in lectures (open browser console for errors)
- [ ] Quiz instant feedback works (answer selection, checkAnswers() runs)
- [ ] Lightbox navigation works in galleries (arrow keys, click next/prev)
- [ ] Mobile responsive design: test at 375px, 768px, 1120px+
- [ ] Color contrast meets WCAG AA standards (use WebAIM tool)
- [ ] All external CDN resources (fonts, KaTeX) load without errors
- [ ] PDF downloads available and correct (6 variants per lecture)

## Related Documentation

- **Source tree**: `D:/Joerg/Research/slides/Fintech/slides/` (contains L01_Fintech_Foundations/ and L02_Fintech_Ecosystem/ folders with source materials)
- **Parent AGENTS.md**: `D:/Joerg/Research/slides/Fintech/AGENTS.md`
- **Course metadata**: See `index.html` `<title>` and `<meta>` tags for SEO and course info
