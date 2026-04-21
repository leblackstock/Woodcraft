# GPT to Claude Handoff Prompt Template

Use this template when GPT-5.4 reaches a final customer-copy step and must hand off to Claude.

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

## Claude Instructions

- Write only final customer-facing prose for the requested output fields.
- Use approved facts only.
- Do not invent facts, claims, pricing, timing, or commitments.
- Treat any prep wording as non-binding context, not as a fact source.

## After Claude Returns

- Human paste-back is required before workflow continuation.
- Paste the Claude output back into the correct asset, record `claude_output_ref`, and only then integrate final copy.