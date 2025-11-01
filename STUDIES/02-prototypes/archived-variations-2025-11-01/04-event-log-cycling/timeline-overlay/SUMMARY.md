# Timeline Event Overlay - Summary

**Location**: `04-event-log-cycling/timeline-overlay/`  
**Created**: 2025-11-01  
**Status**: ✅ Complete

---

## What This Does

Displays OpenAI events as **visual markers overlaid on the P(doom) graph**, positioned by:
- **X-axis**: Event year (2020-2025)
- **Y-axis**: Event impact level (offset from P(doom) curve)

---

## Files Created

1. **scatter-overlay.html** (38KB) - Working dashboard with event markers ✅
2. **IMPLEMENTATION_GUIDE.md** - Complete technical guide
3. **create_timeline_overlay.py** - Generation script
4. **openai_history.csv** - 20 event data points

---

## How It Works

### Event Positioning

**Y-axis offset from P(doom) curve:**
- **Critical events** (★ red): +15% above curve (GPT-5, GPT-6 releases)
- **High events** (◆ orange): +8% above curve (most major releases)
- **Medium events** (● yellow): +3% above curve (API releases, updates)
- **Low events** (○ green): -2% below curve (minor updates)

**Marker sizes:**
- Critical: 20px
- High: 14px
- Medium: 10px
- Low: 8px

**Marker symbols:**
- Critical: Star (★)
- High: Diamond (◆)
- Medium: Filled circle (●)
- Low: Open circle (○)

### Visual Features

✅ **Legend** in top-right corner shows impact levels  
✅ **Hover tooltips** display full event details  
✅ **Color-coded** by impact (red/orange/yellow/green)  
✅ **Size-scaled** by importance  
✅ **Non-intrusive** - doesn't obscure the main curve  

---

## Event Distribution

**By Year:**
- 2020: 1 event (GPT-3)
- 2022: 1 event (ChatGPT)
- 2023: 3 events (GPT-4 series)
- 2024: 5 events (Sora, o1, GPT-5)
- 2025: 10 events (GPT-5/GPT-6 era)

**By Impact:**
- Critical: 2 events (GPT-5, GPT-6 releases)
- High: 11 events (major releases)
- Medium: 7 events (updates, APIs)
- Low: 0 events (none in dataset)

---

## Technical Implementation

**Method**: Plotly scatter trace overlaid on main line graph

**Key Code:**
1. Parse CSV data embedded in JavaScript
2. Map each event to (year, y-position) coordinates
3. Y-position = baseline P(doom) for that year + impact offset
4. Create scatter trace with custom markers
5. Use `Plotly.addTraces()` to overlay on existing graph

**Advantages:**
- ✅ Native Plotly integration
- ✅ Smooth hover interactions
- ✅ Responsive (zooms with graph)
- ✅ No performance impact
- ✅ Easy to update data

---

## Usage

1. **Open** `scatter-overlay.html` in Firefox
2. **Observe** event markers on the P(doom) timeline
3. **Hover** over markers to see event details
4. **Interact** with sliders - markers stay positioned correctly
5. **Legend** shows what each color/size means

---

## Comparison with Text Cycling

| Feature | Text Cycling | Timeline Overlay |
|---------|--------------|------------------|
| **Visual context** | None | Shows events in timeline |
| **All events visible** | No (cycles) | Yes (all at once) |
| **Temporal relationship** | Hidden | Clear |
| **Impact hierarchy** | Text only | Visual (size/color) |
| **Space used** | Text box | Graph area |
| **Interactivity** | Click/wait | Hover |
| **Best for** | Reading details | Overview + context |

**Recommendation**: Use **both** - timeline overlay for context, text box for selected event details.

---

## Future Enhancements

Possible additions:
- Click marker to show details in narrative box
- Filter events by type (release, update, research)
- Animate markers appearing in sequence
- Connect related events with lines (GPT-5 → GPT-6)
- Add more event sources (Anthropic, Google, etc.)

---

**The scatter overlay provides immediate visual context for AI development milestones on the P(doom) timeline!**
