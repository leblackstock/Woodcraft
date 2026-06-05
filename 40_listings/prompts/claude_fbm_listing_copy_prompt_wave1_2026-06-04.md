# Claude FBM Listing Copy Prompt — Wave 1

Date created: 2026-06-04
Generator template: `40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v1.0.md`
Status: Ready to paste into Claude when Lauren wants the Wave 1 listing copy pass
Listing copy owner: Claude
Image text owner: GPT/Codex prep
Voice source: `00_brand/VOICE.md`
Voice mode: Marketplace

This prompt requests final Facebook Marketplace listing titles and descriptions only. It does not request image text, captions, social copy, or publish approval.

Copy only the fenced `text` block into Claude. The surrounding repository metadata is internal provenance; the fenced prompt is standalone.

```text
You are writing final Facebook Marketplace listing copy for Drakkar Designs.

Use only the approved facts below. Do not invent dimensions, materials, lead times, discounts, included items, availability, delivery terms, guarantees, or product claims.

Write in the Drakkar voice:
- use Marketplace Mode: direct, practical, factual, and easy to scan
- lead with the product and buyer-relevant details
- plainspoken
- specific
- local
- unfussy
- no first person
- use short, confident sentences and restraint instead of hype
- use "cedar" when cedar is true
- no wholesale or partner terms
- no fake luxury language

Avoid these words/claims unless explicitly allowed by the facts:
- artisan
- artisanal
- curated
- luxury
- sustainable
- eco-friendly
- bespoke
- heirloom
- handcrafted
- Net 30
- MOQ
- partner terms

Note: "premium" may be used only when describing a material grade, not as a general quality claim.

Return one clearly separated block per listing.

For each listing, return only:
- listing_id
- listing_title
- listing_description

Do not include commentary, strategy notes, image text, captions, hashtags, or alternate options unless a listing is blocked.

If a listing is blocked, return only:
- listing_id
- status: BLOCKED
- missing_info

Global approved facts:
- Channel: Facebook Marketplace
- Business: Drakkar Designs
- Brand context: a small local Georgia cedar shop; keep the work and buyer-relevant details ahead of brand storytelling
- Customer-facing location wording: use locally in Georgia; avoid repeating the exact city unless pickup logistics require it
- Product line: cedar planters, raised beds, and garden pieces
- Build model: made to order
- Delivery wording: pickup or local delivery by arrangement
- Lead-time wording: built to order; lead time provided when order is placed
- Retail means the retail catalog price
- FB Marketplace price means the Marketplace listing price from the partner catalog/order packet
- Custom sizes are by quote where applicable
- Catalog SKU images are approved for FBM use, but do not write copy that implies a fresh finished build photo or current inventory unless the listing facts say so

Listing 1:
- listing_id: list_marketplace_master_catalog_001
- product_name: Handmade Cedar Planters, Raised Beds & Garden Decor
- listing_goal: broad search-capture listing for catalog items
- listing_price: $20, using the lowest FBM catalog price from SKU Q
- product_scope: handmade cedar planters, raised beds, and garden pieces
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- customization: custom sizing/finish by quote where available
- important note: explain that prices vary by item; do not imply all items cost $20

Listing 2:
- listing_id: list_marketplace_classic_square_planter_001
- product_name: Classic Square Cedar Planter
- sku: A
- retail_price: $80
- fb_marketplace_price: $40
- size: 16 x 16 x 16 in
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- customization: finish or sizing requests by quote where practical

Listing 3:
- listing_id: list_marketplace_cedar_planter_trio_set_001
- product_name: Cedar Planter Trio Set
- sku: ABC
- retail_price: $220
- fb_marketplace_price: $110
- set_contents: tall, classic, and small square cedar planters
- bundle_note: $110 is intentionally $20 below the realistic separate FBM total of A $40 + B $30 + C $60 = $130
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- important note: you may mention the set price plainly, but do not overdo discount language

Listing 4:
- listing_id: list_marketplace_raised_bed_001
- product_name: Cedar Raised Garden Bed
- sku: K
- retail_price: $480
- fb_marketplace_price: $240
- featured_size: 72 x 36 x 18 in
- custom_sizes: by quote; do not enumerate other sizes
- material: Western red cedar unless otherwise noted
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- important note: this listing is for the featured size; do not imply every custom size is $240

Before returning the copy, silently check that every statement is supported by the supplied facts, every listing includes all three requested fields, prices and sizes match the correct listing, and none of the banned wording appears.
```
