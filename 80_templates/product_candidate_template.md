# Product Candidate Template

## Basic Info

- record_type: Standalone Product / Configurable Product Family / Variant
- product_id: Required for Standalone Product and Configurable Product Family; leave blank for Variant.
- variant_id: Required for Variant; leave blank otherwise.
- family_product_id: Required for Variant; otherwise leave blank.
- family_catalog_id: Parent catalog ID for Variant reference only; leave blank otherwise.
- family_code: Required for Configurable Product Family and Variant; otherwise leave blank.
- variant_code: Required for a permanent standard Variant; otherwise leave blank.
- colorway_code: Optional approved style/colorway code for a Variant.
- catalog_id: Required for Standalone Product and Configurable Product Family. Leave blank for Variant; child variants use `variant_code` under the parent catalog ID.
- catalog_sku:
- sku_activation_status: Active / Not Active
- clean_ref_files:
- clean_reference_generation_prompt_ref:
- conversion_manifest_ref: Required when this record results from conversion of an existing standalone product into a configurable family or child Variant.
- sku_activation_ref: 30_products/sku_activation_index.md
- product_name:
- category:
- date_created:
- owner:
- build_model: Made to Order / In Stock / Sample Built / Pilot Build
- customer_size_label: Optional for Variant.
- customer_facing_dimensions: Optional for Variant.
- physical_target_dimensions: Optional for Variant.

## Verification Snapshot

- plans_available: Yes / No
- plans_source_ref:
- reference_source:
- reference_code:
- source_links:
- media_truth_status: Owned Real Photo / Owned AI-Assisted Photo / Concept / Mockup / Third-Party Reference Only
- media_provenance_note:
- brand_assets_ref: 00_brand/ when brand-specific media, graphics, templates, or generated visuals are used
- standard_spec_ref:
- cost_sheet_ref:
- verification_evidence_ref:
- verification_packet_ref:
- verification_status: Not Started / Intake Collected / Packet Ready / Approved / Blocked
- unresolved_fact_gaps:

## Buyer + Use Case

- target_buyer:
- primary_use_case:
- seasonal_notes:

## Build + Cost Snapshot

- material_spec:
- build_time_estimate:
- lead_time_estimate:
- unit_cost_estimate:
- materials_cost_estimate:
- pricing_strategy_1_price_floor:
- pricing_strategy_1_note:
- pricing_strategy_2_price_floor:
- target_price:
- margin_estimate:
- material_cost_percent_of_price:
- recommended_price_floor:
- pricing_strategy_review:

## Fulfillment Fit

- delivery_shipping_mode: Pickup / Delivery / Shipping

## Demand + Market Notes

- comparable_examples:
- local_price_range:
- demand_signals:

## Scoring (1–5)

- demand_signal:
- margin_potential:
- build_complexity:
- photo_listability:
- fulfillment_practicality:
- repeatability:
- score_total:

## Decision

- status: Candidate / Approved / Hold / Rejected / Active
- decision_reason:
- next_action:

## Publish Readiness Review (Approved Products Only)

- pricing_validation:
- build_complexity_review:
- fulfillment_review:
- market_clarity_review:
- pending_confirmation:

> Listing-first rule: approved products may move toward made-to-order listing prep before a fresh build exists if the standard launch spec, price logic, lead time, delivery terms, and media truth are locked.

> Configurable-product rule: create the family parent first, then create one child Variant record for every permanent, separately priced standard option. A child Variant has no independent `catalog_id`; it receives a stable `variant_code`, its own price/spec/clean-reference truth, and a link to the family parent. One-off custom requests are quote-only unless later promoted to a permanent Variant.

> Brand asset rule: brand-specific photos, logos, colors, graphics, HTML/template styling, and generated-visual references should point to `00_brand/` rather than older catalog-export folders.

> External prompt rule: any research, analysis, media, graphic, or transformation prompt sent outside this repository must pass `80_templates/standalone_external_prompt_checklist.md` and inline all relevant scope, facts, brand rules, constraints, attachments, output requirements, evidence standards, quality criteria, and uncertainty behavior.

## Notes

- notes:
