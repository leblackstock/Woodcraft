# consolidate_learning_candidates.py Runbook

## Purpose

Create a review-only queue for new decision-log entries and the latest maintenance-audit evidence. It never turns a candidate into a rule or edits the learning log.

## Commands

    python 60_automation/workspace_maintenance/consolidate_learning_candidates.py --write
    python 60_automation/workspace_maintenance/consolidate_learning_candidates.py --check

## Cadence and Safety

Run after a meaningful maintenance pass or before the weekly review is closed. This script intentionally reads the latest archived maintenance report as an explicitly requested evidence source. Review each candidate against the promotion test in LEARNING_REVIEW.md, then manually add only confirmed lessons to MAINTENANCE_LEARNINGS.md.
