# 06 Product Decision Workflow

Purpose: decide what to standardize, list, and build next using lightweight evidence, not guesses.

## Workflow: Intake → Research → Score → Approve → Listing-First Queue

1. **Intake**
   - Capture idea in `30_products/` using template from [80_templates/product_candidate_template.md](80_templates/product_candidate_template.md).
2. **Research**
   - Gather local pricing and demand signals in [20_research/](20_research/).
3. **Score**
   - Apply scoring dimensions below.
4. **Approve / Reject / Hold**
   - Approve only if it clears business rules in [04_BUSINESS_RULES.md](04_BUSINESS_RULES.md).
5. **Queue for Listing-First Prep**
   - Move approved products into listing workflow in [07_LISTING_AND_CONTENT_WORKFLOW.md](07_LISTING_AND_CONTENT_WORKFLOW.md).
   - A fresh build is not a universal prerequisite if the standard launch spec, estimated pricing, lead-time logic, delivery terms, and truthful media are ready.

## Final Bundled Operator Review (Before Listing-First Progression)

Before an approved product moves forward to listing progression, prepare one bundled operator-review block that confirms:

- product/spec confirmation
- build model confirmation (`build_model`)
- standard launch spec confirmation
- pricing confirmation when relevant
- dual pricing strategy review when relevant, including the default Strategy 2 baseline and any >15% Strategy 1 variance warning
- replacement/override confirmation when relevant
- estimated lead-time confirmation
- delivery/pickup terms confirmation
- media truth confirmation (`media_truth_status` and provenance note when needed)
- whether plans are available (`plans_available`)
- source confirmation when plans exist (`plans_source_ref` and, when applicable, `reference_source` / `reference_code`)

## Made-to-Order Listing-First Gate

A product may move toward listing prep before a fresh build exists only when all of the following are true:

- standard launch spec is locked
- plans/source truth is recorded
- dimensions/specs are locked from plan, reference, or standard spec
- estimated cost sheet exists
- estimated labor time exists
- made-to-order lead time is defined
- delivery/pickup terms are defined
- media used for listing is truthful under the media-governance rules in [07_LISTING_AND_CONTENT_WORKFLOW.md](07_LISTING_AND_CONTENT_WORKFLOW.md)

For `build_model: Made to Order`, locked standard-spec dimensions or approved plan/reference dimensions are valid pre-sale truth. Actual measured finished dimensions move to the post-build update loop unless the launch spec itself is still unresolved.

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

## Questions That Must Be Answered Before Listing-First Prep or Building

1. Who is the likely buyer and use case?
2. What are comparable local prices?
3. What is estimated unit cost and target price?
4. What do both pricing strategies show, and is Strategy 1 more than 15% different from the default Strategy 2 baseline?
   - current total-cost guardrail pricing
   - materials-at-30%-of-finished-price pricing
5. Is fulfillment realistic with current capacity, including truthful made-to-order lead time and delivery terms?
6. Can truthful listing media be prepared with current setup using owned real photos, owned AI-assisted images derived from owned photos, or clearly governed concept media?
7. Is this likely repeatable, not just a one-off novelty?
8. Are build plans available (`plans_available`), and if yes, is the real plan/reference source recorded (`plans_source_ref` plus source metadata where applicable)?
9. Is the standard launch spec locked tightly enough that pre-sale dimensions/specs can be stated without guessing?

## After First Sale / Build

After the first real made-to-order build is completed, update the product record and linked refs with:

- actual receipts
- actual labor time
- actual finished dimensions
- actual finished photos
- updated cost-sheet learnings
- keep / drop / reprice decision if needed
