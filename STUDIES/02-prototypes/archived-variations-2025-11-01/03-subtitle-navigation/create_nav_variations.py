#!/usr/bin/env python3
"""
Create 3 navigation link variations for pdoom dashboard
"""

import re
import shutil
from pathlib import Path

BASE_FILE = Path("dashboard-nav.html")
OUTPUT_DIR = Path(".")

def create_method1_subtitle():
    """Method 1: Subtitle row below title"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS for subtitle navigation
    css_addition = """
  .header-content {
    display:flex;
    flex-direction:column;
    align-items:center;
    gap:8px;
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
"""
    
    # Insert CSS before closing style tag
    content = content.replace('</style>', css_addition + '</style>')
    
    # Modify header HTML
    header_pattern = r'(<div id="header">)\s*(<h1>.*?</h1>)\s*(<div id="timestamp">.*?</div>)\s*(<div id="status">.*?</div>)\s*(</div>)'
    
    new_header = r'''<div id="header">
  <div class="header-content">
    \2
    <nav class="subtitle-nav">
      <a href="https://pdoom1.com/" target="_blank">pdoom1</a>
      <span class="nav-separator">|</span>
      <a href="https://github.com/PipFoweraker/pdoom-data" target="_blank">Data Repo</a>
      <span class="nav-separator">|</span>
      <a href="https://github.com/PipFoweraker/pdoom1" target="_blank">Game Repo</a>
    </nav>
  </div>
  <div class="header-info">
    \3
    \4
  </div>
</div>'''
    
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    with open(OUTPUT_DIR / "method1-subtitle.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created method1-subtitle.html")

def create_method2_inline():
    """Method 2: Inline links next to title"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS for inline navigation
    css_addition = """
  .title-row {
    display:flex;
    align-items:baseline;
    gap:20px;
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
    letter-spacing:0.5px;
    font-weight:500;
  }

  .inline-nav a:hover {
    color:#00ff41;
    text-shadow:0 0 8px #00ff41;
  }

  .inline-nav span {
    color:#444444;
  }

  .header-info {
    display:flex;
    flex-direction:column;
    align-items:flex-end;
    gap:4px;
  }
"""
    
    # Make title smaller for inline
    content = re.sub(r'#header h1 \{[^}]+font-size:28px;', 
                     '#header h1 { font-size:22px;', content)
    
    content = content.replace('</style>', css_addition + '</style>')
    
    # Shorten title and add inline nav
    header_pattern = r'(<div id="header">)\s*(<h1>)P\(DOOM\) DASHBOARD – AI Existential Risk Monitor(</h1>)\s*(<div id="timestamp">.*?</div>)\s*(<div id="status">.*?</div>)\s*(</div>)'
    
    new_header = r'''<div id="header">
  <div class="title-row">
    \2P(DOOM) DASHBOARD\3
    <nav class="inline-nav">
      <a href="https://pdoom1.com/" target="_blank">pdoom1</a>
      <span>|</span>
      <a href="https://github.com/PipFoweraker/pdoom-data" target="_blank">Data</a>
      <span>|</span>
      <a href="https://github.com/PipFoweraker/pdoom1" target="_blank">Repo</a>
    </nav>
  </div>
  <div class="header-info">
    \4
    \5
  </div>
</div>'''
    
    content = re.sub(header_pattern, new_header, content, flags=re.DOTALL)
    
    with open(OUTPUT_DIR / "method2-inline.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created method2-inline.html")

def create_method3_separate():
    """Method 3: Separate navigation bar"""
    with open(BASE_FILE) as f:
        content = f.read()
    
    # Add CSS for separate nav bar
    css_addition = """
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
"""
    
    content = content.replace('</style>', css_addition + '</style>')
    
    # Add nav bar after header
    nav_html = '''
<nav id="dashboardNav">
  <ul class="nav-links">
    <li><a href="https://pdoom1.com/" target="_blank">pdoom1 Home</a></li>
    <li><a href="https://github.com/PipFoweraker/pdoom-data" target="_blank">Data Repository</a></li>
    <li><a href="https://github.com/PipFoweraker/pdoom1" target="_blank">Game Repository</a></li>
    <li><a href="/leaderboard/" target="_blank">Leaderboard</a></li>
  </ul>
</nav>
'''
    
    content = content.replace('<div id="container">', nav_html + '\n<div id="container">')
    
    # Adjust container height
    content = re.sub(r'#container \{[^}]+height:100vh;', 
                     '#container { height:calc(100vh - 120px);', content)
    
    with open(OUTPUT_DIR / "method3-separate.html", 'w') as f:
        f.write(content)
    
    print("[OK] Created method3-separate.html")

if __name__ == "__main__":
    if not BASE_FILE.exists():
        print(f"[ERROR] {BASE_FILE} not found!")
        exit(1)
    
    create_method1_subtitle()
    create_method2_inline()
    create_method3_separate()
    
    print("\n[OK] All 3 navigation methods created!")
    print("Files: method1-subtitle.html, method2-inline.html, method3-separate.html")
