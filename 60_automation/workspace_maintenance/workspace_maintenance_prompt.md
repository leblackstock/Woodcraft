# Reusable Workspace Maintenance Prompt

Use this prompt for a deliberate Woodcraft maintenance session.

    You are maintaining the Woodcraft workspace. Your job is to reduce search time and prevent workflow drift while preserving truthful records and source evidence.

    Start by reading 00_START_HERE.md, 03_GOVERNANCE.md, 04_BUSINESS_RULES.md, 02_INDEX.md, 12_DECISION_LOG.md, and 60_automation/workspace_maintenance/CURRENT_MAINTENANCE_STATUS.md. Check git status before changing anything.

    Search live work only by default. The repository .ignore excludes 90_archive/ and deprecated/ paths. Search those paths only when the task explicitly requires historical material, using rg --no-ignore.

    Run the read-only maintenance audit. Classify every significant finding as one of:
    - Canonical owner: the one file that owns an active rule, fact, or workflow.
    - Intentional standalone copy: required complete context in an external prompt, schema, or agent-specific instruction file.
    - Short pointer or summary: brief navigation text that links to its canonical owner.
    - Stale or conflicting duplicate: repeated active content that could mislead work or lengthen discovery.
    - Needs user decision: unclear ownership, factual disagreement, business-policy conflict, published record, raw source evidence, or uncertain archive choice.

    For safe mechanical work only, consolidate accidental duplicates into one canonical owner and short pointers; repair relative links; regenerate indexes; correct mojibake only in editable canonical files; and archive files explicitly marked Deprecated, Superseded, or Retired when an active replacement is known. Preserve history with git mv and update the archive ledger. Do not delete files.

    Never remove required context from standalone external prompts. Never replace the separate agent instruction files with pointers that their tools cannot read. Do not change final customer-facing prose, publish status, prices, business rules, source evidence, or a locked reference without explicit approval.

    Treat daily session briefings as operational snapshots only. They may summarize current facts in chat and save a dated report, but they do not create tasks, lessons, policy changes, customer copy, schedules, or publishing actions.
    When a due briefing needs confirmation, ask the user to reply "Brief me"; treat that phrase as confirmation to run the briefing.

    Finish by running the checks, reviewing git diff and git status, updating CURRENT_MAINTENANCE_STATUS.md through the audit, and drafting a compact maintenance-learning entry only for a verified recurring lesson. Report completed mechanical repairs, unresolved decisions, commands run, and any follow-up.
