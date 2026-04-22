# QA Review — Who's the Voss Planter Summary

Date: 2026-04-21

## QA Scope

This QA pass re-checked three things in `whosthevoss_planter_summary.md`:

1. **Descriptions** against the captured website wording
2. **Dimensions** to separate verified facts from inference
3. **Suggested pricing** against workspace pricing guardrails and internal draft comps

## QA Result Summary

- **Descriptions:** Mostly pass
- **Dimensions:** Partial pass, with important limitations
- **Pricing:** Partial pass, with two recommended corrections

## 1) Description QA

### Pass

Most descriptions are acceptable high-level summaries of the captured source text.

Examples:
- **Post Planter Box** summary matches source wording about hanging plants, patio lighting, birdhouses, and wind chimes.
- **One Picket Planter** summary matches source wording describing it as tiny/cute.
- **Mailbox Post Planter** summary matches source wording describing it as a variation of the popular post planter with added options.
- **Raised Garden Bed** summary matches the product intent shown on the source page.

### Notes

The descriptions are generally **paraphrases**, not direct quotes. That is fine for a research summary, but they should not be treated as exact marketing copy.

## 2) Dimension QA

### Verified / defensible dimension notes

- **46\" Long Planter Box** → verified from the product name only
- **3 Picket Planter** → verified only as a 3-picket format from the product name
- **One Picket Planter** → verified only as a one-picket format from the product name
- **Tall Planter Box** → verified only as a tall-format naming claim from the product name

### Inferred, not fully verified

- **Post Planter Box** → 4x4-post fit comes from the related YouTube title, not the captured product-page dimension field

### Not dimension data and should not be treated as dimensions

- **Three Tiered Planter** → `six cedar pickets + two 2x4x8s` is a **material clue**, not a finished-size specification

### QA conclusion on dimensions

Most exact finished dimensions remain **unverified / unavailable** from the reviewed public sources. The summary now reflects that more clearly.

## 3) Pricing QA

### Guardrails used

- Medium planters / garden items: **>= $40 profit floor**
- Raised beds / larger local-delivery items: **>= $75 profit floor**
- Existing internal draft comps:
  - Cedar planter box target: **$145**
  - Cedar window box target: **$89**
  - Cedar raised bed target: **$225**
  - Cedar entry bench target: **$275**

### Pricing items that looked reasonable

- **One Picket Planter** at **$35-$45** as a small add-on item
- **46\" Long Planter Box** at **$145-$185**
- **3 Picket Planter** at **$55-$75**
- **Three Tiered Planter** at **$95-$125** because the source itself frames about **$100** as an achievable sale price
- **Tapered Planter Box** at **$125-$165**

### Pricing items adjusted in QA

- **Raised Garden Bed**
  - Prior range: **$150-$225**
  - QA issue: too low against the workspace's own raised-bed draft target and local draft comp range
  - Revised range: **$200-$275**

- **Bench Planter**
  - Prior range: **$175-$275**
  - QA issue: too low on the lower end compared with the workspace's plain cedar entry bench target of **$275**
  - Revised range: **$225-$325**

## Remaining Uncertainties

- Exact finished dimensions are still missing for most products.
- Suggested prices are still **draft research estimates**, not cost-sheet-backed publish prices.
- If you want true publish-ready confidence, the next QA step should be building a **costed spec assumption** for each planter before locking a final single list price.

## QA Verdict

The summary is usable as a **research reference**, but not yet as a publish-ready pricing or specification document. The biggest ongoing weakness is missing verified dimensions, not the descriptions.