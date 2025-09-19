# GitHub Actions and Automation

## Daily Data Refresh Workflow

The dashboard uses GitHub Actions to automatically sync data from the `pdoom-data` repository.

### Schedule
- **Automatic**: Every day at 6:00 AM UTC
- **Manual**: Can be triggered via GitHub Actions tab

### What It Does
1. **Clones pdoom-data**: Downloads latest data from the data repository
2. **Applies Filters**: Uses `config/data_sync.yaml` to determine what to sync
3. **Processes Files**: Copies matching files to `data/raw/` preserving folder structure
4. **Logs Activity**: Creates detailed logs in `data/refresh_log.json`
5. **Commits Changes**: Automatically commits new data and pushes to repository

### Configuration
Edit `config/data_sync.yaml` to control sync behavior:

```yaml
# Sync all files or be selective
sync_mode: "selective"

# Only sync these folders (when selective)
include_paths:
  - "safety_metrics/"
  - "governance_data/"
  - "funding_data/"

# Skip files matching these patterns
exclude_patterns:
  - "*.tmp"
  - "*.bak" 
  - "*_draft.json"
  - "test_*"

# Allowed file types
allowed_file_types:
  - ".json"
  - ".csv"
  - ".yaml"

# Maximum file size in MB
max_file_size: 10
```

### Monitoring
- View workflow runs in the GitHub Actions tab
- Check `data/refresh_log.json` for detailed sync history
- Each log entry includes:
  - Timestamp
  - Files processed and skipped
  - Reasons for skipping files
  - Configuration used

### Troubleshooting
- Workflow failures appear in GitHub Actions tab
- Check logs for specific error messages
- Ensure pdoom-data repository is accessible
- Verify configuration file syntax

## Future Enhancements
- Real-time sync triggers via webhooks
- Data validation and quality checks
- Multiple data source support
- Notification system for sync status