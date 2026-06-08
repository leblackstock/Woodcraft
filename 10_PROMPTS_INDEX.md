# 10 Prompts Index

Purpose: prevent prompt sprawl and keep reusable prompt sets organized.

Brand source-of-truth note: any prompt that creates or references Drakkar-specific text, graphics, ads, images, HTML, templates, copy, or generated visuals must reference [00_brand/](00_brand/) for current assets and identity guidance. Use `00_brand/VOICE.md`, `00_brand/COLOR_PALETTE.md`, `00_brand/TEXT_STYLE_RULES.md`, and `00_brand/VISUAL_STYLE.md` instead of owning separate brand rules in a prompt folder.

## Standalone External Prompt Standard

Any prompt meant to leave this repository must pass [80_templates/standalone_external_prompt_checklist.md](80_templates/standalone_external_prompt_checklist.md).

- Repository files are preparation sources, not instructions the external target can follow.
- Inline the relevant source facts, task context, brand rules, voice mode, palette, typography, visual direction, literal required text, constraints, reference requirements, copy-shape or output requirements, and quality criteria.
- Remove local-path dependencies from the delivered prompt unless the referenced file contents are actually attached.
- Make each delivered prompt independently usable. Do not require another prompt in the pack or surrounding notes.
- For image prompts that require an attached image, begin the copied prompt with `Please see attached "[plain-language item being attached]"`.
- For Claude final-copy prompts, inline the negative style rules: no em dashes or en dashes in final output, regular hyphens are okay when needed, and no AI-isms or common AI tells.
- Apply this standard to image prompts, graphic prompts, Claude handoffs, writing prompts, research prompts, analysis prompts, automation prompts, and transformation prompts.

## Dual-Model Prompt Roles

### GPT-5.5 Workflow Orchestration Prompts

Use GPT prompts for:

- workflow progression
- validation against approved facts
- queue movement
- missing-info detection
- structured prep for assets
- Claude handoff generation
- image graphic text when an active review-by-exception image workflow assigns it to GPT/Codex

### Claude Final Customer-Copy Prompts

Use Claude prompts for:

- final customer-facing listing prose
- final Facebook Page post copy
- final Instagram captions
- final post copy, caption, listing, ad, and reply CTA lines and promo blurbs outside governed image graphic text
- final customer-facing reply templates

Claude prompts are for final publishable customer-facing prose only.

Image graphic text assigned to GPT/Codex by an active review-by-exception image workflow does not require Claude approval.

### GPT-to-Claude Handoff Prompts

- GPT-5.5 must generate Claude handoff prompts from approved facts only.
- Each handoff must name the applicable mode from the one shared `00_brand/VOICE.md`: Catalog, Brand Post, Marketplace, or Customer Reply.
- Voice modes adjust emphasis only and never override core voice, banned-word, truthfulness, or approved-fact rules.
- Each Claude handoff must include the no-em-dash/no-en-dash rule and the no-AI-isms rule.
- Each Claude handoff must tell Claude to silently write several internal versions, analyze them, and then produce a stronger final version as the visible output.
- If facts are incomplete, stop upstream and resolve missing info before creating the handoff.
- Record the resulting handoff in `claude_handoff_ref` only after `approved_facts_status: Approved`.
- The human pastes Claude output back into the workflow for integration.
- Record pasted-back output in `claude_output_ref` before marking the asset `publish_ready: Yes`.

## Current Reusable Prompt Templates

These shared prompt templates live in [80_templates/](80_templates/):

- `80_templates/standalone_external_prompt_checklist.md`
- `80_templates/gpt_to_claude_handoff_prompt_template.md`
- `80_templates/claude_final_marketplace_listing_prompt.md`
- `80_templates/claude_final_social_post_copy_prompt.md`
- `80_templates/claude_final_customer_reply_prompt.md`

Current FBM workflow entry point:

- `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`

Brand identity references used by prompts:

- `00_brand/VOICE.md`
- `00_brand/COLOR_PALETTE.md`
- `00_brand/TEXT_STYLE_RULES.md`
- `00_brand/VISUAL_STYLE.md`

Workflow-specific listing image prompt templates live in [40_listings/prompts/](40_listings/prompts/):

- `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v1.1.md`
- `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md`
- `40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md`
- `40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v1.0.md`
- `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md`

Current Facebook Page brand-post image workflow:

- `30_products/sku_activation_index.md`
- `50_content/facebook_brand_post_rules.md`
- `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md`
- `80_templates/social_post_template.md`

Fast path for short "fb brand post prompt" requests:

- Treat as a Facebook Page brand-post prompt request unless the operator explicitly says Marketplace, ad, Instagram, or another channel.
- Start from the active/open content or prompt file when the target is clear.
- Read `30_products/sku_activation_index.md`, `50_content/facebook_brand_post_rules.md`, the active generator, and the target `50_content/content_fbpage_*.md` record before broader discovery.
- Create or deliver product-specific post prompts only for SKUs marked `Active` in the SKU activation index.
- If the content record already has an `image_prompt_ref`, open and deliver from that saved prompt instead of rebuilding the concept only when the linked SKU is still active.
- For Facebook Page post asks, deliver the filename block, standalone image prompt block, and Claude Facebook Page post-copy handoff block by default.
- Deliver only the filename block plus standalone image prompt block when the operator explicitly asks for an image prompt only.

Deprecated but retained for traceability:

- `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v1.0.md`

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
   - Text-bearing image prompts are allowed when the requested image needs readable words, labels, signage, branding, price text, catalog marks, packaging text, captions, or similar literal text.
   - Do not remove requested text from image prompts by default. ChatGPT Image 2 is considered capable for text-bearing image generation in this workflow.
   - Delivered image prompts must be standalone when copied into a target image model without repository access. Inline the required visual direction, palette values, typography direction, and literal image text rather than relying on local reference paths.
   - Copied image prompts should use direct positive instructions and exact rendered text, not internal repo labels, pricing-policy explanations, or long negative style-category lists.
   - For Facebook Marketplace listing images, exact product fidelity is always required: require the approved catalog image or reference image attachment and stop instead of delivering a text-only approximation when the attachment is missing.
   - When an attachment is required, the copied prompt starts with `Please see attached "[plain-language item being attached]"`.
   - FBM price-card graphics use one plain selling-price line from the approved FBM price; copied prompts should specify the exact rendered text instead of explaining internal price-label exceptions.
5. **Content Prompts**
   - GPT-5.5 orchestration/prep: short-form concept extraction from listings
   - GPT-5.5 orchestration/prep: Facebook Page brand-post image concepts, rotation checks, image graphic text, and standalone image prompts for active SKUs only
   - Claude final customer-facing prose: one best Facebook Page post-copy or Instagram caption output by default
   - Claude final customer-facing prose: social post-copy or caption CTA variants only when explicitly requested
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

- Image prompt packs may include exact in-image text instructions when text is part of the desired visual output. Keep the text literal and approved for the intended use; do not strip it merely because it is text.

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
