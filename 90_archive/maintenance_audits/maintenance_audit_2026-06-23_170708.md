# Workspace Maintenance Audit

Generated: 2026-06-23T17:07:08-04:00
Scope: live paths only

## Summary

- Errors: 0
- Warnings: 0
- Intentional copies: 25
- Archive searches are excluded unless --include-archive is supplied.

## Repeated Guidance

- **info** — 80_templates/claude_final_customer_reply_prompt.md; 80_templates/claude_final_marketplace_listing_prompt.md; 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Avoid AI-isms and common AI tells. If a phrase, transition, structure, or cadence is commonly recognized as AI-written, do not use it.
- **info** — 80_templates/claude_final_marketplace_listing_prompt.md; 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Avoid artisan, artisanal, curated, thoughtfully, lovingly, carefully crafted, handcrafted, elevate, experience, journey, story, sustainable, eco-friendly, luxury, bespoke, timele
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md; 40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md: intentional standalone or template copy | - Avoid hype words such as artisan, artisanal, bespoke, heirloom, luxury, curated, sustainable, eco-friendly, handcrafted, thoughtfully crafted, lovingly crafted, elevate, experien
- **info** — 80_templates/claude_final_social_post_copy_prompt.md; 80_templates/gpt_to_claude_handoff_prompt_template.md: intentional standalone or template copy | - Before producing the visible answer, silently write several internal versions, analyze them for truthfulness, voice fit, specificity, natural rhythm, and AI-isms, then write a st
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | - Do not invent other sizes, colors, styles, discounts, finish systems, hardware, delivery fees, lead-time ranges, availability, or durability claims.
- **info** — 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_l_nat_wavy_flag_2026-06-14.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md; 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md: intentional standalone or template copy | - Keep the tone direct, practical, local, and free of fake urgency, hype, AI-isms, em dashes, and en dashes. Ordinary hyphens are allowed when needed.
- **info** — AGENTS.md; CLAUDE.md; CODEX.md: intentional agent-specific instruction copy | - On the first substantive response in each chat, run python 60_automation/workspace_maintenance/session_repo_briefing.py --status.
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

## Workflow Package Trace

- Baseline: initial snapshot.
- Eligible live workflow documents: 69
- Changed workflow documents: 69
- Checks: broken package links, active references to retired files, and non-intentional exact repeated guidance.
- Free-form prose is trace context for human review; this audit does not claim semantic contradictions.

### 00_START_HERE.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — changed workflow document, governance root, outbound link from 02_INDEX.md, outbound link from README.md.
  - `01_VISION.md` — governance root, outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from README.md.
  - `02_INDEX.md` — direct inbound link, outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from README.md.
  - `03_GOVERNANCE.md` — direct inbound link, governance root, outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from README.md.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from 80_templates/cost_sheet_template.md, outbound link from README.md.
  - `05_CHANNEL_STRATEGY.md` — outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from README.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from README.md.
  - `08_AUTOMATION_ROADMAP.md` — outbound link from 02_INDEX.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `09_DATA_MODEL.md` — outbound link from 02_INDEX.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `10_PROMPTS_INDEX.md` — outbound link from 02_INDEX.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `11_WEEKLY_OPERATIONS.md` — outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from README.md.
  - `12_DECISION_LOG.md` — outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 09_DATA_MODEL.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md, outbound link from 14_GLOSSARY.md, outbound link from README.md.
  - `13_BACKLOG.md` — outbound link from 00_START_HERE.md, outbound link from 02_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md, outbound link from README.md.
  - `14_GLOSSARY.md` — outbound link from 02_INDEX.md, outbound link from README.md.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `50_content/facebook_brand_post_rules.md` — outbound link from 02_INDEX.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 05_CHANNEL_STRATEGY.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md, outbound link from 50_content/facebook_brand_post_rules.md.
  - `80_templates/weekly_review_template.md` — outbound link from 11_WEEKLY_OPERATIONS.md.
  - `README.md` — direct inbound link, outbound link from 02_INDEX.md.
- Link evidence:
  - `00_START_HERE.md:34` → `01_VISION.md`
  - `00_START_HERE.md:35` → `03_GOVERNANCE.md`
  - `00_START_HERE.md:36` → `04_BUSINESS_RULES.md`
  - `00_START_HERE.md:37` → `05_CHANNEL_STRATEGY.md`
  - `00_START_HERE.md:38` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `00_START_HERE.md:39` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `00_START_HERE.md:40` → `11_WEEKLY_OPERATIONS.md`
  - `00_START_HERE.md:41` → `13_BACKLOG.md`
  - `00_START_HERE.md:42` → `02_INDEX.md`
  - `00_START_HERE.md:60` → `12_DECISION_LOG.md`
  - `00_START_HERE.md:66` → `01_VISION.md`
  - `00_START_HERE.md:67` → `04_BUSINESS_RULES.md`
  - `00_START_HERE.md:68` → `05_CHANNEL_STRATEGY.md`
  - `00_START_HERE.md:69` → `13_BACKLOG.md`
  - `02_INDEX.md:3` → `00_START_HERE.md`
  - `02_INDEX.md:3` → `00_START_HERE.md`
  - `02_INDEX.md:7` → `README.md`
  - `02_INDEX.md:8` → `00_START_HERE.md`
  - `02_INDEX.md:8` → `00_START_HERE.md`
  - `02_INDEX.md:9` → `01_VISION.md`
  - `02_INDEX.md:10` → `02_INDEX.md`
  - `02_INDEX.md:11` → `03_GOVERNANCE.md`
  - `02_INDEX.md:12` → `04_BUSINESS_RULES.md`
  - `02_INDEX.md:13` → `14_GLOSSARY.md`
  - `02_INDEX.md:17` → `05_CHANNEL_STRATEGY.md`
  - `02_INDEX.md:18` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `02_INDEX.md:19` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `02_INDEX.md:20` → `08_AUTOMATION_ROADMAP.md`
  - `02_INDEX.md:21` → `11_WEEKLY_OPERATIONS.md`
  - `02_INDEX.md:25` → `09_DATA_MODEL.md`
  - `02_INDEX.md:26` → `10_PROMPTS_INDEX.md`
  - `02_INDEX.md:27` → `50_content/facebook_brand_post_rules.md`
  - `02_INDEX.md:28` → `12_DECISION_LOG.md`
  - `02_INDEX.md:29` → `13_BACKLOG.md`
  - `03_GOVERNANCE.md:7` → `00_START_HERE.md`
  - `05_CHANNEL_STRATEGY.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `08_AUTOMATION_ROADMAP.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `08_AUTOMATION_ROADMAP.md:14` → `09_DATA_MODEL.md`
  - `08_AUTOMATION_ROADMAP.md:32` → `11_WEEKLY_OPERATIONS.md`
  - `09_DATA_MODEL.md:12` → `12_DECISION_LOG.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:208` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `11_WEEKLY_OPERATIONS.md:46` → `80_templates/weekly_review_template.md`
  - `11_WEEKLY_OPERATIONS.md:49` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:50` → `13_BACKLOG.md`
  - `13_BACKLOG.md:27` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `13_BACKLOG.md:28` → `10_PROMPTS_INDEX.md`
  - `13_BACKLOG.md:32` → `04_BUSINESS_RULES.md`
  - `13_BACKLOG.md:39` → `08_AUTOMATION_ROADMAP.md`
  - `13_BACKLOG.md:40` → `09_DATA_MODEL.md`
  - `14_GLOSSARY.md:15` → `12_DECISION_LOG.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `50_content/facebook_brand_post_rules.md:317` → `80_templates/standalone_external_prompt_checklist.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:19` → `00_START_HERE.md`
  - `README.md:19` → `00_START_HERE.md`
  - `README.md:20` → `01_VISION.md`
  - `README.md:21` → `03_GOVERNANCE.md`
  - `README.md:22` → `04_BUSINESS_RULES.md`
  - `README.md:23` → `02_INDEX.md`
  - `README.md:27` → `00_START_HERE.md`
  - `README.md:27` → `00_START_HERE.md`
  - `README.md:28` → `01_VISION.md`
  - `README.md:29` → `03_GOVERNANCE.md`
  - `README.md:30` → `04_BUSINESS_RULES.md`
  - `README.md:31` → `05_CHANNEL_STRATEGY.md`
  - `README.md:36` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `README.md:37` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `README.md:38` → `11_WEEKLY_OPERATIONS.md`
  - `README.md:42` → `08_AUTOMATION_ROADMAP.md`
  - `README.md:43` → `09_DATA_MODEL.md`
  - `README.md:44` → `10_PROMPTS_INDEX.md`
  - `README.md:45` → `12_DECISION_LOG.md`
  - `README.md:46` → `13_BACKLOG.md`
  - `README.md:47` → `14_GLOSSARY.md`
  - `README.md:51` → `02_INDEX.md`
- Package findings: none.

### 00_brand/COLOR_PALETTE.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `00_brand/COLOR_PALETTE.md` — changed workflow document.
  - `00_brand/README.md` — direct inbound link.
  - `00_brand/TEXT_STYLE_RULES.md` — direct inbound link.
  - `00_brand/VISUAL_STYLE.md` — direct inbound link.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
- Link evidence:
  - `00_brand/README.md:11` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/TEXT_STYLE_RULES.md:5` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/VISUAL_STYLE.md:5` → `00_brand/COLOR_PALETTE.md`
- Package findings: none.

### 00_brand/README.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `00_brand/COLOR_PALETTE.md` — outbound link from 00_brand/README.md, outbound link from 00_brand/TEXT_STYLE_RULES.md, outbound link from 00_brand/VISUAL_STYLE.md.
  - `00_brand/README.md` — changed workflow document.
  - `00_brand/TEXT_STYLE_RULES.md` — outbound link from 00_brand/README.md, outbound link from 00_brand/VISUAL_STYLE.md.
  - `00_brand/VISUAL_STYLE.md` — outbound link from 00_brand/README.md.
  - `00_brand/VOICE.md` — outbound link from 00_brand/README.md, outbound link from 00_brand/TEXT_STYLE_RULES.md.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `60_automation/workspace_maintenance/ASSET_LOCATOR.md` — outbound link from 00_brand/README.md.
- Link evidence:
  - `00_brand/README.md:11` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/README.md:12` → `00_brand/TEXT_STYLE_RULES.md`
  - `00_brand/README.md:13` → `00_brand/VISUAL_STYLE.md`
  - `00_brand/README.md:14` → `00_brand/VOICE.md`
  - `00_brand/README.md:38` → `60_automation/workspace_maintenance/ASSET_LOCATOR.md`
  - `00_brand/TEXT_STYLE_RULES.md:5` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/TEXT_STYLE_RULES.md:6` → `00_brand/VOICE.md`
  - `00_brand/VISUAL_STYLE.md:5` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/VISUAL_STYLE.md:6` → `00_brand/TEXT_STYLE_RULES.md`
- Package findings: none.

### 00_brand/TEXT_STYLE_RULES.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `00_brand/COLOR_PALETTE.md` — outbound link from 00_brand/TEXT_STYLE_RULES.md.
  - `00_brand/README.md` — direct inbound link.
  - `00_brand/TEXT_STYLE_RULES.md` — changed workflow document.
  - `00_brand/VISUAL_STYLE.md` — direct inbound link.
  - `00_brand/VOICE.md` — outbound link from 00_brand/TEXT_STYLE_RULES.md.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
- Link evidence:
  - `00_brand/README.md:12` → `00_brand/TEXT_STYLE_RULES.md`
  - `00_brand/TEXT_STYLE_RULES.md:5` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/TEXT_STYLE_RULES.md:6` → `00_brand/VOICE.md`
  - `00_brand/VISUAL_STYLE.md:6` → `00_brand/TEXT_STYLE_RULES.md`
- Package findings: none.

### 00_brand/VISUAL_STYLE.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `00_brand/COLOR_PALETTE.md` — outbound link from 00_brand/TEXT_STYLE_RULES.md, outbound link from 00_brand/VISUAL_STYLE.md.
  - `00_brand/README.md` — direct inbound link.
  - `00_brand/TEXT_STYLE_RULES.md` — outbound link from 00_brand/VISUAL_STYLE.md.
  - `00_brand/VISUAL_STYLE.md` — changed workflow document.
  - `00_brand/VOICE.md` — outbound link from 00_brand/TEXT_STYLE_RULES.md.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
- Link evidence:
  - `00_brand/README.md:13` → `00_brand/VISUAL_STYLE.md`
  - `00_brand/TEXT_STYLE_RULES.md:5` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/TEXT_STYLE_RULES.md:6` → `00_brand/VOICE.md`
  - `00_brand/VISUAL_STYLE.md:5` → `00_brand/COLOR_PALETTE.md`
  - `00_brand/VISUAL_STYLE.md:6` → `00_brand/TEXT_STYLE_RULES.md`
- Package findings: none.

### 00_brand/VOICE.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `00_brand/README.md` — direct inbound link.
  - `00_brand/TEXT_STYLE_RULES.md` — direct inbound link.
  - `00_brand/VOICE.md` — changed workflow document.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
- Link evidence:
  - `00_brand/README.md:14` → `00_brand/VOICE.md`
  - `00_brand/TEXT_STYLE_RULES.md:6` → `00_brand/VOICE.md`
- Package findings: none.

### 00_brand/references/PRODUCT_REF_IMAGES_MANIFEST.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `00_brand/references/PRODUCT_REF_IMAGES_MANIFEST.md` — changed workflow document.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
- Link evidence: none.
- Package findings: none.

### 01_VISION.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root.
  - `01_VISION.md` — changed workflow document, governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `05_CHANNEL_STRATEGY.md` — outbound link from 01_VISION.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 05_CHANNEL_STRATEGY.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:34` → `01_VISION.md`
  - `00_START_HERE.md:66` → `01_VISION.md`
  - `01_VISION.md:45` → `05_CHANNEL_STRATEGY.md`
  - `02_INDEX.md:9` → `01_VISION.md`
  - `03_GOVERNANCE.md:8` → `01_VISION.md`
  - `05_CHANNEL_STRATEGY.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `README.md:20` → `01_VISION.md`
  - `README.md:28` → `01_VISION.md`
- Package findings: none.

### 02_INDEX.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root, outbound link from 02_INDEX.md, outbound link from README.md.
  - `01_VISION.md` — governance root, outbound link from 02_INDEX.md, outbound link from README.md.
  - `02_INDEX.md` — changed workflow document, direct inbound link, outbound link from 02_INDEX.md, outbound link from README.md.
  - `03_GOVERNANCE.md` — governance root, outbound link from 02_INDEX.md, outbound link from README.md.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 02_INDEX.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from 80_templates/cost_sheet_template.md, outbound link from README.md.
  - `05_CHANNEL_STRATEGY.md` — outbound link from 02_INDEX.md, outbound link from README.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — outbound link from 02_INDEX.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — outbound link from 02_INDEX.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from README.md.
  - `08_AUTOMATION_ROADMAP.md` — outbound link from 02_INDEX.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `09_DATA_MODEL.md` — outbound link from 02_INDEX.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `10_PROMPTS_INDEX.md` — outbound link from 02_INDEX.md, outbound link from 13_BACKLOG.md, outbound link from README.md.
  - `11_WEEKLY_OPERATIONS.md` — outbound link from 02_INDEX.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from README.md.
  - `12_DECISION_LOG.md` — outbound link from 02_INDEX.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 09_DATA_MODEL.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md, outbound link from 14_GLOSSARY.md, outbound link from README.md.
  - `13_BACKLOG.md` — outbound link from 02_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md, outbound link from README.md.
  - `14_GLOSSARY.md` — outbound link from 02_INDEX.md, outbound link from README.md.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `50_content/facebook_brand_post_rules.md` — outbound link from 02_INDEX.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 05_CHANNEL_STRATEGY.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md, outbound link from 50_content/facebook_brand_post_rules.md.
  - `80_templates/weekly_review_template.md` — outbound link from 11_WEEKLY_OPERATIONS.md.
  - `README.md` — direct inbound link, outbound link from 02_INDEX.md.
- Link evidence:
  - `00_START_HERE.md:42` → `02_INDEX.md`
  - `02_INDEX.md:3` → `00_START_HERE.md`
  - `02_INDEX.md:7` → `README.md`
  - `02_INDEX.md:8` → `00_START_HERE.md`
  - `02_INDEX.md:9` → `01_VISION.md`
  - `02_INDEX.md:10` → `02_INDEX.md`
  - `02_INDEX.md:10` → `02_INDEX.md`
  - `02_INDEX.md:11` → `03_GOVERNANCE.md`
  - `02_INDEX.md:12` → `04_BUSINESS_RULES.md`
  - `02_INDEX.md:13` → `14_GLOSSARY.md`
  - `02_INDEX.md:17` → `05_CHANNEL_STRATEGY.md`
  - `02_INDEX.md:18` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `02_INDEX.md:19` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `02_INDEX.md:20` → `08_AUTOMATION_ROADMAP.md`
  - `02_INDEX.md:21` → `11_WEEKLY_OPERATIONS.md`
  - `02_INDEX.md:25` → `09_DATA_MODEL.md`
  - `02_INDEX.md:26` → `10_PROMPTS_INDEX.md`
  - `02_INDEX.md:27` → `50_content/facebook_brand_post_rules.md`
  - `02_INDEX.md:28` → `12_DECISION_LOG.md`
  - `02_INDEX.md:29` → `13_BACKLOG.md`
  - `05_CHANNEL_STRATEGY.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `08_AUTOMATION_ROADMAP.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `08_AUTOMATION_ROADMAP.md:14` → `09_DATA_MODEL.md`
  - `08_AUTOMATION_ROADMAP.md:32` → `11_WEEKLY_OPERATIONS.md`
  - `09_DATA_MODEL.md:12` → `12_DECISION_LOG.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:208` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `11_WEEKLY_OPERATIONS.md:46` → `80_templates/weekly_review_template.md`
  - `11_WEEKLY_OPERATIONS.md:49` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:50` → `13_BACKLOG.md`
  - `13_BACKLOG.md:27` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `13_BACKLOG.md:28` → `10_PROMPTS_INDEX.md`
  - `13_BACKLOG.md:32` → `04_BUSINESS_RULES.md`
  - `13_BACKLOG.md:39` → `08_AUTOMATION_ROADMAP.md`
  - `13_BACKLOG.md:40` → `09_DATA_MODEL.md`
  - `14_GLOSSARY.md:15` → `12_DECISION_LOG.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `50_content/facebook_brand_post_rules.md:317` → `80_templates/standalone_external_prompt_checklist.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:19` → `00_START_HERE.md`
  - `README.md:20` → `01_VISION.md`
  - `README.md:21` → `03_GOVERNANCE.md`
  - `README.md:22` → `04_BUSINESS_RULES.md`
  - `README.md:23` → `02_INDEX.md`
  - `README.md:23` → `02_INDEX.md`
  - `README.md:27` → `00_START_HERE.md`
  - `README.md:28` → `01_VISION.md`
  - `README.md:29` → `03_GOVERNANCE.md`
  - `README.md:30` → `04_BUSINESS_RULES.md`
  - `README.md:31` → `05_CHANNEL_STRATEGY.md`
  - `README.md:36` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `README.md:37` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `README.md:38` → `11_WEEKLY_OPERATIONS.md`
  - `README.md:42` → `08_AUTOMATION_ROADMAP.md`
  - `README.md:43` → `09_DATA_MODEL.md`
  - `README.md:44` → `10_PROMPTS_INDEX.md`
  - `README.md:45` → `12_DECISION_LOG.md`
  - `README.md:46` → `13_BACKLOG.md`
  - `README.md:47` → `14_GLOSSARY.md`
  - `README.md:51` → `02_INDEX.md`
  - `README.md:51` → `02_INDEX.md`
- Package findings: none.

### 03_GOVERNANCE.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root, outbound link from 03_GOVERNANCE.md.
  - `01_VISION.md` — governance root, outbound link from 03_GOVERNANCE.md.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — changed workflow document, direct inbound link, governance root, outbound link from 03_GOVERNANCE.md.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 03_GOVERNANCE.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from 80_templates/cost_sheet_template.md.
  - `05_CHANNEL_STRATEGY.md` — outbound link from 03_GOVERNANCE.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — outbound link from 03_GOVERNANCE.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 13_BACKLOG.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — outbound link from 03_GOVERNANCE.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `08_AUTOMATION_ROADMAP.md` — outbound link from 03_GOVERNANCE.md, outbound link from 13_BACKLOG.md.
  - `09_DATA_MODEL.md` — outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 13_BACKLOG.md.
  - `10_PROMPTS_INDEX.md` — outbound link from 13_BACKLOG.md.
  - `11_WEEKLY_OPERATIONS.md` — outbound link from 03_GOVERNANCE.md, outbound link from 08_AUTOMATION_ROADMAP.md.
  - `12_DECISION_LOG.md` — outbound link from 03_GOVERNANCE.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 09_DATA_MODEL.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `13_BACKLOG.md` — outbound link from 03_GOVERNANCE.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 03_GOVERNANCE.md, outbound link from 05_CHANNEL_STRATEGY.md, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `80_templates/weekly_review_template.md` — outbound link from 11_WEEKLY_OPERATIONS.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:35` → `03_GOVERNANCE.md`
  - `02_INDEX.md:11` → `03_GOVERNANCE.md`
  - `03_GOVERNANCE.md:7` → `00_START_HERE.md`
  - `03_GOVERNANCE.md:8` → `01_VISION.md`
  - `03_GOVERNANCE.md:9` → `03_GOVERNANCE.md`
  - `03_GOVERNANCE.md:9` → `03_GOVERNANCE.md`
  - `03_GOVERNANCE.md:10` → `04_BUSINESS_RULES.md`
  - `03_GOVERNANCE.md:11` → `05_CHANNEL_STRATEGY.md`
  - `03_GOVERNANCE.md:12` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `03_GOVERNANCE.md:12` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `03_GOVERNANCE.md:12` → `08_AUTOMATION_ROADMAP.md`
  - `03_GOVERNANCE.md:12` → `11_WEEKLY_OPERATIONS.md`
  - `03_GOVERNANCE.md:13` → `12_DECISION_LOG.md`
  - `03_GOVERNANCE.md:13` → `13_BACKLOG.md`
  - `03_GOVERNANCE.md:21` → `12_DECISION_LOG.md`
  - `03_GOVERNANCE.md:41` → `04_BUSINESS_RULES.md`
  - `03_GOVERNANCE.md:64` → `80_templates/standalone_external_prompt_checklist.md`
  - `03_GOVERNANCE.md:182` → `12_DECISION_LOG.md`
  - `03_GOVERNANCE.md:183` → `13_BACKLOG.md`
  - `05_CHANNEL_STRATEGY.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `08_AUTOMATION_ROADMAP.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `08_AUTOMATION_ROADMAP.md:14` → `09_DATA_MODEL.md`
  - `08_AUTOMATION_ROADMAP.md:32` → `11_WEEKLY_OPERATIONS.md`
  - `09_DATA_MODEL.md:12` → `12_DECISION_LOG.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:208` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `11_WEEKLY_OPERATIONS.md:46` → `80_templates/weekly_review_template.md`
  - `11_WEEKLY_OPERATIONS.md:49` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:50` → `13_BACKLOG.md`
  - `13_BACKLOG.md:27` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `13_BACKLOG.md:28` → `10_PROMPTS_INDEX.md`
  - `13_BACKLOG.md:32` → `04_BUSINESS_RULES.md`
  - `13_BACKLOG.md:39` → `08_AUTOMATION_ROADMAP.md`
  - `13_BACKLOG.md:40` → `09_DATA_MODEL.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:21` → `03_GOVERNANCE.md`
  - `README.md:29` → `03_GOVERNANCE.md`
- Package findings: none.

### 04_BUSINESS_RULES.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — changed workflow document, governance root.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — direct inbound link.
  - `13_BACKLOG.md` — direct inbound link.
  - `30_products/cost_cedar_decorative_obelisk_trellis_001.md` — direct inbound link.
  - `30_products/cost_cedar_five_finger_trellis_001.md` — direct inbound link.
  - `30_products/cost_cedar_petite_planter_box_111113_001.md` — direct inbound link.
  - `30_products/cost_cedar_planter_box_001.md` — direct inbound link.
  - `30_products/cost_cedar_raised_bed_001.md` — direct inbound link.
  - `80_templates/cost_sheet_template.md` — direct inbound link.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:36` → `04_BUSINESS_RULES.md`
  - `00_START_HERE.md:67` → `04_BUSINESS_RULES.md`
  - `02_INDEX.md:12` → `04_BUSINESS_RULES.md`
  - `03_GOVERNANCE.md:10` → `04_BUSINESS_RULES.md`
  - `03_GOVERNANCE.md:41` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `13_BACKLOG.md:32` → `04_BUSINESS_RULES.md`
  - `30_products/cost_cedar_decorative_obelisk_trellis_001.md:65` → `04_BUSINESS_RULES.md`
  - `30_products/cost_cedar_five_finger_trellis_001.md:64` → `04_BUSINESS_RULES.md`
  - `30_products/cost_cedar_petite_planter_box_111113_001.md:64` → `04_BUSINESS_RULES.md`
  - `30_products/cost_cedar_planter_box_001.md:62` → `04_BUSINESS_RULES.md`
  - `30_products/cost_cedar_raised_bed_001.md:67` → `04_BUSINESS_RULES.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:22` → `04_BUSINESS_RULES.md`
  - `README.md:30` → `04_BUSINESS_RULES.md`
- Package findings: none.

### 05_CHANNEL_STRATEGY.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root.
  - `01_VISION.md` — direct inbound link, governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `05_CHANNEL_STRATEGY.md` — changed workflow document.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 05_CHANNEL_STRATEGY.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:37` → `05_CHANNEL_STRATEGY.md`
  - `00_START_HERE.md:68` → `05_CHANNEL_STRATEGY.md`
  - `01_VISION.md:45` → `05_CHANNEL_STRATEGY.md`
  - `02_INDEX.md:17` → `05_CHANNEL_STRATEGY.md`
  - `03_GOVERNANCE.md:11` → `05_CHANNEL_STRATEGY.md`
  - `05_CHANNEL_STRATEGY.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `README.md:31` → `05_CHANNEL_STRATEGY.md`
- Package findings: none.

### 06_PRODUCT_DECISION_WORKFLOW.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 80_templates/cost_sheet_template.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — changed workflow document, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — direct inbound link, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `12_DECISION_LOG.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `13_BACKLOG.md` — direct inbound link.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:38` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `02_INDEX.md:18` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `03_GOVERNANCE.md:12` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `13_BACKLOG.md:27` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:36` → `06_PRODUCT_DECISION_WORKFLOW.md`
- Package findings: none.

### 07_LISTING_AND_CONTENT_WORKFLOW.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 80_templates/cost_sheet_template.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — direct inbound link, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — changed workflow document, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `12_DECISION_LOG.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:39` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `02_INDEX.md:19` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `03_GOVERNANCE.md:12` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:37` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
- Package findings: none.

### 08_AUTOMATION_ROADMAP.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from 80_templates/cost_sheet_template.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 13_BACKLOG.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `08_AUTOMATION_ROADMAP.md` — changed workflow document, outbound link from 13_BACKLOG.md.
  - `09_DATA_MODEL.md` — outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 13_BACKLOG.md.
  - `10_PROMPTS_INDEX.md` — outbound link from 13_BACKLOG.md.
  - `11_WEEKLY_OPERATIONS.md` — outbound link from 08_AUTOMATION_ROADMAP.md.
  - `12_DECISION_LOG.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 09_DATA_MODEL.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `13_BACKLOG.md` — direct inbound link, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `80_templates/weekly_review_template.md` — outbound link from 11_WEEKLY_OPERATIONS.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `02_INDEX.md:20` → `08_AUTOMATION_ROADMAP.md`
  - `03_GOVERNANCE.md:12` → `08_AUTOMATION_ROADMAP.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `08_AUTOMATION_ROADMAP.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `08_AUTOMATION_ROADMAP.md:14` → `09_DATA_MODEL.md`
  - `08_AUTOMATION_ROADMAP.md:32` → `11_WEEKLY_OPERATIONS.md`
  - `09_DATA_MODEL.md:12` → `12_DECISION_LOG.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:208` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `11_WEEKLY_OPERATIONS.md:46` → `80_templates/weekly_review_template.md`
  - `11_WEEKLY_OPERATIONS.md:49` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:50` → `13_BACKLOG.md`
  - `13_BACKLOG.md:27` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `13_BACKLOG.md:28` → `10_PROMPTS_INDEX.md`
  - `13_BACKLOG.md:32` → `04_BUSINESS_RULES.md`
  - `13_BACKLOG.md:39` → `08_AUTOMATION_ROADMAP.md`
  - `13_BACKLOG.md:39` → `08_AUTOMATION_ROADMAP.md`
  - `13_BACKLOG.md:40` → `09_DATA_MODEL.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:42` → `08_AUTOMATION_ROADMAP.md`
- Package findings: none.

### 09_DATA_MODEL.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `08_AUTOMATION_ROADMAP.md` — direct inbound link.
  - `09_DATA_MODEL.md` — changed workflow document.
  - `12_DECISION_LOG.md` — outbound link from 09_DATA_MODEL.md.
  - `13_BACKLOG.md` — direct inbound link.
  - `README.md` — direct inbound link.
- Link evidence:
  - `02_INDEX.md:25` → `09_DATA_MODEL.md`
  - `08_AUTOMATION_ROADMAP.md:14` → `09_DATA_MODEL.md`
  - `09_DATA_MODEL.md:12` → `12_DECISION_LOG.md`
  - `13_BACKLOG.md:40` → `09_DATA_MODEL.md`
  - `README.md:43` → `09_DATA_MODEL.md`
- Package findings: none.

### 10_PROMPTS_INDEX.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `10_PROMPTS_INDEX.md` — changed workflow document.
  - `12_DECISION_LOG.md` — outbound link from 10_PROMPTS_INDEX.md.
  - `13_BACKLOG.md` — direct inbound link.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 10_PROMPTS_INDEX.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `02_INDEX.md:26` → `10_PROMPTS_INDEX.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:208` → `12_DECISION_LOG.md`
  - `13_BACKLOG.md:28` → `10_PROMPTS_INDEX.md`
  - `README.md:44` → `10_PROMPTS_INDEX.md`
- Package findings: none.

### 11_WEEKLY_OPERATIONS.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — direct inbound link, governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 13_BACKLOG.md, outbound link from 80_templates/cost_sheet_template.md.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 13_BACKLOG.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `08_AUTOMATION_ROADMAP.md` — direct inbound link, outbound link from 13_BACKLOG.md.
  - `09_DATA_MODEL.md` — outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 13_BACKLOG.md.
  - `10_PROMPTS_INDEX.md` — outbound link from 13_BACKLOG.md.
  - `11_WEEKLY_OPERATIONS.md` — changed workflow document, outbound link from 08_AUTOMATION_ROADMAP.md.
  - `12_DECISION_LOG.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 09_DATA_MODEL.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `13_BACKLOG.md` — outbound link from 11_WEEKLY_OPERATIONS.md.
  - `30_products/product_to_family_conversion_workflow.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
  - `80_templates/cost_sheet_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/listing_template.md` — outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md.
  - `80_templates/product_candidate_template.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 06_PRODUCT_DECISION_WORKFLOW.md, outbound link from 07_LISTING_AND_CONTENT_WORKFLOW.md, outbound link from 08_AUTOMATION_ROADMAP.md, outbound link from 10_PROMPTS_INDEX.md, outbound link from 11_WEEKLY_OPERATIONS.md.
  - `80_templates/weekly_review_template.md` — outbound link from 11_WEEKLY_OPERATIONS.md.
  - `README.md` — direct inbound link.
- Link evidence:
  - `00_START_HERE.md:40` → `11_WEEKLY_OPERATIONS.md`
  - `02_INDEX.md:21` → `11_WEEKLY_OPERATIONS.md`
  - `03_GOVERNANCE.md:12` → `11_WEEKLY_OPERATIONS.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:20` → `04_BUSINESS_RULES.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:22` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:55` → `07_LISTING_AND_CONTENT_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:15` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:183` → `12_DECISION_LOG.md`
  - `08_AUTOMATION_ROADMAP.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `08_AUTOMATION_ROADMAP.md:14` → `09_DATA_MODEL.md`
  - `08_AUTOMATION_ROADMAP.md:32` → `11_WEEKLY_OPERATIONS.md`
  - `08_AUTOMATION_ROADMAP.md:32` → `11_WEEKLY_OPERATIONS.md`
  - `09_DATA_MODEL.md:12` → `12_DECISION_LOG.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:208` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `11_WEEKLY_OPERATIONS.md:46` → `80_templates/weekly_review_template.md`
  - `11_WEEKLY_OPERATIONS.md:49` → `12_DECISION_LOG.md`
  - `11_WEEKLY_OPERATIONS.md:50` → `13_BACKLOG.md`
  - `13_BACKLOG.md:27` → `06_PRODUCT_DECISION_WORKFLOW.md`
  - `13_BACKLOG.md:28` → `10_PROMPTS_INDEX.md`
  - `13_BACKLOG.md:32` → `04_BUSINESS_RULES.md`
  - `13_BACKLOG.md:39` → `08_AUTOMATION_ROADMAP.md`
  - `13_BACKLOG.md:40` → `09_DATA_MODEL.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
  - `README.md:38` → `11_WEEKLY_OPERATIONS.md`
- Package findings: none.

### 30_products/product_to_family_conversion_workflow.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — direct inbound link.
  - `30_products/product_to_family_conversion_workflow.md` — changed workflow document.
  - `30_products/usa1_variant_migration_2026-06-21.md` — outbound link from 30_products/product_to_family_conversion_workflow.md.
- Link evidence:
  - `06_PRODUCT_DECISION_WORKFLOW.md:14` → `30_products/product_to_family_conversion_workflow.md`
  - `30_products/product_to_family_conversion_workflow.md:7` → `30_products/usa1_variant_migration_2026-06-21.md`
- Package findings: none.

### 40_listings/claude_handoff_prep_marketplace_raised_bed_001_2026-06-04.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/claude_handoff_prep_marketplace_raised_bed_001_2026-06-04.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/claude_handoff_prep_wave1_fbm_catalog_2026-06-04.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/claude_handoff_prep_wave1_fbm_catalog_2026-06-04.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/facebook_marketplace_catalog_rollout_2026-06-03.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/claude_fbm_listing_copy_prompt_k_raised_bed_2026-06-09.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_l_nat_wavy_flag_2026-06-14.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_l_nat_wavy_flag_2026-06-14.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_m_nat_wavy_flag_2026-06-21.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/claude_fbm_listing_copy_prompt_usa1_s_nat_wavy_flag_2026-06-21.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/claude_fbm_listing_copy_prompt_wave1_2026-06-04.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_abc_operator_run_sheet_2026-06-08.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_abc_operator_run_sheet_2026-06-08.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_image_prompt_pack_usa1_l_nat_wavy_flag_2026-06-14.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_image_prompt_pack_usa1_l_nat_wavy_flag_2026-06-14.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_image_prompt_pack_usa1_m_nat_wavy_flag_2026-06-21.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_image_prompt_pack_usa1_m_nat_wavy_flag_2026-06-21.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_image_prompt_pack_usa1_s_nat_wavy_flag_2026-06-21.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_image_prompt_pack_usa1_s_nat_wavy_flag_2026-06-21.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_image_prompt_pack_wave1_2026-06-04.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_image_prompt_pack_wave1_5_2026-06-10.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_image_prompt_pack_wave1_5_2026-06-10.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/fbm_sku_image_plan_2026-06-04.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/fbm_sku_image_plan_2026-06-04.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/prompt_fbm_listing_image_pack_generator_v2.0.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v2.0.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/prompt_fbm_variant_scope_clean_reference_generator_v1.0.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/prompt_fbm_variant_scope_clean_reference_generator_v1.0.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/prompt_usa1_m_nat_clean_reference_generator_2026-06-21.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/prompt_usa1_m_nat_clean_reference_generator_2026-06-21.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/prompts/prompt_usa1_s_nat_clean_reference_generator_2026-06-21.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/prompts/prompt_usa1_s_nat_clean_reference_generator_2026-06-21.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 40_listings/variant_scope_marketplace_listing_workflow.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `40_listings/variant_scope_marketplace_listing_workflow.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 50_content/facebook_brand_post_rules.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `02_INDEX.md` — direct inbound link.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/facebook_brand_post_rules.md` — changed workflow document.
  - `80_templates/standalone_external_prompt_checklist.md` — outbound link from 50_content/facebook_brand_post_rules.md.
- Link evidence:
  - `02_INDEX.md:27` → `50_content/facebook_brand_post_rules.md`
  - `50_content/facebook_brand_post_rules.md:317` → `80_templates/standalone_external_prompt_checklist.md`
- Package findings: none.

### 50_content/prompts/content_fbpage_cedar_obelisk_trellis_vines_001_claude_post_copy_prompt_2026-06-23.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/prompts/content_fbpage_cedar_obelisk_trellis_vines_001_claude_post_copy_prompt_2026-06-23.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 50_content/prompts/content_fbpage_cedar_obelisk_trellis_vines_001_image_prompt_2026-06-23.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/prompts/content_fbpage_cedar_obelisk_trellis_vines_001_image_prompt_2026-06-23.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 50_content/prompts/content_fbpage_classic_square_planter_spotlight_001_claude_post_copy_prompt_2026-06-08.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/prompts/content_fbpage_classic_square_planter_spotlight_001_claude_post_copy_prompt_2026-06-08.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 50_content/prompts/content_fbpage_classic_square_planter_spotlight_001_image_prompt_2026-06-08.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/prompts/content_fbpage_classic_square_planter_spotlight_001_image_prompt_2026-06-08.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 50_content/prompts/content_fbpage_raised_bed_spotlight_001_image_prompt_2026-06-04.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/prompts/content_fbpage_raised_bed_spotlight_001_image_prompt_2026-06-04.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `50_content/prompts/prompt_facebook_brand_post_image_generator_v1.0.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 60_automation/workspace_maintenance/README.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `60_automation/workspace_maintenance/README.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 60_automation/workspace_maintenance/audit_workspace.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `60_automation/workspace_maintenance/audit_workspace.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 60_automation/workspace_maintenance/run_weekly_maintenance.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `60_automation/workspace_maintenance/run_weekly_maintenance.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 60_automation/workspace_maintenance/session_repo_briefing.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `60_automation/workspace_maintenance/session_repo_briefing.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 60_automation/workspace_maintenance/workspace_maintenance_prompt.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `60_automation/workspace_maintenance/workspace_maintenance_prompt.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/ad_test_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/ad_test_template.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/claude_final_customer_reply_prompt.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/claude_final_customer_reply_prompt.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/claude_final_marketplace_listing_prompt.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/claude_final_marketplace_listing_prompt.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/claude_final_social_post_copy_prompt.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/claude_final_social_post_copy_prompt.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/cost_sheet_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root, outbound link from 80_templates/cost_sheet_template.md.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — direct inbound link.
  - `80_templates/cost_sheet_template.md` — changed workflow document.
- Link evidence:
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:19` → `80_templates/cost_sheet_template.md`
  - `80_templates/cost_sheet_template.md:72` → `04_BUSINESS_RULES.md`
- Package findings: none.

### 80_templates/gpt_to_claude_handoff_prompt_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/gpt_to_claude_handoff_prompt_template.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/listing_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — direct inbound link.
  - `80_templates/listing_template.md` — changed workflow document.
- Link evidence:
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:25` → `80_templates/listing_template.md`
- Package findings: none.

### 80_templates/product_candidate_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — direct inbound link.
  - `80_templates/product_candidate_template.md` — changed workflow document.
- Link evidence:
  - `06_PRODUCT_DECISION_WORKFLOW.md:12` → `80_templates/product_candidate_template.md`
- Package findings: none.

### 80_templates/product_to_family_conversion_manifest_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/product_to_family_conversion_manifest_template.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/social_post_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/social_post_template.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/standalone_external_prompt_checklist.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — direct inbound link, governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `05_CHANNEL_STRATEGY.md` — direct inbound link.
  - `06_PRODUCT_DECISION_WORKFLOW.md` — direct inbound link.
  - `07_LISTING_AND_CONTENT_WORKFLOW.md` — direct inbound link.
  - `08_AUTOMATION_ROADMAP.md` — direct inbound link.
  - `10_PROMPTS_INDEX.md` — direct inbound link.
  - `11_WEEKLY_OPERATIONS.md` — direct inbound link.
  - `50_content/facebook_brand_post_rules.md` — direct inbound link.
  - `80_templates/standalone_external_prompt_checklist.md` — changed workflow document.
- Link evidence:
  - `03_GOVERNANCE.md:64` → `80_templates/standalone_external_prompt_checklist.md`
  - `05_CHANNEL_STRATEGY.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `06_PRODUCT_DECISION_WORKFLOW.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `07_LISTING_AND_CONTENT_WORKFLOW.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `08_AUTOMATION_ROADMAP.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `10_PROMPTS_INDEX.md:9` → `80_templates/standalone_external_prompt_checklist.md`
  - `11_WEEKLY_OPERATIONS.md:7` → `80_templates/standalone_external_prompt_checklist.md`
  - `50_content/facebook_brand_post_rules.md:317` → `80_templates/standalone_external_prompt_checklist.md`
- Package findings: none.

### 80_templates/standard_product_spec_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/standard_product_spec_template.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/verification_packet_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `80_templates/verification_packet_template.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### 80_templates/weekly_review_template.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `11_WEEKLY_OPERATIONS.md` — direct inbound link.
  - `80_templates/weekly_review_template.md` — changed workflow document.
- Link evidence:
  - `11_WEEKLY_OPERATIONS.md:46` → `80_templates/weekly_review_template.md`
- Package findings: none.

### AGENTS.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `AGENTS.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### CLAUDE.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `CLAUDE.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

### CODEX.md

- Change: initial.
- Package members:
  - `00_START_HERE.md` — governance root.
  - `01_VISION.md` — governance root.
  - `03_GOVERNANCE.md` — governance root.
  - `04_BUSINESS_RULES.md` — governance root.
  - `CODEX.md` — changed workflow document.
- Link evidence: none.
- Package findings: none.

## Repair Boundary

Repair only generated indexes, clear relative links, archive-ledger pointers, and encoding in editable canonical files without additional approval. Escalate business-policy conflicts, uncertain ownership, customer-facing copy, published records, and source evidence.
