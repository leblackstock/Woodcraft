# 06 Product Decision Workflow

Purpose: decide what to build/list next using lightweight evidence, not guesses.

## Workflow: Intake → Research → Score → Approve → Listing Queue

1. **Intake**
   - Capture idea in `30_products/` using template from [80_templates/product_candidate_template.md](80_templates/product_candidate_template.md).
2. **Research**
   - Gather local pricing and demand signals in [20_research/](20_research/).
3. **Score**
   - Apply scoring dimensions below.
4. **Approve / Reject / Hold**
   - Approve only if it clears business rules in [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md).
5. **Queue for Listing**
   - Move approved products into listing workflow in [07_LISTING_AND_CONTENT_WORKFLOW.md](07_LISTING_AND_CONTENT_WORKFLOW.md).

## Scoring Dimensions (1–5 each)

- **Demand Signal** — evidence of buyer interest locally.
- **Margin Potential** — projected profitability after true costs.
- **Build Complexity** — lower complexity scores higher.
- **Photo/Listability** — can this be presented clearly and attractively?
- **Fulfillment Practicality** — realistic lead time, delivery/shipping viability.
- **Repeatability** — can this be produced consistently?

Record all six component scores plus `score_total` in the product record.

## Simple Decision Rubric

- **Approve:** total score >= 22 and no hard rule conflicts.
- **Hold:** total score 17–21 or key unknowns unresolved.
- **Reject:** total score <= 16 or fails hard business guardrails.

## Questions That Must Be Answered Before Building/Listing

1. Who is the likely buyer and use case?
2. What are comparable local prices?
3. What is estimated unit cost and target price?
4. Does it meet margin/profit guardrails?
5. Is fulfillment realistic with current capacity?
6. Can listing photos/content be produced with current setup?
7. Is this likely repeatable, not just a one-off novelty?
