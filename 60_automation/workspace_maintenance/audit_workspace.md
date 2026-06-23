# audit_workspace.py Runbook

## Purpose

Read-only scan of live Markdown for broken relative links, references to currently retired files, UTF-8 decoding artifacts in editable workspace files, and exact repeated long guidance in important workflow files. Immutable raw source packages are outside encoding reporting.

## Inputs and Output

- Default input: live Markdown files in the repository.
- Default exclusions: 90_archive/, deprecated/, .git/, and Python cache paths.
- Console output: classified audit report.
- Optional persistent output: a timestamped report in 90_archive/maintenance_audits/ and an updated CURRENT_MAINTENANCE_STATUS.md pointer.

## Commands

    python 60_automation/workspace_maintenance/audit_workspace.py
    python 60_automation/workspace_maintenance/audit_workspace.py --write-report
    python 60_automation/workspace_maintenance/audit_workspace.py --include-archive

## Cadence and Safety

Run before cleanup and during the Friday review. The script makes no change unless --write-report is provided. A nonzero exit means at least one error-level finding needs review; warnings remain classified rather than automatically repaired.
