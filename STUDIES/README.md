# STUDIES Directory

Research, design, and prototypes for the pdoom-dashboard project.

## Structure

### 00-research/
Data analysis and research documentation:
- `compute-estimates/` - AI training compute projections
- `pdoom-analysis/` - P(doom) estimate analysis

### 01-design/
Design system and specifications:
- `style-guide.md` - Visual design system matching pdoom1 game
- `color-schemes/` - Color palette variations
- `component-specs/` - Component design specifications

### 02-prototypes/
Dashboard development iterations:
- `early/` - First 5 prototypes (DG, DJ, DOOMPLOT, etc.)
- `component-variations/` - Individual UI component tests
  - title/, subtitle-links/, event-log/, calmer-ui/
  - game-ui-consistency/, investment-graph/, manifold-api/, world-map/
- `integrated/` - Full dashboard versions
  - `STAGE2_DASHBOARD.html` - **Current production version**
  - Various v2, v3, v4 iterations
- `compute-focused/` - OpenAI compute visualization experiments

### 03-shaders/
WebGL shader experiments:
- `ai-risk-themes/` - Risk-themed shaders (neural mesh, coordination failure, etc.)
- `pdoom1-branded/` - Game-branded shaders
- `fun/` - Cat and seasonal shaders

## Key Files

**Production Dashboard**: `02-prototypes/integrated/STAGE2_DASHBOARD.html`  
**Style Guide**: `01-design/style-guide.md`

## File Count

- HTML files: 59
- Markdown docs: 16
- Python scripts: 0 (all in root directory)

Last reorganized: 2025-11-01
