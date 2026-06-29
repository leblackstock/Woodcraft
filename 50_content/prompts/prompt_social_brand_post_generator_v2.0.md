# Social Brand Post Generator v2.0

Status: Active current generator
Supersedes: `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md`
Purpose: create one shared, standalone ChatGPT Image 2 prompt for a vertical `4:5` social brand-post graphic that works for both Facebook Page and Instagram feed, plus one standalone Claude handoff that asks for both the Facebook Page post body and Instagram caption.

Owner: GPT/Codex orchestration and image-prompt preparation
Delivery scope: internal repository generator; deliver the standalone image prompt it produces, and include one separate standalone Claude dual-channel handoff prompt when the operator requests a post package
Approval mode: Review by exception
Image graphic-text owner: GPT/Codex
Final Facebook Page post-copy owner: Claude
Final Instagram caption owner: Claude
Current image creation path: manual generation in ChatGPT Image 2
Default output: vertical `4:5` static Facebook Page and Instagram feed brand-awareness graphic

Repository files are preparation sources only. Do not tell an external image model, Claude, or another tool to open repository paths.

## Source Priority

Use these internal sources in this order:

1. Approved facts in the current content, product, and listing records
2. `30_products/sku_activation_index.md`
3. `50_content/facebook_brand_post_rules.md`
4. `00_brand/VOICE.md`, using Brand Post Mode for image graphic text
5. `00_brand/COLOR_PALETTE.md`
6. `00_brand/TEXT_STYLE_RULES.md`, using social brand-post text-style guidance
7. `00_brand/VISUAL_STYLE.md`
8. Approved assets and governed media in `00_brand/` or linked operational records
9. Recent social brand-post records with selected creative fields, including Facebook Page, Instagram, and dual-channel records
10. `80_templates/claude_final_social_post_copy_prompt.md` when a Claude final-copy handoff prompt is needed

## Required Inputs

- current social content record
- `platform: FB Page + Instagram` for the default dual-channel package
- active SKU status from `30_products/sku_activation_index.md`, or active status for every code in `variant_scope`
- post objective
- audience or context
- approved facts
- approved or governed media/reference images
- exact clean ref file(s) for the active SKU when product fidelity matters
- for a scope-based family showcase: exact `variant_scope`, individual active clean refs, and approved `scope_reference_asset` when the image shows the full collection together
- recent social creative-history records
- image graphic-text goal, any supplied required literal wording, or `NO_TEXT`
- `post_copy_exception_approval: None` for normal product posts, or the exact approved exception record when one is authorized
- requested output format, if not the static feed default of `4:5`
- `output_aspect_ratio`: use `4:5` for static Facebook Page and Instagram feed graphics, `9:16` only for Story/Reel output, or another explicitly approved requested format

## Fast Path

For short operator requests like "brand post for today," "fb brand post," "ig brand post," or "Facebook brand post," treat the request as a dual Facebook Page + Instagram feed brand-post package unless the operator explicitly asks for a single channel, Marketplace, ad, Story/Reel, or another format.

Fast route:

1. Classify the request. If the operator asks for a brand post, social post, post package, post copy, caption/body, or publish-prep bundle, default to the full three-block delivery: filename, shared standalone image prompt, and Claude dual-channel post-copy/caption handoff. Deliver only the filename and image prompt when the operator explicitly asks for an image prompt only.
2. Open `50_content/facebook_brand_post_rules.md`, this generator, and the target content record.
3. Check `30_products/sku_activation_index.md`. Single-product posts may be created only for SKUs marked `Active`. Scope-based family showcases may be created only when every code in `variant_scope` is `Active`.
4. If the linked product is inactive, has no catalog SKU, or has no clean ref file, do not create or deliver a new product-specific post prompt. If any scoped variant is inactive or missing its individual clean reference, return `BLOCKED` with the scope activation reason.
5. If the target content record already points to a saved `image_prompt_ref`, open that prompt first.
6. Reuse the saved selection audit, filename, attachment reminder, and standalone prompt only when the facts, objective, dual-channel scope, activation status, attachment requirement, output aspect ratio, and current visual rules still match.
7. Rebuild when the operator requests a new variation, the saved prompt is missing, the saved prompt is Facebook-only but a dual-channel package is needed, the facts changed, the attachment requirement changed, SKU activation changed, visual rules changed, or the prompt fails the standalone checklist.
8. For rotation, use targeted searches across `50_content/content_*.md` for the six creative fields instead of broad repo discovery.
9. Read `00_brand/` files only when rebuilding the prompt or when a missing detail must be refreshed.

## Copy Ownership

- GPT/Codex may generate image graphic text directly from approved facts under review by exception.
- Image graphic text does not require Claude approval.
- Follow Brand Post Mode and the shared voice guardrails in `00_brand/VOICE.md`.
- Keep image text short, readable, truthful, and specific.
- Prefer concrete product-use, form, material, feature, process, or scene language instead of vague lifestyle slogans.
- For social brand-post customer-facing wording, convert any `Pine` or `pine` material reference from approved facts into `Solid wood` or `solid wood`. Do not put `pine` in image graphic text, Facebook Page post-copy instructions, or Instagram caption instructions unless Lauren explicitly asks for species/spec wording.
- Record the final literal wording in `exact_in_image_text`.
- Do not generate final Facebook Page post copy or Instagram caption text. Claude owns both final publishable prose outputs.
- When a full dual-channel package is requested, create one standalone Claude handoff prompt that asks for both labeled outputs:
  - `Facebook Page post copy:`
  - `Instagram caption:`
- `NO_TEXT` is an explicit creative choice for images that should have no readable words, not a default restriction and not a requirement caused by Claude ownership.

## Blocked Conditions

Return `BLOCKED` with a concise missing-information list when:

- the target record is not a social content record
- the linked product does not resolve to an active SKU in `30_products/sku_activation_index.md`
- the linked product has no catalog SKU or no clean ref file and the request is product-specific
- any scoped variant is inactive, missing a clean ref, or absent from the declared scope
- a requested claim is not supported by approved facts
- exact product fidelity is required but no approved product reference image is available
- exact logo fidelity is required but no approved logo asset is available
- the requested visual would violate media-truth rules
- required literal wording, dimensions, output aspect ratio, or output requirements cannot be determined safely
- a measurement, specification, price, or disclaimer is recommended for final product-post prose but `post_copy_exception_approval` is not Approved

Recent-post history gaps do not block prompt generation. Set `rotation_check_status: Not Enough History` and do not claim the concept was checked against unavailable history.

## Generator Workflow

1. Confirm the content record, channel scope, and approved facts.
2. Confirm the linked product resolves to an active SKU with clean ref file(s). For a scope-based family showcase, confirm every listed variant is Active and the scope reference is approved when the full group appears together.
3. Confirm `platform: FB Page + Instagram` for the default package and `output_aspect_ratio: 4:5` unless the operator explicitly requested Story/Reel or another approved format.
4. Read the current social brand-post rules and relevant `00_brand/` sources.
5. Review the most recent seven social brand-post records with selected creative fields, including draft, handoff-prepared, scheduled, and published records.
6. Select one option for each creative field: `layout_family`, `photo_subject`, `message_angle`, `graphic_treatment`, `text_intensity`, and `cta_style`.
7. Apply rotation and compatibility rules.
8. Generate concise literal image graphic text from approved facts when the concept needs readable words; choose `NO_TEXT` only when the image should intentionally have no readable text.
9. Identify every required attachment or reference image.
10. Create one standalone external image prompt for a shared Facebook Page and Instagram feed graphic.
11. Run the standalone-prompt and final self-checks.
12. Update the linked content record with the selected fields, `platform`, output aspect ratio, channel publish/status fields, SKU activation status, literal image text, post-copy exception state, history check, attachment refs, and `image_prompt_ref`.
13. If the operator requested a full package, classify the post. For product-focused posts, use the fixed problem-led product-post shape. For process, community, shop-proof, and other non-product-focused posts, derive the post-copy lane from the selected mix-and-match fields.
14. Create one standalone Claude dual-channel final-copy handoff that asks for both labeled outputs.

## Standalone Image Prompt Requirements

Every delivered image prompt must pass `80_templates/standalone_external_prompt_checklist.md` and work without repository access.

The copied prompt must inline:

- the image objective and Facebook Page + Instagram feed use case
- the selected composition and subject
- approved product, material, process, local, or seasonal facts needed for the image
- relevant Drakkar visual direction from active brand sources
- exact relevant palette hex values when the design uses brand graphics or text
- one explicit background choice, including the exact background color or photo/overlay background treatment
- remaining approved palette colors listed without assigning them to text, dividers/rules, accents, panels, labels, ornaments, or inset fields
- relevant social brand-post typography direction when text appears
- the literal `exact_in_image_text`, or an explicit instruction to use no readable text
- required reference-image and attachment instructions
- a first prompt line of `Please see attached "[plain-language item being attached]"` when an attached image is required
- the correct output aspect ratio: `4:5` for static Facebook Page and Instagram feed graphics, `9:16` for Story/Reel output, or another explicitly approved requested format
- mobile-feed readability, material realism, visual hierarchy, and quality criteria
- visible avoid rules
- failure behavior that prohibits invented substitutes when a required attachment, fact, logo, product detail, or literal text cannot be used

Do not copy local paths into the external prompt. Refer to required attachments by their supplied role, such as `the attached approved product reference image` or `the attached approved Drakkar Designs logo`.

### Internal Prompt Construction Shape

Use this structure while generating the external prompt. Replace every bracketed instruction with actual standalone content and remove all brackets before delivery.

```text
[If an attached image is required, start with: Please see attached "[plain-language item being attached]". Omit this line only when no image attachment is required.]

Create a vertical 4:5 Facebook Page and Instagram feed brand-awareness graphic for Drakkar Designs.

Objective and audience:
[Inline the post objective, audience, and dual-channel use case.]

Subject and composition:
[Inline the selected subject, layout family, message angle, graphic treatment, setting, camera direction, and relevant approved facts.]

Reference attachments:
[State which supplied approved images control exact product, logo, or visual fidelity. State when no attachment is required.]

Brand visual direction:
[Inline the relevant current visual direction from the brand source of truth.]

Palette:
[Choose and state the exact background first. Then list the remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, labels, ornaments, or inset fields. Do not tell the image model which color to use where except for the background.]

Typography:
[When text appears, inline the relevant social brand-post typography direction.]

Readable text:
[State NO_TEXT, or list the exact literal wording and require no extra words.]

Output and quality:
[State vertical 4:5 output for both Facebook Page and Instagram feed, mobile-feed readability, material realism, visual hierarchy, and other relevant quality criteria.]

Failure behavior:
[State what the external model must do instead of inventing missing references, facts, product details, logos, or replacement wording.]

Avoid:
[Include only concise, visually controllable avoid instructions.]
```

## Filename Rule

Use:

`{content_id}_social_{layout_or_role_slug}_v01.png`

Use lowercase filenames, underscores between words, and a short layout or role slug.

## Chat Delivery Rule

When the operator requests a dual-channel brand post, deliver these assets in chat as three separate copy-ready blocks:

Filename:

```text
{content_id}_social_{layout_or_role_slug}_v01.png
```

Image prompt:

```text
[One standalone external image prompt for Facebook Page and Instagram feed with no repository-path dependency]
```

Claude prompt:

```text
[One standalone Claude final-copy handoff prompt with no repository-path dependency, approved product facts, Brand Post Mode rules, actual image-text context, the applicable product-post or non-product post shape, and instructions to return both labeled outputs: Facebook Page post copy and Instagram caption]
```

Do not combine these into one block. Do not put the filename inside the image prompt. The Claude prompt is for final Facebook Page post copy and Instagram caption only and must not ask Claude to approve image prompts, image graphic text, or generated visuals.

## Claude Dual-Channel Handoff Requirements

When generating the Claude prompt for a dual-channel package:

- Keep the prompt clean and usable, not a long compliance dump.
- Ask Claude for exactly two labeled outputs:
  - `Facebook Page post copy:`
  - `Instagram caption:`
- Ask for one strongest output per channel, not multiple options.
- Tell Claude the Facebook Page output must be a complete organic post body, not a tiny caption or product-spec paragraph.
- Tell Claude the Instagram output must be a shorter feed caption that shares the same approved facts and feeling, but is not a copy-paste duplicate of the Facebook post.
- Ask Claude to end each channel output with 3 to 5 restrained, relevant hashtags written with leading `#` characters unless the content record explicitly says `NO_HASHTAGS`.
- Classify the post first. Product-focused posts use the fixed problem-led product-post shape for the Facebook Page output, then adapt the same approved facts into a shorter Instagram caption. Non-product-focused posts derive both outputs from the selected mix-and-match fields.
- For product-focused Facebook Page post copy, require a direct flat product-label opening, buyer frustration, two to four concrete examples, what the product addresses, quiet pride, placement, approved Georgia fulfillment, and a soft message close. `cedar [product], made to order.` is an example opening, not required literal wording.
- Let Claude choose the buyer frustration and concrete examples. Use real plant names or planting uses for garden products; use concrete uses, places, or situations for non-garden products. Do not let those choices create unsupported product claims, inclusions, or customer outcomes.
- For Instagram, keep the caption visual-first, shorter, and natural for the feed while preserving approved facts and the same CTA limits.
- Treat the image context and literal image graphic text as context only. Do not rewrite, validate, or apply final-post restrictions or exception rules to the image prompt or image graphic text.
- If approved facts say `Pine` or `pine`, tell Claude to use `Solid wood` or `solid wood` in both outputs anywhere that material would otherwise be named. Do not ask Claude to say `pine`, and do not call the product cedar unless cedar is the approved material.
- For Facebook Page copy, use `locally in Georgia` or `Built locally in Georgia` when location wording is useful; do not use Lovejoy unless logistics require the exact city or the operator explicitly asks for it.
- Require no first person, no hard-sell CTA unless approved, no invented facts, no em dashes or en dashes, no AI-isms or common AI tells, and no generic inspirational language.
- Explicitly prohibit invented weatherproofing, anchoring, included plants, delivery radius, or customer outcomes.
- Default final product-post prose to no measurements, technical specifications, price, or disclaimers unless `post_copy_exception_approval` records the exact approved exception.
- Tell Claude to silently write several internal versions for each channel, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write stronger final visible outputs.

## Required Delivery Format

Return this internal delivery structure:

Selection audit:

```text
- platform: FB Page + Instagram
- layout_family:
- photo_subject:
- message_angle:
- graphic_treatment:
- text_intensity:
- cta_style:
- exact_in_image_text:
- output_aspect_ratio: 4:5
- post_copy_exception_approval:
- linked_product_family_id:
- variant_scope:
- scope_reference_asset:
- scope_reference_variant_codes:
- scope_activation_status:
- sku_activation_status:
- sku_activation_ref:
- recent_post_history_ref:
- rotation_check_status:
- rotation_notes:
- approved_reference_images:
```

Filename:

```text
{content_id}_social_{layout_or_role_slug}_v01.png
```

Image prompt:

```text
[One standalone external image prompt with no repository-path dependency]
```

Claude prompt:

```text
[One standalone Claude final-copy handoff prompt requesting Facebook Page post copy and Instagram caption]
```

The filename, selection audit, and Claude prompt stay outside the copied image prompt.

## Final Checks

Before saving or delivering the prompt, confirm:

- the concept serves the current post objective for both Facebook Page and Instagram feed
- the linked product is an active SKU with clean ref file(s), or every variant in `variant_scope` is Active and the group image has an approved scope reference
- all six creative fields are selected and recorded
- `platform: FB Page + Instagram` is recorded for a dual package
- the output aspect ratio is recorded as `4:5` for static feed use unless another approved format was explicitly requested
- the rotation check is truthful across recent social brand-post records
- compatibility rules pass or an exception is recorded
- image graphic text uses approved facts and Brand Post Mode
- customer-facing social material wording uses `Solid wood` or `solid wood` instead of `Pine` or `pine` wherever pine would otherwise be said
- the image prompt says `Facebook Page and Instagram feed brand-awareness graphic`
- the prompt contains the literal image text or explicitly requests no readable text
- the prompt contains no local-path instruction
- relevant palette, typography, and visual direction are inlined
- the prompt explicitly chooses the background color or photo/overlay background treatment
- the prompt lists remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, labels, ornaments, or inset fields
- required attachments are explicit
- any required image attachment is named in a first-line `Please see attached "[plain-language item being attached]"` prompt reminder
- exact fidelity is not promised without a required reference attachment
- visible avoid rules are concise and controllable
- failure behavior prohibits invented substitutes
- the Claude handoff asks for both labeled outputs and does not ask Claude to approve image graphic text
- final-post restrictions and exception rules have not been copied into the image prompt or image graphic-text instructions
