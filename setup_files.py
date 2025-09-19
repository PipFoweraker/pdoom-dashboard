#!/usr/bin/env python3
"""
Quick setup script for P(Doom) Dashboard
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd):
    """Run command and return success status"""
    try:
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def create_directory_structure():
    """Create necessary directories"""
    directories = [
        'config',
        'data', 
        'templates',
        '.github/workflows'
    ]
    
    for dir_name in directories:
        Path(dir_name).mkdir(parents=True, exist_ok=True)
        print(f"✓ Created directory: {dir_name}")

def create_requirements():
    """Create requirements.txt if it doesn't exist"""
    requirements_content = """jinja2>=3.1.0
pyyaml>=6.0
requests>=2.28.0
"""
    
    if not Path('requirements.txt').exists():
        with open('requirements.txt', 'w') as f:
            f.write(requirements_content)
        print("✓ Created requirements.txt")

def create_github_workflow():
    """Create GitHub Actions workflow"""
    workflow_content = """# .github/workflows/build-dashboard.yml
name: Build P(Doom) Dashboard

on:
  push:
    branches: [ main ]
  schedule:
    - cron: '0 * * * *'  # Build hourly
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    
    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Build dashboard
      run: |
        python build.py --init
        python build.py
    
    - uses: actions/configure-pages@v3
    - uses: actions/upload-pages-artifact@v2
      with:
        path: '.'
    - uses: actions/deploy-pages@v2
      id: deployment
"""
    
    workflow_path = Path('.github/workflows/build-dashboard.yml')
    if not workflow_path.exists():
        workflow_path.parent.mkdir(parents=True, exist_ok=True)
        with open(workflow_path, 'w') as f:
            f.write(workflow_content)
        print("✓ Created GitHub Actions workflow")

def create_readme():
    """Create README.md"""
    readme_content = """# P(Doom) Dashboard

A strategic dashboard for monitoring global AI safety metrics.

## Quick Start

1. **Setup:**
   ```bash
   python setup.py  # Run this setup script
   pip install -r requirements.txt
   ```

2. **Initialize configuration:**
   ```bash
   python build.py --init
   ```

3. **Build dashboard:**
   ```bash
   python build.py
   ```

4. **Serve locally:**
   ```bash
   python -m http.server 8000
   # Visit http://localhost:8000
   ```

## Architecture

- `build.py` - Main build system
- `config/` - Dashboard and metrics configuration
- `templates/` - Jinja2 HTML templates
- `data/` - Local data cache
- `.github/workflows/` - Automated builds

## Data Sources

The dashboard pulls data from the [pdoom-data repository](https://github.com/PipFoweraker/pdoom-data) via the protocol defined in `docs/data_schema.md`.

## Configuration

Edit `config/dashboard_config.yaml` and `config/metrics.yaml` to customize the dashboard.

## Deployment

GitHub Pages deployment is automatic via GitHub Actions when you push to main.

Custom domain: Configure in repository settings under Pages.
"""
    
    if not Path('README.md').exists():
        with open('README.md', 'w') as f:
            f.write(readme_content)
        print("✓ Created README.md")

def main():
    """Main setup function"""
    print("Setting up P(Doom) Dashboard...")
    
    create_directory_structure()
    create_requirements()
    create_github_workflow() 
    create_readme()
    
    print("\n✓ Setup complete!")
    print("\nNext steps:")
    print("1. pip install -r requirements.txt")
    print("2. python build.py --init")
    print("3. python build.py")
    print("4. python -m http.server 8000")
    print("\nThen visit http://localhost:8000")

if __name__ == "__main__":
    main()
