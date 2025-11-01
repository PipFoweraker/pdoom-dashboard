# P(doom)1 Style Guide
**Visual Design System for AI Risk Dashboards**

---

## Color Palette

### Primary Colors
```css
--bg-primary: #1a1a1a;      /* Near-black background */
--bg-secondary: #2d2d2d;    /* Dark gray panels */
--bg-tertiary: #3d3d3d;     /* Medium-dark gray elements */
```

### Accent Colors
```css
--accent-matrix-green: #00ff41;   /* Matrix green - primary interactive */
--accent-warning: #ff6b35;        /* Warning orange - caution states */
--accent-danger: #ff4444;         /* Error red - critical alerts */
--accent-success: #4caf50;        /* Success green - positive states */
```

### Text Colors
```css
--text-primary: #ffffff;     /* White - main text */
--text-secondary: #cccccc;   /* Light gray - secondary text */
--text-muted: #888888;       /* Medium gray - less important */
```

### Utility Colors
```css
--border-color: #444444;     /* Dark gray borders */
--shadow-green: rgba(0, 255, 65, 0.3);   /* Glow effect */
```

---

## Typography

### Font Family
```css
font-family: 'Courier New', monospace;
```
**Rationale:** Terminal/retro aesthetic, reinforces hacker/developer culture

### Font Sizes
```css
--font-3xl: 3rem;      /* Major headings */
--font-2xl: 2rem;      /* Section headings */
--font-xl: 1.5rem;     /* Subheadings */
--font-lg: 1.25rem;    /* Large body text */
--font-base: 1rem;     /* Body text */
--font-sm: 0.875rem;   /* Small text */
--font-xs: 0.75rem;    /* Extra small */
```

### Font Weights
```css
--weight-normal: 400;
--weight-semibold: 600;
--weight-bold: 700;
```

---

## Spacing System

### Padding/Margin Scale
```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
```

---

## Border Radius

```css
--radius-sm: 4px;      /* Small elements */
--radius-md: 6px;      /* Medium elements */
--radius-lg: 10px;     /* Large panels */
```

---

## Shadows & Effects

### Box Shadows
```css
--shadow-glow-green: 0 0 20px rgba(0, 255, 65, 0.4);
--shadow-glow-orange: 0 0 20px rgba(255, 107, 53, 0.4);
--shadow-glow-red: 0 0 20px rgba(255, 68, 68, 0.4);
--shadow-panel: 0 10px 20px rgba(0, 255, 65, 0.3);
```

### Text Shadows
```css
--text-glow-green: 0 0 15px #00ff41;
--text-glow-orange: 0 0 15px #ff6b35;
--text-glow-red: 0 0 15px #ff4444;
--text-shadow-black: 0 0 3px #000, 0 0 8px #000; /* Readability on backgrounds */
```

---

## Animation

### Timing Functions
```css
--ease-smooth: cubic-bezier(0.2, 0.8, 0.2, 1);
```

### Durations
```css
--duration-fast: 150ms;
--duration-base: 300ms;
--duration-slow: 500ms;
```

### Example Animations

**Pulse (for status indicators):**
```css
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.7; }
}
animation: pulse 2s infinite ease-in-out;
```

**Blink (for critical warnings):**
```css
@keyframes blink {
  0%, 50%, 100% { opacity: 1; }
  25%, 75% { opacity: 0.5; }
}
animation: blink 1.5s infinite;
```

---

## Layout Patterns

### Grid System
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
gap: 1rem;
```

### Flexbox Utilities
```css
display: flex;
justify-content: space-between;
align-items: center;
```

### Container Max Width
```css
max-width: 1200px;
margin: 0 auto;
```

---

## Component Patterns

### Panel/Card
```css
.panel {
  background: #2d2d2d;
  border: 1px solid #444;
  border-radius: 10px;
  padding: 1.5rem;
  box-shadow: 0 10px 20px rgba(0, 255, 65, 0.3);
}
```

### Button
```css
.button {
  background: #00ff41;
  color: #1a1a1a;
  border: none;
  border-radius: 6px;
  padding: 0.75rem 1.5rem;
  font-family: 'Courier New', monospace;
  font-weight: 600;
  cursor: pointer;
  transition: all 300ms cubic-bezier(0.2, 0.8, 0.2, 1);
}

.button:hover {
  box-shadow: 0 0 20px rgba(0, 255, 65, 0.6);
}
```

### Header
```css
.header {
  background: linear-gradient(180deg, #1a1a1a 0%, #2d2d2d 100%);
  border-bottom: 2px solid #00ff41;
  padding: 1rem 2rem;
  box-shadow: 0 0 30px rgba(0, 255, 65, 0.4);
}
```

### Metric Display
```css
.metric {
  background: rgba(0, 40, 20, 0.8);
  border-left: 4px solid #00ff41;
  padding: 1rem;
  border-radius: 4px;
}

.metric-value {
  font-size: 2rem;
  color: #00ff41;
  text-shadow: 0 0 15px #00ff41;
  font-weight: bold;
}
```

### Warning States
```css
.warning {
  color: #ff6b35;
  border-left-color: #ff6b35;
  text-shadow: 0 0 15px #ff6b35;
}

.critical {
  color: #ff4444;
  border-left-color: #ff4444;
  text-shadow: 0 0 20px #ff4444;
  animation: blink 1.5s infinite;
}
```

---

## Accessibility

### Contrast Requirements
- Matrix green (#00ff41) on black (#1a1a1a): **19.97:1** ✅
- White (#ffffff) on dark gray (#2d2d2d): **13.14:1** ✅
- Orange (#ff6b35) on black: **6.41:1** ✅

### Focus States
```css
:focus {
  outline: 2px solid #00ff41;
  outline-offset: 2px;
}
```

---

## Dashboard-Specific Guidelines

### Transparency for Shader Backgrounds
```css
background: rgba(0, 0, 0, 0.75);
backdrop-filter: blur(8px);
```

### High-Contrast Text on Dynamic Backgrounds
```css
text-shadow:
  0 0 3px #000,      /* Inner shadow for readability */
  0 0 8px #000,      /* Mid shadow for depth */
  0 0 15px #00ff41;  /* Outer glow for accent */
```

### Scrollbar Styling
```css
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: rgba(0, 10, 5, 0.5);
  border-radius: 5px;
}

::-webkit-scrollbar-thumb {
  background: #00ff41;
  border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
  background: #00ff41ee;
  box-shadow: 0 0 10px #00ff41;
}
```

---

## Usage Examples

### Dashboard Header
```html
<header class="header">
  <h1 style="color: #00ff41; text-shadow: 0 0 20px #00ff41;">
    ⚠ P(DOOM) DASHBOARD ⚠
  </h1>
  <div class="timestamp" style="color: #0ff; text-shadow: 0 0 12px #0ff;">
    2025-10-29 22:45:12 UTC
  </div>
</header>
```

### Metric Card
```html
<div class="metric warning">
  <div class="metric-label">P(doom) Estimate</div>
  <div class="metric-value">12.1%</div>
  <div class="metric-subtext">Expert consensus</div>
</div>
```

### Critical Alert
```html
<div class="alert critical">
  <span class="alert-icon">⚠</span>
  <span class="alert-text">EXPONENTIAL ESCALATION DETECTED</span>
</div>
```

---

## Design Philosophy

**Cyberpunk Terminal Aesthetic**
- Dark backgrounds evoke command-line interfaces
- Matrix green represents "the code" / AI systems
- Monospace typography reinforces developer culture
- Glow effects suggest screens in dark rooms
- Orange/red warnings create urgency

**Information Density**
- High-information dashboards with multiple data streams
- Clear visual hierarchy through color and size
- Animation draws attention to changing/critical data

**Contrast & Readability**
- High contrast ratios ensure accessibility
- Multiple shadow layers for text on dynamic backgrounds
- Color coding provides instant semantic meaning

---

**Version:** 1.0
**Last Updated:** October 29, 2025
**Based on:** pdoom1.com visual analysis
