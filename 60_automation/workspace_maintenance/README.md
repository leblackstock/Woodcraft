# Workspace Maintenance Toolkit

Use this toolkit to keep the Woodcraft workspace navigable without changing business facts, customer copy, publishing state, or source evidence by accident.

## Default Search Boundary

The root .ignore excludes 90_archive/ and any deprecated/ directory from normal rg searches. Search historical material only when the task calls for it:

    rg --no-ignore "search phrase" 90_archive

## Commands

| Tool | Use it when | Command | Safe side effects |
|---|---|---|---|
| audit_workspace.py | Before a cleanup or during weekly review | python 60_automation/workspace_maintenance/audit_workspace.py | None unless --write-report is supplied; persistent runs also refresh the workflow package-trace baseline |
| refresh_live_indexes.py | After live docs, assets, or archive routing changes | python 60_automation/workspace_maintenance/refresh_live_indexes.py --write | Rewrites generated indexes only |
| consolidate_learning_candidates.py | After meaningful maintenance or before closing weekly review | python 60_automation/workspace_maintenance/consolidate_learning_candidates.py --write | Rewrites the review-only learning queue |
| session_repo_briefing.py | When a new chat needs to check or create today’s repo briefing | python 60_automation/workspace_maintenance/session_repo_briefing.py --status | Reads status only; --write saves or replays the daily briefing |
| run_weekly_maintenance.ps1 | Friday review or a deliberate light maintenance pass | ./60_automation/workspace_maintenance/run_weekly_maintenance.ps1 | Writes a dated report, generated indexes, and the review-only learning queue |
| research_database/build_research_db.py | After transcript, product-record, or cross-reference source changes | python 60_automation/research_database/build_research_db.py | Rebuilds the tracked local SQLite research database |
| research_database/server.py | When browsing the local research database | python 60_automation/research_database/server.py | Starts a local-only web server |

Read the adjacent runbooks before using a script for the first time. The research database has its own README in 60_automation/research_database/.

For a due chat briefing, the user confirmation phrase is "Brief me"; it authorizes the agent to run session_repo_briefing.py --write and paste the result into chat.

## Maintenance Boundary

- The audit and indexes exclude archives by default and never delete files.
- The audit traces each changed live workflow document against the prior persistent-audit baseline. A package includes governance roots, recursive live relative links, and direct live inbound links; archive material remains outside package membership.
- Package findings are evidence-based only: broken links, active references to Deprecated/Retired/Superseded files, removed workflow documents needing lifecycle review, and non-intentional exact repeated guidance. Free-form prose remains human-review context, not an automated contradiction finding.
- A mechanically safe repair may update generated indexes, archive ledgers, relative links, or obvious encoding errors in editable canonical files.
- Escalate business-rule conflicts, unclear source ownership, customer-facing copy, published-record changes, raw source evidence, and uncertain archive decisions.
- Record a confirmed recurring lesson in MAINTENANCE_LEARNINGS.md; record an actual policy decision in 12_DECISION_LOG.md.

## Generated Files

- LIVE_FILE_MAP.md — detailed live-file locator.
- RULE_OWNERSHIP_MAP.md — canonical owner for important rules and intentional-copy boundaries.
- ASSET_LOCATOR.md — reusable brand, external created-reference, and research asset routing.
- CURRENT_MAINTENANCE_STATUS.md — latest audit summary and report pointer.
- LEARNING_REVIEW.md — generated candidate queue; human review decides whether anything becomes a durable learning.
- SESSION_BRIEFING_STATUS.md — today’s America/New_York daily-briefing state and report pointer.
- WORKFLOW_TRACE_BASELINE.json — generated SHA-256 snapshot used to identify workflow-document changes since the prior persistent audit.
