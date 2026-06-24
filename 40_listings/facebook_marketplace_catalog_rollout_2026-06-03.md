# Facebook Marketplace Catalog Rollout Workflow

Date updated: 2026-06-21
Status: Active workflow hub
Channel: Facebook Marketplace
Catalog source of truth: `20_research/catalog_exports/2026-06-03/`
Brand asset source of truth: `00_brand/`
Original source plan: `20_research/facebook_marketplace_catalog_rollout_plan_2026-06-03.md`

Use this file first. It is the operating map for turning the Drakkar Designs catalog into Facebook Marketplace listings.

## Workflow In One Pass

1. Pick the next wave/SKU from the rollout table.
2. Confirm catalog facts: product name, size/spec, retail price, FBM price, and approved catalog image. For a custom configurable family without a catalog row, confirm the approved family and variant records instead.
3. Generate images manually in ChatGPT Image 2 from the active prompt pack or generator.
4. Prepare or update the listing record in `40_listings/`.
5. Run the Claude final-copy pass from approved facts only.
6. Paste Claude output back into the listing record.
7. Get final operator approval, then manually post to Facebook Marketplace.

## Current Files

| Need | File |
| --- | --- |
| This workflow hub | `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md` |
| Brand assets and identity guidance | `00_brand/` |
| Brand voice | `00_brand/VOICE.md` |
| Brand color palette | `00_brand/COLOR_PALETTE.md` |
| Brand text style | `00_brand/TEXT_STYLE_RULES.md` |
| Brand visual style | `00_brand/VISUAL_STYLE.md` |
| Standalone external-prompt checklist | `80_templates/standalone_external_prompt_checklist.md` |
| Variant-scope listing workflow | `40_listings/variant_scope_marketplace_listing_workflow.md` |
| Variant-scope clean-reference prompt generator | `40_listings/prompts/prompt_fbm_variant_scope_clean_reference_generator_v1.0.md` |
| Image sequence and per-SKU shot plan | `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md` |
| Active image prompt generator | `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v2.0.md` |
| Wave 1 image prompt pack | `40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md` |
| Wave 1.5 image prompt pack | `40_listings/prompts/fbm_image_prompt_pack_wave1_5_2026-06-10.md` |
| Claude copy generator | `40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md` |
| K focused sellability-first Claude prompt | `40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md` |
| Wave 1 paste-ready Claude prompt | `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md` |
| Wave 1 Claude prep facts | `40_listings/claude_handoff_prep_wave1_fbm_catalog_2026-06-04.md` |

## Non-Negotiables

- Catalog facts win for this rollout: SKU names, specs, retail prices, FBM prices, and catalog images come from `20_research/catalog_exports/2026-06-03/`.
- For a custom configurable family with no saved catalog row, the approved family record, included child-variant records, and linked listing record are the fact source. Do not invent a catalog price, retail label, or catalog image to fill that gap.
- Current brand assets and reusable identity guidance live in `00_brand/`.
- `Retail` means the retail catalog price.
- `FB Marketplace price` means the wholesale price from the partner catalog/order packet.
- Retail catalog prices and FB Marketplace price labels are internal pricing context only. Customer-facing FBM image graphics and Claude listing prose use the plain listing price unless Lauren explicitly asks for retail-comparison wording.
- All saved catalog SKU images are approved for FBM use.
- Final customer-facing listing prose belongs to Claude.
- GPT/Codex may prepare facts, workflow state, image prompts, and factual in-image text.
- Marketplace listing prose and factual in-image text use Marketplace Mode from `00_brand/VOICE.md` as a light guardrail. For FBM, optimize first for buyer response, skim clarity, price/size/use-case confidence, trust, and easy next action while keeping approved facts and banned-word rules intact.
- Visible FBM listing copy and factual image text should use `cedar`, not `Western red cedar`, unless Lauren explicitly requests the full material spec for that asset. Keep the full species wording in internal material/spec fields where useful for fact accuracy.
- Every image prompt and Claude prompt delivered outside this repository must pass `80_templates/standalone_external_prompt_checklist.md`. Use repository files during preparation, then inline all relevant facts, brand/voice/visual rules, literal text, constraints, attachment instructions, copy-shape or output requirements, and quality criteria. Claude final-copy prompts must also inline the negative style rules: no em dashes or en dashes in final output, regular hyphens are okay when needed, and no AI-isms or common AI tells. Claude final-copy prompts must instruct Claude to silently write several internal versions, analyze them, and then produce a stronger final version as the visible output. Resolve missing facts upstream before creating a Claude final-copy prompt.
- Do not mark anything `publish_ready: Yes` until Claude output is pasted back, integrated, and final operator approval is recorded.

## Image Defaults

Default SKU image pack:

1. Lifestyle hero, no text overlay
2. Clean/empty product image, no text overlay, defines what is included
3. Size/context photo
4. Use-case photo
5. Detail/craftsmanship photo
6. Price card
7. Dimensions/details graphic
8. Final ordering graphic

Use 10 images only when the SKU needs it:

1. Lifestyle hero, no text overlay
2. Clean/empty product image, no text overlay, defines what is included
3. Size/context photo
4. Use-case photo
5. Detail/craftsmanship photo
6. Support/variation photo, no text overlay
7. Price card
8. Dimensions/details graphic
9. Important details graphic, approved facts only
10. Final ordering graphic

Image prompt rules:

- Use ChatGPT Image 2 manually.
- Review mode is by exception; do not ask for approval on every prompt.
- Use the sellability-first v2.0 generator for new packs. Brand style, palette, and voice should support the listing, not outrank a stronger Marketplace thumbnail, clearer price/size proof, or easier buyer action.
- Text-bearing image prompts are allowed.
- Every delivered image prompt must be standalone when copied into an image model without repository access. Inline the necessary brand direction, exact palette values for graphics, typography direction, and literal in-image text.
- Copied image prompts should use direct positive instructions and exact text lines. Do not add internal repo labels, pricing-policy explanations, or long negative style-category lists the target model would not otherwise know.
- For FBM SKU or catalog listing prompt packs with approved catalog image(s), treat the approved catalog image(s) as required attachments for every delivered prompt in that listing's image set, including text graphics. The copied prompt's first line must be `Please see attached "[plain-language item being attached]"`.
- Exact product fidelity is always required for Facebook Marketplace listing images. Do not deliver or generate an FBM listing image prompt from text only; if the approved catalog image or required reference image is missing, stop and ask for the attachment.
- Filename fields are required for every image prompt.
- Do not put SKU letters/numbers inside generated images.
- Do not repeat the same photo with different flowers. Change the buyer question and the composition.
- Use `00_brand/COLOR_PALETTE.md`, `00_brand/TEXT_STYLE_RULES.md`, and `00_brand/VISUAL_STYLE.md`; follow the Marketplace text-style guidance for text-bearing graphics, and do not force every image to be dark.
- FBM price-card graphics use one plain selling-price line from the approved FBM price, plus the product or category name when useful. If the price applies only to a featured configuration, such as K's $240 raised-bed price, label it plainly as a featured-size/configuration price in the exact rendered text. For a non-bundle variant-scope listing with different approved option prices, use a clear option-and-price chart that lists only the variants in `variant_scope` and their exact approved prices. Copied prompts should specify the exact rendered text instead of explaining internal price-label exceptions.
- Use `Built locally in Georgia`, not repeated exact-city wording.
- Use `Lead time available by request` in compact image graphics.
- Use `Pickup or local delivery available` in image graphics.
- Do not include deposit terms.
- For every 8-image or 10-image pack, all real photographs occupy the leading positions in one continuous run and all composite text cards follow in one continuous run at the end. For eight images, Images 1 through 5 are photographs and Images 6 through 8 are price, dimensions/details, and final ordering cards. For ten images, Images 1 through 6 are photographs and Images 7 through 10 are price, dimensions/details, important details, and final ordering cards. The final ordering card is always last. If fewer usable photographs exist than lead slots, fill the available leading photo slots and leave the rest empty rather than moving a text card forward. For the ten-image important-details card, use only approved facts; if no approved fact justifies it, omit the card and run nine images with final ordering as Image 9.

## Listing Copy Defaults

Claude/listing prose prompts should be sellability-first creative briefs, not compliance worksheets. Give Claude the listing type, approved specs, buyer context, likely buyer objections, sales priorities, and only the voice guardrails needed for fact safety. Ask for the strongest Marketplace listing within the facts, optimized for click-through, search usefulness, skim clarity, trust, and an easy next action. Include the internal draft pass: Claude should silently write several sales-angle versions, score them, combine the best parts, and then produce a stronger final version as the visible output.

Claude/listing prose should use:

- `pickup or local delivery by arrangement`
- `built to order; lead time provided when order is placed`
- custom sizes/finishes by quote only when supported by the SKU facts
- the plain customer-facing price, without `Retail`, `Marketplace`, or discount labels unless Lauren explicitly asks for that framing
- `small local Georgia woodshop` when shop context is needed

Claude/listing prose should avoid:

- wholesale or partner terms
- unsupported availability or inventory claims
- unsupported discount framing
- exact city repetition unless pickup logistics require it
- rigid field-output scaffolding such as `listing_id`, `listing_title`, and `listing_description` unless the user explicitly needs machine-readable pasteback
- older shop wording that narrows the business to cedar only

## Known SKU Exceptions

- ABC: $110 FBM price is intentionally $20 below the realistic separate FBM total of A $40 + B $30 + C $60 = $130.
- B: $30 FBM price was allowed to pass with review-later notes.
- C: $60 FBM price was allowed to pass with review-later notes.
- E: decorative planter only; do not imply it is for sitting.
- F image surface rule: any F / Tiered Cedar Pyramid Planter image prompt or product-inset prompt must show the planter over soil, grass, garden bed ground, or yard/garden surface only. Do not place it on porch boards, decks, patios, concrete, pavers, indoor floors, showroom floors, or other hard-surface staging. Each tier is an open cedar frame/ring with no solid tray bottom. The dirt between tiers should look like dark, packed planting soil formed into compact sloped terraced banks between the cedar tier rings, visible in the open spaces between levels and continuing from one planting tier into the next as dark triangular soil banks behind the cedar boards and around the center supports. The soil should look settled and packed in place, not spilling, pouring, cascading, or falling loose.
- J: clean image should show the included structure; do not imply a mailbox is included unless later approved.
- K: the Cedar Raised Garden Bed is fully customizable by quote. Use the featured 72 x 36 x 18 in configuration for the current listing, and treat its $240 price and specs as featured-configuration facts only.
- K image surface rule: any K image prompt or product-inset prompt must show the raised bed over soil, grass, garden bed ground, or yard/garden surface only. Do not place it on porch boards, decks, patios, concrete, pavers, indoor floors, showroom floors, or other hard-surface staging.
- Q: do not add a default flowers-not-included image disclaimer; the clean/empty image defines what is included.
- TT: includes three standard 4-inch clay pots.

## Wave Status

| Wave | Listings | Current Action |
| ---: | --- | --- |
| 1 | Master catalog; A; ABC; K | A, ABC, and K are posted/completed. The prepared Master Catalog draft remains available, but it is not in the current catalog-product sequence. |
| 1.5 | F, T1, and T2 | F / Tiered Cedar Pyramid Planter posted 2026-06-10; T1 / Cedar Five-Finger Trellis posted 2026-06-11; T2 / Cedar Decorative Obelisk Trellis externally posted before screenshot evidence was supplied on 2026-06-22. Monitor all Wave 1.5 listing metrics. |
| Pre-2 | USA1-L-NAT — Wavy Flag Large; USA1-SML — Wavy Flag Small, Medium & Large | USA1-L-NAT was posted 2026-06-23; monitor its metrics. DEC-110 authorizes `USA1-L-NAT_wavy_wooden_american_flag_ref_clean-01.png` plus `USA1-SML_wavy_wooden_american_flag_ref_clean-01.png` as the paired fallback visual-reference set for Medium, Small, and USA1-SML Marketplace-image preparation. DEC-111 maps USA1-SML to a new three-size best thumbnail generated from those references as Image 1, reuses four proven USA1-L-NAT listing photos as Images 2–5, and creates three text-bearing scoped cards from the Large and/or SML reference as needed. First-build, factual, and publication gates remain. |
| 2 | B; C; G; H | Begins after USA1-SML prep: create the Wave 2 image prompt pack, then run B first before moving one SKU at a time through C, G, and H. |
| 3 | N; P; M | Validate pricing/cost notes, then create prompt pack. |
| 4 | D; J; E; TT; Q; PS | Validate pricing/cost notes, then create prompt pack. |

## Wave 1.5 Trellis Readiness Note

The following two trellises are independent Wave 1.5 products. T1 may also be offered as an add-on to any planter.

| Trellis SKU | Product | Product record | Draft spec | Draft cost note | Source note | Status |
| --- | --- | --- | --- | --- | --- | --- |
| T1 | Cedar Five-Finger Trellis | `30_products/prod_cedar_five_finger_trellis_001.md` | `30_products/spec_cedar_five_finger_trellis_standard.md` | `30_products/cost_cedar_five_finger_trellis_001.md` | `20_research/trellis_wave_1_5_source_notes_2026-06-09.md` | Published 2026-06-11; FBM listing completed; $40 price approved; offered standalone and as add-on to any planter; standalone clean ref `T1_cedar_five_finger_trellis_ref_clean-01.png` approved; dimensions 70 in H x 32 in W x 2.25 in thick; final live title/description and final posted media set not duplicated in repo |
| T2 | Cedar Decorative Obelisk Trellis | `30_products/prod_cedar_decorative_obelisk_trellis_001.md` | `30_products/spec_cedar_decorative_obelisk_trellis_standard.md` | `30_products/cost_cedar_decorative_obelisk_trellis_001.md` | `20_research/trellis_wave_1_5_source_notes_2026-06-09.md` | Published externally; $120 price approved; standalone only; eight-image pack complete; screenshot supplied 2026-06-22 reports the live listing as posted about a week earlier; exact publish date, final live copy, and final posted media set are not duplicated in repo |

Wave 1.5 prompt-pack production is complete. T1 is posted as of 2026-06-11, and T2 was externally posted before screenshot evidence was supplied on 2026-06-22. Lead time will be given when order is made. Do not imply physical attachment for T1 unless separately approved; safe staging is alone or behind/beside Planter C. T2 is shown alone. The T2 paid plan has been purchased and located, so plan-backed dimensions/material facts may be used, but do not reproduce the full paid cut list in customer-facing prompts.

## SKU Rollout Map

| SKU | Product | Product Record | Retail | FBM Price | Image | Wave | Status | Next Action |
| --- | --- | --- | ---: | ---: | --- | ---: | --- | --- |
| A | Classic Square Cedar Planter | `30_products/prod_cedar_three_picket_planter_001.md` | $80 | $40 | `00_brand/photos/planter-a.png` | 1 | Published 2026-06-05; Claude-approved prose integrated | Monitor performance and capture metrics. |
| ABC | Cedar Planter Trio Set | `30_products/prod_cedar_trio_planter_box_set_001.md` | $220 | $110 | `00_brand/photos/planter-abc.png` | 1 | Done 2026-06-08; FBM listing completed | Monitor performance and capture metrics. |
| B | Small Square Cedar Planter | `30_products/prod_cedar_petite_planter_box_111113_001.md` | $60 | $30 | `00_brand/photos/planter-b.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack; revisit price later. |
| C | Tall Square Cedar Planter | `30_products/prod_cedar_tall_square_planter_161625_001.md` | $120 | $60 | `00_brand/photos/planter-c.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack; revisit price later. |
| D | Cedar Post Planter Box | `30_products/prod_cedar_post_planter_box_001.md` | $220 | $110 | `00_brand/photos/planter-d.png` | 4 | Product mapped; media approved | Validate cost/pricing. |
| E | Mini Adirondack Cedar Planter | `30_products/prod_cedar_bench_planter_001.md` | $120 | $60 | `00_brand/photos/planter-e.png` | 4 | Product synced; media approved | Validate cost/pricing. |
| F | Tiered Cedar Pyramid Planter | `30_products/prod_cedar_pyramid_planter_001.md` | $320 | $160 | `00_brand/photos/planter-f.png` | 1.5 | Published 2026-06-10; FBM listing completed | Monitor performance and capture metrics; continue trellis follow-up if needed. |
| T1 | Cedar Five-Finger Trellis | `30_products/prod_cedar_five_finger_trellis_001.md` | n/a | $40 | `T1_cedar_five_finger_trellis_ref_clean-01.png` | 1.5 | Published 2026-06-11; FBM listing completed | Monitor performance and capture metrics. |
| T2 | Cedar Decorative Obelisk Trellis | `30_products/prod_cedar_decorative_obelisk_trellis_001.md` | n/a | $120 | `T2_cedar_decorative_obelisk_trellis_ref_clean-01.png` | 1.5 | Published externally; screenshot supplied 2026-06-22 reports the listing as posted about a week earlier | Monitor performance and capture metrics. |
| USA1-L-NAT | Wavy Wooden American Flag — Large — Natural Wood with Red & Blue Stain | `30_products/variant_usa1_l_nat.md` | n/a | $120 | `C:\Users\outdo\Documents\Woodcraft Catalog Setup\Facebook Marketing\Marketplace\USA1\USA1-L-NAT` | Pre-2 | Published 2026-06-23; final live copy not archived | Monitor performance and capture metrics; USA1-SML preparation still precedes Wave 2. |
| G | Long Rectangle Cedar Planter | `30_products/prod_cedar_long_planter_box_46in_001.md` | $260 | $130 | `00_brand/photos/planter-g.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack. |
| H | Tall Cedar Planter w/ Shelf | `30_products/prod_cedar_tall_rectangular_planter_461632_001.md` | $320 | $160 | `00_brand/photos/planter-h.png` | 2 | Draft exists; media approved | Include in Wave 2 prompt pack. |
| J | Mailbox Post Cedar Planter | `30_products/prod_cedar_mailbox_post_planter_001.md` | $240 | $120 | `00_brand/photos/planter-j.png` | 4 | Product mapped; media approved | Validate cost/pricing. |
| K | Cedar Raised Garden Bed | `30_products/prod_cedar_raised_bed_001.md` | $480 | $240 featured configuration | `00_brand/photos/planter-k.png` | 1 | Published 2026-06-09; FBM listing completed | Monitor performance and capture metrics. |
| M | Small Tapered Cedar Planter | `30_products/prod_cedar_tapered_planter_box_001.md` | $100 | $50 | `00_brand/photos/planter-m.png` | 3 | Product mapped; media approved | Validate cost/pricing. |
| N | Three-Tier Cedar Planter | `30_products/prod_cedar_three_tier_planter_001.md` | $240 | $120 | `00_brand/photos/planter-n.png` | 3 | Product mapped; media approved | Validate cost/pricing. |
| P | Tall Patio Planter Box | `30_products/prod_cedar_wide_planter_box_262812_001.md` | $320 | $160 | `00_brand/photos/planter-p.png` | 3 | Product synced; media approved | Validate cost/pricing. |
| PS | Wooden Plant Stand | `30_products/prod_cedar_plant_stand_001.md` | $70 | $35 | `00_brand/photos/planter-ps.png` | 4 | Product mapped; media approved | Validate cost/pricing. |
| Q | Mini Cedar Cube Planter | `30_products/prod_cedar_one_picket_planter_001.md` | $40 | $20 | `00_brand/photos/planter-q.png` | 4 | Product synced; media approved | Validate cost/pricing. |
| TT | 3-Pot Tabletop Herb Planter | `30_products/prod_cedar_tabletop_plant_holder_001.md` | $60 | $30 | `00_brand/photos/planter-tt.png` | 4 | Product mapped; media approved | Validate cost/pricing. |

## Next Three Actions

1. Advance requested USA1-SML: generate Image 1 from the paired SML and Large clean-reference attachments, reuse the selected USA1-L-NAT listing photos for Images 2–5, then create scoped price, dimensions, and ordering cards. The new images attach the SML or Large reference as needed and enforce the Small, Medium, and Large dimension and scale comparison. First-build, factual, and publication gates still apply.
2. Create the Wave 2 Facebook Marketplace image prompt pack for B, C, G, and H from their approved catalog references.
3. Run the Wave 2 pack for B first: generate and review B’s required listing-image set before moving one SKU at a time through C, G, and H.
