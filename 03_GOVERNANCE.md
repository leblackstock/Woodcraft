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

## Image Prompt Text Policy

- Do not assume image prompts should avoid text.
- When an image is supposed to include readable words, labels, signage, branding, price text, catalog marks, packaging text, captions, or other literal text, include that text explicitly in the image prompt.
- ChatGPT Image 2 is accepted in this workspace as a capable option for text-bearing image generation. Do not remove requested text based on generic older image-model guidance.
- Remove or avoid in-image text only when the user requests a text-free image, the text is not approved for the intended customer-facing use, or the selected image tool is documented as unable to render it.

## Standalone External Prompt Policy

- Any prompt intended to be copied, pasted, uploaded, or sent to an AI or tool outside this repository must be standalone.
- Use repository source-of-truth files while preparing the prompt, then inline all relevant facts, brand guidance, voice rules, palette values, typography direction, visual direction, constraints, required text, reference instructions, output format, quality criteria, and missing-information behavior into the delivered prompt. For image and graphic prompts, choose the background color or photo/overlay background treatment first, then list the remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, or inset fields.
- Do not require the target system to open repository paths, remember prior chat context, inspect another prompt, infer undocumented shorthand, or read required context that exists only in surrounding notes.
- Include only relevant rules; standalone prompts should be complete and high-signal, not indiscriminate dumps of repository files.
- If exact results require attachments or reference images, state that requirement explicitly. Do not imply text-only prompting can guarantee fidelity that depends on an attachment.
- If an image prompt requires an attached image, the copied prompt must begin with `Please see attached "[plain-language item being attached]"` before any other prompt instruction.
- Claude final-copy prompts must inline the negative style rules: no em dashes or en dashes in final output, regular hyphens are okay when needed, and no AI-isms or common AI tells.
- Every workflow or automation that creates external prompts must apply [80_templates/standalone_external_prompt_checklist.md](80_templates/standalone_external_prompt_checklist.md) before delivery.

## Brand Source Of Truth Policy

- `00_brand/` is the source of truth for reusable Drakkar Designs identity guidance and approved brand assets.
- Reusable color palettes, voice guides, visual-style guides, logo guidance, typography guidance, reusable brand marks, and approved brand-reference media belong in `00_brand/`.
- `00_brand/VOICE.md` owns one shared customer-facing voice with Catalog, Brand Post, Marketplace, and Customer Reply modes. Do not create competing channel voice guides; modes adjust emphasis only and never override core voice or approved-fact rules.
- Any workflow that creates or references brand-specific text, graphics, images, ads, copy, HTML, templates, prompt packs, or generated visuals must check the relevant files in `00_brand/` before proceeding.
- Operational records stay in their role-based folders: products in `30_products/`, listings and listing prompt packs in `40_listings/`, content in `50_content/`, and templates in `80_templates/`. These files point to `00_brand/` instead of owning competing brand rules.
- Catalog export folders may be used as provenance, but they are not the active brand source of truth.

## Dual-Model Customer-Copy Rules

- GPT-5.5 is the workflow orchestrator for internal workflow progression.
- Claude is the only approved writer of final customer-facing prose.
- Image graphic text is a governed exception when an active review-by-exception image workflow assigns it to GPT/Codex. It does not require Claude approval, but it must use approved facts and the applicable voice mode.
- Non-Claude models may prepare:
  - facts
  - structured fields
  - outlines
  - bullets
  - pricing prep
  - validation notes
  - workflow state
- Non-Claude models may **not** write final publishable customer-facing copy.
- Non-Claude models may create image graphic text only when an active image workflow explicitly grants that responsibility.

### Customer-Facing Prose Includes

- listing titles
- listing descriptions
- Facebook Page post copy
- Instagram captions
- CTA lines outside governed image graphic text
- promo blurbs
- ad copy
- customer-facing reply templates

Image graphic text governed by an active review-by-exception image workflow is excluded from this prose list.

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
  - `Historical Operator Evidence` (audit-only exception; never for a new or revised asset)
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
- `Historical Operator Evidence` is permitted only for an already-published asset whose exact visible copy and operator evidence were captured after the fact, but whose Claude output was never recorded. It requires `historical_publish_evidence_ref` and `historical_gate_exception_reason`, may retain its historical `Published` state, and must not be reused as a publish path.
- A historical-exception asset may not be refreshed, scheduled again, or used as source copy. Any customer-facing revision restarts the normal Claude gate and removes the exception.

### Publish-State Truthfulness Rules

- `publish_status` may not imply readiness beyond the Claude gate or `publish_ready`.
- Assets with an incomplete Claude gate may not use readiness, scheduled, or published statuses, except an immutable record using the documented `Historical Operator Evidence` audit exception.
- Prep-only assets must stay in clearly non-publish states.
- Listing records with `publish_ready: No` may use only `Draft`, `Paused`, or `Archived`.
- Content records with `publish_ready: No` may use only `Draft` or `Archived`.
- `Ready for Manual Publish`, `Ready to Schedule`, `Scheduled`, `Published`, and similar publish-near states are allowed only after the Claude gate is complete and `publish_ready: Yes`, except an immutable historical-evidence record covered by the preceding exception.
- `publish_date` is the actual publish date only and stays blank until a manual publish event has happened.

## Document Lifecycle, Search, and Rule Ownership

- Live workflow files are the default discovery scope. `90_archive/` and `deprecated/` paths are historical-only and must be excluded from routine repository searches; use `rg --no-ignore` only when historical material is explicitly needed.
- Archive a document only when it is explicitly Deprecated, Superseded, or Retired and an active successor or traceability pointer is known. Preserve history and record the move in `90_archive/RETIREMENT_LEDGER.md`; do not delete it.
- One live file owns each active rule, fact, or workflow. Other live files use short pointers or summaries instead of restating it.
- Required complete copies remain valid in standalone external prompts, agent-specific instruction files, schemas, templates, and historical evidence. Do not reduce those copies to repository-only pointers.
- The maintenance toolkit at `60_automation/workspace_maintenance/` may update generated indexes, archive-ledger pointers, clear relative links, and obvious encoding errors in editable canonical files. Escalate policy conflicts, factual disagreements, customer-facing copy, published records, raw source evidence, and uncertain archive decisions.

## Daily Session Briefing

- The required user confirmation phrase is "Brief me". A due notice asks for that reply; agents treat it as confirmation to create or replay the briefing.
- A daily session briefing is an operational snapshot, not a workflow action. At first substantive response, agents check its America/New_York date. If due, they prompt once while continuing the user’s request; after explicit confirmation, they create/replay the briefing and paste its full summary into chat.
- A briefing may summarize todos, open projects, campaigns, posting schedules, and maintenance freshness, but may not publish, schedule, create customer copy, reprioritize work, or create a policy/learning entry.

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
