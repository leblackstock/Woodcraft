# 09 Data Model

Purpose: define consistent record schemas so decisions are traceable and automation-ready.

## Source-of-Truth Notes

- Product truth lives in `30_products/`.
- Listing truth lives in `40_listings/`.
- Content truth lives in `50_content/`.
- Ad test truth lives in `70_ads/`.
- Decision-level changes must be logged in [12_DECISION_LOG.md](12_DECISION_LOG.md).

## Copy-State Governance Pattern (Listings + Content)

These fields make the Claude gate enforceable in records instead of leaving it as prose-only policy.

| Field | Required | Allowed Values / Format | Description |
|---|---|---|---|
| approved_facts_status | Yes | `Working` / `Approved` | Whether the asset facts are complete enough for a valid Claude handoff. |
| customer_copy_status | Yes | `Prep Only` / `Claude Required` / `Handoff Prepared` / `Claude Output Pasted Back` / `Final Integrated` | Current state of customer-facing prose in the asset. |
| claude_handoff_ref | No | Free text ref / file / date | Where the approved-facts Claude handoff is recorded. Leave blank until prepared. |
| claude_output_ref | No | Free text ref / date | Where pasted-back Claude output is recorded. Leave blank until received. |
| publish_ready | Yes | `Yes` / `No` | Asset may only be publish-ready when facts are approved, Claude output has been integrated, and required non-copy fields are complete. |

### Copy-State Rules

- Before `customer_copy_status: Final Integrated`, customer-facing fields must contain `[[CLAUDE_FINAL_COPY_REQUIRED]]` or strictly non-publishable structured bullets.
- Draft phrasing that is useful internally but not Claude-final belongs in `customer_copy_prep_notes`.
- `claude_handoff_ref` should appear only after `approved_facts_status: Approved`.
- `publish_ready: Yes` is invalid unless `customer_copy_status: Final Integrated` and `claude_output_ref` is filled.

### Publish-Status Rules

- `publish_status` must not outrun the Claude gate or `publish_ready`.
- Prep-only assets (`customer_copy_status: Prep Only`) must stay in clearly non-publish states.
- Listing records with `publish_ready: No`, incomplete approved facts, or an incomplete Claude gate may use only `Draft`, `Paused`, or `Archived`.
- `Ready for Manual Publish` is valid only when the listing has cleared the Claude gate and `publish_ready: Yes`.
- `Published` is valid only after the listing has cleared the Claude gate, `publish_ready: Yes`, and a manual publish event has happened.
- Content records with `publish_ready: No`, incomplete approved facts, or an incomplete Claude gate may use only `Draft` or `Archived`.
- `Ready to Schedule`, `Scheduled`, and `Published` are valid only when the content asset has cleared the Claude gate and `publish_ready: Yes`.
- `publish_date` is the actual publish date only. Leave it blank until the asset is actually published; do not use it as a tentative schedule field for prep-only assets.

## Product Record Schema

| Field | Required | Description |
|---|---|---|
| product_id | Yes | Unique ID (e.g., `prod_raised_bed_001`) |
| product_name | Yes | Human-readable product name |
| category | Yes | Decor / Planter / Raised Bed / Furniture |
| date_created | Yes | Record creation date |
| owner | Yes | Human owner / approver |
| target_buyer | Yes | Primary buyer/use case |
| primary_use_case | Yes | Main use case described plainly |
| seasonal_notes | No | Seasonal fit, assumptions, or timing notes |
| material_spec | Yes | Key material assumptions |
| build_time_estimate | Yes | Estimated labor time |
| unit_cost_estimate | Yes | Materials + labor estimate |
| target_price | Yes | Initial list price target |
| margin_estimate | Yes | Estimated margin at target price |
| delivery_shipping_mode | Yes | Primary fulfillment mode(s); use slash-separated values from Pickup / Delivery / Shipping |
| comparable_examples | No | Comparable market examples or notes |
| local_price_range | No | Observed or assumed local price band |
| demand_signals | No | Summary of observed or assumed demand signals |
| demand_signal | No | 1–5 score |
| margin_potential | No | 1–5 score |
| build_complexity | No | 1–5 score |
| photo_listability | No | 1–5 score |
| fulfillment_practicality | No | 1–5 score |
| repeatability | No | 1–5 score |
| status | Yes | Candidate / Approved / Hold / Rejected / Active |
| score_total | No | Decision score from workflow |
| decision_reason | No | Why the current status was chosen |
| next_action | No | Immediate next step |
| pricing_validation | No | Approved-product readiness note |
| build_complexity_review | No | Approved-product readiness note |
| fulfillment_review | No | Approved-product readiness note |
| market_clarity_review | No | Approved-product readiness note |
| pending_confirmation | No | Outstanding checks before listing/publish |
| notes | No | Freeform notes |

## Listing Record Schema

| Field | Required | Description |
|---|---|---|
| listing_id | Yes | Unique ID |
| product_id | Yes | Reference to product record |
| channel | Yes | Marketplace / Etsy / Other |
| publish_status | Yes | Draft / Ready for Manual Publish / Published / Paused / Archived (`Ready for Manual Publish` and `Published` require `publish_ready: Yes`) |
| last_updated | Yes | Date updated |
| approved_facts_status | Yes | See copy-state governance pattern |
| customer_copy_status | Yes | See copy-state governance pattern |
| claude_handoff_ref | No | See copy-state governance pattern |
| claude_output_ref | No | See copy-state governance pattern |
| publish_ready | Yes | See copy-state governance pattern |
| listing_title | Yes | Final customer-facing title or `[[CLAUDE_FINAL_COPY_REQUIRED]]` |
| listing_description | Yes | Final customer-facing description or `[[CLAUDE_FINAL_COPY_REQUIRED]]` |
| customer_copy_prep_notes | No | Internal prep copy, bullets, or non-Claude draft phrasing |
| listing_price | Yes | Posted price |
| short_pitch | No | Internal offer summary only; not a publishable customer-facing field |
| key_features | No | Internal feature bullets only; not a publishable customer-facing field |
| dimensions_specs | Yes | Size/spec detail |
| material_details | Yes | Material detail |
| location_scope | Yes | Service area/pickup details |
| pickup_delivery_options | Yes | Fulfillment options summary |
| lead_time | Yes | Fulfillment expectation |
| customization_options | No | Customization boundaries |
| media_assets | Yes | Photos/video references |
| hero_photo | No | Primary photo plan |
| angle_shots | No | Additional angle shot plan |
| detail_shots | No | Detail shot plan |
| in-use_shot | No | Lifestyle or scale shot plan |
| optional_video | No | Video reference or plan |
| faq_prep | No | Internal FAQ prep notes |
| objection_handling_prep | No | Internal objection-handling prep notes |
| publish_date | No | Actual publish date only; leave blank until manually published |
| views | No | Count metric |
| saves | No | Count metric |
| messages | No | Count metric |
| sales | No | Count metric |
| performance_snapshot | No | Views, saves, messages, sales summary |
| notes | No | Freeform notes |

## Content Record Schema

| Field | Required | Description |
|---|---|---|
| content_id | Yes | Unique ID |
| linked_product_id | No | Optional product reference |
| linked_listing_id | No | Optional listing reference |
| platform | Yes | FB Page / Instagram / TikTok / Shorts |
| content_type | Yes | Photo post / Reel / Story / Short |
| publish_status | Yes | Draft / Ready to Schedule / Scheduled / Published / Archived (`Ready to Schedule`, `Scheduled`, and `Published` require `publish_ready: Yes`) |
| publish_ready | Yes | See copy-state governance pattern |
| approved_facts_status | Yes | See copy-state governance pattern |
| customer_copy_status | Yes | See copy-state governance pattern |
| claude_handoff_ref | No | See copy-state governance pattern |
| claude_output_ref | No | See copy-state governance pattern |
| hook | Yes | Internal opening angle; not final customer-facing copy |
| core_message | Yes | Internal post message or purpose |
| caption | Yes | Final customer-facing caption or `[[CLAUDE_FINAL_COPY_REQUIRED]]` |
| customer_copy_prep_notes | No | Internal prep copy, bullets, or non-Claude caption draft |
| cta | Yes | Internal CTA goal or direction; final CTA phrasing belongs in the Claude-written caption |
| hashtag_notes | No | Hashtag plan |
| local_context_tags | No | Local tag plan |
| asset_refs | Yes | Image/video references |
| thumbnail_note | No | Cover/thumbnail plan |
| publish_date | No | Actual publish date only; leave blank until published |
| outcome_notes | No | Engagement and learnings |

## Ad Test Record Schema

| Field | Required | Description |
|---|---|---|
| ad_test_id | Yes | Unique ID |
| linked_listing_id | Yes | Listing being promoted |
| channel | Yes | Ad platform/channel |
| owner_approval | Yes | Human approval record |
| status | Yes | Planned / Live / Complete / Stopped |
| objective | Yes | Messages / Traffic / etc. |
| audience_notes | No | Targeting notes |
| budget_total | Yes | Total planned spend |
| duration_days | Yes | Planned test length |
| creative_variant | No | Creative/copy variant being tested |
| organic_proof_summary | No | Organic signals that justified testing |
| launch_criteria | Yes | Why this qualified for testing |
| launch_criteria_met | No | Yes / No check |
| stop_rule | Yes | Predefined fail condition |
| success_rule | Yes | Predefined pass condition |
| max_loss_tolerance | No | Additional budget-loss guardrail |
| spend | No | Actual spend |
| key_metrics | No | Performance metrics snapshot |
| result_summary | No | Outcome snapshot |
| decision | No | Scale / Iterate / Stop |
| next_action | No | Follow-up step |
