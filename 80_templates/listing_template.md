# Listing Template

## Listing Identity

- listing_id:
- product_id:
- build_model: Made to Order / In Stock / Sample Built
- channel: Marketplace / Etsy / Other
- publish_status: Draft / Ready for Manual Publish / Published / Paused / Archived
- last_updated:
- approved_facts_status: Working / Approved
- customer_copy_status: Prep Only / Claude Required / Handoff Prepared / Claude Output Pasted Back / Final Integrated
- claude_handoff_ref:
- claude_output_ref:
- publish_ready: Yes / No
- standard_spec_ref:
- cost_sheet_ref:
- verification_evidence_ref:
- verification_packet_ref:
- verification_status: Not Started / Intake Collected / Packet Ready / Approved / Blocked
- unresolved_fact_gaps:

> Governed status rule: if `publish_ready: No` or the Claude gate is incomplete, keep `publish_status` at `Draft`, `Paused`, or `Archived` only. Do not use `Ready for Manual Publish` or `Published` until the asset has cleared the gate.

> Verification rule: `verification_status` supports approved-facts readiness and one-shot operator review. It does not replace `approved_facts_status`, manual approval, or the Claude gate.

> Pricing rule: every `listing_price` must be checked against both approved pricing strategies in the linked cost sheet or verification packet. If the price was set earlier, reverse-check it before treating it as good pricing.

> Made-to-order rule: a fresh build is not required before listing if the standard spec, pricing logic, lead time, delivery terms, and media truth are locked.

## Core Offer

- listing_title: [[CLAUDE_FINAL_COPY_REQUIRED]]
- listing_description: [[CLAUDE_FINAL_COPY_REQUIRED]]
- customer_copy_prep_notes:
- listing_price:
- pricing_strategy_review:
- short_pitch: Internal offer summary only
- key_features: Internal feature bullets only
- dimensions_specs:
- material_details:

## Fulfillment Terms

- location_scope:
- pickup_delivery_options:
- lead_time:
- customization_options:

## Media Plan

- media_truth_status: Owned Real Photo / Owned AI-Assisted Photo / Concept / Mockup / Third-Party Reference Only
- media_provenance_note:
- media_assets:
- hero_photo:
- angle_shots:
- detail_shots:
- in-use_shot:
- optional_video:

> Media truth rule: owned real photos from prior builds are allowed for listing use. AI-assisted images are allowed only when derived from owned real photos and still used truthfully. Third-party/source/tutorial/plan images must not be used as listing media.

> Media planning rule: if `media_truth_status` is `Third-Party Reference Only`, keep that asset in planning/reference notes only and out of publishable listing media fields.

## Buyer Support Copy

- faq_prep:
- objection_handling_prep:

## Performance Log

- publish_date: Leave blank until the listing is actually published
- views:
- saves:
- messages:
- sales:
- performance_snapshot:
- notes:
