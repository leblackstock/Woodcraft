# Claude Final Marketplace Listing Prompt Template

Use this template when Claude is needed to write final customer-facing Facebook Marketplace listing prose.

## Asset Context

- channel: Facebook Marketplace
- asset_type: Marketplace listing
- current_asset:
- asset_id:
- voice_mode: Marketplace

## Internal Preparation Only

- Use `00_brand/VOICE.md` and the applicable listing/product records while preparing this prompt.
- Replace every placeholder with the relevant content before delivery.
- Do not send repository paths to Claude.
- The delivered prompt must pass `80_templates/standalone_external_prompt_checklist.md`.

## Fields Needed

- listing_title:
- listing_description:

## Approved Facts Only

- product_name:
- approved_facts:
- pricing:
- dimensions:
- materials:
- fulfillment:
- lead_time:
- customization_notes:

## Tone and Guardrails

- tone:
- cta_goal:
- banned_claims_or_words:

## Voice Rules To Include In The Delivered Prompt

- Use Marketplace Mode: direct, practical, factual, and easy to scan.
- Lead with the product and buyer-relevant details.
- Make approved price, size, material, ordering, pickup/delivery, and lead-time details easy to find.
- Keep the writing plainspoken, specific, local, and unfussy.
- Use short, confident sentences, no first person, and restraint instead of hype.
- Use `cedar` instead of `wood` when cedar is true.
- If shop context is needed, describe Drakkar Designs as a small local Georgia woodshop.
- Use no em dashes or en dashes in final output. Regular hyphens are okay when needed.
- Avoid AI-isms and common AI tells. If a phrase, transition, structure, or cadence is commonly recognized as AI-written, do not use it.
- Avoid artisan, artisanal, curated, thoughtfully, lovingly, carefully crafted, handcrafted, elevate, experience, journey, story, sustainable, eco-friendly, luxury, bespoke, timeless, heirloom, crafted, and partner-confidential terms.
- Allow `premium` only when it names a material grade, not as a general quality claim.

## Hard Rules

- Write only final customer-facing prose for the requested fields.
- Use approved facts only.
- Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- Do not invent pricing, dimensions, materials, lead times, delivery terms, availability, or product claims.
- Do not soften missing facts with guesses.
- Before producing the visible answer, silently write several internal versions, analyze them for truthfulness, buyer clarity, voice fit, specificity, natural rhythm, and AI-isms, then write a stronger final version as the visible output.
- Do not use em dashes, en dashes, AI-isms, or common AI tells.
- Do not ask for repository files or assume access to them.
- Do not approve or rewrite image prompts, graphic prompts, overlay text, or image graphic text. This template is only for final Marketplace listing title and description prose outside the image graphic workflow.

## Standalone Delivery Gate

- Inline all approved facts, voice rules, banned wording, constraints, and copy-shape guidance.
- Remove all repository-path instructions and all unfilled placeholders before sending the prompt to Claude.
