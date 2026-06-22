# Listing Template

## Listing Identity

- listing_id:
- listing_ref: Internal plain-language reference for this exact offer or variant collection. Never use as customer-facing title copy.
- listing_handle: Stable lowercase, hyphenated internal handle for prompting, filenames, and chat requests. Never use as customer-facing title copy.
- product_id:
- product_family_id: Leave blank unless this listing represents a configurable product family.
- variant_scope: One or more approved variant codes allowed in this listing; do not use bundle contents here.
- build_model: Made to Order / In Stock / Sample Built / Pilot Build
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

> Pricing rule: every `listing_price` must be checked against the Strategy 2 materials benchmark and any available Strategy 1 calculation in the linked cost sheet or verification packet. If labor-inclusive Strategy 1 is not ready, carry it as a visible note rather than a standalone blocker.

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

- brand_assets_ref: 00_brand/
- media_truth_status: Owned Real Photo / Owned AI-Assisted Photo / Concept / Mockup / Third-Party Reference Only
- media_provenance_note:
- media_assets:
- scope_reference_asset: Listing-level clean reference showing the full `variant_scope`; leave blank when no grouped scope image is needed. This does not replace individual variant clean references.
- scope_reference_variant_codes: Must exactly match `variant_scope` when `scope_reference_asset` is set.
- scope_reference_status: Not Needed / Pending Operator Approval / Approved.
- hero_photo:
- angle_shots:
- detail_shots:
- in-use_shot:
- optional_video:

> Media truth rule: owned real photos from prior builds are allowed for listing use. AI-assisted images are allowed only when derived from owned real photos and still used truthfully. Third-party/source/tutorial/plan images must not be used as listing media.

> Media planning rule: if `media_truth_status` is `Third-Party Reference Only`, keep that asset in planning/reference notes only and out of publishable listing media fields.

> Brand asset rule: any brand-specific image, graphic, logo, color, HTML, or template work for this listing must reference `00_brand/` as the current brand asset source of truth.

> External prompt rule: any listing-copy, image, graphic, research, or transformation prompt sent outside this repository must pass `80_templates/standalone_external_prompt_checklist.md` and inline all relevant facts, brand/voice/visual rules, literal text, constraints, attachments, output requirements, quality criteria, and failure behavior.

## Buyer Support Copy

- faq_prep:
- objection_handling_prep:

## Performance Log

- publish_date: Leave blank until the listing is actually published
- published_variant_scope: Snapshot of the exact `variant_scope` posted live; leave blank until actual publication.
- live_listing_url:
- views:
- saves:
- messages:
- sales:
- performance_snapshot:
- notes:
