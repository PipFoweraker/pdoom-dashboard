#!/bin/bash
# Apply CSS Variables and Design System

FILE="dashboard-v1.html"

# Backup
cp "$FILE" "${FILE}.backup"

# Add CSS variables right after <style> tag
sed -i '/<style>/a\
  :root {\
    --bg-primary: #000000;\
    --bg-secondary: rgba(0, 0, 0, 0.85);\
    --bg-overlay: rgba(0, 0, 0, 0.7);\
    --bg-panel: rgba(0, 0, 0, 0.75);\
    --accent-primary: #00ff41;\
    --accent-secondary: #ff6b35;\
    --accent-danger: #ff4444;\
    --accent-info: #00ffff;\
    --text-primary: #ffffff;\
    --text-secondary: #cccccc;\
    --border-primary: #00ff41;\
    --border-secondary: #444444;\
    --shadow-glow: rgba(0, 255, 65, 0.5);\
    --spacing-sm: 10px;\
    --spacing-md: 15px;\
    --spacing-lg: 20px;\
    --spacing-xl: 25px;\
    --border-radius-sm: 5px;\
    --border-radius-md: 8px;\
    --border-width: 3px;\
  }\
' "$FILE"

# Replace hardcoded values with CSS variables
sed -i 's/background:#000;/background:var(--bg-primary);/g' "$FILE"
sed -i 's/background:rgba(0,0,0,0\.75);/background:var(--bg-panel);/g' "$FILE"
sed -i 's/background:rgba(0,0,0,0\.85);/background:var(--bg-secondary);/g' "$FILE"
sed -i 's/background:rgba(0,0,0,0\.7);/background:var(--bg-overlay);/g' "$FILE"
sed -i 's/border:3px solid #00ff41;/border:var(--border-width) solid var(--border-primary);/g' "$FILE"
sed -i 's/border:2px solid #00ff41;/border:2px solid var(--border-primary);/g' "$FILE"
sed -i 's/border-bottom:3px solid #00ff41;/border-bottom:var(--border-width) solid var(--border-primary);/g' "$FILE"
sed -i 's/border-bottom:2px solid #00ff41;/border-bottom:2px solid var(--border-primary);/g' "$FILE"
sed -i 's/border-left:3px solid #00ff41;/border-left:var(--border-width) solid var(--border-primary);/g' "$FILE"
sed -i 's/border-left:2px solid #00ff41;/border-left:2px solid var(--border-primary);/g' "$FILE"
sed -i 's/color:#ffffff;/color:var(--text-primary);/g' "$FILE"
sed -i 's/color:#00ff41;/color:var(--accent-primary);/g' "$FILE"
sed -i 's/color:#ff6b35;/color:var(--accent-secondary);/g' "$FILE"
sed -i 's/color:#ff4444;/color:var(--accent-danger);/g' "$FILE"
sed -i 's/color:#0ff;/color:var(--accent-info);/g' "$FILE"
sed -i 's/padding:15px;/padding:var(--spacing-md);/g' "$FILE"
sed -i 's/padding:20px;/padding:var(--spacing-lg);/g' "$FILE"
sed -i 's/padding:25px;/padding:var(--spacing-xl);/g' "$FILE"
sed -i 's/padding:10px;/padding:var(--spacing-sm);/g' "$FILE"
sed -i 's/gap:15px;/gap:var(--spacing-md);/g' "$FILE"
sed -i 's/gap:10px;/gap:var(--spacing-sm);/g' "$FILE"
sed -i 's/border-radius:8px;/border-radius:var(--border-radius-md);/g' "$FILE"
sed -i 's/border-radius:5px;/border-radius:var(--border-radius-sm);/g' "$FILE"

echo "[OK] Design system applied to $FILE"
echo "[OK] Backup saved as ${FILE}.backup"
