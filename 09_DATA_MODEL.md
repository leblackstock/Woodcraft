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

## Verification Governance Pattern (Approved Products + Listings)

These fields add a lightweight audit trail for fact verification before the Claude gate. They support approved-facts progression but do not replace it.

| Field | Required | Allowed Values / Format | Description |
|---|---|---|---|
| standard_spec_ref | No | File path / free text ref | Standard spec used for default-fill assumptions and deviation checks. |
| cost_sheet_ref | No | File path / free text ref | Cost sheet used for margin/profit calculations. |
| verification_evidence_ref | No | File path / free text ref | Where raw evidence intake is stored (measurements, receipts, labor note, photo note, delivery note). |
| verification_packet_ref | No | File path / free text ref | Where the bundled operator approval packet is stored. |
| verification_status | Yes | `Not Started` / `Intake Collected` / `Packet Ready` / `Approved` / `Blocked` | Current verification workflow state. |
| unresolved_fact_gaps | No | Free text list | Remaining missing facts, exceptions, or blockers that prevent truthful approval. |

### Verification-State Rules

- `verification_status` is separate from `approved_facts_status`.
- `verification_status: Not Started` means the verification structure exists but usable intake has not been assembled yet.
- `verification_status: Intake Collected` means raw inputs have been captured, but the approval packet is not ready yet.
- `verification_status: Packet Ready` means GPT-5.4 has done the internal work first and assembled one bundled approval packet for the operator.
- `verification_status: Approved` means the operator has approved or corrected the packet and the linked refs reflect the current truth.
- `verification_status: Blocked` means at least one real-world fact is missing or a guardrail check failed.
- A verification packet may recommend fact approval, but `approved_facts_status` stays `Working` until the facts are actually approved.
- `publish_ready: Yes` still requires the existing approved-facts rules, the Claude gate, and manual pricing/publishing approval.

## Dual Pricing Review Pattern

These fields support the required two-strategy pricing review whenever a price is proposed or an existing price is checked.

| Field | Required | Allowed Values / Format | Description |
|---|---|---|---|
| materials_cost_estimate | No | Currency / free text note | Materials-only estimate used for the 30%-of-finished-price benchmark. |
| pricing_strategy_1_price_floor | No | Currency / free text note | Minimum price from the current total-cost guardrail method. |
| pricing_strategy_2_price_floor | No | Currency / free text note | Minimum/benchmark price when materials are 30% of finished price. |
| material_cost_percent_of_price | No | Percent / free text note | Reverse-check value for `materials_cost_estimate / target_price`. |
| recommended_price_floor | No | Currency / free text note | Default floor after comparing both strategies; normally the higher of Strategy 1 and Strategy 2. |
| pricing_strategy_review | No | Free text note | Summary of whether both strategies pass, fail, or remain blocked pending better inputs. |

## Build Model + Media Truth Pattern

These fields keep listing-first made-to-order truth explicit and auditable.

| Field | Required | Allowed Values / Format | Description |
|---|---|---|---|
| build_model | Yes | `Made to Order` / `In Stock` / `Sample Built` | Truthful operating model for the product or listing. |
| media_truth_status | No | `Owned Real Photo` / `Owned AI-Assisted Photo` / `Concept / Mockup` / `Third-Party Reference Only` | Governing label for the media currently planned or used. |
| media_provenance_note | No | Short free text note | Brief note on owned-photo origin, AI derivation, or why media is reference-only only. |

### Build-Model and Media Rules

- `build_model: Made to Order` allows listing progression before a fresh build exists only when the standard spec, price logic, lead time, delivery terms, and media truth are locked.
- `build_model: In Stock` means the listed item already exists and fulfillment claims should match that inventory truth.
- `build_model: Sample Built` means a real sample/prototype exists and may support truthful listing media for future builds.
- `Owned Real Photo` is allowed for listing use when the photo comes from an owned prior build, sample, or current finished piece.
- `Owned AI-Assisted Photo` is allowed only when the source image is owned and the media is still used truthfully.
- `Concept / Mockup` must not be represented as a fresh finished-product photo.
- `Third-Party Reference Only` may be stored in notes, research, or source fields, but it is not allowed in listing-media fields or publishable content assets.
- After the first real made-to-order build, update existing refs and fields with actual receipts, labor, dimensions, photos, and pricing learnings rather than leaving the record permanently estimate-only.

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
| build_model | Yes | See build model + media truth pattern |
| plans_available | Yes | `Yes` / `No`; default `No` unless a real plan/reference source exists |
| plans_source_ref | No | Actual build-plan/reference URL or local research doc ref supporting `plans_available: Yes` |
| reference_source | No | Source set name for imported/reference products (e.g., `Who’s the Voss 2026 pricing guide`) |
| reference_code | No | Original source code/name from flyer/reference set (e.g., `Planter Box C`) |
| source_links | No | Markdown links or labeled external references used for plans, source pages, or verification support |
| media_truth_status | No | See build model + media truth pattern |
| media_provenance_note | No | Short note on media origin/truth boundary |
| standard_spec_ref | No | Linked standard spec file or reference |
| cost_sheet_ref | No | Linked cost sheet file or reference |
| verification_evidence_ref | No | Linked raw evidence file/reference |
| verification_packet_ref | No | Linked verification packet file/reference |
| verification_status | Yes | See verification governance pattern |
| unresolved_fact_gaps | No | Outstanding missing facts or exceptions |
| target_buyer | Yes | Primary buyer/use case |
| primary_use_case | Yes | Main use case described plainly |
| seasonal_notes | No | Seasonal fit, assumptions, or timing notes |
| material_spec | Yes | Key material assumptions |
| build_time_estimate | Yes | Estimated labor time |
| lead_time_estimate | No | Estimated fulfillment lead time for the current build model |
| unit_cost_estimate | Yes | Materials + labor estimate |
| materials_cost_estimate | No | Materials-only estimate used for the 30% pricing benchmark |
| pricing_strategy_1_price_floor | No | Current-method minimum price based on total-cost guardrails |
| pricing_strategy_2_price_floor | No | Materials-benchmark price based on materials being 30% of finished price |
| target_price | Yes | Initial list price target |
| margin_estimate | Yes | Estimated margin at target price |
| material_cost_percent_of_price | No | Materials cost as a percent of target price |
| recommended_price_floor | No | Higher of the two pricing-strategy floors unless manually overridden |
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
| pricing_strategy_review | No | Dual-strategy pricing result note |
| build_complexity_review | No | Approved-product readiness note |
| fulfillment_review | No | Approved-product readiness note |
| market_clarity_review | No | Approved-product readiness note |
| pending_confirmation | No | Outstanding checks before listing/publish |
| notes | No | Freeform notes |

### Product Source-Link Convention

- When a product record uses an external website, plan page, or reference source, store it in `source_links` instead of creating ad hoc headings like `Website` inside notes.
- Preferred format: markdown link with a short label, for example `[Build plan — Ana White: Modern Fence Picket Planter](https://example.com)`.
- If more than one external reference is needed, separate them with ` | ` on the same field or turn them into a short labeled list in notes only when additional context is necessary.

### Product Naming + Plans/Reference Tracking Rules

- Imported reference products may use a clean human-readable `product_name` instead of raw source/flyer codes.
- Preserve original source/flyer naming in `reference_code` (for example, use `Cedar Tall Square Planter 16x16x25` as `product_name` and store `Planter Box C` in `reference_code`).
- Use `reference_source` to identify the originating source set (for example, `Who’s the Voss 2026 pricing guide`).
- `plans_available` defaults to `No` for non-imported products and any product without a real source-backed plan/reference.
- Set `plans_available: Yes` only when a real source exists, and store the supporting link/doc in `plans_source_ref`.

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
| build_model | Yes | See build model + media truth pattern |
| standard_spec_ref | No | Linked standard spec file or reference |
| cost_sheet_ref | No | Linked cost sheet file or reference |
| verification_evidence_ref | No | Linked raw evidence file/reference |
| verification_packet_ref | No | Linked verification packet file/reference |
| verification_status | Yes | See verification governance pattern |
| unresolved_fact_gaps | No | Outstanding missing facts or exceptions |
| listing_title | Yes | Final customer-facing title or `[[CLAUDE_FINAL_COPY_REQUIRED]]` |
| listing_description | Yes | Final customer-facing description or `[[CLAUDE_FINAL_COPY_REQUIRED]]` |
| customer_copy_prep_notes | No | Internal prep copy, bullets, or non-Claude draft phrasing |
| listing_price | Yes | Posted price |
| pricing_strategy_review | No | Dual-strategy pricing result note for the current listing price |
| short_pitch | No | Internal offer summary only; not a publishable customer-facing field |
| key_features | No | Internal feature bullets only; not a publishable customer-facing field |
| dimensions_specs | Yes | Size/spec detail |
| material_details | Yes | Material detail |
| location_scope | Yes | Service area/pickup details |
| pickup_delivery_options | Yes | Fulfillment options summary |
| lead_time | Yes | Fulfillment expectation |
| customization_options | No | Customization boundaries |
| media_truth_status | Yes | See build model + media truth pattern |
| media_provenance_note | No | Short note on media origin/truth boundary |
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

### Listing Pricing Rule

- `listing_price` should be traceable to the linked cost sheet's dual pricing review.
- `pricing_strategy_review` should summarize whether the current listing price passes both strategies, is blocked, or still needs approval.
- If a listing price is already set before a full cost sheet is finalized, reverse-check it against both pricing strategies before calling it acceptable.

### Listing Media Rule

- `media_assets` should label each planned asset with its truthful media type when needed.
- `Third-Party Reference Only` assets must stay out of listing-media fields even if they remain useful in `source_links`, research notes, or internal planning docs.
- When a made-to-order listing starts with prior-build or AI-assisted media, update the record with stronger actual-build media after the first real build when available.

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

### Content Media Rule

- Published or schedulable content must follow the same media-truth rules as listings.
- Third-party reference media may support planning, but it must not be used as publishable content media.

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
