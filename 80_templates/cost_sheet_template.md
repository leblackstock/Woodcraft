# Cost Sheet Template

Purpose: keep cost math simple, markdown-native, auditable, and aligned with workspace profit guardrails before pricing is approved.

Brand asset reminder: if this cost sheet supports branded listing, ad, graphic, HTML/template, or generated-visual work, reference `00_brand/` through the linked product/listing/content record rather than duplicating brand assets here.

## Cost Sheet Identity

- cost_sheet_id:
- date_prepared:
- prepared_by:
- linked_product_id:
- linked_product_family_id:
- linked_variant_id:
- variant_code:
- linked_listing_id:
- variant_scope: Use only when documenting the selected options shown by a linked scope listing. Do not combine separately priced variants into one bundle cost or price without an approved bundle product.
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
- pricing_strategy_1_note: Higher of `total_unit_cost / 0.60` or `total_unit_cost + applicable profit floor` when labor-inclusive inputs exist; otherwise carry as an advisory pending note.
- pricing_strategy_2_price_floor:
- pricing_strategy_2_note: `materials_cost_total / 0.30`
- material_cost_percent_of_price:
- recommended_price_floor: Default pricing baseline under current policy; normally Strategy 2 unless otherwise stated, with warning if calculated Strategy 1 differs by more than 15%
- pricing_strategy_review: Pass / Fail / Needs Approval / Advisory Strategy 1 Pending

## Guardrail Check

| Check | Target | Result | Notes |
|---|---|---|---|
| Gross margin floor | >= 40% | Pass / Fail / Blocked |  |
| Profit floor | Per [04_BUSINESS_RULES.md](../04_BUSINESS_RULES.md) | Pass / Fail / Blocked |  |
| Materials are 30% of finished price | `materials_cost_total / target_price <= 30%` | Pass / Fail / Blocked |  |
| Strategy 1 variance warning raised when needed | Warn if calculated Strategy 1 differs from Strategy 2 by > 15%; note pending Strategy 1 when labor inputs are not ready | Pass / Fail / Note |  |
| Cost uncertainty acceptable for approval | Low enough to price truthfully | Pass / Fail / Blocked |  |

## Notes and Approval

- unresolved_inputs:
- operator_notes:
- approval_status:
- approved_by:
- approval_date:

> Variant cost rule: prepare or link cost truth per permanent variant. A scope listing may reference those individual cost sheets, but it does not create a combined product cost, bundle price, or savings claim.
