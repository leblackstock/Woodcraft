# FBM Listing Image Pack Generator Prompt v1.1

Purpose: generate an 8-image prompt pack, or a 10-image pack when justified, for each Facebook Marketplace SKU listing using approved catalog facts, approved catalog images, and review-by-exception image text.

Owner: GPT/Codex orchestration and image-prep
Delivery scope: internal repository generator; do not paste this generator outside the repository as a substitute for the standalone image prompts it produces
Approval mode: Review by exception
Image text owner: GPT/Codex may generate factual in-image text as needed
Listing prose owner: Claude remains responsible for final Marketplace title, description, captions, CTAs, promo blurbs, and reply copy outside governed image graphic text
Current image creation path: Lauren generates images manually with ChatGPT Image 2 from these prompt packs.
Automation status: do not build Canva, Figma, HTML, or scripted graphic templates right now. Keep automation/template notes only as future-reference ideas.
Voice mode for factual in-image text: Marketplace

## Source Priority

Use sources in this order:

1. Saved Drakkar catalog artifacts in `20_research/catalog_exports/2026-06-03/`
2. Brand assets and identity guidance in `00_brand/`
3. Workflow rules in `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`
4. The per-SKU image plan at `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md`
5. The visual style reference at `00_brand/VISUAL_STYLE.md`
6. The Marketplace typography guidance at `00_brand/TEXT_STYLE_RULES.md`
7. Product records in `30_products/`
8. Listing records in `40_listings/`
9. The voice guide at `00_brand/VOICE.md`

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
- Brand SOT: use `00_brand/` for current assets and identity guidance, including `VOICE.md`, `COLOR_PALETTE.md`, `TEXT_STYLE_RULES.md`, and `VISUAL_STYLE.md`.
- Factual in-image wording uses Marketplace Mode from `00_brand/VOICE.md`; keep it direct, practical, factual, and easy to scan.
- Customer-facing location wording: use `locally in Georgia`; use exact pickup locality only when necessary for logistics.
- Build model: built to order unless a record says otherwise.
- Lead time: use `Lead time provided when ordering` for listing facts unless a record says otherwise. For compact image graphics, use `Lead time available by request`.
- Fulfillment fact: pickup or local delivery by arrangement for listing prose; use `Pickup or local delivery available` for image text.
- Material: Western red cedar unless otherwise noted.
- Catalog SKU images: all saved catalog SKU images were approved for FBM use by Lauren on 2026-06-04 and copied into `00_brand/photos/` for active use.
- Text-bearing image prompts are allowed when text is part of the desired visual output.
- Do not strip requested text from image prompts by default.
- Do not route image prompts, graphic prompts, overlay text, or literal in-image text to Claude for approval. Claude is only for standalone final copy blocks outside the image graphic workflow.

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

## Text Overlay Default Count And Slots

Use a default number of text-overlay or graphic images so the listing still feels like a real Marketplace product listing, not an ad flyer. These counts are defaults, not hard caps and not text-removal rules. If Lauren requests more image text, or if approved SKU facts need another graphic/overlay for clarity, keep the text and document the reason.

- 8-image listing default: use 3 text-overlay images.
- 10-image listing default: use 4 text-overlay images.
- Image 1 should usually have no text overlay unless Lauren explicitly asks for a hero graphic or overlay-led first image.
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
- Product photos, clean product images, size/context photos, use-case photos, detail shots, and variation photos should usually have no text overlay unless the image's purpose is explicitly a graphic or Lauren requests overlay text for that slot.
- Product photos carry trust first; graphics support price, size/details, local terms, and ordering.
- Do not include deposit terms unless Lauren explicitly approves them later.

Do not generate as image graphic text unless the active image workflow, approved facts, and Lauren's request or the image plan explicitly support it. This is a fact-safety rule for unsupported claims, not a Claude or per-line approval requirement. If the same wording is intended to become a standalone listing, post/caption, advertisement, catalog, or customer-reply prose block outside the image, route that separate prose block through Claude:

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

## Standalone Copy/Paste Requirement

Every delivered `Prompt:` must work when copied into an image model that cannot access this repository or its reference files.

Every delivered `Prompt:` must also pass `80_templates/standalone_external_prompt_checklist.md`.

- Do not rely on phrases such as `follow 00_brand/`, `use the brand guide`, `use the visual reference`, or `render the supplied text` inside the actual prompt.
- Inline the relevant brand colors, visual direction, typography direction, wording mode, literal in-image text, and visible avoid rules inside each prompt.
- Keep repository paths and source references in the surrounding workflow fields for auditability, not as required knowledge inside the copied prompt.
- Retain a separate `Exact in-image text:` field for human review, but also include those literal words inside the copied prompt.
- When exact product fidelity depends on an approved catalog image, say that the image must be attached or supplied to the target model. A text-only fallback may approximate the product but cannot guarantee an exact match.

Required standalone brand direction for photo prompts:

> Drakkar Designs brand direction: cedar-forward, practical, local, warm, and unfussy; realistic warm cedar grain and an honest handmade feel; natural daylight, porch/patio/garden context, and clean useful composition. Avoid bright unrelated colors, neon, glossy luxury styling, generic stock-photo blues, and washed-out beige.

Required standalone palette wording for graphic prompts:

> Use the exact Drakkar Designs brand palette: deep charcoal `#13181B`, warm stone/cream `#DEDCD6`, soft cream `#ebe9e3`, cedar/burnt orange `#CF4E17`, and muted silver `#A4A9A5`. Use charcoal and cream as the primary high-contrast pairing, cedar orange selectively for emphasis, and muted silver only for quiet secondary details.

Required standalone wording direction for factual FBM graphic text:

> Wording direction: Marketplace Mode — direct, practical, factual, easy to scan, restrained, and free of hype or first-person language.

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
- no heavy overlay text on lifestyle, product, context, detail, or variation photos unless that slot is intentionally planned as a graphic or overlay-led image
- do not force every photo to be dark; use daylight, stone/cream, greenery, and warm cedar when that sells the product better
- avoid exaggerated luxury staging
- avoid unrealistic scale
- avoid confusing props in the clean/empty SKU image; that image defines what is included

Graphic prompts:

- square Marketplace-ready composition
- use the approved Drakkar palette, Marketplace typography guidance, and visual direction from `00_brand/COLOR_PALETTE.md`, `00_brand/TEXT_STYLE_RULES.md`, and `00_brand/VISUAL_STYLE.md`
- black/charcoal, stone/cream, muted silver, and cedar/burnt-orange accents
- use clean, practical, sales-focused lettering that still matches the Drakkar Designs premium rustic catalog style
- make the product name largest when present; keep price/details medium and notes smaller
- use cream/stone and charcoal text with cedar-orange highlights, simple divider lines, and restrained rustic styling
- keep all lettering mobile-readable, clear, trustworthy, and easy to act on
- reserve distressed or weathered texture for short product names or major headings only; never distress small text
- use less ornament than a brand post; keep any divider, badge, or heritage-inspired mark subtle and functional
- use varied hierarchy rather than flat, uniform typography
- simple Drakkar catalog feel
- exact text as supplied
- no extra words
- negative/avoid lines for graphic prompts should reject flat uniform typography, generic corporate or cheap flyer styling, cheesy Viking/fantasy lettering, distressed small text, tiny decorative type, and unreadable contrast
- inline the exact Drakkar palette hex values, Marketplace wording direction, and literal in-image text so the prompt remains usable without repository files

Required reusable direction for every text-bearing FBM graphic prompt:

> “Typography direction: use clean, practical, sales-focused lettering that still matches the Drakkar Designs premium rustic catalog style. Make the product name largest, price/details medium, and notes smaller. Use cream/stone and charcoal text with cedar-orange highlights, simple divider lines, restrained rustic styling, and mobile-friendly readability. Keep it clear, trustworthy, and easy to act on.”

Apply the required direction inside each generated graphic prompt, then add role-specific hierarchy:

- Price card: product name largest; prices medium; short price labels or featured-size notes smaller; use cedar orange to emphasize price or one short label.
- Dimensions/details graphic: product name largest when present; dimensions or primary fact medium; local, lead-time, quote, and supporting facts smaller.
- Important-details graphic: short heading or product name largest; essential inclusion/exclusion or customization facts medium; supporting notes smaller.
- Final-ordering graphic: product name largest; `Message to order` medium and clearly separated; pickup/delivery line smaller.
- Master/category graphic without a product name: make the primary fact or action largest, then supporting facts progressively smaller.

## Default Graphic Style

- Background: dark charcoal / near black by default for price and order cards; light stone/cream is also allowed when it improves readability or keeps the image from feeling too dark
- Text: warm cream on dark backgrounds, deep black/charcoal on light backgrounds
- Accent: cedar/burnt orange from the catalog palette, used selectively on a key price, emphasis word, short label, divider, or small mark
- Optional small DD mark only if available/approved
- Layout: simple, legible, not crowded, with clear scale contrast and enough breathing room
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
- Every copied prompt is standalone and does not require access to repository files or unnamed reference guidance.
- Every photo prompt contains the standalone Drakkar visual direction.
- Every graphic prompt contains exact palette hex values, the Marketplace wording direction, typography direction, and literal in-image text.
- Text-overlay default is followed or any override is documented: 8-image packs usually use 3 text-overlay images; 10-image packs usually use 4.
- In-image text is literal and factual.
- Every text-bearing graphic prompt includes the required Marketplace typography direction and role-specific hierarchy.
- Product names are largest when present; price/details are medium; notes are smaller.
- Small text is clean and undistressed, with mobile-readable contrast and spacing.
- Graphic negative/avoid lines reject flat corporate-template styling, fantasy/Viking lettering, distressed small text, and unreadable contrast.
- In-image text does not include SKU numbers or SKU letters.
- No Claude-owned listing prose is presented as final.
- Media truth is clear.
- Review mode says review by exception.
- Prompt pack is usable directly in ChatGPT Image 2 without requiring Canva/Figma/HTML setup.
