#!/usr/bin/env python3
"""
P(Doom) Dashboard Build System
Generates static dashboard from configurable metrics and data sources
"""

import json
import os
import requests
import yaml
from datetime import datetime
from pathlib import Path
from jinja2 import Template
from typing import Dict, List, Any, Optional
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PDoomDashboardBuilder:
    def __init__(self, config_dir: str = "config", data_dir: str = "data", 
                 templates_dir: str = "templates", output_dir: str = "."):
        self.config_dir = Path(config_dir)
        self.data_dir = Path(data_dir)
        self.templates_dir = Path(templates_dir)
        self.output_dir = Path(output_dir)
        
        # Ensure directories exist
        for dir_path in [self.config_dir, self.data_dir, self.templates_dir]:
            dir_path.mkdir(exist_ok=True)
    
    def load_config(self) -> Dict[str, Any]:
        """Load main configuration"""
        config_file = self.config_dir / "dashboard_config.yaml"
        if not config_file.exists():
            return self.create_default_config()
        
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
    
    def create_default_config(self) -> Dict[str, Any]:
        """Create default configuration file"""
        config = {
            'dashboard': {
                'title': 'P(Doom) Global Dashboard',
                'subtitle': 'Real-time AI Safety & Governance Monitoring',
                'update_frequency': '30s',
                'github_repo': 'PipFoweraker/pdoom-data',
                'data_sources': {
                    'pdoom_data_repo': 'https://raw.githubusercontent.com/PipFoweraker/pdoom-data/main',
                    'local_data': './data'
                }
            },
            'suggestion_system': {
                'method': 'github',  # 'github' or 'webform'
                'github_repo': 'PipFoweraker/pdoom-dashboard',
                'webform_endpoint': '/api/suggestions'
            }
        }
        
        config_file = self.config_dir / "dashboard_config.yaml"
        with open(config_file, 'w') as f:
            yaml.dump(config, f, default_flow_style=False)
        
        logger.info(f"Created default config at {config_file}")
        return config
    
    def load_metrics_config(self) -> List[Dict[str, Any]]:
        """Load metrics configuration"""
        metrics_file = self.config_dir / "metrics.yaml"
        if not metrics_file.exists():
            return self.create_default_metrics()
        
        with open(metrics_file, 'r') as f:
            return yaml.safe_load(f)
    
    def create_default_metrics(self) -> List[Dict[str, Any]]:
        """Create default metrics configuration"""
        metrics = [
            {
                'id': 'safety_researchers',
                'title': 'Safety Researchers',
                'description': 'NotKillEveryonist researchers working full-time on AI safety',
                'data_source': 'pdoom_data:safety_researchers.json',
                'placeholder': True,
                'color_scheme': 'safety',
                'grid_position': {'row': 2, 'col': 1},
                'format': 'integer',
                'trend_period': '30d'
            },
            {
                'id': 'governance_researchers', 
                'title': 'Gov Researchers',
                'description': 'AI governance and policy researchers',
                'data_source': 'pdoom_data:governance_researchers.json',
                'placeholder': True,
                'color_scheme': 'neutral',
                'grid_position': {'row': 2, 'col': 2},
                'format': 'integer',
                'trend_period': '30d'
            },
            {
                'id': 'capabilities_researchers',
                'title': 'Capabilities Researchers', 
                'description': 'Researchers working on advancing AI capabilities',
                'data_source': 'pdoom_data:capabilities_researchers.json',
                'placeholder': True,
                'color_scheme': 'danger',
                'grid_position': {'row': 2, 'col': 3},
                'format': 'integer_k',
                'trend_period': '30d',
                'alerts': ['high_growth']
            },
            {
                'id': 'funding_overview',
                'title': 'Funding Overview',
                'description': 'Global AI investment breakdown',
                'data_source': 'pdoom_data:funding_overview.json',
                'placeholder': True,
                'color_scheme': 'funding',
                'grid_position': {'row': 2, 'col': 4},
                'format': 'funding_bars',
                'trend_period': '90d'
            },
            {
                'id': 'aisi_status',
                'title': 'AI Safety Institutes',
                'description': 'Status of AI Safety Institutes globally',
                'data_source': 'pdoom_data:aisi_status.json',
                'placeholder': False,  # This one has real data
                'color_scheme': 'neutral',
                'grid_position': {'row': 3, 'col': 1},
                'format': 'status_list'
            },
            {
                'id': 'governance_scores',
                'title': 'Global Gov Score',
                'description': 'AI Governance effectiveness scores',
                'data_source': 'pdoom_data:governance_scores.json',
                'placeholder': True,
                'color_scheme': 'neutral',
                'grid_position': {'row': 3, 'col': 2},
                'format': 'score_grid'
            }
        ]
        
        metrics_file = self.config_dir / "metrics.yaml"
        with open(metrics_file, 'w') as f:
            yaml.dump(metrics, f, default_flow_style=False)
        
        logger.info(f"Created default metrics config at {metrics_file}")
        return metrics
    
    def fetch_data_source(self, source_spec: str) -> Optional[Dict[str, Any]]:
        """Fetch data from various sources"""
        if ':' not in source_spec:
            logger.error(f"Invalid source spec: {source_spec}")
            return None
        
        source_type, source_path = source_spec.split(':', 1)
        
        if source_type == 'pdoom_data':
            return self.fetch_from_pdoom_data(source_path)
        elif source_type == 'local':
            return self.fetch_from_local(source_path)
        elif source_type == 'url':
            return self.fetch_from_url(source_path)
        else:
            logger.error(f"Unknown source type: {source_type}")
            return None
    
    def fetch_from_pdoom_data(self, path: str) -> Optional[Dict[str, Any]]:
        """Fetch data from pdoom-data repository"""
        config = self.load_config()
        base_url = config['dashboard']['data_sources']['pdoom_data_repo']
        url = f"{base_url}/dashboard_exports/{path}"
        
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.warning(f"Failed to fetch {url}: {e}")
            return None
        except json.JSONDecodeError as e:
            logger.warning(f"Invalid JSON from {url}: {e}")
            return None
    
    def fetch_from_local(self, path: str) -> Optional[Dict[str, Any]]:
        """Fetch data from local file"""
        file_path = self.data_dir / path
        if not file_path.exists():
            logger.warning(f"Local file not found: {file_path}")
            return None
        
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            logger.warning(f"Invalid JSON in {file_path}: {e}")
            return None
    
    def fetch_from_url(self, url: str) -> Optional[Dict[str, Any]]:
        """Fetch data from arbitrary URL"""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            logger.warning(f"Failed to fetch {url}: {e}")
            return None
    
    def create_sample_data(self, metric_id: str) -> Dict[str, Any]:
        """Create sample data for placeholder metrics"""
        samples = {
            'safety_researchers': {
                'current_value': 847,
                'trend': '+23',
                'trend_period': '30d',
                'last_updated': datetime.now().isoformat(),
                'breakdown': {
                    'academic': 312,
                    'industry': 289,
                    'independent': 246
                },
                'confidence': 'low'
            },
            'governance_researchers': {
                'current_value': 312,
                'trend': '+8',
                'trend_period': '30d',
                'last_updated': datetime.now().isoformat(),
                'confidence': 'medium'
            },
            'capabilities_researchers': {
                'current_value': 15247,
                'trend': '+892',
                'trend_period': '30d',
                'last_updated': datetime.now().isoformat(),
                'alerts': ['accelerating_hiring'],
                'confidence': 'low'
            }
        }
        
        return samples.get(metric_id, {
            'current_value': 0,
            'trend': '±0',
            'trend_period': '30d',
            'last_updated': datetime.now().isoformat(),
            'confidence': 'unknown'
        })
    
    def load_template(self, template_name: str) -> Template:
        """Load Jinja2 template"""
        template_path = self.templates_dir / template_name
        if not template_path.exists():
            self.create_default_template()
        
        with open(template_path, 'r') as f:
            return Template(f.read())
    
    def create_default_template(self):
        """Create default dashboard template"""
        # This would be the HTML template version of your dashboard
        # For now, I'll create a simplified version
        template_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ config.dashboard.title }}</title>
    <style>
        /* CSS would go here - similar to your current dashboard */
    </style>
</head>
<body>
    <div class="strategic-grid">
        <div class="header-bar">
            <div class="header-title">{{ config.dashboard.title }}</div>
            <div class="header-status">LIVE | {{ timestamp }} | STATUS: MONITORING</div>
        </div>
        
        {% for metric in metrics %}
        <div class="metric-box" data-metric="{{ metric.id }}">
            {% if metric.placeholder %}
            <div class="placeholder-overlay"></div>
            <div class="placeholder-badge">PLACEHOLDER</div>
            <button class="suggest-data-btn" onclick="openSuggestionModal('{{ metric.id }}')">SUGGEST DATA</button>
            {% endif %}
            
            <div class="metric-header">{{ metric.title }}</div>
            <div class="metric-value {{ metric.color_scheme }}">{{ metric.data.current_value }}</div>
            <div class="metric-trend">{{ metric.data.trend }} {{ metric.data.trend_period }}</div>
        </div>
        {% endfor %}
    </div>
    
    <script>
        // JavaScript would go here
    </script>
</body>
</html>"""
        
        template_path = self.templates_dir / "dashboard.html"
        with open(template_path, 'w') as f:
            f.write(template_content)
        
        logger.info(f"Created default template at {template_path}")
    
    def build_dashboard(self):
        """Main build function"""
        logger.info("Building P(Doom) dashboard...")
        
        # Load configuration
        config = self.load_config()
        metrics_config = self.load_metrics_config()
        
        # Fetch data for each metric
        metrics_with_data = []
        for metric in metrics_config:
            logger.info(f"Processing metric: {metric['id']}")
            
            data = None
            if not metric.get('placeholder', True):
                data = self.fetch_data_source(metric['data_source'])
            
            if data is None:
                logger.info(f"Using sample data for {metric['id']}")
                data = self.create_sample_data(metric['id'])
            
            metric['data'] = data
            metrics_with_data.append(metric)
        
        # Load template and render
        template = self.load_template("dashboard.html")
        
        rendered_html = template.render(
            config=config,
            metrics=metrics_with_data,
            timestamp=datetime.now().strftime('%H:%M:%S AEDT'),
            build_time=datetime.now().isoformat()
        )
        
        # Write output
        output_file = self.output_dir / "index.html"
        with open(output_file, 'w') as f:
            f.write(rendered_html)
        
        logger.info(f"Dashboard built successfully: {output_file}")
        
        # Generate data manifest
        self.generate_data_manifest(metrics_with_data)
    
    def generate_data_manifest(self, metrics: List[Dict[str, Any]]):
        """Generate manifest of data sources and freshness"""
        manifest = {
            'build_time': datetime.now().isoformat(),
            'metrics': []
        }
        
        for metric in metrics:
            manifest['metrics'].append({
                'id': metric['id'],
                'title': metric['title'],
                'data_source': metric['data_source'],
                'placeholder': metric.get('placeholder', True),
                'last_updated': metric['data'].get('last_updated'),
                'confidence': metric['data'].get('confidence', 'unknown')
            })
        
        manifest_file = self.output_dir / "data_manifest.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        
        logger.info(f"Data manifest generated: {manifest_file}")

def main():
    """CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Build P(Doom) Dashboard")
    parser.add_argument("--config-dir", default="config", help="Configuration directory")
    parser.add_argument("--data-dir", default="data", help="Data directory")
    parser.add_argument("--templates-dir", default="templates", help="Templates directory")
    parser.add_argument("--output-dir", default=".", help="Output directory")
    parser.add_argument("--init", action="store_true", help="Initialize default configuration")
    
    args = parser.parse_args()
    
    builder = PDoomDashboardBuilder(
        config_dir=args.config_dir,
        data_dir=args.data_dir, 
        templates_dir=args.templates_dir,
        output_dir=args.output_dir
    )
    
    if args.init:
        logger.info("Initializing default configuration...")
        builder.load_config()
        builder.load_metrics_config()
        builder.create_default_template()
        logger.info("Initialization complete!")
    else:
        builder.build_dashboard()

if __name__ == "__main__":
    main()
