# Verification Packet Template

Purpose: assemble one truthful, bundled approval packet that does maximum internal work first, highlights only real exceptions, and preserves the Claude final-copy gate.

## Packet Identity

- verification_packet_id:
- date_prepared:
- prepared_by:
- verification_status: Intake Collected / Packet Ready / Approved / Blocked
- asset_type: Product / Listing
- linked_product_id:
- linked_listing_id:
- standard_spec_ref:
- cost_sheet_ref:
- verification_evidence_ref:

## Asset Context

- asset_summary:
- current_workflow_state:
- intended_channel_or_use:
- approved_facts_status:
- publish_ready: Yes / No

## Raw Evidence Received

- operator_inputs_received:
- photos_or_media_refs:
- measurement_refs:
- receipt_or_price_refs:
- labor_input_refs:
- delivery_or_lead_time_refs:
- evidence_notes:

## Inferred Facts and Confidence

Use only these confidence labels: `Auto-verified`, `Recommended`, `Needs operator confirmation`, `Blocked`.

| Field | Proposed Value | Basis / Source | Confidence | Notes |
|---|---|---|---|---|
| Dimensions |  |  |  |  |
| Material stack |  |  |  |  |
| Hardware |  |  |  |  |
| Drainage |  |  |  |  |
| Liner |  |  |  |  |
| Lead time |  |  |  |  |
| Delivery policy |  |  |  |  |
| Strategy 1 price floor |  |  |  |  |
| Strategy 2 price floor |  |  |  |  |
| Target price |  |  |  |  |
| Material cost percent of price |  |  |  |  |
| Other key fact |  |  |  |  |

## Cost and Margin Calculation Summary

- total_unit_cost:
- target_price:
- gross_profit:
- gross_margin:
- materials_cost_total:
- pricing_strategy_1_price_floor:
- pricing_strategy_2_price_floor:
- material_cost_percent_of_price:
- recommended_price_floor:
- cost_sheet_summary:

## Guardrail Checks

| Check | Result | Notes |
|---|---|---|
| Gross margin meets workspace floor | Pass / Fail / Blocked |  |
| Profit floor meets workspace rule | Pass / Fail / Blocked |  |
| Materials are 30% of finished price | Pass / Fail / Blocked |  |
| Higher of the two pricing strategies is respected | Pass / Fail / Blocked |  |
| Lead time and delivery terms are truthful | Pass / Fail / Blocked |  |
| Required physical facts are supported | Pass / Fail / Blocked |  |

## Recommended Approval Packet

- auto_verified_items:
- recommended_defaults:
- operator_confirmation_required:
- blocked_items:

## Exceptions Only

- exceptions_summary:

## One-Shot Operator Approval Block

- operator_decision: Approve as bundled / Approve with edits / Block
- operator_edits:
- approved_price:
- approved_lead_time:
- approved_delivery_terms:
- approved_dimensions:
- approved_other_notes:
- approver:
- approval_date:

## Post-Approval Record Updates

- update standard/product/listing refs:
- update verification_status:
- update unresolved_fact_gaps:
- update approved_facts_status only if facts are truly approved:
- Claude handoff readiness after approval: