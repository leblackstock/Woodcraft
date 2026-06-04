# Claude Final Marketplace Listing Prompt Template

Use this template when Claude is needed to write final customer-facing Facebook Marketplace listing prose.

## Asset Context

- channel: Facebook Marketplace
- asset_type: Marketplace listing
- current_asset:
- asset_id:
- brand_assets_ref: 00_brand/

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

Use `00_brand/` as the current brand asset source of truth for brand-specific references, approved photos, colors, logo context, and styling notes when relevant to the prose. Do not approve or rewrite image prompts unless explicitly requested.

## Hard Rules

- Write only final customer-facing prose for the requested fields.
- Use approved facts only.
- Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- Do not invent pricing, dimensions, materials, lead times, delivery terms, availability, or product claims.
- Do not soften missing facts with guesses.

## Output-Only Rule

- If information is sufficient, return only the requested fields with no explanation.

## Missing-Info Behavior

- If required information is missing, return only:
  - status: BLOCKED
  - missing_info:
