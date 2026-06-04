# FBM Listing Image Pack Generator Prompt v1.1

Purpose: generate an 8-image prompt pack, or a 10-image pack when justified, for each Facebook Marketplace SKU listing using approved catalog facts, approved catalog images, and review-by-exception image text.

Owner: GPT/Codex orchestration and image-prep
Approval mode: Review by exception
Image text owner: GPT/Codex may generate factual in-image text as needed
Listing prose owner: Claude remains responsible for final Marketplace title, description, captions, CTAs, promo blurbs, and reply copy
Current image creation path: Lauren generates images manually with ChatGPT Image 2 from these prompt packs.
Automation status: do not build Canva, Figma, HTML, or scripted graphic templates right now. Keep automation/template notes only as future-reference ideas.

## Source Priority

Use sources in this order:

1. Saved Drakkar catalog artifacts in `20_research/catalog_exports/2026-06-03/`
2. Brand assets in `00_brand/`
3. Workflow rules in `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`
4. The per-SKU image plan at `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md`
5. The FBM image visual style reference at `40_listings/prompts/fbm_image_visual_style_reference_2026-06-04.md`
6. Product records in `30_products/`
7. Listing records in `40_listings/`
8. The voice guide at `20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/VOICE.md`

Do not use older product names, older prices, older sizes, or website values when they conflict with the saved catalog artifacts.

## Required Inputs Per SKU

- SKU
- product name
- category
- dimensions/spec
- retail price
- FB Marketplace price
- approved catalog image path
- listing record path, if created
- material facts
- build model
- location
- lead-time wording
- delivery/pickup wording
- special truth notes

## Global Facts

- Product line: handmade cedar garden goods.
- Brand asset SOT: use `00_brand/` for current logos, approved product photos, colors, and brand asset provenance.
- Customer-facing location wording: use `locally in Georgia`; use exact pickup locality only when necessary for logistics.
- Build model: built to order unless a record says otherwise.
- Lead time: use `Lead time provided when ordering` for listing facts unless a record says otherwise. For compact image graphics, use `Lead time available by request`.
- Fulfillment fact: pickup or local delivery by arrangement for listing prose; use `Pickup or local delivery available` for image text.
- Material: Western red cedar unless otherwise noted.
- Catalog SKU images: all saved catalog SKU images were approved for FBM use by Lauren on 2026-06-04 and copied into `00_brand/photos/` for active use.
- Text-bearing image prompts are allowed when text is part of the desired visual output.
- Do not strip requested text from image prompts by default.

## Review-By-Exception Rule

Do not ask Lauren to approve each generated image prompt or each generated graphic text line.

Generate the full pack from approved facts. Lauren will request changes if something looks wrong.

## Image Text Rules

Allowed to generate directly:

- price text from approved retail and FBM prices
- product names from catalog truth
- simple factual labels
- `Built locally in Georgia`
- `Custom sizing available` only when true for the SKU or category
- `Lead time available by request`
- `Message to order`
- `Pickup or local delivery available`
- factual inclusion/exclusion notes only when necessary to prevent a misleading image

## Text Overlay Count And Slots

Use a set number of text-overlay or graphic images so the listing still feels like a real Marketplace product listing, not an ad flyer.

- 8-image listing: use 3 text-overlay images.
- 10-image listing: use 4 text-overlay images.
- Image 1 must have no text overlay.
- For 8-image listings, the 3 text-overlay images are:
  - Image 3: price card
  - Image 7: dimensions/details graphic
  - Image 8: final ordering graphic
- For 10-image listings, the 4 text-overlay images are:
  - Image 3: price card
  - Image 8: dimensions/details graphic
  - Image 9: important details graphic
  - Image 10: final ordering graphic
- Important details graphics may include facts such as pots included, mailbox not included when necessary, custom sizes available, cut/preferred height, finish options, or other SKU-specific facts.
- Image 2 should stay the clean/empty product image by default because it is the inclusion anchor and trust builder.
- Put the price card at Image 3 by default. Use Image 2 for price only as an intentional exception, not the standard sequence.
- Product photos, clean product images, size/context photos, use-case photos, detail shots, and variation photos should usually have no text overlay unless the image's purpose is explicitly a graphic.
- Product photos carry trust first; graphics support price, size/details, local terms, and ordering.
- Do not include deposit terms unless Lauren explicitly approves them later.

Do not generate as final image text without Claude/customer-copy approval:

- promotional hooks
- emotional sales claims
- slogans
- discount framing beyond approved price facts
- CTA lines that go beyond simple factual ordering instructions
- platform captions
- listing titles or descriptions

## Truth Guardrails

- Do not invent construction details.
- Use detail shots only for visible/known features.
- If no SKU-specific detail is known, use cedar grain, board edges, square corners, scale, or general joinery.
- Lifestyle props are allowed when they help the image plan sell the product use case.
- At least one clean/empty SKU image must show exactly what is included with the SKU. Treat that clean/empty image as the inclusion anchor for the listing.
- Props in lifestyle, use-case, size/context, and seasonal images may appear as staging unless SKU facts say they are included.
- Do not add exclusion disclaimers by default. Prefer making the clean/empty product image clear. Use exclusion text only when necessary to prevent a real misunderstanding.
- Do not overuse exact city/location text in image graphics. Prefer `locally in Georgia` or `Built locally in Georgia`.
- Do not put SKU numbers or SKU letters in image text. Use the product name instead.
- Do not write deposit terms, balance-due terms, or fixed lead-time promises in image text unless Lauren explicitly approves those terms later.
- For Q, do not add an exclusion disclaimer; the clean/empty image already defines what is included.
- For E, do not imply it is a functional bench or safe for sitting.
- For K, use the featured catalog size as the default; other sizes are by quote.
- For ABC, show all three planters together and keep the bundle price.
- For TT, three standard 4-inch clay pots are included.

## Negative Prompt Rules

Use negative/avoid lines sparingly. Include only things the image model can visibly control, such as:

- wrong product shape, count, or scale
- extra or unreadable text
- cluttered composition
- confusing props in the clean/empty product image
- wrong background style
- unrealistic materials or finishes

Do not put abstract governance notes in negative prompts when the model cannot visually infer them. Keep pricing rules, approval rules, source-of-truth warnings, and listing-copy ownership in the workflow instructions instead.

## Filename Rules

Every generated image prompt should include a suggested output filename.

Place the filename outside the prompt text. When delivering prompts in chat, use two separate codeboxes: first a filename-only codebox, then a prompt-only codebox. Never embed the filename inside the prompt codebox.

Chat delivery format:

Filename:

```text
example_filename_fbm_01_lifestyle_hero_v01.png
```

Prompt:

```text
Create...
```

SKU listings use this filename pattern:

`{sku}_{product_slug}_fbm_{image_number}_{image_role}_v01.png`

Master or category listings use this filename pattern:

`{listing_slug}_fbm_{image_number}_{image_role}_v01.png`

Use lowercase filenames, underscores between words, two-digit image numbers, and short role slugs.

Standard role slugs:

- `lifestyle_hero`
- `clean_product`
- `size_context`
- `use_case`
- `detail`
- `price_graphic`
- `dimensions_details`
- `final_ordering`
- `support_variation`
- `important_details`

SKU identifiers are allowed in filenames for sorting and traceability. Do not put SKU identifiers inside the generated image text.

## Image Role Separation

Avoid near-duplicate image prompts within the same SKU pack.

- Do not create a new image slot by repeating the same setting, camera angle, product pose, and composition with different flowers or plants.
- Each no-text photo slot must change the buyer question and at least two visible composition variables: setting, camera distance, camera angle, product state, scale reference, use case, background, or detail focus.
- Image 1, Lifestyle Hero: sell the product in an appealing finished-use setting. It may use porch, patio, garden, entryway, plants, and lifestyle props to create desire.
- Image 2, Clean Product: show the empty product clearly and define what is included.
- Image 3, Price Card: show product name, retail price, Marketplace price, and short local/order facts.
- Image 4, Size/Context Photo: answer `how big is it?` quickly. Use practical scale references, a simpler background, and a comparison-photo feel. Do not repeat the lifestyle hero scene.
- Image 5, Use Case Photo: show one specific application, planting idea, or placement use. It should not be another broad lifestyle hero. Change the setting, camera distance, or use type enough that it feels distinct from Image 1.
- Image 6, Detail Photo: show material, shape, corners, rim, shelf, post, tier, or other visible construction details.
- Image 7, Dimensions/Details Graphic: use exact dimensions/specs and built-to-order/local facts.
- Image 8, Final Ordering Graphic: simple final order instruction and pickup/delivery availability.
- For 10-image packs, Image 7 becomes a no-text support/variation photo, Image 8 becomes the dimensions/details graphic, Image 9 becomes the important-details graphic, and Image 10 becomes the final ordering graphic.

For Image 4, prefer everyday scale references such as watering cans, gloves, nursery pots, doors, porch rails, garden paths, fence posts, or a hand when appropriate. Keep it more practical than pretty.

For Image 5, prefer a tighter practical use scene, an overhead/three-quarter planted example, or a specific application such as herbs, seasonal flowers, patio growing, entryway pair, mailbox display, tabletop herbs, or raised-bed vegetables. Avoid repeating the same porch/door hero composition from Image 1.

If the price card is intentionally assigned to Image 2, move the clean/empty product image to Image 3 and keep it no-text. This should be an exception.

## Output Structure

For each SKU, output this structure:

```text
## SKU [SKU] — [Product Name]

Facts:
- Retail:
- FBM:
- Size:
- Approved catalog image:
- Special truth notes:

Image 1 — Lifestyle Hero
- Filename:
- Purpose:
- Prompt:
- Negative/avoid:

Image 2 — Clean Product
- Filename:
- Purpose:
- Use:
- Optional prompt if regeneration is needed:
- Negative/avoid:

Image 3 — Price Card
- Filename:
- Purpose:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 4 — Size/Context Photo
- Filename:
- Purpose:
- Prompt:
- Negative/avoid:

Image 5 — Use Case Photo
- Filename:
- Purpose:
- Prompt:
- Negative/avoid:

Image 6 — Detail Photo
- Filename:
- Purpose:
- Prompt:
- Negative/avoid:

Image 7 — Dimensions/Details Graphic
- Filename:
- Purpose:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 8 — Final Ordering Graphic
- Filename:
- Purpose:
- Prompt:
- Exact in-image text:
- Negative/avoid:

10-image extension:

Image 7 — Support/Variation Photo
- Filename:
- Purpose:
- Prompt:
- Negative/avoid:

Image 8 — Dimensions/Details Graphic
- Filename:
- Purpose:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 9 — Important Details Graphic
- Filename:
- Purpose:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 10 — Final Ordering Graphic
- Filename:
- Purpose:
- Prompt:
- Exact in-image text:
- Negative/avoid:
```

If only 6 images are needed, keep Images 1, 2, 3, 6, 7, plus the stronger of Image 4 or Image 5. Do not use the 10-image extension for a reduced pack.

## Shared Visual Direction

Photo prompts:

- realistic local porch, garden, patio, doorstep, or workshop-adjacent environment
- useful lifestyle props are allowed when requested by the image plan
- natural daylight
- warm cedar color
- catalog palette influence: black/charcoal, warm stone/cream, muted silver, cedar/burnt orange
- product shape clearly readable
- clean composition
- no heavy overlay text on lifestyle, product, context, detail, or variation photos
- do not force every photo to be dark; use daylight, stone/cream, greenery, and warm cedar when that sells the product better
- avoid exaggerated luxury staging
- avoid unrealistic scale
- avoid confusing props in the clean/empty SKU image; that image defines what is included

Graphic prompts:

- square Marketplace-ready composition
- use the Drakkar catalog palette from the visual style reference
- black/charcoal, stone/cream, muted silver, and cedar/burnt-orange accents
- clean readable typography
- simple Drakkar feel
- exact text as supplied
- no extra words

## Default Graphic Style

- Background: dark charcoal / near black by default for price and order cards; light stone/cream is also allowed when it improves readability or keeps the image from feeling too dark
- Text: warm cream on dark backgrounds, deep black/charcoal on light backgrounds
- Accent: cedar/burnt orange from the catalog palette
- Optional small DD mark only if available/approved
- Layout: simple, legible, not crowded
- Aspect ratio: square 1:1 unless the output target says otherwise

## Future Automation Note

If this workflow is automated later, the most likely path is data-filled HTML or design templates for repeated graphics such as price cards, dimensions/details cards, important-details cards, and final-ordering cards.

Do not create those templates during the current workflow. For now, write concise ChatGPT Image 2 prompts that Lauren can generate quickly by hand.

## Final Check Before Saving A Prompt Pack

- Prices match catalog retail and FBM values.
- SKU/product names match catalog truth.
- Approved catalog image path is present.
- Suggested filename is present for each image prompt.
- Filenames are outside the prompt text, placed in their own filename-only codebox, and never embedded inside the prompt codebox.
- Text-overlay count is respected: 8-image packs use 3 text-overlay images; 10-image packs use 4.
- In-image text is literal and factual.
- In-image text does not include SKU numbers or SKU letters.
- No Claude-owned listing prose is presented as final.
- Media truth is clear.
- Review mode says review by exception.
- Prompt pack is usable directly in ChatGPT Image 2 without requiring Canva/Figma/HTML setup.
