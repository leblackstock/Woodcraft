# 04 Business Rules

Hard guardrails for decisions, spending, and product selection.

## Low-Budget Operating Rules

- Protect cash first; avoid speculative spend.
- Prioritize actions that can be executed with existing tools/time.
- Keep experiments small, time-boxed, and measurable.
- If an action cannot show likely ROI, defer it.

### Budget Caps (Starter Defaults)

- Default ad test cap per test: **$20 max** unless explicitly approved.
- Default weekly paid spend cap: **$40 max** across all channels.
- Default monthly paid spend cap: **$120 max** until at least one product shows repeatable organic proof.

## Pricing and Profit Guardrails

- Every product should have a simple cost sheet or explicit cost note before listing.
- Include materials, labor time, delivery/shipping impact, and platform fees when known; mark missing live inputs as notes instead of treating every unknown as a blocker.
- Run both approved pricing strategies whenever the inputs exist, and preserve missing Strategy 1 inputs as advisory notes when labor-inclusive costs are not ready yet.
- Default the draft pricing baseline to the materials-at-30%-of-finished-price method unless the operator explicitly chooses a different rule.
- Show the Strategy 1 calculation alongside Strategy 2 when it can be calculated; otherwise show the Strategy 1 pending note.
- If Strategy 1 differs from Strategy 2 by more than **15%** in either direction, warn the operator and show both calculations before final price approval.
- Use gross-margin and profit-floor results as warning signals and decision support unless the operator explicitly chooses a stricter rule for that item.
- If cost uncertainty is still high, keep the price in draft status and do not publish yet.

### Pricing Strategy 1 (Current Method) — Total-Cost Guardrail Pricing

- Use the current total-cost method as an advisory guardrail when labor-inclusive inputs are available.
- Calculate `total_unit_cost` using materials, labor, delivery/shipping impact, platform fees, and other relevant allowances.
- Calculate the minimum guardrail-compliant price as the greater of:
  - `total_unit_cost / 0.60` to preserve the **>= 40%** gross-margin floor
  - `total_unit_cost + applicable profit floor`
- If live labor-inclusive inputs are missing, record Strategy 1 as a pending note. Missing Strategy 1 alone does not block pricing approval unless the operator explicitly chooses to enforce it for that item.

### Pricing Strategy 2 — Materials at 30% of Finished Price

- Use the default pricing strategy based on materials being **30% of the finished price**.
- Define `materials_cost_total` as materials subtotal plus hardware and consumables that belong in the physical build.
- Calculate the materials-based price as:
  - `materials_cost_total / 0.30`
- When reverse-checking an existing target/list price, calculate:
  - `materials_cost_total / finished_price`
- If the material share is above **30%**, flag the price as weak or needing review.

### Dual-Strategy Pricing Rule

- Use Strategy 2 (`materials_cost_total / 0.30`) as the default pricing baseline unless the operator explicitly states otherwise.
- For every existing target price or listing price, reverse-check:
  - Strategy 2 compliance against the 30%-materials benchmark
  - Strategy 1 compliance against gross-margin and profit-floor rules when live labor-inclusive inputs exist
- If Strategy 1 cannot be calculated yet, keep its status as a note and continue pricing review from the available Strategy 2/materials benchmark.
- If Strategy 1 differs from Strategy 2 by more than **15%** in either direction, flag the variance and require an explicit operator price choice before treating pricing as final.
- A price should not be treated as final pricing until the available pricing basis has been shown, any missing Strategy 1 note is visible, and the chosen price is explicitly approved.

### Initial Profit Rule (Starter)

- Minimum target gross margin: **>= 40%** unless explicitly approved.
- Under the current pricing policy, this remains a warning/reference guardrail unless the operator explicitly chooses to enforce Strategy 1 or another stricter pricing rule for the item.

### Starter Minimum Profit Floors (Use Until Product-Specific Rules Replace Them)

- Small decor / small shippable items: **>= $25 profit per unit**
- Medium planters / garden items: **>= $40 profit per unit**
- Raised beds / larger local-delivery items: **>= $75 profit per unit**
- Larger furniture builds: **>= $100 profit per unit**

If a product does not clearly fit a category yet, use the more conservative floor or mark the product **Hold** pending review in [30_products/](30_products/).

These starter profit floors remain important warning signals, but they do not automatically override the default 30%-materials pricing baseline unless the operator says otherwise.

## Shipping and Delivery Guardrails

- Local delivery/pickup-first for large or heavy items.
- Only pursue shipping when packaging cost, damage risk, and shipping fees still preserve margin.
- Etsy focus is limited to small, shippable products with clear fulfillment practicality.

### Delivery Limits (Starter Defaults)

- Local delivery radius default: **up to 25 miles** from base area unless priced with a delivery fee.
- Deliveries beyond default radius require explicit fee and schedule confirmation.
- No same-day delivery promises unless inventory is already complete and transport is available.

## Ad Spend Rules

- No ad spend on unproven products.
- Ads allowed only after organic proof (messages, saves, sales, or consistent high-intent engagement).
- Start with tiny-budget tests and pre-defined stop rules.
- Escalate spend only if results exceed baseline thresholds.
