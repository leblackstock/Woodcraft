# 05 Channel Strategy

Each channel has one primary job. We avoid spreading effort evenly across everything.

Brand-specific channel assets, graphics, ads, copy, HTML, templates, prompt packs, and generated visuals must reference [00_brand/](00_brand/) for current voice, color palette, visual style, logos, approved photos, and provenance.

Any channel prompt intended for an external AI or tool must pass [80_templates/standalone_external_prompt_checklist.md](80_templates/standalone_external_prompt_checklist.md). Prepare from repository sources, then inline the relevant facts, brand/voice/visual rules, required wording, constraints, attachment instructions, output format, quality criteria, and failure behavior before delivery.

## Voice Mode Routing

Drakkar Designs uses one shared voice from `00_brand/VOICE.md`. Channel modes adjust emphasis without overriding the core voice or approved-fact rules.

| Asset or interaction | Voice mode |
| --- | --- |
| Retail catalog, product book, or catalog-style blurb | Catalog |
| Facebook Page, Instagram, maker/process, or trust-building social post | Brand Post |
| Facebook Marketplace title, description, or factual listing text | Marketplace |
| Buyer message, quote follow-up, coordination, or customer-service response | Customer Reply |

## Facebook Marketplace (Primary Sales Channel)

**Use for:**
- local demand capture
- direct buyer conversations
- fast listing iteration and pricing validation
- primary weekly sales execution

**Do not use for:**
- brand storytelling as the main objective
- complex ad funnels early

## Facebook Page (Trust + Support Channel)

**Use for:**
- proof of activity and legitimacy
- before/after projects and customer proof
- reposting key offers from Marketplace in trust-building format

**Operational image system:**
- Use `50_content/facebook_brand_post_rules.md` and its linked prompt generator for varied, tracked Facebook Page brand-post graphics.
- GPT/Codex may create image graphic text under review by exception; Claude remains responsible for final Facebook Page captions.

**Do not use for:**
- replacing Marketplace listing discipline

## Instagram (Visual Trust + Discovery Support)

**Use for:**
- visual portfolio
- local credibility
- repurposed content from product/listing workflow

**Do not use for:**
- high-effort custom content that cannot be reused

## TikTok / YouTube Shorts (Optional Attention Layer)

**Use for:**
- low-effort, reusable short-form content
- workshop snippets, build process, transformations

**Do not use for:**
- daily unique production demands
- strategy that steals time from listings/sales

## Etsy (Secondary, Shippable Winners)

**Use for:**
- proven small products that ship safely and profitably
- incremental diversified revenue

**Do not use for:**
- large/heavy local-first products
- unproven SKUs without cost and shipping math

## Google Ads (Later-Phase Testing Only)

**Use for:**
- controlled tests on products already proven organically
- small-budget validation with clear stop conditions

**Do not use for:**
- early-stage product discovery
- rescuing weak products with ad spend

## Cross-Channel Rule

- Create once, reuse many times.
- Marketplace listing work should feed Page + Instagram content.
- Only add optional channels after core weekly Marketplace execution is stable.
