import os
import json

def ingest_data(source_path):
    """Ingest data from a source file (raw zone)."""
    if os.path.exists(source_path):
        with open(source_path, 'r') as f:
            return json.load(f)
    return None

def validate_data(data):
    """Validate data format and required fields."""
    if not data or 'metrics' not in data:
        return False, 'Missing metrics key.'
    for metric in data['metrics']:
        if 'name' not in metric or 'value' not in metric:
            return False, f"Metric missing name or value: {metric}"
    return True, 'Valid data.'

def transform_data(data):
    """Transform data for dashboard (e.g., add computed fields, normalize)."""
    # Example: Add a 'quality' field to each metric
    for metric in data.get('metrics', []):
        metric['quality'] = 'high'  # Placeholder logic
    return data

def serve_data():
    """Serve data from the servable zone (production-ready data)."""
    servable_dir = os.path.join('data', 'servable')
    
    # Look for all JSON files in servable zone
    all_metrics = []
    
    if os.path.exists(servable_dir):
        for root, dirs, files in os.walk(servable_dir):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r') as f:
                            data = json.load(f)
                            if 'metrics' in data:
                                all_metrics.extend(data['metrics'])
                    except Exception as e:
                        print(f"Warning: Could not load {file_path}: {e}")
    
    # If no servable data exists, fall back to toy data for demo
    if not all_metrics:
        print("No servable data found, using toy data")
        toy_path = os.path.join('data', 'raw', 'toy_data.json')
        if os.path.exists(toy_path):
            with open(toy_path, 'r') as f:
                toy_data = json.load(f)
                all_metrics = toy_data.get('metrics', [])
    
    return {
        'metrics': all_metrics,
        'source': 'servable_zone',
        'count': len(all_metrics)
    }
