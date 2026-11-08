# ARCHIVED: pdoom-dashboard v0.1 (draft, pending Pip's review)

**Status:** This repo is frozen and no longer maintained. Tag `v0.1` marks the final state, commit `db6d036` (2025-11-01).

## What this was
This was an early (v0.01–v0.1) prototype of a P(Doom) dashboard. It was a Flask/static build pipeline (`pipeline.py`, `build_system.py`) with hourly-build and daily-data-refresh GitHub Actions.

## Data quality warning
- Every metric in `data_manifest.json` is marked `"placeholder": true`, and the confidence levels were assigned by hand.
- `data/raw/toy_data.json` contains toy data.
- None of the numbers here should be cited as estimates.

## Operational history
- In the GitHub Actions history (last 200 runs), the build and data-refresh workflows have no successful runs. The final scheduled runs (2025-12-31) failed.
- GitHub Pages was never enabled, so the dashboard was never deployed from this repo.

## What's worth keeping
- `STUDIES/00-research/`: notes on p(doom) analysis and compute estimates
- `STUDIES/02-prototypes/archived-variations-2025-11-01/`: UI experiments, including `ai_events_comprehensive.csv` and its documentation
- `DASHBOARD_WEBSITE_INTEGRATION_PLAN.md`

## Named third parties
`STUDIES/assets/cat-gallery/README.md` names the cats' custodians. Pip confirmed on 2026-11-09 that they agreed to be named.
If a custodian later withdraws consent: unarchive the repo (`gh repo unarchive`), remove the name from the README, commit, and re-archive.
The name stays in git history (`2b97609`). Removing it from history needs a history rewrite and force-push, done by Pip in person.

## Successor
The data source was `pdoom-data`. A successor project will connect Pip's mapping of risk onto reality with sourced arguments for and against. Its location is not decided yet. <!-- TODO Pip: link -->
