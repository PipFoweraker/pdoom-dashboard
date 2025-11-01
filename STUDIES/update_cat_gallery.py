#!/usr/bin/env python3
"""Update all study HTML files with cat gallery functionality"""

import os
import re
from pathlib import Path

# Cat gallery CSS
CAT_CSS = '''  /* Cat cam */
  #catCam {
    margin-top:18px;
    padding:12px;
    background:rgba(0,20,10,0.75);
    border:2px solid #00ff41;
    border-radius:6px;
    cursor: pointer;
  }

  #catCam img {
    width:100%;
    border-radius:6px;
    border:2px solid #00ff41;
    box-shadow:0 0 20px rgba(0,255,65,0.4);
    transition: opacity 0.3s ease;
  }

  #catStatus {
    text-align:center;
    font-size:11px;
    color:#ffffff;
    margin-top:8px;
    font-weight:bold;
    text-shadow:0 0 2px #000, 0 0 5px #000, 0 0 10px #00ff41;
  }'''

# Cat gallery HTML
CAT_HTML = '''      <!-- Cat Cam -->
      <div id="catCam" onclick="nextCat()" title="Click to see next cat">
        <div class="metric-label" style="text-align:center;margin-bottom:10px;">🐱 CAT CAM</div>
        <img id="catImage" src="../../assets/cat-gallery/web-luna.jpg" alt="Office Cat">
        <div id="catStatus">Luna (Nicki T.) - Click for next cat</div>
      </div>'''

# Cat gallery JavaScript
CAT_JS = '''
// Cat Gallery Rotation
const cats = [
  {name: 'Luna', custodian: 'Nicki T.', file: 'web-luna.jpg'},
  {name: 'Arwen & Chuck', custodian: 'Matilda', file: 'web-arwen-chuck.jpg'},
  {name: 'Arwen', custodian: 'Matilda', file: 'web-arwen.jpg'},
  {name: 'Chucky', custodian: 'Nicki T.', file: 'web-chucky.jpg'},
  {name: 'Mando (Jiggly)', custodian: 'Nicki T.', file: 'web-mando.jpg'},
  {name: 'Missy', custodian: 'Spicy', file: 'web-missy.jpg'},
  {name: 'Nigel', custodian: 'Nicki T.', file: 'web-nigel.jpg'},
  {name: 'Doom Cat', custodian: 'Office', file: 'web-doom-cat.jpg'}
];
let currentCat = 0;

function nextCat() {
  currentCat = (currentCat + 1) % cats.length;
  updateCat();
}

function updateCat() {
  const cat = cats[currentCat];
  const img = document.getElementById('catImage');
  const status = document.getElementById('catStatus');
  
  if (!img || !status) return;
  
  img.style.opacity = '0';
  setTimeout(() => {
    img.src = '../../assets/cat-gallery/' + cat.file;
    img.alt = cat.name;
    status.textContent = cat.name + ' (' + cat.custodian + ') - Click for next cat';
    img.style.opacity = '1';
  }, 300);
}

// Auto-rotate every 30 seconds
setInterval(nextCat, 30000);
'''

def calculate_relative_path(html_file, base_dir):
    """Calculate relative path to cat-gallery from HTML file"""
    html_path = Path(html_file).parent
    gallery_path = Path(base_dir) / 'assets' / 'cat-gallery'
    rel_path = os.path.relpath(gallery_path, html_path)
    return rel_path.replace('\\', '/')

def update_html_file(filepath, base_dir):
    """Update a single HTML file with cat gallery"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has catCam
    if 'catCam' not in content:
        print(f"Skipping {filepath} - no catCam found")
        return False
    
    # Calculate relative path
    rel_path = calculate_relative_path(filepath, base_dir)
    
    # Update CSS
    css_pattern = r'/\* Cat cam \*/\s*#catCam\s*{[^}]+}[^/]*(#catCam img\s*{[^}]+}[^/]*)?(#catStatus\s*{[^}]+})?'
    if re.search(css_pattern, content, re.DOTALL):
        content = re.sub(css_pattern, CAT_CSS, content, flags=re.DOTALL)
    
    # Update HTML
    html_pattern = r'<!-- Cat Cam -->.*?</div>\s*</div>'
    if re.search(html_pattern, content, re.DOTALL):
        # Update the HTML with correct relative path
        cat_html_updated = CAT_HTML.replace('../../assets/cat-gallery/', rel_path + '/')
        # Match the specific cat cam section
        match = re.search(r'(<!-- Cat Cam -->.*?<div id="catCam"[^>]*>.*?</div>)(\s*</div>)', content, re.DOTALL)
        if match:
            cat_section = f'''      <!-- Cat Cam -->
      <div id="catCam" onclick="nextCat()" title="Click to see next cat">
        <div class="metric-label" style="text-align:center;margin-bottom:10px;">🐱 CAT CAM</div>
        <img id="catImage" src="{rel_path}/web-luna.jpg" alt="Office Cat">
        <div id="catStatus">Luna (Nicki T.) - Click for next cat</div>
      </div>'''
            content = content.replace(match.group(1), cat_section)
    
    # Add or update JavaScript
    js_pattern = r'// Cat Gallery Rotation.*?setInterval\(nextCat, \d+\);'
    cat_js_updated = CAT_JS.replace('../../assets/cat-gallery/', rel_path + '/')
    
    if re.search(js_pattern, content, re.DOTALL):
        # Update existing
        content = re.sub(js_pattern, cat_js_updated.strip(), content, flags=re.DOTALL)
    else:
        # Add after first <script> tag
        script_match = re.search(r'(<script[^>]*>)', content)
        if script_match:
            insert_pos = script_match.end()
            content = content[:insert_pos] + cat_js_updated + content[insert_pos:]
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filepath}")
    return True

def main():
    base_dir = Path(__file__).parent
    studies_dir = base_dir
    
    # Find all HTML files with catCam
    html_files = []
    for root, dirs, files in os.walk(studies_dir):
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    if 'catCam' in f.read():
                        html_files.append(filepath)
    
    print(f"Found {len(html_files)} files with catCam")
    
    updated = 0
    for filepath in html_files:
        if update_html_file(filepath, base_dir):
            updated += 1
    
    print(f"\nUpdated {updated} files with cat gallery")

if __name__ == '__main__':
    main()
