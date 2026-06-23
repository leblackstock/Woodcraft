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
- post_copy_exception_approval: `None` by default. For a rare approved exception, record `Approved — [measurement/specification/price/disclaimer] — [buyer-facing reason] — [exact allowed fact or wording]`.

## Facebook Page Post Shape

For Facebook Page post copy, ask Claude for a complete organic post body, not a tiny caption or product-spec paragraph.

Default structure for process, community, shop-proof, and other non-product-focused posts:

- opening hook line with some life in it
- short brand, product, shop, or material context
- 1 to 2 useful body paragraphs, depending on the post goal
- CTA only when the record allows it; otherwise use a softer engagement or no-CTA close
- signature, location, or brand line when useful and approved
- hashtag line when useful and requested by the record

If the operator supplies a good example, match the example's social-post energy and structure while rewriting from the current approved facts. Do not copy unapproved claims, prices, promises, locations, included items, or wording from the example.

When a Facebook Page image has selected mix-and-match fields, include the derived post-copy lane in the delivered Claude prompt. The lane should come from the image concept: `message_angle` chooses the primary post-copy shape, `photo_subject` supplies scene/detail, `layout_family` informs length/structure, `text_intensity` controls how much to support the image text, and `cta_style` controls the close.

## Facebook Page Product-Post Shape

Use this branch when the primary subject is one product, a product pair, a product family, or an approved variant scope. It supersedes the default Facebook Page structure above.

- Open with a direct, flat product label. Do not begin with a scene, meditation, or buildup. Example: `cedar [product], made to order.` This is an example of the desired directness, not required literal wording.
- Let Claude choose an ordinary buyer frustration that suits the product and introduce it in plain language, starting from the buyer's problem rather than the product.
- Give two to four concrete examples. For garden products, use real plant names or planting uses. For non-garden products, use concrete uses, places, or situations that fit the product. These examples must not imply unapproved capability, included items, or customer outcomes.
- Say what the product addresses, then add one short line of quiet pride.
- Include one line on where the product goes or gets used.
- When the approved facts include the exact fulfillment wording, include: `Here in Georgia, pickup or local delivery by arrangement.`
- Close with a soft CTA framed as a small human question, then `send me a message.`
- Keep the voice plain, specific, and a little excited. Use short sentences with varied length; fragments are fine. Sound like the person who built it.
- Return only the final post.
- Treat the actual `exact_in_image_text` as image context only. Do not rewrite, validate, or impose post-copy restrictions on the image prompt or its graphic text.

### Product-Post Exceptions

- Default final-post rule: do not include measurements, technical specifications, price, or disclaimers.
- Recommend an exception only when one of those details materially affects buyer awareness, eligibility, or a genuinely new offer, such as a new smaller or larger size, a new low price, or `adults only`.
- If an exception is recommended, stop before preparing the Claude handoff and request Lauren's approval with the category, reason, exact allowed fact or wording, and proposed final-post scope.
- Permit an exception only when `post_copy_exception_approval` records that approval. Include only the approved category and exact fact or wording; all other default exclusions remain in force.
- Do not add disclaimer language to the finished post unless the approved exception explicitly permits that exact eligibility or safety statement.

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
- Use approved facts for product details, logistics, availability, exclusions, and performance claims. Claude may choose the buyer frustration and concrete examples within the product-post shape, but must not turn them into unsupported claims.
- Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- Do not invent product details, timing, availability, customer outcomes, or local claims.
- Do not invent weatherproofing, anchoring, included plants, delivery radius, or customer outcomes.
- For a product-family showcase, write only about the included active variants. Do not imply an entire family is available and do not use bundle, set, savings, discount, or one-price-for-all language unless a separately approved bundle product is the actual subject.
- Keep the copy aligned to the requested channel and word limit.
- Default to one strongest final post-copy or caption output, not multiple options.
- Before producing the visible answer, silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a stronger final version as the visible output.
- Do not use em dashes, en dashes, AI-isms, or common AI tells.
- If the operator explicitly requests variants, make each delivered variant meaningfully different in emotional angle, sentence rhythm, and scene detail.
- Do not ask for repository files or assume access to them.
- Do not approve or rewrite image prompts, graphic prompts, overlay text, or image graphic text.
- GPT/Codex owns image graphic text under active review-by-exception workflows. This template is only for the final Facebook Page post copy or Instagram caption text block outside the image.
- Do not apply the product-post's measurement, specification, price, disclaimer, or exception rules to image prompts or image graphic text.

## Standalone Delivery Gate

- Inline all approved facts, voice rules, banned wording, constraints, and copy-shape guidance.
- Remove all repository-path instructions and all unfilled placeholders before sending the prompt to Claude.
