# refresh_live_indexes.py Runbook

## Purpose

Generate the detailed live-file map, rule-ownership map, and asset locator. These indexes improve discovery without turning archives into default search scope.

## Inputs and Output

- Input: live repository files, 00_brand/, and competitor-snapshot folders.
- Exclusions: 90_archive/, deprecated/, .git/, and generated index files themselves.
- Output: LIVE_FILE_MAP.md, RULE_OWNERSHIP_MAP.md, and ASSET_LOCATOR.md in this folder.

## Commands

    python 60_automation/workspace_maintenance/refresh_live_indexes.py --check
    python 60_automation/workspace_maintenance/refresh_live_indexes.py --write

## Cadence and Safety

Run with --write after a live-document, asset-routing, or archive-routing change. Run with --check in validation. The script modifies only its three generated index files.
