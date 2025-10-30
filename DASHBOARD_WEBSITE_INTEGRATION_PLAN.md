# P(doom) Dashboard → pdoom1.com Website Integration Plan

**Date**: October 30, 2025
**Status**: Planning Phase
**Objective**: Integrate the interactive P(doom) dashboard prototype into the live pdoom1.com website

---

## Executive Summary

We have successfully created an interactive P(doom) dashboard (`STAGE2_DASHBOARD.html`) that visualizes AI existential risk through real-time graphs, expert estimates, and dynamic shaders. This document outlines the step-by-step process to integrate this dashboard into the pdoom1.com website.

---

## Current State Analysis

### ✅ Dashboard Repository (pdoom-dashboard)
**Location**: `/home/laptop/Documents/Projects/ai-sandbox/pdoom-dashboard/`

**Status**: Complete and committed to git
- **Production file**: `STUDIES/GRAPHICS/variations/STAGE2_DASHBOARD.html` (30KB)
- **Development iterations**: 14 prototypes in `IN_DEVELOPMENT/`
- **Shaders**: 15 WebGL shader experiments in `shaders/`
- **Documentation**: README.md, PDOOM1_STYLE_GUIDE.md, research docs
- **Commit hash**: `2e97882d` ("Track 2ND_PROTOTYPES directory")

**Key Features**:
- Dual-axis P(doom) + compute graph (Plotly.js)
- Interactive adjustment sliders (Safety, Coordination, Regulation)
- Warning lights for milestone dates
- AI company stock tickers with links
- Expert estimates with Wikipedia links
- Country compute pie chart
- Dynamic WebGL shader (green→orange→red transition)
- Draggable panels
- Cat cam with pdoom1 assets

### ✅ Website Repository (pdoom1-website)
**Location**: `/home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/`

**Status**: Operational, currently using Git (needs jj conversion)
- **Hosting**: Netlify (https://pdoom1.com)
- **Framework**: Static HTML + npm scripts + API
- **Version**: v1.0.0 - Production Ready
- **Deployment**: Weekly on Fridays at 16:00 AEST

**Structure**:
```
pdoom1-website/
├── public/               # Static assets (where dashboard goes)
│   ├── index.html       # Main page with navigation
│   ├── about/           # About page
│   ├── blog/            # Dev blog
│   ├── leaderboard/     # Game leaderboard
│   ├── game-stats/      # Statistics page
│   ├── resources/       # AI Safety resources
│   └── assets/          # Images, CSS, JS
│       ├── css/
│       ├── js/
│       └── images/
├── scripts/             # Management scripts
├── docs/                # Documentation
├── api/                 # API endpoints
└── netlify/            # Serverless functions
```

**Navigation Structure**:
- **Top-level**: Game | Leaderboard | Stats
- **Community ▾**: Known Issues | Dev Blog | Updates | GitHub
- **Info ▾**: About | AI Safety Resources | Roadmap | Documentation

**Design System** (already matches our dashboard!):
```css
--bg-primary: #1a1a1a
--accent-primary: #00ff41   /* Matrix green */
--accent-secondary: #ff6b35 /* Warning orange */
--accent-danger: #ff4444    /* Error red */
font-family: 'Courier New', monospace
```

---

## Integration Strategy

### Option 1: Top-Level Navigation Link (RECOMMENDED)
**Pros**:
- High visibility and easy discovery
- Positions dashboard as major feature
- Clear separation from game stats
- Good for educational/research content

**Cons**:
- Adds another top-level item (may clutter nav)

**Implementation**:
Add between "Stats" and "Community" dropdown:
```html
<li role="none"><a href="/dashboard/" role="menuitem">Risk Dashboard</a></li>
```

### Option 2: Under "Stats" Dropdown
**Pros**:
- Logical grouping with game statistics
- Doesn't add top-level clutter
- Natural progression: game stats → risk metrics

**Cons**:
- Less visibility
- May be confused with game-specific stats

### Option 3: Under "AI Safety Resources" (Info dropdown)
**Pros**:
- Perfect thematic fit with educational content
- Groups with resources page
- Expected location for serious content

**Cons**:
- Buried two levels deep
- Less discoverable for casual users

---

## Recommended Approach: Hybrid Strategy

**Primary**: Top-level "Dashboard" link
**Secondary**: Also link from "AI Safety Resources" page with context

This ensures:
- Easy discovery for all users (top-level)
- Thematic connection for interested users (resources page)
- Clear purpose differentiation from game stats

---

## Implementation Steps

### Phase 1: Setup (15 minutes)

#### 1.1 Initialize jj for Website Repo
```bash
cd /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website
jj git init --colocate  # Convert git repo to jj
jj status              # Verify setup
```

#### 1.2 Create Dashboard Directory
```bash
mkdir -p public/dashboard
mkdir -p public/dashboard/assets
mkdir -p public/dashboard/shaders
```

#### 1.3 Verify Cat Asset Exists
```bash
ls -la /home/laptop/Documents/Projects/ai-sandbox/pdoom1/assets/images/ | grep cat
```

Expected files:
- `pdoom1 office cat default png.png`
- `small doom caat.png`

### Phase 2: File Transfer & Adaptation (30 minutes)

#### 2.1 Copy Main Dashboard
```bash
cp /home/laptop/Documents/Projects/ai-sandbox/pdoom-dashboard/STUDIES/GRAPHICS/variations/STAGE2_DASHBOARD.html \
   /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/public/dashboard/index.html
```

#### 2.2 Copy Shader Experiments (Optional - for future expansion)
```bash
cp -r /home/laptop/Documents/Projects/ai-sandbox/pdoom-dashboard/STUDIES/GRAPHICS/variations/shaders/*.html \
      /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/public/dashboard/shaders/
```

#### 2.3 Update Asset Paths in Dashboard
The dashboard currently references:
```html
<img id="catImage" src="/home/laptop/Documents/Projects/ai-sandbox/pdoom1/assets/images/pdoom1 office cat default png.png" alt="Cat">
```

**Change to**:
```html
<img id="catImage" src="/assets/images/pdoom1-office-cat-default.png" alt="Cat">
```

**Action**: Search and replace all hardcoded file paths in `public/dashboard/index.html`

#### 2.4 Copy Cat Images to Website Assets
```bash
cp "/home/laptop/Documents/Projects/ai-sandbox/pdoom1/assets/images/pdoom1 office cat default png.png" \
   /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/public/assets/images/pdoom1-office-cat-default.png

cp "/home/laptop/Documents/Projects/ai-sandbox/pdoom1/assets/images/small doom caat.png" \
   /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/public/assets/images/small-doom-cat.png
```

### Phase 3: Navigation Integration (20 minutes)

#### 3.1 Add Top-Level Nav Link
Edit `/home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/public/index.html` at line ~732:

**Before**:
```html
<li role="none"><a href="/game-stats/" role="menuitem">Stats</a></li>
<li role="none" class="dropdown">
    <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle">Community ▾</a>
```

**After**:
```html
<li role="none"><a href="/game-stats/" role="menuitem">Stats</a></li>
<li role="none"><a href="/dashboard/" role="menuitem">Risk Dashboard</a></li>
<li role="none" class="dropdown">
    <a href="#" role="menuitem" aria-haspopup="true" aria-expanded="false" class="dropdown-toggle">Community ▾</a>
```

#### 3.2 Add Link to Resources Page
Edit `/home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/public/resources/index.html`:

Add section:
```html
<section>
    <h2>📊 Interactive Risk Dashboard</h2>
    <p>
        Explore our <a href="/dashboard/">P(doom) Risk Dashboard</a> - an interactive visualization
        of AI existential risk based on expert estimates, training compute growth, and adjustable
        safety parameters.
    </p>
    <a href="/dashboard/" class="btn-primary">Launch Dashboard →</a>
</section>
```

### Phase 4: Metadata & SEO (10 minutes)

#### 4.1 Update Dashboard Head Section
Add to `public/dashboard/index.html` `<head>`:

```html
<meta name="description" content="Interactive P(doom) dashboard visualizing AI existential risk through expert estimates, training compute growth, and safety parameters." />
<meta property="og:title" content="P(doom) Risk Dashboard - AI Safety Visualization" />
<meta property="og:description" content="Explore AI existential risk through interactive graphs, expert estimates, and real-time data." />
<meta property="og:url" content="https://pdoom1.com/dashboard/" />
<link rel="canonical" href="https://pdoom1.com/dashboard/" />
```

#### 4.2 Update Sitemap
Add to `/public/sitemap.xml`:
```xml
<url>
    <loc>https://pdoom1.com/dashboard/</loc>
    <lastmod>2025-10-30</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
</url>
```

### Phase 5: Testing (20 minutes)

#### 5.1 Local Testing
```bash
cd /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website
npm start  # Start dev server
```

**Test checklist**:
- [ ] Dashboard loads at http://localhost:PORT/dashboard/
- [ ] Cat images display correctly
- [ ] All links work (experts, stocks, sources)
- [ ] Sliders adjust the graph
- [ ] Panels are draggable
- [ ] Shader transitions properly
- [ ] Navigation link works from main page
- [ ] Mobile responsiveness (resize browser)

#### 5.2 Check Browser Console
- [ ] No 404 errors for missing assets
- [ ] No JavaScript errors
- [ ] Plotly.js loads from CDN successfully

### Phase 6: Documentation (15 minutes)

#### 6.1 Create Dashboard README
Create `public/dashboard/README.md`:

```markdown
# P(doom) Risk Dashboard

Interactive visualization of AI existential risk.

## Features
- Real-time P(doom) trajectory (2020-2032)
- Training compute growth (GPT-1 through GPT-5)
- Expert estimates with sources
- Adjustable safety parameters
- Country compute distribution
- AI company stock tracker

## Data Sources
- Expert estimates: AI Impacts, PauseAI, individual researchers
- Training compute: Epoch AI, arXiv papers, Metaculus
- Citations: See individual source links in dashboard

## Local Development
This dashboard is a standalone HTML file with no build dependencies.
Assets required: Cat images in `/assets/images/`

## Updates
Dashboard is maintained in the pdoom-dashboard repository:
https://github.com/PipFoweraker/pdoom-dashboard
```

#### 6.2 Update Main Website README
Add to `/home/laptop/Documents/Projects/ai-sandbox/pdoom1-website/README.md`:

```markdown
### P(doom) Risk Dashboard (NEW)
- **Path**: `/public/dashboard/`
- **Purpose**: Interactive AI existential risk visualization
- **Features**: Expert estimates, compute tracking, adjustable parameters
- **Data Sources**: Epoch AI, AI Impacts, PauseAI, academic papers
- **Technology**: Plotly.js, WebGL shaders, pure HTML/CSS/JS
```

#### 6.3 Update Changelog
Add entry to `/public/blog/`:

```markdown
# 2025-10-30 - P(doom) Risk Dashboard Launch

Added comprehensive AI existential risk dashboard to pdoom1.com/dashboard/

**Features**:
- Interactive P(doom) trajectory graph (2020-2032)
- Real-time training compute visualization
- Expert estimates from leading AI researchers
- Adjustable safety investment, coordination, and regulation parameters
- Country compute distribution analysis
- AI company stock tracker
- Dynamic shader background reflecting risk levels

**Purpose**: Educate visitors about AI safety risks through data visualization and
allow exploration of how different interventions could affect risk trajectories.

**Data Sources**: Epoch AI, AI Impacts, PauseAI, Semantic Scholar, OpenAlex
```

### Phase 7: Commit & Deploy (10 minutes)

#### 7.1 Create Commit with jj
```bash
cd /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website
jj status  # Review changes

jj describe -m "Add P(doom) Risk Dashboard

Integrate interactive AI existential risk dashboard from pdoom-dashboard repository.

Features:
- Interactive P(doom) + training compute dual-axis graph
- Expert estimates with source links (Yudkowsky, Hinton, Bengio, Amodei, surveys)
- Adjustable parameters: safety investment, coordination, regulation
- Warning lights for milestone dates (GPT-4/5 releases, risk thresholds)
- Country compute distribution pie chart
- AI company stock tracker (NVIDIA, Microsoft, Alphabet, Meta)
- Dynamic WebGL shader transitioning green→orange→red with risk level
- Draggable panels for customization
- Cat cam integration with pdoom1 assets

Navigation:
- Added top-level 'Risk Dashboard' link
- Added contextual link from AI Safety Resources page

Assets:
- Copied cat images from pdoom1 repo to /assets/images/
- Updated all asset paths for web deployment

Documentation:
- Created /public/dashboard/README.md
- Updated main README.md with dashboard section
- Added changelog entry for launch

Data Sources:
- Expert estimates: AI Impacts, PauseAI, individual researchers
- Training compute: Epoch AI (5.6mo doubling), arXiv papers, Metaculus
- Citations: Semantic Scholar, OpenAlex, Crossref
- Stocks: Yahoo Finance (placeholder - consider live API)

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"
```

#### 7.2 Review Changes
```bash
jj diff --summary  # Check what changed
jj log --limit 5   # Verify commit message
```

#### 7.3 Push to Remote (if ready for deployment)
```bash
jj bookmark set main -r @
jj git push --bookmark main
```

**Note**: This will trigger Netlify deployment automatically!

---

## Asset Requirements

### Required Files
1. **Cat Images** (source: pdoom1 repo)
   - `pdoom1 office cat default png.png` → `pdoom1-office-cat-default.png`
   - `small doom caat.png` → `small-doom-cat.png`

2. **Dashboard HTML**
   - `STAGE2_DASHBOARD.html` → `public/dashboard/index.html`

3. **External Dependencies** (already in dashboard via CDN)
   - Plotly.js v2.32.0 (https://cdn.plot.ly/plotly-2.32.0.min.js)

### Path Updates Required

| Current Path | New Path |
|-------------|----------|
| `/home/laptop/.../pdoom1/assets/images/pdoom1 office cat default png.png` | `/assets/images/pdoom1-office-cat-default.png` |
| `/home/laptop/.../pdoom1/assets/images/small doom caat.png` | `/assets/images/small-doom-cat.png` |

---

## Deployment Considerations

### Timing
- **Recommended**: Deploy during weekly release window (Friday 16:00 AEST)
- **Reason**: Aligns with existing deployment schedule and Twitch stream
- **Alternative**: Can deploy immediately for emergency/important feature

### Netlify Configuration
The website uses Netlify for hosting. Push to main branch triggers automatic deployment.

**Deployment time**: ~2-3 minutes
**CDN propagation**: ~5-10 minutes globally

### Rollback Plan
If issues arise:
```bash
# Revert to previous commit
jj undo
jj git push --bookmark main --force  # Use with caution!
```

Or temporarily remove nav link and hide dashboard directory.

---

## SSH Access for Website

### Current Setup
The website is hosted on **Netlify**, which is a static site host (not traditional server hosting).

**Access methods**:
1. **Netlify Dashboard**: https://app.netlify.com/
2. **Netlify CLI**: `npm install -g netlify-cli && netlify login`
3. **Git/jj**: Push to GitHub → Netlify auto-deploys

**Important**: There is **no traditional SSH server access** because Netlify is a CDN/static host.

### Alternative: Local Development Server
For testing before deployment:
```bash
cd /home/laptop/Documents/Projects/ai-sandbox/pdoom1-website
npm start  # Runs local server (usually port 8000 or 3000)
```

### If You Need Traditional Server Hosting
Consider:
- **DigitalOcean** ($6/mo droplet with SSH)
- **AWS EC2** (free tier available)
- **Linode** ($5/mo)
- **Hetzner** ($4/mo)

But Netlify is likely sufficient for static sites!

---

## Post-Deployment Tasks

### Immediate (Day 1)
- [ ] Test dashboard on live site
- [ ] Check analytics (if Plausible enabled)
- [ ] Monitor for 404s or console errors
- [ ] Announce on Dev Blog
- [ ] Share on GitHub

### Week 1
- [ ] Gather user feedback
- [ ] Monitor performance (load times)
- [ ] Check mobile usability
- [ ] Consider adding to game's "?" help menu

### Future Enhancements
- [ ] Add more AI models (Anthropic Claude, Google Gemini, Meta Llama)
- [ ] Live stock API integration
- [ ] Historical P(doom) survey data timeline
- [ ] Export/share functionality (PNG, permalink)
- [ ] Mobile-responsive improvements
- [ ] Link from game to dashboard for educational context

---

## Risk Assessment & Mitigation

### Technical Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Asset 404s (cat images) | Low | Medium | Test locally first, verify paths |
| Plotly CDN failure | Low | High | Consider self-hosting Plotly.js |
| Mobile rendering issues | Medium | Medium | Test on multiple devices/browsers |
| Large file size impacts load time | Low | Low | Dashboard is only 30KB + CDN assets |

### User Experience Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Confusing navigation placement | Low | Medium | Clear labeling "Risk Dashboard" |
| Data interpretation errors | Medium | High | Add explanatory text, link to research |
| Information overload | Medium | Medium | Keep UI clean, offer tutorial/guide |

### Content Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Outdated P(doom) estimates | Medium | Medium | Add "Last Updated" dates, update quarterly |
| Misleading statistics | Low | High | Link all data to sources, add disclaimers |
| Controversial framing | Low | Medium | Emphasize educational purpose, cite experts |

---

## Success Metrics

### Quantitative
- **Pageviews**: Track `/dashboard/` visits (via Plausible if enabled)
- **Time on page**: Aim for >2 minutes average (indicates engagement)
- **Bounce rate**: Target <40% (shows content is compelling)
- **Error rate**: Target <1% (404s, JS errors)

### Qualitative
- **User feedback**: Comments, emails, GitHub issues
- **Educational impact**: References in discussions, citations
- **Community adoption**: Shares on social media, forums

### Technical
- **Load time**: Target <3 seconds on 3G
- **Mobile usability**: 100% functional on mobile
- **Accessibility**: WCAG AA compliance
- **Browser support**: Chrome, Firefox, Safari, Edge

---

## Maintenance Plan

### Weekly
- Check for broken external links (expert/source URLs)
- Monitor analytics for usage patterns
- Review console errors (if reported)

### Monthly
- Update AI company stock values
- Review and update P(doom) estimates
- Check for new AI model releases (compute data)
- Update training compute projections

### Quarterly
- Major data refresh (expert estimates, survey results)
- Review and update research documentation
- Consider adding new visualization features
- Audit accessibility and mobile experience

---

## Related Documentation

### In pdoom-dashboard Repository
- `STUDIES/GRAPHICS/README.md` - Dashboard development history
- `STUDIES/GRAPHICS/PDOOM1_STYLE_GUIDE.md` - Visual design system
- `STUDIES/RESEARCH/pdoom_analysis/` - P(doom) research documentation
- `STUDIES/RESEARCH/compute_estimates/` - Training compute data

### In pdoom1-website Repository
- `README.md` - Website overview and quickstart
- `docs/03-integrations/` - Integration guides
- `docs/02-deployment/` - Deployment procedures
- `public/blog/` - Development changelog

---

## Questions & Answers

### Q: Why not build the dashboard as a React/Vue component?
**A**: The dashboard is intentionally a standalone HTML file for:
- **Simplicity**: No build process or dependencies
- **Portability**: Easy to share, embed, or fork
- **Performance**: Zero JS framework overhead
- **Compatibility**: Works anywhere HTML works

### Q: Should we version the dashboard separately?
**A**: Yes, maintain version in dashboard HTML:
```html
<!-- P(doom) Dashboard v2.0 - Last Updated: 2025-10-30 -->
```

Update version on significant changes (new features, major data updates).

### Q: How do we handle future dashboard updates?
**A**:
1. Develop in `pdoom-dashboard` repo
2. Test new version thoroughly
3. Copy updated `index.html` to `pdoom1-website/public/dashboard/`
4. Test integration locally
5. Deploy during weekly release window

### Q: Can users embed the dashboard elsewhere?
**A**: Yes! Provide iframe embed code:
```html
<iframe src="https://pdoom1.com/dashboard/"
        width="100%" height="800px"
        frameborder="0"></iframe>
```

Add to dashboard README.

---

## Timeline Summary

| Phase | Duration | Status |
|-------|----------|--------|
| Planning & Documentation | 2 hours | ✅ Complete |
| Setup (jj, directories) | 15 min | ⏳ Pending |
| File Transfer & Adaptation | 30 min | ⏳ Pending |
| Navigation Integration | 20 min | ⏳ Pending |
| Metadata & SEO | 10 min | ⏳ Pending |
| Testing | 20 min | ⏳ Pending |
| Documentation | 15 min | ⏳ Pending |
| Commit & Deploy | 10 min | ⏳ Pending |
| **Total** | **~4 hours** | **In Progress** |

---

## Next Steps

1. **Review this plan** - Discuss any concerns or modifications
2. **Initialize jj** - Convert pdoom1-website to jj repo (optional, can stay with git)
3. **Execute Phase 1** - Setup directories and verify assets
4. **Execute Phase 2** - Copy and adapt dashboard files
5. **Execute Phase 3** - Add navigation links
6. **Execute Phases 4-6** - Metadata, testing, documentation
7. **Execute Phase 7** - Commit and deploy (or stage for Friday release)

**Recommendation**: Execute Phases 1-6 today, deploy during Friday release window for maximum visibility (Twitch stream showcase).

---

**Document Version**: 1.0
**Last Updated**: 2025-10-30
**Author**: Claude Code
**Repository**: pdoom-dashboard → pdoom1-website integration
