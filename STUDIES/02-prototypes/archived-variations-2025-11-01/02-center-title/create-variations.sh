#!/bin/bash
# Create 4 different centering methods

BASE="dashboard-centered.html"

# Method 1: Flexbox
cp "$BASE" method1-flexbox.html
sed -i '24s/justify-content:space-between;/justify-content:center;/' method1-flexbox.html
sed -i '20a\    position:relative;' method1-flexbox.html
sed -i '/justify-content:center;/a\  }\
\
  .header-info {\
    position:absolute;\
    right:25px;\
    top:15px;\
    text-align:right;' method1-flexbox.html

# Method 2: Grid  
cp "$BASE" method2-grid.html
sed -i '24s/display:flex;/display:grid;/' method2-grid.html
sed -i '24a\    grid-template-columns:1fr auto 1fr;' method2-grid.html
sed -i '31a\    grid-column:2;\
    text-align:center;' method2-grid.html
sed -i '/display:grid;/a\  }\
\
  .header-info {\
    grid-column:3;\
    text-align:right;' method2-grid.html

# Method 3: Hide others
cp "$BASE" method3-hide.html
sed -i '25s/justify-content:space-between;/justify-content:center;/' method3-hide.html
sed -i '/justify-content:center;/a\  }\
\
  #timestamp, #status {\
    display:none;' method3-hide.html

# Method 4: Absolute
cp "$BASE" method4-absolute.html
sed -i '24s/display:flex;/position:relative;/' method4-absolute.html
sed -i '24a\    height:60px;' method4-absolute.html
sed -i '31a\    position:absolute;\
    left:50%;\
    top:50%;\
    transform:translate(-50%, -50%);' method4-absolute.html
sed -i '/height:60px;/a\  }\
\
  .header-info {\
    position:absolute;\
    right:25px;\
    top:50%;\
    transform:translateY(-50%);\
    text-align:right;' method4-absolute.html

echo "[OK] Created 4 method variations"
ls -lh method*.html
