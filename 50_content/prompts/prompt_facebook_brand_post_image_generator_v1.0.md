# Facebook Page Brand Post Image Prompt Generator v1.0

Purpose: create one standalone, copy-ready ChatGPT Image 2 prompt for a Facebook Page brand-post graphic while recording a varied, auditable creative selection in the linked content record.

Owner: GPT/Codex orchestration and image-prompt preparation
Delivery scope: internal repository generator; deliver only the standalone image prompt it produces
Approval mode: Review by exception
Image graphic-text owner: GPT/Codex
Caption owner: Claude
Current image creation path: manual generation in ChatGPT Image 2
Default output: square `1:1` Facebook Page graphic

## Source Priority

Use these internal sources in this order:

1. Approved facts in the current content, product, and listing records
2. `50_content/facebook_brand_post_rules.md`
3. `00_brand/VOICE.md`, using Brand Post Mode for image graphic text
4. `00_brand/COLOR_PALETTE.md`
5. `00_brand/TEXT_STYLE_RULES.md`, using Facebook Brand Post text-style guidance
6. `00_brand/VISUAL_STYLE.md`
7. Approved assets and governed media in `00_brand/` or linked operational records
8. Recent Facebook Page content records with selected creative fields

Repository files are preparation sources only. Do not tell the external image model to open or follow a repository path.

## Required Inputs

- current Facebook Page content record
- post objective
- audience or context
- approved facts
- approved or governed media/reference images
- recent Facebook Page creative-history records
- image graphic-text goal, any supplied required literal wording, or `NO_TEXT`
- requested output format, if not square `1:1`

## Copy Ownership

- Generate image graphic text directly from approved facts under review by exception.
- Follow Brand Post Mode and the shared voice guardrails in `00_brand/VOICE.md`.
- Keep image text short, readable, truthful, and specific.
- Record the final literal wording in `exact_in_image_text`.
- Do not request Claude approval for image graphic text or the image prompt.
- Do not generate the final Facebook Page caption. Claude owns the caption.
- `NO_TEXT` is an explicit creative choice for images that should have no readable words, not a default restriction and not a requirement caused by Claude ownership.

## Blocked Conditions

Return `BLOCKED` with a concise missing-information list when:

- the target record is not a Facebook Page content record
- a requested claim is not supported by approved facts
- exact product fidelity is required but no approved product reference image is available
- exact logo fidelity is required but no approved logo asset is available
- the requested visual would violate media-truth rules
- required literal wording, dimensions, or output requirements cannot be determined safely

Recent-post history gaps do not block prompt generation. Set `rotation_check_status: Not Enough History` and do not claim the concept was checked against unavailable history.

## Generator Workflow

1. Confirm the content record and approved facts.
2. Read the current Facebook brand-post rules and relevant `00_brand/` sources.
3. Review the most recent seven Facebook Page records with selected creative fields.
4. Select one option for each creative field:
   - `layout_family`
   - `photo_subject`
   - `message_angle`
   - `graphic_treatment`
   - `text_intensity`
   - `cta_style`
5. Apply the rotation and compatibility rules.
6. Generate concise literal image graphic text from approved facts when the concept needs readable words; choose `NO_TEXT` only when the image should intentionally have no readable text.
7. Identify every required attachment or reference image.
8. Create one standalone external image prompt.
9. Run the standalone-prompt and final self-checks.
10. Update the linked content record with the selected fields, literal image text, history check, attachment refs, and `image_prompt_ref`.

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
- relevant Facebook Brand Post typography direction when text appears
- the literal `exact_in_image_text`, or an explicit instruction to use no readable text
- required reference-image and attachment instructions
- square `1:1` output unless another format was requested
- visible avoid rules
- quality criteria
- failure behavior that prohibits invented substitutes when a required attachment, fact, logo, product detail, or literal text cannot be used

Do not copy local paths into the external prompt. Refer to required attachments by their supplied role, such as `the attached approved product reference image` or `the attached approved Drakkar Designs logo`.

### Internal Prompt Construction Shape

Use this structure while generating the external prompt. Replace every bracketed instruction with actual standalone content and remove all brackets before delivery.

```text
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
[Inline the relevant exact palette hex values when the design uses brand graphics or text.]

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

The filename and selection audit stay outside the copied image prompt.

## Final Checks

Before saving or delivering the prompt, confirm:

- the concept serves the current post objective
- all six creative fields are selected and recorded
- the rotation check is truthful
- compatibility rules pass or an exception is recorded
- image graphic text uses approved facts and Brand Post Mode
- the prompt contains the literal image text or explicitly requests no readable text
- the prompt contains no local-path instruction
- relevant palette, typography, and visual direction are inlined
- required attachments are explicit
- exact fidelity is not promised without a required reference attachment
- visible avoid rules are concise and controllable
- failure behavior prohibits invented substitutes
- the prompt does not ask Claude to approve image graphic text
- the prompt asks for no unsupported claims
