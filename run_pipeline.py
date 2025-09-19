#!/usr/bin/env python3
"""
Data Pipeline Management Script

Moves data through pipeline stages: raw -> curated -> transformed -> servable
Supports dry-run mode for testing without making changes.
"""

import os
import json
import shutil
import yaml
from datetime import datetime
import argparse

def load_pipeline_config():
    """Load pipeline configuration"""
    config_path = os.path.join('config', 'dashboard_config.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    return {}

def log_pipeline_action(stage, action, files, dry_run=False):
    """Log pipeline actions"""
    log_entry = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'stage': stage,
        'action': action,
        'files_processed': len(files),
        'files': files,
        'dry_run': dry_run
    }
    
    log_file = os.path.join('data', 'metadata', 'pipeline_log.json')
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            log_data = json.load(f)
    else:
        log_data = {'pipeline_runs': []}
    
    log_data['pipeline_runs'].append(log_entry)
    log_data['pipeline_runs'] = log_data['pipeline_runs'][-100:]  # Keep last 100
    
    if not dry_run:
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
    
    return log_entry

def curate_data(dry_run=False):
    """Stage 1: Raw -> Curated (validate and clean)"""
    print("=== CURATION STAGE: Raw -> Curated ===")
    
    raw_dir = os.path.join('data', 'raw')
    curated_dir = os.path.join('data', 'curated')
    
    if not os.path.exists(raw_dir):
        print("No raw data directory found")
        return []
    
    processed_files = []
    
    for root, dirs, files in os.walk(raw_dir):
        for file in files:
            if file.endswith('.json'):
                raw_file = os.path.join(root, file)
                rel_path = os.path.relpath(raw_file, raw_dir)
                curated_file = os.path.join(curated_dir, rel_path)
                
                try:
                    # Load and validate
                    with open(raw_file, 'r') as f:
                        data = json.load(f)
                    
                    # Basic validation
                    if 'metrics' not in data:
                        print(f"  ✗ {rel_path}: Missing 'metrics' field")
                        continue
                    
                    # Clean and validate metrics
                    clean_metrics = []
                    for metric in data.get('metrics', []):
                        if 'name' in metric and 'value' in metric:
                            # Add quality metadata
                            metric['curated_at'] = datetime.utcnow().isoformat() + 'Z'
                            metric['quality_check'] = 'passed'
                            clean_metrics.append(metric)
                    
                    data['metrics'] = clean_metrics
                    data['curated_at'] = datetime.utcnow().isoformat() + 'Z'
                    data['stage'] = 'curated'
                    
                    print(f"  ✓ {rel_path}: {len(clean_metrics)} metrics validated")
                    
                    if not dry_run:
                        os.makedirs(os.path.dirname(curated_file), exist_ok=True)
                        with open(curated_file, 'w') as f:
                            json.dump(data, f, indent=2)
                    
                    processed_files.append(rel_path)
                    
                except Exception as e:
                    print(f"  ✗ {rel_path}: Error - {e}")
    
    log_pipeline_action('curate', 'raw_to_curated', processed_files, dry_run)
    return processed_files

def transform_data(dry_run=False):
    """Stage 2: Curated -> Transformed (aggregate and enrich)"""
    print("=== TRANSFORMATION STAGE: Curated -> Transformed ===")
    
    curated_dir = os.path.join('data', 'curated')
    transformed_dir = os.path.join('data', 'transformed')
    
    if not os.path.exists(curated_dir):
        print("No curated data directory found")
        return []
    
    processed_files = []
    
    for root, dirs, files in os.walk(curated_dir):
        for file in files:
            if file.endswith('.json'):
                curated_file = os.path.join(root, file)
                rel_path = os.path.relpath(curated_file, curated_dir)
                transformed_file = os.path.join(transformed_dir, rel_path)
                
                try:
                    with open(curated_file, 'r') as f:
                        data = json.load(f)
                    
                    # Add transformations (example)
                    for metric in data.get('metrics', []):
                        # Add computed fields
                        metric['transformed_at'] = datetime.utcnow().isoformat() + 'Z'
                        # Example: categorize values
                        value = metric.get('value', 0)
                        if isinstance(value, (int, float)):
                            if value > 1000:
                                metric['magnitude'] = 'high'
                            elif value > 100:
                                metric['magnitude'] = 'medium'
                            else:
                                metric['magnitude'] = 'low'
                    
                    data['transformed_at'] = datetime.utcnow().isoformat() + 'Z'
                    data['stage'] = 'transformed'
                    
                    print(f"  ✓ {rel_path}: Transformed {len(data.get('metrics', []))} metrics")
                    
                    if not dry_run:
                        os.makedirs(os.path.dirname(transformed_file), exist_ok=True)
                        with open(transformed_file, 'w') as f:
                            json.dump(data, f, indent=2)
                    
                    processed_files.append(rel_path)
                    
                except Exception as e:
                    print(f"  ✗ {rel_path}: Error - {e}")
    
    log_pipeline_action('transform', 'curated_to_transformed', processed_files, dry_run)
    return processed_files

def serve_data_stage(dry_run=False):
    """Stage 3: Transformed -> Servable (production ready)"""
    print("=== SERVING STAGE: Transformed -> Servable ===")
    
    transformed_dir = os.path.join('data', 'transformed')
    servable_dir = os.path.join('data', 'servable')
    
    if not os.path.exists(transformed_dir):
        print("No transformed data directory found")
        return []
    
    processed_files = []
    
    for root, dirs, files in os.walk(transformed_dir):
        for file in files:
            if file.endswith('.json'):
                transformed_file = os.path.join(root, file)
                rel_path = os.path.relpath(transformed_file, transformed_dir)
                servable_file = os.path.join(servable_dir, rel_path)
                
                try:
                    with open(transformed_file, 'r') as f:
                        data = json.load(f)
                    
                    # Final preparation for serving
                    data['served_at'] = datetime.utcnow().isoformat() + 'Z'
                    data['stage'] = 'servable'
                    data['ready_for_dashboard'] = True
                    
                    print(f"  ✓ {rel_path}: Ready for dashboard serving")
                    
                    if not dry_run:
                        os.makedirs(os.path.dirname(servable_file), exist_ok=True)
                        with open(servable_file, 'w') as f:
                            json.dump(data, f, indent=2)
                    
                    processed_files.append(rel_path)
                    
                except Exception as e:
                    print(f"  ✗ {rel_path}: Error - {e}")
    
    log_pipeline_action('serve', 'transformed_to_servable', processed_files, dry_run)
    return processed_files

def run_full_pipeline(dry_run=False):
    """Run the complete pipeline"""
    print(f"=== RUNNING {'DRY-RUN' if dry_run else 'FULL'} PIPELINE ===")
    print(f"Timestamp: {datetime.utcnow().isoformat()} UTC")
    
    curated_files = curate_data(dry_run)
    transformed_files = transform_data(dry_run)
    servable_files = serve_data_stage(dry_run)
    
    print(f"=== PIPELINE {'DRY-RUN' if dry_run else ''} COMPLETE ===")
    print(f"Curated: {len(curated_files)} files")
    print(f"Transformed: {len(transformed_files)} files")
    print(f"Servable: {len(servable_files)} files")

def main():
    parser = argparse.ArgumentParser(description='Data Pipeline Management')
    parser.add_argument('--stage', choices=['curate', 'transform', 'serve', 'full'], 
                        default='full', help='Pipeline stage to run')
    parser.add_argument('--dry-run', action='store_true', 
                        help='Show what would be done without making changes')
    
    args = parser.parse_args()
    
    if args.stage == 'curate':
        curate_data(args.dry_run)
    elif args.stage == 'transform':
        transform_data(args.dry_run)
    elif args.stage == 'serve':
        serve_data_stage(args.dry_run)
    else:
        run_full_pipeline(args.dry_run)

if __name__ == '__main__':
    main()