# AGENTS.md — Slide Gallery Pages

<!-- Parent: ../AGENTS.md -->

## Directory Overview

The **galleries/** directory contains interactive slide gallery pages (~1800 lines each) with five viewing variants (mini5, mini10, core, extended, full) and a lightbox viewer for detailed slide inspection. Each gallery is a standalone HTML page with inline CSS and JavaScript, powered by PNG slide images organized in the `images/` subdirectory.

### Purpose

Provide interactive, tabbed browsing of lecture slides with lightweight lightbox navigation. Users can view slides at different granularities (from 6-slide summary to 31-slide full deck) and magnify individual slides for detailed reading.

### Key Features

- 5 viewing tabs (mini5, mini10, core, extended, full) per lecture
- Lightbox modal viewer with keyboard navigation (arrow keys, ESC)
- Lazy image loading for performance on mobile
- Responsive grid layout (2 columns on mobile, 3–4 on desktop)
- Tab persistence (current tab saved in localStorage)
- Click to open lightbox, arrow keys to navigate, ESC to close
- No external image libraries—vanilla JS lightbox implementation

## Files & Structure

### L01_gallery.html — L01 Slide Gallery

**Interactive gallery page for Lecture 1 (~1800 lines)**

**Title**: "L01 Slide Gallery — Fintech Foundations and Overview"

**Viewing Modes** (5 tabs):

| Tab | Slides | Use Case |
|-----|--------|----------|
| mini5 | 6 slides | Executive summary, ultra-quick review |
| mini10 | 11 slides | Overview version, key concepts only |
| core | 10 slides | Core content, recommended for most learners |
| extended | 27 slides | Comprehensive coverage, includes detailed explanations |
| full | 31 slides | Complete deck with appendix and references |

**Images Source**: `images/L01/{variant}/slide-{N}.png`
- `L01/mini5/`: 6 slides (slide-1.png through slide-6.png, note inconsistent naming)
- `L01/mini10/`: 11 slides (slide-01.png through slide-11.png)
- `L01/core/`: 10 slides (slide-01.png through slide-10.png)
- `L01/extended/`: 27 slides (slide-01.png through slide-27.png)
- `L01/full/`: 31 slides (slide-01.png through slide-31.png)

**Special Features**:
- Sticky tab bar with smooth scrolling
- Lightbox with current/total slide counter (e.g., "3 / 31")
- Keyboard navigation: left/right arrows to browse, ESC to close
- Touch support for mobile swiping (optional, basic implementation)

### L02_gallery.html — L02 Slide Gallery

**Interactive gallery page for Lecture 2 (~1800 lines)**

**Title**: "L02 Slide Gallery — Fintech Ecosystem"

**Viewing Modes** (5 tabs): Same as L01

**Images Source**: `images/L02/{variant}/slide-{N}.png`
- `L02/mini5/`: 6 slides
- `L02/mini10/`: 11 slides
- `L02/core/`: 10 slides
- `L02/extended/`: 27 slides
- `L02/full/`: 31 slides

**Special Features**: Same as L01

## HTML Structure

Both gallery pages follow the same structural template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>L01 Slide Gallery</title>
  <style>
    /* Inline CSS (~1400 lines) */
  </style>
</head>
<body>
  <!-- Sticky navigation bar -->
  <nav class="navbar">...</nav>

  <!-- Main gallery container -->
  <div class="main">
    <!-- Sticky tab bar -->
    <div class="tab-bar-wrap">
      <button class="tab-btn active" data-variant="mini5">
        <span class="tab-label">mini5</span>
        <span class="tab-count">6</span>
      </button>
      <!-- ... more tabs ... -->
    </div>

    <!-- Gallery grid (images update based on active tab) -->
    <div class="gallery-grid">
      <!-- Images rendered here via JavaScript -->
    </div>
  </div>

  <!-- Lightbox modal -->
  <div class="lightbox" style="display: none;">
    <div class="lightbox-inner">
      <button class="lightbox-close">&times;</button>
      <button class="lightbox-prev">&#8249;</button>
      <img class="lightbox-image" src="" alt="">
      <button class="lightbox-next">&#8250;</button>
      <div class="lightbox-counter">1 / 31</div>
    </div>
  </div>

  <script>
    // Gallery logic, tab management, lightbox behavior
  </script>
</body>
</html>
```

## Design System

### CSS Variables

Defined in `:root` scope:

```css
:root {
  --nav-bg:         #1a1a4e;
  --nav-text:       #e8e8f0;
  --nav-link:       #14BDEB;
  --hero-from:      #0D7377;
  --hero-to:        #14BDEB;
  --accent:         #FF7F0E;
  --bg:             #f0f2f8;
  --card-bg:        #ffffff;
  --card-border:    #dde2f0;
  --text-dark:      #1a1a2e;
  --text-mid:       #444466;
  --text-light:     #7a7a9a;
  --tab-active-bg:  #0D7377;
  --tab-hover-bg:   rgba(13,115,119,0.1);
  --shadow-sm:      0 2px 8px rgba(26,26,78,0.08);
  --shadow-md:      0 6px 24px rgba(26,26,78,0.13);
  --shadow-lg:      0 16px 48px rgba(26,26,78,0.22);
  --radius:         10px;
  --radius-lg:      16px;
}
```

### Responsive Grid

| Breakpoint | Width | Columns | Item Size |
|------------|-------|---------|-----------|
| Mobile | 375px | 2 | ~170px |
| Tablet | 768px | 3 | ~240px |
| Desktop | 1120px+ | 4 | ~280px |

Items are centered with padding and maintain 16:9 aspect ratio (slides are 16:9 format).

### Tab Bar

- Background: `--card-bg` (#ffffff) with shadow
- Active tab: `--tab-active-bg` (#0D7377), white text
- Hover tab: `--tab-hover-bg` (semi-transparent, light background)
- Smooth scroll on horizontal overflow (mobile)

### Lightbox Modal

- Background: `rgba(0, 0, 0, 0.92)` (nearly opaque dark)
- Image: Centered, max-width 90vw, max-height 85vh
- Controls: Navigation arrows, close button, counter
- Z-index: 1000 (above all page content)

## Image Organization

### Directory Structure

```
galleries/
├── L01_gallery.html
├── L02_gallery.html
└── images/
    ├── L01/
    │   ├── mini5/
    │   │   ├── slide-1.png
    │   │   ├── slide-2.png
    │   │   ...
    │   │   └── slide-6.png
    │   ├── mini10/
    │   │   ├── slide-01.png
    │   │   ├── slide-02.png
    │   │   ...
    │   │   └── slide-11.png
    │   ├── core/
    │   ├── extended/
    │   └── full/
    └── L02/
        ├── mini5/
        ├── mini10/
        ├── core/
        ├── extended/
        └── full/
```

### Naming Convention

**Issue**: mini5 uses single-digit numbering (`slide-1.png`, `slide-2.png`, ..., `slide-6.png`), while other variants use zero-padded double-digit (`slide-01.png`, `slide-02.png`, ...).

**Impact**: JavaScript image path construction must account for this inconsistency.

**Solution** (in gallery HTML):

```javascript
function getImagePath(variant, index) {
  const lecture = 'L01'; // or 'L02'
  if (variant === 'mini5') {
    // single-digit: slide-1.png through slide-6.png
    return `images/${lecture}/${variant}/slide-${index}.png`;
  } else {
    // zero-padded: slide-01.png through slide-31.png
    return `images/${lecture}/${variant}/slide-${String(index).padStart(2, '0')}.png`;
  }
}
```

## JavaScript Functionality

### Tab Switching

```javascript
const tabButtons = document.querySelectorAll('.tab-btn');
const gallery = document.querySelector('.gallery-grid');

tabButtons.forEach(btn => {
  btn.addEventListener('click', () => {
    const variant = btn.dataset.variant;
    tabButtons.forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    // Save to localStorage
    localStorage.setItem('gallery-variant', variant);

    // Render gallery for this variant
    renderGallery(variant);
  });
});

// On load, restore last viewed variant
const savedVariant = localStorage.getItem('gallery-variant') || 'core';
document.querySelector(`[data-variant="${savedVariant}"]`).click();
```

### Image Lazy Loading

Images use `loading="lazy"` attribute. As user scrolls, images load on demand (browser native).

Alternative: Intersection Observer API for custom lazy loading.

### Lightbox Navigation

```javascript
const lightbox = document.querySelector('.lightbox');
const lightboxImage = document.querySelector('.lightbox-image');
const counter = document.querySelector('.lightbox-counter');
let currentImageIndex = 0;
let totalImages = 0;

// Open lightbox on image click
gallery.addEventListener('click', (e) => {
  if (e.target.tagName === 'IMG') {
    currentImageIndex = Array.from(gallery.querySelectorAll('img')).indexOf(e.target);
    totalImages = gallery.querySelectorAll('img').length;
    showLightbox();
  }
});

// Navigation
document.querySelector('.lightbox-prev').addEventListener('click', () => {
  currentImageIndex = (currentImageIndex - 1 + totalImages) % totalImages;
  updateLightbox();
});

document.querySelector('.lightbox-next').addEventListener('click', () => {
  currentImageIndex = (currentImageIndex + 1) % totalImages;
  updateLightbox();
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  if (lightbox.style.display === 'block') {
    if (e.key === 'ArrowLeft') currentImageIndex--;
    if (e.key === 'ArrowRight') currentImageIndex++;
    if (e.key === 'Escape') closeLightbox();
  }
});

function updateLightbox() {
  const img = gallery.querySelectorAll('img')[currentImageIndex];
  lightboxImage.src = img.src;
  lightboxImage.alt = img.alt;
  counter.textContent = `${currentImageIndex + 1} / ${totalImages}`;
}
```

### Responsive Grid Rendering

Grid layout defined in CSS:

```css
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
  padding: 24px;
}

@media (max-width: 768px) {
  .gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .gallery-grid {
    grid-template-columns: 1fr;
  }
}
```

Each image maintains 16:9 aspect ratio via CSS:

```css
.gallery-item {
  position: relative;
  padding-bottom: 56.25%; /* 16:9 */
  overflow: hidden;
  border-radius: var(--radius);
  cursor: pointer;
}

.gallery-item img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
```

## Common Tasks

### Adding a New Lecture Gallery

1. **Create new gallery HTML** at `galleries/L03_gallery.html` (copy from L01_gallery.html)
2. **Update `<title>` and `.nav-brand`** to reference L03
3. **Create image directories**: `images/L03/mini5/`, `mini10/`, `core/`, `extended/`, `full/`
4. **Place slide PNGs** in corresponding directories (ensure correct naming: single-digit for mini5, zero-padded for others)
5. **Update lecture reference** in JavaScript (change `'L01'` to `'L03'` in `getImagePath()`)
6. **Test all tabs** to verify images load and lightbox works

### Updating Slide Images

1. **Identify variant** (mini5, mini10, core, extended, or full)
2. **Replace PNG file** in `images/L0{N}/{variant}/slide-{N}.png`
3. **Hard refresh** browser (Ctrl+Shift+R or Cmd+Shift+R) to bypass cache
4. **Verify image loads** in gallery and lightbox

### Fixing Image Path Issues

If images don't load, check:
1. File exists at correct path (use file explorer or `ls` command)
2. Naming convention correct (single-digit for mini5, zero-padded for others)
3. JavaScript `getImagePath()` function handles variant correctly
4. Browser console shows no 404 errors (DevTools Network tab)

### Customizing Tab Order or Names

Edit tab buttons in HTML:

```html
<div class="tab-bar-wrap">
  <button class="tab-btn active" data-variant="mini5">
    <span class="tab-label">Quick</span>
    <span class="tab-count">6</span>
  </button>
  <!-- Rename "mini5" to "Quick" above -->
</div>
```

Also update corresponding data-variant attributes and JavaScript logic.

## Testing Checklist

- [ ] All 5 tabs load without errors
- [ ] Images display in correct grid (2 cols mobile, 3+ cols desktop)
- [ ] Lightbox opens on image click
- [ ] Keyboard navigation works (arrow keys, ESC)
- [ ] Counter shows correct current/total slide numbers
- [ ] Tab state persists across page reloads (localStorage)
- [ ] Lazy loading works (check DevTools Network tab)
- [ ] Responsive design: test 375px, 768px, 1120px+
- [ ] No 404 errors in console (all images load)
- [ ] Touch/swipe works on mobile (optional, if implemented)

## AI Agent Instructions

### Designer / Frontend Developer

- **Focus**: Grid layout, lightbox UX, responsive design, color scheme consistency
- **Key tasks**: Adjust grid breakpoints, refine lightbox styling, test on real devices
- **DO**: Use CSS Grid/Flexbox. Inline all CSS. Test keyboard and touch navigation.
- **AVOID**: External image libraries. Keep lightbox vanilla JS.

### QA / Testing

- **Focus**: Image loading, tab switching, lightbox navigation, responsive design
- **Key tasks**: Test all tabs, verify images load, check keyboard navigation
- **DO**: Test on actual mobile devices, check DevTools Network for 404s, verify image paths
- **AVOID**: Assuming images are correct—always test each variant.

### DevOps / Optimization

- **Focus**: Image optimization, lazy loading performance, cache headers
- **Key tasks**: Verify lazy loading, optimize PNG sizes, test load times
- **DO**: Use DevTools Lighthouse for performance metrics. Profile image loading.
- **AVOID**: Over-optimizing—balance quality and file size.

## Related Documentation

- **Parent**: `../AGENTS.md` — Overview of entire website
- **Lectures**: `../lectures/AGENTS.md` — Lecture content pages
- **Charts**: `../charts/AGENTS.md` — Chart image organization (related to gallery images)
- **Quizzes**: `../quizzes/AGENTS.md` — Interactive quizzes (similar structure)
- **Image Directory**: `images/` — PNG slide organization (5 variants per lecture)
