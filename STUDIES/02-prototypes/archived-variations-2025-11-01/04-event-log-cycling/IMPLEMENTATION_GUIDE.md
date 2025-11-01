# Event Log Cycling - Implementation Guide

**Variation**: 04-event-log-cycling  
**Date**: 2025-11-01  
**Feature**: Cycle through OpenAI events in the narrative text box

---

## CSV Data Structure

**File**: `openai_history.csv`  
**Location**: `pdoom1/data/openai_history.csv`

**Columns:**
- `date` - Event date (YYYY-MM-DD)
- `model` - Model name (GPT-3, GPT-4, GPT-5, etc.)
- `event_type` - Type (release, update, announcement, safety, research)
- `description` - Event description text
- `impact_level` - Impact (low, medium, high, critical)

**Total events**: 20 events from 2020-2025

---

## Current Dashboard State

**Narrative Box Location**: Bottom-right of dashboard grid  
**ID**: `#narrativeBox`  
**Current content**: Static text about P(doom) and AI risk

```html
<div id="narrativeBox">
  <div class="narrative-title">About P(doom)</div>
  <div class="narrative-text">...</div>
  <!-- Static content -->
</div>
```

---

## Method 1: Time-Based Cycling (Auto-Rotate)

### Description
Events automatically cycle every 5 seconds, showing one at a time.

### How It Works

1. **Load CSV**: Parse CSV data into JavaScript array
2. **Start interval**: `setInterval()` runs every 5000ms
3. **Update display**: Each interval shows next event
4. **Loop**: When reaching end, restart from beginning

### Code Implementation

**Step 1: Add CSV parsing function**

```javascript
let events = [];
let currentEventIndex = 0;

// Parse CSV data
async function loadEvents() {
  const response = await fetch('openai_history.csv');
  const text = await response.text();
  const lines = text.split('\n').slice(1); // Skip header
  
  events = lines
    .filter(line => line.trim())
    .map(line => {
      const [date, model, type, desc, impact] = line.split(',');
      return { date, model, type, desc, impact };
    });
  
  console.log(`[OK] Loaded ${events.length} events`);
  displayEvent(0);
}
```

**Step 2: Display function**

```javascript
function displayEvent(index) {
  if (events.length === 0) return;
  
  const event = events[index];
  const box = document.getElementById('narrativeBox');
  
  // Get color based on impact
  const impactColors = {
    'critical': '#ff4444',
    'high': '#ff6b35',
    'medium': '#ffaa00',
    'low': '#00ff41'
  };
  
  const color = impactColors[event.impact] || '#00ff41';
  
  box.innerHTML = `
    <div class="narrative-title" style="color:${color}">
      ${event.model} - ${event.type.toUpperCase()}
    </div>
    <div class="event-date">${event.date}</div>
    <div class="narrative-text">${event.desc}</div>
    <div class="event-navigation">
      Event ${index + 1} of ${events.length}
    </div>
  `;
}
```

**Step 3: Add CSS for event display**

```css
.event-date {
  font-size:11px;
  color:#00ff41;
  margin-bottom:8px;
  font-weight:bold;
  text-shadow:0 0 5px #00ff41;
}

.event-navigation {
  font-size:10px;
  color:#666;
  margin-top:12px;
  text-align:center;
  font-style:italic;
}
```

**Step 4: Start auto-cycling**

```javascript
function startAutoCycle() {
  setInterval(() => {
    currentEventIndex = (currentEventIndex + 1) % events.length;
    displayEvent(currentEventIndex);
  }, 5000); // Change every 5 seconds
}

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {
  loadEvents().then(() => {
    startAutoCycle();
  });
});
```

### Pros/Cons

**Pros:**
- ✅ Fully automatic
- ✅ Simple to implement
- ✅ User sees all events over time

**Cons:**
- ❌ No user control
- ❌ May change while user reading
- ❌ Not synchronized with graph

---

## Method 2: Year-Based Cycling (Graph Slider)

### Description
Events change when user moves the year slider, showing events for that year.

### How It Works

1. **Load CSV**: Parse and group events by year
2. **Listen to slider**: Detect slider value changes
3. **Filter events**: Show only events matching selected year
4. **Cycle within year**: If multiple events, rotate through them

### Code Implementation

**Step 1: Group events by year**

```javascript
let eventsByYear = {};
let currentYear = 2020;
let yearEventIndex = 0;

function groupEventsByYear() {
  eventsByYear = {};
  
  events.forEach(event => {
    const year = parseInt(event.date.substring(0, 4));
    if (!eventsByYear[year]) {
      eventsByYear[year] = [];
    }
    eventsByYear[year].push(event);
  });
  
  console.log('[OK] Events grouped by year:', Object.keys(eventsByYear));
}
```

**Step 2: Display events for year**

```javascript
function displayEventsForYear(year) {
  const yearEvents = eventsByYear[year] || [];
  
  if (yearEvents.length === 0) {
    document.getElementById('narrativeBox').innerHTML = `
      <div class="narrative-title">Year ${year}</div>
      <div class="narrative-text" style="opacity:0.5">
        No OpenAI events recorded for this year.
      </div>
    `;
    return;
  }
  
  // Show first event for this year
  yearEventIndex = 0;
  displayYearEvent(year, yearEventIndex);
  
  // If multiple events, cycle through them
  if (yearEvents.length > 1) {
    cycleYearEvents(year);
  }
}

function displayYearEvent(year, index) {
  const yearEvents = eventsByYear[year];
  if (!yearEvents || index >= yearEvents.length) return;
  
  const event = yearEvents[index];
  const impactColors = {
    'critical': '#ff4444',
    'high': '#ff6b35',
    'medium': '#ffaa00',
    'low': '#00ff41'
  };
  
  const color = impactColors[event.impact] || '#00ff41';
  
  document.getElementById('narrativeBox').innerHTML = `
    <div class="narrative-title" style="color:${color}">
      ${event.model} - ${event.type.toUpperCase()}
    </div>
    <div class="event-date">${event.date}</div>
    <div class="narrative-text">${event.desc}</div>
    ${yearEvents.length > 1 ? `
      <div class="event-navigation">
        Event ${index + 1} of ${yearEvents.length} in ${year}
      </div>
    ` : ''}
  `;
}

let yearCycleInterval = null;

function cycleYearEvents(year) {
  // Clear previous interval
  if (yearCycleInterval) {
    clearInterval(yearCycleInterval);
  }
  
  const yearEvents = eventsByYear[year];
  
  yearCycleInterval = setInterval(() => {
    yearEventIndex = (yearEventIndex + 1) % yearEvents.length;
    displayYearEvent(year, yearEventIndex);
  }, 4000); // Cycle every 4 seconds
}
```

**Step 3: Connect to slider**

Find existing slider code (around line 700):

```javascript
// Existing slider for pdoom value
const slider = document.getElementById('pdoomSlider');
slider.addEventListener('input', function(e) {
  const year = parseInt(e.target.value);
  currentYear = year;
  
  // Update graph (existing code)
  updateGraph();
  
  // NEW: Update events display
  displayEventsForYear(year);
});
```

**Step 4: Initialize**

```javascript
window.addEventListener('DOMContentLoaded', () => {
  loadEvents().then(() => {
    groupEventsByYear();
    
    // Show events for initial year
    const initialYear = document.getElementById('pdoomSlider').value || 2020;
    displayEventsForYear(parseInt(initialYear));
  });
});
```

### Pros/Cons

**Pros:**
- ✅ Synchronized with graph
- ✅ Shows relevant events for selected year
- ✅ User controls when events change

**Cons:**
- ❌ Requires slider interaction
- ❌ More complex implementation
- ❌ Some years may have no events

---

## Method 3: Hybrid (Auto + Manual)

### Description
Combines both: auto-cycles through all events, but user can pause and filter by year.

### Additional Controls

Add play/pause button and year filter:

```html
<div id="narrativeBox">
  <div class="event-controls">
    <button id="playPauseBtn" class="event-btn">⏸ Pause</button>
    <label>
      <input type="checkbox" id="filterByYear"> Filter by slider year
    </label>
  </div>
  <div id="eventContent">
    <!-- Event content here -->
  </div>
</div>
```

**CSS for controls:**

```css
.event-controls {
  display:flex;
  justify-content:space-between;
  align-items:center;
  margin-bottom:10px;
  padding-bottom:10px;
  border-bottom:1px solid #00ff41;
}

.event-btn {
  background:rgba(0,255,65,0.2);
  border:1px solid #00ff41;
  color:#00ff41;
  padding:4px 12px;
  border-radius:4px;
  cursor:pointer;
  font-family:'Courier New',monospace;
  font-size:11px;
  transition:all 150ms;
}

.event-btn:hover {
  background:rgba(0,255,65,0.4);
  box-shadow:0 0 10px #00ff41;
}
```

**JavaScript for hybrid mode:**

```javascript
let isPlaying = true;
let filterByYear = false;

document.getElementById('playPauseBtn').addEventListener('click', () => {
  isPlaying = !isPlaying;
  const btn = document.getElementById('playPauseBtn');
  
  if (isPlaying) {
    btn.textContent = '⏸ Pause';
    startAutoCycle();
  } else {
    btn.textContent = '▶ Play';
    if (yearCycleInterval) clearInterval(yearCycleInterval);
  }
});

document.getElementById('filterByYear').addEventListener('change', (e) => {
  filterByYear = e.target.checked;
  
  if (filterByYear) {
    // Switch to year-based mode
    const year = document.getElementById('pdoomSlider').value || 2020;
    displayEventsForYear(parseInt(year));
  } else {
    // Switch back to all events
    displayEvent(currentEventIndex);
  }
});
```

---

## Comparison Table

| Method | User Control | Complexity | Graph Sync | Best For |
|--------|--------------|------------|------------|----------|
| **1. Time-Based** | Low | Low | No | Ambient info display |
| **2. Year-Based** | High | Medium | Yes | Interactive exploration ✅ |
| **3. Hybrid** | High | High | Optional | Power users |

---

## Recommended: Method 2 (Year-Based)

**Why:**
- ✅ Matches dashboard's interactive nature
- ✅ Events relevant to graph position
- ✅ User feels in control
- ✅ Educational - see events by timeline

---

## CSV Loading Notes

### Option A: Inline Data (Simplest)

Embed CSV data directly in JavaScript:

```javascript
const eventsData = `date,model,event_type,description,impact_level
2020-06-11,GPT-3,release,OpenAI releases GPT-3 with 175B parameters,high
2022-11-30,ChatGPT,release,ChatGPT launches and reaches 1M users in 5 days,high
...`;

function parseInlineCSV() {
  const lines = eventsData.trim().split('\n').slice(1);
  events = lines.map(line => {
    const [date, model, type, desc, impact] = line.split(',');
    return { date, model, type, desc, impact };
  });
}
```

**Pros**: No HTTP request, works offline  
**Cons**: Data in HTML file (harder to update)

### Option B: Fetch CSV (Cleaner)

Load from external file:

```javascript
async function loadEvents() {
  try {
    const response = await fetch('openai_history.csv');
    const text = await response.text();
    // Parse as shown above
  } catch (error) {
    console.error('[ERROR] Failed to load events:', error);
    // Fallback to inline data
    parseInlineCSV();
  }
}
```

**Pros**: Cleaner separation, easy to update CSV  
**Cons**: Requires HTTP server (or file:// protocol issues)

---

## Implementation Files

This directory contains:
1. `method1-time-based.html` - Auto-cycling every 5s
2. `method2-year-based.html` - Synced with graph slider ✅
3. `method3-hybrid.html` - Both modes with controls
4. `openai_history.csv` - Event data

---

## Testing Checklist

For each method:
- ✅ Events load correctly
- ✅ Text displays in narrative box
- ✅ Colors match impact level
- ✅ Cycling works smoothly
- ✅ No console errors
- ✅ Graph still functions
- ✅ Other dashboard features intact

---

## Quick Implementation (Method 2)

1. **Copy CSV** to dashboard directory
2. **Add CSS** for event display (date, navigation)
3. **Add JavaScript** for CSV parsing and year grouping
4. **Connect to slider** to trigger event display
5. **Test** by moving slider and watching events change

Done! Events now cycle based on graph year.

---

**All methods maintain full dashboard functionality while adding dynamic event display!**
