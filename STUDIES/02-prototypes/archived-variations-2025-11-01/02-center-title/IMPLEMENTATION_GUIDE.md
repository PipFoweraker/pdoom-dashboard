# Center Title - Implementation Guide

**Variation**: 02-center-title  
**Date**: 2025-11-01  
**Feature**: Center "P(DOOM) DASHBOARD" title at top of page

---

## Current State (Before)

The header uses `justify-content: space-between` which spreads items across:
- Left: Title (h1)
- Right: Timestamp and Status

```css
#header {
  display:flex;
  justify-content:space-between;  /* <-- This spreads items apart */
  align-items:center;
}
```

---

## Method 1: Center with Flexbox (Simplest)

### Description
Change flexbox layout to center the title, move timestamp/status to absolute positioning.

### Code Changes

**CSS - Change header layout:**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  display:flex;
  justify-content:center;  /* <-- CHANGED: center instead of space-between */
  align-items:center;
  box-shadow:0 0 30px rgba(0,255,65,0.6);
  backdrop-filter:blur(5px);
  position:relative;  /* <-- ADDED: for absolute positioning children */
}

#header h1 {
  font-size:28px;
  color:#ffffff;
  text-shadow:0 0 5px #000, 0 0 10px #000, 0 0 20px #00ff41;
  letter-spacing:4px;
  font-weight:bold;
  /* Title is now centered by parent flex */
}

/* Move timestamp/status to top-right corner */
.header-info {
  position:absolute;  /* <-- ADDED: absolute positioning */
  right:25px;         /* <-- ADDED: align to right */
  top:15px;           /* <-- ADDED: align to top */
  text-align:right;   /* <-- ADDED: right-align text */
}
```

**HTML - Wrap timestamp/status in div:**
```html
<div id="header">
  <h1>P(DOOM) DASHBOARD – AI Existential Risk Monitor</h1>
  <div class="header-info">  <!-- ADDED wrapper -->
    <div id="timestamp">2025-11-01 13:01:18 AEDT</div>
    <div id="status">MONITORING ACTIVE</div>
  </div>
</div>
```

**How it works:**
- `justify-content:center` centers the h1 in the flex container
- Timestamp/status wrapped in div with `position:absolute` takes them out of flex flow
- They're positioned in top-right corner with `right:25px` and `top:15px`

---

## Method 2: Center with Grid (More Control)

### Description
Use CSS Grid for precise 3-column layout: left (empty), center (title), right (info).

### Code Changes

**CSS:**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  display:grid;                          /* <-- CHANGED: use grid */
  grid-template-columns:1fr auto 1fr;    /* <-- ADDED: 3 columns */
  align-items:center;
  box-shadow:0 0 30px rgba(0,255,65,0.6);
  backdrop-filter:blur(5px);
}

#header h1 {
  font-size:28px;
  color:#ffffff;
  text-shadow:0 0 5px #000, 0 0 10px #000, 0 0 20px #00ff41;
  letter-spacing:4px;
  font-weight:bold;
  grid-column:2;      /* <-- ADDED: place in center column */
  text-align:center;  /* <-- ADDED: center text */
}

.header-info {
  grid-column:3;      /* <-- ADDED: place in right column */
  text-align:right;   /* <-- ADDED: right-align text */
}
```

**HTML:**
```html
<div id="header">
  <div></div>  <!-- Empty left column for balance -->
  <h1>P(DOOM) DASHBOARD – AI Existential Risk Monitor</h1>
  <div class="header-info">
    <div id="timestamp">2025-11-01 13:01:18 AEDT</div>
    <div id="status">MONITORING ACTIVE</div>
  </div>
</div>
```

**How it works:**
- `grid-template-columns:1fr auto 1fr` creates:
  - Column 1: Flexible left spacer (1fr)
  - Column 2: Auto-sized center (title)
  - Column 3: Flexible right spacer (1fr)
- Title in column 2 is automatically centered
- Info in column 3 stays right-aligned

---

## Method 3: Pure Centering (Hide Others)

### Description
Only show title, hide timestamp/status. Simplest centering.

### Code Changes

**CSS:**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  display:flex;
  justify-content:center;  /* <-- CHANGED: center */
  align-items:center;
  box-shadow:0 0 30px rgba(0,255,65,0.6);
  backdrop-filter:blur(5px);
}

#header h1 {
  font-size:28px;
  color:#ffffff;
  text-shadow:0 0 5px #000, 0 0 10px #000, 0 0 20px #00ff41;
  letter-spacing:4px;
  font-weight:bold;
}

/* Hide timestamp/status */
#timestamp, #status {
  display:none;  /* <-- ADDED: hide these elements */
}
```

**HTML:** (No changes needed)

**How it works:**
- Only title remains visible
- Flexbox centers it automatically
- Simplest solution if you don't need timestamp/status

---

## Method 4: Absolute Center (No Flex)

### Description
Use absolute positioning to perfectly center title, regardless of other content.

### Code Changes

**CSS:**
```css
#header {
  background:rgba(0,0,0,0.75);
  border-bottom:3px solid #00ff41;
  padding:15px 25px;
  position:relative;  /* <-- CHANGED: for absolute children */
  height:60px;        /* <-- ADDED: fixed height */
  box-shadow:0 0 30px rgba(0,255,65,0.6);
  backdrop-filter:blur(5px);
}

#header h1 {
  font-size:28px;
  color:#ffffff;
  text-shadow:0 0 5px #000, 0 0 10px #000, 0 0 20px #00ff41;
  letter-spacing:4px;
  font-weight:bold;
  position:absolute;     /* <-- ADDED: absolute positioning */
  left:50%;              /* <-- ADDED: start at 50% */
  top:50%;               /* <-- ADDED: start at 50% */
  transform:translate(-50%, -50%);  /* <-- ADDED: offset by own size */
}

.header-info {
  position:absolute;
  right:25px;
  top:50%;
  transform:translateY(-50%);  /* <-- ADDED: vertical center */
  text-align:right;
}
```

**How it works:**
- Title positioned at `left:50%, top:50%` (center of parent)
- `transform:translate(-50%, -50%)` shifts it back by half its own width/height
- This perfectly centers it regardless of title length
- Info positioned absolute in top-right

---

## Comparison Table

| Method | Pros | Cons | Best For |
|--------|------|------|----------|
| **1. Flexbox** | Simple, modern | Requires HTML change | Most cases |
| **2. Grid** | Precise control | More complex | Complex layouts |
| **3. Hide Others** | Simplest code | Loses info display | Minimal design |
| **4. Absolute** | Perfect centering | Fixed height needed | Pixel-perfect |

---

## Recommended: Method 1 (Flexbox)

**Why:**
- Clean modern approach
- Easy to understand
- Responsive by default
- Minimal code changes

---

## Implementation Files

I've created 4 variations in this directory:
1. `method1-flexbox.html` - Flexbox approach
2. `method2-grid.html` - CSS Grid approach
3. `method3-hide.html` - Hide timestamp/status
4. `method4-absolute.html` - Absolute positioning

Each file has comments explaining the changes.

---

## Testing Checklist

For each method, verify:
- ✅ Title is visually centered
- ✅ Timestamp/status readable (or hidden if Method 3)
- ✅ Responsive on different window sizes
- ✅ All other dashboard functionality intact
- ✅ Graph still renders
- ✅ Warning lights still appear

---

## Quick Implementation

To apply Method 1 (recommended):

1. Find the `#header` CSS block
2. Change `justify-content:space-between` to `justify-content:center`
3. Add `position:relative` to `#header`
4. Wrap timestamp/status in HTML:
   ```html
   <div class="header-info">
     <div id="timestamp">...</div>
     <div id="status">...</div>
   </div>
   ```
5. Add CSS for `.header-info`:
   ```css
   .header-info {
     position:absolute;
     right:25px;
     top:15px;
     text-align:right;
   }
   ```

Done! Title is now centered.
