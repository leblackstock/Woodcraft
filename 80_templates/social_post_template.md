# Social Post Template

## Post Identity

- content_id:
- linked_product_id:
- linked_listing_id:
- linked_product_family_id: Required when this post presents a selected variant scope.
- variant_scope: Exact active variant codes shown by a scope-based post; do not use for bundles.
- scope_reference_asset: Required when the image shows the complete variant scope together.
- scope_reference_variant_codes: Must exactly match `variant_scope` when `scope_reference_asset` is set.
- scope_activation_status: Not Needed / All Variants Active / Blocked.
- sku_activation_status: Active / Not Active / Blocked
- sku_activation_ref: 30_products/sku_activation_index.md
- platform: FB Page / Instagram / TikTok / Shorts
- publish_status: Draft / Ready to Schedule / Scheduled / Published / Archived
- publish_ready: Yes / No
- approved_facts_status: Working / Approved
- customer_copy_status: Prep Only / Claude Required / Handoff Prepared / Claude Output Pasted Back / Final Integrated
- claude_handoff_ref:
- claude_output_ref:

> Governed status rule: if `publish_ready: No` or the Claude gate is incomplete, keep `publish_status` at `Draft` or `Archived` only. Do not use `Ready to Schedule`, `Scheduled`, or `Published` until the asset has cleared the gate.

> SKU activation rule: create product-specific social posts only for SKUs marked `Active` in `30_products/sku_activation_index.md`. If the linked product is inactive, has no catalog SKU, or has no clean ref file, set `sku_activation_status: Not Active` or `Blocked` and do not create a new image prompt or post package.

> Variant-scope activation rule: a product-family showcase may use `variant_scope` only when every listed variant is `Active`. A grouped scope reference does not activate a variant. When the image shows the full scope together, attach the approved `scope_reference_asset` and keep the individual clean references as the underlying product controls.

## Creative Direction

- content_type: Photo post / Reel / Story / Short
- hook: Internal opening angle only
- core_message:
- cta: Internal post-copy or caption CTA goal only; final Facebook Page post copy and Instagram caption wording belongs to Claude
- layout_family:
- photo_subject:
- message_angle:
- graphic_treatment:
- text_intensity:
- cta_style:

## Copy

- post_copy: [[CLAUDE_FINAL_COPY_REQUIRED]] for Facebook Page
- caption: [[CLAUDE_FINAL_COPY_REQUIRED]] for Instagram
- exact_in_image_text: `NO_TEXT` or final literal image graphic text
- customer_copy_prep_notes:
- hashtag_notes:
- local_context_tags:

## Asset Plan

- brand_assets_ref: 00_brand/
- asset_refs:
- approved_reference_images:
- recent_post_history_ref:
- rotation_check_status: Not Checked / Checked / Not Enough History / Exception Recorded
- rotation_notes:
- image_prompt_ref:
- thumbnail_note:

> Brand asset rule: any brand-specific image, graphic, logo, color, template, post-copy prompt, caption prompt, or generated visual for this post must reference `00_brand/` as the current brand asset source of truth.

> External prompt rule: any post-copy, caption, image, graphic, or transformation prompt sent outside this repository must pass `80_templates/standalone_external_prompt_checklist.md` and inline all relevant facts, brand/voice/visual rules, literal text, constraints, attachments, output requirements, quality criteria, and failure behavior.

> Facebook Page image rule: use `50_content/facebook_brand_post_rules.md` and `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md`. GPT/Codex owns image graphic text under review by exception; Claude approval is not required for image graphic text. Claude still owns the final Facebook Page post copy.

## Publishing + Outcome

- publish_date: Leave blank until the post is actually published
- outcome_notes:
