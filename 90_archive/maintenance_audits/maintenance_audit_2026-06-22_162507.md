# Workspace Maintenance Audit

Generated: 2026-06-22T16:25:07-04:00
Scope: live paths only

## Summary

- Errors: 0
- Warnings: 4
- Intentional copies: 24
- Archive searches are excluded unless --include-archive is supplied.

## Possible Mojibake

- **warning** — 20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/RETAIL-CATALOG-NOTES.md: UTF-8 decoding artifacts detected
- **warning** — 20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/uploads/Drakkar Designs Catalog/uploads/Woodcraft_Claude_Product_Sheet_v01.md: UTF-8 decoding artifacts detected
- **warning** — 20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/uploads/Woodcraft_Claude_Product_Sheet_v01.md: UTF-8 decoding artifacts detected
- **warning** — 20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/VOICE.md: UTF-8 decoding artifacts detected

## Repeated Guidance

- **info** — 80_templates/claude_final_customer_reply_prompt.md; 80_templates/claude_final_marketplace_listing_prompt.md; 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Avoid AI-isms and common AI tells. If a phrase, transition, structure, or cadence is commonly recognized as AI-written, do not use it.
- **info** — 80_templates/claude_final_marketplace_listing_prompt.md; 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Avoid artisan, artisanal, curated, thoughtfully, lovingly, carefully crafted, handcrafted, elevate, experience, journey, story, sustainable, eco-friendly, luxury, bespoke, timele
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md; 40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md: intentional standalone or template copy | - Avoid hype words such as artisan, artisanal, bespoke, heirloom, luxury, curated, sustainable, eco-friendly, handcrafted, thoughtfully crafted, lovingly crafted, elevate, experien
- **info** — 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Before producing the visible answer, silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a st
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | - Do not invent other sizes, colors, styles, discounts, finish systems, hardware, delivery fees, lead-time ranges, availability, or durability claims.
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_l_nat_wavy_flag_2026-06-14.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | - Keep the tone direct, practical, local, and free of fake urgency, hype, AI-isms, em dashes, and en dashes. Ordinary hyphens are allowed when needed.
- **info** — 80_templates/claude_final_customer_reply_prompt.md; 80_templates/claude_final_marketplace_listing_prompt.md; 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Remove all repository-path instructions and all unfilled placeholders before sending the prompt to Claude.
- **info** — 00_START_HERE.md; CLAUDE.md: intentional agent-specific instruction copy | - Reusable brand-specific guidance belongs in `00_brand/`; operational records stay in their workflow folders and point back to it.
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_l_nat_wavy_flag_2026-06-14.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | - Silently write and compare several internal sales angles, then return only the strongest final answer.
- **info** — 80_templates/claude_final_marketplace_listing_prompt.md; 80_templates/claude_final_social_post_copy_prompt.md: intentional standalone or template copy | - Treat `current_asset` or `customer_copy_prep_notes` as context only, not as an approved fact source.
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md; 40_listings/prompts/fbm_abc_operator_run_sheet_2026-06-08.md: intentional standalone or template copy | - Use "cedar" as the visible material word. Do not write "Western red cedar" or "western red cedar" in the title or description unless Lauren explicitly asks for the full spec.
- **info** — AGENTS.md; CODEX.md: intentional agent-specific instruction copy | - Use the one shared voice in `00_brand/VOICE.md` and name its applicable Catalog, Brand Post, Marketplace, or Customer Reply mode. Do not create competing channel voice guides or
- **info** — 80_templates/listing_template.md; 80_templates/social_post_template.md: intentional standalone or template copy | - customer_copy_status: Prep Only / Claude Required / Handoff Prepared / Claude Output Pasted Back / Final Integrated
- **info** — 80_templates/listing_template.md; 80_templates/product_candidate_template.md: intentional standalone or template copy | - media_truth_status: Owned Real Photo / Owned AI-Assisted Photo / Concept / Mockup / Third-Party Reference Only
- **info** — 80_templates/listing_template.md; 80_templates/social_post_template.md: intentional standalone or template copy | - scope_reference_variant_codes: Must exactly match `variant_scope` when `scope_reference_asset` is set.
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md; 40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md: intentional standalone or template copy | Brand voice is a guardrail, not the main goal. Keep the copy practical, direct, factual, local when useful, and free of fake hype, but do not make it quieter, prettier, or more bra
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md: intentional standalone or template copy | Copy only the fenced `text` block into Claude. The surrounding repository metadata is internal provenance; the fenced prompt is standalone.
- **info** — 40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md; 40_listings/prompts/prompt_fbm_listing_image_pack_generator_v2.0.md: intentional standalone or template copy | For a custom configurable family with no saved catalog row, use the approved family record, included child-variant records, and listing record as the fact source. Do not invent a c
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | Not currently offered or included: frame, draped version, Wood Burned, Blacked Out, Black & Blue, thin-line, flag-cross, custom dimensions, shipping, installation, wall anchors, we
- **info** — 40_listings/prompts/prompt_usa1_m_nat_clean_reference_generator_2026-06-21.md; 40_listings/prompts/prompt_usa1_s_nat_clean_reference_generator_2026-06-21.md: intentional standalone or template copy | Output a square clean reference suitable for later operator approval and downstream listing-image prompts.
- **info** — 40_listings/prompts/prompt_usa1_m_nat_clean_reference_generator_2026-06-21.md; 40_listings/prompts/prompt_usa1_s_nat_clean_reference_generator_2026-06-21.md: intentional standalone or template copy | Please see attached "USA1-L-NAT clean reference image for the Natural Wood with Red & Blue Stain wavy solid wood American flag family".
- **info** — 40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md; 40_listings/prompts/fbm_image_prompt_pack_wave1_5_2026-06-10.md: intentional standalone or template copy | Use: copy the filename first, generate the image from the prompt, and save the output with that filename. Review by exception only.
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | Write one practical, customer-facing Marketplace listing for the exact product below. Prioritize buyer response, skim clarity, local trust, factual safety, and an easy next step. D
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md; 40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md: intentional standalone or template copy | Write the strongest sellable Facebook Marketplace listing you can from the approved brief below. The goal is buyer response: click-through, skim clarity, trust, search visibility,

## Repair Boundary

Repair only generated indexes, clear relative links, archive-ledger pointers, and encoding in editable canonical files without additional approval. Escalate business-policy conflicts, uncertain ownership, customer-facing copy, published records, and source evidence.
