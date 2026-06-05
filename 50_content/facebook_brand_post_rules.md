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
- Standalone external-prompt gate: `80_templates/standalone_external_prompt_checklist.md`

Use repository paths only for internal preparation. Every prompt delivered to an external image model must inline its relevant brand direction, exact colors, typography direction, literal in-image text, constraints, attachments, output requirements, quality criteria, and failure behavior.

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
- final Facebook Page captions
- product, price, availability, fulfillment, or customization truth

## Copy Ownership

- GPT/Codex may create short customer-facing image graphic text for Facebook Page brand posts under review by exception.
- Image graphic text does not require Claude approval.
- Record the final literal image wording in `exact_in_image_text`.
- Use approved facts only and follow Brand Post Mode from `00_brand/VOICE.md`.
- Claude remains responsible for final Facebook Page captions and other final customer-facing prose outside the image graphic.
- Do not ask Claude to approve image prompts or image graphic text.

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

## Required Inputs

Before creating a Facebook brand-post image prompt, gather:

- `content_id`
- post objective
- audience or context
- approved facts
- linked product or listing records when relevant
- governed media or approved reference images
- any required product, logo, or layout attachments
- recent Facebook Page post history with recorded creative-selection fields
- image graphic-text direction, any required literal wording, or a clear decision to use `NO_TEXT`
- requested output format; default is square `1:1`

If approved facts are insufficient for the requested message, return `BLOCKED` and list the missing facts. Do not solve missing truth with vague promotional language.

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
- Require an approved source image attachment when exact product fidelity matters.
- Require an approved logo attachment when exact logo fidelity matters.
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
- `recent_post_history_ref`
- `rotation_check_status`
- `rotation_notes`
- `image_prompt_ref`

The image prompt may be prepared before the Claude caption gate is complete. The overall content asset still cannot become publish-ready until its final caption and all other required checks are complete.
