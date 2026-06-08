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

Write the strongest natural Facebook Marketplace listing you can for each listing below. Do not treat this as a form-fill task. Use the listing type, facts, buyer context, and tone to decide the best title and description structure for a local Marketplace buyer.

Use only the approved facts below. Do not invent dimensions, materials, lead times, discounts, included items, availability, delivery price, guarantees, or product claims.

Tone:
- practical, local, clear, warm, and unfussy
- direct and easy to scan
- sounds like a real person selling useful cedar garden pieces, not a catalog sheet, not ad copy, and not luxury branding
- short, confident sentences are good, but do not make the copy choppy
- use "cedar" when cedar is true

Rules:
- Do not mention retail price or discounts unless the listing facts explicitly say to do that.
- Write prices as plain customer-facing prices, without Marketplace labels.
- Do not force every fact into the title.
- Do not use the phrase "unless otherwise noted" in customer copy.
- Use no em dashes or en dashes; regular hyphens are okay when needed.
- Avoid AI-isms and common AI tells.
- Avoid hype words like artisan, artisanal, curated, luxury, sustainable, eco-friendly, bespoke, heirloom, and handcrafted.
- Do not use wholesale or partner terms such as Net 30, MOQ, or partner pricing.

For each listing, give one title and one description. Keep the product name visible enough that the listing can be matched back to the facts. No notes, no options, no strategy commentary, no image text, no captions, and no hashtags.

If a listing is missing required information, mark that listing as BLOCKED and list only the missing information.

Global approved facts:
- Channel: Facebook Marketplace
- Business: Drakkar Designs
- Brand context: a small local Georgia woodshop; keep the work and buyer-relevant details ahead of brand storytelling
- Customer-facing location wording: use locally in Georgia; avoid repeating the exact city unless pickup logistics require it
- Product line: cedar planters, raised beds, and garden pieces
- Build model: made to order
- Delivery wording: pickup or local delivery by arrangement
- Lead-time wording: built to order; lead time provided when order is placed
- Retail catalog prices are internal context only; do not include retail comparisons unless Lauren explicitly asks for them
- Listing prices are the plain customer-facing prices from the partner catalog/order packet; write them as prices without `Marketplace` labels
- Custom sizes are by quote where applicable
- Catalog SKU images are approved for FBM use, but do not write copy that implies a fresh finished build photo or current inventory unless the listing facts say so

Listing 1:
- listing_id: list_marketplace_master_catalog_001
- product_name: Handmade Cedar Planters, Raised Beds & Garden Decor
- listing_goal: broad search-capture listing for catalog items
- price: starts at $20; prices vary by item
- product_scope: handmade cedar planters, raised beds, and garden pieces
- material: Western red cedar
- buyer_context: someone browsing local Marketplace for cedar planters, raised beds, or garden pieces and needing to understand that this is a catalog-style listing with item prices varying
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- customization: custom sizing/finish by quote where available
- important note: explain that prices vary by item; do not imply all items cost $20

Listing 2:
- listing_id: list_marketplace_classic_square_planter_001
- product_name: Classic Square Cedar Planter
- sku: A
- price: $40
- size: 16 x 16 x 16 in
- material: Western red cedar
- buyer_context: porch, patio, deck, front step, herb planter, flower planter, or small garden container
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- customization: finish or sizing requests by quote where practical

Listing 3:
- listing_id: list_marketplace_cedar_planter_trio_set_001
- product_name: Cedar Planter Trio Set
- sku: ABC
- price: $110
- set_contents: tall, classic, and small square cedar planters
- material: Western red cedar
- buyer_context: coordinated porch, patio, deck, or entry setup where the three planter sizes can be used together
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- important note: mention the set price plainly; do not use discount language

Listing 4:
- listing_id: list_marketplace_raised_bed_001
- product_name: Cedar Raised Garden Bed
- sku: K
- price: $240
- featured_size: 72 x 36 x 18 in
- custom_sizes: by quote; do not enumerate other sizes
- material: Western red cedar
- buyer_context: backyard, side-yard, or garden-edge raised bed for herbs, vegetables, or simple planting
- fulfillment: pickup or local delivery by arrangement
- lead_time: built to order; lead time provided when order is placed
- important note: this listing is for the featured size; do not imply every custom size is $240

Before answering, silently write several internal versions for each listing, analyze them for truthfulness, buyer clarity, voice fit, specificity, natural rhythm, correct prices and sizes, banned wording, dash tells, and AI-isms, then write a stronger final version as the visible output.
```
