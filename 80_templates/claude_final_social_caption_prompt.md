# Claude Final Social Caption Prompt Template

Use this template when Claude is needed to write final customer-facing Facebook Page or Instagram caption copy.

## Asset Context

- channel: Facebook Page / Instagram
- asset_type: Social caption
- current_asset:
- asset_id:
- voice_mode: Brand Post

## Internal Preparation Only

- Use `00_brand/VOICE.md` and the applicable content/product records while preparing this prompt.
- Replace every placeholder with the relevant content before delivery.
- Do not send repository paths to Claude.
- The delivered prompt must pass `80_templates/standalone_external_prompt_checklist.md`.

## Fields Needed

- caption:

## Approved Facts Only

- approved_facts:
- audience_or_context:
- offer_or_focus:

## Tone and Constraints

- tone:
- word_limit:
- cta_goal:
- banned_claims_or_words:

## Voice Rules To Include In The Delivered Prompt

- Use Brand Post Mode: allow more feeling, personality, and expressive rhythm while staying grounded and specific.
- Use short maker, shop, cedar, place, or process details when approved and useful.
- Keep the writing plainspoken, specific, local, and unfussy.
- Use short, confident sentences, no first person, and restraint instead of hype.
- Use `cedar` instead of `wood` when cedar is true.
- Do not turn emotional language into hype, fake luxury, or generic inspiration copy.
- Avoid artisan, artisanal, curated, thoughtfully, lovingly, carefully crafted, handcrafted, elevate, experience, journey, story, sustainable, eco-friendly, luxury, bespoke, timeless, heirloom, crafted, and partner-confidential terms.
- Allow `premium` only when it names a material grade, not as a general quality claim.

## Hard Rules

- Write only final customer-facing prose for the requested fields.
- Use approved facts only.
- Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- Do not invent product details, timing, availability, customer outcomes, or local claims.
- Keep the copy aligned to the requested channel and word limit.
- Do not ask for repository files or assume access to them.
- Do not approve or rewrite image prompts, graphic prompts, overlay text, or image graphic text.
- GPT/Codex owns image graphic text under active review-by-exception workflows. This template is only for the final caption text block outside the image.

## Output-Only Rule

- If information is sufficient, return only the requested fields with no explanation.

## Missing-Info Behavior

- If required information is missing, return only:
  - status: BLOCKED
  - missing_info:

## Standalone Delivery Gate

- Inline all approved facts, voice rules, banned wording, constraints, and output requirements.
- Remove all repository-path instructions and all unfilled placeholders before sending the prompt to Claude.
