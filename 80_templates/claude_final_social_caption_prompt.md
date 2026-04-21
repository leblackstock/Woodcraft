# Claude Final Social Caption Prompt Template

Use this template when Claude is needed to write final customer-facing Facebook Page or Instagram caption copy.

## Asset Context

- channel: Facebook Page / Instagram
- asset_type: Social caption
- current_asset:
- asset_id:

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

## Hard Rules

- Write only final customer-facing prose for the requested fields.
- Use approved facts only.
- Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- Do not invent product details, timing, availability, customer outcomes, or local claims.
- Keep the copy aligned to the requested channel and word limit.

## Output-Only Rule

- If information is sufficient, return only the requested fields with no explanation.

## Missing-Info Behavior

- If required information is missing, return only:
  - status: BLOCKED
  - missing_info: