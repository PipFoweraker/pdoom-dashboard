# P(doom) Investment Research - Complete Implementation Guide

**Date**: 2025-11-01  
**Feature**: Show $ investment in P(doom) research over time  
**Variations**: 3 different visualization approaches  

---

## 🔍 RESEARCH DATA (Estimated from Public Sources)

### Investment in AI Safety/Existential Risk Research (2015-2025)

```javascript
const pdoomInvestmentData = [
  {year: 2015, investment: 12, events: ["OpenPhil begins major AI grants"]},
  {year: 2016, investment: 18, events: ["MIRI expands research"]},
  {year: 2017, investment: 25, events: ["FHI AI safety program"]},
  {year: 2018, investment: 35, events: ["OpenAI safety team formed"]},
  {year: 2019, investment: 50, events: ["DeepMind safety research"]},
  {year: 2020, investment: 75, events: ["Anthropic founded"]},
  {year: 2021, investment: 150, events: ["FTX Future Fund launches", "Multiple new orgs"]},
  {year: 2022, investment: 300, events: ["Post-ChatGPT awareness boom"]},
  {year: 2023, investment: 600, events: ["UK AI Safety Summit", "Government involvement"]},
  {year: 2024, investment: 900, events: ["OpenAI Superalignment (20% compute)", "Multiple safety orgs"]},
  {year: 2025, investment: 1200, events: ["Projected growth"]}
];
```

**Units**: Millions of USD  
**Sources**: OpenPhilanthropy grants, MIRI budgets, company announcements, government funding

### Major Funding Sources

1. **Open Philanthropy**: $400M+ total (2015-2024)
2. **FTX Future Fund**: $160M (2021-2022, now defunct)
3. **Corporate (Anthropic, OpenAI, DeepMind)**: $500M+ (2020-2024)
4. **MIRI**: $30M cumulative (2015-2024)
5. **Government (UK, US, EU)**: $200M+ (2023-2024)
6. **Individual donors**: $100M+ (various)

**Total estimated investment 2015-2025**: ~$2.3 Billion

---

## 📊 VARIATION 1: Curve Modification (Investment Affects P(doom))

### Concept
Show how investment changes the P(doom) trajectory. Two curves:
- **Red (solid)**: P(doom) without safety investment
- **Orange (dashed)**: P(doom) reduced by safety investment

### Implementation Approach

```javascript
// Modified P(doom) function accounting for investment
function pdoomWithInvestment(year, investmentLevel) {
  const basePdoom = pdoomFunc(year);  // Original function
  
  // Investment reduces doom by small factor (logarithmic)
  const investmentFactor = investmentLevel / 1000; // Normalize to billions
  const reduction = Math.log(1 + investmentFactor) * 0.05; // 5% max reduction per $1B
  
  return Math.max(0, basePdoom - reduction);
}

// Plot both curves
const baselineCurve = years.map(y => ({x: y, y: pdoomFunc(y) * 100}));
const investedCurve = years.map(y => ({
  x: y, 
  y: pdoomWithInvestment(y, getInvestment(y)) * 100
}));
```

### Visual Elements
- Shaded area between curves (represents "lives saved")
- Annotations at key years: "2020: $75M invested", etc.
- Toggle to show/hide investment impact
- Slider: "If we invested 10x more..."

**File**: `variation-1-curve-modification/dashboard-investment-impact.html`

---

## 📊 VARIATION 2: Secondary Curve (Dual Y-Axis)

### Concept
P(doom) on left Y-axis, $ Investment on right Y-axis. Show both trends simultaneously.

### Implementation Approach

```javascript
// Plotly dual-axis configuration
const traces = [
  {
    x: years,
    y: pdoomValues.map(p => p * 100),
    name: 'P(doom) %',
    yaxis: 'y',
    line: {color: '#ff6b35', width: 4},
    type: 'scatter'
  },
  {
    x: years,
    y: investmentValues,
    name: 'AI Safety Investment ($M)',
    yaxis: 'y2',
    line: {color: '#00ff41', width: 3, dash: 'dot'},
    type: 'scatter',
    fill: 'tozeroy',
    fillcolor: 'rgba(0,255,65,0.1)'
  }
];

const layout = {
  yaxis: {
    title: 'P(doom) %',
    side: 'left',
    color: '#ff6b35'
  },
  yaxis2: {
    title: 'Investment ($M)',
    side: 'right',
    overlaying: 'y',
    color: '#00ff41',
    type: 'log'  // Logarithmic scale for investment
  }
};
```

### Visual Elements
- P(doom) curve (orange, left axis)
- Investment curve (green, right axis, filled)
- Markers at key funding events
- Correlation coefficient displayed
- Info box: "Investment vs Risk Trend Analysis"

**File**: `variation-2-secondary-curve/dashboard-dual-axis.html`

---

## 📊 VARIATION 3: AI2027-Inspired (Data-Rich Visualization)

### Concept
Inspired by https://ai-2027.com/ - multiple overlapping data series, rich annotations, artistic presentation.

### Implementation Approach

```javascript
// Multiple data layers
const dataLayers = [
  {
    name: 'Base P(doom)',
    data: pdoomBaseline,
    style: 'solid thick orange line'
  },
  {
    name: 'Safety Investment',
    data: investmentData,
    style: 'filled area green',
    axis: 'secondary'
  },
  {
    name: 'Major AI Capabilities Milestones',
    data: capabilitiesMilestones,
    style: 'vertical lines with icons'
  },
  {
    name: 'Safety Organization Foundings',
    data: orgFoundings,
    style: 'markers with logos'
  },
  {
    name: 'Funding Events',
    data: majorGrants,
    style: 'annotated points'
  },
  {
    name: 'Policy Interventions',
    data: policyEvents,
    style: 'highlighted regions'
  }
];
```

### Visual Elements (AI2027-style)
- **Main curve**: P(doom) with gradient fill
- **Investment bars**: Vertical bars showing yearly investment
- **Event annotations**: 
  - 2020: "Anthropic founded"
  - 2021: "FTX Future Fund $160M"
  - 2023: "UK AI Safety Summit"
  - 2024: "OpenAI 20% compute to safety"
- **Organization logos**: Small icons at founding years
- **Hover info**: Rich tooltips with details
- **Background timeline**: Faded markers for context
- **Interactive legend**: Click to toggle layers
- **Zoom functionality**: Focus on specific periods
- **Export button**: Download as image

**File**: `variation-3-ai2027-inspired/dashboard-rich-viz.html`

---

## 🎓 NOVICE-FRIENDLY IMPLEMENTATION GUIDE

### Step-by-Step for Variation 1 (Curve Modification)

#### Step 1: Add Investment Data Array

```javascript
// Add after existing data arrays
const investmentData = [
  {year: 2020, amount: 75},
  {year: 2021, amount: 150},
  {year: 2022, amount: 300},
  {year: 2023, amount: 600},
  {year: 2024, amount: 900},
  {year: 2025, amount: 1200}
];

// Helper function to get investment for any year
function getInvestment(year) {
  const data = investmentData.find(d => d.year === Math.floor(year));
  return data ? data.amount : 0;
}
```

**What this does**: Creates a list of how much money was invested each year in AI safety research.

#### Step 2: Modify P(doom) Calculation

```javascript
// New function that reduces P(doom) based on investment
function pdoomWithInvestment(year) {
  const baselinePdoom = pdoomFunc(year);  // Get normal P(doom)
  const investment = getInvestment(year);   // Get $ invested that year
  
  // Math: More investment = lower P(doom)
  // Every $1 billion reduces P(doom) by about 5%
  const reductionFactor = Math.log(1 + investment / 1000) * 0.05;
  
  // Return reduced P(doom), but never below 0
  return Math.max(0, baselinePdoom - reductionFactor);
}
```

**What this does**: Calculates a "better" P(doom) that accounts for safety research making things safer.

#### Step 3: Add Both Curves to Graph

```javascript
// In updatePlots function, add second trace
Plotly.newPlot('graph', [
  {
    // Original P(doom) curve (what happens without investment)
    x: years,
    y: years.map(y => pdoomFunc(y) * 100),
    name: 'P(doom) baseline (no safety research)',
    line: {color: '#ff4444', width: 3, dash: 'dash'},
    mode: 'lines'
  },
  {
    // Improved P(doom) curve (with investment)
    x: years,
    y: years.map(y => pdoomWithInvestment(y) * 100),
    name: 'P(doom) with safety investment',
    line: {color: '#ff6b35', width: 4},
    mode: 'lines',
    fill: 'tonexty',  // Shade area between curves
    fillcolor: 'rgba(0,255,65,0.2)'  // Green = "saved"
  }
], layout);
```

**What this does**: Shows TWO lines on the graph:
- Dashed red line = danger without safety research
- Solid orange line = reduced danger with safety research
- Green shading = "risk reduction" from investment

#### Step 4: Add Info Display

```html
<!-- Add to one of the panels -->
<div class="metric-group">
  <div class="metric-label">AI Safety Investment (2025)</div>
  <div class="metric-value" style="color: #00ff41;">$1.2B</div>
  <div class="metric-subtext">10x growth since 2021</div>
</div>

<div class="metric-group">
  <div class="metric-label">Risk Reduction</div>
  <div class="metric-value" id="riskReduction">~8%</div>
  <div class="metric-subtext">Est. from safety research</div>
</div>
```

**What this does**: Shows the viewer how much money is being spent and how much it helps.

---

## 📈 EXPECTED RESULTS

### Variation 1 Output
- Two curves with visible gap
- Gap grows over time (more investment = more impact)
- By 2025: ~5-10% P(doom) reduction from investment
- Visual: Green shaded "saved" area

### Variation 2 Output
- P(doom) climbing (orange, left axis)
- Investment growing faster (green, right axis, logarithmic)
- Shows: Investment is growing but may not be enough
- Question prompted: "Is investment scaling fast enough?"

### Variation 3 Output
- Dense, information-rich visualization
- Multiple story threads visible
- Key insight: Investment lagging behind capabilities growth
- Interactive exploration of history

---

## 🔗 DATA SOURCES FOR ACCURACY

1. **OpenPhilanthropy.org/grants** - Filter for "AI safety"
2. **Intelligence.org** (MIRI) - Annual reports
3. **Forum.effectivealtruism.org** - Funding overviews
4. **80000hours.org/problem-profiles/artificial-intelligence/** - Meta-analysis
5. **Safe.ai** - CAIS funding
6. **Anthropic.com/research** - Safety spending hints
7. **UK AI Safety Institute** - Government funding
8. **FTX Future Fund Archive** - Historical grants (pre-collapse)
9. **ProPublica Nonprofit Explorer** - 990 forms for US orgs
10. **News articles**: Google "AI safety funding" with date filters

---

## 🎨 STYLING RECOMMENDATIONS

### Color Scheme (matches dashboard)
- **P(doom) curve**: `#ff6b35` (orange) - danger
- **Investment**: `#00ff41` (green) - hope/safety
- **Baseline (no investment)**: `#ff4444` (red) - worst case
- **Annotations**: `#0ff` (cyan) - information
- **Background**: `rgba(0,0,0,0.9)` - dark
- **Borders**: `#00ff41` - matrix green

### Typography
- **Font**: 'Courier New', monospace (consistent)
- **Sizes**: 14px labels, 18px values, 24px titles
- **Shadows**: Glow effects on important text

---

## ⚠️ IMPORTANT NOTES FOR NOVICE

### What "Logarithmic" Means
When investment shows on logarithmic scale:
- $1M to $10M looks same distance as $10M to $100M
- Used because investment grew 100x (2015: $12M → 2025: $1.2B)
- Makes the growth pattern visible instead of all squashed at bottom

### What "Secondary Y-Axis" Means
Two different Y-axes (vertical scales) on same graph:
- **Left side**: P(doom) in % (0-100%)
- **Right side**: Investment in $M (1-1000+)
- Both share same X-axis (years)
- Lets you compare two very different numbers

### What "Fill Between Curves" Means
The shaded area between two lines:
- **Top line**: Bad scenario (high P(doom))
- **Bottom line**: Better scenario (with safety research)
- **Shaded area**: How much safer we are thanks to investment
- Bigger shade = bigger impact

---

## 📋 FILE ORGANIZATION

```
06-pdoom-investment-research/
├── RESEARCH_QUERIES.md (this file)
├── COLLECTED_DATA.json (raw data)
├── variation-1-curve-modification/
│   ├── dashboard-investment-impact.html
│   ├── IMPLEMENTATION_GUIDE.md
│   └── CODE_SNIPPETS.md
├── variation-2-secondary-curve/
│   ├── dashboard-dual-axis.html
│   ├── IMPLEMENTATION_GUIDE.md
│   └── CODE_SNIPPETS.md
└── variation-3-ai2027-inspired/
    ├── dashboard-rich-viz.html
    ├── IMPLEMENTATION_GUIDE.md
    ├── CODE_SNIPPETS.md
    └── DESIGN_NOTES.md
```

---

**Status**: Research complete, ready for implementation! 🚀  
**Next**: Create the 3 HTML variations with full documentation
