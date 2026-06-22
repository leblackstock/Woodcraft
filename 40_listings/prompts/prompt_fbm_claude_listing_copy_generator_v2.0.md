# FBM Claude Listing Copy Generator Prompt v2.0

Purpose: generate paste-ready Claude prompts for final Facebook Marketplace listing title and description copy that is optimized to sell, using approved facts only.

Owner: GPT/Codex orchestration
Final prose owner: Claude
Use when: a listing record has enough approved facts for a Claude final-copy pass.
Delivery scope: internal repository generator; deliver only the standalone Claude prompt it produces, not this generator file

## Strategy Change From v1.0

This generator is sellability-first.

Do not make brand voice the main scoring target. Use the Drakkar Marketplace voice as a light guardrail that prevents fake, over-polished, or unsupported copy. The generated Claude prompt should optimize for buyer response, search visibility, skim speed, price clarity, confidence, and an easy next action.

If a choice pits perfect voice-guide fit against a more useful, more clickable, more buyer-relevant Marketplace listing, choose the more sellable version while keeping approved facts, banned wording, no first person, no AI-isms, and truthfulness intact.

## Source Priority

Use sources in this order:

1. Saved Drakkar catalog artifacts in `20_research/catalog_exports/2026-06-03/`
2. Active FBM workflow hub at `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md`
3. Product records in `30_products/`
4. Listing records and approved handoff prep packets in `40_listings/`
5. Brand source of truth in `00_brand/`
6. The voice guide at `00_brand/VOICE.md`

Do not use older product names, older prices, older sizes, older website values, or unsupported draft wording when they conflict with the saved catalog artifacts.

For a custom configurable family with no saved catalog row, use the approved family record, included child-variant records, and listing record as the fact source. Do not invent a catalog price, retail label, or catalog image to fill a missing catalog source.

## Output From This Generator

Create a Claude prompt, not final listing copy.

The generated Claude prompt is intended for use outside this repository. It must pass `80_templates/standalone_external_prompt_checklist.md` and work without repository access. Use local files only while preparing it, then inline the relevant facts, buyer context, Marketplace sellability direction, light voice guardrails, banned wording, constraints, copy-shape guidance, and quality criteria. Do not tell Claude to open or follow a repository path.

Resolve missing facts upstream before creating the Claude prompt. If a required fact is missing, mark the internal generator result `BLOCKED` and list the missing facts outside the Claude prompt.

The Claude prompt should request one strong Marketplace listing title and one strong Marketplace listing description.

Default stance: give Claude a sales brief, not a compliance worksheet. Inline the approved facts and the likely buyer questions, then tell Claude to silently write several internal versions with different sales angles, score them, combine what works, and produce the strongest final listing as the visible output.

Optional only if needed:

- `faq_notes`
- `buyer_reply_starters`

## Optimization Order

Use this order when preparing the Claude prompt:

1. Factual accuracy and approved-source boundaries.
2. Marketplace sellability: click, skim, trust, clarity, and buyer action.
3. Buyer usefulness: price, size, material, included item, pickup/delivery, lead time, customization, and likely use case.
4. Natural local Marketplace readability.
5. Drakkar voice fit as a light guardrail.

Brand mood, poetic restraint, and quiet catalog polish should never weaken a Marketplace listing.

## Sellability Levers To Build Into The Claude Prompt

Ask Claude to make the listing work like a strong local Marketplace listing:

- Put the most buyer-relevant product phrase in the title.
- Use natural search terms a local buyer would actually type, such as cedar planter, raised garden bed, planter box, herb planter, patio planter, or the approved product category.
- Make the first line of the description useful enough to keep a buyer reading.
- Put approved price, size, material, ordering, pickup/delivery, and lead-time information where it is easy to see.
- Use concrete use cases supported by facts, such as porch, patio, herbs, flowers, vegetables, entryway, garden bed, or tabletop use.
- Answer friction points before the buyer asks: what is included, what size it is, whether it is built to order, how to order, and how pickup or local delivery works.
- Include a simple, direct call to action when supported, such as `Message to order`.
- Keep paragraphs short and scannable.
- Prefer useful shopper language over brand-performance language.

Do not invent urgency, scarcity, discounts, durability claims, availability, lead times, delivery promises, included items, finishes, or construction details.

## Hard Governance Rules

- Claude writes final customer-facing listing prose.
- GPT/Codex prepares facts and the prompt only.
- Use approved facts only.
- If a required fact is missing, do not create a Claude prompt. Mark the internal generator result `BLOCKED` and list the missing facts outside the Claude prompt.
- Do not ask Claude to invent facts, discounts, urgency, lead times, delivery promises, materials, finishes, included items, durability claims, or availability.
- Keep `publish_ready: No` until Claude output is pasted back, integrated, and final operator publish approval is recorded.

## SKU-Specific Prompt Rules

- For K / Cedar Raised Garden Bed, state that the raised bed is fully customizable by quote, and make clear that the current size, price, and specs apply only to the featured 72 x 36 x 18 in configuration. Do not let Claude imply custom configurations share the featured price or specs.

## Variant-Scope Listing Mode

Use this mode when a Marketplace listing intentionally offers a selected `variant_scope` from one `product_family_id` without creating a bundle.

- Treat `listing_ref` and `listing_handle` as internal routing labels only. Claude must write a customer-facing title from the approved buyer facts; never expose the internal handle or assume it is suitable title copy.
- Inline every included variant's approved customer name, dimensions, price, finish options, and relevant exclusions. List the included variants in the intended buyer order.
- State plainly that the buyer may choose from the included options. Do not mention or imply family variants outside `variant_scope`.
- If the choices have different prices, ask Claude to make the price differences unmistakable and easy to scan. Do not use bundle, set, savings, discount, or one-price-for-all language unless the offer is a separately approved bundle product.
- Do not create the handoff until every included variant's relevant facts, pricing, and media truth are approved for the scope.

## Image Text Boundary

Do not send image prompts, graphic prompts, overlay text, or image graphic text to Claude for approval.

Codex/GPT may generate factual image text under the FBM image prompt workflow. If any wording from an image is later reused as a standalone Marketplace listing title, listing description, caption, advertisement, catalog, customer reply, CTA, or promo blurb outside the image, route that separate prose block through Claude.

## Brand Voice Role

Use the one shared Drakkar voice and Marketplace Mode at `00_brand/VOICE.md` while preparing the prompt, but do not optimize primarily for sounding branded.

Inline only the voice rules that help Marketplace conversion and fact safety:

- direct, practical, factual, and easy to scan
- plainspoken and specific
- local when relevant
- no first person
- use `cedar` when cedar is true
- use `cedar` as visible customer-facing material wording; do not write `Western red cedar` or `western red cedar` in FBM titles/descriptions unless Lauren explicitly asks for the full spec
- no em dashes or en dashes in final output; regular hyphens are okay when needed
- no AI-isms or common AI tells
- describe Drakkar Designs as a small local Georgia woodshop when shop context is useful
- no wholesale/partner terms in customer-facing copy
- no fake luxury language

Avoid:

- artisan
- artisanal
- curated
- luxury
- sustainable
- eco-friendly
- bespoke
- heirloom
- handcrafted
- thoughtfully crafted
- lovingly crafted
- elevate
- experience
- journey
- story
- Net 30
- MOQ
- partner terms

`premium` may be used only when describing a material grade, such as premium grade pine, not as a general quality claim.

## Standard Claude Prompt Shape

```text
You are writing final Facebook Marketplace listing copy for Drakkar Designs.

Write the strongest sellable Facebook Marketplace listing you can from the approved brief below. The goal is buyer response: click-through, skim clarity, trust, search visibility, and an easy next action.

Brand voice is a guardrail, not the main goal. Keep the copy practical, direct, factual, local when useful, and free of fake hype, but do not make it quieter, prettier, or more brand-like at the expense of selling the product.

Listing type:
 [single-product listing, non-bundle variant-scope listing, bundle listing, master catalog listing, etc.]

Approved facts:
[facts]

Buyer context:
[plain-language use cases, shopper questions, and buyer objections supported by the product facts]

Sales priorities:
- Make the title searchable, concrete, and buyer-relevant.
- Make the first description line carry the product, core use, and strongest approved reason to keep reading.
- Make approved price, size, material, ordering, pickup/delivery, and lead-time information easy to find.
- Use short, scannable paragraphs or natural bullets if they make the listing easier to act on.
- Include a simple direct next step when supported by the facts.

Rules:
- Use only the approved facts.
- Do not invent dimensions, materials, lead times, discounts, urgency, included items, availability, delivery price, guarantees, durability claims, finishes, or construction details.
- Do not mention retail price or discounts unless Lauren explicitly asks for retail-comparison wording.
- Write the listing price as the plain customer-facing price, without Marketplace labels.
- Do not force every fact into the title.
- Use `cedar` as the visible material word. Do not write `Western red cedar` or `western red cedar` in the title or description unless Lauren explicitly asks for the full spec.
- Do not use the phrase "unless otherwise noted" in customer copy.
- Use no em dashes or en dashes; regular hyphens are okay when needed.
- Avoid AI-isms and common AI tells.
- Avoid hype words such as artisan, artisanal, bespoke, heirloom, luxury, curated, sustainable, eco-friendly, handcrafted, thoughtfully crafted, lovingly crafted, elevate, experience, journey, and story.
- Avoid wholesale or partner terms.

Before answering, silently write several internal versions with different sales angles. Score them for buyer response, search usefulness, skim clarity, trust, objection handling, factual safety, natural local rhythm, and banned wording. Combine the best parts into one stronger final version.

Give one listing title and one listing description. No notes, no options.
```

## Batch Prompt Rule

For batches, ask Claude to create one listing per fact set and make each listing easy for the operator to match back to the product. Do not force `listing_id`, `listing_title`, or `listing_description` labels unless the user explicitly needs machine-readable pasteback.

Do not ask Claude to write or approve image graphic text, image prompts, captions, or social copy in the same listing-copy pass.

## Final Check Before Saving A Claude Prompt

- Every price matches catalog truth, or for a custom configurable family without a catalog row, the approved family and scoped variant records.
- Listing price guidance uses plain customer-facing prices; retail comparison is not included unless Lauren explicitly asks for it.
- Product names match catalog truth.
- Dimensions/specs match catalog truth.
- Media facts are not used as unsupported selling claims.
- SKU-specific restrictions are included.
- K prompts, when present, state the fully customizable quote path and featured-configuration-only price/spec boundary.
- Variant-scope prompts list every and only the included variants, their approved customer-facing facts, and their exact approved prices without bundle wording.
- Prompt asks Claude for listing prose only.
- Prompt tells Claude to silently write several internal sales-angle versions, score them, and then produce a stronger final version as the visible output.
- Prompt makes sellability the main scoring target and brand voice a light guardrail.
- Prompt does not ask Claude to approve image prompts, graphic prompts, overlay text, or image graphic text.
- Prompt passes `80_templates/standalone_external_prompt_checklist.md`.
- Prompt contains no instruction to open or follow repository paths.
- Relevant facts, buyer context, sales priorities, voice guardrails, no-em-dash/no-en-dash rule, no-AI-isms rule, and quality criteria are inlined without turning the prompt into a rigid worksheet.
