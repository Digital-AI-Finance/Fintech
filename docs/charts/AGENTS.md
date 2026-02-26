# AGENTS.md — Chart Images

<!-- Parent: ../AGENTS.md -->

## Directory Overview

The **charts/** directory contains raster PNG images of charts and diagrams, organized by lecture and derived from PDF source files. These images are embedded as `<img>` elements in lecture HTML pages and serve as visual aids for explaining complex concepts. All images are high-quality PNGs converted from vector PDFs, enabling crisp rendering across all screen sizes.

### Purpose

Provide reusable, high-quality chart graphics for embedding in lecture pages, galleries, and potentially PDFs. Images are PNG (raster) for web delivery but sourced from vector PDFs (scalable source). This approach balances quality with web performance.

### Key Features

- PNG format (8-bit or 24-bit color depth)
- Organized by lecture (L01/, L02/, ...)
- Consistent naming convention (snake_case.png)
- 12 charts per lecture (opening cartoon, 10 content charts, closing cartoon)
- Optimized for web (typically 100–500 KB per image)
- High-quality rendering (typically 150–300 DPI equivalent)
- Responsive sizing via CSS (`max-width: 100%`, etc.)

## Directory Structure

```
charts/
├── L01/
│   ├── opening_cartoon.png           # Intro slide visual
│   ├── fintech_evolution_timeline.png
│   ├── banking_value_chain_disruption.png
│   ├── fintech_ecosystem_overview.png
│   ├── collaboration_models_matrix.png
│   ├── fintech_investment_growth.png
│   ├── bank_fintech_partnership_flow.png
│   ├── great_recession_catalyst.png
│   ├── embedded_finance_architecture.png
│   ├── key_concepts_summary.png
│   └── closing_cartoon.png           # Closing slide visual
│
├── L02/
│   ├── opening_cartoon.png
│   ├── fintech_ecosystem_map.png
│   ├── growth_drivers_dashboard.png
│   ├── financial_inclusion_gap.png
│   ├── mpesa_adoption_flow.png
│   ├── trust_framework_comparison.png
│   ├── technology_adoption_lifecycle.png
│   ├── adoption_barriers_matrix.png
│   ├── nudging_architecture.png
│   ├── choice_architecture_examples.png
│   ├── ecosystem_stakeholder_impact.png
│   └── closing_cartoon.png
│
└── AGENTS.md (this file)
```

## L01 Charts (12 images)

### Category: Foundation & Evolution

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Opening | `opening_cartoon.png` | Illustration | Visual hook, light-hearted intro to fintech topic |
| Timeline | `fintech_evolution_timeline.png` | Timeline diagram | Historical progression from 2008 financial crisis to present |
| Catalyst | `great_recession_catalyst.png` | Context diagram | How 2008 recession triggered fintech innovation |

### Category: Market Structure & Impact

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Ecosystem | `fintech_ecosystem_overview.png` | Network diagram | Fintech players (startups, banks, platforms, regulators) |
| Value Chain | `banking_value_chain_disruption.png` | Flow diagram | How fintech disrupts traditional banking value chain |
| Investment | `fintech_investment_growth.png` | Line/bar chart | VC funding and investment trends over time |

### Category: Business Models & Partnerships

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Models | `collaboration_models_matrix.png` | Matrix diagram | Competition, partnership, acquisition models |
| Flow | `bank_fintech_partnership_flow.png` | Flowchart | Value flow in bank-fintech partnerships |
| Embedded | `embedded_finance_architecture.png` | Architecture diagram | How embedded finance integrates into non-financial platforms |

### Category: Summary & Closing

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Summary | `key_concepts_summary.png` | Infographic | Key takeaways, taxonomy summary |
| Closing | `closing_cartoon.png` | Illustration | Wrap-up visual, humorous or reflective |

## L02 Charts (12 images)

### Category: Ecosystem & Structure

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Opening | `opening_cartoon.png` | Illustration | Visual hook, ecosystem theme |
| Map | `fintech_ecosystem_map.png` | Spatial diagram | Stakeholder positions in fintech landscape |
| Drivers | `growth_drivers_dashboard.png` | Dashboard | Key factors driving fintech growth (regulation, tech, demand) |

### Category: Financial Inclusion & Access

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Inclusion | `financial_inclusion_gap.png` | Map/chart | Geographic and demographic gaps in financial access |
| M-Pesa | `mpesa_adoption_flow.png` | Flow diagram | Case study: M-Pesa mobile money adoption in Kenya |

### Category: Behavioral & Regulatory

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Adoption | `technology_adoption_lifecycle.png` | Curve diagram | S-curve of innovation adoption (early adopters → mainstream) |
| Barriers | `adoption_barriers_matrix.png` | Matrix diagram | Technical, behavioral, regulatory barriers to adoption |
| Trust | `trust_framework_comparison.png` | Comparison table | Different trust models (regulations, brand, blockchain, etc.) |
| Nudging | `nudging_architecture.png` | Architecture diagram | Behavioral economics: choice architecture and nudges |
| Choice | `choice_architecture_examples.png` | Examples | Real-world examples of choice architecture in fintech |

### Category: Impact & Summary

| Chart | Filename | Type | Description |
|-------|----------|------|-------------|
| Impact | `ecosystem_stakeholder_impact.png` | Network/matrix | How fintech impacts different ecosystem stakeholders |
| Closing | `closing_cartoon.png` | Illustration | Wrap-up visual |

## Image Specifications

### Format & Dimensions

| Property | Standard | Notes |
|----------|----------|-------|
| Format | PNG-24 (RGB) | 24-bit color with alpha channel if needed |
| Dimensions | 1280×720 (16:9) or 1440×810 | Standard widescreen for slides |
| DPI (print equivalent) | 150–300 | Sufficient for web and light printing |
| File size | 100–500 KB | Optimized for web, not massive |
| Color space | sRGB | Standard for web browsers |

### Quality Standards

- No artifacts, compression noise, or pixelation
- Text readable at standard viewing distance (no smaller than ~12pt font)
- Colors vibrant, consistent with design system palette
- Contrast sufficient for accessibility (WCAG AA minimum)
- Transparency preserved if applicable (PNG alpha channel)

## Conversion from PDF Source

### Source Location

PDFs are located in:
- `D:/Joerg/Research/slides/Fintech/lectures/L01/slides/` (L01 source)
- `D:/Joerg/Research/slides/Fintech/lectures/L02/slides/` (L02 source)

### Conversion Process

**Tool**: pdftoppm (Linux/Mac) or equivalent Windows tool

**Command** (Linux/Mac):
```bash
pdftoppm -png -r 150 -f 1 -l 1 input.pdf output
# -png: Output PNG format
# -r 150: 150 DPI resolution
# -f 1: Start from page 1
# -l 1: End at page 1
# Result: output-1.png
```

**Alternative Tools**:
- **ImageMagick** (convert): `convert -density 150 input.pdf -resize 1280x720 output.png`
- **Ghostscript** (gs): Direct PDF-to-PNG conversion with color management
- **Online tools**: Zamzar, CloudConvert, ilovepdf.com (if batch conversion not available)

### Optimization

After conversion, optimize PNG file size:

**pngquant** (reduce colors intelligently):
```bash
pngquant --quality=75-95 output.png
```

**pngcrush** (lossless compression):
```bash
pngcrush -brute output.png output-optimized.png
```

**OptiPNG** (maximum lossless compression):
```bash
optipng -o5 output.png
```

**Result**: Reduce file size by 30–50% while maintaining visual quality.

## Embedding in HTML

### Standard Pattern

All lecture pages embed charts using semantic `<figure>` + `<figcaption>`:

```html
<figure class="chart-figure">
  <img src="../charts/L01/fintech_evolution_timeline.png"
       alt="Timeline showing fintech evolution from 2008 to 2024, with major milestones marked"
       loading="lazy">
  <figcaption>Figure 1: Fintech Evolution Timeline. Source: Lecture L01.</figcaption>
</figure>
```

### Key Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `src` | Image path | `../charts/L01/chart_name.png` |
| `alt` | Accessibility, fallback text | Descriptive, complete sentence |
| `loading` | Performance optimization | `loading="lazy"` for deferred loading |
| `class` | CSS styling | `class="chart-figure"` |

### CSS Styling

```css
.chart-figure {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 2rem 0;
  padding: 1rem;
  background: var(--surface-soft);
  border-radius: 8px;
}

.chart-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.chart-figure figcaption {
  font-size: 0.9rem;
  color: var(--ink-subtle);
  margin-top: 1rem;
  text-align: center;
  font-style: italic;
}

@media (max-width: 768px) {
  .chart-figure img {
    max-width: 95%;
  }
}
```

Responsive sizing ensures images scale properly on mobile, tablet, and desktop.

## Naming Convention

### Snake_case Pattern

All filenames use lowercase snake_case:

```
fintech_evolution_timeline.png
banking_value_chain_disruption.png
key_concepts_summary.png
```

**Not**:
```
FinTechEvolutionTimeline.png  (PascalCase - wrong)
fintech_evolution_timeline.PNG (uppercase extension - avoid)
fintech-evolution-timeline.png (kebab-case - inconsistent)
```

### Semantic Naming

Names describe content, not position or lecture number:

```
✓ Correct:
fintech_ecosystem_overview.png
fintech_investment_growth.png

✗ Incorrect:
slide_5_chart.png (position-based)
L01_figure_3.png (redundant with directory)
image1.png (non-semantic)
```

## Common Tasks

### Adding a New Chart

1. **Create or export chart** from design tool (PowerPoint, Keynote, Figma, etc.)
2. **Save as PDF** (if not already)
3. **Convert to PNG** using pdftoppm or similar:
   ```bash
   pdftoppm -png -r 150 chart.pdf chart_output
   # Result: chart_output-1.png
   ```
4. **Optimize PNG** (reduce file size 30–50%):
   ```bash
   pngquant --quality=75-95 chart_output-1.png
   optipng -o5 chart_output-1.png
   ```
5. **Rename to semantic name**: `growth_drivers_dashboard.png`
6. **Move to correct directory**: `charts/L02/`
7. **Embed in lecture HTML**: Add `<figure>` with `<img>` tag
8. **Test rendering** on desktop, tablet, mobile

### Updating an Existing Chart

1. **Edit source chart** (PowerPoint, design tool, etc.)
2. **Export as PDF** with same name
3. **Convert to PNG** (same process as above)
4. **Optimize file size**
5. **Replace PNG file** in charts/ directory (same filename)
6. **Browser cache**: Users may see old image. Add cache-buster if needed:
   ```html
   <img src="../charts/L01/chart_name.png?v=2" ...>
   ```
7. **Test** in browser (hard refresh: Ctrl+Shift+R)

### Creating a New Lecture's Charts

1. **Design/export 12 chart images** (following naming convention)
2. **Create directory** `charts/L0{N}/`
3. **Move PNGs** to new directory
4. **Document chart descriptions** in this AGENTS.md (or separate README)
5. **Embed in lecture HTML** (add `<figure>` tags for each chart)
6. **Test responsive sizing** (mobile, tablet, desktop)

### Batch Conversion from PDF

If you have multiple PDFs to convert:

**Linux/Mac script**:
```bash
for file in *.pdf; do
  base="${file%.pdf}"
  pdftoppm -png -r 150 "$file" "$base"
  pngquant --quality=75-95 "${base}-1.png"
  mv "${base}-1-or8.png" "${base}.png"  # Rename optimized version
done
```

**Windows (PowerShell)**:
```powershell
Get-ChildItem *.pdf | ForEach-Object {
  $name = $_.BaseName
  & pdftoppm -png -r 150 $_ $name
  # Then optimize with pngquant or other tools
}
```

## Testing Checklist

- [ ] All 12 L01 charts present and accessible
- [ ] All 12 L02 charts present and accessible
- [ ] File names follow snake_case convention
- [ ] File sizes reasonable (< 500 KB each)
- [ ] Images render correctly in browsers (no broken image icons)
- [ ] PNG quality acceptable (no obvious compression artifacts)
- [ ] Text in charts readable at standard viewing sizes
- [ ] Responsive design works (images scale on mobile/tablet)
- [ ] Alt text complete and descriptive (for accessibility)
- [ ] Color contrast meets WCAG AA standards (if text on colored backgrounds)
- [ ] Lazy loading works (DevTools confirms deferred loading)

## AI Agent Instructions

### Designer / Visual Editor

- **Focus**: Chart quality, visual consistency, design system alignment
- **Key tasks**: Create/update charts, verify visual consistency, optimize images
- **DO**: Use consistent color palette from design system. Export high-quality PNGs. Test on multiple devices.
- **AVOID**: Raster images as source (always source from vector PDFs or design tools). Low-quality exports.

### DevOps / Image Optimization

- **Focus**: File sizes, loading performance, compression
- **Key tasks**: Optimize PNGs, monitor file sizes, test lazy loading
- **DO**: Use pngquant or optipng for compression. Target < 300 KB per image. Verify lazy loading works.
- **AVOID**: Storing unoptimized originals. Over-compressing (visible quality loss).

### Content Editor

- **Focus**: Chart accuracy, figure captions, alt text quality
- **Key tasks**: Verify chart accuracy, write descriptive captions and alt text
- **DO**: Ensure alt text is complete, descriptive sentence. Check captions match content.
- **AVOID**: Vague or placeholder alt text. Missing figure captions.

## Related Documentation

- **Parent**: `../AGENTS.md` — Overview of entire website
- **Lectures**: `../lectures/AGENTS.md` — Lecture pages (where charts are embedded)
- **Galleries**: `../galleries/AGENTS.md` — Slide galleries (may reference chart images)
- **Downloads**: `../downloads/AGENTS.md` — PDF variants (may embed chart PNGs)
- **Source Materials**: `D:/Joerg/Research/slides/Fintech/lectures/L01/slides/` — Original slide decks
