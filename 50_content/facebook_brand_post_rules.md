# Facebook Page Brand Post Rules

Status: Active operational rules
Scope: Facebook Page brand-post image planning, variation, graphic-text ownership, and rotation tracking
Channel role: trust, brand awareness, local credibility, engagement, seasonal inspiration, and handmade-shop proof

Use this file for Facebook Page brand-post visuals. It is not a separate brand guide and does not own reusable Drakkar identity rules.

## Source Routing

- Brand identity source of truth: `00_brand/`
- Brand voice and Brand Post Mode: `00_brand/VOICE.md`
- Color palette: `00_brand/COLOR_PALETTE.md`
- Typography and text appearance: `00_brand/TEXT_STYLE_RULES.md`
- Visual direction: `00_brand/VISUAL_STYLE.md`
- Content record template: `80_templates/social_post_template.md`
- Internal image-prompt generator: `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md`
- Claude social post-copy prompt template: `80_templates/claude_final_social_post_copy_prompt.md`
- Standalone external-prompt gate: `80_templates/standalone_external_prompt_checklist.md`
- SKU activation gate: `30_products/sku_activation_index.md`

Use repository paths only for internal preparation. Every prompt delivered to an external image model must inline its relevant brand direction, exact colors, typography direction, literal in-image text, constraints, attachments, output requirements, quality criteria, and failure behavior. Exact colors must include one chosen background color or photo/overlay background treatment first. After that, list the remaining approved palette colors only; do not assign them to text, dividers/rules, accents, panels, or inset fields.

## Fast Path For Short Operator Requests

When the operator asks for a "fb brand post prompt," "Facebook brand post prompt," or similar short request, treat it as a Facebook Page brand-post workflow request unless they explicitly say Marketplace, ad, Instagram, or another channel.

Use this fast path before broader discovery:

1. Start with the active/open content or prompt file when the operator context clearly points to one.
2. Read this file and `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md`.
3. Read the target content record under `50_content/`.
4. Check `30_products/sku_activation_index.md`. Product-specific Facebook Page posts may be created only for SKUs marked `Active` there.
5. If the linked product is inactive, has no catalog SKU, or has no clean ref file, do not create or deliver a new post prompt. Return `BLOCKED` or archive/mark the draft as inactive.
6. If the content record already has `approved_facts_status: Approved`, creative-selection fields, `exact_in_image_text`, `approved_reference_images`, `image_prompt_ref`, and active SKU status, open the saved image prompt and deliver from that rather than rebuilding the concept.
7. If the saved image prompt is missing or the operator asks for a new variation, read only the linked product/listing records and `00_brand/` source files needed to fill missing approved facts, visual direction, palette, typography, or attachment instructions.
8. Check recent rotation with targeted searches across `50_content/content_fbpage_*.md`; do not run broad repo discovery unless the target content record is unknown.
9. Ask one short clarifying question only when there are multiple plausible target content records and the operator context does not identify which one to use.

Default delivery for a Facebook Page post request is the filename block, standalone image prompt block, and Claude post-copy handoff block. Deliver only the filename and standalone image prompt when the operator explicitly asks for an image prompt only.

## Ownership Boundary

This file owns:

- Facebook Page brand-post visual-purpose rules
- mix-and-match creative selection pools
- compatibility and do-not-pair rules
- rotation checks using saved content records
- Facebook brand-post image graphic-text workflow

This file does not own:

- reusable voice, palette, typography, visual-style, logo, or asset rules
- Facebook Marketplace listing or image-pack rules
- Marketplace pricing-card strategy
- final Facebook Page post copy
- product, price, availability, fulfillment, or customization truth

## Copy Ownership

- GPT/Codex may create short customer-facing image graphic text for Facebook Page brand posts under review by exception.
- Image graphic text does not require Claude approval.
- Record the final literal image wording in `exact_in_image_text`.
- Use approved facts only and follow Brand Post Mode from `00_brand/VOICE.md`.
- Claude remains responsible for final Facebook Page post copy and other final customer-facing prose outside the image graphic.
- Do not ask Claude to approve image prompts or image graphic text.
- When a Facebook Page post is requested, GPT/Codex may prepare the standalone Claude post-copy handoff prompt from approved facts, but must not write the final post copy.

Allowed image graphic text may include:

- short headlines
- short supporting lines
- factual labels
- short calls to action
- local or handmade positioning supported by approved facts
- product, process, material, or seasonal wording supported by approved facts

Do not generate:

- unsupported quality, durability, sourcing, availability, timing, pricing, discount, or customization claims
- first-person wording
- banned or suspect wording from `00_brand/VOICE.md`
- long paragraphs
- Marketplace-style price cards unless the operator specifically requests a price-focused Facebook Page post
- website URLs unless specifically requested and approved

## Chat Delivery Rule

When the operator requests a Facebook Page post, deliver the working assets in chat as separate blocks:

- filename in its own filename-only code block
- image prompt in its own copy-ready prompt code block
- Claude post-copy handoff prompt in its own copy-ready text or prompt code block

Do not combine the filename, image prompt, and Claude prompt in one code block. Do not embed the filename inside the image prompt. The Claude prompt must be a standalone final Facebook Page post-copy handoff only: inline approved facts, Brand Post Mode voice rules, banned claims or words, and post-shape guidance. It must not ask Claude to approve image prompts, image graphic text, generated visuals, or missing-information handling.

The Claude prompt must also carry the Brand Post Mode emotional job explicitly: ask Claude to make the post feel like something specific while staying truthful. Use approved maker, shop, cedar, place, process, product-use, or image-context details to create connection. Avoid bland fact summaries, compliance-checklist captions, generic inspirational language, AI-isms, and common AI tells. The prompt must prohibit em dashes and en dashes in Claude's final output; regular hyphens are okay when needed.

For Facebook Page post copy, the Claude prompt must request a complete organic post body rather than a tiny caption or product-spec paragraph. It should support a hook, short brand/product/shop/material context, useful body copy, an approved CTA or soft close, optional signature/location line, and hashtags when useful. When location wording is useful, use `locally in Georgia` or `Built locally in Georgia`; do not use Lovejoy unless logistics require the exact city or the operator explicitly asks for it. If the operator provides an example of good post copy, preserve that example's social-post energy and structure while using only approved facts for the current post.

Every Claude post-copy handoff prompt must include an internal draft pass: tell Claude to silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a stronger final version as the visible output.

## Required Inputs

Before creating a Facebook brand-post image prompt, gather:

- `content_id`
- active SKU status from `30_products/sku_activation_index.md`
- post objective
- audience or context
- approved facts
- linked product or listing records when relevant
- governed media or approved reference images
- exact clean ref file(s) for the active SKU when product fidelity matters
- any required product, logo, or layout attachments
- recent Facebook Page post history with recorded creative-selection fields
- image graphic-text direction, any required literal wording, or a clear decision to use `NO_TEXT`
- requested output format; default is square `1:1`

If the linked product is not an active SKU, return `BLOCKED` and list the SKU activation reason. If approved facts are insufficient for the requested message, return `BLOCKED` and list the missing facts. Do not solve missing truth with vague promotional language.

## Mix-And-Match System

Choose one option from each category. Treat these as interoperable creative ingredients, not fixed templates.

### Layout Family

- Dark split panel
- Light catalog card
- Full-photo overlay
- Workshop/process narrative
- Product close-up
- Product family showcase
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
- Keep text short enough to remain readable in the Facebook feed.
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

When a full Facebook Page post package is requested, derive the Claude post-copy lane from the selected image mix-and-match fields. Do not ask Claude for multiple options by default; use the selected lane to request one strongest final Facebook Page post body.

Use the fields this way:

- `message_angle` chooses the primary post-copy shape.
- `photo_subject` supplies the concrete scene, material, product, or process detail.
- `layout_family` influences post length and structure.
- `graphic_treatment` influences how much the post should feel like a shop note, garden note, catalog note, or brand proof.
- `text_intensity` controls how much the post should echo or support the image text.
- `cta_style` controls the close: no CTA, soft engagement, order inquiry, local-support close, follow/new-builds close, or custom inquiry when approved.

Default post-copy lanes:

- **Product spotlight:** use for single products, product pairs, product families, product variety, or clean catalog-style product graphics. Shape: hook, product/use context, useful fact, approved CTA or soft close.
- **Garden/use-scene post:** use for garden inspiration, porch or patio inspiration, seasonal planting, raised beds, porch/patio scenes, and garden scenes. Shape: scene-first hook, feeling/use context, practical product detail, soft close.
- **Local shop proof:** use for handmade-shop proof, local Georgia shop, local badge/label, minimal logo-forward, or community/trust graphics. Shape: place/shop hook, short shop context, product or proof detail, local-support close.
- **Material/process note:** use for cedar material detail, raw cedar boards, product in progress, workshop/process narrative, one-bench maker process, or raw cedar to finished-piece transformation. Shape: material/process hook, shop or bench detail, product relevance, soft close.
- **Craft/detail post:** use for construction, craftsmanship detail, product close-up, cedar grain close-up, rim, corner, shelf, post, or detail imagery. Shape: detail-first hook, why the detail matters visually or practically, restrained close.
- **Community/support post:** use for small-business thank-you, community/thank-you, local-support message, follow/new-builds message, or non-sales trust posts. Shape: warm community hook, short gratitude or activity note, soft local-support or follow close.

Use the selected lane as guidance, not a rigid template. If fields conflict, prioritize `message_angle`, then `photo_subject`, then `cta_style`. Record any exception in `rotation_notes` or the Claude handoff notes when the post-copy lane intentionally diverges from the image concept.

## Rotation Rules

Review the most recent seven Facebook Page content records that already have selected creative fields. Include prompt-ready drafts, scheduled posts, and published posts so unpublished work does not accidentally duplicate the next concept.

- Do not reuse the same `layout_family` as either of the two most recent Facebook Page concepts unless the current objective requires it.
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
- Do not make a Facebook Page brand post look like a Facebook Marketplace price card unless specifically requested.

## Reference And Media Rules

- Follow the repository media-truth rules.
- Use approved or governed owned media for publishable content.
- Product-specific Facebook Page posts require an active SKU with a clean ref file in `30_products/sku_activation_index.md`.
- Do not create new Facebook Page post prompts for inactive/no-SKU products.
- Require an approved source image attachment when exact product fidelity matters.
- Require an approved logo attachment when exact logo fidelity matters.
- If a delivered image prompt requires an attached image, begin the copied prompt with `Please see attached "[plain-language item being attached]"`.
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
- `exact_in_image_text`
- `approved_reference_images`
- `sku_activation_status`
- `sku_activation_ref`
- `recent_post_history_ref`
- `rotation_check_status`
- `rotation_notes`
- `image_prompt_ref`

The image prompt may be prepared before the Claude post-copy gate is complete. The overall content asset still cannot become publish-ready until its final Facebook Page post copy and all other required checks are complete.
