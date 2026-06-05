# Facebook Marketplace Catalog Rollout Plan

Date saved: 2026-06-03
Source: Operator-provided Marketplace planning note
Status: Internal planning reference only
Related catalog artifacts: `20_research/catalog_exports/2026-06-03/`
Workflow tracker: `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`
Brand asset source of truth: `00_brand/`

This document captures the original working plan for a broader Facebook Marketplace catalog rollout. It is not final customer-facing copy. Final listing titles, descriptions, captions, promotional blurbs, calls to action, and reply copy must still pass the Claude final-copy gate before publish approval. Factual in-image text follows the active review-by-exception image-prompt workflow.

Current execution note: this is the original research plan. The workflow tracker at `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`, the active prompt generators, `00_brand/`, and `80_templates/standalone_external_prompt_checklist.md` supersede this note wherever current rules differ. Use repository paths only for internal preparation; every prompt delivered outside the repository must inline its relevant facts, brand direction, literal text, constraints, output requirements, quality criteria, and failure behavior.

Source-of-truth rule: for this Facebook Marketplace catalog rollout, the saved catalog artifacts are the source of truth for catalog-facing SKU names, specs, retail prices, and FB Marketplace prices. Older repo product specs should be reconciled to the catalog before listing files are created.

Brand asset rule: active Drakkar-specific logos, approved catalog photos, palette notes, graphics, HTML/template styling, and generated-visual references should come from `00_brand/`; the catalog export folder remains provenance.

Image rule: every catalog SKU has a saved catalog image. Listing workflow should treat catalog images as available assets, then approve and label them under the media-truth rules before publishing.

## Save Location Rationale

This belongs in `20_research/` because it is a channel/listing strategy reference and SKU rollout plan. It should inform future listing records in `40_listings/`, but it should not itself become a publishable listing asset.

Use this note as the source for:

- Marketplace listing batch planning
- SKU-by-SKU image planning
- retail-vs-wholesale Marketplace price review
- Claude handoff preparation
- future updates to `07_LISTING_AND_CONTENT_WORKFLOW.md`, if the operator approves a workflow change

## Marketplace Listing Structure

Create these listing types over time:

1. Master catalog listing
2. Category listings
3. Individual SKU listings

### Master Catalog Listing

- Purpose: catch broad Marketplace searches.
- Draft title concept: Handmade Cedar Planters, Raised Beds & Garden Decor, Built to Order
- Draft price logic: use the lowest item price, likely `$20`, then explain item-specific pricing in the description.
- Copy status: `[[CLAUDE_FINAL_COPY_REQUIRED]]`

### Category Listings

Potential category-level listings:

- cedar planters
- raised beds
- post/mailbox planters
- tiered planters
- small gifts/accessories

### Individual SKU Listings

Create one listing per SKU:

- A
- ABC
- B
- C
- D
- E
- F
- G
- H
- J
- K
- M
- N
- P
- PS
- Q
- TT

Operator pricing decision:

- FB Marketplace listing price = wholesale price from the partner catalog/order packet
- If a listing, price graphic, or Claude handoff says `Retail`, that number must be the retail catalog price
- Show retail price and FB Marketplace wholesale price only after pricing is approved and customer-facing copy clears the Claude gate

## Product Truth Notes

The operator note frames these as built-to-order cedar garden goods from Lovejoy, Georgia, with custom sizing/finish options and lead times confirmed per order.

Before any listing becomes publish-ready, each SKU still needs the normal repo workflow checks:

- product record exists or is created in `30_products/`
- `build_model` is truthful
- standard spec or approved dimensions are locked
- cost sheet or cost note is linked
- pricing is reviewed against the repo pricing rules
- lead time and delivery/pickup terms are explicit
- media truth is recorded
- Claude final-copy gate is complete
- `publish_ready: Yes`

K size note: the Cedar Raised Garden Bed has many possible sizes. The catalog-shown `72 x 36 x 18 in` size is the featured size for the rollout; other sizes are handled by quote and do not need to be enumerated now.

## Image Set Standard

Use 6 to 8 useful images per listing. Avoid filling the listing with redundant images.

Recommended image order:

1. Lifestyle hero image
2. Clean product image
3. Size/context image
4. Detail shot
5. Variation image
6. Simple price graphic
7. Built-to-order graphic
8. Catalog/order graphic

### Image Requirements

Lifestyle hero image:

- porch, garden, patio, or other natural use setting
- first image in the listing
- no heavy text

Clean product image:

- white or simple background
- shows the actual shape clearly

Size/context image:

- product beside a door, porch rail, plant pot, watering can, hand, or similar scale reference

Detail shot:

- cedar grain
- corners
- brads/screws where truthful
- mitered rim where applicable
- shelf, posts, or other defining product detail

Variation image:

- unfinished cedar
- stained
- clear coat
- painted
- maker mark

Simple price graphic:

- show retail price and FB Marketplace wholesale price only after pricing approval
- follow the Marketplace guidance in `00_brand/COLOR_PALETTE.md`, `00_brand/TEXT_STYLE_RULES.md`, and `00_brand/VISUAL_STYLE.md`
- follow the active tracker and image-prompt generator for factual graphic-text and approval rules

Built-to-order graphic:

- built locally in Georgia
- custom sizing available
- follow the active tracker and image-prompt generator for factual graphic-text and approval rules

Catalog/order graphic:

- message-to-order instruction
- follow the active tracker and image-prompt generator for factual graphic-text and approval rules

## Retail vs FB Marketplace Wholesale Pricing Draft

These values are operator-provided draft inputs and must be reconciled against current product records, cost sheets, and pricing guardrails before final listing approval.

| SKU | Product | Retail | FB Marketplace Wholesale |
| --- | --- | ---: | ---: |
| A | Classic Square Cedar Planter | $80 | $40 |
| ABC | Cedar Planter Trio Set | $220 | $110 |
| B | Small Square Cedar Planter | $60 | $30 |
| C | Tall Square Cedar Planter | $120 | $60 |
| D | Cedar Post Planter Box | $220 | $110 |
| E | Mini Adirondack Cedar Planter | $120 | $60 |
| F | Tiered Cedar Pyramid Planter | $320 | $160 |
| G | Long Rectangle Cedar Planter | $260 | $130 |
| H | Tall Cedar Planter w/ Shelf | $320 | $160 |
| J | Mailbox Post Cedar Planter | $240 | $120 |
| K | Cedar Raised Garden Bed | $480 | $240 |
| M | Small Tapered Cedar Planter | $100 | $50 |
| N | Three-Tier Cedar Planter | $240 | $120 |
| P | Tall Patio Planter Box | $320 | $160 |
| PS | Wooden Plant Stand | $70 | $35 |
| Q | Mini Cedar Cube Planter | $40 | $20 |
| TT | 3-Pot Tabletop Herb Planter | $60 | $30 |

Pricing source note from operator: FB Marketplace listing prices should use the wholesale prices from the partner catalog/order packet.

Bundle note:

- ABC is intentionally discounted by $20 from the realistic separate FB Marketplace total for A + B + C.
- Separate FB Marketplace total: A $40 + B $30 + C $60 = $130.
- ABC bundle FB Marketplace price: $110.
- If customer-facing copy says `Retail`, the retail bundle price is $220 from the retail catalog.

Label rule:

- `Retail` = retail catalog price
- `FB Marketplace price` = wholesale price from the partner catalog/order packet

Validation needed:

- confirm the saved catalog PDFs and source package in `20_research/catalog_exports/2026-06-03/` as the active pricing source
- map each SKU to an existing or new `30_products/` product record
- compare the FB Marketplace wholesale price against current cost sheet or cost note
- run Strategy 2 materials benchmark
- run Strategy 1 when labor-inclusive inputs exist
- record operator approval before the wholesale FB Marketplace listing price is treated as approved

## Description Formula For Claude Handoff

Use this as structured input only, not final listing copy.

Required facts:

- product name
- build location: Lovejoy, GA
- retail price, if the customer-facing copy will say `Retail`
- FB Marketplace price, using the wholesale price from the partner catalog/order packet
- material: Western red cedar, if true for that SKU
- build model: built one at a time / made to order, if true
- custom sizing/finish availability
- pickup location
- local delivery availability
- use cases
- buyer instruction: message with SKU/name and size or finish requests

Formula:

1. Opening hook: handmade cedar product, built to order in Lovejoy, GA
2. Price line: retail price, if used, and FB Marketplace price
3. Quick value bullets
4. Use-case line
5. Close: message with SKU/name and any size or finish requests

## Draft Posting Schedule

Post in waves to avoid posting too many similar listings at once.

### Day 1

- Master catalog listing
- A Classic Square
- ABC Trio Set
- K Raised Garden Bed

### Day 2

- B Small Square
- C Tall Square
- G Long Rectangle
- H Tall Planter w/ Shelf

### Day 3

- F Tiered Pyramid
- N Three-Tier
- P Tall Patio Planter
- M Small Tapered

### Day 4

- D Post Planter
- J Mailbox Post Planter
- E Mini Adirondack
- TT Herb Planter
- Q Mini Cube
- PS Plant Stand

## Title Style For Claude Handoff

Use simple searchable Marketplace title patterns. Final title text still requires Claude.

Preferred title ingredients:

- Handmade
- Cedar
- product type
- key dimensions when approved
- built to order

Example pattern for handoff only:

- Handmade Cedar Planter Box - 16x16x16 - Built to Order

Avoid vague titles that do not include product type or searchable material words.

## Workflow Conversion Notes

When this plan is converted into workflow steps, likely additions are:

1. Create a SKU-to-product-record map.
2. Create a Marketplace batch tracker for master, category, and SKU listings.
3. Add a media checklist field set for the 6 to 8 image standard.
4. Add a pricing-validation step for the retail-to-wholesale Marketplace table.
5. Generate Claude handoff packets only after approved facts are complete.
6. Keep posting waves manual until the first catalog rollout is proven.
