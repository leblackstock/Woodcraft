# Claude Final Social Post Copy Prompt Template

Use this template when Claude is needed to write final customer-facing Facebook Page post copy or Instagram caption copy.

## Asset Context

- channel: Facebook Page / Instagram
- asset_type: Facebook Page post copy / Instagram caption
- current_asset:
- asset_id:
- voice_mode: Brand Post
- post_copy_lane:

## Internal Preparation Only

- Use `00_brand/VOICE.md` and the applicable content/product records while preparing this prompt.
- Replace every placeholder with the relevant content before delivery.
- Do not send repository paths to Claude.
- The delivered prompt must pass `80_templates/standalone_external_prompt_checklist.md`.

## Fields Needed

- facebook_page_post_copy: one best final output for Facebook Page
- instagram_caption: one best final output for Instagram
- optional_variants: only when the operator explicitly asks for options or variants

## Approved Facts Only

- approved_facts:
- audience_or_context:
- offer_or_focus:
- included_variant_scope: When this post is a product-family showcase, list every included variant's approved customer-facing name, relevant facts, and any allowed choice wording. Otherwise leave blank.
- excluded_variant_scope: When this post is a product-family showcase, list sibling variants that Claude must not mention or imply. Otherwise leave blank.
- selected_image_mix:

## Tone and Constraints

- tone:
- reference_style_or_example:
- feeling_target:
- specific_scene_or_connection:
- post_shape_guidance:
- word_limit:
- location_wording: for Facebook Page, prefer `locally in Georgia` or `Built locally in Georgia`; do not use Lovejoy unless logistics require the exact city or the operator explicitly asks for it
- output_count: default `1`; use more only when the operator explicitly asks for options or variants
- cta_goal:
- hashtag_direction:
- banned_claims_or_words:

## Facebook Page Post Shape

For Facebook Page post copy, ask Claude for a complete organic post body, not a tiny caption or product-spec paragraph.

Default structure:

- opening hook line with some life in it
- short brand, product, shop, or material context
- 1 to 2 useful body paragraphs, depending on the post goal
- CTA only when the record allows it; otherwise use a softer engagement or no-CTA close
- signature, location, or brand line when useful and approved
- hashtag line when useful and requested by the record

If the operator supplies a good example, match the example's social-post energy and structure while rewriting from the current approved facts. Do not copy unapproved claims, prices, promises, locations, included items, or wording from the example.

When a Facebook Page image has selected mix-and-match fields, include the derived post-copy lane in the delivered Claude prompt. The lane should come from the image concept: `message_angle` chooses the primary post-copy shape, `photo_subject` supplies scene/detail, `layout_family` informs length/structure, `text_intensity` controls how much to support the image text, and `cta_style` controls the close.

## Voice Rules To Include In The Delivered Prompt

- Use Brand Post Mode: allow more feeling, personality, and expressive rhythm while staying grounded and specific.
- Use short maker, shop, cedar, place, or process details when approved and useful.
- Make the post feel like something specific instead of simply summarizing facts. Tie the feeling to approved details such as cedar, soil, porch, patio, garden, shop, bench, one pair of hands, local place, or the relief of a useful thing already built.
- Keep the writing plainspoken, specific, local, and unfussy.
- Use short, confident sentences, no first person, and restraint instead of hype.
- Use `cedar` instead of `wood` when cedar is true.
- Use no em dashes or en dashes in final output. Regular hyphens are okay when needed.
- Avoid AI-isms and common AI tells. If a phrase, transition, structure, or cadence is commonly recognized as AI-written, do not use it.
- For Facebook Page post copy, use `locally in Georgia` or `Built locally in Georgia` when location wording is useful; do not use Lovejoy unless logistics require the exact city or the operator explicitly asks for it.
- Do not turn emotional language into hype, fake luxury, or generic inspiration copy.
- Do not write a compliance checklist, bland product summary, or generic inspirational caption.
- Do not write a clipped caption when the channel is Facebook Page; write the full post body that accompanies the image.
- Avoid artisan, artisanal, curated, thoughtfully, lovingly, carefully crafted, handcrafted, elevate, experience, journey, story, sustainable, eco-friendly, luxury, bespoke, timeless, heirloom, crafted, and partner-confidential terms.
- Allow `premium` only when it names a material grade, not as a general quality claim.

## Hard Rules

- Write only final customer-facing prose for the requested fields.
- Use approved facts only.
- Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- Do not invent product details, timing, availability, customer outcomes, or local claims.
- For a product-family showcase, write only about the included active variants. Do not imply an entire family is available and do not use bundle, set, savings, discount, or one-price-for-all language unless a separately approved bundle product is the actual subject.
- Keep the copy aligned to the requested channel and word limit.
- Default to one strongest final post-copy or caption output, not multiple options.
- Before producing the visible answer, silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a stronger final version as the visible output.
- Do not use em dashes, en dashes, AI-isms, or common AI tells.
- If the operator explicitly requests variants, make each delivered variant meaningfully different in emotional angle, sentence rhythm, and scene detail.
- Do not ask for repository files or assume access to them.
- Do not approve or rewrite image prompts, graphic prompts, overlay text, or image graphic text.
- GPT/Codex owns image graphic text under active review-by-exception workflows. This template is only for the final Facebook Page post copy or Instagram caption text block outside the image.

## Standalone Delivery Gate

- Inline all approved facts, voice rules, banned wording, constraints, and copy-shape guidance.
- Remove all repository-path instructions and all unfilled placeholders before sending the prompt to Claude.
