# 00 Start Here

This workspace is a repo-backed operating system for running a low-budget, AI-assisted woodcraft marketing and sales workflow.

Primary goal: help Lauren make better decisions faster, with less stress and less wasted effort.

## Dual-Model Operating Note

- This workspace uses a dual-model operating pattern.
- GPT-5.5 handles workflow orchestration and upstream prep.
- Claude writes final customer-facing prose, and customer-facing assets must pass the Claude gate before publish approval.
- Image graphic text may be created by GPT/Codex without Claude approval when an active review-by-exception image workflow assigns that responsibility.

## Brand Asset Source

- `00_brand/` is the source of truth for Drakkar Designs identity guidance and approved assets, including voice, color palette, visual style, logos, approved product photos, and provenance.
- Workflows that create brand-specific text, graphics, ads, images, HTML, templates, prompt packs, or generated visuals must reference `00_brand/`.
- Reusable brand-specific guidance belongs in `00_brand/`; operational records stay in their workflow folders and point back to it.

## External Prompt Rule

- Any prompt intended for an AI or tool outside this repository must be standalone and pass `80_templates/standalone_external_prompt_checklist.md`.
- Use repository files during preparation, then inline the relevant facts, brand guidance, constraints, required text, reference instructions, output format, and quality criteria into the delivered prompt.
- Never expect an external target to open repository paths or know prior repo context.

## Workspace Maintenance

- Use `60_automation/workspace_maintenance/` for safe repository maintenance, generated live indexes, and the reusable maintenance prompt.
- Default searches intentionally exclude `90_archive/` and `deprecated/` paths. Search historical files only when the task specifically requires them, using `rg --no-ignore`.
- Consolidate repeated active guidance into its canonical owner and short pointers. Keep intentional full copies only where a separate agent tool, schema, or standalone external prompt needs the information locally.

## Read in This Exact Order

1. [01_VISION.md](01_VISION.md)
2. [03_GOVERNANCE.md](03_GOVERNANCE.md)
3. [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md)
4. [05_CHANNEL_STRATEGY.md](05_CHANNEL_STRATEGY.md)
5. [06_PRODUCT_DECISION_WORKFLOW.md](06_PRODUCT_DECISION_WORKFLOW.md)
6. [07_LISTING_AND_CONTENT_WORKFLOW.md](07_LISTING_AND_CONTENT_WORKFLOW.md)
7. [11_WEEKLY_OPERATIONS.md](11_WEEKLY_OPERATIONS.md)
8. [13_BACKLOG.md](13_BACKLOG.md)
9. Use [02_INDEX.md](02_INDEX.md) for everything else.

## What This Workspace Is For

- Choosing what to build/list based on demand and margin.
- Creating repeatable listing and content workflows.
- Keeping Facebook Marketplace as the main sales engine.
- Using Facebook Page and Instagram for trust/content support.
- Running small, controlled experiments instead of random activity.
- Building clean records so automation becomes possible later.

## What Not To Do Yet

- Do **not** build new external scripts or platform integrations in this phase.
- The existing local research database in `60_automation/research_database/` is an approved internal, rebuildable research tool. It may be maintained, but it must not publish, message customers, change prices, or connect to external marketing platforms.
- Do **not** assume big ad budgets.
- Do **not** treat every channel as equally important.
- Do **not** invent metrics or fake certainty.
- Do **not** change strategy files without logging it in [12_DECISION_LOG.md](12_DECISION_LOG.md).

## Session Startup Rule (Human or AI)

Before creating new plans or tasks:

1. Confirm current priorities in [01_VISION.md](01_VISION.md).
2. Confirm hard constraints in [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md).
3. Confirm channel purpose in [05_CHANNEL_STRATEGY.md](05_CHANNEL_STRATEGY.md).
4. Pull next actionable tasks from [13_BACKLOG.md](13_BACKLOG.md).
5. On the first substantive AI response in a chat, run session_repo_briefing.py --status from the maintenance toolkit.
6. If today’s America/New_York briefing is due, say once that it is due while continuing the user’s actual request. Run --write only after the user confirms, then paste the full briefing into chat in addition to the requested work.
7. The due notice must ask the user to reply "Brief me". Treat that phrase as confirmation to run --write.
