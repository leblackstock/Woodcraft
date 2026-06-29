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
- platform: FB Page / Instagram / FB Page + Instagram / TikTok / Shorts
- cadence_date: YYYY-MM-DD / Not Assigned
- cadence_tracker_ref: 50_content/social_post_cadence_tracker.md
- output_aspect_ratio: 4:5 / 9:16 / 1:1 / Other approved requested format
- publish_status: Draft / Ready to Schedule / Scheduled / Published / Archived
- publish_ready: Yes / No
- facebook_page_publish_status: Not Used / Draft / Ready to Schedule / Scheduled / Published / Missed / Waived
- facebook_page_publish_date:
- instagram_publish_status: Not Used / Draft / Ready to Schedule / Scheduled / Published / Missed / Waived
- instagram_publish_date:
- approved_facts_status: Working / Approved
- customer_copy_status: Prep Only / Claude Required / Handoff Prepared / Claude Output Pasted Back / Final Integrated
- claude_handoff_ref:
- claude_output_ref:

> Governed status rule: if `publish_ready: No` or the Claude gate is incomplete, keep `publish_status` and each channel publish status at `Draft`, `Archived`, or `Not Used` only. Do not use `Ready to Schedule`, `Scheduled`, or `Published` until the asset has cleared the gate for that channel.

> SKU activation rule: create product-specific social posts only for SKUs marked `Active` in `30_products/sku_activation_index.md`. If the linked product is inactive, has no catalog SKU, or has no clean ref file, set `sku_activation_status: Not Active` or `Blocked` and do not create a new image prompt or post package.

> Variant-scope activation rule: a product-family showcase may use `variant_scope` only when every listed variant is `Active`. A grouped scope reference does not activate a variant. When the image shows the full scope together, attach the approved `scope_reference_asset` and keep the individual clean references as the underlying product controls.

> Daily cadence rule: Facebook Page and Instagram brand/support posts are tracked separately in `50_content/social_post_cadence_tracker.md`. A dual `platform: FB Page + Instagram` content record may appear in both tracker columns, but each channel counts toward the daily minimum only after that channel's approved-facts, Claude-copy, readiness, and manual publish/schedule gates are complete.

> Output ratio rule: static Facebook Page brand-awareness and static Instagram feed posts use `4:5`; Facebook or Instagram Story/Reel content uses `9:16`; Facebook Marketplace listing images and cards use `1:1`.

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
- post_copy_exception_approval: None / Approval Required / Approved — category, buyer-facing reason, and exact allowed fact or wording
- customer_copy_prep_notes:
- hashtag_notes: Ask Claude for 3 to 5 restrained, relevant hashtags written with leading `#` characters by default / `NO_HASHTAGS` if explicitly waived
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

> Social brand-post image rule: use `50_content/facebook_brand_post_rules.md` and `50_content/prompts/prompt_social_brand_post_generator_v2.0.md` for new dual Facebook Page + Instagram feed posts. GPT/Codex owns image graphic text under review by exception; Claude approval is not required for image graphic text. Claude still owns the final Facebook Page post copy and Instagram caption.

## Publishing + Outcome

- publish_date: Legacy/single-channel field; for dual records, use `facebook_page_publish_date` and `instagram_publish_date`
- outcome_notes:
