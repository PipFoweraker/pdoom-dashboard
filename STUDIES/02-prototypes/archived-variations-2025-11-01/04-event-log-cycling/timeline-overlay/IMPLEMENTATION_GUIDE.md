# Timeline Event Overlay - Implementation Guide

**Variation**: 04-event-log-cycling/timeline-overlay  
**Date**: 2025-11-01  
**Feature**: Display events as markers on the main P(doom) graph timeline

---

## Concept

Instead of cycling events in the text box, display them as **visual markers** on the graph itself, positioned by:
- **X-axis (Horizontal)**: Event date/year
- **Y-axis (Vertical)**: Event impact/power level

---

## Visual Design

```
P(doom) Graph
│
│  ▲ Critical events (top)
│  
│  ● High impact events
│  
│  ○ Medium impact events
│  
│  · Low impact events (bottom)
│
└────────────────────────────> Time
   2020    2023    2025
   
Legend:
▲ = Critical (red)
● = High (orange) 
○ = Medium (yellow)
· = Low (green)
```

---

## Implementation Approach 1: Scatter Overlay

### Description
Add events as a scatter plot layer on top of the main P(doom) line.

### How It Works

1. **Parse CSV**: Load events with dates and impact levels
2. **Map to coordinates**: 
   - X = Year from date
   - Y = Impact level mapped to P(doom) scale (0-100)
3. **Add scatter trace**: Use Plotly's scatter mode with custom markers
4. **Add hover text**: Show event details on hover

### Code Implementation

**JavaScript to add event markers:**

```javascript
// Parse events
const eventsData = `date,model,event_type,description,impact_level
2020-06-11,GPT-3,release,OpenAI releases GPT-3 with 175B parameters,high
...`;

function parseEvents() {
  const lines = eventsData.trim().split('\\n').slice(1);
  return lines.filter(line => line.trim()).map(line => {
    const [date, model, type, desc, impact] = line.split(',');
    return { date, model, type, desc, impact };
  });
}

// Map impact to Y-position (P(doom) scale)
function impactToYPosition(impact, baselinePdoom) {
  const offsets = {
    'critical': baselinePdoom + 15,  // 15% above curve
    'high': baselinePdoom + 8,       // 8% above curve
    'medium': baselinePdoom + 3,     // 3% above curve
    'low': baselinePdoom - 2         // 2% below curve
  };
  return offsets[impact] || baselinePdoom;
}

// Create event scatter trace
function createEventTrace(events, pdoomData) {
  const eventYears = [];
  const eventYPositions = [];
  const eventTexts = [];
  const eventColors = [];
  const eventSizes = [];
  
  events.forEach(event => {
    const year = parseInt(event.date.substring(0, 4));
    
    // Find baseline P(doom) for this year
    const yearIndex = pdoomData.years.indexOf(year);
    const baselinePdoom = yearIndex >= 0 ? pdoomData.values[yearIndex] : 50;
    
    eventYears.push(year);
    eventYPositions.push(impactToYPosition(event.impact, baselinePdoom));
    
    // Hover text
    eventTexts.push(
      `<b>${event.model} - ${event.type}</b><br>` +
      `${event.date}<br>` +
      `${event.desc}<br>` +
      `<i>Impact: ${event.impact}</i>`
    );
    
    // Colors and sizes
    const impactColors = {
      'critical': '#ff4444',
      'high': '#ff6b35',
      'medium': '#ffaa00',
      'low': '#00ff41'
    };
    
    const impactSizes = {
      'critical': 20,
      'high': 14,
      'medium': 10,
      'low': 8
    };
    
    eventColors.push(impactColors[event.impact]);
    eventSizes.push(impactSizes[event.impact]);
  });
  
  return {
    x: eventYears,
    y: eventYPositions,
    mode: 'markers',
    type: 'scatter',
    name: 'OpenAI Events',
    text: eventTexts,
    hovertemplate: '%{text}<extra></extra>',
    marker: {
      size: eventSizes,
      color: eventColors,
      symbol: 'diamond',
      line: {
        color: '#00ff41',
        width: 2
      }
    }
  };
}

// Add to existing Plotly graph
function addEventsToGraph() {
  const events = parseEvents();
  
  // Get current P(doom) data from graph
  const pdoomTrace = document.getElementById('graphContainer').data[0];
  const pdoomData = {
    years: pdoomTrace.x,
    values: pdoomTrace.y
  };
  
  // Create event trace
  const eventTrace = createEventTrace(events, pdoomData);
  
  // Add trace to graph
  Plotly.addTraces('graphContainer', [eventTrace]);
}
```

### CSS for Legend

```css
.event-legend {
  position: absolute;
  top: 10px;
  right: 10px;
  background: rgba(0,0,0,0.8);
  border: 1px solid #00ff41;
  border-radius: 4px;
  padding: 10px;
  font-size: 11px;
  z-index: 10;
}

.legend-item {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 4px;
}

.legend-marker {
  width: 12px;
  height: 12px;
  border-radius: 2px;
}

.legend-marker.critical { background: #ff4444; }
.legend-marker.high { background: #ff6b35; }
.legend-marker.medium { background: #ffaa00; }
.legend-marker.low { background: #00ff41; }
```

---

## Comparison Table

| Approach | Visual Impact | Complexity | Graph Integration | Best For |
|----------|---------------|------------|-------------------|----------|
| **1. Scatter Overlay** | High | Medium | Excellent | Dense data ✅ |
| **2. Annotations** | Medium | High | Good | Few events |
| **3. Timeline Bar** | Low | Low | Separate | Overview |

---

## Recommended: Approach 1 (Scatter Overlay)

**Why:**
- ✅ Shows events in context with P(doom) curve
- ✅ Hover for details without cluttering
- ✅ Visual hierarchy by marker size
- ✅ Maintains graph readability

---

## Impact to Y-Position Mapping

```javascript
// Option A: Fixed offsets (simpler)
const offsets = {
  'critical': +15,   // 15% above curve
  'high': +8,        // 8% above curve
  'medium': +3,      // 3% above curve
  'low': -2          // 2% below curve
};

// Option B: Scaled by model power (more accurate)
const powerLevels = {
  'GPT-3': 175e9,      // 175B parameters
  'GPT-4': 1.76e12,    // ~1.76T estimated
  'GPT-5': 5e26,       // 5×10²⁶ FLOPS
  'GPT-6': 10e26       // 10×10²⁶ FLOPS
};

function calculateYPosition(event, baselinePdoom) {
  const power = powerLevels[event.model] || 1e9;
  const logPower = Math.log10(power);
  const offset = (logPower - 9) * 2; // Scale logarithmically
  return baselinePdoom + Math.min(offset, 20); // Cap at +20
}
```

---

## Implementation Files

This directory contains:
1. `scatter-overlay.html` - Scatter plot markers on graph ✅
2. `openai_history.csv` - Event data
3. `IMPLEMENTATION_GUIDE.md` - This guide

---

## Testing Checklist

- ✅ Events appear at correct years
- ✅ Y-positions reflect impact levels
- ✅ Hover shows event details
- ✅ Markers don't obscure P(doom) curve
- ✅ Colors match impact levels
- ✅ Graph remains responsive
- ✅ All 20 events visible

---

**Scatter overlay shows events on the timeline while maintaining dashboard functionality!**
