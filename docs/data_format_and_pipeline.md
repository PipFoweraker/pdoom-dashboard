# Data Format and Pipeline Overview

## Expected Data Format

Data files should be JSON with the following structure:

```json
{
  "metrics": [
    {"name": "safety_researchers", "value": 847},
    {"name": "governance_researchers", "value": 312},
    {"name": "capabilities_researchers", "value": 15247},
    {"name": "funding_overview", "value": 1000000},
    {"name": "aisi_status", "value": 3},
    {"name": "governance_scores", "value": 75}
  ],
  "source": "toy"
}
```

- Each metric must have a `name` and a `value`.
- Additional fields (e.g., `quality`, `trend`) can be added as needed.
- Supported file types: JSON, CSV, YAML
- Files can be organized in folders (structure is preserved)

## Pipeline Stages

1. **Ingestion**: Loads data from the raw zone (e.g., `data/raw/toy_data.json`).
2. **Validation**: Checks for required fields and correct format.
3. **Transformation**: Adds computed fields or normalizes data for dashboard use.
4. **Serving**: Makes data available via the `/api/data` endpoint.

## Automated Data Sync

The dashboard automatically pulls data from the `pdoom-data` repository daily at 6:00 AM UTC.

### Sync Configuration

Data sync behavior is controlled by `config/data_sync.yaml`:

```yaml
sync_mode: "selective"  # "all" or "selective"
include_paths:
  - "safety_metrics/"
  - "governance_data/"
exclude_patterns:
  - "*.tmp"
  - "*_draft.json"
allowed_file_types:
  - ".json"
  - ".csv"
  - ".yaml"
max_file_size: 10  # MB
```

### Sync Modes
- **"all"**: Pulls all supported files from pdoom-data
- **"selective"**: Only pulls files from specified `include_paths`

### File Filtering
- Files matching `exclude_patterns` are skipped
- Only `allowed_file_types` are processed
- Files larger than `max_file_size` are rejected
- Folder structure is preserved in the raw data zone

## How to Contribute Data
1. Add your data files to the `pdoom-data` repository
2. Ensure files match the expected format above
3. Place files in appropriate folders (e.g., `safety_metrics/`, `governance_data/`)
4. Submit a pull request to `pdoom-data`
5. Data will be automatically synced to the dashboard within 24 hours

## Manual Data Addition
- Place files directly in `data/raw/` for immediate use
- Follow the same folder structure as automated sync
- Commit changes to trigger pipeline processing

## Next Steps
- Expand pipeline to support more sources and transformations
- Add data validation and quality checks
- Implement real-time sync triggers
