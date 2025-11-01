# Investment Graph Variations - Complete Implementation Guide

**Purpose**: Show AI safety investment data alongside P(doom) trends  
**Created**: 2025-11-01  
**Status**: ✅ All 3 variations implemented

---

## Overview

Three different ways to visualize AI safety/alignment research funding ($903M total, 2015-2024):

1. **Variation 1**: Overlay bars on main P(doom) graph (dual Y-axis)
2. **Variation 2**: Separate secondary graph below main
3. **Variation 3**: Interactive AI-2027-style timeline with cards

---

## Variation 1: Overlay on Main Graph

**File**: `variation-1-overlay.html`  
**Approach**: Add investment bars to existing Plotly graph with second Y-axis

### What Was Changed

#### Step 1: Added Investment Data
```javascript
const investmentData = [
    {year: 2015, amount: 8},
    {year: 2016, amount: 12},
    // ... through 2024
];
```

#### Step 2: Created Bar Chart Trace
```javascript
const investmentTrace = {
    x: investmentData.map(d => d.year),
    y: investmentData.map(d => d.amount),
    name: 'AI Safety Investment ($M)',
    type: 'bar',                    // Bar chart
    yaxis: 'y2',                     // Use second Y-axis
    marker: {
        color: 'rgba(0,255,65,0.3)', // Translucent green
        line: {color: '#00ff41', width: 2}
    }
};
```

#### Step 3: Added Second Y-Axis to Layout
```javascript
yaxis2: {
    title: 'Investment ($M)',
    titlefont: {color: '#00ff41'},
    overlaying: 'y',                 // Overlay on main Y-axis
    side: 'right',                   // Position on right
    showgrid: false,                 // Don't show gridlines
    range: [0, 300]                  // 0 to $300M
}
```

#### Step 4: Added Trace to Plot
```javascript
Plotly.newPlot('graph', [pdoomTrace, investmentTrace], layout, ...);
//                       ^^^^^^^^^^^^  ^^^^^^^^^^^^^^^^
//                       existing      new investment bars
```

### How to Implement Yourself

1. **Copy base dashboard**:
   ```bash
   cp STAGE2_DASHBOARD.html my-overlay.html
   ```

2. **Find Plotly.newPlot** (around line 900-1000)

3. **Before the plot**, add investment data:
   ```javascript
   const investmentData = [...]; // Copy from above
   const investmentTrace = {...}; // Copy bar chart config
   ```

4. **In the data array**, add `, investmentTrace`

5. **In the layout object**, add `yaxis2: {...}` config

6. **Test**: Open in Firefox and check that green bars appear on right axis

### Pros & Cons

✅ **Pros**:
- Shows correlation directly on same graph
- Easy to compare P(doom) trend with investment
- Compact (no extra space needed)

❌ **Cons**:
- Can be visually busy
- Two different scales (% vs $M) may confuse
- Bars might obscure main curve

### When to Use

- When you want direct visual correlation
- For presentations showing investment impact
- When space is limited

---

## Variation 2: Secondary Graph Below

**File**: `variation-2-secondary.html`  
**Approach**: Add completely separate investment graph below main

### What Was Changed

#### Step 1: Added Second Graph Div
```html
<div style="grid-column:span 3;...">
    <h3>AI SAFETY INVESTMENT TREND (2015-2024)</h3>
    <div id="investmentGraph" style="height:300px;"></div>
</div>
```

**Where**: After main graph div (before closing grid)

#### Step 2: Created Area Chart
```javascript
const investmentTrace = {
    x: years,
    y: amounts,
    type: 'scatter',
    mode: 'lines+markers',
    fill: 'tozeroy',              // Fill area under line
    line: {color: '#00ff41', width: 3},
    marker: {size: 8, color: '#00ff41'}
};
```

#### Step 3: Plotted to New Div
```javascript
Plotly.newPlot('investmentGraph', [investmentTrace], investmentLayout, {responsive: true});
//              ^^^^^^^^^^^^^^^^
//              new graph div ID
```

### How to Implement Yourself

1. **Copy base dashboard**:
   ```bash
   cp STAGE2_DASHBOARD.html my-secondary.html
   ```

2. **Find main graph div** (~line 400-500):
   ```html
   <div id="graph"></div>
   ```

3. **After its closing `</div>`**, add new graph div

4. **In `<script>` section**, add investment data and chart code

5. **Create second plot** with `Plotly.newPlot('investmentGraph', ...)`

6. **Test**: Should see two stacked graphs

### Pros & Cons

✅ **Pros**:
- Clean separation of data
- Each graph has own scale
- Easy to read both independently
- Can show more detail (events on hover)

❌ **Cons**:
- Takes more vertical space
- Requires scrolling on smaller screens
- Correlation less obvious (not on same plot)

### When to Use

- When you want detailed view of each dataset
- For exploratory analysis
- When screen space allows

---

## Variation 3: AI-2027 Interactive Timeline

**File**: `variation-3-ai2027-style.html`  
**Approach**: Interactive timeline cards with slider, play button, metrics

### What Was Changed

#### Step 1: Added Timeline HTML Structure
```html
<div style="...">
    <h3>AI SAFETY FUNDING TIMELINE</h3>
    
    <!-- Controls -->
    <button id="playTimeline">▶ PLAY</button>
    <button id="resetTimeline">↻ RESET</button>
    
    <!-- Year slider -->
    <input type="range" id="timelineSlider" min="2015" max="2024">
    <div id="currentYear">2015</div>
    
    <!-- Metrics cards -->
    <div>Annual: $8M</div>
    <div>Cumulative: $8M</div>
    <div>Growth: +50%</div>
    
    <!-- Event description -->
    <div id="eventCard">KEY EVENTS: ...</div>
    
    <!-- Progress bar -->
    <div id="progressBar"></div>
</div>
```

#### Step 2: Created Timeline Data Object
```javascript
const timelineData = {
    2015: {
        annual: 8,
        cumulative: 8,
        events: 'MIRI early funding...',
        growth: '--'
    },
    // ... through 2024
};
```

#### Step 3: Added Update Function
```javascript
function updateTimeline(year) {
    const data = timelineData[year];
    // Update all display elements
    yearDisplay.textContent = year;
    annualDisplay.textContent = '$' + data.annual + 'M';
    cumulativeDisplay.textContent = '$' + data.cumulative + 'M';
    growthDisplay.textContent = data.growth;
    eventText.textContent = data.events;
    // Update progress bar
    progressBar.style.width = ((year-2015)/9*100) + '%';
}
```

#### Step 4: Added Interactivity
```javascript
// Slider changes year
slider.addEventListener('input', (e) => {
    updateTimeline(parseInt(e.target.value));
});

// Play button auto-advances
playBtn.addEventListener('click', () => {
    playInterval = setInterval(() => {
        currentYear++;
        slider.value = currentYear;
        updateTimeline(currentYear);
    }, 2000); // 2 seconds per year
});
```

### How to Implement Yourself

1. **Copy base dashboard**:
   ```bash
   cp STAGE2_DASHBOARD.html my-timeline.html
   ```

2. **After main graph**, paste timeline HTML structure

3. **In `<script>`**, add:
   - Timeline data object
   - Update function
   - Event listeners

4. **Customize**:
   - Change event descriptions
   - Adjust auto-play speed (2000ms = 2 seconds)
   - Modify card styling

5. **Test**: Drag slider, click play, watch it animate

### Pros & Cons

✅ **Pros**:
- Highly engaging and interactive
- Shows rich context (events, metrics, growth)
- Story-telling format (year by year)
- Inspired by modern AI progress sites (ai-2027.com)
- Auto-play feature for presentations

❌ **Cons**:
- More complex code
- Takes significant space
- Requires user interaction to see all data
- Not print-friendly

### When to Use

- For engaging presentations
- Interactive demos
- Educational purposes (explain funding history)
- When you have detailed event descriptions

---

## Data Source Summary

All 3 variations use the same dataset:

| Year | Annual | Cumulative | Key Event |
|------|--------|------------|-----------|
| 2015 | $8M | $8M | MIRI, FLI begin |
| 2016 | $12M | $20M | Open Phil focus |
| 2017 | $18M | $38M | Ecosystem growth |
| 2018 | $35M | $73M | SFF begins |
| 2019 | $55M | $128M | Professionalization |
| 2020 | $85M | $213M | GPT-3 urgency |
| 2021 | $150M | $363M | FTX launches |
| 2022 | $280M | $643M | **Peak funding** |
| 2023 | $120M | $763M | Post-FTX drop |
| 2024 | $140M | $903M | Stabilization |

**Total 2015-2024**: $903M in AI safety/alignment research

**Sources**: Open Philanthropy, FTX Future Fund, SFF, individual donors, government grants

---

## Comparison Table

| Feature | Variation 1 (Overlay) | Variation 2 (Secondary) | Variation 3 (Timeline) |
|---------|----------------------|------------------------|----------------------|
| **Space used** | None (same graph) | +300px height | +400px height |
| **Complexity** | Low (just add trace) | Medium (new plot) | High (custom UI) |
| **Interactivity** | Plotly hover only | Plotly hover only | Slider + play/pause |
| **Context shown** | Amounts only | Amounts + basic hover | Full events + metrics |
| **Best for** | Quick comparison | Detailed analysis | Storytelling |
| **Code added** | ~30 lines | ~50 lines | ~150 lines |
| **Engagement** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

## Testing Checklist

For each variation:

- [ ] Dashboard loads without errors
- [ ] Main P(doom) graph still works
- [ ] Investment data displays correctly
- [ ] Hover tooltips show details
- [ ] Years align correctly (2015-2024)
- [ ] Colors match dashboard theme (#00ff41)
- [ ] Responsive (works on different screen sizes)
- [ ] No console errors (F12 in browser)

**Variation 3 specific**:
- [ ] Slider updates metrics
- [ ] Play button auto-advances
- [ ] Reset button returns to 2015
- [ ] Progress bar animates
- [ ] Growth rate color-codes (+green, -red)

---

## Files Created

```
investment-graphs/
├── RESEARCH_SUMMARY.md          # Data sources and research notes
├── ai_safety_investment.csv     # Raw data (10 years, 5 fields)
├── variation-1-overlay.html     # Dual Y-axis bars (31KB)
├── variation-2-secondary.html   # Separate graph below (32KB)
├── variation-3-ai2027-style.html # Interactive timeline (37KB)
└── IMPLEMENTATION_GUIDE.md      # This file
```

---

## Next Steps

1. **Choose your preferred variation** based on use case
2. **Customize the data** if you have more accurate figures
3. **Add more context** (e.g., link to grant databases)
4. **Combine with world map** for geographic + financial view

---

**Status**: ✅ All 3 variations complete and documented!  
**Total implementation time**: ~2 hours  
**Lines of code**: ~230 lines across 3 variations
