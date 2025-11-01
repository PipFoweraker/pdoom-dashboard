# Subtitle Navigation Links - Implementation Guide

**Variation**: 03-subtitle-navigation  
**Date**: 2025-11-01  
**Feature**: Add navigation links to pdoom1 game, data repo, and game repo

---

## Research Summary

The pdoom1-website uses a horizontal navigation bar with:
- **Color**: `--text-secondary: #cccccc` (default), `--accent-primary: #00ff41` (hover)
- **Spacing**: `gap: 2rem` between links
- **Font**: `0.95rem` size, `letter-spacing: 0.5px`
- **Hover effect**: Color change + text-shadow glow
- **Transition**: `150ms` smooth

See `RESEARCH_NOTES.md` for full analysis.

---

## Approach 1: Subtitle Row Below Title (RECOMMENDED)

###Description
Add a centered row of links directly under the title, inside the header.

### Visual Layout
```
┌─────────────────────────────────────────┐
│  P(DOOM) DASHBOARD – AI Risk Monitor    │  <-- Title
│    pdoom1 | Data Repo | Game Repo       │  <-- NEW: Links
│                         Timestamp/Status │
└─────────────────────────────────────────┘
```

### HTML Changes

**Find this section (around line 590):**
```html
<div id="header">
  <h1>P(DOOM) DASHBOARD – AI Existential Risk Monitor</h1>
  <div id="timestamp">...</div>
  <div id="status">...</div>
</div>
```

**Replace with:**
```html
<div id="header">
  <div class="header-content">
    <h1>P(DOOM) DASHBOARD – AI Existential Risk Monitor</h1>
    <nav class="subtitle-nav">
      <a href="https://pdoom1.com/" target="_blank">pdoom1</a>
      <span class="nav-separator">|</span>
      <a href="https://github.com/PipFoweraker/pdoom-data" target="_blank">Data Repo</a>
      <span class="nav-separator">|</span>
      <a href="https://github.com/PipFoweraker/pdoom1" target="_blank">Game Repo</a>
    </nav>
  </div>
  <div class="header-info">
    <div id="timestamp">...</div>
    <div id="status">...</div>
  </div>
</div>
```

### CSS Changes

**Find the `#header` block (around line 19):**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  display:flex;
  justify-content:space-between;
  align-items:center;
  box-shadow:0 0 30px rgba(0,255,65,0.6);
  backdrop-filter:blur(5px);
}
```

**Replace with:**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  display:flex;
  justify-content:space-between;
  align-items:flex-start;  /* <-- CHANGED: top-align for multiline */
  box-shadow:0 0 30px rgba(0,255,65,0.6);
  backdrop-filter:blur(5px);
}

.header-content {
  display:flex;
  flex-direction:column;
  align-items:center;
  gap:8px;  /* Space between title and links */
}

#header h1 {
  font-size:28px;
  color:#ffffff;
  text-shadow:0 0 5px #000, 0 0 10px #000, 0 0 20px #00ff41;
  letter-spacing:4px;
  font-weight:bold;
  margin-bottom:0;  /* Remove default margin */
}

.subtitle-nav {
  display:flex;
  align-items:center;
  gap:15px;
  font-size:14px;
}

.subtitle-nav a {
  color:#cccccc;
  text-decoration:none;
  transition:all 150ms ease;
  letter-spacing:0.5px;
  font-weight:500;
}

.subtitle-nav a:hover {
  color:#00ff41;
  text-shadow:0 0 8px #00ff41;
}

.nav-separator {
  color:#444444;
  font-weight:300;
}

.header-info {
  display:flex;
  flex-direction:column;
  align-items:flex-end;
  gap:4px;
}
```

### How It Works

1. **Wrapper div** (`.header-content`) groups title + links together
2. **Flex column** layout stacks title above links
3. **Center alignment** centers both title and links
4. **Gap property** controls spacing between title and links
5. **Separator spans** add visual dividers between links
6. **Hover states** match website style (green glow)

---

## Approach 2: Inline Links Next to Title

### Description
Put links on the same line as the title, to the right of it.

### Visual Layout
```
┌─────────────────────────────────────────┐
│  P(DOOM) DASHBOARD  pdoom1 | Data | Repo│
│                         Timestamp/Status │
└─────────────────────────────────────────┘
```

### HTML Changes

```html
<div id="header">
  <div class="title-row">
    <h1>P(DOOM) DASHBOARD</h1>
    <nav class="inline-nav">
      <a href="https://pdoom1.com/" target="_blank">pdoom1</a>
      <span>|</span>
      <a href="https://github.com/PipFoweraker/pdoom-data" target="_blank">Data</a>
      <span>|</span>
      <a href="https://github.com/PipFoweraker/pdoom1" target="_blank">Repo</a>
    </nav>
  </div>
  <div class="header-info">
    <div id="timestamp">...</div>
    <div id="status">...</div>
  </div>
</div>
```

### CSS Changes

```css
.title-row {
  display:flex;
  align-items:baseline;  /* Align title and links on baseline */
  gap:20px;
}

#header h1 {
  font-size:24px;  /* Smaller to fit on one line */
  color:#ffffff;
  text-shadow:0 0 5px #000, 0 0 10px #000, 0 0 20px #00ff41;
  letter-spacing:4px;
  font-weight:bold;
  margin:0;
}

.inline-nav {
  display:flex;
  align-items:center;
  gap:12px;
  font-size:13px;
}

.inline-nav a {
  color:#cccccc;
  text-decoration:none;
  transition:all 150ms ease;
}

.inline-nav a:hover {
  color:#00ff41;
  text-shadow:0 0 8px #00ff41;
}

.inline-nav span {
  color:#444444;
}
```

### How It Works

1. **Flex row** layout puts title and links side-by-side
2. **Baseline alignment** lines up text properly
3. **Smaller title** makes room for links
4. **Compact spacing** fits everything on one line

### Pros/Cons

**Pros:**
- ✅ Compact, saves vertical space
- ✅ Links easily discoverable

**Cons:**
- ❌ Crowded on smaller screens
- ❌ Title must be shortened
- ❌ Less emphasis on links

---

## Approach 3: Separate Navigation Bar

### Description
Add a completely separate navigation bar below the header.

### Visual Layout
```
┌─────────────────────────────────────────┐
│  P(DOOM) DASHBOARD         Timestamp    │  <-- Header
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│    pdoom1  |  Data Repo  |  Game Repo   │  <-- NEW: Nav Bar
└─────────────────────────────────────────┘
```

### HTML Changes

**After the `#header` div, add:**
```html
<div id="header">
  <!-- Existing header content unchanged -->
</div>

<!-- NEW: Separate nav bar -->
<nav id="dashboardNav">
  <ul class="nav-links">
    <li><a href="https://pdoom1.com/" target="_blank">pdoom1 Home</a></li>
    <li><a href="https://github.com/PipFoweraker/pdoom-data" target="_blank">Data Repository</a></li>
    <li><a href="https://github.com/PipFoweraker/pdoom1" target="_blank">Game Repository</a></li>
    <li><a href="/leaderboard/" target="_blank">Leaderboard</a></li>
  </ul>
</nav>

<div id="container">
  <!-- Rest of dashboard -->
</div>
```

### CSS Changes

**Add new styles:**
```css
#dashboardNav {
  background:rgba(0,20,10,0.7);
  border-bottom:2px solid #00ff41;
  padding:10px 0;
  backdrop-filter:blur(5px);
  position:relative;
  z-index:15;
}

.nav-links {
  display:flex;
  justify-content:center;
  align-items:center;
  gap:30px;
  list-style:none;
  margin:0;
  padding:0;
}

.nav-links li {
  margin:0;
}

.nav-links a {
  color:#cccccc;
  text-decoration:none;
  font-size:14px;
  letter-spacing:0.5px;
  padding:6px 12px;
  border-radius:4px;
  transition:all 150ms ease;
  font-weight:500;
}

.nav-links a:hover {
  color:#00ff41;
  background:rgba(0,255,65,0.1);
  text-shadow:0 0 8px #00ff41;
}
```

**Adjust main content:**
```css
#container {
  height:calc(100vh - 120px);  /* Subtract header + nav height */
}
```

### How It Works

1. **Separate section** is independent of header
2. **Full-width bar** spans entire viewport
3. **Centered list** of navigation links
4. **More space** allows additional links (leaderboard, etc.)
5. **Container height** adjusted to account for nav bar

### Pros/Cons

**Pros:**
- ✅ Clean separation of concerns
- ✅ Room for more links
- ✅ Doesn't modify header
- ✅ Matches website pattern

**Cons:**
- ❌ Uses more vertical space
- ❌ Requires container height adjustment
- ❌ More complex to implement

---

## Comparison Table

| Approach | Vertical Space | Complexity | Website Match | Best For |
|----------|----------------|------------|---------------|----------|
| **1. Subtitle** | Low (8px gap) | Low | Medium | Most cases ✅ |
| **2. Inline** | Lowest | Medium | Low | Compact layouts |
| **3. Separate Bar** | High (35px) | High | High | Full navigation |

---

## Recommended: Approach 1 (Subtitle)

**Why:**
- ✅ Cleanest visual hierarchy
- ✅ Centered like title
- ✅ Easy to implement
- ✅ Minimal space usage
- ✅ Doesn't crowd title

---

## Link Styling Details

### Default State
```css
color: #cccccc;           /* Light gray */
text-decoration: none;    /* No underline */
letter-spacing: 0.5px;    /* Slight spacing */
font-weight: 500;         /* Medium weight */
```

### Hover State
```css
color: #00ff41;                    /* Matrix green */
text-shadow: 0 0 8px #00ff41;     /* Green glow */
transition: all 150ms ease;        /* Smooth change */
```

### Separator
```css
color: #444444;           /* Dark gray */
font-weight: 300;         /* Light weight */
```

---

## Implementation Files

This directory contains:
1. `method1-subtitle.html` - Subtitle row (RECOMMENDED)
2. `method2-inline.html` - Inline with title
3. `method3-separate.html` - Separate nav bar

---

## Testing Checklist

For each method:
- ✅ Links clickable and open correct URLs
- ✅ Hover effects work (color + glow)
- ✅ Separators visible
- ✅ Title still prominent
- ✅ Timestamp/status still visible
- ✅ Graph still renders
- ✅ Responsive on window resize

---

## Quick Implementation (Method 1)

1. **Wrap title in container:**
   ```html
   <div class="header-content">
     <h1>...</h1>
     <nav class="subtitle-nav"><!-- links here --></nav>
   </div>
   ```

2. **Add CSS for layout:**
   ```css
   .header-content { display:flex; flex-direction:column; align-items:center; gap:8px; }
   .subtitle-nav { display:flex; gap:15px; font-size:14px; }
   .subtitle-nav a { color:#ccc; transition:all 150ms; }
   .subtitle-nav a:hover { color:#00ff41; text-shadow:0 0 8px #00ff41; }
   ```

3. **Add links:**
   ```html
   <a href="https://pdoom1.com/">pdoom1</a>
   <span>|</span>
   <a href="https://github.com/PipFoweraker/pdoom-data">Data Repo</a>
   <span>|</span>
   <a href="https://github.com/PipFoweraker/pdoom1">Game Repo</a>
   ```

Done! Navigation links added.

---

**All approaches maintain full dashboard functionality while adding navigation!**
