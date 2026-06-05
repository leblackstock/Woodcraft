# GPT to Claude Handoff Prompt Template

Use this template when GPT-5.5 reaches a final customer-copy step and must hand off to Claude.

Use this template only after upstream validation is complete.
If required facts are missing, stop upstream and resolve them before Claude handoff.
Do not use this template to ask Claude to polish unsupported draft copy.

## Handoff Eligibility

- approved_facts_status: Approved
- unresolved_fact_gaps: None
- customer_copy_status before handoff: Claude Required or Handoff Prepared

## Handoff Context

- current_asset:
- asset_id:
- current_workflow_step:
- requested_output_fields:
- voice_mode: Catalog / Brand Post / Marketplace / Customer Reply
- inline_voice_rules:
- inline_brand_rules:
- inline_constraints:
- required_output_format:
- required_attachments_or_source_text:

## Internal Preparation Only

- Use `00_brand/` and the applicable operational records while preparing the handoff.
- Do not include repository paths as instructions to Claude.
- Replace every placeholder and inline all relevant source contents before delivery.
- The delivered Claude prompt must pass `80_templates/standalone_external_prompt_checklist.md`.

## Approved Facts Only

- approved_facts:
- pricing:
- dimensions:
- materials:
- fulfillment:
- lead_time:
- channel_context:
- tone_or_brand_notes:
- banned_claims_or_words:

## Shared Drakkar Voice Rules To Inline

- Name and describe the applicable voice mode for each requested output.
- Keep the writing plainspoken, specific, local, and unfussy.
- Use approved facts and truthful claims only.
- Use no first person.
- Prefer short, confident sentences and restraint instead of hype.
- Use `cedar` instead of `wood` when cedar is true.
- Use no em dashes or en dashes in final output. Regular hyphens are okay when needed.
- Avoid AI-isms and common AI tells. If a phrase, transition, structure, or cadence is commonly recognized as AI-written, do not use it.
- Avoid artisan, artisanal, curated, thoughtfully, lovingly, carefully crafted, handcrafted, elevate, experience, journey, story, sustainable, eco-friendly, luxury, bespoke, timeless, heirloom, crafted, and partner-confidential terms.
- Allow `premium` only when it names a material grade, not as a general quality claim.
- Modes adjust emphasis only and never override core voice, banned-word, truthfulness, or approved-fact rules.

## Claude Instructions

- Write only final customer-facing prose for the requested output fields.
- Use approved facts only.
- Do not invent facts, claims, pricing, timing, or commitments.
- Treat any prep wording as non-binding context, not as a fact source.
- Follow the inlined voice, brand, constraint, and output-format rules in this prompt.
- Do not use em dashes, en dashes, AI-isms, or common AI tells in the final copy.
- If required information is missing, return `status: BLOCKED` and list only the missing information.
- Do not ask for repository files or assume access to them.

## Standalone Delivery Gate

- Confirm the delivered prompt contains the actual approved facts, applicable voice-mode rules, banned wording, no-em-dash/no-en-dash rule, no-AI-isms rule, constraints, output format, attachments/source text, quality criteria, and blocked behavior.
- Remove all repository-path instructions and all unfilled placeholders before sending the prompt to Claude.
- Do not ask Claude to approve image prompts, graphic prompts, graphic assets, overlay text, or image graphic text.
- If wording from an image/graphic is later reused as a standalone listing, post/caption, advertisement, catalog, or customer-reply prose block, create a separate Claude handoff for that prose block only.

## After Claude Returns

- Human paste-back is required before workflow continuation.
- Paste the Claude output back into the correct asset, record `claude_output_ref`, and only then integrate final copy.
