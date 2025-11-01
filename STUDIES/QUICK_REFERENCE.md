# STUDIES Directory Quick Reference

## Current Production File

**Path**: `02-prototypes/integrated/STAGE2_DASHBOARD.html`  
**Size**: 30KB  
**Date**: Oct 30, 2025  
**Status**: Baseline for new work

Open in Firefox:
```bash
firefox STUDIES/02-prototypes/integrated/STAGE2_DASHBOARD.html
```

## Directory Layout

```
00-research/      Research data and analysis
01-design/        Design system and specs
02-prototypes/    Dashboard development
  early/          First 5 HTML prototypes
  integrated/     Full dashboard (STAGE2 here)
03-shaders/       WebGL shader experiments (empty)
```

## Key Files

- **Production baseline**: `02-prototypes/integrated/STAGE2_DASHBOARD.html`
- **Style guide**: `01-design/style-guide.md`
- **Compute data**: `00-research/compute-estimates/OpenAI_Training_Compute_Estimates.md`
- **P(doom) data**: `00-research/pdoom-analysis/04_NOTABLE_ESTIMATES.md`

## Workflow

Create new variation:
```bash
cd STUDIES/02-prototypes/integrated
cp STAGE2_DASHBOARD.html my-variation.html
vim my-variation.html
firefox my-variation.html
```

## File Counts

- HTML prototypes: 6 (5 early + 1 production)
- Markdown docs: 16
- All Oct 30 good files preserved
- All Nov 1 bad files removed
