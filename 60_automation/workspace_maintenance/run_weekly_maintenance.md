# run_weekly_maintenance.ps1 Runbook

## Purpose

Perform the lightweight weekly maintenance pass used during Friday review.

## What It Runs

1. audit_workspace.py with --write-report.
2. refresh_live_indexes.py with --write.
3. consolidate_learning_candidates.py with --write.
4. git diff --check.

## Command

    ./60_automation/workspace_maintenance/run_weekly_maintenance.ps1

## Safety and Failure Handling

The runner does not publish, message customers, change prices, rebuild the research database, or stage/commit files. It writes only the dated audit report, current-status pointer, generated indexes, and review-only learning queue. It exits nonzero after completing the safe checks when the audit found an error-level issue.
