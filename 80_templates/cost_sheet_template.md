# Cost Sheet Template

Purpose: keep cost math simple, markdown-native, auditable, and aligned with workspace profit guardrails before pricing is approved.

## Cost Sheet Identity

- cost_sheet_id:
- date_prepared:
- prepared_by:
- linked_product_id:
- linked_listing_id:
- standard_spec_ref:
- cost_basis_date:
- pricing_status: Draft / Ready for Approval / Approved

## Materials Line Items

| Item | Qty | Unit Cost | Line Total | Basis / Note |
|---|---:|---:|---:|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

- materials_subtotal:

## Hardware and Consumables

- hardware_allowance:
- finish_or_consumables_allowance:
- materials_cost_total:

## Labor

- labor_hours:
- labor_rate:
- labor_total:

## Delivery / Platform Allowances

- delivery_cost_allowance:
- platform_fee_allowance:
- other_allowances:

## Unit Economics

- total_unit_cost:
- target_price:
- gross_profit:
- gross_margin:

## Dual Pricing Strategy Check

- pricing_strategy_1_price_floor:
- pricing_strategy_1_note: Higher of `total_unit_cost / 0.60` or `total_unit_cost + applicable profit floor`
- pricing_strategy_2_price_floor:
- pricing_strategy_2_note: `materials_cost_total / 0.30`
- material_cost_percent_of_price:
- recommended_price_floor:
- pricing_strategy_review: Pass / Fail / Blocked / Needs Approval

## Guardrail Check

| Check | Target | Result | Notes |
|---|---|---|---|
| Gross margin floor | >= 40% | Pass / Fail / Blocked |  |
| Profit floor | Per [04_BUSINESS_RULES.md](../04_BUSINESS_RULES.md) | Pass / Fail / Blocked |  |
| Materials are 30% of finished price | `materials_cost_total / target_price <= 30%` | Pass / Fail / Blocked |  |
| Recommended price floor used | Higher of Strategy 1 and Strategy 2 unless explicitly overridden | Pass / Fail / Blocked |  |
| Cost uncertainty acceptable for approval | Low enough to price truthfully | Pass / Fail / Blocked |  |

## Notes and Approval

- unresolved_inputs:
- operator_notes:
- approval_status:
- approved_by:
- approval_date: