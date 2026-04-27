# Cost Sheet — Cedar Planter Box 24x24x18

## Cost Sheet Identity

- cost_sheet_id: cost_cedar_planter_box_001
- date_prepared: 2026-04-22
- prepared_by: GPT-5.5
- linked_product_id: prod_cedar_planter_box_001
- linked_listing_id: list_marketplace_planter_box_001
- standard_spec_ref: 30_products/spec_cedar_planter_box_standard.md
- cost_basis_date: 2026-04-27
- pricing_status: Owner Confirmed with Guardrail Warnings — owner confirmed a $90 sale price and $30 estimated full-cedar material cost on 2026-04-27.

## Materials Line Items

| Item | Qty | Unit Cost | Line Total | Basis / Note |
|---|---:|---:|---:|---|
| Full-cedar material estimate | 1 | $30.00 | $30.00 | Owner-confirmed estimate on 2026-04-27 for full-cedar build materials. |

- materials_subtotal: $30.00

## Hardware and Consumables

- hardware_allowance: Included in owner-confirmed $30.00 full-cedar material estimate.
- finish_or_consumables_allowance: Included in owner-confirmed $30.00 full-cedar material estimate.
- materials_cost_total: $30.00

## Labor

- labor_hours: 4.0 hours — using the high end of the approved 2.5 to 4 hour draft range for conservative pre-sale guardrail pricing.
- labor_rate: $20.00/hour
- labor_total: $80.00

## Delivery / Platform Allowances

- delivery_cost_allowance: $0.00 — base calculation assumes pickup-first pricing and treats any delivery charge as a separate buyer-facing fee.
- platform_fee_allowance: $0.00 — no Marketplace fee allowance included in this draft.
- other_allowances: $0.00

## Unit Economics

- total_unit_cost: $110.00
- target_price: $90.00 — owner-confirmed sale price on 2026-04-27.
- gross_profit: Materials-only spread is $60.00 before labor and delivery; labor-inclusive gross profit is -$20.00 using the current draft labor allowance.
- gross_margin: Materials-only margin is 66.7%; labor-inclusive margin is -22.2% using the current draft labor allowance.

## Dual Pricing Strategy Check

- pricing_strategy_1_price_floor: $183.33
- pricing_strategy_1_note: Higher of `total_unit_cost / 0.60` or `total_unit_cost + applicable profit floor`. Here that is higher of $183.33 (`$110.00 / 0.60`) or $150.00 (`$110.00 + $40` medium-planter profit floor).
- pricing_strategy_2_price_floor: $100.00
- pricing_strategy_2_note: `materials_cost_total / 0.30` = `$30.00 / 0.30` = $100.00.
- material_cost_percent_of_price: 33.3% at the owner-confirmed $90 sale price.
- recommended_price_floor: $100.00 default Strategy 2 baseline; Strategy 1 is $183.33 and remains a major warning.
- pricing_strategy_review: Owner Approved Override / Warning — owner confirmed $90 sale price after review context. The selected price is $10.00 below Strategy 2 and $93.33 below Strategy 1, so guardrail warnings remain visible even though the price is owner-confirmed.

## Guardrail Check

| Check | Target | Result | Notes |
|---|---|---|---|
| Gross margin floor | >= 40% | Fail / Owner Override | Labor-inclusive margin is -22.2% at the owner-confirmed $90 price using the current draft labor allowance. |
| Profit floor | Per [04_BUSINESS_RULES.md](../04_BUSINESS_RULES.md) | Fail / Owner Override | Labor-inclusive gross profit is -$20.00 at the owner-confirmed $90 price, below the $40 medium-planter floor. |
| Materials are 30% of finished price | `materials_cost_total / target_price <= 30%` | Fail / Owner Override | $30.00 / $90.00 = 33.3%. |
| Strategy 1 variance warning raised when needed | Warn if Strategy 1 differs from Strategy 2 by > 15% | Pass | Strategy 1 ($183.33) is 83.3% above Strategy 2 ($100.00), so the warning threshold is triggered and preserved. |
| Cost uncertainty acceptable for approval | Low enough to price truthfully | Pass with Owner Estimate | Owner confirmed the $30 material estimate for pre-sale pricing. Receipt-backed materials and actual labor remain post-build validation items. |

## Notes and Approval

- unresolved_inputs: Receipt-backed materials refresh / final delivery-fee wording within 25 miles / selected owned listing photos / actual labor timing after first build.
- operator_notes: Owner confirmed a $90 sale price and $30 estimated full-cedar material cost on 2026-04-27. Guardrail warnings remain because the chosen price is below Strategy 2 and far below Strategy 1 when draft labor is included.
- approval_status: Owner Confirmed with Guardrail Warnings
- approved_by: Lauren
- approval_date: 2026-04-27
