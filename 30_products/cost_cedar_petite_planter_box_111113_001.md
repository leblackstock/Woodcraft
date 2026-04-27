# Cost Sheet — Cedar Petite Planter Box 11x11x13

## Cost Sheet Identity

- cost_sheet_id: cost_cedar_petite_planter_box_111113_001
- date_prepared: 2026-04-21
- prepared_by: GPT-5.5
- linked_product_id: prod_cedar_petite_planter_box_111113_001
- linked_listing_id:
- standard_spec_ref:
- cost_basis_date: 2026-04-21
- pricing_status: Draft — explicitly blocked pending full review.

## Materials Line Items

| Item | Qty | Unit Cost | Line Total | Basis / Note |
|---|---:|---:|---:|---|
| Dog-eared cedar pickets | 3 | $3.68 | $11.04 | 20_research/material_cost_reference.md |
| Glue | 1 oz | $0.3125 per oz | $0.31 | $40.00 per gallon / 128 oz |
| Nail gun nails | 40 | $0.002 | $0.08 | $10.00 / 5,000 |

- materials_subtotal: $11.43

## Hardware and Consumables

- hardware_allowance: $0.00
- finish_or_consumables_allowance: $0.00
- materials_cost_total: $11.43

## Labor

- labor_hours: Pending — live build timing not yet verified.
- labor_rate: Pending
- labor_total: Pending

## Delivery / Platform Allowances

- delivery_cost_allowance: $0.00
- platform_fee_allowance: $0.00
- other_allowances: $0.00

## Unit Economics

- total_unit_cost: Pending — labor-inclusive unit cost not yet verified.
- target_price: $30.00
- gross_profit: Materials-only spread is $18.57 before labor.
- gross_margin: Materials-only margin is 61.9% before labor.

## Dual Pricing Strategy Check

- pricing_strategy_1_price_floor: Blocked — labor-inclusive total unit cost is still pending.
- pricing_strategy_1_note: Cannot complete total-cost guardrail pricing until labor hours and labor rate are verified.
- pricing_strategy_2_price_floor: $38.10
- pricing_strategy_2_note: $11.43 / 0.30 = $38.10
- material_cost_percent_of_price: 38.1%
- recommended_price_floor: At least $38.10 before labor; final floor may be higher once Strategy 1 is complete.
- pricing_strategy_review: Blocked / Pending Full Review — the user-set $30 target price is below the materials-at-30% benchmark, Strategy 1 is still incomplete, and labor is still unpriced.

## Guardrail Check

| Check | Target | Result | Notes |
|---|---|---|---|
| Gross margin floor | >= 40% | Blocked | Materials-only margin passes, but labor-inclusive margin is still unknown. |
| Profit floor | Per [04_BUSINESS_RULES.md](../04_BUSINESS_RULES.md) | Blocked | Medium planter profit floor cannot be checked without labor-inclusive total cost. |
| Materials are 30% of finished price | `materials_cost_total / target_price <= 30%` | Fail | $11.43 / $30.00 = 38.1%. |
| Recommended price floor used | Higher of Strategy 1 and Strategy 2 unless explicitly overridden | Fail | Current draft target price is $30.00 versus a minimum known floor of $38.10 before labor. |
| Cost uncertainty acceptable for approval | Low enough to price truthfully | Blocked | Labor timing and labor rate still need verification. |

## Notes and Approval

- unresolved_inputs: Standalone dimensions beyond trio-small reference / live build timing / labor rate / labor-inclusive unit cost.
- operator_notes: User requested a standalone draft price of $30; current material-cost benchmark suggests this is below guardrail before labor is included. Keep this price explicitly blocked pending full review rather than treating it as approved or ready.
- approval_status: Draft
- approved_by:
- approval_date: