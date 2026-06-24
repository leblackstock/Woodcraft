# FBM Listing Image Pack Generator Prompt v2.0

Purpose: generate an 8-image prompt pack, or a 10-image pack when justified, for each Facebook Marketplace SKU listing using approved catalog facts, approved catalog images, and review-by-exception image text, optimized for the most sellable Marketplace image set.

Owner: GPT/Codex orchestration and image-prep
Delivery scope: internal repository generator; do not paste this generator outside the repository as a substitute for the standalone image prompts it produces
Approval mode: Review by exception
Image text owner: GPT/Codex may generate factual in-image text as needed
Listing prose owner: Claude remains responsible for final Marketplace title, description, captions, CTAs, promo blurbs, and reply copy outside governed image graphic text
Current image creation path: Lauren generates images manually with ChatGPT Image 2 from these prompt packs.
Automation status: do not build Canva, Figma, HTML, or scripted graphic templates right now. Keep automation/template notes only as future-reference ideas.

## Strategy Change From v1.1

This generator is sellability-first.

Do not make brand mood, perfect palette obedience, or voice-guide fit the main target. Use brand guidance as a tool for trust and consistency, then prioritize the image set most likely to make a local Marketplace buyer stop, understand the offer, trust the product, and message to order.

If a more sellable image needs a brighter background, more useful staging, a tighter crop, stronger price clarity, clearer dimensions, or a more practical composition than the default brand mood would suggest, choose the more sellable image while keeping approved facts, exact product fidelity, readable text, and palette/background rules intact.

## Source Priority

Use sources in this order:

1. Saved Drakkar catalog artifacts in `20_research/catalog_exports/2026-06-03/`
2. Active FBM workflow hub at `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`
3. Brand assets and approved product photos in `00_brand/`
4. The per-SKU image plan at `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md`
5. Product records in `30_products/`
6. Listing records in `40_listings/`
7. Visual, color, text-style, and voice guidance in `00_brand/`

Do not use older product names, older prices, older sizes, or website values when they conflict with the saved catalog artifacts.

For a custom configurable family with no saved catalog row, use the approved family record, included child-variant records, and listing record as the fact source. Do not invent a catalog price, retail label, or catalog image to fill a missing catalog source.

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

## Variant-Scope Listing Mode

Use this mode only when the listing record has a `product_family_id` and a non-empty `variant_scope`. A variant scope is a selected set of separately priced standard options from one product family. It is not a bundle.

Required additional inputs:

- `listing_ref` and `listing_handle` for internal routing only; never put either into customer-facing image text unless the approved product facts independently call for those words
- exact `variant_scope`, in the intended display order
- approved name, customer-facing dimensions, price, finish choices, and exclusions for every included variant
- individual approved clean-reference attachment for every variant shown alone
- approved `scope_reference_asset` when an image shows the full selected collection together
- exact customer-facing option-and-price wording when prices differ

Rules for scope images:

- Show exactly the variants named in `variant_scope`, no more and no fewer.
- A group image must preserve their real relative scale and show one of each variant unless the approved shot plan says otherwise.
- For a group image, attach the approved scope reference as the primary visual control. Attach individual references as supporting controls when needed for exact fidelity.
- For a single-variant image, attach that variant's individual clean reference; do not use the group reference as a substitute.
- When the variants have different prices, create a factual option-and-price graphic that lists every included option and its approved price. Do not use bundle, set, savings, discount, or one-price-for-all wording.
- Do not generate prompts for a variant that lacks its required approved clean reference. Mark that image blocked until the reference is approved.

## Global Facts

- Product line: handmade cedar garden goods.
- Brand SOT: use `00_brand/` for current assets and identity guidance, including `VOICE.md`, `COLOR_PALETTE.md`, `TEXT_STYLE_RULES.md`, and `VISUAL_STYLE.md`.
- Customer-facing location wording: use `locally in Georgia`; use exact pickup locality only when necessary for logistics.
- Build model: built to order unless a record says otherwise.
- Lead time: use `Lead time provided when ordering` for listing facts unless a record says otherwise. For compact image graphics, use `Lead time available by request`.
- Fulfillment fact: pickup or local delivery by arrangement for listing prose; use `Pickup or local delivery available` for image text.
- Material: Western red cedar unless otherwise noted.
- Visible Marketplace wording should use `cedar`, not `Western red cedar`, unless Lauren explicitly requests the full material spec for that asset.
- Numeric dimension image rule: every FBM listing/post image pack must include at least one generated image or graphic with numeric dimensions when approved dimensions exist. For bundles or sets, include the numeric dimensions for each included size. If approved dimensions are missing, mark the dimension image as blocked instead of producing a dimensionless substitute.
- Catalog SKU images: all saved catalog SKU images were approved for FBM use by Lauren on 2026-06-04 and copied into `00_brand/photos/` for active use.
- Text-bearing image prompts are allowed when text is part of the desired visual output.
- Do not strip requested text from image prompts by default.
- Do not route image prompts, graphic prompts, overlay text, or literal in-image text to Claude for approval. Claude is only for standalone final copy blocks outside the image graphic workflow.

## Sellability Priorities

Optimize every pack for Marketplace buyer behavior:

1. Click: Image 1 must be the strongest first thumbnail for a mobile Marketplace feed.
2. Clarity: the buyer should quickly understand product type, size, material, price, and what is included.
3. Trust: include a clean product anchor, practical scale, realistic cedar, and detail proof.
4. Desire: show at least one finished use case that makes the item feel useful now, not merely documented.
5. Action: make price and ordering graphics simple enough to act on without reading a long description.

Brand style should support those goals, not outrank them.

## Review-By-Exception Rule

Do not ask Lauren to approve each generated image prompt or each generated graphic text line.

Generate the full pack from approved facts. Lauren will request changes if something looks wrong.

## Image Text Rules

Allowed to generate directly when supported by approved facts:

- plain selling-price text from approved FBM prices
- set or bundle savings text when the separate-item total, set price, and savings amount are approved facts or explicitly requested by Lauren
- product names from catalog truth
- direct buyer-benefit labels that follow from approved facts, such as herb planter, patio planter, raised garden bed, tabletop herb planter, or planter trio set
- simple factual labels
- `Built locally in Georgia`
- `Custom sizing available` only when true for the SKU or category
- `Lead time available by request`
- `Message to order`
- `Pickup or local delivery available`
- numeric dimensions from approved product or catalog facts
- factual inclusion/exclusion notes only when necessary to prevent a misleading image

Do not generate unsupported slogans, urgency, scarcity, emotional claims, discounts, durability claims, guarantees, or promotional hooks that go beyond approved facts.

If the same wording is intended to become a standalone listing, post/caption, advertisement, catalog, or customer-reply prose block outside the image, route that separate prose block through Claude.

## Text Overlay Defaults And Sellability Overrides

Use enough text-bearing graphics to make the listing easy to buy from, but not so much that it feels like an ad flyer.

- 8-image listing default: use 3 text-overlay images.
- 10-image listing default: use 4 text-overlay images.
- In every new 8-image or 10-image pack, real photographs occupy the leading positions in one continuous run. Composite text cards occupy one continuous run at the end. Never place a photograph after the first text card or a text card inside the photograph run.
- For the standard 8-image pack, Images 1 through 5 are reserved for real photographs with no composite text card or text overlay. For the 10-image pack, Images 1 through 6 are reserved for real photographs with no composite text card or text overlay.
- Image 1 is a no-text best-thumbnail photograph. Image 2 is the clean/empty product photograph because it is the inclusion anchor and trust builder.
- Product photos, clean product images, size/context photos, use-case photos, detail shots, and variation photos should usually have no text overlay unless the image's purpose is explicitly a graphic or overlay-led image.
- Product photos carry trust and desire first; graphics support price, size/details, local terms, and ordering.
- For the standard 8-image pack, Images 6 through 8 are the Price/Value Card, Dimensions/Details Graphic, and Final Ordering Graphic in that order. The ordering graphic is always last.
- For the 10-image pack, Images 7 through 10 are the Price/Value Card, Dimensions/Details Graphic, Important Details Graphic, and Final Ordering Graphic in that order. The ordering graphic is always last.
- If a product has fewer usable photographs than its leading photo slots, use the available photographs in those slots and leave the remaining photo slots empty. Do not promote a text card forward.
- Do not include deposit terms unless Lauren explicitly approves them later.

Default 8-image sequence:

1. Best Thumbnail: the image most likely to stop a Marketplace buyer while still showing the exact product.
2. Clean Product: show the empty product clearly and define what is included.
3. Size/Context Photo: answer `how big is it?` with practical scale.
4. Use-Case Photo: show one specific application, planting idea, or placement use.
5. Detail/Trust Photo: show cedar grain, shape, rim, post, shelf, tier, corner, or other visible construction detail.
6. Price/Value Card: show the product name and one plain selling-price line from the approved FBM price. If the price applies only to a featured configuration, label the price line plainly. For a non-bundle variant-scope listing with different prices, use a clear option-and-price chart listing every included variant and its exact approved price.
7. Dimensions/Details Graphic: use exact numeric dimensions/specs and local/order facts.
8. Final Ordering Graphic: simple order instruction and pickup/delivery availability.

Default 10-image extension:

1. Best Thumbnail: the image most likely to stop a Marketplace buyer while still showing the exact product.
2. Clean Product: show the empty product clearly and define what is included.
3. Size/Context Photo: answer `how big is it?` with practical scale.
4. Use-Case Photo: show one specific application, planting idea, or placement use.
5. Detail/Trust Photo: show cedar grain, shape, rim, post, shelf, tier, corner, or other visible construction detail.
6. Support/Variation Photo: no-text practical variation or alternate use.
7. Price/Value Card: show the product name and one plain selling-price line from the approved FBM price.
8. Dimensions/Details Graphic: exact numeric dimensions/specs.
9. Important Details Graphic: supported inclusion, customization, size, or quote facts.
10. Final Ordering Graphic: simple order instruction and pickup/delivery availability.

For Image 9, use only approved product facts. Do not introduce claims about hanging hardware, wall anchors, weatherproofing, outdoor durability, shipping, installation, current inventory, lead-time ranges, delivery fees, or any size, color, or variation outside the approved list. If no approved fact justifies Image 9, omit it and run the sequence as nine images, with Final Ordering Graphic as Image 9.

Do not use the former six-image shortcut for new packs. The standard 8-image sequence preserves the five leading photo positions, then price, dimensions, and final ordering.

## Best Thumbnail Rules

Image 1 should be judged by whether a buyer would stop scrolling.

- Make the product large and readable in a square mobile crop.
- Use the approved attachment to keep the product's exact shape, count, dimensions, board proportions, rim, legs/posts/shelf/tier details, cedar tone, and included pieces.
- Use a desirable but believable porch, patio, garden, doorstep, entryway, or workshop-adjacent setting.
- Prefer useful staging over generic prettiness: herbs, flowers, vegetables, gloves, watering cans, porch rails, patio stone, garden paths, or entry details when they support the product.
- Keep the scene honest and local, not luxury real estate, fantasy, glossy studio, or generic stock.
- If text is used on Image 1, keep it minimal, factual, and mobile-readable.

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
- Do not omit numeric dimensions from the dimensions/details image when approved dimensions exist. For a set or bundle, use numeric dimensions for every included size, not just `set of 3` or a count-only phrase.
- For Q, do not add an exclusion disclaimer; the clean/empty image already defines what is included.
- For E, do not imply it is a functional bench or safe for sitting.
- For K, treat the Cedar Raised Garden Bed as fully customizable by quote. Use the featured catalog configuration as the default current listing example, and make clear that its size, price, and specs apply only to that featured configuration. K is an open-bottom raised bed and must always be shown over soil, grass, garden bed ground, or yard/garden surface in any product photo or product-inset prompt; never place it on porch boards, decks, patios, concrete, pavers, indoor floors, showroom floors, or other hard-surface staging.
- For ABC, show all three planters together and keep the bundle price.
- For TT, three standard 4-inch clay pots are included.

## Negative Prompt Rules

Copied image prompts go to an external image model with no repository access. Do not explain internal repo policy or tell the model not to use internal labels it would not otherwise know.

Use positive, direct instructions first: exact product, exact attachment, exact text, exact palette, and the intended composition. Use negative/avoid lines only when they are short, concrete, and visually controllable, such as:

- wrong product shape, count, or scale
- extra or unreadable text
- cluttered composition
- confusing props in the clean/empty product image
- wrong background style
- unrealistic materials or finishes

Do not put abstract governance notes, pricing-policy explanations, approval rules, source-of-truth warnings, listing-copy ownership, or repo-only labels in copied prompt text.

## Filename Rules

Every generated image prompt should include a suggested output filename.

Place the filename outside the prompt text. When delivering prompts in chat, use two separate codeboxes: first a filename-only codebox, then a prompt-only codebox. Never embed the filename inside the prompt codebox.

SKU listings use this filename pattern:

`{sku}_{product_slug}_fbm_{image_number}_{image_role}_v01.png`

Master or category listings use this filename pattern:

`{listing_slug}_fbm_{image_number}_{image_role}_v01.png`

Use lowercase filenames, underscores between words, two-digit image numbers, and short role slugs.

Standard role slugs:

- `best_thumbnail`
- `clean_product`
- `size_context`
- `use_case`
- `detail_trust`
- `price_value`
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
- For FBM SKU or catalog listing prompt packs with an approved catalog image, treat the approved catalog image as a required attachment for every delivered product-specific prompt, including lifestyle photos, clean product images, price graphics, size/context photos, use-case photos, detail photos, dimensions/details graphics, important-details graphics, and final ordering graphics.
- The first line of every such copied `Prompt:` must be `Please see attached "[plain-language item being attached]"`.
- Do this even when the prompt is mainly a text graphic. The attachment gives the image model the correct product and prevents detached, generic graphics.
- Exact product fidelity is always required for Facebook Marketplace listing images. Do not deliver or generate an FBM listing image prompt from text only.
- If the approved catalog image or required reference image is missing, stop and ask for the attachment instead of producing a text-only approximation.

Required standalone brand direction for photo prompts:

> Drakkar Designs direction for FBM listing photos: sell the product clearly first. Show realistic warm cedar grain, honest handmade character, and exact product proportions from the attached reference. Use practical local porch, patio, garden, doorstep, entryway, or workshop-adjacent settings with natural daylight and soft shadows. Choose a specific physical background or surface before describing the rest of the scene. Remaining approved palette colors, listed without assigning roles: warm stone/cream `#DEDCD6`, soft cream `#ebe9e3`, deep charcoal `#13181B`, charcoal `#414444`, cedar/burnt orange `#CF4E17`, and muted silver `#A4A9A5`. Keep the product large, trustworthy, and easy to understand in a square mobile Marketplace crop.

Required standalone palette wording for graphic prompts:

> Choose the background first, then list the remaining approved palette colors without assigning them to specific elements. Use whichever background makes this specific graphic most readable and sellable. For dark Marketplace graphics, default background is deep charcoal `#13181B`. For light-card graphics, default background is soft cream `#ebe9e3`. Remaining approved palette colors to list without role assignments: warm stone/cream `#DEDCD6`, deep charcoal `#13181B`, charcoal `#414444`, cedar/burnt orange `#CF4E17`, and muted silver `#A4A9A5`. Do not tell the image model which remaining color to use for text, dividers/rules, accents, panels, badges, or inset fields.

Required standalone wording direction for factual FBM graphic text:

> Keep the graphic direct, practical, factual, easy to scan, buyer-focused, and free of unsupported hype or first-person language.

## Prompt Specificity Requirements

Write the copied image prompts explicitly. Each prompt should tell ChatGPT Image 2 exactly what the image is for, what buyer question it answers, what should stay realistic, what makes it sell, what colors or physical background to use, and where artistic variation is welcome.

For every FBM prompt:

- State that the image is for a Facebook Marketplace listing and should read quickly in a mobile Marketplace feed.
- Name the image role and buyer job, such as best thumbnail, inclusion anchor, price clarity, size check, specific use case, detail proof, dimensions/details, or final ordering instruction.
- Explain what makes this slot sell: click appeal, confidence, price clarity, size proof, use-case desire, trust, or action.
- Explicitly name the background color or physical background/surface. Graphic prompts must choose a background color first. Photo prompts must state the actual environment background, such as porch boards, patio stone, garden path, soft cream product field, or workshop-adjacent surface.
- Require realistic product proportions. Use the approved attachment to control the product's exact shape, count, dimensions, board proportions, rim, legs/posts/shelf/tier details, cedar tone, and included pieces.
- Say not to stretch, shrink, rotate, add, remove, or redesign the product beyond what the approved attachment supports.
- Allow artistic expression in staging, lighting, background texture, divider placement, typography rhythm, and small catalog-style ornaments, as long as the product facts, exact text, proportions, readability, and brand palette remain correct.

For photo, hero, lifestyle, use-case, size/context, clean-product, variation, and detail prompts:

- Include a camera angle and distance.
- Include framing guidance for a square crop: leave breathing room, keep the product large enough to read at phone size, and avoid cropping off important edges.
- Include lighting and color direction for materials and setting: natural daylight, soft shadows, warm realistic cedar, practical porch/patio/garden surfaces, natural greenery, and believable concrete, stone, or metal when useful.
- Choose only the background or physical setting first, then list remaining palette colors without assigning them to scene elements.
- Do not make lifestyle or hero images look like luxury real estate ads, fantasy scenes, glossy studio renders, or generic stock photos.

For text-bearing graphic prompts:

- Generate the exact in-image text from approved facts using Marketplace Mode only as a guardrail: direct, practical, factual, easy to scan, no first person, no unsupported hype.
- Use `cedar` as the visible material word in image text. Do not write `Western red cedar` or `western red cedar` unless Lauren explicitly requests the full spec.
- Include the literal words in the prompt and require no extra readable words.
- Specify the chosen background color first, then list the remaining approved palette colors without assigning them to text, dividers/rules, badges, accents, panels, or inset fields.
- Spell out text styling: product name largest when present, price/details medium, notes smaller, simple divider lines, restrained rustic styling, mobile-readable spacing, and no distressing on small text.
- Do not assign any remaining palette color to a specific text, divider, badge, accent, panel, or inset role.

## Image Role Separation

Avoid near-duplicate image prompts within the same SKU pack.

- Do not create a new image slot by repeating the same setting, camera angle, product pose, and composition with different flowers or plants.
- Each no-text photo slot must change the buyer question and at least two visible composition variables: setting, camera distance, camera angle, product state, scale reference, use case, background, or detail focus.
- Image 1, Best Thumbnail: sell the product at first glance. It may be a lifestyle hero, clean product hero, or use-case hero, whichever is most likely to stop a Marketplace buyer while preserving exact product fidelity.
- Image 2, Clean Product: show the empty product clearly and define what is included.
- Image 3, Size/Context Photo: answer `how big is it?` quickly. Use practical scale references and a simpler background. Do not repeat the first thumbnail scene.
- Image 4, Use-Case Photo: show one specific application, planting idea, or placement use. It should not be another broad lifestyle hero.
- Image 5, Detail/Trust Photo: show material, shape, corners, rim, shelf, post, tier, or other visible construction details.
- Image 6, Price/Value Card: show the product name and one plain selling-price line from the approved FBM price. When the approved price applies only to a featured configuration, as with K, label the line plainly, such as `Featured size $240`, so the graphic does not imply every custom build shares that price. For a non-bundle variant-scope listing with different approved option prices, replace the single price line with a clear option-and-price chart that lists every and only the scoped variants with their exact approved prices. For approved sets or bundles, savings wording may be added when the separate-item total, set price, and savings amount are approved facts or Lauren explicitly requests it. Keep it factual, such as `3 separately $130`, `Set price $110`, and `Save $20 as a set`, rather than vague sale hype.
- Image 7, Dimensions/Details Graphic: use exact numeric dimensions/specs and built-to-order/local facts. For bundles or sets, include the numeric dimensions for each included size.
- Image 8, Final Ordering Graphic: simple final order instruction and pickup/delivery availability.
- For 10-image packs, Images 1 through 5 retain the standard photo roles, Image 6 is the no-text support/variation photo, Image 7 is the price/value card, Image 8 is the dimensions/details graphic with numeric dimensions, Image 9 is the approved-facts-only important-details graphic, and Image 10 is the final ordering graphic. If no approved fact justifies Image 9, omit it and run nine images with the final ordering graphic as Image 9.

For Image 3, prefer everyday scale references such as watering cans, gloves, nursery pots, doors, porch rails, garden paths, fence posts, or a hand when appropriate. Keep it more practical than pretty.

For Image 4, prefer a tighter practical use scene, an overhead/three-quarter planted example, or a specific application such as herbs, seasonal flowers, patio growing, entryway pair, mailbox display, tabletop herbs, or raised-bed vegetables. Avoid repeating the same porch/door hero composition from Image 1.

## Output Structure

For each SKU, output this structure:

```text
## SKU [SKU] - [Product Name]

Facts:
- Retail:
- FBM:
- Size:
- Approved catalog image:
- Special truth notes:

Image 1 - Best Thumbnail
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Negative/avoid:

Image 2 - Clean Product
- Filename:
- Purpose:
- Use:
- Optional exact-fidelity prompt if regeneration is needed:
- Negative/avoid:

Image 3 - Size/Context Photo
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Negative/avoid:

Image 4 - Use-Case Photo
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Negative/avoid:

Image 5 - Detail/Trust Photo
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Negative/avoid:

Image 6 - Price/Value Card
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 7 - Dimensions/Details Graphic
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 8 - Final Ordering Graphic
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:

10-image extension:

Images 1 through 5 use the same Best Thumbnail, Clean Product, Size/Context, Use-Case, and Detail/Trust fields as the standard 8-image structure above.

Image 6 - Support/Variation Photo
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Negative/avoid:

Image 7 - Price/Value Card
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 8 - Dimensions/Details Graphic
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:

Image 9 - Important Details Graphic
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:
- Approved-facts check: omit this image when no approved fact requires it; do not substitute unsupported claims.

Image 10 - Final Ordering Graphic
- Filename:
- Purpose:
- Sellability reason:
- Prompt:
- Exact in-image text:
- Negative/avoid:
```

## Shared Visual Direction

Photo prompts:

- start from the image role, buyer question, and sellability reason
- realistic local porch, garden, patio, doorstep, entryway, or workshop-adjacent environment
- useful lifestyle props are encouraged when they make the product easier to imagine buying or using
- natural daylight with soft shadows, not harsh studio glare
- warm realistic cedar color with visible grain; keep cedar orange-brown, not painted orange, yellow pine, plastic, or glossy furniture finish
- choose the background or physical setting explicitly, then list the remaining approved palette colors without assigning them to specific elements
- product shape clearly readable, with realistic proportions, count, size, board scale, rims, posts, legs, shelves, tiers, or open-top structure controlled by the approved attachment
- square composition with enough breathing room for Marketplace cropping; product large enough to read in a mobile feed
- camera angle named in the prompt
- clean composition that still allows natural handmade imperfection, staging warmth, and artistic daylight variation
- no heavy overlay text on product/context/detail photos unless that slot is intentionally planned as a graphic or overlay-led image
- do not force every photo to be dark; use daylight, stone/cream, greenery, and warm cedar when that sells the product better
- avoid exaggerated luxury staging
- avoid unrealistic scale
- avoid confusing props in the clean/empty SKU image; that image defines what is included

Graphic prompts:

- square Marketplace-ready composition
- choose the exact background color in the copied prompt, then list the remaining approved palette colors without assigning them to graphic elements
- choose dark or light backgrounds based on readability and sellability for the specific card
- use clean, practical, sales-focused lettering that still feels like Drakkar
- make the product name largest when present; keep price/details medium and notes smaller
- keep price, dimensions, and `Message to order` highly readable at phone size
- use less ornament than a brand post; any divider, badge, or heritage-inspired mark must support readability
- use varied hierarchy rather than flat, uniform typography
- exact text as supplied
- no extra words
- allow artistic expression in the balance of type sizes, divider placement, subtle texture, small heritage/catalog ornaments, and product-photo inset treatment while preserving exact text, exact facts, realistic product proportions, readability, and the chosen background
- negative/avoid lines for graphic prompts should be short and visual, such as `no extra words` or `text must be readable`
- inline the exact Drakkar palette hex values, Marketplace wording direction, and literal in-image text so the prompt remains usable without repository files

Required reusable direction for every text-bearing FBM graphic prompt:

> Typography direction: use clean, practical, sales-focused lettering that is easy to read in a Facebook Marketplace feed. Make the product name largest when present, price/details medium, and notes smaller. Use simple divider lines, restrained rustic styling, generous spacing, and mobile-friendly readability. Keep small text clean and undistressed. Allow tasteful artistic variation in type scale, spacing, divider placement, and subtle catalog ornaments while keeping the exact words readable, factual, and easy to act on. The prompt must choose only the background color; list all other palette colors without assigning them to text, dividers, accents, panels, or inset fields.

Apply the required direction inside each generated graphic prompt, then add role-specific hierarchy:

- Price/value card: product name largest; price medium-large; factual savings callout medium-large only when approved; short size or featured-use note smaller.
- Dimensions/details graphic: product name largest when present; dimensions or primary fact medium; local, lead-time, quote, and supporting facts smaller.
- Important-details graphic: short heading or product name largest; essential inclusion/exclusion or customization facts medium; supporting notes smaller.
- Final-ordering graphic: product name largest; `Message to order` medium-large and clearly separated; pickup/delivery line smaller.
- Master/category graphic without a product name: make the primary fact or action largest, then supporting facts progressively smaller.

## Default Graphic Style

- Background: choose dark charcoal, light cream, or another approved background treatment based on which is most readable and sellable for that card
- Other palette colors: list the approved palette colors without assigning them to text, dividers, accents, panels, badges, or inset fields
- Optional small DD mark only if available/approved
- Layout: simple, legible, not crowded, with clear scale contrast and enough breathing room
- Aspect ratio: square 1:1 unless the output target says otherwise

## Future Automation Note

If this workflow is automated later, the most likely path is data-filled HTML or design templates for repeated graphics such as price cards, dimensions/details cards, important-details cards, and final-ordering cards.

Do not create those templates during the current workflow. For now, write concise ChatGPT Image 2 prompts that Lauren can generate quickly by hand.

## Final Check Before Saving A Prompt Pack

- Prices match catalog retail and FBM values.
- Featured-configuration prices, such as K's current $240 price, are labeled as featured-only when used in image text.
- Variant-scope packs show every and only the codes in `variant_scope`; when scoped variants have different prices, their option-and-price chart uses the exact approved price for each and no bundle wording.
- Set or bundle savings graphics show only approved separate-item totals, approved set prices, and approved savings amounts.
- SKU/product names match catalog truth.
- At least one image or graphic contains numeric dimensions when approved dimensions exist.
- Dimensions/details graphics include numeric dimensions, not count-only wording such as `set of 3`.
- Approved catalog image path is present.
- Suggested filename is present for each image prompt.
- Filenames are outside the prompt text, placed in their own filename-only codebox, and never embedded inside the prompt codebox.
- Every copied prompt is standalone and does not require access to repository files or unnamed reference guidance.
- Every copied prompt says what the image is for, what buyer question it answers, and why the slot helps sell the listing.
- Every generated product photo prompt names a camera angle, framing/crop intent, lighting/tone, and practical color environment.
- Every generated product prompt explicitly requires realistic proportions controlled by the approved attachment.
- Any K / Cedar Raised Garden Bed product photo or product-inset prompt places the bed over soil, grass, garden bed ground, or yard/garden surface and explicitly avoids porch/deck/patio/concrete/hard-surface staging.
- Every photo prompt contains the standalone FBM visual direction.
- Every graphic prompt contains the chosen background color, remaining approved palette hex values without role assignments, Marketplace wording direction, typography direction, and literal in-image text.
- Text-overlay default is followed or any sellability override is documented.
- In-image text is literal and factual.
- Product names are largest when present; price/details are medium; notes are smaller.
- Small text is clean and undistressed, with mobile-readable contrast and spacing.
- Graphic negative/avoid lines stay short and visual.
- In-image text does not include SKU numbers or SKU letters.
- No Claude-owned listing prose is presented as final.
- Media truth is clear.
- Review mode says review by exception.
- Prompt pack is usable directly in ChatGPT Image 2 without requiring Canva/Figma/HTML setup.
