#!/usr/bin/env python3
"""Update variation titles and headers to match, and ensure responsive viewport"""

import os
import re
from pathlib import Path

# Define variation mappings: filename pattern -> (tab title, h1 header)
VARIATIONS = {
    # Calmer UI
    'CALMER-UI-minimal-no-glows.html': (
        'P(Doom) - Minimal UI (No Glows)',
        '⚠ P(DOOM) DASHBOARD - MINIMAL UI ⚠'
    ),
    'CALMER-UI-soft-muted-colors.html': (
        'P(Doom) - Soft Muted Colors',
        '⚠ P(DOOM) DASHBOARD - SOFT COLORS ⚠'
    ),
    'CALMER-UI-spacious-readable.html': (
        'P(Doom) - Spacious Readable',
        '⚠ P(DOOM) DASHBOARD - SPACIOUS LAYOUT ⚠'
    ),
    
    # Game UI
    'GAME-UI-doom-red-theme.html': (
        'P(Doom) - DOOM Red Theme',
        '⚠ P(DOOM) DASHBOARD - DOOM RED THEME ⚠'
    ),
    'GAME-UI-retro-crt-screen.html': (
        'P(Doom) - Retro CRT Screen',
        '⚠ P(DOOM) DASHBOARD - RETRO CRT ⚠'
    ),
    'GAME-UI-terminal-style-website-code.html': (
        'P(Doom) - Terminal Style',
        '⚠ P(DOOM) DASHBOARD - TERMINAL STYLE ⚠'
    ),
    
    # Investment Graphs
    'INVESTMENT-ai2027-timeline.html': (
        'P(Doom) - AI-2027 Timeline',
        '⚠ P(DOOM) DASHBOARD - AI-2027 TIMELINE ⚠'
    ),
    'INVESTMENT-overlay-dual-axis.html': (
        'P(Doom) - Overlay Dual Axis',
        '⚠ P(DOOM) DASHBOARD - DUAL AXIS VIEW ⚠'
    ),
    'INVESTMENT-secondary-graph.html': (
        'P(Doom) - Secondary Graph',
        '⚠ P(DOOM) DASHBOARD - SECONDARY GRAPH ⚠'
    ),
    
    # Manifold Markets
    'MANIFOLD-aggregated-intelligence.html': (
        'P(Doom) - Aggregated Intelligence',
        '⚠ P(DOOM) DASHBOARD - AGGREGATED INTELLIGENCE ⚠'
    ),
    'MANIFOLD-iframe-embeds.html': (
        'P(Doom) - Manifold iFrame',
        '⚠ P(DOOM) DASHBOARD - MANIFOLD EMBEDS ⚠'
    ),
    'MANIFOLD-live-api-fetch.html': (
        'P(Doom) - Manifold Live API',
        '⚠ P(DOOM) DASHBOARD - LIVE MANIFOLD API ⚠'
    ),
    
    # World Maps
    'WORLDMAP-svg-clickable-regions.html': (
        'P(Doom) - SVG Clickable Map',
        '⚠ P(DOOM) DASHBOARD - CLICKABLE MAP ⚠'
    ),
    'FLOURISH-bubble-investment-map.html': (
        'P(Doom) - Bubble Investment Map',
        '⚠ P(DOOM) DASHBOARD - BUBBLE MAP ⚠'
    ),
    'FLOURISH-choropleth-heat-map.html': (
        'P(Doom) - Choropleth Heat Map',
        '⚠ P(DOOM) DASHBOARD - HEAT MAP ⚠'
    ),
    'FLOURISH-projection-research-centers.html': (
        'P(Doom) - Research Centers Map',
        '⚠ P(DOOM) DASHBOARD - RESEARCH CENTERS ⚠'
    ),
}

def ensure_viewport_meta(content):
    """Ensure proper viewport meta tag exists"""
    viewport_pattern = r'<meta\s+name="viewport"[^>]*>'
    
    if not re.search(viewport_pattern, content):
        # Add viewport meta after charset
        charset_pattern = r'(<meta\s+charset[^>]*>)'
        if re.search(charset_pattern, content):
            content = re.sub(
                charset_pattern,
                r'\1\n<meta name="viewport" content="width=device-width, initial-scale=1.0">',
                content
            )
    return content

def update_titles(filepath):
    """Update title and h1 to be descriptive of variation"""
    
    filename = os.path.basename(filepath)
    
    if filename not in VARIATIONS:
        print(f"Skipping {filename} - no variation mapping")
        return False
    
    tab_title, h1_header = VARIATIONS[filename]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update <title>
    content = re.sub(
        r'<title>.*?</title>',
        f'<title>{tab_title}</title>',
        content
    )
    
    # Update <h1>
    content = re.sub(
        r'<h1>.*?</h1>',
        f'<h1>{h1_header}</h1>',
        content
    )
    
    # Ensure viewport meta
    content = ensure_viewport_meta(content)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Updated: {filename}")
    print(f"  Tab: {tab_title}")
    print(f"  H1:  {h1_header}")
    return True

def main():
    base_dir = Path(__file__).parent
    variations_dir = base_dir / '02-prototypes' / 'integrated' / 'variations'
    
    updated = 0
    
    # Process all variation files
    for root, dirs, files in os.walk(variations_dir):
        for file in files:
            if file.endswith('.html') and file in VARIATIONS:
                filepath = os.path.join(root, file)
                if update_titles(filepath):
                    updated += 1
    
    print(f"\n✅ Updated {updated} variation files")

if __name__ == '__main__':
    main()
