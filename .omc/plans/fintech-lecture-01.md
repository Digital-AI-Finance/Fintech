# Work Plan: Lecture 1 -- Fintech Foundations and Overview

## Context

### Source Plan
Full course plan: `.omc/plans/fintech-course.md`

### Lecture Identity
- **Number:** 1
- **Title:** Fintech Foundations and Overview
- **Subtitle:** Understanding the Revolution in Financial Services
- **Module:** Foundations (green `#2CA02C`)
- **Duration:** ~2h15m (Day 1 morning, 09:00-11:15)
- **Prerequisites:** None (this is Lecture 1)
- **Audience:** MSc Finance/Business (strong finance, limited tech/coding)
- **Chart constraint:** Conceptual diagrams ONLY (no real market data)

### Topics from Manifest
1. Definitions and evolution of fintech
2. The great recession as a catalyst for fintech innovation
3. Importance and impact of fintech in the financial industry
4. Collaboration vs. competition between traditional financial institutions and fintech
5. Key trends and innovations in fintech

### Course Creator Pipeline Reference
- Stage 1: `course-creator-slides.md` -- LaTeX .tex generation
- Stage 2: `course-creator-charts.md` -- Python chart scripts + PDF compilation
- Stage 3: `course-creator-galleries.md` -- PDF-to-PNG + gallery HTML
- Stage 4: `course-creator-lectures.md` -- LaTeX-to-HTML lecture pages
- Stage 5: `course-creator-quizzes.md` -- Interactive quiz HTML pages
- Beamer architecture: `beamer-slide-creator.md`
- Full lecture: `full-lecture-generator.md` (30-slide arc)
- Mini lecture: `mini-lecture-generator.md` (5/10-slide arcs)

---

## Lecture 1 Directory Structure

```
D:/Joerg/Research/slides/Fintech/
  _shared/
    preamble.tex                          (Fintech-specific shared preamble)
    chart_styles.py                       (Fintech theme V4_COLORS)
  lectures/
    L01_fintech_foundations/
      slides/
        L01_full.tex     + L01_full.pdf     (~30 slides)
        L01_overview.tex + L01_overview.pdf  (~25-30 slides)
        L01_deepdive.tex + L01_deepdive.pdf  (~15-20 slides)
        L01_core.tex     + L01_core.pdf      (~10 slides)
        L01_mini10.tex   + L01_mini10.pdf    (10 slides)
        L01_mini5.tex    + L01_mini5.pdf     (5 slides)
      figures/
        01_fintech_evolution_timeline/chart.py + chart.pdf
        02_banking_value_chain_disruption/chart.py + chart.pdf
        03_collaboration_models_matrix/chart.py + chart.pdf
        04_fintech_ecosystem_overview/chart.py + chart.pdf
        05_great_recession_catalyst/chart.py + chart.pdf
        06_fintech_investment_growth/chart.py + chart.pdf
        07_bank_fintech_partnership_flow/chart.py + chart.pdf
        08_embedded_finance_architecture/chart.py + chart.pdf
        09_fintech_impact_comparison/chart.py + chart.pdf
        10_key_concepts_summary/chart.py + chart.pdf
        11_opening_cartoon/cartoon.py + cartoon.pdf
        12_closing_cartoon/cartoon.py + cartoon.pdf
      quizzes/
        L01_quiz_standard.tex + L01_quiz_standard.pdf
        L01_quiz_advanced.tex + L01_quiz_advanced.pdf
      exercises/
        L01_exercises.tex + L01_exercises.pdf
  website/
    lectures/
      L01.html
    quizzes/
      L01_quiz.html
      L01_quiz_advanced.html
    galleries/
      L01_gallery.html
      images/
        L01/
          mini5/    slide_01.png ... slide_05.png
          mini10/   slide_01.png ... slide_10.png
          core/     slide_01.png ... slide_10.png
          extended/ slide_01.png ... slide_NN.png
          full/     slide_01.png ... slide_NN.png
    downloads/
      L01_mini5.pdf
      L01_mini10.pdf
      L01_core.pdf
      L01_overview.pdf
      L01_deepdive.pdf
      L01_full.pdf
    charts/
      L01/
        fintech_evolution_timeline.png
        banking_value_chain_disruption.png
        collaboration_models_matrix.png
        fintech_ecosystem_overview.png
        great_recession_catalyst.png
        fintech_investment_growth.png
        bank_fintech_partnership_flow.png
        embedded_finance_architecture.png
        fintech_impact_comparison.png
        key_concepts_summary.png
        opening_cartoon.png
        closing_cartoon.png
```

---

## Part 1: Full Variant Slide-by-Slide Breakdown (~31 frames)

### Core Tension
"Technology is reshaping finance faster than any force since the printing press -- but is fintech replacing banks, or are banks becoming fintech?"

### Learning Objectives (Bloom's tagged)
1. **Describe** the defining characteristics of fintech and trace its historical evolution from early electronic banking to modern embedded finance. [Understand]
2. **Explain** how the 2008 financial crisis acted as a catalyst for fintech innovation by eroding trust in traditional institutions. [Understand]
3. **Classify** the major collaboration models between traditional financial institutions and fintech companies. [Apply]
4. **Compare** the competitive advantages and disadvantages of incumbent banks vs. fintech startups across key service dimensions. [Analyze]
5. **Evaluate** which collaboration model (partnership, acquisition, white-label, open banking) best fits a given strategic scenario. [Evaluate]

### Notation Table
No Greek letters (MSc audience but finance/business focus, not quantitative). All concepts described in plain English. Terminology:
- Fintech = Financial Technology
- Incumbent = Traditional financial institution (bank, insurer, asset manager)
- Neobank = Digital-only bank with no physical branches
- Open banking = Regulatory framework mandating API access to bank data
- Embedded finance = Financial services integrated into non-financial platforms

### Frame-by-Frame Specification

#### WHY Section (Frames 1-4): Opening and Motivation

**Frame 1: Title Page** [FIXED]
- Layout: `\titlepage`
- Title: "Fintech Foundations and Overview"
- Subtitle: "Understanding the Revolution in Financial Services"
- Author: Joerg Osterrieder
- Course: Financial Technology (FinTech) -- MSc Course

**Frame 2: Opening Cartoon** [FIXED]
- Layout: Full-width image
- Chart ref: `figures/11_opening_cartoon/cartoon.pdf`
- Content: XKCD-style cartoon showing a traditional banker looking at their phone showing a sleek fintech app. Thought bubble: "They built in a weekend what took us 20 years?" A smaller figure with a laptop (fintech founder) responds: "And no branch offices needed!"
- Punchline: "The revolution started in a garage, not a boardroom."
- Bottomnote: "This is the tension at the heart of fintech: speed vs. scale, innovation vs. regulation."

**Frame 3: Learning Objectives** [FIXED]
- Layout: Full-width enumerate
- Content: 5 learning objectives with Bloom's levels (listed above)
- Closing line: `\textcolor{mlpurple}{\textbf{Bloom's levels covered:}} Understand, Apply, Analyze, Evaluate`
- Bottomnote: "These objectives map directly to quiz and exercise assessments."

**Frame 4: Bridge/Welcome** [Content-variable]
- Layout: Two-column (text 0.55 + chart 0.42)
- Chart ref: `figures/04_fintech_ecosystem_overview/chart.pdf`
- Left column: "Welcome to Financial Technology. This course examines how technology is transforming every corner of financial services -- from payments and lending to insurance and wealth management. This first lecture establishes the foundation: what fintech IS, where it came from, and where it is going."
- Right column: Ecosystem overview chart showing the fintech landscape
- Bottomnote: "By the end of this lecture you will have a framework for understanding every topic in the rest of the course."

#### FEEL Section (Frame 5): Personal Connection

**Frame 5: The Fintech in Your Pocket**
- Layout: Full-width text with prompt
- Content: "Think about the last 48 hours. How many financial transactions did you make? How many involved a traditional bank branch? Now open your phone -- how many apps touch your money? Banking, payments, investment, insurance? Each one is a fintech story."
- Exampleblock: "Quick Exercise: Count the financial apps on your phone. For each, ask: Is this from a traditional bank, a fintech startup, or a big tech company? Bring your count to the discussion."
- Bottomnote: "Most MSc students have 5-10 financial apps -- and most are NOT from their bank."

#### WHAT Section (Frames 6-9): Foundational Concepts

**Frame 6: What Is Fintech? Definitions Across Perspectives**
- Layout: Two-column (table 0.55 + elaboration 0.42)
- Left: Comparison table with 4 rows:
  | Perspective | Definition Focus |
  | Academic | Technology-enabled financial innovation |
  | Industry | Companies using tech to improve financial services |
  | Regulatory | New entrants requiring new oversight frameworks |
  | Consumer | Faster, cheaper, more accessible financial products |
- Right: "Notice: every definition emphasizes a different stakeholder. Academics see innovation. Industry sees competition. Regulators see risk. Consumers see convenience. Fintech is all four simultaneously."
- Block: "Fintech is not a product -- it is a force that reshapes how financial services are created, delivered, and consumed."
- Bottomnote: "The term 'fintech' was first used in the early 1990s but gained mainstream adoption after 2010."

**Frame 7: The Scope of Fintech -- Seven Verticals**
- Layout: Full-width itemize
- Content: Seven fintech verticals, each with one-line description:
  1. Payments (mobile wallets, real-time transfers, cross-border)
  2. Lending (peer-to-peer, alternative credit scoring, BNPL)
  3. Insurance -- Insurtech (on-demand, parametric, automated claims)
  4. Wealth Management (robo-advisors, micro-investing, social trading)
  5. Capital Markets (algorithmic trading, tokenization, crowdfunding)
  6. RegTech (compliance automation, identity verification, transaction monitoring)
  7. Banking Infrastructure (neobanks, BaaS, open banking APIs)
- Block: "Each vertical is a lecture in this course. Today we see the forest; later we examine each tree."
- Bottomnote: "Lectures 3-7 each deep-dive into one or more of these verticals."

**Frame 8: From Abacus to Algorithm -- A Timeline of Financial Innovation**
- Layout: Chart + 3 interpretation bullets
- Chart ref: `figures/01_fintech_evolution_timeline/chart.pdf`
- Bullets:
  1. "What you see: A timeline from the 1950s to the 2020s showing major fintech milestones -- credit cards, ATMs, online banking, mobile payments, blockchain, embedded finance."
  2. "Key pattern: Notice how the pace of innovation accelerates. The gap between credit cards (1950s) and ATMs (1960s) was a decade. The gap between mobile payments and blockchain was just years."
  3. "Takeaway: Each wave builds on the infrastructure of the previous one. Today's innovations stand on decades of accumulated technology."
- Bottomnote: "The timeline is illustrative. Exact dates vary by region -- ATMs arrived in the US in 1969 but in many developing countries decades later."

**Frame 9: Traditional Banking vs. Fintech -- What Changed?**
- Layout: Chart + interpretation
- Chart ref: `figures/02_banking_value_chain_disruption/chart.pdf`
- Content: Flowchart showing the traditional banking value chain (origination, distribution, servicing, risk management) and how fintech companies have unbundled each component
- Bullets:
  1. "What you see: The traditional bank as a vertically integrated institution vs. specialized fintech companies attacking each layer."
  2. "Key pattern: Fintech does not replace the bank. It unbundles it -- each startup attacks the most profitable or most inefficient piece."
  3. "Takeaway: The question is not 'Will banks disappear?' but 'Which parts of banking can survive unbundling?'"
- Bottomnote: "This unbundling-rebundling cycle is the central dynamic of fintech disruption. See L02 for ecosystem analysis."

#### CASE Section (Frames 10-13): The Great Recession Catalyst

**Frame 10: Before 2008 -- The Trust Assumption**
- Layout: Two-column (text + items)
- Content: Description of pre-2008 banking: high trust in institutions, limited alternatives, regulatory frameworks designed for incumbents, innovation happening inside banks (not outside)
- Items: "Banks were the only game in town. Consumers trusted them by default. Regulation protected them from competition. Innovation meant a new savings product, not a new business model."
- Block: "Trust in banks was not earned -- it was assumed. The crisis exposed the assumption."
- Bottomnote: "In 2007, over 80% of consumers in developed markets expressed high trust in their primary bank."

**Frame 11: The 2008 Crisis -- Trust Collapses**
- Layout: Chart + 3 bullets
- Chart ref: `figures/05_great_recession_catalyst/chart.pdf`
- Content: Conceptual diagram showing the causal chain: housing bubble -> bank failures -> bailouts -> consumer trust erosion -> regulatory response -> space for alternatives
- Bullets:
  1. "What you see: A causal chain from the housing bubble to the opening of space for fintech entrants."
  2. "Key pattern: Each step in the chain reduced a barrier to fintech entry. Trust erosion created demand. Regulatory response created opportunity. Unemployment created talent supply."
  3. "Takeaway: The 2008 crisis did not cause fintech, but it removed the barriers that had been holding it back for decades."
- Bottomnote: "By 2010, trust in banks had fallen to historic lows in the US, UK, and Eurozone."

**Frame 12: Three Forces That Opened the Door**
- Layout: Three-column split
- Column 1: "Demand Shift" -- Consumers, especially millennials, sought alternatives to banks they no longer trusted. Digital-native expectations (speed, transparency, mobile-first).
- Column 2: "Regulatory Response" -- Post-crisis regulation (Dodd-Frank, PSD2, Open Banking) inadvertently created space for non-bank competitors. Regulatory sandboxes invited startups.
- Column 3: "Technology + Talent" -- Cloud computing reduced infrastructure costs. Smartphones created distribution channels. Laid-off bankers became fintech founders.
- Block: "Fintech needed all three forces simultaneously. Technology alone was not enough -- it needed demand and regulatory permission."
- Bottomnote: "The smartphone was necessary but not sufficient. The crisis provided the push; the technology provided the path."

**Frame 13: Post-Crisis Fintech Boom -- The Numbers**
- Layout: Chart + items
- Chart ref: `figures/06_fintech_investment_growth/chart.pdf`
- Content: Conceptual bar chart showing illustrative growth in global fintech investment from 2010 to 2023 (labeled "Illustrative Growth Trend")
- Items: "After 2010, venture capital flooded into fintech. Initial investments were small (seed/Series A); by 2020, fintech companies were raising billions. The pandemic in 2020 further accelerated digital adoption."
- Bottomnote: "Investment data is illustrative of the growth trajectory. Actual figures vary by source and definition of 'fintech'."

#### HOW Section (Frames 14-17): Collaboration Models

**Frame 14: The Collaboration Spectrum -- From Competition to Partnership**
- Layout: Chart + 3 bullets
- Chart ref: `figures/03_collaboration_models_matrix/chart.pdf`
- Content: Comparison matrix showing four collaboration models (Partnership, Acquisition, White-Label, Open Banking) across dimensions: control, speed, cost, innovation, risk
- Bullets:
  1. "What you see: Four distinct models for how banks and fintechs work together, scored across five dimensions."
  2. "Key pattern: No single model dominates. Partnerships offer speed but less control. Acquisitions offer control but are expensive and slow."
  3. "Takeaway: The 'right' model depends on the bank's strategic priorities and the fintech's maturity."
- Bottomnote: "Most large banks use multiple models simultaneously -- partnering in payments, acquiring in lending, building white-label for compliance."

**Frame 15: Partnership Model -- How It Works**
- Layout: Chart + text
- Chart ref: `figures/07_bank_fintech_partnership_flow/chart.pdf`
- Content: Flowchart showing a typical bank-fintech partnership: bank provides license + customer base + capital; fintech provides technology + user experience + speed. Joint product goes to market.
- Text: "Partnerships are the most common model. The bank brings what it has (license, trust, capital). The fintech brings what it does better (technology, speed, design). The product combines both."
- Block: "A partnership succeeds when each party contributes something the other cannot build faster alone."
- Bottomnote: "Examples include Goldman Sachs + Apple (Apple Card), JPMorgan + OnDeck (small business lending), BBVA + Atom Bank."

**Frame 16: Acquisition and White-Label -- Two More Paths**
- Layout: Two-column comparison
- Left: "Acquisition" -- Bank buys fintech outright. Gains technology and talent. Risk: culture clash kills innovation. The acquired team leaves. Example pattern: large bank buys Series B fintech for technology stack.
- Right: "White-Label" -- Fintech builds infrastructure; bank puts its brand on top. Banking-as-a-Service (BaaS). The fintech is invisible to the consumer. Example pattern: neobank runs on a licensed bank's infrastructure.
- Block: "Acquisition buys the past. White-label rents the present. Partnership builds the future."
- Bottomnote: "White-label and BaaS are growing fastest. They let banks innovate without building, and fintechs scale without a banking license."

**Frame 17: Open Banking -- The Regulatory Path**
- Layout: Two-column (text + architecture diagram)
- Left: Explanation of open banking: regulatory mandate (PSD2 in EU, similar in UK, Australia, Brazil) requiring banks to share customer data via APIs with authorized third parties. Creates a level playing field by turning bank data from a moat into a shared resource.
- Right: Simple architecture diagram showing: Consumer -> consents -> Bank (data holder) -> API -> Fintech App (data consumer) -> enriched service back to Consumer
- Block: "Open banking turns the bank's greatest asset -- customer data -- into a shared resource. The bank that adapts fastest wins."
- Bottomnote: "PSD2 (EU, 2018) was the first major open banking mandate. The UK's Open Banking Standard, Brazil's PIX, and India's Account Aggregator followed."

#### RISK Section (Frames 18-20): What Can Go Wrong

**Frame 18: When Fintech Fails -- Common Failure Modes**
- Layout: Full-width itemize with categories
- Content: Four failure categories:
  1. "Regulatory risk" -- Operating without adequate licenses; crossing jurisdictional boundaries
  2. "Trust risk" -- Data breaches; lack of deposit insurance; unclear complaint resolution
  3. "Scalability risk" -- Customer acquisition costs exceed lifetime value; unit economics never work
  4. "Systemic risk" -- Fintech becomes "too connected to fail"; concentration in cloud providers
- Block: "Fintech disruption is not risk-free. The question is whether fintech creates new risks or merely redistributes old ones."
- Bottomnote: "See L04 (RegTech) for detailed analysis of regulatory failure modes."

**Frame 19: The Consumer Protection Challenge**
- Layout: Two-column (text + items)
- Left: "Traditional banks are regulated, insured, and supervised. Fintech companies often operate in regulatory gaps -- between banking law and technology law, between national jurisdictions."
- Right: Key consumer protection concerns: deposit insurance gaps, data privacy vulnerabilities, algorithmic bias in lending, cross-border enforcement difficulties
- Block: "Innovation without consumer protection is not progress -- it is risk transfer from institutions to individuals."
- Bottomnote: "This tension between innovation and protection is the central theme of L04 (Fintech Security and Regulation)."

**Frame 20: Cybersecurity and Operational Risk**
- Layout: Two-column (risk table + text)
- Left: Table of operational risks:
  | Risk Type | Traditional Bank | Fintech |
  | Data breach | Internal systems | Cloud + API surface |
  | System outage | Redundant infrastructure | Single cloud provider |
  | Fraud | Known patterns | Novel attack vectors |
  | Compliance | Established frameworks | Evolving requirements |
- Right: "Fintech companies often have larger attack surfaces (more APIs, more cloud dependencies, more third-party integrations) but smaller security teams. The trade-off is speed-to-market vs. security-in-depth."
- Bottomnote: "L07 (Technology of FinTech) covers identity, encryption, and cybersecurity in depth."

#### WHERE Section (Frames 21-23): Evidence at Scale

**Frame 21: Fintech Around the World -- Regional Patterns**
- Layout: Chart + items
- Chart ref: `figures/09_fintech_impact_comparison/chart.pdf`
- Content: Conceptual comparison bar chart showing fintech adoption/penetration across regions (North America, Europe, Asia-Pacific, Africa/Middle East, Latin America) across dimensions like mobile payments, digital lending, neobank penetration
- Bullets:
  1. "What you see: Fintech adoption varies dramatically by region, with Asia-Pacific and Africa leading in mobile payments, while North America and Europe lead in digital lending and wealth management."
  2. "Key pattern: Regions with weaker traditional banking infrastructure often leapfrog to fintech solutions -- the 'leapfrog effect.'"
  3. "Takeaway: Fintech is not a Western phenomenon. The most transformative fintech innovations (M-Pesa, Alipay, PIX) emerged outside the US and Europe."
- Bottomnote: "Data is illustrative of broad adoption patterns. Actual metrics depend on the definition and measurement methodology."

**Frame 22: Key Trends Reshaping Fintech**
- Layout: Full-width itemize
- Content: Five major trends:
  1. "Embedded finance" -- Financial services integrated into non-financial platforms (ride-sharing with payments, e-commerce with lending, social media with tipping)
  2. "Neobanks" -- Digital-only banks challenging incumbents on user experience and fees
  3. "Decentralized finance (DeFi)" -- Financial services built on blockchain, removing intermediaries
  4. "Super-apps" -- Single platforms combining messaging, payments, shopping, banking (WeChat, Grab, Gojek)
  5. "Sustainable fintech" -- Green bonds, ESG scoring, carbon-tracking financial products
- Block: "Each of these trends is both an opportunity and a threat. The winners will be those who combine innovation with trust."
- Bottomnote: "Lectures 3-7 examine these trends in depth. Today we establish the landscape."

**Frame 23: The Future of Banking -- Three Scenarios**
- Layout: Three-column split
- Column 1: "Banks Win" -- Incumbents absorb fintech capabilities through acquisition and internal innovation. Regulation protects their position. Result: banks look different but remain dominant.
- Column 2: "Fintech Wins" -- Startups capture enough market share to become the new incumbents. Big tech enters financial services. Banks become utilities (infrastructure, not customer-facing).
- Column 3: "Coexistence" -- Banks and fintechs specialize. Banks handle regulated activities (deposits, lending); fintechs handle customer experience and innovation. Open banking APIs connect them.
- Block: "The most likely outcome is coexistence -- but which specific segments go to banks vs. fintechs will define the next decade of finance."
- Bottomnote: "This question recurs throughout the course. Each lecture adds evidence for one scenario or another."

#### IMPACT Section (Frames 24-25): Who Wins, Who Loses

**Frame 24: Stakeholder Impact Analysis**
- Layout: Chart + items
- Chart ref: `figures/08_embedded_finance_architecture/chart.pdf` (or use a stakeholder map)
- Content: Stakeholder analysis showing how fintech affects: consumers (more choice, lower fees, but less protection), banks (competitive pressure, forced innovation, potential disintermediation), regulators (new oversight challenges, innovation vs. stability trade-off), fintech companies (growth opportunity, but funding cycles and regulatory uncertainty), society (financial inclusion gains, but digital divide risks)
- Block: "Fintech is not zero-sum. Both consumers and institutions can benefit -- but the benefits are not evenly distributed."
- Bottomnote: "Financial inclusion -- serving the unbanked and underbanked -- is examined in detail in L02 (Fintech Ecosystem)."

**Frame 25: The Financial Inclusion Promise**
- Layout: Two-column (text + items)
- Content: How fintech enables financial inclusion: mobile money serving unbanked populations, alternative credit scoring using non-traditional data, micro-investing lowering entry barriers, cross-border remittance cost reduction
- Items: "Over 1.7 billion adults globally lack access to formal financial services. Fintech's greatest promise is reaching them -- not through branches, but through smartphones."
- Block: "If fintech only serves the already-served, it is optimization, not transformation. Inclusion is the test of genuine impact."
- Bottomnote: "M-Pesa (Kenya, 2007) remains the canonical example. See L02 for the full financial inclusion discussion."

#### SO WHAT Section (Frames 26-27): Synthesis and Evaluation

**Frame 26: Five Questions That Reveal Any Fintech's True Strategy**
- Layout: Two-column (numbered list 0.55 + metaphor visual 0.42)
- Left: Evaluation framework:
  1. "Who is the customer?" -- Consumer, SME, enterprise, or another fintech?
  2. "What part of the value chain does it attack?" -- Origination, distribution, servicing, or infrastructure?
  3. "How does it make money?" -- Transaction fees, subscription, data monetization, or float?
  4. "What is its regulatory position?" -- Licensed, partnered, or operating in a gap?
  5. "Does it create or capture value?" -- Building new markets or taking share from incumbents?
- Right: Conceptual visual -- a funnel or evaluation flowchart
- Block: "These five questions work for any fintech company you encounter -- in this course, in the news, or in your career."
- Bottomnote: "Apply these questions to a fintech you use. You will use this framework in the Workshop C evaluation exercise on Day 5."

**Frame 27: The Central Tension Revisited**
- Layout: Full-width text
- Content: Return to the core tension: "Technology is reshaping finance -- but the outcome depends on design choices. Will fintech replace institutions or strengthen them? Will it include the excluded or serve only the already-served? Will it create resilience or fragility? These are not technology questions -- they are governance, regulation, and strategy questions. This course gives you the tools to answer them."
- Block: "Fintech is not a technology story. It is a governance story told in the language of technology."
- Bottomnote: "This course covers: Ecosystem (L02), Payments (L03), Regulation (L04), Wealth Management (L05), Insurance (L06), and Technology (L07)."

#### ACT Section (Frame 28): Forward Look

**Frame 28: What Comes Next**
- Layout: Full-width items
- Content: Preview of remaining course:
  - "Next: L02 (Fintech Ecosystem) -- growth drivers, financial inclusion, trust, and behavioral dimensions"
  - "This afternoon: L02 begins at 11:30 after the break"
  - "Before L02, think about: What fintech services do you trust MORE than your bank? Why?"
- Block: "The rest of this course fills in the detail. Today you have the map. Starting with L02, we explore each territory."
- Bottomnote: "If you want to read ahead, the course website has all lecture slides and materials available for download."

#### CLOSING SEQUENCE (Frames 29-31): Fixed Structure

**Frame 29: Closing Cartoon** [FIXED]
- Layout: Full-width image
- Chart ref: `figures/12_closing_cartoon/cartoon.pdf`
- Content: XKCD-style cartoon showing a traditional banker and a fintech founder shaking hands, both looking slightly suspicious. The banker thinks: "I need their tech." The founder thinks: "I need their license." Below: "And that's how partnerships are born."
- Bottomnote: "The collaboration imperative is the most important take-away from this lecture. Neither side can win alone."

**Frame 30: Key Takeaways** [FIXED]
- Layout: Numbered enumerate (7 items)
- Content:
  1. "Fintech defined: Technology-enabled innovation that creates new financial products, processes, or business models."
  2. "Historical arc: From credit cards (1950s) through online banking (1990s) to embedded finance (2020s) -- each wave built on the last."
  3. "Crisis catalyst: The 2008 financial crisis eroded trust, opened regulatory space, and released talent -- creating the conditions for fintech's explosive growth."
  4. "Unbundling: Fintech companies attack specific layers of the banking value chain, not the entire bank."
  5. "Collaboration spectrum: Banks and fintechs interact through partnership, acquisition, white-label, and open banking -- each with distinct trade-offs."
  6. "Global variation: Fintech adoption is highest where traditional banking infrastructure is weakest (the leapfrog effect)."
  7. "Evaluation tool: Five questions (customer, value chain, revenue model, regulatory position, value creation) reveal any fintech's true strategy."
- Bottomnote: "Review question: Which collaboration model would you recommend for a mid-sized European bank entering mobile payments? Why?"

**Frame 31: Summary / Next Lesson** [FIXED]
- Layout: Summary + multicol vocabulary
- Summary: "Fintech is the application of technology to financial services, driven by the convergence of eroded trust, enabling technology, and regulatory change after 2008. Traditional banks and fintech companies are increasingly choosing collaboration over competition, through models ranging from partnerships to open banking APIs. The key question is not whether fintech will transform finance, but how the benefits and risks will be distributed across stakeholders."
- Key Vocabulary (two-column):
  - Fintech
  - Neobank
  - Open Banking
  - Embedded Finance
  - Unbundling
  - Banking-as-a-Service (BaaS)
  - RegTech
  - Financial Inclusion
- Next lesson: "Lecture 2: Fintech Ecosystem -- Growth drivers, financial inclusion, trust in fintech, and how behavioral economics shapes digital financial products."
- Bottomnote: "L02 begins this afternoon at 11:30. Bring your phone app count from the exercise in slide 5."

---

## Part 2: Six .tex Variant Specifications

### Variant 1: Full (~31 slides)
- **File:** `L01_full.tex`
- **Generator:** `full-lecture-generator` skill
- **Preamble:** `\input{../../_shared/preamble.tex}` (shared)
- **Frame count:** 31 (range 29-33 acceptable)
- **Sections:** WHY(4) + FEEL(1) + WHAT(4) + CASE(4) + HOW(4) + RISK(3) + WHERE(3) + IMPACT(2) + SOWHAT(2) + ACT(1) + Closing(3) = 31
- **Charts:** 10 content charts + 2 cartoons = 12 `\includegraphics`
- **Content:** Complete slide-by-slide spec from Part 1 above
- **Section markers:** Comment-block markers (`% === FOUNDATIONAL CONCEPTS ===`), NOT `\section{}` commands
- **Speaker notes guidance:** Each `\bottomnote{}` serves as the instructor note

### Variant 2: Overview (~25-30 slides)
- **File:** `L01_overview.tex`
- **Generator:** `beamer-slide-creator` (three-zone: INTRO/CORE/CLOSING)
- **Preamble:** `\input{../../_shared/preamble.tex}` (shared)
- **Frame count:** ~25-28
- **Section framework:** PMSP (Problem-Method-Solution-Practice)
- **Content focus:** Accessible, visual, problem-first. Same content as full but with lighter treatment of RISK and more visual emphasis. Omit the detailed partnership flowchart (frame 15) and the three-scenario slide (frame 23). Consolidate CASE into 3 frames.
- **Charts:** Same figure directory; references subset of the 12 charts
- **Distinct from full:** Uses `\section{}` commands (not comment-block markers). Three-zone architecture with explicit INTRO/CORE/CLOSING zones.

### Variant 3: Deep Dive (~17 slides)
- **File:** `L01_deepdive.tex`
- **Generator:** `beamer-slide-creator` (MAIN BODY + `\appendix`)
- **Preamble:** `\input{../../_shared/preamble.tex}` (shared)
- **Frame count:** ~15-18
- **Content focus:** Advanced/analytical depth. Deeper treatment of:
  - Collaboration model economics (when does each model create vs. destroy value?)
  - Regulatory theory behind open banking mandates
  - Fintech valuation frameworks and unit economics
  - Historical parallels (previous waves of financial innovation -- telegraph, telephone, internet)
  - Appendix: Academic definitions debate, further reading
- **Uses:** `\section*{}` after `\appendix`
- **Charts:** Subset of the 12 charts plus any deepdive-specific ones from the same figure directory

### Variant 4: Core (~10 slides)
- **File:** `L01_core.tex`
- **Generator:** Frame-index extraction from full variant (mechanical, not AI-generated)
- **Preamble:** Self-contained (inline, no `\input` commands)
- **Frame count:** 10
- **Extraction algorithm:** Title + first frame from each of 8 arc sections + Key Takeaways
  - Frame 1 (title)
  - Frame 4 (WHY: Bridge/Welcome)
  - Frame 6 (WHAT: Definitions)
  - Frame 10 (CASE: Before 2008)
  - Frame 14 (HOW: Collaboration Spectrum)
  - Frame 18 (RISK: Failure Modes)
  - Frame 21 (WHERE: Regional Patterns)
  - Frame 24 (IMPACT: Stakeholder Analysis)
  - Frame 26 (SOWHAT: Five Questions)
  - Frame 30 (Key Takeaways)
- **Content:** Extracted verbatim from full variant

### Variant 5: Mini-10 (10 slides)
- **File:** `L01_mini10.tex`
- **Generator:** `mini-lecture-generator` (10-slide arc)
- **Preamble:** Self-contained (inline, no `\input` commands)
- **Frame count:** 10
- **Arc:** WHY > FEEL > WHAT > CASE > HOW > RISK > WHERE > IMPACT > SO WHAT > ACT
- **Core tension:** Same as full variant
- **Visual types (one per slide, no repeats):**
  1. WHY: TikZ comic (banker vs. fintech founder dilemma)
  2. FEEL: Text-only prompt (phone app exercise)
  3. WHAT: Comparison table (bank vs. fintech across dimensions)
  4. CASE: Step diagram (2008 crisis causal chain)
  5. HOW: Architecture diagram (four collaboration models side-by-side)
  6. RISK: TikZ comic (fintech failure scene)
  7. WHERE: pgfplots bar chart (regional adoption patterns)
  8. IMPACT: Stakeholder map (winners/losers)
  9. SO WHAT: Balance scale (innovation vs. regulation)
  10. ACT: Activity frame (evaluate a fintech using the 5-question framework)
- **All visuals inline TikZ/pgfplots (no external charts)**
- **No `\includegraphics`, no `\input{}`**

### Variant 6: Mini-5 (5 slides, teaser)
- **File:** `L01_mini5.tex`
- **Generator:** `mini-lecture-generator` (5-slide teaser arc)
- **Preamble:** Self-contained (inline, no `\input` commands)
- **Frame count:** 5
- **Arc:** WHY > WHAT > HOW > WHERE > SO WHAT
- **Core tension:** Same as full variant
- **Visual types:**
  1. WHY: TikZ comic (traditional banker facing app disruption)
  2. WHAT: Comparison table (what makes fintech different from traditional banking)
  3. HOW: Architecture diagram (bank-fintech collaboration models)
  4. WHERE: pgfplots chart (illustrative global fintech adoption)
  5. SO WHAT: Balance scale metaphor (innovation + inclusion vs. risk + regulation)
- **All visuals inline TikZ/pgfplots**
- **No `\includegraphics`, no `\input{}`**

---

## Part 3: Chart/Diagram Specifications (12 figures)

All charts use conceptual/illustrative data only. No real market data.

### Figure 01: Fintech Evolution Timeline
- **Directory:** `figures/01_fintech_evolution_timeline/`
- **Type:** Time series / annotated timeline
- **Title:** "Evolution of Financial Technology: 1950s -- 2020s"
- **Data/labels:**
  - 1950s: Credit cards
  - 1960s: ATMs
  - 1970s: Electronic trading (NASDAQ)
  - 1980s: Online banking experiments
  - 1990s: Internet banking, PayPal
  - 2000s: Mobile banking, P2P lending
  - 2007: M-Pesa (mobile money, Kenya)
  - 2008: Financial crisis (inflection point, highlighted)
  - 2009: Bitcoin
  - 2010s: Neobanks, robo-advisors, BNPL
  - 2018: PSD2 / Open Banking
  - 2020s: Embedded finance, DeFi, super-apps
- **Implementation:** `matplotlib` with `ax.plot()` creating a stepped timeline. Key events as annotated points. The 2008 crisis highlighted with a red vertical band. Use `V4_COLORS['MLPURPLE']` for the main timeline, `V4_COLORS['MLRED']` for the crisis zone, `V4_COLORS['MLGREEN']` for post-crisis acceleration zone. `figsize=(10,6)`. Horizontal layout with time on x-axis and "Impact/Adoption" on y-axis as a conceptual S-curve with milestones annotated.
- **CHART_METADATA:** `{title: "Fintech Evolution Timeline", type: "time_series", section: "WHAT", lecture_number: 1}`

### Figure 02: Banking Value Chain Disruption
- **Directory:** `figures/02_banking_value_chain_disruption/`
- **Type:** Flowchart / comparison diagram
- **Title:** "Traditional Banking Value Chain vs. Fintech Unbundling"
- **Data/labels:**
  - Top row: Traditional Bank as single integrated entity spanning: Origination > Distribution > Servicing > Risk Management > Infrastructure
  - Bottom row: Specialized fintechs attacking each layer: "Lending platforms" (origination), "Neobanks" (distribution), "Robo-advisors" (servicing), "RegTech" (risk management), "BaaS providers" (infrastructure)
  - Arrows showing the unbundling flow
- **Implementation:** `matplotlib.patches.FancyBboxPatch` + arrows. Top row is one large purple box. Bottom row is 5 smaller colored boxes. Downward arrows show the unbundling. Use `V4_COLORS` palette. `figsize=(10,6)`, `ax.axis('off')`.
- **CHART_METADATA:** `{title: "Banking Value Chain Disruption", type: "flowchart", section: "WHAT", lecture_number: 1}`

### Figure 03: Collaboration Models Matrix
- **Directory:** `figures/03_collaboration_models_matrix/`
- **Type:** Comparison bar chart / grouped horizontal bar
- **Title:** "Bank-Fintech Collaboration Models: Comparative Analysis"
- **Data/labels:** Four models (Partnership, Acquisition, White-Label, Open Banking) rated on 5 dimensions (Control, Speed-to-Market, Cost, Innovation Potential, Risk) on a 1-5 conceptual scale
- **Implementation:** Grouped horizontal bar chart. Each model is a group of 5 bars. Use `V4_COLORS` for each dimension. Legend at bottom. Synthetic ratings (illustrative). `np.random.seed(42)` not needed (fixed illustrative data). `figsize=(10,6)`.
- **CHART_METADATA:** `{title: "Collaboration Models Comparison", type: "comparison_bar", section: "HOW", lecture_number: 1}`

### Figure 04: Fintech Ecosystem Overview
- **Directory:** `figures/04_fintech_ecosystem_overview/`
- **Type:** Architecture / ecosystem diagram
- **Title:** "The Fintech Ecosystem: Key Players and Relationships"
- **Data/labels:** Central hub "Financial Services" surrounded by 7 nodes: Payments, Lending, Insurance, Wealth Management, Capital Markets, RegTech, Banking Infrastructure. Outer ring: Regulators, Consumers, Investors, Technology Providers, Incumbents
- **Implementation:** `matplotlib.patches` with circles and arrows. Central node in `MLPURPLE`, inner ring in various `V4_COLORS`, outer ring in `MLGRAY`. Connecting lines show relationships. `figsize=(10,6)`, `ax.axis('off')`.
- **CHART_METADATA:** `{title: "Fintech Ecosystem Overview", type: "diagram", section: "WHY", lecture_number: 1}`

### Figure 05: Great Recession as Catalyst
- **Directory:** `figures/05_great_recession_catalyst/`
- **Type:** Flowchart / causal chain
- **Title:** "The 2008 Crisis: A Catalyst for Fintech Innovation"
- **Data/labels:** Sequential chain: Housing Bubble -> Bank Failures -> Government Bailouts -> Consumer Trust Erosion -> Regulatory Response (Dodd-Frank, PSD2) -> [Three parallel outputs:] Demand for Alternatives + Regulatory Space + Available Talent -> Fintech Boom
- **Implementation:** `matplotlib.patches.FancyBboxPatch` with arrows between boxes. Sequential left-to-right flow. Crisis events in `MLRED`, regulatory response in `MLORANGE`, fintech outcomes in `MLGREEN`. `figsize=(10,6)`, `ax.axis('off')`.
- **CHART_METADATA:** `{title: "Great Recession Catalyst Chain", type: "flowchart", section: "CASE", lecture_number: 1}`

### Figure 06: Fintech Investment Growth
- **Directory:** `figures/06_fintech_investment_growth/`
- **Type:** Bar chart (conceptual/illustrative)
- **Title:** "Illustrative Global Fintech Investment Growth (2010--2023)"
- **Data/labels:** Conceptual bar chart with years 2010-2023 on x-axis, "Illustrative Investment Index" on y-axis. Shows exponential growth pattern: low bars 2010-2013, moderate 2014-2017, high 2018-2019, dip 2020, spike 2021, correction 2022-2023
- **Implementation:** `ax.bar()` with gradient coloring (lighter for earlier years, darker for later). Annotated zones: "Early stage" (2010-2013), "Growth" (2014-2017), "Boom" (2018-2021), "Correction" (2022-2023). Subtitle: "Illustrative -- not actual investment data". Use `V4_COLORS['MLPURPLE']`. `figsize=(10,6)`.
- **CHART_METADATA:** `{title: "Fintech Investment Growth (Illustrative)", type: "comparison_bar", section: "CASE", lecture_number: 1}`

### Figure 07: Bank-Fintech Partnership Flow
- **Directory:** `figures/07_bank_fintech_partnership_flow/`
- **Type:** Flowchart / process diagram
- **Title:** "How a Bank-Fintech Partnership Works"
- **Data/labels:** Three-layer flow:
  - Left: Bank (provides: banking license, customer base, capital, compliance)
  - Center: Joint Product (combined offering reaching the market)
  - Right: Fintech (provides: technology platform, UX design, speed, innovation)
  - Arrows from both sides into the center product
  - Bottom: Consumer receives the combined product
- **Implementation:** `FancyBboxPatch` boxes + arrows. Bank in `MLPURPLE`, Fintech in `MLORANGE`, Joint Product in `MLGREEN`, Consumer in `MLBLUE`. `figsize=(10,6)`, `ax.axis('off')`.
- **CHART_METADATA:** `{title: "Bank-Fintech Partnership Flow", type: "flowchart", section: "HOW", lecture_number: 1}`

### Figure 08: Embedded Finance Architecture
- **Directory:** `figures/08_embedded_finance_architecture/`
- **Type:** Architecture / layered diagram
- **Title:** "Embedded Finance: Financial Services Inside Non-Financial Platforms"
- **Data/labels:** Three-layer architecture:
  - Top: Consumer-facing platforms (ride-sharing, e-commerce, social media)
  - Middle: Embedded financial services layer (payments, lending, insurance) via APIs
  - Bottom: Licensed financial infrastructure (banks, payment networks, insurance companies)
  - Vertical arrows showing API connections between layers
- **Implementation:** `FancyBboxPatch` layered boxes. Top layer in `MLORANGE`, middle in `MLPURPLE`, bottom in `MLBLUE`. API connections as dashed arrows. `figsize=(10,6)`, `ax.axis('off')`.
- **CHART_METADATA:** `{title: "Embedded Finance Architecture", type: "diagram", section: "WHERE", lecture_number: 1}`

### Figure 09: Fintech Impact Comparison by Region
- **Directory:** `figures/09_fintech_impact_comparison/`
- **Type:** Grouped bar chart
- **Title:** "Illustrative Fintech Adoption by Region and Category"
- **Data/labels:** 5 regions (North America, Europe, Asia-Pacific, Africa/ME, Latin America) x 4 categories (Mobile Payments, Digital Lending, Neobanks, InsurTech). Conceptual adoption scores (1-10 scale, illustrative).
- **Implementation:** Grouped bar chart using `ax.bar()` with offset positions. Each category a different `V4_COLORS` color. Legend and axis labels. Subtitle: "Conceptual adoption levels -- illustrative comparison". `figsize=(10,6)`.
- **CHART_METADATA:** `{title: "Fintech Adoption by Region (Illustrative)", type: "comparison_bar", section: "WHERE", lecture_number: 1}`

### Figure 10: Key Concepts Summary Table
- **Directory:** `figures/10_key_concepts_summary/`
- **Type:** Summary table / visual reference
- **Title:** "Lecture 1: Key Concepts at a Glance"
- **Data/labels:** 2-column visual summary: Left column lists 7 key concepts (Fintech Definition, Historical Evolution, Crisis Catalyst, Value Chain Unbundling, Collaboration Models, Global Patterns, Evaluation Framework). Right column provides one-sentence summary for each.
- **Implementation:** `ax.table()` or manual `ax.text()` placement creating a clean summary reference card. Purple header row, alternating row backgrounds. `figsize=(10,6)`, `ax.axis('off')`.
- **CHART_METADATA:** `{title: "Key Concepts Summary", type: "summary_table", section: "SOWHAT", lecture_number: 1}`

### Figure 11: Opening Cartoon
- **Directory:** `figures/11_opening_cartoon/`
- **File:** `cartoon.py` + `cartoon.pdf`
- **Type:** XKCD-style cartoon
- **Title:** "The Fintech Disruption"
- **Scene:** Traditional banker in suit (left) staring at smartphone showing sleek app. Fintech founder in t-shirt (right) with laptop. Banker's thought bubble: "They built this in a weekend?" Founder's thought bubble: "And no branch offices needed!" Below: "The revolution started in a garage, not a boardroom."
- **Implementation:** `plt.xkcd()` context manager. `fig, ax = plt.subplots(figsize=(12,6))`. `ax.axis('off')`. Characters drawn with `ax.annotate()` and `ax.text()`. Speech bubbles with `FancyBboxPatch`. Scene at conceptual positions.
- **CHART_METADATA:** `{title: "Opening Cartoon: Fintech Disruption", type: "cartoon_opening", section: "WHY", lecture_number: 1}`

### Figure 12: Closing Cartoon
- **Directory:** `figures/12_closing_cartoon/`
- **File:** `cartoon.py` + `cartoon.pdf`
- **Type:** XKCD-style cartoon
- **Title:** "The Partnership Imperative"
- **Scene:** Banker and fintech founder shaking hands, both looking slightly suspicious. Banker thinks: "I need their tech." Founder thinks: "I need their license." Below: "And that's how partnerships are born."
- **Implementation:** Same `plt.xkcd()` pattern as opening cartoon. Different scene, emphasizing collaboration over competition.
- **CHART_METADATA:** `{title: "Closing Cartoon: Partnership Imperative", type: "cartoon_closing", section: "CLOSING", lecture_number: 1}`

---

## Part 4: Quiz Specifications

### Standard Quiz (20 MCQ)

**Bloom's Distribution:** Understand(4) + Apply(8) + Analyze(6) + Evaluate(2) = 20

**Question-by-Question Specification:**

**Understand Level (4 questions):**

Q1: "Which of the following best describes fintech?"
- A. Software companies that write code for banks
- B. Technology-enabled innovation creating new financial products, processes, or business models
- C. Digital-only banks that have no physical branches
- D. Government programs to modernize financial regulation
- **Correct: B** -- Fintech encompasses all technology-enabled financial innovation, not just banks or software.

Q2: "What does 'unbundling' mean in the context of fintech disruption?"
- A. Banks selling off their international operations
- B. Specialized companies attacking specific layers of the banking value chain
- C. Fintech companies merging into larger conglomerates
- D. Regulators breaking up large financial institutions
- **Correct: B** -- Unbundling describes how fintech startups target individual banking functions rather than competing across the entire value chain.

Q3: "Which event is most commonly cited as the primary catalyst for the modern fintech boom?"
- A. The dot-com bubble of 2000
- B. The launch of the iPhone in 2007
- C. The 2008 global financial crisis
- D. The introduction of Bitcoin in 2009
- **Correct: C** -- The 2008 crisis eroded consumer trust in banks and created regulatory space for alternatives.

Q4: "What is open banking?"
- A. Banks that operate without physical branches
- B. A regulatory framework requiring banks to share customer data via APIs with authorized third parties
- C. A type of fintech startup that provides free banking services
- D. An industry consortium that sets standards for mobile payments
- **Correct: B** -- Open banking is a regulatory mandate (e.g., PSD2) that requires banks to provide API access to customer data.

**Apply Level (8 questions):**

Q5: "A mid-sized European bank wants to offer a mobile payment solution quickly without building it in-house. Which collaboration model is most appropriate?"
- A. Acquisition of a payment fintech
- B. Partnership with an established mobile payment provider
- C. Building a white-label solution from scratch
- D. Waiting for open banking APIs to provide the functionality
- **Correct: B** -- Partnership provides speed-to-market without the cost and integration complexity of acquisition.

Q6: "A fintech startup has innovative lending algorithms but no banking license. Which collaboration model best fits their situation?"
- A. Acquiring a small bank for its license
- B. Operating without a license in a regulatory sandbox
- C. White-label arrangement where a licensed bank provides the regulatory infrastructure
- D. Lobbying regulators for a new fintech-specific license
- **Correct: C** -- White-label/BaaS lets the fintech leverage a bank's license while focusing on its technology strength.

Q7: "According to the 'five questions' evaluation framework, a fintech that earns revenue by selling user transaction data to advertisers would be classified under which revenue model?"
- A. Transaction fees
- B. Subscription
- C. Data monetization
- D. Interest on float
- **Correct: C** -- Selling user data to third parties is data monetization.

Q8: "If a country has very low bank account penetration but high smartphone ownership, what type of fintech innovation would you predict to emerge first?"
- A. Robo-advisory wealth management
- B. Mobile money and digital payments
- C. Blockchain-based decentralized finance
- D. RegTech compliance solutions
- **Correct: B** -- This describes the leapfrog effect: markets skip traditional banking and go directly to mobile financial services.

Q9: "A neobank offers free current accounts, no-fee international transfers, and instant notifications. Using the value chain framework, which layer of traditional banking is it primarily attacking?"
- A. Origination
- B. Distribution (customer-facing services)
- C. Risk management
- D. Infrastructure
- **Correct: B** -- Neobanks primarily compete on the distribution/customer experience layer of banking.

Q10: "In the banking-as-a-service (BaaS) model, which party holds the banking license?"
- A. The fintech company serving end customers
- B. The infrastructure provider (BaaS platform)
- C. The end customer
- D. The payment network
- **Correct: B** -- In BaaS, the licensed bank provides regulatory infrastructure; the fintech builds the customer-facing product on top.

Q11: "The 2008 financial crisis contributed to fintech growth through three mechanisms. Which of the following is NOT one of them?"
- A. Eroded consumer trust in traditional banks
- B. Created regulatory space through post-crisis reforms
- C. Directly funded fintech startups through government bailout programs
- D. Released experienced talent as financial institutions downsized
- **Correct: C** -- Bailout funds went to banks, not fintechs. Fintech benefited indirectly through trust erosion, regulatory change, and talent availability.

Q12: "Apply the five-question evaluation framework: A company provides real-time compliance monitoring for banks using AI. It charges a monthly subscription fee. Its customers are enterprise banks, not consumers. What is this company's fintech vertical?"
- A. Payments
- B. RegTech
- C. Wealth Management
- D. Lending
- **Correct: B** -- Real-time compliance monitoring for banks using AI is the definition of RegTech.

**Analyze Level (6 questions):**

Q13: "Why did the 2008 financial crisis benefit fintech startups more than previous financial crises?"
- A. Previous crises did not erode consumer trust in banks
- B. The convergence of trust erosion with smartphone adoption and cloud computing created a unique window
- C. Governments specifically created programs to fund fintech after 2008
- D. The 2008 crisis was more severe than any previous crisis
- **Correct: B** -- The 2008 crisis was unique because it coincided with enabling technologies (smartphones, cloud) that made alternative financial services technically feasible.

Q14: "Compare the partnership and acquisition models. Which statement best captures their fundamental trade-off?"
- A. Partnerships are always cheaper than acquisitions
- B. Acquisitions give more control but risk killing the innovation they acquired; partnerships preserve innovation but give less control
- C. Partnerships are only suitable for small banks; acquisitions are for large banks
- D. There is no trade-off -- acquisition is always preferable when affordable
- **Correct: B** -- This captures the core tension: control vs. innovation preservation.

Q15: "Analyze the 'leapfrog effect' in fintech adoption. Why does weak traditional banking infrastructure sometimes lead to FASTER fintech adoption?"
- A. Because regulators in those countries are more permissive
- B. Because there is less incumbency resistance and consumers adopt the first adequate solution available
- C. Because those countries receive more foreign investment in fintech
- D. Because technology is cheaper in developing countries
- **Correct: B** -- The leapfrog effect occurs because consumers with no existing banking relationship adopt mobile/digital solutions without the switching costs that slow adoption in well-banked markets.

Q16: "What is the most important difference between embedded finance and a traditional bank-fintech partnership?"
- A. Embedded finance is always cheaper for consumers
- B. In embedded finance, the financial service is invisible -- it is integrated into a non-financial platform, whereas partnerships create visible co-branded products
- C. Embedded finance does not require any banking license
- D. Partnerships are more innovative than embedded finance
- **Correct: B** -- The defining feature of embedded finance is that the financial service is seamlessly integrated into a non-financial experience.

Q17: "A fintech claims to 'democratize finance.' Analyze this claim using the stakeholder impact framework. Which stakeholder group is most at risk of being underserved by this narrative?"
- A. Tech-savvy millennials in urban areas
- B. Elderly and digitally excluded populations who cannot use app-based services
- C. Institutional investors
- D. Fintech employees
- **Correct: B** -- The 'democratize finance' narrative often overlooks the digital divide, leaving digitally excluded populations further behind.

Q18: "Why is the unbundling of banking not necessarily permanent? What force might drive re-bundling?"
- A. Banks will always be more profitable than fintechs
- B. As fintechs mature, they may expand into adjacent services, re-creating integrated platforms (super-apps, neobanks adding lending, insurance, etc.)
- C. Regulators will force fintechs to merge with banks
- D. Consumers prefer a single provider for all financial services
- **Correct: B** -- Re-bundling occurs as successful fintechs expand their product range, gradually recreating the integrated model they originally disrupted.

**Evaluate Level (2 questions):**

Q19: "A Central European bank with 5 million retail customers and aging technology infrastructure wants to compete with neobanks. Evaluate: which strategy offers the best balance of speed, control, and innovation?"
- A. Build a digital bank from scratch internally
- B. Acquire a successful neobank and migrate customers
- C. Partner with a neobank for the digital front-end while retaining the license and customer relationship
- D. Ignore neobanks and focus on corporate banking
- **Correct: C** -- Partnership preserves the bank's strengths (license, customers, trust) while gaining digital capabilities quickly. Internal build is too slow; acquisition risks culture clash; ignoring neobanks cedes the retail market.

Q20: "Evaluate the following argument: 'Fintech regulation should be minimal because excessive regulation stifles innovation.' Which response best captures the nuance of this debate?"
- A. The argument is correct -- regulation always reduces innovation
- B. The argument ignores that unregulated fintech creates consumer protection gaps that ultimately undermine trust and adoption
- C. The argument is wrong -- more regulation always leads to better outcomes
- D. Regulation is irrelevant to fintech because technology moves faster than regulators
- **Correct: B** -- The innovation-protection trade-off is the core regulatory challenge. Minimal regulation may boost short-term innovation but creates long-term trust and stability risks.

### Advanced Quiz (20 MCQ)

**Bloom's Distribution:** Apply(4) + Analyze(8) + Evaluate(6) + Create(2) = 20

**Question Focus Areas (higher cognitive level, no duplicates with standard):**

Q1 [Apply]: A Southeast Asian country with 70% smartphone penetration but only 30% bank account ownership asks you to recommend a fintech development strategy. Which approach is most likely to succeed?
- A. Subsidize traditional bank branch expansion
- B. Develop a mobile money ecosystem leveraging existing telecom infrastructure
- C. Launch a government-run neobank
- D. Import European open banking regulations unchanged
- **Correct: B** -- Mobile money leveraging existing telecom infrastructure (M-Pesa model) has proven most effective in markets with high mobile but low banking penetration.

Q2 [Apply]: A fintech startup wants to offer micro-loans in three different countries with different regulatory frameworks. Using the collaboration model framework, which approach minimizes regulatory complexity?
- A. Obtain a separate lending license in each country
- B. Use a BaaS provider that holds licenses in all three jurisdictions
- C. Operate without licenses until regulators notice
- D. Partner with a different local bank in each country
- **Correct: B** -- BaaS providers with multi-jurisdictional licenses provide the simplest path to regulatory compliance across borders.

Q3 [Apply]: Using the five-question evaluation framework, classify a company that: serves SMEs, attacks the lending layer, earns from interest spreads, holds a banking license, and creates new credit access for underserved businesses.
- A. Payments fintech
- B. Digital lender / challenger bank
- C. RegTech provider
- D. Wealth management platform
- **Correct: B** -- All five criteria point to a digital lending institution serving underserved SMEs.

Q4 [Apply]: A European bank must comply with PSD2 open banking requirements. Which of the following represents the minimum compliance approach vs. the strategic opportunity?
- A. Minimum: publish APIs; Strategic: build a platform ecosystem around those APIs
- B. Minimum: acquire a fintech; Strategic: build better branches
- C. Minimum: hire a compliance officer; Strategic: lobby against PSD2
- D. Minimum: ignore the regulation; Strategic: wait for enforcement
- **Correct: A** -- PSD2 compliance requires API publication (minimum), but strategic banks build platform ecosystems to attract third-party innovation.

Q5 [Analyze]: Analyze why the 'unbundling' narrative is simultaneously accurate and misleading. What does it correctly describe, and what does it miss?
- A. It correctly describes specialization but misses that many fintechs are now re-bundling into integrated platforms
- B. It correctly describes bank failures but misses that fintechs fail more often
- C. It correctly describes technology but misses that regulation prevents unbundling
- D. It correctly describes consumer demand but misses that banks have no technology
- **Correct: A** -- Unbundling describes the initial disruption wave accurately, but the re-bundling trend (super-apps, neobanks adding products) shows the dynamic is cyclical, not unidirectional.

Q6 [Analyze]: Compare the regulatory responses to fintech in the EU (PSD2/MiCA) vs. the US (fragmented federal/state approach). Which analysis is most accurate?
- A. The EU approach is always superior because it is unified
- B. The EU's unified approach enables cross-border innovation but may stifle local experimentation; the US's fragmented approach allows state-level innovation but creates compliance burden for national fintechs
- C. The US approach is always superior because it is market-driven
- D. Both approaches are identical in practice despite different structures
- **Correct: B** -- Both approaches have genuine trade-offs. The EU enables scale but constrains experimentation; the US enables experimentation but burdens scale.

Q7 [Analyze]: The 'leapfrog effect' suggests weak banking infrastructure enables fintech. Analyze the limits of this thesis. Under what conditions does leapfrogging NOT occur?
- A. When smartphone penetration is high
- B. When regulatory frameworks actively block non-bank financial service providers, or when digital literacy is too low to use mobile financial services
- C. When traditional banks are profitable
- D. When the country is large
- **Correct: B** -- Leapfrogging requires both enabling technology AND permissive regulation AND sufficient digital literacy. Missing any one blocks the effect.

Q8 [Analyze]: Analyze the claim that "fintech democratizes finance." What evidence supports it, and what evidence contradicts it?
- A. Fully supported -- fintech always improves access
- B. Supported by mobile money inclusion data; contradicted by the digital divide, algorithmic bias in lending, and the concentration of fintech benefits among already-banked populations
- C. Fully contradicted -- fintech only serves the wealthy
- D. Neither supported nor contradicted -- fintech has no impact on access
- **Correct: B** -- The evidence is mixed. Genuine inclusion gains (M-Pesa, micro-investing) coexist with digital exclusion and bias concerns.

Q9 [Analyze]: Why might a bank choose to acquire a fintech even though partnerships are cheaper and faster?
- A. Acquisitions are always better investments
- B. When the fintech's technology is a competitive moat that the bank cannot access through partnership, or when the bank needs to prevent competitors from partnering with that fintech
- C. Banks always prefer to own rather than rent
- D. Regulators prefer acquisitions to partnerships
- **Correct: B** -- Acquisition makes strategic sense when the fintech's IP is a competitive differentiator that must be exclusively controlled.

Q10 [Analyze]: Analyze the systemic risk implications of fintech. How might widespread fintech adoption create new systemic risks that did not exist in traditional banking?
- A. Fintech eliminates all systemic risk
- B. Concentration risk in cloud providers, interconnectedness through APIs, speed of digital bank runs, and regulatory gaps for non-bank financial institutions
- C. Fintech is too small to create systemic risk
- D. Systemic risk only exists in traditional banking
- **Correct: B** -- Fintech introduces new systemic risk vectors: cloud concentration, API interdependence, digital contagion speed, and regulatory coverage gaps.

Q11 [Analyze]: Compare embedded finance with open banking as strategies for financial inclusion. Which is more likely to reach unbanked populations, and why?
- A. Open banking, because it gives consumers control of their data
- B. Embedded finance, because it integrates financial services into platforms people already use (e-commerce, ride-sharing, social media) without requiring them to seek out financial products
- C. Neither -- only traditional bank branch expansion reaches the unbanked
- D. Both are equally effective
- **Correct: B** -- Embedded finance meets people where they already are (non-financial platforms), reducing the friction of seeking out financial products -- a key barrier for unbanked populations.

Q12 [Analyze]: What is the fundamental difference between a fintech that "creates value" and one that "captures value"? Give an example of each.
- A. There is no difference
- B. Value creation expands the total market (e.g., mobile money serving previously unbanked populations); value capture takes market share from incumbents without expanding the market (e.g., a neobank attracting existing bank customers with lower fees)
- C. Value creation means higher profits; value capture means lower profits
- D. Only banks create value; fintechs only capture value
- **Correct: B** -- This distinction is critical for evaluating fintech impact. M-Pesa created new value by serving the unbanked; many neobanks primarily capture value from existing bank customers.

Q13 [Evaluate]: Evaluate the sustainability of the neobank business model. Most neobanks have not achieved profitability despite rapid customer growth. Is this a temporary growth-stage phenomenon or a structural problem?
- A. Purely temporary -- all will be profitable soon
- B. Likely structural for many: customer acquisition costs are high, revenue per customer is low (free accounts), and the customers they attract are often the least profitable (young, low-balance). Sustainable profitability requires either cross-selling higher-margin products or achieving massive scale.
- C. Purely structural -- no neobank can ever be profitable
- D. Profitability is irrelevant for technology companies
- **Correct: B** -- Most neobanks face a structural challenge: free basic accounts attract cost-conscious customers who generate little revenue. Profitability requires either scale (spreading fixed costs) or cross-selling (moving into lending, insurance, investment).

Q14 [Evaluate]: Evaluate the argument that regulatory sandboxes are the best way to balance innovation and consumer protection in fintech. What are the strongest counterarguments?
- A. There are no counterarguments -- sandboxes are universally beneficial
- B. Sandboxes may create an uneven playing field (sandbox participants get advantages over non-participants), give a false sense of regulatory endorsement, and may not scale -- products tested in a sandbox may behave differently at full market scale
- C. Sandboxes are always harmful because they delay regulation
- D. The concept of sandboxes has been abandoned by all regulators
- **Correct: B** -- Sandboxes have real limitations: competitive fairness concerns, implicit endorsement risks, and the gap between controlled testing and real-world deployment at scale.

Q15 [Evaluate]: A venture capital firm asks you to evaluate a fintech that claims to "disrupt insurance using AI." The company has no insurance license, operates in three jurisdictions, and has been growing users at 50% month-over-month. Evaluate the investment risk using the five-question framework.
- A. Invest immediately -- growth rate justifies any risk
- B. The regulatory risk is the critical concern: no insurance license in three jurisdictions creates existential regulatory risk. Growth without regulatory foundation is fragile. Recommend: invest only after the company secures licenses or establishes BaaS/white-label partnerships in all jurisdictions.
- C. Pass -- all insurtechs are bad investments
- D. Evaluate only the technology, not the regulatory position
- **Correct: B** -- The five-question framework highlights the regulatory gap as the critical risk. Fast growth without regulatory compliance is unsustainable.

Q16 [Evaluate]: Evaluate whether the 2008 financial crisis thesis (crisis -> fintech boom) applies to the 2020 COVID-19 pandemic. Did COVID accelerate fintech in the same way the 2008 crisis did?
- A. No -- COVID had no effect on fintech
- B. Partially similar: COVID accelerated digital adoption (demand shift) and remote work (technology enablement), but it did NOT erode trust in banks or create new regulatory space. The mechanism was acceleration of existing trends rather than creation of new conditions.
- C. Identical mechanism -- trust erosion, regulatory change, and talent release all occurred again
- D. COVID harmed fintech by reducing consumer spending
- **Correct: B** -- COVID was an acceleration event (digital adoption), not a trust-erosion event (unlike 2008). The mechanisms are related but distinct.

Q17 [Evaluate]: Which of the five fintech verticals (payments, lending, insurance, wealth management, RegTech) faces the highest regulatory barriers to disruption, and why?
- A. Payments -- because payments are universally regulated
- B. Lending -- because extending credit requires banking licenses, capital requirements, and consumer protection compliance that are among the most stringent in financial regulation
- C. Wealth management -- because investment advice is the most regulated activity
- D. RegTech -- because compliance software faces the strictest oversight
- **Correct: B** -- Lending involves the heaviest regulatory burden: capital adequacy requirements, consumer credit protection laws, anti-money laundering compliance, and (in many jurisdictions) banking license requirements.

Q18 [Evaluate]: Evaluate the claim that big tech companies (Google, Apple, Amazon, Meta) pose a greater competitive threat to banks than fintech startups. What evidence supports or undermines this claim?
- A. Fully supported -- big tech will replace both banks and fintechs
- B. Partially supported: big tech has massive distribution (billions of users), data advantages, and technology capabilities. However, they face regulatory scrutiny, reputational risk from entering finance, and may prefer partnership/embedded roles over direct banking.
- C. Fully undermined -- big tech has no interest in financial services
- D. Big tech and fintech are the same thing
- **Correct: B** -- Big tech's distribution and data advantages are formidable, but regulatory constraints, reputational considerations, and strategic preferences for platform roles (rather than licensed banking) moderate the threat.

Q19 [Create]: Design a fintech evaluation scorecard that a bank's strategy team could use to assess potential partnership candidates. What dimensions should it include, and how would you weight them?
- A. Only evaluate technology quality
- B. A comprehensive scorecard should include: Technology fit (25%), Regulatory compliance (20%), Cultural alignment (15%), Financial sustainability (15%), Customer overlap (15%), Data security posture (10%). Weight regulatory compliance highly because non-compliance creates existential risk.
- C. Only evaluate the fintech's valuation
- D. Evaluation is unnecessary -- banks should partner with all fintechs
- **Correct: B** -- A balanced scorecard covering technology, regulation, culture, finances, customer fit, and security provides a systematic evaluation framework. The specific weights reflect the priority of regulatory compliance.

Q20 [Create]: Propose a regulatory framework for a new fintech vertical: AI-powered autonomous financial advisors that make investment decisions without human oversight. What principles should guide the framework?
- A. No regulation needed -- AI is always rational
- B. Key principles should include: algorithmic transparency (explainability requirements), human override mechanisms, fiduciary duty assignment (who is liable when AI makes a loss?), testing and validation standards, ongoing monitoring requirements, and consumer disclosure rules. The framework must balance innovation incentives with investor protection.
- C. Ban autonomous AI advisors entirely
- D. Apply existing wealth management regulations unchanged
- **Correct: B** -- A purpose-built framework is needed because existing regulations do not address autonomous AI decision-making. The principles balance innovation with protection through transparency, accountability, and oversight mechanisms.

---

## Part 5: Gallery Page Specification

**File:** `website/galleries/L01_gallery.html`

**Template:** Use the complete gallery HTML template from `course-creator-galleries.md`.

**Substitutions:**
- `{NN}` -> `01`
- `{TOPIC_TITLE}` -> `Fintech Foundations and Overview`
- `{COURSE_NAME}` -> `Financial Technology (FinTech)`
- SLIDE_SETS counts: Replace with actual PDF page counts after compilation

**Tabs (5):**
1. mini5 (5 slides)
2. mini10 (10 slides)
3. core (~10 slides)
4. extended (page count from L01_overview.pdf)
5. full (page count from L01_full.pdf)

**Note:** Deepdive variant is NOT shown in gallery but IS included in downloads. This is by design per `course-creator-galleries.md`.

**Nav links:**
- Back to `../lectures/L01.html`
- Home to `../index.html`
- Downloads to `../downloads/L01.html`

**Filename:** Per course plan note 7, gallery filenames must be `L{NN}_gallery.html` to match deploy skill links. If the galleries template generates `L01.html`, rename to `L01_gallery.html`.

---

## Part 6: HTML Lecture Page Specification

**File:** `website/lectures/L01.html`

**Template:** Use the complete lecture HTML template from `course-creator-lectures.md`.

**Substitutions:**
- `{NN}` -> `01`
- `{TITLE}` -> `Fintech Foundations and Overview`
- `{SUBTITLE}` -> `Understanding the Revolution in Financial Services`
- `{DESCRIPTION}` -> One paragraph summarizing the lecture scope
- `{COURSE_NAME}` -> `Financial Technology (FinTech)`
- `{MODULE_NAME}` -> `Foundations`
- `{SLIDE_COUNT}` -> Actual frame count from full .tex
- `{DURATION}` -> `135` (2h15m)
- `{YEAR}` -> `2026`

**Hero gradient:** Use Fintech theme colors: `#0D7377` to `#14BDEB` (NOT the default `#3333B2` to `#0066CC`)

**Section mapping from full .tex:**
| Arc Role | HTML Section | Frames | Section Title |
|----------|-------------|--------|---------------|
| WHY | `#why` | 1-4 | Why Fintech Matters |
| WHAT | `#what` | 6-9 | Foundational Concepts |
| CASE | `#case` | 10-13 | The Great Recession Catalyst |
| HOW | `#how` | 14-17 | Collaboration Models |
| RISK | `#risk` | 18-20 | Risks and Challenges |
| WHERE | `#where` | 21-23 | Global Landscape |
| IMPACT | `#impact` | 24-25 | Stakeholder Impact |
| SO WHAT | `#sowhat` | 26-27 | Synthesis and Evaluation |

**Chart images:** Copy from `lectures/L01_fintech_foundations/figures/` to `website/charts/L01/` as PNGs.

**Download section:** Links to all 6 PDF variants in `../downloads/`.

**Action links:**
- Gallery: `../galleries/L01_gallery.html`
- Quiz: `../quizzes/L01_quiz.html`
- Advanced Quiz: `../quizzes/L01_quiz_advanced.html`

**KaTeX:** Minimal math in this lecture (no complex formulas), but include KaTeX CDN scripts per template for consistency.

---

## Part 7: Execution TODOs

### Task 1: Generate Shared Assets + Full Variant .tex
**Agent:** executor-high (opus)
**Depends on:** course.yaml must exist (Task 1 of course plan)
**Actions:**
1. Create `_shared/preamble.tex` with Fintech-specific metadata (title: "Financial Technology (FinTech)", institution: "University of Zurich", instructor: "Joerg Osterrieder", course: "MSc", semester: "Spring 2026"). Use the preamble pattern from `full-lecture-generator.md` Part 6, adapted with Fintech colors.
2. Create `_shared/chart_styles.py` with Fintech theme V4_COLORS (using teal/blue palette from course manifest theme: `#0D7377`, `#14BDEB`, plus the standard V4_COLORS).
3. Generate master content plan for L01 (topics, figure allocation, notation table, narrative arc).
4. Generate `L01_full.tex` using full-lecture-generator skill (31 frames, 10-role arc, 12 `\includegraphics` references, comment-block section markers).
5. Generate `L01_quiz_standard.tex` (20 MCQ with Bloom's distribution).
6. Generate `L01_exercises.tex` (7-8 exercises with answer key).

**Acceptance Criteria:**
- [ ] `_shared/preamble.tex` exists and defines all required colors, theme settings, `\bottomnote` command
- [ ] `_shared/chart_styles.py` exists with `V4_COLORS` dict, `apply_v4_style()`, `save_chart()` functions
- [ ] `L01_full.tex` has 29-33 frames (`grep -c "\\begin{frame}"`)
- [ ] `\begin{frame}` and `\end{frame}` counts match
- [ ] 10+ `\includegraphics` references
- [ ] Zero `\section{}` commands (only comment-block markers)
- [ ] `\input{../../_shared/preamble.tex}` present
- [ ] Opening cartoon reference (frame 2) and closing cartoon reference (frame N-2) present
- [ ] Learning Objectives frame with Bloom's levels
- [ ] Key Takeaways frame with 5-7 numbered items
- [ ] Quiz file has 21 frames (title + 20 questions)
- [ ] Exercise file has 11-13 frames

### Task 2: Generate 5 Other .tex Variants
**Agent:** executor (sonnet) -- can parallelize overview + deepdive + mini10 + mini5; core waits for full
**Depends on:** Task 1 (master content plan + full variant)
**Actions:**
1. Generate `L01_overview.tex` using beamer-slide-creator (three-zone, ~25-28 frames, PMSP framework, shared preamble).
2. Generate `L01_deepdive.tex` using beamer-slide-creator (MAIN BODY + appendix, ~15-18 frames, shared preamble).
3. Extract `L01_core.tex` from `L01_full.tex` using frame-index extraction algorithm (10 frames, self-contained preamble).
4. Generate `L01_mini10.tex` using mini-lecture-generator (10 frames, self-contained preamble, inline TikZ/pgfplots only).
5. Generate `L01_mini5.tex` using mini-lecture-generator (5 frames, self-contained preamble, inline TikZ/pgfplots only).

**Acceptance Criteria:**
- [ ] All 6 .tex files exist in `lectures/L01_fintech_foundations/slides/`
- [ ] Frame counts within expected ranges: mini5(5-6), mini10(10-11), core(10-11), overview(25-30), deepdive(15-20), full(29-33)
- [ ] Self-contained preamble in mini5, mini10, core (zero `\input` commands)
- [ ] Shared preamble in full, overview, deepdive
- [ ] Zero `\includegraphics` in mini5, mini10 (inline TikZ/pgfplots only)
- [ ] mini5 and mini10 compile with `pdflatex` alone (no external dependencies)

### Task 3: Generate Chart Scripts and Compile All to PDF
**Agent:** executor (sonnet) for chart scripts; build-fixer (sonnet) for compilation issues
**Depends on:** Task 1 (chart references in .tex), Task 2 (all variants exist)
**Actions:**
1. Generate all 12 `chart.py`/`cartoon.py` scripts in `figures/` subdirectories (per specifications in Part 3).
2. Execute all chart scripts: `python chart.py` in each figure directory.
3. Verify all `chart.pdf` / `cartoon.pdf` files produced.
4. Compile all 6 .tex files with `pdflatex` (two passes each).
5. Verify all 6 PDFs produced without errors.
6. Check for overfull vbox warnings.

**Acceptance Criteria:**
- [ ] 12 `chart.py`/`cartoon.py` scripts exist
- [ ] All scripts have `CHART_METADATA` dict
- [ ] All scripts import from `_shared/chart_styles.py` (full/extended variants) or are self-contained (cartoons)
- [ ] All scripts produce valid PDF output (exit code 0)
- [ ] `figsize=(10,6)` used in all charts
- [ ] `np.random.seed(42)` present where randomness used
- [ ] No `plt.show()` calls
- [ ] V4_COLORS palette used consistently
- [ ] All 6 .tex files compile to valid .pdf
- [ ] Zero compilation errors (`grep -c "^!" *.log` returns 0)
- [ ] All conceptual charts use illustrative/synthetic data (visual inspection)

### Task 4: Create Gallery Page
**Agent:** executor (sonnet)
**Depends on:** Task 3 (compiled PDFs)
**Actions:**
1. Convert all 6 PDFs (but only 5 for gallery: mini5, mini10, core, overview, full) to PNGs using `pdftoppm`.
   - Note: deepdive is NOT shown in gallery but IS included in downloads.
   - The "extended" tab in the gallery uses the overview PDF as its source.
2. Place PNGs in `website/galleries/images/L01/{variant}/slide_XX.png`.
3. Get actual page counts from each PDF.
4. Generate `website/galleries/L01_gallery.html` from template with correct slide counts.
5. Verify all 5 tabs functional.

**Acceptance Criteria:**
- [ ] PNG files exist for 5 variants (mini5, mini10, core, extended/overview, full)
- [ ] PNG count matches PDF page count for each variant
- [ ] Gallery HTML file exists at `website/galleries/L01_gallery.html`
- [ ] All 5 tabs present and functional
- [ ] Tab badge counts match actual slide counts
- [ ] Lightbox opens on click
- [ ] Download buttons link to correct PDFs in `../downloads/`
- [ ] Back link points to `../lectures/L01.html`
- [ ] No broken image references

### Task 5: Create Lecture HTML Page
**Agent:** executor (sonnet)
**Depends on:** Task 3 (compiled PDFs + chart PNGs)
**Actions:**
1. Parse `L01_full.tex` to extract content by arc section.
2. Convert LaTeX content to HTML using the conversion rules from `course-creator-lectures.md`.
3. Copy chart PDFs to `website/charts/L01/` as PNGs.
4. Generate `website/lectures/L01.html` from template.
5. Replace hero gradient with Fintech theme colors (`#0D7377` to `#14BDEB`).

**Acceptance Criteria:**
- [ ] `website/lectures/L01.html` exists
- [ ] All 8 sections present (why, what, case, how, risk, where, impact, sowhat)
- [ ] No raw LaTeX commands in HTML output
- [ ] All `<img>` src paths resolve to existing files
- [ ] KaTeX CDN scripts included in `<head>`
- [ ] Sidebar navigation matches section IDs
- [ ] Download links point to correct PDF paths
- [ ] Hero gradient uses `#0D7377` to `#14BDEB`
- [ ] Scroll-tracking JavaScript functional
- [ ] Module badge shows "Foundations" with green `#2CA02C`

### Task 6: Create Quiz Pages (Standard + Advanced)
**Agent:** executor (sonnet)
**Depends on:** Task 1 (quiz .tex from Stage 1)
**Actions:**
1. Parse `L01_quiz_standard.tex` and convert to interactive HTML (`website/quizzes/L01_quiz.html`).
2. Generate 20 advanced quiz questions (higher Bloom's levels) and create `website/quizzes/L01_quiz_advanced.html`.
3. Ensure both pages have: ANSWERS JavaScript object, checkAnswers() function, correct radio button names, feedback divs.
4. Verify zero question overlap between standard and advanced quizzes.

**Acceptance Criteria:**
- [ ] `website/quizzes/L01_quiz.html` exists (standard quiz)
- [ ] `website/quizzes/L01_quiz_advanced.html` exists (advanced quiz)
- [ ] Each quiz contains exactly 20 question blocks
- [ ] Standard quiz Bloom's: Understand(4) + Apply(8) + Analyze(6) + Evaluate(2) = 20
- [ ] Advanced quiz Bloom's: Apply(4) + Analyze(8) + Evaluate(6) + Create(2) = 20
- [ ] ANSWERS object has keys "1" through "20" with non-empty explanations
- [ ] checkAnswers() function present and syntactically correct
- [ ] `id="fb-{N}"` divs match `name="q{N}"` radio groups for N=1..20
- [ ] Nav bar links are correct relative paths
- [ ] Standard and advanced quizzes have zero duplicate questions
- [ ] All questions test conceptual understanding (no coding questions)
- [ ] Filenames match deploy skill expectations: `L01_quiz.html` and `L01_quiz_advanced.html`

### Task 7: Copy PDFs to Downloads Directory
**Agent:** executor-low (haiku)
**Depends on:** Task 3 (compiled PDFs)
**Actions:**
1. Copy all 6 L01 PDFs to `website/downloads/`:
   - `L01_mini5.pdf`
   - `L01_mini10.pdf`
   - `L01_core.pdf`
   - `L01_overview.pdf`
   - `L01_deepdive.pdf`
   - `L01_full.pdf`

**Acceptance Criteria:**
- [ ] All 6 PDFs exist in `website/downloads/`
- [ ] File sizes are non-zero
- [ ] Filenames match exactly (case-sensitive)

---

## Commit Strategy

| Commit | After Task | Message |
|--------|-----------|---------|
| 1 | Task 1 | `feat(L01): generate shared preamble, chart styles, and full-variant LaTeX for Lecture 1` |
| 2 | Task 2 | `feat(L01): generate 5 additional LaTeX variants (overview, deepdive, core, mini10, mini5)` |
| 3 | Task 3 | `feat(L01): generate 12 chart scripts, compile all charts and PDFs` |
| 4 | Tasks 4-7 | `feat(L01): generate gallery, lecture HTML, quiz pages, and copy downloads` |

---

## Success Criteria

### Quantitative
- [ ] 6 `.tex` files in `lectures/L01_fintech_foundations/slides/`
- [ ] 6 `.pdf` files compiled from those .tex files
- [ ] 12 chart/cartoon scripts generated and executed
- [ ] 12 chart/cartoon PDF outputs
- [ ] 1 gallery HTML page with PNGs for 5 variants
- [ ] 1 lecture HTML page with 8 sections
- [ ] 2 quiz HTML pages (standard + advanced) with 20 questions each (40 total)
- [ ] 6 PDFs in `website/downloads/`

### Qualitative
- [ ] Content appropriate for MSc finance/business students
- [ ] No coding exercises or programming requirements
- [ ] All charts are conceptual (no real market data)
- [ ] Consistent Fintech theme (teal-to-blue gradient, `#0D7377` to `#14BDEB`)
- [ ] Professional academic quality
- [ ] Audience calibration: strong finance assumed, technology explained at conceptual level

### Final Verification
- [ ] All 6 PDFs open correctly in a PDF reader
- [ ] Gallery page loads all thumbnails in browser
- [ ] Lecture HTML page renders all 8 sections correctly
- [ ] Both quiz pages score correctly when answers selected
- [ ] No raw LaTeX in any HTML output
- [ ] All cross-references (download links, gallery links, quiz links) resolve to existing files

---

## Notes for Executor

1. **Fintech theme colors override defaults.** The hero gradient must be `#0D7377` to `#14BDEB`, NOT the default purple-to-blue (`#3333B2` to `#0066CC`). Module badge for Foundations is green `#2CA02C`.

2. **MSc audience calibration.** Assume students understand: DCF, portfolio theory, risk management, financial regulation, basic statistics. They do NOT know: programming, API design, blockchain internals, machine learning, cloud architecture. Explain technology at a conceptual level using finance analogies.

3. **Conceptual charts are paramount.** Every chart.py must produce a conceptual diagram with illustrative data. Label any bar charts or trends as "Illustrative" or "Conceptual". No real investment figures, no real company financials, no real market data.

4. **Quiz filenames must match deploy skill.** Standard quiz: `L01_quiz.html` (NOT `L01_standard.html`). Advanced quiz: `L01_quiz_advanced.html` (NOT `L01_advanced.html`). Gallery: `L01_gallery.html` (NOT `L01.html`).

5. **This is Lecture 1 -- it sets the tone.** The first lecture establishes the course's pedagogical style, visual quality, and content depth. Extra care should be taken to ensure it is polished and complete, as all subsequent lectures will follow its pattern.

6. **Shared preamble and chart_styles.py are course-wide assets.** They will be used by all 7 lectures. Design them for reuse, not just L01. The preamble should define all colors needed across all modules. The chart_styles should include all V4_COLORS.

7. **Generation order matters.** Within L01: master plan first, then full variant, then (in parallel) overview + deepdive + mini10 + mini5, then core (extracted from full). Charts can be generated in parallel with overview/deepdive/mini variants since the full variant establishes chart references.
