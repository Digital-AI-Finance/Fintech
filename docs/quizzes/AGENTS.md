# AGENTS.md — Interactive Quiz Pages

<!-- Parent: ../AGENTS.md -->

## Directory Overview

The **quizzes/** directory contains interactive multiple-choice question (MCQ) quiz pages (~1600 lines each) with instant feedback, Bloom's taxonomy classification, and progress tracking. Each lecture has two quiz variants (standard and advanced), for a total of 4 quiz pages. Quizzes are self-contained HTML files with inline CSS and JavaScript—no server-side scoring or databases.

### Purpose

Provide formative assessment for learners with immediate feedback, difficulty levels based on Bloom's taxonomy, and visual progress tracking. Quizzes reinforce lecture content and help learners self-assess comprehension.

### Key Features

- 20 MCQ questions per quiz (4 answer options A–D)
- Instant feedback on answer submission (correct/incorrect with color coding)
- Bloom's taxonomy badges: Understand, Apply, Analyze, Evaluate, Create
- Color-coded difficulty indicators (linked to Bloom's levels)
- Progress bar showing completion percentage
- Score calculation and display
- No server required—all logic in client-side JavaScript
- Responsive design for mobile, tablet, desktop

## Files & Structure

### L01_quiz.html — L01 Standard Quiz

**Interactive quiz page for Lecture 1 - Standard Difficulty (~1600 lines)**

**Title**: "L01 Standard Quiz — Financial Technology (FinTech)"

**Content**: 20 MCQ questions covering L01 core content
- Questions target Understand, Apply, Analyze, Evaluate levels
- Mix of direct fact recall and conceptual understanding
- Each question is self-contained in a `.q-card` div

**Question Breakdown by Bloom's Level**:
- Understand (U): ~40% (8 questions)
- Apply (AP): ~30% (6 questions)
- Analyze (AN): ~20% (4 questions)
- Evaluate (EV): ~10% (2 questions)
- Create (CR): ~0% (0 questions - rare in quizzes)

**Example Question Structure**:

```html
<div class="q-card">
  <div class="q-header">
    <div class="q-num">1</div>
    <div class="q-meta">
      <div class="q-text">
        What is the primary definition of fintech?
      </div>
      <div class="bloom-badge bloom-u">Understand</div>
    </div>
  </div>
  <div class="q-options">
    <label><input type="radio" name="q1" value="a"> A) Technology used exclusively in banking</label>
    <label><input type="radio" name="q1" value="b"> B) Financial services powered by technology</label>
    <label><input type="radio" name="q1" value="c"> C) Cryptocurrency only</label>
    <label><input type="radio" name="q1" value="d"> D) Software for banks to manage accounts</label>
  </div>
</div>
```

### L01_quiz_advanced.html — L01 Advanced Quiz

**Interactive quiz page for Lecture 1 - Advanced Difficulty (~1600 lines)**

**Title**: "L01 Advanced Quiz — Financial Technology (FinTech)"

**Content**: 20 MCQ questions covering L01 advanced topics and synthesis
- Questions target Apply, Analyze, Evaluate, Create levels
- Focus on critical thinking, scenario analysis, synthesis
- Designed for learners seeking deeper understanding

**Question Breakdown by Bloom's Level**:
- Understand (U): ~0% (0 questions)
- Apply (AP): ~30% (6 questions)
- Analyze (AN): ~40% (8 questions)
- Evaluate (EV): ~25% (5 questions)
- Create (CR): ~5% (1 question)

### L02_quiz.html — L02 Standard Quiz

**Interactive quiz page for Lecture 2 - Standard Difficulty (~1600 lines)**

**Title**: "L02 Standard Quiz — Financial Technology (FinTech)"

**Content**: 20 MCQ questions covering L02 core content (fintech ecosystem, growth drivers, financial inclusion)

### L02_quiz_advanced.html — L02 Advanced Quiz

**Interactive quiz page for Lecture 2 - Advanced Difficulty (~1600 lines)**

**Title**: "L02 Advanced Quiz — Financial Technology (FinTech)"

**Content**: 20 MCQ questions covering L02 advanced topics (behavioral economics, regulation, ecosystem impact)

## HTML Structure

All quiz pages follow the same structural template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>L01 Standard Quiz</title>
  <style>
    /* Inline CSS (~1200 lines) */
  </style>
</head>
<body>
  <!-- Sticky navigation bar -->
  <nav class="navbar">...</nav>

  <!-- Hero section -->
  <section class="hero">...</section>

  <!-- Quiz container -->
  <div class="quiz-container">
    <!-- Progress bar -->
    <div class="progress-section">
      <h2>Progress</h2>
      <div class="progress-bar">
        <div class="progress-fill"></div>
      </div>
      <div class="progress-text">0 / 20 answered</div>
    </div>

    <!-- Quiz questions -->
    <div class="quiz-form">
      <!-- 20 .q-card divs, one per question -->
    </div>

    <!-- Check answers button -->
    <button class="check-btn">Check Answers</button>

    <!-- Results display -->
    <div class="results-section" style="display: none;">
      <h2>Your Score: <span class="score-value">0</span>/20</h2>
      <div class="score-breakdown">
        <!-- Bloom's level breakdown -->
      </div>
    </div>
  </div>

  <script>
    // Quiz logic, answer validation, scoring
  </script>
</body>
</html>
```

## Design System

### CSS Variables

Defined in `:root` scope:

```css
:root {
  --nav-bg:       #1a1a4e;
  --nav-text:     #e8e8f0;
  --nav-link:     #14BDEB;
  --hero-from:    #0D7377;
  --hero-to:      #14BDEB;
  --accent:       #FF7F0E;
  --bg:           #f5f6fa;
  --card-bg:      #ffffff;
  --card-border:  #e0e4ef;
  --text-dark:    #1a1a2e;
  --text-mid:     #444466;
  --text-light:   #888;

  /* Bloom's taxonomy colors */
  --bloom-u:      #2CA02C;  /* Understand - Green */
  --bloom-ap:     #1F77B4;  /* Apply - Blue */
  --bloom-an:     #FF7F0E;  /* Analyze - Orange */
  --bloom-ev:     #D62728;  /* Evaluate - Red */
  --bloom-cr:     #9467BD;  /* Create - Purple */

  /* Feedback colors */
  --correct:      #2CA02C;
  --incorrect:    #D62728;
  --check-btn:    #0D7377;
  --check-hover:  #0a5e62;

  --shadow-sm:    0 2px 8px rgba(26,26,78,0.08);
  --shadow-md:    0 4px 20px rgba(26,26,78,0.12);
  --radius:       10px;
}
```

### Bloom's Taxonomy Badges

| Level | Abbrev | Color | Hex | Use |
|-------|--------|-------|-----|-----|
| Understand | U | Green | #2CA02C | Recall, define, identify |
| Apply | AP | Blue | #1F77B4 | Use concepts, solve examples |
| Analyze | AN | Orange | #FF7F0E | Break down, compare, distinguish |
| Evaluate | EV | Red | #D62728 | Judge, critique, justify |
| Create | CR | Purple | #9467BD | Generate, design, compose |

Each badge is a small span with background color, white text, rounded corners:

```css
.bloom-badge {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 2px 9px;
  border-radius: 6px;
  color: #ffffff;
}

.bloom-u  { background-color: var(--bloom-u);  }
.bloom-ap { background-color: var(--bloom-ap); }
.bloom-an { background-color: var(--bloom-an); }
.bloom-ev { background-color: var(--bloom-ev); }
.bloom-cr { background-color: var(--bloom-cr); }
```

### Question Card Styling

```css
.q-card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--radius);
  padding: 24px 28px;
  margin-bottom: 16px;
  box-shadow: var(--shadow-sm);
  transition: box-shadow 0.2s, border-color 0.2s;
}

.q-card:hover {
  box-shadow: var(--shadow-md);
  border-color: #c8d0e8;
}

.q-card.correct {
  border-left: 4px solid var(--correct);
  background: #f6fff6;
}

.q-card.incorrect {
  border-left: 4px solid var(--incorrect);
  background: #fff7f7;
}
```

### Progress Bar

```css
.progress-section {
  margin-bottom: 32px;
  padding: 24px;
  background: var(--card-bg);
  border-radius: var(--radius);
  box-shadow: var(--shadow-sm);
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: var(--card-border);
  border-radius: 10px;
  overflow: hidden;
  margin: 12px 0;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--hero-from), var(--hero-to));
  transition: width 0.3s ease;
}

.progress-text {
  font-size: 0.85rem;
  color: var(--text-mid);
}
```

## JavaScript Answer Data Structure

### ANSWERS Object

Central data structure containing correct answers and metadata:

```javascript
const ANSWERS = {
  q1: {
    correct: 'b',
    bloom: 'Understand',
    explanation: 'Fintech refers to financial services delivered through technology...'
  },
  q2: {
    correct: 'a',
    bloom: 'Apply',
    explanation: 'Mobile banking exemplifies fintech by...'
  },
  // ... q3 through q20 ...
};
```

**Keys**:
- `q1` – `q20`: Question identifiers (must match HTML input `name` attributes)
- `correct`: Answer key ('a', 'b', 'c', or 'd')
- `bloom`: Bloom's taxonomy level ('Understand', 'Apply', 'Analyze', 'Evaluate', 'Create')
- `explanation`: Feedback text shown after answer submission (optional but recommended)

### Quiz Logic

**Main functions**:

```javascript
// Get user's answer for question N
function getUserAnswer(questionNum) {
  const radio = document.querySelector(`input[name="q${questionNum}"]:checked`);
  return radio ? radio.value : null;
}

// Check if answer is correct
function isCorrect(questionNum, answer) {
  return ANSWERS[`q${questionNum}`].correct === answer;
}

// Validate all answers
function checkAnswers() {
  let score = 0;
  let bloomCounts = { Understand: 0, Apply: 0, Analyze: 0, Evaluate: 0, Create: 0 };

  for (let i = 1; i <= 20; i++) {
    const card = document.querySelector(`.q-card[data-q="${i}"]`);
    const userAnswer = getUserAnswer(i);
    const correct = isCorrect(i, userAnswer);

    if (correct) {
      score++;
      card.classList.add('correct');
      bloomCounts[ANSWERS[`q${i}`].bloom]++;
    } else {
      card.classList.add('incorrect');
    }
  }

  displayResults(score, bloomCounts);
}

// Display score and breakdown
function displayResults(score, bloomCounts) {
  document.querySelector('.results-section').style.display = 'block';
  document.querySelector('.score-value').textContent = score;

  const breakdown = document.querySelector('.score-breakdown');
  breakdown.innerHTML = `
    <p>Understand: ${bloomCounts['Understand']} correct</p>
    <p>Apply: ${bloomCounts['Apply']} correct</p>
    <p>Analyze: ${bloomCounts['Analyze']} correct</p>
    <p>Evaluate: ${bloomCounts['Evaluate']} correct</p>
  `;
}

// Update progress bar
window.addEventListener('change', () => {
  let answered = 0;
  for (let i = 1; i <= 20; i++) {
    if (getUserAnswer(i)) answered++;
  }
  document.querySelector('.progress-fill').style.width = `${(answered / 20) * 100}%`;
  document.querySelector('.progress-text').textContent = `${answered} / 20 answered`;
});
```

## Common Tasks

### Adding a New Quiz Question

1. **Add HTML question card** in `.quiz-form`:
```html
<div class="q-card" data-q="21">
  <div class="q-header">
    <div class="q-num">21</div>
    <div class="q-meta">
      <div class="q-text">
        New question text here?
      </div>
      <div class="bloom-badge bloom-an">Analyze</div>
    </div>
  </div>
  <div class="q-options">
    <label><input type="radio" name="q21" value="a"> A) Option 1</label>
    <label><input type="radio" name="q21" value="b"> B) Option 2</label>
    <label><input type="radio" name="q21" value="c"> C) Option 3</label>
    <label><input type="radio" name="q21" value="d"> D) Option 4</label>
  </div>
</div>
```

2. **Add entry to ANSWERS object**:
```javascript
q21: {
  correct: 'c',
  bloom: 'Analyze',
  explanation: 'Explanation text here...'
}
```

3. **Update quiz form** to include 21 questions (modify loop limits if using generated HTML)

**Note**: Current implementation has exactly 20 questions. Adding more requires updating hardcoded loops.

### Changing Question Difficulty Level

Edit the `.bloom-badge` class and ANSWERS object `bloom` value:

```html
<!-- Before: Understand -->
<div class="bloom-badge bloom-u">Understand</div>

<!-- After: Analyze -->
<div class="bloom-badge bloom-an">Analyze</div>
```

```javascript
// Before:
q1: { correct: 'b', bloom: 'Understand', ... }

// After:
q1: { correct: 'b', bloom: 'Analyze', ... }
```

### Updating Question Text or Options

Edit question text and/or answer options in HTML. Update correct answer in ANSWERS object if needed:

```html
<!-- Change question text -->
<div class="q-text">
  Updated question text here?
</div>

<!-- Change answer options -->
<label><input type="radio" name="q1" value="a"> A) Updated option 1</label>
```

```javascript
// Update correct answer if option order changed
q1: { correct: 'a', ... }  // was 'b', now 'a'
```

### Creating a New Quiz for a Lecture

1. **Copy existing quiz** (e.g., L01_quiz.html → L03_quiz.html)
2. **Update `<title>`, `.nav-brand`, hero section** to reference L03
3. **Verify 20 questions** present in `.quiz-form`
4. **Update ANSWERS object** with L03 correct answers and Bloom's levels
5. **Test all 20 questions** to verify checkAnswers() works correctly

## Testing Checklist

- [ ] All 20 questions display correctly
- [ ] Bloom's badges show correct colors and labels
- [ ] Radio buttons work (only one answer per question)
- [ ] Progress bar updates as answers are selected
- [ ] "Check Answers" button calculates score correctly
- [ ] Correct answers highlighted in green, incorrect in red
- [ ] Score breakdown by Bloom's level displayed
- [ ] Explanations show (if included in ANSWERS)
- [ ] Responsive design: test 375px, 768px, 1120px+
- [ ] No console errors (check DevTools)

## AI Agent Instructions

### Content Writer / Subject Matter Expert

- **Focus**: Question accuracy, Bloom's classification, explanation clarity
- **Key tasks**: Write/edit questions, verify correct answers, update explanations
- **DO**: Ensure questions align with lecture content. Double-check Bloom's levels.
- **AVOID**: Changing HTML structure or JavaScript. Content edits only.

### QA / Testing

- **Focus**: Answer validation, scoring logic, responsive design
- **Key tasks**: Test all questions, verify scoring, check mobile UX
- **DO**: Test checkAnswers() function. Verify score calculation. Test on real devices.
- **AVOID**: Assuming correct answers—verify each against lecture content.

### Designer / Frontend Developer

- **Focus**: Visual hierarchy, color scheme, badge styling, responsive layout
- **Key tasks**: Refine styling, ensure accessibility, adjust breakpoints
- **DO**: Maintain Bloom's color scheme. Test color contrast. Inline all CSS.
- **AVOID**: External CSS files or frameworks. Keep design consistent with other pages.

## Related Documentation

- **Parent**: `../AGENTS.md` — Overview of entire website
- **Lectures**: `../lectures/AGENTS.md` — Lecture content (referenced by quiz questions)
- **Galleries**: `../galleries/AGENTS.md` — Slide galleries (companion to quizzes)
- **Bloom's Taxonomy Reference**: https://en.wikipedia.org/wiki/Bloom%27s_taxonomy
