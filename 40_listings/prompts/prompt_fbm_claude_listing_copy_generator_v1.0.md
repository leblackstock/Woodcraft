# FBM Claude Listing Copy Generator Prompt v1.0

Purpose: generate paste-ready Claude prompts for final Facebook Marketplace listing title and description copy using approved catalog facts only.

Owner: GPT/Codex orchestration
Final prose owner: Claude
Use when: a listing record has enough approved facts for a Claude final-copy pass.

## Source Priority

Use sources in this order:

1. Saved Drakkar catalog artifacts in `20_research/catalog_exports/2026-06-03/`
2. Brand source of truth in `00_brand/`
3. Product records in `30_products/`
4. Listing records in `40_listings/`
5. Approved handoff prep packets in `40_listings/`
6. The voice guide at `20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/VOICE.md`

Do not use older product names, older prices, older sizes, older website values, or unsupported draft wording when they conflict with the saved catalog artifacts.

## Output From This Generator

Create a Claude prompt, not final listing copy.

The Claude prompt should request:

- `listing_title`
- `listing_description`

Optional only if needed:

- `faq_notes`
- `buyer_reply_starters`

## Hard Governance Rules

- Claude writes final customer-facing listing prose.
- GPT/Codex prepares facts and the prompt only.
- Use approved facts only.
- If a required fact is missing, mark the Claude prompt `BLOCKED` and list missing facts.
- Do not ask Claude to invent facts, discounts, lead times, delivery promises, materials, finishes, or included items.
- Keep `publish_ready: No` until Claude output is pasted back, integrated, and final operator publish approval is recorded.

## Image Text Boundary

Do not send image-prompt text to Claude for approval unless it is being used as listing prose.

Codex/GPT may generate factual image text under the FBM image prompt workflow. Claude remains responsible for listing title, listing description, captions, CTAs, promo blurbs, and reply copy.

## Voice Guardrails

Use the Drakkar voice guide:

Brand-specific copy, graphic text, ad text, and template language should reference `00_brand/` for current brand asset context, approved photos, and palette/styling notes when those details matter.

- plainspoken
- specific
- local
- unfussy
- no first person
- use `cedar` when cedar is true
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
- Net 30
- MOQ
- partner terms

`premium` may be used only when describing a material grade, such as premium grade pine, not as a general quality claim.

## Standard Claude Prompt Shape

```text
You are writing final Facebook Marketplace listing copy for Drakkar Designs.

Use only the approved facts below. Do not invent dimensions, materials, lead times, discounts, included items, availability, delivery terms, or product claims.

Write in the Drakkar voice:
- plainspoken
- specific
- local
- unfussy
- no first person
- no wholesale/partner terms

Return only:
1. listing_title
2. listing_description

Listing facts:
[facts]

Pricing:
[retail and FBM price rules]

Fulfillment:
[pickup/delivery/lead time]

Do not say:
[banned claims and SKU-specific restrictions]
```

## Batch Prompt Rule

For batches, ask Claude to return one clearly separated block per listing. Each block must include only:

- listing_id
- listing_title
- listing_description

Do not ask Claude to write final image text, captions, or social copy in the same pass.

## Final Check Before Saving A Claude Prompt

- Every price matches catalog truth.
- Retail/FBM labels are defined.
- Product names match catalog truth.
- Dimensions/specs match catalog truth.
- Media facts are not used as unsupported selling claims.
- SKU-specific restrictions are included.
- Prompt asks Claude for listing prose only.
- Prompt does not ask Claude to approve image prompt text.
