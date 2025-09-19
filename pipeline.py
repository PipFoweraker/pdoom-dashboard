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
    """Full pipeline: ingest, validate, transform, and return data."""
    source_path = os.path.join('data', 'raw', 'toy_data.json')
    data = ingest_data(source_path)
    valid, msg = validate_data(data)
    if not valid:
        return {'error': msg}
    data = transform_data(data)
    return data
