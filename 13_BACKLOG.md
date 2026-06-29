# 13 Backlog

Ordered next tasks after initial scaffold. Keep this list short, practical, and priority-driven.

## Now (Highest Priority)

1. Create the Wave 2 Facebook Marketplace image prompt pack for B, C, G, and H from their approved catalog references.
2. Run the Wave 2 pack for B first: generate and review B’s required listing-image set before moving one SKU at a time through C, G, and H.
3. Maintain the daily Facebook Page + Instagram brand-post cadence tracker: minimum one Facebook Page brand post and one Instagram brand/support post per America/New_York day in `50_content/social_post_cadence_tracker.md`.
4. After listing facts and timing are final, run the Claude final post-copy pass for the next Facebook Page support post and the Claude final caption pass for the next Instagram support post.
5. Build draft assumption-based cost sheets, labor assumptions, and verification packets for catalog products before advancing secondary products; capture receipt-backed actuals later through the post-build validation loop.
6. Capture required photo sets for approved catalog products: hero, angle, detail, and in-use shots with clear scale references.
7. Keep lower-priority imported, accessory, furniture, and non-catalog items in secondary/reference status until catalog-product work is complete.

## Not in Line Yet (After Catalog Products)

1. Resolve the bundled made-to-order approval packet for `prod_cedar_planter_box_001` using the locked standard spec plus approved draft pricing, labor, fulfillment, and media assumptions.
2. Advance `list_marketplace_planter_box_001.md` from prep-only status through its verification packet and Claude handoff using approved facts only.
3. Review `20_research/current_product_portfolio_triage.md` and resolve the remaining Cedar Planter Box 24x24x18 operator approval packet.

## Soon

1. Backfill `build_model`, `lead_time_estimate`, `media_truth_status`, and `media_provenance_note` on the active first-wave product and listing records, and mark any third-party images as reference-only.
2. Backfill active first-wave cost sheets, product records, and listing records to the updated pricing policy: Strategy 2 default baseline, both pricing calculations shown every time, and a warning whenever Strategy 1 differs by more than 15%.
3. After the first real made-to-order sale is completed, run one post-sale actuals capture pass (receipts, labor, finished dimensions, finished photos, repricing decision) and document the estimate-vs-actual delta.
4. Add starter research snapshots in [20_research/](20_research/) for local pricing, competitor positioning, and seasonal demand notes.
5. Expand [06_PRODUCT_DECISION_WORKFLOW.md](06_PRODUCT_DECISION_WORKFLOW.md) with a lightweight approval checklist if repeated product scoring starts drifting.
6. Create the first prompt pack defined in [10_PROMPTS_INDEX.md](10_PROMPTS_INDEX.md) with model-safe ownership:
   - GPT product scoring prompt
   - GPT weekly review synthesis prompt
   - Claude final Marketplace listing prompt pack derived from approved facts only
7. Define low-budget ad test thresholds in [70_ads/](70_ads/) and align them with [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md).
8. After 2–3 live verification runs, decide whether the workspace needs a dedicated raw-evidence intake template or whether the current packet/cost-sheet workflow is sufficient.
9. Convert additional imported guide records into listing candidates only after standard dimensions, labor timing, and plan/source truth are approved per the operator review.


## Later

1. Introduce semi-automated reminder/checklist workflow per [08_AUTOMATION_ROADMAP.md](08_AUTOMATION_ROADMAP.md).
2. Build structured weekly reporting roll-up from data model fields in [09_DATA_MODEL.md](09_DATA_MODEL.md).
3. Evaluate Etsy pilot listing process for one proven small shippable product.
4. Run first controlled Google Ads micro-test only after organic proof criteria are met.
5. Future maintenance: normalize legacy secondary-product schema in `30_products/` without inventing missing facts.

## Future Maintenance — Normalize legacy secondary-product schema in `30_products/`

- **Priority:** Medium
- **Status:** Not Started
- **Owner:** Lauren

### Objective
Normalize older non-first-wave product records so they more consistently match the current schema in `09_DATA_MODEL.md`, without inventing missing facts.

### Why this matters
The repo now operates in a mostly governance-aligned state, but some secondary legacy product records still lag on newer schema requirements, especially fields like `build_model` and newer pricing-governance structure.

### Scope
- Review older secondary product records in `30_products/`
- Backfill newer required fields only when directly supported by existing record truth
- Use truthful placeholders like `Pending` or `Blocked` where allowed
- Do not invent pricing, labor, media, or approval facts

### Success criteria
- Legacy secondary product records no longer create avoidable schema QA failures
- Newer required fields are present where safely supported
- Remaining unknowns are explicitly marked instead of guessed

### Not included
- No rewrite of customer-facing copy
- No forced approval-state changes
- No speculative pricing approval
- No folder restructuring unless separately approved
