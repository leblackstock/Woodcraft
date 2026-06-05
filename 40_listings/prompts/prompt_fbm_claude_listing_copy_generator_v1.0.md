# FBM Claude Listing Copy Generator Prompt v1.0

Purpose: generate paste-ready Claude prompts for final Facebook Marketplace listing title and description copy using approved catalog facts only.

Owner: GPT/Codex orchestration
Final prose owner: Claude
Use when: a listing record has enough approved facts for a Claude final-copy pass.
Delivery scope: internal repository generator; deliver only the standalone Claude prompt it produces, not this generator file

## Source Priority

Use sources in this order:

1. Saved Drakkar catalog artifacts in `20_research/catalog_exports/2026-06-03/`
2. Brand source of truth in `00_brand/`
3. Product records in `30_products/`
4. Listing records in `40_listings/`
5. Approved handoff prep packets in `40_listings/`
6. The voice guide at `00_brand/VOICE.md`

Do not use older product names, older prices, older sizes, older website values, or unsupported draft wording when they conflict with the saved catalog artifacts.

## Output From This Generator

Create a Claude prompt, not final listing copy.

The generated Claude prompt is intended for use outside this repository. It must pass `80_templates/standalone_external_prompt_checklist.md` and work without repository access. Use local files only while preparing it, then inline the relevant facts, Marketplace voice rules, banned wording, constraints, output format, quality criteria, and blocked behavior. Do not tell Claude to open or follow a repository path.

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

Do not send image prompts, graphic prompts, overlay text, or image graphic text to Claude for approval.

Codex/GPT may generate factual image text under the FBM image prompt workflow. If any wording from an image is later reused as a standalone Marketplace listing title, listing description, caption, advertisement, catalog, customer reply, CTA, or promo blurb outside the image, route that separate prose block through Claude.

## Voice Guardrails

Use the one shared Drakkar voice and **Marketplace Mode** at `00_brand/VOICE.md` while preparing the prompt. Marketplace Mode changes emphasis only; it does not override any core voice, banned-word, truthfulness, or approved-fact rule. Inline the applicable rules in the generated Claude prompt.

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
- use Marketplace Mode: direct, practical, factual, and easy to scan
- lead with the product and buyer-relevant details
- plainspoken
- specific
- local
- unfussy
- no first person
- use short, confident sentences and restraint instead of hype
- use "cedar" instead of "wood" when cedar is true
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

Before returning the copy, silently check that every statement is supported by the supplied facts and that all requested fields are present.

If required information is missing, return only:
- status: BLOCKED
- missing_info
```

## Batch Prompt Rule

For batches, ask Claude to return one clearly separated block per listing. Each block must include only:

- listing_id
- listing_title
- listing_description

Do not ask Claude to write or approve image graphic text, image prompts, captions, or social copy in the same listing-copy pass.

## Final Check Before Saving A Claude Prompt

- Every price matches catalog truth.
- Retail/FBM labels are defined.
- Product names match catalog truth.
- Dimensions/specs match catalog truth.
- Media facts are not used as unsupported selling claims.
- SKU-specific restrictions are included.
- Prompt asks Claude for listing prose only.
- Prompt does not ask Claude to approve image prompts, graphic prompts, overlay text, or image graphic text.
- Prompt passes `80_templates/standalone_external_prompt_checklist.md`.
- Prompt contains no instruction to open or follow repository paths.
- Relevant voice rules, banned wording, quality criteria, output format, and blocked behavior are inlined.
