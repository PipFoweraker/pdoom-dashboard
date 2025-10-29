# P(doom) Dashboard Project

**AI Existential Risk Visualization Suite**

---

## Overview

This project is a collection of interactive dashboard prototypes designed to visualize and communicate the probability of existential catastrophe from artificial intelligence (P(doom)). The dashboards combine real-time data, expert estimates, and dynamic visualizations to educate and inform about AI safety risks.

## What Was Requested

The initial request was to create an interactive P(doom) dashboard that:

1. **Visualizes exponential AI scaling** - Show training compute growth and its correlation with risk
2. **Displays expert consensus** - Include estimates from leading AI researchers
3. **Allows parameter adjustment** - Interactive sliders to explore how safety investment, coordination, and regulation affect risk trajectories
4. **Uses pdoom1.com aesthetic** - Dark cyberpunk terminal style with matrix green (#00ff41) accent colors
5. **Includes real-world data** - AI company stocks, model release dates, compute metrics
6. **Provides educational context** - Links to research, clear explanations of concepts
7. **Creates engaging visualizations** - WebGL shaders showing risk concepts (misalignment, coordination failure, intelligence explosion)

## What Currently Exists

### 📊 Main Dashboards

#### **STAGE2_DASHBOARD.html** (Current Production Version)
Located: `/variations/STAGE2_DASHBOARD.html`

**Features:**
- ✅ Dual-axis P(doom) and training compute graph
- ✅ Warning lights for milestone dates (GPT-4/5 releases, P(doom) thresholds)
- ✅ Adjustment sliders (AI Safety Investment, International Coordination, Regulatory Strength)
- ✅ Real-time AI company stock tickers (NVIDIA, Microsoft, Alphabet, Meta)
- ✅ Expert P(doom) estimates with Wikipedia links
- ✅ Country compute distribution pie chart
- ✅ Dynamic narrative text box describing current situation
- ✅ Neural mesh shader that transitions green→orange→red as P(doom) increases
- ✅ Draggable panels for customization
- ✅ Cat cam with pdoom1 assets
- ✅ Clickable source links to research papers and organizations

**Technical:**
- Pure HTML/CSS/JavaScript (no build system required)
- Plotly.js for interactive charts
- WebGL fragment shaders for background effects
- Follows pdoom1.com color palette and design language

### 🧪 Development Prototypes

Located: `/variations/IN_DEVELOPMENT/`

These represent the iterative development process:

| File | Description | Key Features |
|------|-------------|--------------|
| **pdoom_dashboard_v4.html** | Split layout prototype | First version with pie chart + narrative box |
| **pdoom_dashboard_v3.html** | High contrast version | Transparency experiments |
| **pdoom_dashboard_final.html** | Pre-split version | AI stocks + sliders |
| **pdoom_mission_control_final.html** | Mission control style | Cat cam integration |
| **ai_mission_control_full.html** | Early mission control | Widget experiments |
| **pdoom_main_compute_secondary.html** | Compute secondary axis | Dual Y-axis testing |
| **openai_compute_*.html** | Various scaling views | Linear, normalized, relative, canvas versions |

### 🎨 Visual Experiments

Located: `/variations/shaders/`

**P(doom) Concept Shaders:**
- `exponential_escalation.html` - Shows capability doubling via expanding rings
- `misalignment_pattern.html` - Visualizes human vs AI objective divergence
- `intelligence_explosion.html` - Recursive self-improvement singularity
- `coordination_failure.html` - Multiple competing actors, prisoner's dilemma
- `takeoff_speed.html` - Slow→fast transition with acceleration

**Fun/Themed Shaders:**
- `bouncing_cat_screensaver.html` - DVD-logo style bouncing cat
- `cat_laser_eyes.html` - Cat shooting laser beams
- `cat_chase_laser.html` - Interactive cat chasing laser pointer
- `oldschool_pdoom_windows.html` - Windows 95/98 screensaver aesthetic
- `pdoom_halloween.html` - Halloween special with pumpkins, ghosts, bats

**Original Experiments:**
- `neural_mesh.html` / `neural_mesh_pdoom1.html` - Neural network visualizations
- `cellular_flow.html` / `organic_circuits.html` - Organic growth patterns
- `discontinuity_shift.html` - Sudden regime changes

### 📁 Early Prototypes

Located: `/1ST_PROTOTYPES/`

Initial exploration of visualization approaches:
- `DOOMPLOT.html` - Basic P(doom) curve
- `DG.html` / `DJ.html` - Data visualization experiments
- `plotty4.html` / `plotnasty.html` - Plotting library tests

### 📚 Documentation

- **PDOOM1_STYLE_GUIDE.md** - Complete visual design system extracted from pdoom1.com
  - Color palette (matrix green, warning orange, error red)
  - Typography (Courier New monospace)
  - Spacing system, shadows, animations
  - Component patterns (panels, buttons, metrics)
  - Accessibility guidelines

- **Early_opinions.txt** - Initial design considerations

## Software/Libraries Used

### Core Technologies
- **HTML5 + CSS3** - Layout and styling
- **JavaScript (ES6+)** - Interactivity and logic
- **WebGL** - Fragment shaders for visual effects

### Libraries
- **Plotly.js** (v2.32.0) - Interactive charting
  - Used for: Dual-axis graphs, pie charts, annotations
  - Pros: Rich interactivity, no external dependencies beyond one CDN link
  - Cons: Large file size (~3MB), limited shader/3D integration

### Design System
- **Monospace fonts**: Courier New (terminal aesthetic)
- **Color system**: Based on pdoom1.com (see style guide)
- **Icons**: Unicode emoji (🐱 🎃 ⚠ 💹 📊)

### Development Tools
- No build system required - works directly in browser
- Testing: Firefox/Chrome (WebGL required)

## Data Sources

**Note on Database Creation**: If you wish to create a fresh dataset from scratch, you'll want to clear existing output files first. The fetch scripts append to existing files to avoid re-fetching, so delete them before running if you want a clean start:

```bash
rm /path/to/all_abstracts_v2.txt  # Clear abstracts database
./fetch_abstracts_v2.sh           # Create new database from scratch
```

### Training Compute
- OpenAI models (GPT-1 through GPT-5)
- Sources: Epoch AI, arXiv papers, Metaculus predictions
- Documentation: `/STUDIES/RESEARCH/compute_estimates/OpenAI_Training_Compute_Estimates.md`

### P(doom) Estimates
- Expert surveys and individual estimates
- Sources: AI Impacts surveys, PauseAI.info, direct quotes
- Documentation: `/STUDIES/RESEARCH/pdoom_analysis/`
  - `00_OVERVIEW.md` - Project summary
  - `01_CORE_PRINCIPLES.md` - Definitions and frameworks
  - `04_NOTABLE_ESTIMATES.md` - Individual researcher predictions
  - `QUICK_REFERENCE.md` - One-page summary

### Real-time Data
- AI company stock prices (placeholder values - would need API for live data)
- Model release dates (historical, from public announcements)

## How to Use

### Running the Dashboard

1. **Open directly in browser:**
   ```bash
   firefox /path/to/STAGE2_DASHBOARD.html
   ```

2. **Or via local server (recommended for development):**
   ```bash
   python3 -m http.server 8000
   # Navigate to http://localhost:8000/STAGE2_DASHBOARD.html
   ```

### Interacting with the Dashboard

- **Year Slider**: Explore P(doom) trajectory over time (2020-2032)
- **Safety Investment**: Adjust AI safety research funding (0.1x to 5x)
- **International Coordination**: Set cooperation level (0 to 1)
- **Regulatory Strength**: Adjust governance effectiveness (0 to 1)
- **Panels**: Click and drag to move panels around
- **Links**: Click on metrics, stocks, or experts to open source information

### Viewing Shaders

Navigate to `/shaders/` and open any HTML file:
```bash
firefox /path/to/shaders/intelligence_explosion.html
```

Each shader is self-contained and demonstrates a specific AI risk concept.

## Project Structure

```
STUDIES/GRAPHICS/
├── README.md (this file)
├── PDOOM1_STYLE_GUIDE.md
├── Early_opinions.txt
├── 1ST_PROTOTYPES/
│   └── [5 early experimental files]
├── 2ND_PROTOTYPES/ (empty - consolidated into variations)
└── variations/
    ├── STAGE2_DASHBOARD.html ⭐ (main production file)
    ├── IN_DEVELOPMENT/
    │   └── [14 development iterations]
    └── shaders/
        └── [15 visual concept demonstrations]
```

## Future Enhancements

### Planned Features
- [ ] Live stock data API integration
- [ ] More AI models (Anthropic Claude, Google Gemini, Meta Llama)
- [ ] Historical P(doom) survey data over time
- [ ] Citation network visualization
- [ ] Mobile-responsive layout
- [ ] Export/share functionality (PNG, PDF, permalink)
- [ ] Accessibility improvements (keyboard navigation, screen reader support)

### Technical Improvements
- [ ] Modularize code (separate JS files)
- [ ] Add TypeScript for type safety
- [ ] Implement proper state management
- [ ] Optimize WebGL shader performance
- [ ] Add automated testing
- [ ] Create build system for production optimization

### Content Enhancements
- [ ] More expert estimates from recent surveys
- [ ] Timeline of key AI safety events
- [ ] Scenario analysis (slow vs fast takeoff)
- [ ] Risk factor breakdown (misalignment, deception, coordination failure)
- [ ] Interactive tutorial/walkthrough

## Contributing

### Adding New Data
1. **P(doom) estimates**: Edit `/STUDIES/RESEARCH/pdoom_analysis/04_NOTABLE_ESTIMATES.md`
2. **Compute data**: Edit `/STUDIES/RESEARCH/compute_estimates/OpenAI_Training_Compute_Estimates.md`
3. **Update dashboard**: Modify data arrays in STAGE2_DASHBOARD.html

### Creating New Shaders
Template:
```html
<!DOCTYPE html>
<html>
<head>
  <title>My Shader</title>
  <style>/* pdoom1 colors */</style>
</head>
<body>
  <canvas id="canvas"></canvas>
  <script>
    // WebGL setup
    // Fragment shader (GLSL)
    // Render loop
  </script>
</body>
</html>
```

Place in `/variations/shaders/` with descriptive name.

## License

[User to specify - e.g., MIT, GPL, CC-BY]

## Contact

[User to specify]

## Acknowledgments

- **pdoom1.com** - Design inspiration and visual language
- **Epoch AI** - Training compute estimates
- **AI Impacts** - Survey data
- **PauseAI** - P(doom) compilation and advocacy
- **Semantic Scholar, OpenAlex, Crossref** - Citation data APIs
- **OpenAI, Anthropic, Google, Meta** - Model development and transparency

---

**Last Updated**: October 29, 2025
**Status**: Active Development
**Version**: 2.0 (STAGE2_DASHBOARD)
