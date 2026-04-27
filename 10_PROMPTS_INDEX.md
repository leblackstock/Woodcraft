# 10 Prompts Index

Purpose: prevent prompt sprawl and keep reusable prompt sets organized.

## Dual-Model Prompt Roles

### GPT-5.5 Workflow Orchestration Prompts

Use GPT prompts for:

- workflow progression
- validation against approved facts
- queue movement
- missing-info detection
- structured prep for assets
- Claude handoff generation

### Claude Final Customer-Copy Prompts

Use Claude prompts for:

- final customer-facing listing prose
- final Facebook Page captions
- final Instagram captions
- final CTA lines and promo blurbs
- final customer-facing reply templates

Claude prompts are for final publishable customer-facing prose only.

### GPT-to-Claude Handoff Prompts

- GPT-5.5 must generate Claude handoff prompts from approved facts only.
- If facts are incomplete, stop upstream and resolve missing info before creating the handoff.
- Record the resulting handoff in `claude_handoff_ref` only after `approved_facts_status: Approved`.
- The human pastes Claude output back into the workflow for integration.
- Record pasted-back output in `claude_output_ref` before marking the asset `publish_ready: Yes`.

## Current Reusable Prompt Templates

These shared prompt templates live in [80_templates/](80_templates/):

- `80_templates/gpt_to_claude_handoff_prompt_template.md`
- `80_templates/claude_final_marketplace_listing_prompt.md`
- `80_templates/claude_final_social_caption_prompt.md`
- `80_templates/claude_final_customer_reply_prompt.md`

## Prompt Categories to Build Next

Each future prompt family must be explicitly scoped to either GPT-5.5 orchestration/prep or Claude final customer-facing prose.

1. **Market Research Prompts**
   - Owner: GPT-5.5 orchestration/prep
   - Competitor scan
   - Local pricing snapshot
   - Seasonal demand hypotheses
2. **Product Decision Prompts**
   - Owner: GPT-5.5 orchestration/prep
   - Candidate scoring
   - Margin/risk sanity checks
   - Build-vs-list priority ranking
3. **Listing Prompts**
   - GPT-5.5 orchestration/prep: listing field completeness checks and approved-fact packaging
   - Claude final customer-facing prose: title variants
   - Claude final customer-facing prose: description drafts
   - Claude final customer-facing prose: FAQ + objection handling copy
4. **Image Planning Prompts**
   - Owner: GPT-5.5 orchestration/prep
   - Listing shot plan and required angles
   - Social content image concept prompts
   - Ad creative image prompt drafts for later testing
5. **Content Prompts**
   - GPT-5.5 orchestration/prep: short-form concept extraction from listings
   - Claude final customer-facing prose: caption variations by platform
   - Claude final customer-facing prose: CTA variants
   - Claude final customer-facing prose: reply-template prompts
6. **Ad Test Prompts**
   - Owner: GPT-5.5 orchestration/prep
   - Tiny-budget test planning
   - Pass/fail analysis
   - Learnings-to-next-test conversion
7. **Weekly Ops Prompts**
   - Owner: GPT-5.5 orchestration/prep
   - Weekly planning
   - Low-energy fallback planning
   - Weekly review synthesis

## Where Prompts Should Live

- Store reusable shared prompt templates in `80_templates/`.
- Store workflow-specific prompt packs as markdown files under:
  - `60_automation/prompts/` (automation/ops prompts)
  - `40_listings/prompts/` (listing prompts)
  - `50_content/prompts/` (content prompts + social image prompts)
  - `70_ads/prompts/` (ad prompts)

- Image planning prompts should live with the workflow they support:
  - listing image planning in `40_listings/prompts/`
  - social image prompts in `50_content/prompts/`
  - ad creative image prompts in `70_ads/prompts/`

Create these folders when prompt packs are actually added.

## Prompt Naming Convention

`prompt_<domain>_<job>_v<major>.<minor>.md`

Examples:

- `prompt_listing_title_variants_v1.0.md`
- `prompt_product_scoring_v1.0.md`
- `prompt_weekly_review_synthesis_v1.0.md`

## Versioning Notes

- Increment **minor** for wording/clarity improvements.
- Increment **major** for logic/rule changes.
- Log major prompt strategy updates in [12_DECISION_LOG.md](12_DECISION_LOG.md).
