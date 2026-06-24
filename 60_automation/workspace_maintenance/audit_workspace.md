# audit_workspace.py Runbook

## Purpose

Read-only scan of live Markdown for broken relative links, retirement-lifecycle integrity, references to currently retired files, UTF-8 decoding artifacts in editable workspace files, and exact repeated long guidance in important workflow files. It also traces each changed eligible workflow document through its live linked package. Immutable raw source packages are outside encoding reporting.

## Inputs and Output

- Default input: live Markdown files in the repository, plus the retirement ledger and its managed archived targets.
- Default exclusions: 90_archive/, deprecated/, .git/, and Python cache paths.
- Retirement lifecycle always validates `90_archive/RETIREMENT_LEDGER.md`: every ledger target exists in a managed retired/deprecated folder, its original live path is gone, successor/pointer and reason are present, and every managed retired/deprecated archive Markdown file has one ledger row.
- A live file marked Deprecated, Retired, or Superseded without a completed ledger move is an error. Active references to retired material remain warnings; archive-to-archive trace references are informational history.
- Console output: classified audit report.
- Workflow package: the changed document, governance roots, recursive live relative links, and direct live inbound links. Archive paths are never package members.
- Package checks: broken links, retirement lifecycle, active references to Deprecated/Retired/Superseded files, removed workflow documents needing lifecycle review, and exact non-intentional repeated guidance. The trace does not infer semantic contradictions from free-form prose.
- Optional persistent output: a timestamped report in 90_archive/maintenance_audits/, an updated CURRENT_MAINTENANCE_STATUS.md pointer, and WORKFLOW_TRACE_BASELINE.json with sorted workflow-document SHA-256 fingerprints.

## Commands

    python 60_automation/workspace_maintenance/audit_workspace.py
    python 60_automation/workspace_maintenance/audit_workspace.py --write-report
    python 60_automation/workspace_maintenance/audit_workspace.py --include-archive

## Cadence and Safety

Run before cleanup and during the Friday review. The script makes no change unless --write-report is provided. Read-only runs inspect the existing trace baseline without advancing it; persistent runs advance the baseline after the scan even when warnings or error-level findings need review. A nonzero exit means at least one error-level finding needs review; warnings remain classified rather than automatically repaired.
