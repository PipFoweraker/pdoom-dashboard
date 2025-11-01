# Website Navigation Research Notes

**Date**: 2025-11-01  
**Purpose**: Understand pdoom1-website navigation to implement in dashboard

---

## Website Navigation Structure

### Main Navigation Bar (Header)

**Location**: Top of page, sticky positioned  
**Container**: `<nav>` inside `<header>`

**Structure:**
```html
<header>
  <nav role="navigation">
    <div class="logo-container">
      <a href="#" class="logo">p(Doom)1</a>
    </div>
    <ul class="nav-links" role="menubar">
      <!-- Navigation items here -->
    </ul>
  </nav>
</header>
```

**Navigation Items (from line 731-754):**

1. **Game** - `href="#home"`
2. **Leaderboard** - `href="/leaderboard/"`
3. **Stats** - `href="/game-stats/"`
4. **Risk Dashboard** - `href="/dashboard/"`
5. **Community ▾** (dropdown)
   - Known Issues - `href="#known-issues"`
   - Dev Blog - `href="/blog/"`
   - Updates - `href="/game-changelog/"`
   - GitHub - `href="https://github.com/PipFoweraker/pdoom1"`
6. **Info ▾** (dropdown)
   - About - `href="/about/"`
   - AI Safety Resources - `href="/resources/"`
   - Roadmap - `href="/roadmap/"`
   - Documentation - `href="/docs/"`

### CSS Styling (from lines 70-169)

**Navigation bar:**
```css
nav {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;
}
```

**Links:**
```css
.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-links a {
  color: var(--text-secondary);
  text-decoration: none;
  transition: color var(--duration-fast);
  font-size: 0.95rem;
  letter-spacing: 0.5px;
}

.nav-links a:hover {
  color: var(--accent-primary);
  text-shadow: 0 0 5px var(--accent-primary);
}
```

**Dropdowns:**
```css
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background: var(--bg-tertiary);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  min-width: 200px;
  padding: 0.5rem 0;
  display: none;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.dropdown:hover .dropdown-menu {
  display: block;
}
```

---

## Key URLs to Link

**Primary:**
- `/` - Home (game page)
- `/leaderboard/` - Leaderboard
- `/game-stats/` - Stats
- `/dashboard/` - Risk Dashboard (where our dashboard will be)

**Data Sources:**
- `https://github.com/PipFoweraker/pdoom1` - Game repository
- `https://github.com/PipFoweraker/pdoom-data` - Data repository (inferred)

**Community:**
- `/blog/` - Dev Blog
- `/game-changelog/` - Updates
- `https://github.com/PipFoweraker/pdoom1` - GitHub

**Info:**
- `/about/` - About page
- `/resources/` - AI Safety Resources
- `/docs/` - Documentation
- `/roadmap/` - Roadmap

---

## Design Tokens Used

**Colors:**
```css
--bg-primary: #1a1a1a
--bg-secondary: #2d2d2d
--text-primary: #ffffff
--text-secondary: #cccccc
--accent-primary: #00ff41  /* Matrix green */
--border-color: #444444
```

**Spacing/Sizing:**
```css
--radius-sm: 4px
--border-width: 1px
gap: 2rem (between nav items)
padding: 0.8rem 0 (nav bar)
font-size: 0.95rem (nav links)
```

**Transitions:**
```css
--duration-fast: 150ms
transition: color var(--duration-fast)
```

---

## Dashboard Current State

**Title location**: Inside `#header` div  
**Current content**: Just title, timestamp, status

**HTML:**
```html
<div id="header">
  <h1>P(DOOM) DASHBOARD – AI Existential Risk Monitor</h1>
  <div id="timestamp">...</div>
  <div id="status">...</div>
</div>
```

**CSS:**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  display:flex;
  justify-content:space-between;
  align-items:center;
}
```

---

## Implementation Plan

### Option 1: Subtitle Below Title (Simplest)

Add a subtitle row with links right under the title.

**Placement**: Between title and main content  
**Style**: Horizontal list of links, center-aligned

### Option 2: Integrated Header (Like Website)

Transform header into website-style nav with logo + links.

**Placement**: Replace current header structure  
**Style**: Flex layout with logo left, links right

### Option 3: Subtitle Row (Separate Section)

Add a new row below header specifically for navigation.

**Placement**: New section between header and main grid  
**Style**: Full-width bar with centered links

---

## Links to Include

**Core 3:**
1. **pdoom1** - Link to game page
2. **Data Repo** - Link to pdoom-data GitHub
3. **Game Repo** - Link to pdoom1 GitHub

**Possible additions:**
- Leaderboard
- Game Stats
- About
- Resources

---

## Design Considerations

**Color scheme:**
- Keep dashboard's matrix green (#00ff41)
- Use same hover effects as website
- Match text colors (--text-secondary: #cccccc)

**Spacing:**
- Consistent with website (gap: 2rem)
- Don't crowd the title

**Responsiveness:**
- Links should stack on mobile
- Keep readable at all sizes

**Accessibility:**
- Proper link text
- Keyboard navigation
- Focus states

---

## Next Steps

1. Create 3 variations showing different placements
2. Each with code snippets explaining approach
3. Show before/after for each method
4. Include working HTML files to compare

