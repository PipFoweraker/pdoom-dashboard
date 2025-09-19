# Data Pipeline Management Guide

## Overview
The pdoom-dashboard uses a multi-stage data pipeline based on data lake principles:
- **Raw Zone**: Incoming data from GitHub Actions and manual uploads
- **Curated Zone**: Validated and cleaned data
- **Transformed Zone**: Enriched and aggregated data
- **Servable Zone**: Production-ready data consumed by dashboard

## Quick Start Commands
```bash
# Dry run the full pipeline (see what would happen)
python run_pipeline.py --dry-run

# Run the full pipeline (raw -> curated -> transformed -> servable)
python run_pipeline.py

# Run specific stages
python run_pipeline.py --stage curate
python run_pipeline.py --stage transform  
python run_pipeline.py --stage serve
```

## Detailed Pipeline Stages

### Stage 1: Curation (Raw -> Curated)
**Purpose**: Validate, clean, and standardize incoming data

**What it does**:
1. Scans `data/raw/` for JSON files
2. Validates each file has required `metrics` field
3. Validates each metric has `name` and `value` fields
4. Adds quality metadata:
   - `curated_at`: Timestamp of processing
   - `quality_check`: Status of validation
5. Filters out invalid metrics
6. Preserves folder structure in `data/curated/`

**Example transformation**:
```json
// Before (raw)
{"metrics": [{"name": "safety_researchers", "value": 847}]}

// After (curated)  
{
  "metrics": [{
    "name": "safety_researchers", 
    "value": 847,
    "curated_at": "2025-09-19T10:30:00Z",
    "quality_check": "passed"
  }],
  "curated_at": "2025-09-19T10:30:00Z",
  "stage": "curated"
}
```

**To extend**: Modify `curate_data()` function in `run_pipeline.py`
- Add new validation rules
- Implement data cleaning logic
- Add metadata enrichment

### Stage 2: Transformation (Curated -> Transformed)
**Purpose**: Enrich, aggregate, and compute derived metrics

**What it does**:
1. Loads validated data from `data/curated/`
2. Adds computed fields based on business logic
3. Categorizes metrics (e.g., magnitude: high/medium/low)
4. Applies transformations and enrichments
5. Adds transformation metadata
6. Outputs to `data/transformed/`

**Example transformation**:
```json
// Before (curated)
{"name": "safety_researchers", "value": 847, "quality_check": "passed"}

// After (transformed)
{
  "name": "safety_researchers", 
  "value": 847,
  "quality_check": "passed",
  "transformed_at": "2025-09-19T10:35:00Z",
  "magnitude": "medium"  // Added computation
}
```

**To extend**: Modify `transform_data()` function in `run_pipeline.py`
- Add aggregation logic (sum, average, trends)
- Implement metric categorization
- Add external data enrichment
- Create derived metrics

### Stage 3: Serving (Transformed -> Servable)
**Purpose**: Final preparation for dashboard consumption

**What it does**:
1. Loads enriched data from `data/transformed/`
2. Adds serving metadata
3. Marks data as production-ready
4. Outputs to `data/servable/`
5. Dashboard exclusively reads from this zone

**Example transformation**:
```json
// Before (transformed)
{"name": "safety_researchers", "value": 847, "magnitude": "medium"}

// After (servable)
{
  "name": "safety_researchers", 
  "value": 847,
  "magnitude": "medium",
  "served_at": "2025-09-19T10:40:00Z",
  "stage": "servable",
  "ready_for_dashboard": true
}
```

**To extend**: Modify `serve_data_stage()` function in `run_pipeline.py`
- Add final data formatting
- Implement caching optimizations  
- Add API-specific metadata

## Usage Examples

```bash
# Test what the pipeline would do
python run_pipeline.py --dry-run

# Process only new raw data through curation
python run_pipeline.py --stage curate

# Run full pipeline after adding new raw data
python run_pipeline.py

# Check pipeline logs
cat data/metadata/pipeline_log.json
```

## Data Flow
```
Raw Zone -> Curate -> Curated Zone -> Transform -> Transformed Zone -> Serve -> Servable Zone
    ↓           ↓            ↓             ↓              ↓            ↓         ↓
GitHub     Validate     Clean Data    Enrich Data   Add Metadata   Dashboard  Users
Actions      Data                                                   Consumes
```

## Pipeline Logging and Monitoring

### Log Storage
- **Location**: `data/metadata/pipeline_log.json`
- **Retention**: Last 100 pipeline runs
- **Format**: JSON with detailed metadata

### Log Structure
```json
{
  "pipeline_runs": [{
    "timestamp": "2025-09-19T10:30:00Z",
    "stage": "curate",
    "action": "raw_to_curated", 
    "files_processed": 3,
    "files": ["toy_data.json", "safety_metrics/data.json"],
    "dry_run": false
  }]
}
```

### Monitoring Commands
```bash
# View recent pipeline activity
cat data/metadata/pipeline_log.json | jq '.pipeline_runs[-5:]'

# Count files in each zone
find data/raw -name "*.json" | wc -l
find data/curated -name "*.json" | wc -l  
find data/transformed -name "*.json" | wc -l
find data/servable -name "*.json" | wc -l

# Check what dashboard is serving
curl localhost:5000/api/data
```

## Extending the Pipeline

### Adding New Validation Rules
Edit `curate_data()` in `run_pipeline.py`:
```python
# Add after existing validation
if metric.get('value') < 0:
    print(f"  ✗ {rel_path}: Negative value not allowed")
    continue
```

### Adding New Transformations  
Edit `transform_data()` in `run_pipeline.py`:
```python
# Add new computed field
if 'trend' not in metric:
    metric['trend'] = calculate_trend(metric['value'])
```

### Adding New Data Sources
1. Update GitHub Actions sync config in `config/data_sync.yaml`
2. Add new include paths or file patterns
3. Pipeline automatically processes new sources

### Troubleshooting

**Common Issues**:
- **No servable data**: Run `python run_pipeline.py` to process raw data
- **Validation errors**: Check `pipeline_log.json` for specific file issues  
- **Dashboard shows old data**: Ensure pipeline completed successfully
- **Missing files**: Verify GitHub Actions sync is working

**Debug Steps**:
1. Run `python run_pipeline.py --dry-run` to see what would be processed
2. Check `data/metadata/pipeline_log.json` for errors
3. Manually inspect files in each zone for format issues
4. Verify dashboard is reading from servable zone