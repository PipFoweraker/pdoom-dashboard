#!/usr/bin/env python3
"""
Create 3 event log cycling variations for pdoom dashboard
"""

import re
from pathlib import Path

BASE_FILE = Path("dashboard-events.html")
CSV_FILE = Path("openai_history.csv")

# Read CSV data to embed
with open(CSV_FILE) as f:
    csv_data = f.read().strip()

def create_method1_time_based():
    """Method 1: Auto-cycle every 5 seconds"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS for event display
    css_addition = """
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
"""
    
    content = content.replace('</style>', css_addition + '</style>')
    
    # Add JavaScript for time-based cycling
    js_code = f"""
<script>
// Inline CSV data
const eventsData = `{csv_data}`;

let events = [];
let currentEventIndex = 0;

// Parse CSV
function parseEvents() {{
  const lines = eventsData.trim().split('\\n').slice(1);
  events = lines
    .filter(line => line.trim())
    .map(line => {{
      const parts = line.split(',');
      return {{
        date: parts[0],
        model: parts[1],
        type: parts[2],
        desc: parts[3],
        impact: parts[4]
      }};
    }});
  console.log(`[OK] Loaded ${{events.length}} events`);
}}

// Display event
function displayEvent(index) {{
  if (events.length === 0) return;
  
  const event = events[index];
  const box = document.getElementById('narrativeBox');
  
  const impactColors = {{
    'critical': '#ff4444',
    'high': '#ff6b35',
    'medium': '#ffaa00',
    'low': '#00ff41'
  }};
  
  const color = impactColors[event.impact] || '#00ff41';
  
  box.innerHTML = `
    <div class="narrative-title" style="color:${{color}}">
      ${{event.model}} - ${{event.type.toUpperCase()}}
    </div>
    <div class="event-date">${{event.date}}</div>
    <div class="narrative-text">${{event.desc}}</div>
    <div class="event-navigation">
      Event ${{index + 1}} of ${{events.length}}
    </div>
  `;
}}

// Start auto-cycling
function startAutoCycle() {{
  setInterval(() => {{
    currentEventIndex = (currentEventIndex + 1) % events.length;
    displayEvent(currentEventIndex);
  }}, 5000);
}}

// Initialize
window.addEventListener('DOMContentLoaded', () => {{
  parseEvents();
  displayEvent(0);
  startAutoCycle();
}});
</script>
"""
    
    # Insert before closing body tag
    content = content.replace('</body>', js_code + '\n</body>')
    
    with open("method1-time-based.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created method1-time-based.html")

def create_method2_year_based():
    """Method 2: Sync with graph slider"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS
    css_addition = """
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
"""
    
    content = content.replace('</style>', css_addition + '</style>')
    
    # Add JavaScript for year-based cycling
    js_code = f"""
<script>
// Inline CSV data
const eventsData = `{csv_data}`;

let events = [];
let eventsByYear = {{}};
let currentYear = 2020;
let yearEventIndex = 0;
let yearCycleInterval = null;

// Parse CSV
function parseEvents() {{
  const lines = eventsData.trim().split('\\n').slice(1);
  events = lines
    .filter(line => line.trim())
    .map(line => {{
      const parts = line.split(',');
      return {{
        date: parts[0],
        model: parts[1],
        type: parts[2],
        desc: parts[3],
        impact: parts[4]
      }};
    }});
  console.log(`[OK] Loaded ${{events.length}} events`);
}}

// Group by year
function groupByYear() {{
  eventsByYear = {{}};
  events.forEach(event => {{
    const year = parseInt(event.date.substring(0, 4));
    if (!eventsByYear[year]) {{
      eventsByYear[year] = [];
    }}
    eventsByYear[year].push(event);
  }});
  console.log('[OK] Events grouped by year:', Object.keys(eventsByYear));
}}

// Display year event
function displayYearEvent(year, index) {{
  const yearEvents = eventsByYear[year];
  if (!yearEvents || index >= yearEvents.length) return;
  
  const event = yearEvents[index];
  const impactColors = {{
    'critical': '#ff4444',
    'high': '#ff6b35',
    'medium': '#ffaa00',
    'low': '#00ff41'
  }};
  
  const color = impactColors[event.impact] || '#00ff41';
  const box = document.getElementById('narrativeBox');
  
  box.innerHTML = `
    <div class="narrative-title" style="color:${{color}}">
      ${{event.model}} - ${{event.type.toUpperCase()}}
    </div>
    <div class="event-date">${{event.date}}</div>
    <div class="narrative-text">${{event.desc}}</div>
    ${{yearEvents.length > 1 ? `
      <div class="event-navigation">
        Event ${{index + 1}} of ${{yearEvents.length}} in ${{year}}
      </div>
    ` : ''}}
  `;
}}

// Display events for year
function displayEventsForYear(year) {{
  const yearEvents = eventsByYear[year] || [];
  
  if (yearEvents.length === 0) {{
    document.getElementById('narrativeBox').innerHTML = `
      <div class="narrative-title">Year ${{year}}</div>
      <div class="narrative-text" style="opacity:0.5">
        No OpenAI events recorded for this year.
      </div>
    `;
    return;
  }}
  
  yearEventIndex = 0;
  displayYearEvent(year, yearEventIndex);
  
  // Cycle if multiple events
  if (yearEvents.length > 1) {{
    if (yearCycleInterval) clearInterval(yearCycleInterval);
    
    yearCycleInterval = setInterval(() => {{
      yearEventIndex = (yearEventIndex + 1) % yearEvents.length;
      displayYearEvent(year, yearEventIndex);
    }}, 4000);
  }}
}}

// Hook into slider - find existing slider listener and extend it
window.addEventListener('DOMContentLoaded', () => {{
  parseEvents();
  groupByYear();
  
  // Find slider and add event listener
  const slider = document.getElementById('pdoomSlider');
  if (slider) {{
    slider.addEventListener('input', function(e) {{
      const year = parseInt(e.target.value);
      displayEventsForYear(year);
    }});
    
    // Show initial year
    const initialYear = parseInt(slider.value) || 2020;
    displayEventsForYear(initialYear);
  }}
}});
</script>
"""
    
    content = content.replace('</body>', js_code + '\n</body>')
    
    with open("method2-year-based.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created method2-year-based.html")

def create_method3_hybrid():
    """Method 3: Both modes with controls"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS
    css_addition = """
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

  .event-filter {
    font-size:10px;
    color:#cccccc;
  }

  .event-filter input {
    margin-right:5px;
  }
"""
    
    content = content.replace('</style>', css_addition + '</style>')
    
    # Modify narrative box HTML to add controls
    narrative_pattern = r'(<div id="narrativeBox">)(.*?)(</div>\s*</div>\s*<!-- Event log -->)'
    
    new_narrative = r'''<div id="narrativeBox">
  <div class="event-controls">
    <button id="playPauseBtn" class="event-btn">⏸ Pause</button>
    <label class="event-filter">
      <input type="checkbox" id="filterByYear"> Filter by slider year
    </label>
  </div>
  <div id="eventContent"></div>
</div>
</div><!-- Event log -->'''
    
    content = re.sub(narrative_pattern, new_narrative, content, flags=re.DOTALL)
    
    # Add comprehensive JavaScript
    js_code = f"""
<script>
// Inline CSV data
const eventsData = `{csv_data}`;

let events = [];
let eventsByYear = {{}};
let currentEventIndex = 0;
let yearEventIndex = 0;
let currentYear = 2020;
let isPlaying = true;
let filterByYear = false;
let autoCycleInterval = null;
let yearCycleInterval = null;

// Parse CSV
function parseEvents() {{
  const lines = eventsData.trim().split('\\n').slice(1);
  events = lines
    .filter(line => line.trim())
    .map(line => {{
      const parts = line.split(',');
      return {{
        date: parts[0],
        model: parts[1],
        type: parts[2],
        desc: parts[3],
        impact: parts[4]
      }};
    }});
  
  // Group by year
  eventsByYear = {{}};
  events.forEach(event => {{
    const year = parseInt(event.date.substring(0, 4));
    if (!eventsByYear[year]) {{
      eventsByYear[year] = [];
    }}
    eventsByYear[year].push(event);
  }});
  
  console.log(`[OK] Loaded ${{events.length}} events`);
}}

// Display event (all events mode)
function displayEvent(index) {{
  if (events.length === 0) return;
  
  const event = events[index];
  const impactColors = {{
    'critical': '#ff4444',
    'high': '#ff6b35',
    'medium': '#ffaa00',
    'low': '#00ff41'
  }};
  
  const color = impactColors[event.impact] || '#00ff41';
  
  document.getElementById('eventContent').innerHTML = `
    <div class="narrative-title" style="color:${{color}}">
      ${{event.model}} - ${{event.type.toUpperCase()}}
    </div>
    <div class="event-date">${{event.date}}</div>
    <div class="narrative-text">${{event.desc}}</div>
    <div class="event-navigation">
      Event ${{index + 1}} of ${{events.length}}
    </div>
  `;
}}

// Display year event
function displayYearEvent(year, index) {{
  const yearEvents = eventsByYear[year];
  if (!yearEvents || index >= yearEvents.length) return;
  
  const event = yearEvents[index];
  const impactColors = {{
    'critical': '#ff4444',
    'high': '#ff6b35',
    'medium': '#ffaa00',
    'low': '#00ff41'
  }};
  
  const color = impactColors[event.impact] || '#00ff41';
  
  document.getElementById('eventContent').innerHTML = `
    <div class="narrative-title" style="color:${{color}}">
      ${{event.model}} - ${{event.type.toUpperCase()}}
    </div>
    <div class="event-date">${{event.date}}</div>
    <div class="narrative-text">${{event.desc}}</div>
    ${{yearEvents.length > 1 ? `
      <div class="event-navigation">
        Event ${{index + 1}} of ${{yearEvents.length}} in ${{year}}
      </div>
    ` : ''}}
  `;
}}

// Start auto cycle (all events)
function startAutoCycle() {{
  if (autoCycleInterval) clearInterval(autoCycleInterval);
  
  autoCycleInterval = setInterval(() => {{
    currentEventIndex = (currentEventIndex + 1) % events.length;
    displayEvent(currentEventIndex);
  }}, 5000);
}}

// Display events for year
function displayEventsForYear(year) {{
  const yearEvents = eventsByYear[year] || [];
  
  if (yearEvents.length === 0) {{
    document.getElementById('eventContent').innerHTML = `
      <div class="narrative-title">Year ${{year}}</div>
      <div class="narrative-text" style="opacity:0.5">
        No OpenAI events recorded for this year.
      </div>
    `;
    return;
  }}
  
  yearEventIndex = 0;
  displayYearEvent(year, yearEventIndex);
  
  // Cycle if multiple
  if (yearEvents.length > 1) {{
    if (yearCycleInterval) clearInterval(yearCycleInterval);
    
    yearCycleInterval = setInterval(() => {{
      yearEventIndex = (yearEventIndex + 1) % yearEvents.length;
      displayYearEvent(year, yearEventIndex);
    }}, 4000);
  }}
}}

// Initialize
window.addEventListener('DOMContentLoaded', () => {{
  parseEvents();
  displayEvent(0);
  startAutoCycle();
  
  // Play/Pause button
  document.getElementById('playPauseBtn').addEventListener('click', () => {{
    isPlaying = !isPlaying;
    const btn = document.getElementById('playPauseBtn');
    
    if (isPlaying) {{
      btn.textContent = '⏸ Pause';
      if (filterByYear) {{
        const year = parseInt(document.getElementById('pdoomSlider').value) || 2020;
        displayEventsForYear(year);
      }} else {{
        startAutoCycle();
      }}
    }} else {{
      btn.textContent = '▶ Play';
      if (autoCycleInterval) clearInterval(autoCycleInterval);
      if (yearCycleInterval) clearInterval(yearCycleInterval);
    }}
  }});
  
  // Filter checkbox
  document.getElementById('filterByYear').addEventListener('change', (e) => {{
    filterByYear = e.target.checked;
    
    if (autoCycleInterval) clearInterval(autoCycleInterval);
    if (yearCycleInterval) clearInterval(yearCycleInterval);
    
    if (filterByYear) {{
      const year = parseInt(document.getElementById('pdoomSlider').value) || 2020;
      displayEventsForYear(year);
    }} else {{
      displayEvent(currentEventIndex);
      if (isPlaying) startAutoCycle();
    }}
  }});
  
  // Hook into slider
  const slider = document.getElementById('pdoomSlider');
  if (slider) {{
    slider.addEventListener('input', function(e) {{
      if (filterByYear) {{
        const year = parseInt(e.target.value);
        displayEventsForYear(year);
      }}
    }});
  }}
}});
</script>
"""
    
    content = content.replace('</body>', js_code + '\n</body>')
    
    with open("method3-hybrid.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created method3-hybrid.html")

if __name__ == "__main__":
    if not BASE_FILE.exists():
        print(f"[ERROR] {BASE_FILE} not found!")
        exit(1)
    
    if not CSV_FILE.exists():
        print(f"[ERROR] {CSV_FILE} not found!")
        exit(1)
    
    create_method1_time_based()
    create_method2_year_based()
    create_method3_hybrid()
    
    print("\n[OK] All 3 event cycling methods created!")
    print("Files: method1-time-based.html, method2-year-based.html, method3-hybrid.html")
