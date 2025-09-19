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

## Pipeline Stages

1. **Ingestion**: Loads data from the raw zone (e.g., `data/raw/toy_data.json`).
2. **Validation**: Checks for required fields and correct format.
3. **Transformation**: Adds computed fields or normalizes data for dashboard use.
4. **Serving**: Makes data available via the `/api/data` endpoint.

## How to Contribute Data
- Prepare a JSON file matching the format above.
- Place it in the appropriate data zone (e.g., `data/raw/`).
- Submit a pull request or data request via the dashboard (coming soon).

## Next Steps
- Expand pipeline to support more sources and transformations.
- Document additional fields and data types as needed.
