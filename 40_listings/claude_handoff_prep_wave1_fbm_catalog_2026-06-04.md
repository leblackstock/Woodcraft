# Claude Handoff Prep — Wave 1 FBM Catalog Listings

Status: Prep complete; paste-ready Claude prompt exists at `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md`
Batch tracker: `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`
Catalog artifacts: `20_research/catalog_exports/2026-06-03/`
Brand asset SOT: `00_brand/`
Voice guide: `20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/VOICE.md`

This file gathers approved facts for the Wave 1 Facebook Marketplace listings. Do not mark any listing `publish_ready: Yes` until Claude output is pasted back, integrated, and the operator gives final publish approval.

## Global Rules

- Channel: Facebook Marketplace
- Brand asset source of truth: `00_brand/`
- Customer-facing location wording: locally in Georgia; use exact pickup locality only if logistics require it
- Build model: Made to Order
- Delivery wording approved: pickup or local delivery by arrangement
- Lead-time wording approved where noted: built to order; lead time provided when order is placed
- `Retail` means the retail catalog price.
- `FB Marketplace price` means the wholesale price from the partner catalog/order packet.
- Custom sizes are by quote where applicable.
- Do not invent availability, lead times, delivery promises, finishes, included plants, soil, liners, or discounts.

## Tone And Guardrails

- tone source: follow `20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/VOICE.md`
- tone: plainspoken, specific, local, unfussy
- cta_goal: get the buyer to message with the SKU/name and any size, finish, or delivery questions
- voice rules to preserve:
  - small local Georgia cedar shop
  - no first person
  - use "cedar" when cedar is true
  - simple, practical, specific wording
  - short sentences
  - no wholesale/partner terms in customer-facing copy
- banned_claims_or_words: artisan, artisanal, curated, luxury, sustainable, eco-friendly, bespoke, heirloom, handcrafted, Net 30, MOQ, partner terms

## Listing: A

- listing_record: `40_listings/list_marketplace_classic_square_planter_001.md`
- product_record: `30_products/prod_cedar_three_picket_planter_001.md`
- product_name: Classic Square Cedar Planter
- sku: A
- retail_price: $80
- fb_marketplace_price: $40
- size: 16 x 16 x 16 in
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- media: operator-approved catalog image `00_brand/photos/planter-a.png`
- pricing_status: operator approved $40 FBM price on 2026-06-04

## Listing: ABC

- listing_record: `40_listings/list_marketplace_cedar_planter_trio_set_001.md`
- product_record: `30_products/prod_cedar_trio_planter_box_set_001.md`
- product_name: Cedar Planter Trio Set
- sku: ABC
- retail_price: $220
- fb_marketplace_price: $110
- bundle_note: $110 is intentionally $20 below the realistic separate FBM total of A $40 + B $30 + C $60 = $130
- set_contents: tall, classic, and small square cedar planters
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- media: operator-approved catalog image `00_brand/photos/planter-abc.png`
- pricing_status: operator approved $110 FBM bundle price on 2026-06-04

## Listing: K

- listing_record: `40_listings/list_marketplace_raised_bed_001.md`
- product_record: `30_products/prod_cedar_raised_bed_001.md`
- product_name: Cedar Raised Garden Bed
- sku: K
- retail_price: $480
- fb_marketplace_price: $240
- featured_size: 72 x 36 x 18 in
- custom_sizes: by quote; do not enumerate other sizes
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- media: operator-approved catalog image `00_brand/photos/planter-k.png`
- pricing_status: operator approved $240 FBM catalog price on 2026-06-04; advisory cost sheet clears Strategy 2 on assumption-based inputs

## Listing: Master Catalog

- listing_record: `40_listings/list_marketplace_master_catalog_001.md`
- product_record: multiple_catalog_skus
- listing_goal: broad search-capture listing for catalog items
- listing_price: $20, using lowest FBM catalog price from SKU Q
- product_scope: handmade cedar planters, raised beds, and garden pieces
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- customization: custom sizing/finish by quote where available
- media_status: all saved catalog SKU images approved for FBM use by Lauren on 2026-06-04; master image still needs operator choice if using cover/collage
- copy_note: explain that prices vary by item; do not imply all items cost $20

## Remaining Before Official Claude Pass

- Paste `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md` into Claude when ready.
- Paste Claude output back into the listing records, then record `claude_output_ref` and final operator publish approval before marking anything publish-ready.
