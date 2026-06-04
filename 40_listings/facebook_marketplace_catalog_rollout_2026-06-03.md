# Facebook Marketplace Catalog Rollout Workflow

Date updated: 2026-06-04
Status: Active workflow hub
Channel: Facebook Marketplace
Catalog source of truth: `20_research/catalog_exports/2026-06-03/`
Brand asset source of truth: `00_brand/`
Original source plan: `20_research/facebook_marketplace_catalog_rollout_plan_2026-06-03.md`

Use this file first. It is the operating map for turning the Drakkar Designs catalog into Facebook Marketplace listings.

## Workflow In One Pass

1. Pick the next wave/SKU from the rollout table.
2. Confirm catalog facts: product name, size/spec, retail price, FBM price, and approved catalog image.
3. Generate images manually in ChatGPT Image 2 from the active prompt pack or generator.
4. Prepare or update the listing record in `40_listings/`.
5. Run the Claude final-copy pass from approved facts only.
6. Paste Claude output back into the listing record.
7. Get final operator approval, then manually post to Facebook Marketplace.

## Current Files

| Need | File |
| --- | --- |
| This workflow hub | `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md` |
| Brand assets for graphics, prompts, and photos | `00_brand/` |
| Image sequence and per-SKU shot plan | `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md` |
| Active image prompt generator | `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v1.1.md` |
| Wave 1 image prompt pack | `40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md` |
| Visual color/style reference | `40_listings/prompts/fbm_image_visual_style_reference_2026-06-04.md` |
| Claude copy generator | `40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v1.0.md` |
| Wave 1 paste-ready Claude prompt | `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md` |
| Wave 1 Claude prep facts | `40_listings/claude_handoff_prep_wave1_fbm_catalog_2026-06-04.md` |

## Non-Negotiables

- Catalog facts win for this rollout: SKU names, specs, retail prices, FBM prices, and catalog images come from `20_research/catalog_exports/2026-06-03/`.
- Current brand assets, logos, palette notes, and approved product photos live in `00_brand/`.
- `Retail` means the retail catalog price.
- `FB Marketplace price` means the wholesale price from the partner catalog/order packet.
- All saved catalog SKU images are approved for FBM use.
- Final customer-facing listing prose belongs to Claude.
- GPT/Codex may prepare facts, workflow state, image prompts, and factual in-image text.
- Do not mark anything `publish_ready: Yes` until Claude output is pasted back, integrated, and final operator approval is recorded.

## Image Defaults

Default SKU image pack:

1. Lifestyle hero, no text overlay
2. Clean/empty product image, no text overlay, defines what is included
3. Price card
4. Size/context photo
5. Use-case photo
6. Detail/craftsmanship photo
7. Dimensions/details graphic
8. Final ordering graphic

Use 10 images only when the SKU needs it:

7. Support/variation photo, no text overlay
8. Dimensions/details graphic
9. Important details graphic
10. Final ordering graphic

Image prompt rules:

- Use ChatGPT Image 2 manually.
- Review mode is by exception; do not ask for approval on every prompt.
- Text-bearing image prompts are allowed.
- Filename fields are required for every image prompt.
- Do not put SKU letters/numbers inside generated images.
- Do not repeat the same photo with different flowers. Change the buyer question and the composition.
- Use the catalog color palette; not every image has to be dark.
- Use `Built locally in Georgia`, not repeated exact-city wording.
- Use `Lead time available by request` in compact image graphics.
- Use `Pickup or local delivery available` in image graphics.
- Do not include deposit terms.

## Listing Copy Defaults

Claude/listing prose should use:

- `pickup or local delivery by arrangement`
- `built to order; lead time provided when order is placed`
- custom sizes/finishes by quote only when supported by the SKU facts

Claude/listing prose should avoid:

- wholesale or partner terms
- unsupported availability or inventory claims
- unsupported discount framing
- exact city repetition unless pickup logistics require it

## Known SKU Exceptions

- ABC: $110 FBM price is intentionally $20 below the realistic separate FBM total of A $40 + B $30 + C $60 = $130.
- B: $30 FBM price was allowed to pass with review-later notes.
- C: $60 FBM price was allowed to pass with review-later notes.
- E: decorative planter only; do not imply it is for sitting.
- J: clean image should show the included structure; do not imply a mailbox is included unless later approved.
- K: use the featured 72 x 36 x 18 in size; other sizes are by quote and do not need to be enumerated now.
- Q: do not add a default flowers-not-included image disclaimer; the clean/empty image defines what is included.
- TT: includes three standard 4-inch clay pots.

## Wave Status

| Wave | Listings | Current Action |
| ---: | --- | --- |
| 1 | Master catalog; A; ABC; K | Generate/review Wave 1 images, then run Claude copy pass. |
| 2 | B; C; G; H | Create Wave 2 image prompt pack after Wave 1 flow feels good. |
| 3 | F; N; P; M | Validate pricing/cost notes, then create prompt pack. |
| 4 | D; J; E; TT; Q; PS | Validate pricing/cost notes, then create prompt pack. |

## SKU Rollout Map

| SKU | Product | Product Record | Retail | FBM Price | Image | Wave | Status | Next Action |
| --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |
| A | Classic Square Cedar Planter | `30_products/prod_cedar_three_picket_planter_001.md` | $80 | $40 | `00_brand/photos/planter-a.png` | 1 | Image prompt ready; Claude prompt ready | Generate/review images, then run Claude batch. |
| ABC | Cedar Planter Trio Set | `30_products/prod_cedar_trio_planter_box_set_001.md` | $220 | $110 | `00_brand/photos/planter-abc.png` | 1 | Image prompt ready; Claude prompt ready | Generate/review images, then run Claude batch. |
| B | Small Square Cedar Planter | `30_products/prod_cedar_petite_planter_box_111113_001.md` | $60 | $30 | `00_brand/photos/planter-b.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack; revisit price later. |
| C | Tall Square Cedar Planter | `30_products/prod_cedar_tall_square_planter_161625_001.md` | $120 | $60 | `00_brand/photos/planter-c.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack; revisit price later. |
| D | Cedar Post Planter Box | `30_products/prod_cedar_post_planter_box_001.md` | $220 | $110 | `00_brand/photos/planter-d.png` | 4 | Product mapped; media approved | Validate cost/pricing. |
| E | Mini Adirondack Cedar Planter | `30_products/prod_cedar_bench_planter_001.md` | $120 | $60 | `00_brand/photos/planter-e.png` | 4 | Product synced; media approved | Validate cost/pricing. |
| F | Tiered Cedar Pyramid Planter | `30_products/prod_cedar_pyramid_planter_001.md` | $320 | $160 | `00_brand/photos/planter-f.png` | 3 | Product mapped; media approved | Validate cost/pricing. |
| G | Long Rectangle Cedar Planter | `30_products/prod_cedar_long_planter_box_46in_001.md` | $260 | $130 | `00_brand/photos/planter-g.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack. |
| H | Tall Cedar Planter w/ Shelf | `30_products/prod_cedar_tall_rectangular_planter_461632_001.md` | $320 | $160 | `00_brand/photos/planter-h.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack. |
| J | Mailbox Post Cedar Planter | `30_products/prod_cedar_mailbox_post_planter_001.md` | $240 | $120 | `00_brand/photos/planter-j.png` | 4 | Product mapped; media approved | Validate cost/pricing. |
| K | Cedar Raised Garden Bed | `30_products/prod_cedar_raised_bed_001.md` | $480 | $240 | `00_brand/photos/planter-k.png` | 1 | Image prompt ready; Claude prompt ready | Generate/review images, then run Claude batch. |
| M | Small Tapered Cedar Planter | `30_products/prod_cedar_tapered_planter_box_001.md` | $100 | $50 | `00_brand/photos/planter-m.png` | 3 | Product mapped; media approved | Validate cost/pricing. |
| N | Three-Tier Cedar Planter | `30_products/prod_cedar_three_tier_planter_001.md` | $240 | $120 | `00_brand/photos/planter-n.png` | 3 | Product mapped; media approved | Validate cost/pricing. |
| P | Tall Patio Planter Box | `30_products/prod_cedar_wide_planter_box_262812_001.md` | $320 | $160 | `00_brand/photos/planter-p.png` | 3 | Product synced; media approved | Validate cost/pricing. |
| PS | Wooden Plant Stand | `30_products/prod_cedar_plant_stand_001.md` | $70 | $35 | `00_brand/photos/planter-ps.png` | 4 | Product mapped; media approved | Validate cost/pricing. |
| Q | Mini Cedar Cube Planter | `30_products/prod_cedar_one_picket_planter_001.md` | $40 | $20 | `00_brand/photos/planter-q.png` | 4 | Product synced; media approved | Validate cost/pricing. |
| TT | 3-Pot Tabletop Herb Planter | `30_products/prod_cedar_tabletop_plant_holder_001.md` | $60 | $30 | `00_brand/photos/planter-tt.png` | 4 | Product mapped; media approved | Validate cost/pricing. |

## Next Three Actions

1. Generate Wave 1 images from `40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md`.
2. If Wave 1 images look good, paste `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md` into Claude.
3. After Claude output is pasted back, update the four Wave 1 listing records and ask for final manual publish approval.
