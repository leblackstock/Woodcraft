# Facebook Page Brand Post Image Prompt Generator v1.0

Purpose: create one standalone, copy-ready ChatGPT Image 2 prompt for a Facebook Page brand-post graphic while recording a varied, auditable creative selection in the linked content record. When a full Facebook Page post package is requested, also prepare a separate standalone Claude Facebook Page post-copy handoff prompt.

Owner: GPT/Codex orchestration and image-prompt preparation
Delivery scope: internal repository generator; deliver the standalone image prompt it produces, and include a separate standalone Claude Facebook Page post-copy handoff prompt when the operator requests the post package
Approval mode: Review by exception
Image graphic-text owner: GPT/Codex
Facebook Page post-copy owner: Claude
Current image creation path: manual generation in ChatGPT Image 2
Default output: square `1:1` Facebook Page graphic

## Source Priority

Use these internal sources in this order:

1. Approved facts in the current content, product, and listing records
2. `30_products/sku_activation_index.md`
3. `50_content/facebook_brand_post_rules.md`
4. `00_brand/VOICE.md`, using Brand Post Mode for image graphic text
5. `00_brand/COLOR_PALETTE.md`
6. `00_brand/TEXT_STYLE_RULES.md`, using Facebook Brand Post text-style guidance
7. `00_brand/VISUAL_STYLE.md`
8. Approved assets and governed media in `00_brand/` or linked operational records
9. Recent Facebook Page content records with selected creative fields
10. `80_templates/claude_final_social_post_copy_prompt.md` when a Claude Facebook Page post-copy handoff prompt is needed

Repository files are preparation sources only. Do not tell the external image model to open or follow a repository path.

## Required Inputs

- current Facebook Page content record
- active SKU status from `30_products/sku_activation_index.md`, or for a scope-based family showcase, active status for every code in `variant_scope`
- post objective
- audience or context
- approved facts
- approved or governed media/reference images
- exact clean ref file(s) for the active SKU when product fidelity matters
- for a scope-based family showcase: exact `variant_scope`, individual active clean refs, and approved `scope_reference_asset` when the image shows the full collection together
- recent Facebook Page creative-history records
- image graphic-text goal, any supplied required literal wording, or `NO_TEXT`
- `post_copy_exception_approval: None` for normal product posts, or the exact approved exception record when one is authorized
- requested output format, if not square `1:1`

## Fast Path

For short operator requests like "I need a prompt for fb brand post," do not restart full repository discovery when the target is clear from the open file, current content record, or operator context.

Fast route:

1. Classify the request. If the operator asks for a Facebook Page post, brand post, post package, post copy, caption/body, or publish-prep bundle, default to the full three-block delivery: filename, standalone image prompt, and Claude post-copy handoff. Deliver only the filename and standalone image prompt when the operator explicitly asks for an image prompt only.
2. Open `50_content/facebook_brand_post_rules.md`, this generator, and the target content record.
3. Check `30_products/sku_activation_index.md`. Single-product posts may be created only for SKUs marked `Active`. Scope-based family showcases may be created only when every code in `variant_scope` is `Active`.
4. If the linked product is inactive, has no catalog SKU, or has no clean ref file, do not create or deliver a new single-product post prompt. If any scoped variant is inactive or missing its individual clean reference, return `BLOCKED` with the scope activation reason.
5. If the target content record already points to a saved `image_prompt_ref`, open that prompt first.
6. Reuse the saved selection audit, filename, attachment reminder, and standalone prompt when the facts, objective, single-SKU or full-scope activation status, and applicable visual rules still match.
7. Rebuild only when the operator requests a new variation, the saved prompt is missing, the facts changed, the attachment requirement changed, SKU activation changed, a SKU-specific visual rule changed, or the prompt fails the standalone checklist.
8. For rotation, use targeted `50_content/content_fbpage_*.md` searches for the six creative fields instead of broad file discovery.
9. Read `00_brand/` files only when rebuilding the prompt or when a missing detail must be refreshed.

## Copy Ownership

- Generate image graphic text directly from approved facts under review by exception.
- Follow Brand Post Mode and the shared voice guardrails in `00_brand/VOICE.md`.
- Keep image text short, readable, truthful, and specific.
- Prefer concrete product-use, form, material, feature, or scene language. Do not default to vague, interchangeable lifestyle slogans; use them only when Lauren explicitly supplies the wording.
- Record the final literal wording in `exact_in_image_text`.
- Do not request Claude approval for image graphic text or the image prompt.
- Do not generate the final Facebook Page post copy. Claude owns the post copy.
- When a full Facebook Page post package is requested, create a standalone Claude post-copy handoff prompt. Product claims, logistics, availability, exclusions, and performance claims must use approved facts; Claude may choose the ordinary buyer frustration and concrete examples required by the product-post shape. Do not write the final post copy yourself.
- `NO_TEXT` is an explicit creative choice for images that should have no readable words, not a default restriction and not a requirement caused by Claude ownership.

## Blocked Conditions

Return `BLOCKED` with a concise missing-information list when:

- the target record is not a Facebook Page content record
- the linked product does not resolve to an active SKU in `30_products/sku_activation_index.md`
- the linked product has no catalog SKU or no clean ref file and the request is product-specific
- a requested claim is not supported by approved facts
- exact product fidelity is required but no approved product reference image is available
- exact logo fidelity is required but no approved logo asset is available
- the requested visual would violate media-truth rules
- required literal wording, dimensions, or output requirements cannot be determined safely
- a measurement, specification, price, or disclaimer is recommended for a product post but `post_copy_exception_approval` is not Approved; return `APPROVAL REQUIRED` with the category, buyer-facing reason, exact allowed fact or wording, and proposed final-post scope

Recent-post history gaps do not block prompt generation. Set `rotation_check_status: Not Enough History` and do not claim the concept was checked against unavailable history.

## Generator Workflow

1. Confirm the content record and approved facts.
2. Confirm the linked product resolves to an active SKU with clean ref file(s) in `30_products/sku_activation_index.md`. For a scope-based family showcase, confirm every listed variant is Active and the scope reference is approved when the full group appears together.
3. Read the current Facebook brand-post rules and relevant `00_brand/` sources.
4. Review the most recent seven Facebook Page records with selected creative fields.
5. Select one option for each creative field:
   - `layout_family`
   - `photo_subject`
   - `message_angle`
   - `graphic_treatment`
   - `text_intensity`
   - `cta_style`
6. Apply the rotation and compatibility rules.
7. Generate concise literal image graphic text from approved facts when the concept needs readable words; choose `NO_TEXT` only when the image should intentionally have no readable text.
8. Identify every required attachment or reference image.
9. Create one standalone external image prompt.
10. Run the standalone-prompt and final self-checks.
11. Update the linked content record with the selected fields, SKU activation status, literal image text, post-copy exception state, history check, attachment refs, and `image_prompt_ref`.
12. If the operator requested a full Facebook Page post package, classify it. For a product-focused post, use the fixed problem-led product-post shape and the recorded `post_copy_exception_approval` state. For process, community, shop-proof, and other non-product-focused posts, derive the post-copy lane from the selected mix-and-match fields. Then create the standalone Claude final-post-copy handoff.

## Image Graphic-Text Rules

- Use only approved facts and Brand Post Mode.
- Short headlines, labels, supporting lines, and short calls to action are allowed.
- Do not invent claims, product details, prices, availability, timing, delivery, customization, sourcing, or customer outcomes.
- Do not use first person.
- Do not use banned or suspect wording from the active voice guide.
- Do not include pricing, discounts, sale language, or a website URL unless specifically requested and supported by approved facts.
- Use `NO_TEXT` only when no readable text should appear for that specific image concept.
- When text is used, include the literal wording inside the copied prompt and require no extra words.

## Standalone Prompt Requirements

Every delivered prompt must pass `80_templates/standalone_external_prompt_checklist.md` and work without repository access.

The copied prompt must inline:

- the image objective and Facebook Page use case
- the selected composition and subject
- approved product, material, process, local, or seasonal facts needed for the image
- relevant Drakkar visual direction from the active brand sources
- exact relevant palette hex values when the design uses brand graphics or text
- one explicit background choice, including the exact background color or photo/overlay background treatment
- remaining approved palette colors listed without assigning them to text, dividers/rules, accents, panels, or inset fields
- relevant Facebook Brand Post typography direction when text appears
- the literal `exact_in_image_text`, or an explicit instruction to use no readable text
- required reference-image and attachment instructions
- a first prompt line of `Please see attached "[plain-language item being attached]"` when an attached image is required
- square `1:1` output unless another format was requested
- visible avoid rules
- quality criteria
- failure behavior that prohibits invented substitutes when a required attachment, fact, logo, product detail, or literal text cannot be used

Do not copy local paths into the external prompt. Refer to required attachments by their supplied role, such as `the attached approved product reference image` or `the attached approved Drakkar Designs logo`.

## SKU-Specific Visual Rules

- For SKU K / Cedar Raised Garden Bed, the raised bed is open-bottom and must be shown over soil, grass, garden bed ground, or yard/garden surface. Do not place K on porch boards, decks, patios, concrete, pavers, indoor floors, showroom floors, or other hard-surface staging.
- For SKU K, choose garden/backyard/side-yard/soil/grass framing instead of porch or patio framing, even when generic Facebook Page creative pools include porch or patio options.

## Variant-Scope Family Showcase Rules

Use this mode only when the content record has a `linked_product_family_id` and a non-empty `variant_scope`.

- Show every and only the variants named in `variant_scope`; do not imply the whole product family is available.
- Every scoped variant must be Active in `30_products/sku_activation_index.md` and have its own approved clean reference.
- When the image shows the full selected collection together, attach the approved `scope_reference_asset` as the primary composition control and use the individual clean references as supporting fidelity controls when needed.
- The scope reference never activates a variant and never creates a bundle. Do not use bundle, set, savings, discount, or one-price-for-all wording unless a separately approved bundle product is the actual subject.
- Use the product family's approved facts plus the scoped variants' approved customer-facing facts. Do not include an excluded sibling variation in the image or the Claude post-copy handoff.

### Internal Prompt Construction Shape

Use this structure while generating the external prompt. Replace every bracketed instruction with actual standalone content and remove all brackets before delivery.

```text
[If an attached image is required, start with: Please see attached "[plain-language item being attached]". Omit this line only when no image attachment is required.]

Create a square 1:1 Facebook Page brand graphic for Drakkar Designs.

Objective and audience:
[Inline the post objective, audience, and use case.]

Subject and composition:
[Inline the selected subject, layout family, message angle, graphic treatment, setting, camera direction, and relevant approved facts.]

Reference attachments:
[State which supplied approved images control exact product, logo, or visual fidelity. State when no attachment is required.]

Brand visual direction:
[Inline the relevant current visual direction from the brand source of truth.]

Palette:
[Choose and state the exact background first. Then list the remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, or inset fields. Do not tell the image model which color to use where except for the background.]

Typography:
[When text appears, inline the relevant Facebook Brand Post typography direction.]

Readable text:
[State NO_TEXT, or list the exact literal wording and require no extra words.]

Output and quality:
[State 1:1 output, mobile-feed readability, material realism, visual hierarchy, and other relevant quality criteria.]

Failure behavior:
[State what the external model must do instead of inventing missing references, facts, product details, logos, or replacement wording.]

Avoid:
[Include only concise, visually controllable avoid instructions.]
```

## Reference Attachment Rules

- If exact product fidelity matters, require the approved product image to be attached.
- If exact logo fidelity matters, require the approved logo to be attached.
- If any image attachment is required, the copied prompt must begin with `Please see attached "[plain-language item being attached]"`.
- State what each attachment controls.
- Do not imply that text-only prompting can guarantee an exact product or logo match.
- Keep local asset paths in the surrounding internal audit fields, not inside the copied prompt.

## Visible Avoid Rules

Use only visually controllable avoid instructions, such as:

- wrong product shape, scale, count, material, or finish
- extra products or confusing props
- unreadable or additional text
- cluttered composition
- weak text contrast
- generic corporate or cheap-flyer styling
- Marketplace price-card appearance unless specifically requested
- cartoon Viking motifs, horned helmets, shields, fantasy runes, or clipart
- invented or distorted logos

Do not put repository governance notes inside the external image prompt.

## Filename Rule

Use:

`{content_id}_fbpage_{layout_or_role_slug}_v01.png`

Use lowercase filenames, underscores between words, and a short layout or role slug.

## Chat Delivery Rule

When the operator requests a Facebook Page post, deliver these assets in chat as three separate copy-ready blocks:

Filename:

```text
{content_id}_fbpage_{layout_or_role_slug}_v01.png
```

Image prompt:

```text
[One standalone external image prompt with no repository-path dependency]
```

Claude prompt:

```text
[One standalone Claude final-post-copy handoff prompt with approved product facts, Brand Post Mode rules, actual image-text context, the applicable product-post or non-product post shape, any approved exception only, and internal draft/analyze/improve instruction inlined]
```

Do not combine these into one block. Do not put the filename inside the image prompt. The Claude prompt is for final Facebook Page post copy only and must not ask Claude to approve image prompts, image graphic text, or generated visuals.

## Claude Post-Copy Handoff Prompt Requirements

When generating the Claude prompt for a Facebook Page post package:

- Keep the prompt clean and usable, not a long compliance dump.
- Classify the post first. For a product-focused post, use the fixed problem-led product-post shape in `80_templates/claude_final_social_post_copy_prompt.md`. For a process, community, shop-proof, or other non-product-focused post, derive the post-copy lane from the selected image mix-and-match fields.
- For a product-focused post, require a direct flat product-label opening, buyer frustration, two to four concrete examples, what the product addresses, quiet pride, placement, approved Georgia fulfillment, and a soft message close. `cedar [product], made to order.` is an example opening, not required literal wording.
- Let Claude choose the buyer frustration and concrete examples. Use real plant names or planting uses for garden products; use concrete uses, places, or situations for non-garden products. Do not let those choices create unsupported product claims, inclusions, or customer outcomes.
- Inline product-post voice direction: plain, specific, and a little excited; short varied sentences; fragments are fine; sound like the person who built it. Require Claude to return only the final post.
- Default to no measurements, technical specifications, price, or disclaimers in the finished product post. If one is recommended, return `APPROVAL REQUIRED` before generating the handoff. After approval, permit only the recorded category and exact fact or wording.
- Treat the image context and literal image graphic text as context only. Do not rewrite, validate, or apply final-post restrictions or exception rules to the image prompt or image graphic text.
- For a non-product-focused post, treat `message_angle` as the primary post-copy shape, `photo_subject` as the concrete scene/detail source, `layout_family` as length/structure guidance, `text_intensity` as image-text echo guidance, and `cta_style` as the close/CTA control. Include an appropriate `feeling_target` and `specific_scene_or_connection` grounded in approved facts or image context.
- Default to requesting one strongest final Facebook Page post-copy output.
- Tell Claude to silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a stronger final version as the visible output.
- Do not request multiple post-copy options unless the operator explicitly asks for options or variants.
- If options are explicitly requested, ask for meaningfully different emotional angles, sentence rhythm, and scene details.
- Ask for a complete organic Facebook Page post body, not a tiny caption or product-spec paragraph.
- For non-product-focused posts, include post-shape guidance: opening hook, short brand/product/shop/material context, useful body copy, approved CTA or soft close, optional signature/location line, and hashtags when useful.
- For Facebook Page post copy, use `locally in Georgia` or `Built locally in Georgia` when location wording is useful; do not use Lovejoy unless logistics require the exact city or the operator explicitly asks for it.
- If the operator supplied an example of good Facebook post copy, tell Claude to match its social-post energy and structure while using only current approved facts.
- Require no first person, no hard-sell CTA unless approved, no invented facts, no em dashes or en dashes, no AI-isms or common AI tells, and no generic inspirational language.
- Explicitly prohibit invented weatherproofing, anchoring, included plants, delivery radius, or customer outcomes.
- Require no disclaimer language in a finished product post unless the approved exception explicitly permits that exact eligibility or safety statement.
- Keep the Claude prompt standalone with no repository-path dependency.

## Required Delivery Format

Return this internal delivery structure:

Selection audit:

```text
- layout_family:
- photo_subject:
- message_angle:
- graphic_treatment:
- text_intensity:
- cta_style:
- exact_in_image_text:
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
{content_id}_fbpage_{layout_or_role_slug}_v01.png
```

Prompt:

```text
[One standalone external image prompt with no repository-path dependency]
```

For a full Facebook Page post package, also return:

Claude prompt:

```text
[One standalone Claude final-post-copy handoff prompt with no repository-path dependency, the applicable product-post or non-product post shape, and internal draft/analyze/improve instruction]
```

The filename, selection audit, and Claude prompt stay outside the copied image prompt.

## Final Checks

Before saving or delivering the prompt, confirm:

- the concept serves the current post objective
- the linked product is an active SKU with clean ref file(s) in `30_products/sku_activation_index.md`, or every variant in `variant_scope` is Active and the group image has an approved scope reference
- all six creative fields are selected and recorded
- the rotation check is truthful
- compatibility rules pass or an exception is recorded
- image graphic text uses approved facts and Brand Post Mode
- the prompt contains the literal image text or explicitly requests no readable text
- the prompt contains no local-path instruction
- relevant palette, typography, and visual direction are inlined
- the prompt explicitly chooses the background color or photo/overlay background treatment
- the prompt lists remaining approved palette colors without assigning them to text, dividers/rules, accents, panels, or inset fields
- required attachments are explicit
- any required image attachment is named in a first-line `Please see attached "[plain-language item being attached]"` prompt reminder
- exact fidelity is not promised without a required reference attachment
- visible avoid rules are concise and controllable
- failure behavior prohibits invented substitutes
- the prompt does not ask Claude to approve image graphic text
- the prompt asks for no unsupported claims
- a product-focused final post defaults to no measurements, technical specifications, price, or disclaimers, unless `post_copy_exception_approval` records the exact approved exception
- final-post restrictions and exception rules have not been copied into the image prompt or image graphic-text instructions
