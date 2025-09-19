# Development and Extension Guide

## Architecture Overview

The pdoom-dashboard follows data lake and DevOps best practices:

```
GitHub Actions (Daily) -> Raw Zone -> Pipeline -> Servable Zone -> Dashboard -> Users
                             ↓           ↓            ↓            ↓
                         Validation  Transform    Metadata     API Serving
```

## Key Components

### 1. Backend (`app.py`)
- Flask web server
- Serves API endpoint `/api/data`  
- Reads from servable zone via `pipeline.py`
- Easily extensible for new endpoints

### 2. Data Pipeline (`pipeline.py` + `run_pipeline.py`)
- **`pipeline.py`**: Core functions for data loading
- **`run_pipeline.py`**: Management script with CLI interface
- Modular design for easy extension

### 3. GitHub Actions (`.github/workflows/daily-data-refresh.yml`)
- Automated daily sync from pdoom-data repository
- Configurable via `config/data_sync.yaml`
- Comprehensive logging and error handling

### 4. Configuration System
- **`config/data_zones.yaml`**: Zone paths and descriptions
- **`config/data_sync.yaml`**: GitHub Actions sync settings
- **`config/dashboard_config.yaml`**: Dashboard-specific settings

## Development Workflow

### Setting Up Development Environment
```bash
# Clone repository
git clone https://github.com/PipFoweraker/pdoom-dashboard.git
cd pdoom-dashboard

# Install dependencies
pip install flask pyyaml

# Run backend locally
python app.py

# Test pipeline
python run_pipeline.py --dry-run
```

### Adding New Features

#### New API Endpoint
1. Add route to `app.py`:
```python
@app.route('/api/new-endpoint')
def new_endpoint():
    # Implementation here
    return jsonify(data)
```

#### New Pipeline Stage
1. Add function to `run_pipeline.py`:
```python
def new_stage(dry_run=False):
    # Process data
    # Log actions
    # Return processed files
```

2. Add to CLI arguments:
```python
parser.add_argument('--stage', choices=['curate', 'transform', 'serve', 'new-stage'])
```

#### New Data Source
1. Update `config/data_sync.yaml`:
```yaml
include_paths:
  - "existing_path/"
  - "new_data_source/"
```

2. GitHub Actions will automatically sync new source

### Testing and Quality Assurance

#### Testing Pipeline Changes
```bash
# Always test with dry-run first
python run_pipeline.py --dry-run

# Test specific stages
python run_pipeline.py --stage curate --dry-run

# Check logs for issues
cat data/metadata/pipeline_log.json
```

#### Testing GitHub Actions
- Use `workflow_dispatch` trigger for manual testing
- Check Actions tab for detailed logs
- Verify sync configuration in `config/data_sync.yaml`

### Code Organization

```
pdoom-dashboard/
├── app.py                    # Flask backend
├── pipeline.py              # Core pipeline functions  
├── run_pipeline.py          # Pipeline management CLI
├── passenger_wsgi.py        # DreamHost deployment
├── config/                  # Configuration files
├── data/                    # Data lake zones
│   ├── raw/                 # Incoming data
│   ├── curated/            # Validated data
│   ├── transformed/        # Enriched data
│   ├── servable/           # Dashboard-ready data
│   └── metadata/           # Logs and metadata
├── docs/                   # Documentation
├── templates/              # HTML templates
└── .github/workflows/      # GitHub Actions
```

## Best Practices for Extensions

### Data Processing
- Always validate input data format
- Log all processing steps with timestamps
- Handle errors gracefully with informative messages
- Use dry-run mode for testing changes

### Configuration Management  
- Use YAML files for configuration
- Provide sensible defaults
- Document all configuration options
- Validate configuration on load

### API Development
- Follow REST conventions
- Return consistent JSON format
- Include error handling and status codes
- Add logging for debugging

### Documentation
- Update relevant docs when adding features
- Include code examples
- Explain the "why" not just the "how"
- Keep README and setup guides current

## Future Enhancement Ideas

### Short Term
- Real-time data validation API
- Dashboard suggestion form implementation
- Additional data source connectors
- Enhanced error reporting

### Medium Term  
- Data quality scoring system
- Automated anomaly detection
- Interactive dashboard components
- REST API for external integrations

### Long Term
- Machine learning pipeline integration
- Multi-tenant support
- Advanced analytics and forecasting
- Real-time streaming data support

## Getting Help

- Check existing documentation in `docs/`
- Review GitHub Issues for known problems
- Look at `pipeline_log.json` for processing errors
- Use dry-run mode to test changes safely