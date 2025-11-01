#!/usr/bin/env python3
"""
Create timeline event overlay variation for pdoom dashboard
Displays events as scatter plot markers on the P(doom) graph
"""

from pathlib import Path

BASE_FILE = Path("dashboard-timeline.html")
CSV_FILE = Path("openai_history.csv")

# Read CSV data to embed
with open(CSV_FILE) as f:
    csv_data = f.read().strip()

def create_scatter_overlay():
    """Scatter plot markers overlaid on graph"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS for legend
    css_addition = """
  .event-legend {
    position:absolute;
    top:10px;
    right:10px;
    background:rgba(0,0,0,0.8);
    border:1px solid #00ff41;
    border-radius:4px;
    padding:10px;
    font-size:11px;
    z-index:10;
  }

  .legend-item {
    display:flex;
    align-items:center;
    gap:8px;
    margin-bottom:4px;
  }

  .legend-marker {
    width:12px;
    height:12px;
    border-radius:2px;
  }

  .legend-marker.critical { background:#ff4444; }
  .legend-marker.high { background:#ff6b35; }
  .legend-marker.medium { background:#ffaa00; }
  .legend-marker.low { background:#00ff41; }
"""
    
    content = content.replace('</style>', css_addition + '</style>')
    
    # Add legend HTML to graph container
    legend_html = '''
<!-- Event Legend -->
<div class="event-legend">
  <div style="margin-bottom:8px;font-weight:bold;color:#00ff41;">OpenAI Events</div>
  <div class="legend-item">
    <div class="legend-marker critical"></div>
    <span>Critical</span>
  </div>
  <div class="legend-item">
    <div class="legend-marker high"></div>
    <span>High Impact</span>
  </div>
  <div class="legend-item">
    <div class="legend-marker medium"></div>
    <span>Medium</span>
  </div>
  <div class="legend-item">
    <div class="legend-marker low"></div>
    <span>Low</span>
  </div>
</div>
'''
    
    # Insert legend after graph container opens
    content = content.replace('<div id="graphContainer">', 
                            '<div id="graphContainer" style="position:relative;">\n' + legend_html)
    
    # Add JavaScript for event overlay
    js_code = f"""
<script>
// Inline CSV data
const eventsData = `{csv_data}`;

let events = [];

// Parse events
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
  console.log(`[OK] Loaded ${{events.length}} events for overlay`);
}}

// Map impact to Y-position offset
function impactToYPosition(impact, baselinePdoom) {{
  const offsets = {{
    'critical': 15,   // 15% above curve
    'high': 8,        // 8% above curve
    'medium': 3,      // 3% above curve
    'low': -2         // 2% below curve
  }};
  const offset = offsets[impact] || 0;
  return Math.min(Math.max(baselinePdoom + offset, 0), 100); // Clamp 0-100
}}

// Create event scatter trace
function createEventTrace(pdoomYears, pdoomValues) {{
  const eventYears = [];
  const eventYPositions = [];
  const eventTexts = [];
  const eventColors = [];
  const eventSizes = [];
  const eventSymbols = [];
  
  events.forEach(event => {{
    const year = parseInt(event.date.substring(0, 4));
    
    // Find baseline P(doom) for this year (interpolate if needed)
    let baselinePdoom = 50;
    const yearIndex = pdoomYears.indexOf(year);
    
    if (yearIndex >= 0) {{
      baselinePdoom = pdoomValues[yearIndex];
    }} else {{
      // Interpolate between nearest years
      for (let i = 0; i < pdoomYears.length - 1; i++) {{
        if (year > pdoomYears[i] && year < pdoomYears[i + 1]) {{
          const ratio = (year - pdoomYears[i]) / (pdoomYears[i + 1] - pdoomYears[i]);
          baselinePdoom = pdoomValues[i] + ratio * (pdoomValues[i + 1] - pdoomValues[i]);
          break;
        }}
      }}
    }}
    
    eventYears.push(year);
    eventYPositions.push(impactToYPosition(event.impact, baselinePdoom));
    
    // Hover text with HTML formatting
    eventTexts.push(
      `<b>${{event.model}} - ${{event.type.toUpperCase()}}</b><br>` +
      `${{event.date}}<br>` +
      `${{event.desc}}<br>` +
      `<i>Impact: ${{event.impact}}</i>`
    );
    
    // Colors by impact
    const impactColors = {{
      'critical': '#ff4444',
      'high': '#ff6b35',
      'medium': '#ffaa00',
      'low': '#00ff41'
    }};
    eventColors.push(impactColors[event.impact]);
    
    // Sizes by impact
    const impactSizes = {{
      'critical': 20,
      'high': 14,
      'medium': 10,
      'low': 8
    }};
    eventSizes.push(impactSizes[event.impact]);
    
    // Symbols by impact
    const impactSymbols = {{
      'critical': 'star',
      'high': 'diamond',
      'medium': 'circle',
      'low': 'circle-open'
    }};
    eventSymbols.push(impactSymbols[event.impact]);
  }});
  
  return {{
    x: eventYears,
    y: eventYPositions,
    mode: 'markers',
    type: 'scatter',
    name: 'OpenAI Events',
    text: eventTexts,
    hovertemplate: '%{{text}}<extra></extra>',
    marker: {{
      size: eventSizes,
      color: eventColors,
      symbol: eventSymbols,
      line: {{
        color: '#00ff41',
        width: 1
      }},
      opacity: 0.9
    }}
  }};
}}

// Hook into existing graph creation
// Wait for Plotly to finish drawing, then add events
const originalUpdate = window.updateGraph || function() {{}};

window.updateGraph = function() {{
  // Call original update if it exists
  if (originalUpdate) originalUpdate();
  
  // Wait a bit for graph to render
  setTimeout(() => {{
    try {{
      const graphDiv = document.getElementById('graphContainer');
      if (!graphDiv || !graphDiv.data || graphDiv.data.length === 0) {{
        console.log('[WARN] Graph not ready yet');
        return;
      }}
      
      // Get P(doom) trace (should be first trace)
      const pdoomTrace = graphDiv.data[0];
      const pdoomYears = pdoomTrace.x;
      const pdoomValues = pdoomTrace.y;
      
      // Create event trace
      const eventTrace = createEventTrace(pdoomYears, pdoomValues);
      
      // Check if events already added (avoid duplicates)
      const hasEvents = graphDiv.data.some(trace => trace.name === 'OpenAI Events');
      
      if (!hasEvents) {{
        Plotly.addTraces('graphContainer', [eventTrace]);
        console.log('[OK] Added event markers to graph');
      }}
    }} catch (error) {{
      console.error('[ERROR] Failed to add events:', error);
    }}
  }}, 500);
}};

// Initialize on page load
window.addEventListener('DOMContentLoaded', () => {{
  parseEvents();
  
  // Try to add events after a delay (in case graph loads late)
  setTimeout(() => {{
    if (window.updateGraph) {{
      window.updateGraph();
    }}
  }}, 1000);
}});
</script>
"""
    
    # Insert before closing body tag
    content = content.replace('</body>', js_code + '\n</body>')
    
    with open("scatter-overlay.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created scatter-overlay.html")

if __name__ == "__main__":
    if not BASE_FILE.exists():
        print(f"[ERROR] {BASE_FILE} not found!")
        exit(1)
    
    if not CSV_FILE.exists():
        print(f"[ERROR] {CSV_FILE} not found!")
        exit(1)
    
    create_scatter_overlay()
    
    print("\n[OK] Timeline event overlay created!")
    print("File: scatter-overlay.html")
    print("\nOpen in browser to see events overlaid on P(doom) graph.")
    print("Hover over markers to see event details.")
