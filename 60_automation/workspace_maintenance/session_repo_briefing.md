# session_repo_briefing.py Runbook

## Purpose

Inspect or create the once-daily Woodcraft session briefing. It summarizes saved workspace state for chat delivery and never performs operational work.

## Commands

    python 60_automation/workspace_maintenance/session_repo_briefing.py --status
    python 60_automation/workspace_maintenance/session_repo_briefing.py --write

## Behavior

- Dates use America/New_York.
- --status is read-only and reports whether today has a saved briefing.
- --write creates one report in 90_archive/session_briefings/ and SESSION_BRIEFING_STATUS.md, then prints the complete Markdown briefing for the AI to paste into chat.
- A second --write on the same date replays the existing report without creating another one.

## Chat Delivery and Safety

When today is due, the notice must ask the user to reply "Brief me". Treat that phrase as the explicit confirmation to run --write.

When today is due, the AI prompts once in the current chat while continuing the user’s original request. Run --write only after the user confirms. Always paste the resulting briefing into chat; saved files are not a substitute for chat delivery.

The briefing reads only the backlog, rollout, product/listing/content status fields, ad-campaign folder, and maintenance status. It does not publish, schedule, reprioritize, create customer copy, or run maintenance.
