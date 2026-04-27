# 03 Governance

This file defines how this workspace is managed so strategy stays consistent over time.

## File Precedence (When Conflicts Exist)

1. [00_START_HERE.md](00_START_HERE.md)
2. [01_VISION.md](01_VISION.md)
3. [03_GOVERNANCE.md](03_GOVERNANCE.md)
4. [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md)
5. [05_CHANNEL_STRATEGY.md](05_CHANNEL_STRATEGY.md)
6. Workflow files ([06](06_PRODUCT_DECISION_WORKFLOW.md), [07](07_LISTING_AND_CONTENT_WORKFLOW.md), [08](08_AUTOMATION_ROADMAP.md), [11](11_WEEKLY_OPERATIONS.md))
7. Logs/backlog/archive ([12](12_DECISION_LOG.md), [13](13_BACKLOG.md), [90_archive/](90_archive/))

## Editing Rules

- Keep one clear purpose per file.
- Update existing files before creating duplicates.
- Cross-link related files when adding new policy or workflow content.
- Keep docs practical and concise.
- If a strategy-defining file changes, add an entry to [12_DECISION_LOG.md](12_DECISION_LOG.md).

## Locked Reference Files

- `20_research/whosthevoss_2026_pricing_guide_reference.md` is an official reference file and is locked by default.
- Do not edit that file unless the user gives explicit permission for the specific change.
- When edits are approved, preserve source pricing data, customer-facing dimensions, and official table structure unless the user explicitly authorizes a broader revision.

## Naming Conventions

- Root docs use numeric prefixes (`00_`, `01_`, etc.).
- Use descriptive names; avoid clever/ambiguous file names.
- Markdown-first for planning and operations.
- Templates live in [80_templates/](80_templates/).
- Upcoming or in-progress weekly review drafts live in `15_weekly_review_drafts/` using `weekly_review_draft_YYYY-MM-DD.md`.
- Completed weekly review instance files live in `90_archive/weekly_reviews/` using `weekly_review_YYYY-MM-DD.md`.

## AI Operating Rules

- Optimize for profit and consistency before complexity.
- Assume low budget unless explicitly updated in [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md).
- Do not recommend paid scaling before organic proof.
- Prefer reusable content across channels.
- Clearly tag steps as **manual**, **semi-automated**, or **fully automated**.
- When uncertain, flag uncertainty and list required inputs.
- Do not fabricate numbers, market evidence, or outcomes.

## Dual-Model Customer-Copy Rules

- GPT-5.5 is the workflow orchestrator for internal workflow progression.
- Claude is the only approved writer of final customer-facing prose.
- Non-Claude models may prepare:
  - facts
  - structured fields
  - outlines
  - bullets
  - pricing prep
  - validation notes
  - workflow state
- Non-Claude models may **not** write final publishable customer-facing copy.

### Customer-Facing Prose Includes

- listing titles
- listing descriptions
- Facebook Page captions
- Instagram captions
- CTA lines
- promo blurbs
- ad copy
- customer-facing reply templates

### Required Workflow Behavior

- When the workflow reaches a final customer-copy step, the orchestrator must stop and request a Claude pass.
- The orchestrator must generate the Claude prompt from approved facts only.
- If approved facts are incomplete, the orchestrator must stop with missing-info notes instead of guessed copy.
- After Claude output is pasted back by the human, the orchestrator may integrate it into the correct asset and continue the workflow.

### Placeholder Rule Before Claude

- If final customer prose is still pending Claude, non-Claude outputs must use either:
  - structured bullets or approved facts only
  - `[[CLAUDE_FINAL_COPY_REQUIRED]]`
- Do not present non-Claude prep output as publish-ready customer copy.

### Record-Level Copy Governance

- Listing and content records with customer-facing prose must include these governance fields:
  - `approved_facts_status`
  - `customer_copy_status`
  - `claude_handoff_ref`
  - `claude_output_ref`
  - `publish_ready`
- Allowed `approved_facts_status` values:
  - `Working`
  - `Approved`
- Allowed `customer_copy_status` values:
  - `Prep Only`
  - `Claude Required`
  - `Handoff Prepared`
  - `Claude Output Pasted Back`
  - `Final Integrated`
- Until `customer_copy_status: Final Integrated`, customer-facing fields must contain `[[CLAUDE_FINAL_COPY_REQUIRED]]` or strictly non-publishable structured bullets.
- Draft phrasing, outline language, and non-Claude copy experiments belong in internal prep fields such as `customer_copy_prep_notes`, not in publishable customer-facing fields.
- `claude_handoff_ref` is blank until a valid approved-facts handoff is prepared.
- `claude_output_ref` is blank until Claude output is pasted back by the human.
- `publish_ready: Yes` is allowed only when:
  - `approved_facts_status: Approved`
  - `customer_copy_status: Final Integrated`
  - `claude_output_ref` is filled
  - required non-copy asset fields are complete
- `publish_ready: Yes` does not remove manual approval requirements for pricing, publishing, or scheduling.

### Publish-State Truthfulness Rules

- `publish_status` may not imply readiness beyond the Claude gate or `publish_ready`.
- Assets with an incomplete Claude gate may not use readiness, scheduled, or published statuses.
- Prep-only assets must stay in clearly non-publish states.
- Listing records with `publish_ready: No` may use only `Draft`, `Paused`, or `Archived`.
- Content records with `publish_ready: No` may use only `Draft` or `Archived`.
- `Ready for Manual Publish`, `Ready to Schedule`, `Scheduled`, `Published`, and similar publish-near states are allowed only after the Claude gate is complete and `publish_ready: Yes`.
- `publish_date` is the actual publish date only and stays blank until a manual publish event has happened.

## Change Management Rules

- Major changes must include:
  - what changed
  - why it changed
  - expected impact
  - owner/approver
- Log a decision when a change alters operating behavior, source-of-truth rules, schema/template fields, governance rules, or channel priority/role.
- Do **not** log typo fixes, wording-only clarifications, or template cleanup that does not change fields or operating behavior.
- Log major changes in [12_DECISION_LOG.md](12_DECISION_LOG.md).
- Add follow-up actions to [13_BACKLOG.md](13_BACKLOG.md).

## Handling Uncertainty

When information is missing:

1. Mark assumptions explicitly.
2. Record unknowns as questions/tasks.
3. Avoid irreversible recommendations until key unknowns are resolved.
4. Default to low-risk actions that preserve optionality.
