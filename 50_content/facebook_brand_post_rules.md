# Social Brand Post Rules

Status: Active operational rules
Scope: Facebook Page + Instagram feed brand-post image planning, variation, graphic-text ownership, dual-channel Claude handoff prep, and rotation tracking
Channel role: trust, brand awareness, local credibility, engagement, seasonal inspiration, and handmade-shop proof

Use this file for shared Facebook Page + Instagram feed brand-post visuals. It is not a separate brand guide and does not own reusable Drakkar identity rules.

## Source Routing

- Brand identity source of truth: `00_brand/`
- Brand voice and Brand Post Mode: `00_brand/VOICE.md`
- Color palette: `00_brand/COLOR_PALETTE.md`
- Typography and text appearance: `00_brand/TEXT_STYLE_RULES.md`
- Visual direction: `00_brand/VISUAL_STYLE.md`
- Content record template: `80_templates/social_post_template.md`
- Active social brand-post generator: `50_content/prompts/prompt_social_brand_post_generator_v2.0.md`
- Legacy Facebook-only generator: `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md`
- Claude social post-copy prompt template: `80_templates/claude_final_social_post_copy_prompt.md`
- Standalone external-prompt gate: `80_templates/standalone_external_prompt_checklist.md`
- SKU activation gate: `30_products/sku_activation_index.md`
- Daily social cadence tracker: `50_content/social_post_cadence_tracker.md`

Use repository paths only for internal preparation. Every prompt delivered to an external image model must inline its relevant brand direction, exact colors, typography direction, literal in-image text, constraints, attachments, output requirements, quality criteria, and failure behavior. Exact colors must include one chosen background color or photo/overlay background treatment first. After that, list the remaining approved palette colors only; do not assign them to text, dividers/rules, accents, panels, or inset fields.

## Fast Path For Short Operator Requests

When the operator asks for a "brand post for today," "fb brand post," "ig brand post," "Facebook brand post," "Instagram brand post," or similar short request, treat it as a shared Facebook Page + Instagram feed brand-post workflow request unless they explicitly say Marketplace, ad, single-channel only, Story/Reel, or another channel.

Use this fast path before broader discovery:

1. Start with the active/open content or prompt file when the operator context clearly points to one.
2. Read this file and `50_content/prompts/prompt_social_brand_post_generator_v2.0.md`.
3. Read the target content record under `50_content/`.
4. Check `30_products/sku_activation_index.md`. A single-product Facebook Page or Instagram feed post may be created only for an `Active` SKU. A scope-based product-family showcase may be created only when every code in `variant_scope` is `Active`.
5. If a linked product is inactive, has no catalog SKU, or has no clean ref file, do not create or deliver a new single-product post prompt. If a scoped variant is inactive, missing a clean ref, or absent from the declared scope, set `scope_activation_status: Blocked` and return `BLOCKED`.
6. If the content record already has `approved_facts_status: Approved`, `platform: FB Page + Instagram`, creative-selection fields, `exact_in_image_text`, `approved_reference_images`, `image_prompt_ref`, `output_aspect_ratio: 4:5`, and valid activation status for its single SKU or complete variant scope, open the saved image prompt and deliver from that rather than rebuilding the concept only when it still matches current social visual rules.
7. If the saved image prompt is missing, the operator asks for a new variation, the saved prompt is Facebook-only but a dual-channel package is needed, or the saved prompt conflicts with a newer visual rule, read only the linked product/listing records and `00_brand/` source files needed to fill missing approved facts, visual direction, palette, typography, or attachment instructions.
8. Check recent rotation with targeted searches across `50_content/content_*.md`; do not run broad repo discovery unless the target content record is unknown.
9. Ask one short clarifying question only when there are multiple plausible target content records and the operator context does not identify which one to use.

Default delivery for a social brand-post request is the filename block, one shared standalone image prompt block, and one Claude handoff block that asks for both `Facebook Page post copy:` and `Instagram caption:`. Deliver only the filename and standalone image prompt when the operator explicitly asks for an image prompt only.

## Ownership Boundary

This file owns:

- Facebook Page + Instagram feed brand-post visual-purpose rules
- mix-and-match creative selection pools
- compatibility and do-not-pair rules
- rotation checks using saved content records
- social brand-post image graphic-text workflow
- dual-channel Claude handoff prep rules
- SKU-specific social visual compatibility rules

This file does not own:

- reusable voice, palette, typography, visual-style, logo, or asset rules
- Facebook Marketplace listing or image-pack rules
- Marketplace pricing-card strategy
- final Facebook Page post copy or Instagram caption text
- product, price, availability, fulfillment, or customization truth

## SKU-Specific Visual Rules

- SKU K / Cedar Raised Garden Bed is an open-bottom raised bed. Any social brand-post image prompt for K must show the raised bed over soil, grass, garden bed ground, or yard/garden surface. Do not place K on porch boards, decks, patios, concrete, pavers, indoor floors, showroom floors, or other hard-surface staging.
- For SKU K, use garden inspiration, backyard garden, side-yard growing, soil/grass, or garden-ground framing. Do not pair K with porch or patio scene/inspiration even though those options are valid for other planter SKUs.

## Copy Ownership

- GPT/Codex may create short customer-facing image graphic text for social brand posts under review by exception.
- Image graphic text does not require Claude approval.
- Record the final literal image wording in `exact_in_image_text`.
- Use approved facts only and follow Brand Post Mode from `00_brand/VOICE.md`.
- Claude remains responsible for final Facebook Page post copy, Instagram captions, and other final customer-facing prose outside the image graphic.
- Do not ask Claude to approve image prompts or image graphic text.
- When a social brand post is requested, GPT/Codex may prepare the standalone Claude final-copy handoff prompt from approved facts, but must not write the final post copy or caption.

Allowed image graphic text may include:

- short headlines
- short supporting lines
- factual labels
- short calls to action
- local or handmade positioning supported by approved facts
- product, process, material, or seasonal wording supported by approved facts

### Social Material Wording

- For Facebook Page and Instagram brand posts, when approved facts would normally say `Pine` or `pine`, use `Solid wood` or `solid wood` instead in customer-facing brand-post wording.
- Apply this to image graphic text, final-post Claude handoffs, Facebook Page post-copy instructions, and Instagram caption instructions.
- Do not ask Claude to say `pine` in brand-post final copy. Tell Claude to use `Solid wood` or `solid wood` anywhere a pine material reference would otherwise appear, and to avoid calling the product cedar unless cedar is the approved material.
- Internal product records, source facts, Marketplace/spec contexts, and visual-reference notes may still retain the exact material/species when needed for truth and traceability.

### Image Text Quality Floor

- Image text must be concrete and earn its place through an approved product use, form, material, feature, or scene.
- Prefer useful, product-specific language such as `Give your vines somewhere to go` for a trellis over vague, interchangeable lifestyle slogans.
- Do not recommend generic mood statements that could apply to any garden product unless Lauren explicitly supplies that wording.

Do not generate:

- unsupported quality, durability, sourcing, availability, timing, pricing, discount, or customization claims
- first-person wording
- banned or suspect wording from `00_brand/VOICE.md`
- long paragraphs
- Marketplace-style price cards unless the operator specifically requests a price-focused Facebook Page post
- website URLs unless specifically requested and approved

## Chat Delivery Rule

When the operator requests a social brand post, deliver the working assets in chat as separate blocks:

- filename in its own filename-only code block
- shared Facebook Page + Instagram feed image prompt in its own copy-ready prompt code block
- Claude dual-channel final-copy handoff prompt in its own copy-ready text or prompt code block

Do not combine the filename, image prompt, and Claude prompt in one code block. Do not embed the filename inside the image prompt. The Claude prompt must be a standalone final-copy handoff only: inline approved facts, Brand Post Mode voice rules, banned claims or words, post-shape guidance, and the requirement to return both labeled outputs: `Facebook Page post copy:` and `Instagram caption:`. It must not ask Claude to approve image prompts, image graphic text, generated visuals, or missing-information handling.

The Claude prompt must also carry the Brand Post Mode emotional job explicitly: ask Claude to make the post feel like something specific while staying truthful. Use approved maker, shop, cedar, place, process, product-use, or image-context details to create connection. Avoid bland fact summaries, compliance-checklist captions, generic inspirational language, AI-isms, and common AI tells. The prompt must prohibit em dashes and en dashes in Claude's final output; regular hyphens are okay when needed.

For Facebook Page post copy, the Claude prompt must request a complete organic post body rather than a tiny caption or product-spec paragraph. For Instagram, the Claude prompt must request a shorter feed caption that shares the same approved facts and feeling without duplicating the Facebook post word for word. For process, community, shop-proof, and other non-product-focused posts, it should support a hook, short brand/product/shop/material context, useful body copy, an approved CTA or soft close, optional signature/location line where appropriate, and a short hashtag line. Hashtags are requested by default for both channel outputs: ask Claude for 3 to 5 restrained, relevant hashtags written with leading `#` characters and tied to the product, use, garden/shop context, or local Georgia maker context unless the content record explicitly says `NO_HASHTAGS`. When location wording is useful, use `locally in Georgia` or `Built locally in Georgia`; do not use Lovejoy unless logistics require the exact city or the operator explicitly asks for it. If the operator provides an example of good post copy, preserve that example's social-post energy and structure while using only approved facts for the current post.

Every Claude post-copy handoff prompt must include an internal draft pass: tell Claude to silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a stronger final version as the visible output.

### Product-Focused Problem-Led Handoffs

For a single product, product pair, product family, or approved variant scope, use the product-post shape in `80_templates/claude_final_social_post_copy_prompt.md` for the Facebook Page output, then adapt the same approved facts into a shorter Instagram caption. The Facebook shape starts with a direct, flat product label, then moves through buyer frustration, concrete examples, what the product addresses, quiet pride, placement, approved Georgia fulfillment, and a soft message close. `cedar [product], made to order.` is an example opening, not required literal wording.

Claude chooses the buyer frustration and the concrete examples. Garden products use real plant names or planting uses; non-garden products use concrete places, uses, or situations. Product details, logistics, availability, exclusions, and performance claims still require approved facts.

Product-focused dual-channel handoffs also ask Claude for a short hashtag line in each channel output by default. Use 3 to 5 restrained, relevant hashtags written with leading `#` characters unless `hashtag_notes` explicitly says `NO_HASHTAGS`.

The normal finished post does not include measurements, technical specifications, price, or disclaimers. Recommend an exception only when one materially affects buyer awareness, eligibility, or a genuinely new offer. Before preparing that handoff, return `APPROVAL REQUIRED` with the category, buyer-facing reason, exact allowed fact or wording, and proposed final-post scope. Permit only an approved exception recorded in `post_copy_exception_approval`; do not add other excluded details or disclaimer language.

These are final-post-copy rules only. Do not automatically transfer them to the image prompt or image graphic text; those remain governed by their existing image workflow rules.

## Required Inputs

Before creating a social brand-post image prompt, gather:

- `content_id`
- `platform: FB Page + Instagram`
- active SKU status from `30_products/sku_activation_index.md`
- post objective
- audience or context
- approved facts
- linked product or listing records when relevant
- governed media or approved reference images
- exact clean ref file(s) for the active SKU when product fidelity matters
- for a scope-based product-family showcase: `linked_product_family_id`, exact `variant_scope`, `scope_activation_status`, all individual active clean refs, and an approved `scope_reference_asset` when the image shows the full collection together
- any required product, logo, or layout attachments
- recent social brand-post history with recorded creative-selection fields
- image graphic-text direction, any required literal wording, or a clear decision to use `NO_TEXT`
- `post_copy_exception_approval: None` for normal product posts, or the exact approved exception record when one is authorized
- requested output format; static Facebook Page + Instagram feed brand-awareness default is `4:5`, and Story/Reel output is `9:16` only when explicitly requested

If the linked product is not an active SKU, return `BLOCKED` and list the SKU activation reason. For a scope-based post, return `BLOCKED` unless every listed variant is Active; do not use a scope reference as a substitute for an inactive variant's clean reference. If approved facts are insufficient for the requested message, return `BLOCKED` and list the missing facts. Do not solve missing truth with vague promotional language.

## Mix-And-Match System

Choose one option from each category. Treat these as interoperable creative ingredients, not fixed templates.

### Layout Family

- Dark split panel
- Light catalog card
- Full-photo overlay
- Workshop/process narrative
- Product close-up
- Product family showcase

`Product family showcase` may present a selected `variant_scope`, not an implied full catalog. It must show every and only the active scoped variants, use the approved scope reference for a group composition, and never describe the collection as a bundle unless a separately approved bundle product is linked.
- Minimal logo-forward
- Local badge/label
- Poster-style brand graphic
- Community/thank-you

### Photo Subject

- Single cedar product
- Product pair
- Product trio or family
- Raised garden bed
- Mailbox or post planter
- Mini or tabletop item
- Plant stand
- Raw cedar boards
- Workbench and tools
- Cedar grain close-up
- Product detail, corner, rim, shelf, or post
- Porch or patio scene
- Garden scene
- Seasonal planting arrangement
- Product in progress

### Message Angle

- Handmade-shop proof
- Built-to-order process
- Local Georgia shop
- Approved cedar material detail or benefit
- Porch or patio inspiration
- Garden inspiration
- Approved custom-sizing availability
- One-bench maker process
- Small-business thank-you
- Seasonal refresh
- Product variety
- Construction or craftsmanship detail
- Raw cedar to finished-piece transformation

### Graphic Treatment

- Charcoal textured panel
- Warm stone editorial field
- Cedar-orange accent strip
- Thin catalog divider lines
- Small corner ornaments
- Icon-style feature row
- Maker-mark or stamped-label feel
- Soft photo vignette
- Product cutout on clean background
- Bottom brand strip
- Minimal caption label

### Text Intensity

- `NO_TEXT`
- Brand name or approved logo only
- Minimal: short headline only
- Moderate: headline plus one support line
- Editorial: calm headline plus brief supporting copy
- Poster-style: large short headline plus one compact supporting element

### CTA Style

- No CTA
- Soft engagement
- Order inquiry
- Custom inquiry, only when customization is approved
- Local-support message
- Follow/new-builds message

`cta_style` records the intent and treatment. The final literal CTA belongs in `exact_in_image_text`.

## Selection Rules

- Choose a combination that serves the current post objective and approved facts.
- Let the product, process, or message remain visually clear.
- Use `NO_TEXT` when the image is stronger without graphic wording.
- Keep text short enough to remain readable in both Facebook Page and Instagram feeds.
- Do not treat the combination examples below as templates that must be copied.
- Do not make every post a product sales graphic; rotate product, process, material, local, seasonal, and community subjects.

Example combinations:

- Dark split panel + single cedar product + handmade-shop proof + icon-style feature row
- Light catalog card + raised garden bed + garden inspiration + thin catalog divider lines
- Full-photo overlay + porch scene + seasonal refresh + minimal text
- Workshop/process narrative + raw cedar boards + one-bench maker process + stamped-label feel
- Product close-up + cedar grain detail + craftsmanship detail + minimal caption label
- Community/thank-you + warm shop or product photo + local-support message + no CTA

## Post-Copy Variance Mapping

When a full dual-channel package is requested, first classify whether it is product-focused. Product-focused posts use the fixed problem-led product-post shape for the Facebook Page output and a shorter Instagram caption derived from the same approved facts. Process, community, shop-proof, and other non-product-focused posts use the selected image mix-and-match lane for both channel outputs. Do not ask Claude for multiple options by default; request one strongest Facebook Page post body and one strongest Instagram caption.

Use the fields this way:

- `message_angle` chooses the primary post-copy shape.
- `photo_subject` supplies the concrete scene, material, product, or process detail.
- `layout_family` influences post length and structure.
- `graphic_treatment` influences how much the post should feel like a shop note, garden note, catalog note, or brand proof.
- `text_intensity` controls how much the post should echo or support the image text.
- `cta_style` controls the close: no CTA, soft engagement, order inquiry, local-support close, follow/new-builds close, or custom inquiry when approved.

For product-focused posts, use these fields to supply the buyer context, examples, placement, and CTA without changing the required problem-led order.

Default post-copy lanes:

- **Product spotlight:** use for single products, product pairs, product families, product variety, or clean catalog-style product graphics. Shape: fixed problem-led product-post sequence.
- **Garden/use-scene post:** use the fixed problem-led product-post sequence when the image promotes a product. Retain the scene-first shape only when the post is not product-focused.
- **Local shop proof:** use for handmade-shop proof, local Georgia shop, local badge/label, minimal logo-forward, or community/trust graphics. Shape: place/shop hook, short shop context, product or proof detail, local-support close.
- **Material/process note:** use for cedar material detail, raw cedar boards, product in progress, workshop/process narrative, one-bench maker process, or raw cedar to finished-piece transformation. Shape: material/process hook, shop or bench detail, product relevance, soft close.
- **Craft/detail post:** use for construction, craftsmanship detail, product close-up, cedar grain close-up, rim, corner, shelf, post, or detail imagery. Shape: detail-first hook, why the detail matters visually or practically, restrained close.
- **Community/support post:** use for small-business thank-you, community/thank-you, local-support message, follow/new-builds message, or non-sales trust posts. Shape: warm community hook, short gratitude or activity note, soft local-support or follow close.

For non-product-focused posts, use the selected lane as guidance, not a rigid template. If fields conflict, prioritize `message_angle`, then `photo_subject`, then `cta_style`. Record any exception in `rotation_notes` or the Claude handoff notes when the post-copy lane intentionally diverges from the image concept.

## Rotation Rules

Review the most recent seven social brand-post content records that already have selected creative fields. Include Facebook Page, Instagram, and dual-channel prompt-ready drafts, scheduled posts, and published posts so unpublished work does not accidentally duplicate the next concept.

- Do not reuse the same `layout_family` as either of the two most recent social brand-post concepts unless the current objective requires it.
- Do not repeat the same `photo_subject` more than two concepts in a row.
- Change at least three of these six fields from the immediately previous concept: `layout_family`, `photo_subject`, `message_angle`, `graphic_treatment`, `text_intensity`, and `cta_style`.
- Prefer underused options from the reviewed recent history.
- Do not reuse an exact six-field combination.
- Record a justified exception in `rotation_notes` when a requested product, campaign, or objective requires repetition.
- If recent history is unavailable or incomplete, set `rotation_check_status: Not Enough History`; do not claim repetition was checked.

## Compatibility Rules

- Do not pair a busy product-family showcase with a long text block.
- Do not place small low-contrast text over a full-photo background.
- Do not deliver a graphic prompt that lists palette colors without choosing the actual background color or background treatment.
- Do not tell the image model which palette color to use where except for the chosen background.
- Do not pair a light catalog card with heavy grunge typography.
- Do not place delicate typography on a cluttered workshop background without a clean text field.
- Do not let dramatic poster typography make the product unclear.
- Do not overload minimal logo-forward layouts with badges, icons, or paragraphs.
- Do not pair community or thank-you messages with aggressive sales language.
- Do not pair seasonal lifestyle imagery with unrelated workshop/process wording.
- Do not pair raw-material imagery with finished-product claims unless the composition clearly tells a transformation story.
- Do not use cedar-benefit wording when the visible product appears painted, plastic, metal, or non-cedar.
- Do not imply customization, sizing, availability, or fulfillment options that are not approved facts.
- Do not use product wording that conflicts with the visible product type or scale.
- Do not use cartoon Viking motifs, horned helmets, shields, fantasy runes, or clipart.
- Do not make a social brand post look like a Facebook Marketplace price card unless specifically requested.

## Reference And Media Rules

- Follow the repository media-truth rules.
- Use approved or governed owned media for publishable content.
- Product-specific social posts require an active SKU with a clean ref file in `30_products/sku_activation_index.md`. A scope-based product-family showcase requires every code in `variant_scope` to be Active, plus an approved scope reference when the group is shown together.
- Do not create new social post prompts for inactive/no-SKU products.
- Require an approved source image attachment when exact product fidelity matters.
- Require an approved logo attachment when exact logo fidelity matters.
- Apply the attachment-first requirement in [80_templates/standalone_external_prompt_checklist.md](../80_templates/standalone_external_prompt_checklist.md) whenever an image prompt needs an attachment.
- Do not ask an image model to invent or redraw an exact product or logo from text alone.
- Keep third-party reference media internal and out of publishable content.

## Recordkeeping

Before saving a generated image prompt, update the content record with:

- `layout_family`
- `photo_subject`
- `message_angle`
- `graphic_treatment`
- `text_intensity`
- `cta_style`
- `platform`
- `exact_in_image_text`
- `output_aspect_ratio`
- `facebook_page_publish_status`
- `instagram_publish_status`
- `approved_reference_images`
- `linked_product_family_id`
- `variant_scope`
- `scope_reference_asset`
- `scope_reference_variant_codes`
- `scope_activation_status`
- `sku_activation_status`
- `sku_activation_ref`
- `recent_post_history_ref`
- `rotation_check_status`
- `rotation_notes`
- `image_prompt_ref`

The image prompt may be prepared before the Claude final-copy gate is complete. The overall content asset still cannot become publish-ready until its final Facebook Page post copy, final Instagram caption, channel readiness fields, and all other required checks are complete.
