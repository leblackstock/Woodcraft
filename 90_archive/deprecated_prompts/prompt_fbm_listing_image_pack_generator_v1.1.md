# FBM Listing Image Pack Generator Prompt v1.1

Status: Superseded by `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v2.0.md` for new sellability-first FBM image prompt packs. Retain for traceability only.

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
- Visible Marketplace wording should use `cedar`, not `Western red cedar`, unless Lauren explicitly requests the full material spec for that asset.
- Numeric dimension image rule: every FBM listing/post image pack must include at least one generated image or graphic with numeric dimensions when approved dimensions exist. For bundles or sets, include the numeric dimensions for each included size. If approved dimensions are missing, mark the dimension image as blocked instead of producing a dimensionless substitute.
- Catalog SKU images: all saved catalog SKU images were approved for FBM use by Lauren on 2026-06-04 and copied into `00_brand/photos/` for active use.
- Text-bearing image prompts are allowed when text is part of the desired visual output.
- Do not strip requested text from image prompts by default.
- Do not route image prompts, graphic prompts, overlay text, or literal in-image text to Claude for approval. Claude is only for standalone final copy blocks outside the image graphic workflow.

## Review-By-Exception Rule

Do not ask Lauren to approve each generated image prompt or each generated graphic text line.

Generate the full pack from approved facts. Lauren will request changes if something looks wrong.

## Image Text Rules

Allowed to generate directly:

- plain selling-price text from approved FBM prices
- set or bundle savings text when the separate-item total, set price, and savings amount are approved facts or explicitly requested by Lauren
- product names from catalog truth
- simple factual labels
- `Built locally in Georgia`
- `Custom sizing available` only when true for the SKU or category
- `Lead time available by request`
- `Message to order`
- `Pickup or local delivery available`
- numeric dimensions from approved product or catalog facts
- factual inclusion/exclusion notes only when necessary to prevent a misleading image

## Text Overlay Default Count And Slots

Use a default number of text-overlay or graphic images so the listing still feels like a real Marketplace product listing, not an ad flyer. These counts are defaults, not hard caps and not text-removal rules. If Lauren requests more image text, or if approved SKU facts need another graphic/overlay for clarity, keep the text and document the reason.

- 8-image listing default: use 3 text-overlay images.
- 10-image listing default: use 4 text-overlay images.
- Image 1 should usually have no text overlay unless Lauren explicitly asks for a hero graphic or overlay-led first image.
- For 8-image listings, the 3 text-overlay images are:
  - Image 3: price card
  - Image 7: dimensions/details graphic with numeric dimensions
  - Image 8: final ordering graphic
- For 10-image listings, the 4 text-overlay images are:
  - Image 3: price card
  - Image 8: dimensions/details graphic with numeric dimensions
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
- discount or savings framing beyond approved price facts or explicit operator direction
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

Do not put abstract governance notes, pricing-policy explanations, approval rules, source-of-truth warnings, listing-copy ownership, or repo-only labels in copied prompt text. If the prompt already says `Render exactly these lines and no other words`, do not add a separate list of labels or phrases to avoid.

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
Please see attached "the approved catalog image for [plain-language product or listing name]".

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
- For FBM SKU or catalog listing prompt packs with an approved catalog image, treat the approved catalog image as a required attachment for every delivered product-specific prompt, including lifestyle photos, clean product images, price graphics, size/context photos, use-case photos, detail photos, dimensions/details graphics, important-details graphics, and final ordering graphics.
- The first line of every such copied `Prompt:` must be `Please see attached "[plain-language item being attached]"`.
- Do this even when the prompt is mainly a text graphic. The attachment gives the image model the correct product and prevents detached, generic graphics.
- Exact product fidelity is always required for Facebook Marketplace listing images. Do not deliver or generate an FBM listing image prompt from text only.
- If the approved catalog image or required reference image is missing, stop and ask for the attachment instead of producing a text-only approximation.
- If a delivered `Prompt:` requires an attached image, make the first line of that prompt `Please see attached "[plain-language item being attached]"`.
- Clean-product image slots may use the approved catalog image directly as the listing asset. If any Marketplace listing image is generated or regenerated, its copied prompt still starts with the required `Please see attached ...` line.

Required standalone brand direction for photo prompts:

> Drakkar Designs brand direction: cedar-forward, practical, local, warm, and unfussy; realistic warm cedar grain and an honest handmade feel; natural daylight with soft shadows; porch, patio, garden, doorstep, or workshop-adjacent context; warm stone/cream surfaces, natural garden greens, muted silver/gray concrete or hardware, and small cedar/burnt-orange accents only when they fit the scene; clean useful composition that keeps the product proportions realistic and readable in a mobile Marketplace feed.

Required standalone palette wording for graphic prompts:

> Choose the background first, then list the remaining approved palette colors without assigning them to specific elements. For dark Marketplace graphics, default background is deep charcoal `#13181B` unless the prompt explicitly chooses a light card. For light-card graphics, default background is soft cream `#ebe9e3`. Remaining approved palette colors to list without role assignments: warm stone/cream `#DEDCD6`, deep charcoal `#13181B`, charcoal `#414444`, cedar/burnt orange `#CF4E17`, and muted silver `#A4A9A5`. Do not tell the image model which remaining color to use for text, dividers/rules, badges, accents, panels, or inset fields.

Required standalone wording direction for factual FBM graphic text:

> Keep the graphic direct, practical, factual, easy to scan, restrained, and free of hype or first-person language.

## Prompt Specificity Requirements

Write the copied image prompts more explicitly than a normal creative brief. Each prompt should tell ChatGPT Image 2 exactly what the image is for, what buyer question it answers, what should stay realistic, what colors to use, and where artistic variation is welcome.

For every FBM prompt:

- State that the image is for a Facebook Marketplace listing and should read quickly in a mobile Marketplace feed.
- Name the image role and buyer job, such as first thumbnail, inclusion anchor, price clarity, size check, specific use case, detail proof, dimensions/details, or final ordering instruction.
- Explicitly name the background color or physical background/surface. Graphic prompts must choose a background color first. Photo prompts must state the actual environment background, such as porch boards, patio stone, garden path, soft cream product field, or workshop-adjacent surface.
- Require realistic product proportions. Use the approved attachment to control the product's exact shape, count, dimensions, board proportions, rim, legs/posts/shelf/tier details, cedar tone, and included pieces.
- Say not to stretch, shrink, rotate, add, remove, or redesign the product beyond what the approved attachment supports.
- Describe the intended tone: practical, local, warm, cedar-forward, trustworthy, handmade, and unfussy.
- Allow artistic expression in staging, lighting, background texture, divider placement, typography rhythm, and small catalog-style ornaments, as long as the product facts, exact text, proportions, and brand palette remain correct.

For photo, hero, lifestyle, use-case, size/context, clean-product, variation, and detail prompts:

- Include a camera angle and distance. Examples: front three-quarter view at about chest height, slightly higher three-quarter view into an open planter, low front corner detail close-up, overhead-ish practical garden view, or wider patio comparison view.
- Include framing guidance for a square crop: leave breathing room, keep the product large enough to read at phone size, and avoid cropping off important edges.
- Include lighting and color direction for materials and setting: natural daylight, soft shadows, warm realistic cedar, practical porch/patio/garden surfaces, natural greenery, and believable concrete, stone, or metal when useful. For brand palette colors, choose only the background and list the remaining palette colors without assigning them to scene elements.
- Do not make lifestyle or hero images look like luxury real estate ads, fantasy scenes, glossy studio renders, or generic stock photos.

For text-bearing graphic prompts:

- Generate the exact in-image text from approved facts using Marketplace Mode: direct, practical, factual, easy to scan, no first person, no hype.
- Use `cedar` as the visible material word in image text. Do not write `Western red cedar` or `western red cedar` unless Lauren explicitly requests the full spec.
- Include the literal words in the prompt and require no extra readable words.
- Specify the chosen background color first, then list the remaining approved palette colors without assigning them to text, dividers/rules, badges, accents, panels, or inset fields.
- Spell out text styling: product name largest when present, price/details medium, notes smaller, simple divider lines, restrained rustic styling, mobile-readable spacing, and no distressing on small text.
- Do not assign any remaining palette color to a specific text, divider, badge, accent, panel, or inset role.

## Image Role Separation

Avoid near-duplicate image prompts within the same SKU pack.

- Do not create a new image slot by repeating the same setting, camera angle, product pose, and composition with different flowers or plants.
- Each no-text photo slot must change the buyer question and at least two visible composition variables: setting, camera distance, camera angle, product state, scale reference, use case, background, or detail focus.
- Image 1, Lifestyle Hero: sell the product in an appealing finished-use setting. It may use porch, patio, garden, entryway, plants, and lifestyle props to create desire.
- Image 2, Clean Product: show the empty product clearly and define what is included.
- Image 3, Price Card: show the product name and one plain selling-price line from the approved FBM price. When the approved price applies only to a featured configuration, as with K, label the line plainly, such as `Featured size $240`, so the graphic does not imply every custom build shares that price. For approved sets or bundles, savings wording may be added when the separate-item total, set price, and savings amount are approved facts or Lauren explicitly requests it. Keep it factual, such as `3 separately $130`, `Set price $110`, and `Save $20 as a set`, rather than vague sale hype. The copied prompt should specify only the exact rendered text, not internal labels or price-policy explanations.
- Image 4, Size/Context Photo: answer `how big is it?` quickly. Use practical scale references, a simpler background, and a comparison-photo feel. Do not repeat the lifestyle hero scene.
- Image 5, Use Case Photo: show one specific application, planting idea, or placement use. It should not be another broad lifestyle hero. Change the setting, camera distance, or use type enough that it feels distinct from Image 1.
- Image 6, Detail Photo: show material, shape, corners, rim, shelf, post, tier, or other visible construction details.
- Image 7, Dimensions/Details Graphic: use exact numeric dimensions/specs and built-to-order/local facts. For bundles or sets, include the numeric dimensions for each included size.
- Image 8, Final Ordering Graphic: simple final order instruction and pickup/delivery availability.
- For 10-image packs, Image 7 becomes a no-text support/variation photo, Image 8 becomes the dimensions/details graphic with numeric dimensions, Image 9 becomes the important-details graphic, and Image 10 becomes the final ordering graphic.

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
- Optional exact-fidelity prompt if regeneration is needed:
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

- begin from the image role and buyer question, such as first thumbnail, actual included item, scale check, use case, or construction/detail proof
- realistic local porch, garden, patio, doorstep, or workshop-adjacent environment
- useful lifestyle props are allowed when requested by the image plan
- natural daylight with soft shadows, not harsh studio glare
- warm realistic cedar color with visible grain; keep cedar orange-brown, not painted orange, yellow pine, plastic, or glossy furniture finish
- catalog palette influence: choose the background explicitly, then list the remaining approved palette colors without assigning them to specific elements
- product shape clearly readable, with realistic proportions, count, size, board scale, rims, posts, legs, shelves, tiers, or open-top structure controlled by the approved attachment
- square composition with enough breathing room for Marketplace cropping; product large enough to read in a mobile feed
- camera angle named in the prompt, such as front three-quarter, slightly higher three-quarter, wider practical comparison view, overhead-ish garden view, or close corner detail
- clean composition that still allows a little natural handmade imperfection, staging warmth, and artistic daylight variation
- no heavy overlay text on lifestyle, product, context, detail, or variation photos unless that slot is intentionally planned as a graphic or overlay-led image
- do not force every photo to be dark; use daylight, stone/cream, greenery, and warm cedar when that sells the product better
- avoid exaggerated luxury staging
- avoid unrealistic scale
- avoid confusing props in the clean/empty SKU image; that image defines what is included

Graphic prompts:

- square Marketplace-ready composition
- use the approved Drakkar palette, Marketplace typography guidance, and visual direction from `00_brand/COLOR_PALETTE.md`, `00_brand/TEXT_STYLE_RULES.md`, and `00_brand/VISUAL_STYLE.md`
- choose the exact background color in the copied prompt, then list the remaining approved palette colors without assigning them to graphic elements
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
- allow artistic expression in the balance of type sizes, divider placement, subtle texture, small heritage/catalog ornaments, and product-photo inset treatment while preserving exact text, exact facts, realistic product proportions, and the chosen background
- negative/avoid lines for graphic prompts should be short and visual, such as `no extra words` or `text must be readable`
- inline the exact Drakkar palette hex values, Marketplace wording direction, and literal in-image text so the prompt remains usable without repository files

Required reusable direction for every text-bearing FBM graphic prompt:

> “Typography direction: use clean, practical, sales-focused lettering that still matches the Drakkar Designs premium rustic catalog style. Make the product name largest when present, price/details medium, and notes smaller. Use simple divider lines, restrained rustic styling, generous spacing, and mobile-friendly readability. Keep small text clean and undistressed. Allow tasteful artistic variation in type scale, spacing, divider placement, and subtle catalog ornaments while keeping the exact words readable, factual, and easy to act on. The prompt must choose only the background color; list all other palette colors without assigning them to text, dividers, accents, panels, or inset fields.”

Apply the required direction inside each generated graphic prompt, then add role-specific hierarchy:

- Price card: product name largest; prices medium; savings callout medium-large when approved; short price labels or featured-size notes smaller; use cedar orange to emphasize price, savings, or one short label.
- Dimensions/details graphic: product name largest when present; dimensions or primary fact medium; local, lead-time, quote, and supporting facts smaller.
- Important-details graphic: short heading or product name largest; essential inclusion/exclusion or customization facts medium; supporting notes smaller.
- Final-ordering graphic: product name largest; `Message to order` medium and clearly separated; pickup/delivery line smaller.
- Master/category graphic without a product name: make the primary fact or action largest, then supporting facts progressively smaller.

## Default Graphic Style

- Background: dark charcoal / near black by default for price and order cards; light stone/cream is also allowed when it improves readability or keeps the image from feeling too dark
- Other palette colors: list the approved palette colors without assigning them to text, dividers, accents, panels, or inset fields
- Optional small DD mark only if available/approved
- Layout: simple, legible, not crowded, with clear scale contrast and enough breathing room
- Aspect ratio: square 1:1 unless the output target says otherwise

## Future Automation Note

If this workflow is automated later, the most likely path is data-filled HTML or design templates for repeated graphics such as price cards, dimensions/details cards, important-details cards, and final-ordering cards.

Do not create those templates during the current workflow. For now, write concise ChatGPT Image 2 prompts that Lauren can generate quickly by hand.

## Final Check Before Saving A Prompt Pack

- Prices match catalog retail and FBM values.
- Featured-configuration prices, such as K's current $240 price, are labeled as featured-only when used in image text.
- Set or bundle savings graphics show only approved separate-item totals, approved set prices, and approved savings amounts.
- SKU/product names match catalog truth.
- At least one image or graphic contains numeric dimensions when approved dimensions exist.
- Dimensions/details graphics include numeric dimensions, not count-only wording such as `set of 3`.
- Approved catalog image path is present.
- Suggested filename is present for each image prompt.
- Filenames are outside the prompt text, placed in their own filename-only codebox, and never embedded inside the prompt codebox.
- Every copied prompt is standalone and does not require access to repository files or unnamed reference guidance.
- Every copied prompt says what the image is for and what buyer question the image answers.
- Every generated product photo prompt names a camera angle, framing/crop intent, lighting/tone, and practical color environment.
- Every generated product prompt explicitly requires realistic proportions controlled by the approved attachment.
- Any K / Cedar Raised Garden Bed product photo or product-inset prompt places the bed over soil, grass, garden bed ground, or yard/garden surface and explicitly avoids porch/deck/patio/concrete/hard-surface staging.
- Every photo prompt contains the standalone Drakkar visual direction.
- Every graphic prompt contains the chosen background color, remaining approved palette hex values without role assignments, the Marketplace wording direction, typography direction, and literal in-image text.
- Text-overlay default is followed or any override is documented: 8-image packs usually use 3 text-overlay images; 10-image packs usually use 4.
- In-image text is literal and factual.
- Every text-bearing graphic prompt includes the required Marketplace typography direction and role-specific hierarchy.
- Product names are largest when present; price/details are medium; notes are smaller.
- Small text is clean and undistressed, with mobile-readable contrast and spacing.
- Graphic negative/avoid lines stay short and visual; do not add style-category lists the image model cannot reliably interpret.
- In-image text does not include SKU numbers or SKU letters.
- No Claude-owned listing prose is presented as final.
- Media truth is clear.
- Review mode says review by exception.
- Prompt pack is usable directly in ChatGPT Image 2 without requiring Canva/Figma/HTML setup.
