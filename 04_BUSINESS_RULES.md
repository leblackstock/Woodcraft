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

- Every product must have a simple cost sheet before listing.
- Include materials, labor time, delivery/shipping impact, and platform fees when relevant.
- Run both approved pricing strategies whenever proposing a price or reviewing an already-set price.
- Do not price below target profit floor.
- If price needed to sell is below profit floor, pause or redesign product.
- If cost uncertainty is still high, keep the price in draft status and do not publish yet.

### Pricing Strategy 1 (Current Method) — Total-Cost Guardrail Pricing

- Use the current total-cost method as the first required pricing strategy.
- Calculate `total_unit_cost` using materials, labor, delivery/shipping impact, platform fees, and other relevant allowances.
- Calculate the minimum guardrail-compliant price as the greater of:
  - `total_unit_cost / 0.60` to preserve the **>= 40%** gross-margin floor
  - `total_unit_cost + applicable profit floor`
- This is the current baseline pricing method already used in the workspace.

### Pricing Strategy 2 — Materials at 30% of Finished Price

- Use a second required pricing strategy based on materials being **30% of the finished price**.
- Define `materials_cost_total` as materials subtotal plus hardware and consumables that belong in the physical build.
- Calculate the materials-based price as:
  - `materials_cost_total / 0.30`
- When reverse-checking an existing target/list price, calculate:
  - `materials_cost_total / finished_price`
- If the material share is above **30%**, flag the price as weak or needing review.

### Dual-Strategy Pricing Rule

- For every new draft price, calculate both Strategy 1 and Strategy 2.
- Use the higher resulting price as the default pricing baseline unless an explicit human override is recorded.
- For every existing target price or listing price, reverse-check both:
  - Strategy 1 compliance against gross-margin and profit-floor rules
  - Strategy 2 compliance against the 30%-materials benchmark
- A price should not be treated as good pricing unless both strategies pass or a documented exception is approved.

### Initial Profit Rule (Starter)

- Minimum target gross margin: **>= 40%** unless explicitly approved.

### Starter Minimum Profit Floors (Use Until Product-Specific Rules Replace Them)

- Small decor / small shippable items: **>= $25 profit per unit**
- Medium planters / garden items: **>= $40 profit per unit**
- Raised beds / larger local-delivery items: **>= $75 profit per unit**
- Larger furniture builds: **>= $100 profit per unit**

If a product does not clearly fit a category yet, use the more conservative floor or mark the product **Hold** pending review in [30_products/](30_products/).

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

## Do Not Pursue a Product If

- Build complexity is high and margin is weak.
- Delivery/logistics make fulfillment unreliable.
- Price needed for profit is far above local market willingness.
- Product cannot be photographed/listed well with current capabilities.
- Repeatability is low and customization burden is excessive.

## Risk Rules

- Avoid promises on lead times without production confidence.
- Avoid one-off custom commitments that disrupt core workflow.
- Keep manual approval for final pricing, publishing, and ad launch decisions.

## Assumptions vs Confirmed Facts

### Current Assumptions (Need Validation)

- Facebook Marketplace is strongest near-term channel for local sales.
- Core cedar product categories used in this workspace (decor, planters, raised beds, and outdoor furniture) are viable primary focus.
- Low-budget approach requires mostly organic + process improvements first.

### Materials Assumptions (Need Validation)

- Cedar remains primary material due to outdoor durability and positioning value.
- Material price volatility can materially affect margin and may require monthly price updates.
- Standard fastener/finish choices should prioritize weather resistance over lowest upfront cost.

### Confirmed Facts (Update Over Time)

- This workspace is markdown-first and process-first before heavy automation.
- Facebook Marketplace is the primary sales channel in the current operating strategy.
- Facebook Page and Instagram are support/trust channels, not primary sales channels.
- Google Ads are restricted to later-phase testing on proven products only.
- Human approval is required for final pricing, publishing, and ad launch decisions.

These are confirmed workspace operating decisions, not claims of proven market performance.
