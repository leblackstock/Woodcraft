# FBM Image Prompt Generation and Order Index

Status: Active navigation index
Created: 2026-06-23
Scope: current live Markdown sources that govern, prepare, record, or exemplify Facebook Marketplace listing-image prompt generation. `90_archive/` and `deprecated/` are intentionally excluded.

## Use This Index For

- Finding the authoritative FBM image sequence before creating a new pack.
- Tracing the facts, attachments, and constraints that must be resolved before a product-specific prompt is written.
- Distinguishing current rules from product-specific examples and historical decision records.

This is a navigation aid, not a second rule owner. When a source conflicts with an example, use the active generator first, then the workflow hub and the applicable approved product/listing facts.

## Authoritative Reading and Generation Path

1. Start with the [FBM catalog rollout workflow](../facebook_marketplace_catalog_rollout_2026-06-03.md) for the overall manual process and gating.
2. Use the [FBM listing image pack generator v2.0](prompt_fbm_listing_image_pack_generator_v2.0.md) for the authoritative image roles, order, prompt schema, source priority, and standalone-prompt rules.
3. Consult the [FBM SKU image plan](fbm_sku_image_plan_2026-06-04.md) for the standard sequence, shopper questions, and SKU-specific shot/truth notes.
4. Resolve current facts and the approved reference attachment from the applicable product, variant, and listing record before writing any prompt.
5. Write and run the image prompts in the numbered listing order below, manually in ChatGPT Image 2. Review is by exception.
6. Run the separate [Claude FBM listing-copy generator](prompt_fbm_claude_listing_copy_generator_v2.0.md) only for the Marketplace title and description. Claude does not approve or write image prompts or factual in-image text.

Every delivered FBM image prompt is standalone, begins with the required attachment reminder when a reference is needed, and stops rather than approximating a product whose approved attachment is missing. See the [standalone external prompt checklist](../../80_templates/standalone_external_prompt_checklist.md).

## Standard 8-Image Listing Order

| Image | Role | What the image must do for the buyer |
| --- | --- | --- |
| 1 | Best thumbnail | Stop the scroll and make the product understandable at first glance. It may be a lifestyle, clean-product, or use-case hero, whichever is most sellable while staying exactly faithful to the reference. No text overlay by default. |
| 2 | Clean product | Show the empty product clearly and establish exactly what is included. This is the trust anchor; keep props from confusing the offer. No text overlay by default. |
| 3 | Size/context photo | Answer “How big is it?” quickly with practical scale references and a simpler, distinct scene. Do not reuse the thumbnail composition. |
| 4 | Use-case photo | Show one specific useful application, planting idea, or placement. It should make ownership easier to picture, not repeat a broad hero. |
| 5 | Detail/trust photo | Prove the visible construction and material details that build confidence: grain, boards, rim, corners, posts, shelf, tier, shape, or other relevant features. |
| 6 | Price/value card | Put the product name and the approved plain FBM selling price in an easy-to-scan graphic. Use a featured-size label, variant option-and-price chart, or approved set savings only when the facts require it. |
| 7 | Dimensions/details graphic | Give exact numeric dimensions/specs plus approved local-build or made-to-order facts. For a set, show every included size numerically. |
| 8 | Final ordering graphic | Give the buyer a simple last action: product name, `Message to order`, and approved pickup/delivery availability. |

For every 8-image or 10-image pack, all real photographs occupy the leading positions in one continuous run and all composite text cards follow in one continuous run at the end. Never place a photograph after the first text card or a text card inside the photograph run. For eight images, Images 1 through 5 are photographs and Images 6 through 8 are the Price/Value Card, Dimensions/Details Graphic, and Final Ordering Graphic. If fewer usable photographs exist than lead slots, fill the available leading photo slots and leave the remaining photo slots empty rather than promoting a text card forward.

For all no-text photo slots, change the buyer question and at least two visible composition variables from the other photos: setting, distance, angle, product state, scale reference, use case, background, or detail focus. For every graphic, render only approved literal wording and no extra readable words.

## Variant-Scope 10-Image Default

Use the dedicated Variant-Scope Listing Mode in the active generator, not the standard 8-image or 10-image role table below. A non-bundle selected-variant listing defaults to ten images: Images 1 and 2 are group hero and clean group coverage; Images 3 through 5 are individual combo photos that show both use and practical scale; Image 6 is fixed Detail / Trust; Images 7 through 10 are options/prices, dimensions, selection details, and final ordering. For one to three scoped variants, give every variant one combo photo. For four or more, select two or three by explicit operator direction or documented buyer relevance, while retaining complete-scope coverage in Images 1, 2, 7, and 8. See the [variant-scope workflow](../variant_scope_marketplace_listing_workflow.md) for reference and attachment gates.

## 10-Image Extension

Use the extension only when a real product-complexity or clarity need justifies it. The entire sequence is:

| Image | Role | What the image must do for the buyer |
| --- | --- | --- |
| 1 | Best thumbnail | Stop the scroll and make the product understandable at first glance. |
| 2 | Clean product | Show the empty product clearly and establish exactly what is included. |
| 3 | Size/context photo | Answer “How big is it?” with practical scale proof. |
| 4 | Use-case photo | Show one specific useful application, planting idea, or placement. |
| 5 | Detail/trust photo | Prove material, shape, and visible construction details. |
| 6 | Support/variation photo | Give one additional no-text, approved variation or useful supporting detail. |
| 7 | Price/value card | State the approved plain price or approved scoped option-and-price chart. |
| 8 | Dimensions/details graphic | Give exact numeric dimensions/specs and approved factual details. |
| 9 | Important-details graphic | Give one necessary buyer clarification using approved facts only. Omit this card and run nine images if no approved fact justifies it. |
| 10 | Final ordering graphic | Give the final clear order instruction and approved pickup/delivery availability. |

For the ten-image pack, Images 1 through 6 are photographs and Images 7 through 10 are composite text cards. Image 9 may not introduce hanging hardware, wall anchors, weatherproofing, outdoor durability, shipping, installation, current inventory, lead-time ranges, delivery fees, or any size, color, or variation outside the approved list. If Image 9 is omitted, Final Ordering Graphic becomes Image 9.

## Current Source and Reference Inventory

### Canonical workflow and prompt rules

| Source | Role in image-prompt generation | Order relevance |
| --- | --- | --- |
| [FBM listing image pack generator v2.0](prompt_fbm_listing_image_pack_generator_v2.0.md) | Canonical owner for source priority, prompt requirements, output schema, and image role separation. | Authoritative 8- and 10-image order. |
| [FBM catalog rollout workflow](../facebook_marketplace_catalog_rollout_2026-06-03.md) | Workflow hub for facts, manual Image 2 generation, review-by-exception, publishing sequence, and default image pack. | Confirms the same 8/10 sequence and when to use it. |
| [FBM SKU image plan](fbm_sku_image_plan_2026-06-04.md) | Working per-SKU shot plan and current creation path. | Defines the universal sequence and supplies SKU-specific image 8/extension notes. |
| [Prompt index](../../10_PROMPTS_INDEX.md) | Top-level discovery point for live FBM prompt assets. | Points to this workflow; not an independent sequence owner. |
| [Variant-scope Marketplace workflow](../variant_scope_marketplace_listing_workflow.md) | Adds the selected-variant path: approve individual and scope references first, then use the v2.0 generator in Variant-Scope Listing Mode. | Keeps all scoped variants in intended buyer display order and gates image prompts on approved references. |
| [Variant-scope clean-reference generator](prompt_fbm_variant_scope_clean_reference_generator_v1.0.md) | Upstream reference-preparation prompt for a variant-scope listing. | Precedes listing-image generation; it does not replace the listing-image sequence. |
| [Standalone external prompt checklist](../../80_templates/standalone_external_prompt_checklist.md) | Required copy/paste completeness and attachment/fidelity check. | Applies to every numbered image prompt, including graphics. |
| [Claude listing-copy generator v2.0](prompt_fbm_claude_listing_copy_generator_v2.0.md) | Defines the boundary between image graphic text and Claude-owned listing prose. | Runs after image-prompt preparation; it is not an image-order source. |

### Brand and reusable visual inputs

| Source | Role in image-prompt generation |
| --- | --- |
| [Brand README](../../00_brand/README.md) | Routes prompts to approved brand assets and product photos. |
| [Visual style](../../00_brand/VISUAL_STYLE.md) | Explains how Marketplace photo slots and graphic slots should differ visually. |
| [Color palette](../../00_brand/COLOR_PALETTE.md) | Supplies approved palette values; prompts choose only the background and list remaining colors without assigning roles. |
| [Text style rules](../../00_brand/TEXT_STYLE_RULES.md) | Supplies typography and mobile-readability guidance for graphics. |
| [Voice](../../00_brand/VOICE.md) | Supplies Marketplace Mode as a factual tone guardrail for literal image text. |

### Active prompt-pack and operator examples

| Source | What it demonstrates | Sequence status |
| --- | --- | --- |
| [Wave 1 prompt pack](fbm_image_prompt_pack_wave1_2026-06-04.md) | Master-listing and early SKU eight-image packs. | Historical example in the former price-at-Image-3 sequence; its “Lifestyle Hero” is the earlier name for the current Best Thumbnail role. |
| [ABC operator run sheet](fbm_abc_operator_run_sheet_2026-06-08.md) | A run-ready eight-image execution sheet for the Cedar Planter Trio Set. | Historical example in the former price-at-Image-3 sequence; do not use its order for new packs. |
| [Wave 1.5 prompt pack](fbm_image_prompt_pack_wave1_5_2026-06-10.md) | Eight-image examples for the pyramid planter and two trellises. | Historical example in the former price-at-Image-3 sequence; do not use its order for new packs. |
| [USA1-L-NAT Wavy Flag pack](fbm_image_prompt_pack_usa1_l_nat_wavy_flag_2026-06-14.md) | An eight-image product-specific pack. | Historical example in the former price-at-Image-3 sequence; do not use its order for new packs. |
| [USA1-M-NAT Wavy Flag pack](fbm_image_prompt_pack_usa1_m_nat_wavy_flag_2026-06-21.md) | Historical compact product-specific draft using the DEC-110 paired fallback visual references. | Six-image draft; do not use as the active USA1-SML-NAT sequence. |
| [USA1-S-NAT Wavy Flag pack](fbm_image_prompt_pack_usa1_s_nat_wavy_flag_2026-06-21.md) | Historical compact product-specific draft using the DEC-110 paired fallback visual references. | Same six-image draft pattern as Medium; do not use as the active USA1-SML-NAT sequence. |
| [USA1-SML-NAT Wavy Flag pack](fbm_image_prompt_pack_usa1_sml_nat_wavy_flag_2026-06-24.md) | Active Natural S/M/L scoped pack under DEC-110 and DEC-113. | Dedicated ten-image variant-scope sequence: Group Hero, Clean Group View, Small Combo, Medium Combo, Large Combo, Detail / Trust, Options + Prices, Dimensions, Selection Details, Final Ordering. |
| [USA1-SML-RUS Wavy Flag pack](fbm_image_prompt_pack_usa1_sml_rus_wavy_flag_2026-06-24.md) | Prep-only Rustic S/M/L scoped pack. | Same DEC-113 ten-image variant-scope sequence; blocked until RUS clean references and media gates clear. |

### Product, listing, and media-truth records

| Source | Why it belongs in this index |
| --- | --- |
| [T1 Five-Finger Trellis product record](../../30_products/prod_cedar_five_finger_trellis_001.md) | Requires the T1-with-Planter-C image to be made through FBM prompts using both approved references. |
| [T1 standard spec](../../30_products/spec_cedar_five_finger_trellis_standard.md) | Repeats the two-reference T1/Planter C image requirement and truthful placement boundary. |
| [T2 Decorative Obelisk Trellis product record](../../30_products/prod_cedar_decorative_obelisk_trellis_001.md) | Identifies the approved T2 clean reference and Wave 1.5 prompt-pack use. |
| [T1 listing record](../list_marketplace_cedar_five_finger_trellis_001.md) | Links the posted listing’s media provenance and image prompt pack. |
| [Tiered Cedar Pyramid Planter listing record](../list_marketplace_tiered_cedar_pyramid_planter_001.md) | Links the published F listing to the Wave 1.5 prompt pack. |
| [Wavy Flag listing record](../list_marketplace_wavy_wooden_american_flag_standard_001.md) | Links the family listing to the variant image-prompt workflow. |
| [USA1-SML-NAT Wavy Flag listing record](../list_marketplace_usa1_sml_nat_001.md) | Owns the exact Natural Small, Medium & Large scope, fallback-reference exception, media map, and pending publication gates. |
| [USA1-SML-RUS Wavy Flag prep placeholder](../list_marketplace_usa1_sml_rus_001.md) | Records the prep-only Rustic Small, Medium & Large scope, prompt-only boundary, and pending RUS gates; no RUS Marketplace listing has been created. |
| [USA1-L-NAT variant record](../../30_products/variant_usa1_l_nat.md) | Links the approved Large reference and eight-image pack. |
| [USA1-M-NAT variant record](../../30_products/variant_usa1_m_nat.md) | Records the Medium clean-reference dependency before running its prepared pack. |
| [USA1-S-NAT variant record](../../30_products/variant_usa1_s_nat.md) | Records the Small clean-reference dependency before running its prepared pack. |
| [Trellis Wave 1.5 source notes](../../20_research/trellis_wave_1_5_source_notes_2026-06-09.md) | Establishes T1’s two-reference media requirement and no-attachment implication for the planter pairing. |

### Governance, queue, and discovery records

| Source | Role |
| --- | --- |
| [Decision log](../../12_DECISION_LOG.md) | Preserves why the workflow uses review by exception, manual Image 2 generation, distinct photo roles, fixed graphic slots, exact reference attachments, standalone prompts, and sellability-first v2.0. Historical context only; it does not supersede the active generator. |
| [Backlog](../../13_BACKLOG.md) | Queues the next clean-reference approvals and Wave 2 pack generation. |
| [Live file map](../../60_automation/workspace_maintenance/LIVE_FILE_MAP.md) | Machine-maintained inventory of current prompt assets; a discovery aid, not a workflow owner. |

## Legacy and Exception Handling

- Do not infer a new standard from an older prompt pack’s naming or a compact product-specific exception.
- DEC-111 is historical context for the legacy USA1-SML draft. The active Natural scope is USA1-SML-NAT, and DEC-113 now controls its ten-image sequence. DEC-111 does not supersede the DEC-110 fallback-reference exception or historical media evidence.
- The standard sequence is eight images unless a documented 10-image extension is justified. Do not treat an older shorter pack as an approved standard without an explicit operator decision.
- Use the approved attachment for every product-specific listing image, including text-bearing graphics. A graphic may use a small product inset only when it can preserve the product faithfully.
- For a variant-scope listing, show exactly the selected variants in the intended buyer display order. Do not turn separately priced variants into a bundle in the price graphic.

## Index Maintenance

When a new live FBM image generator, plan, prompt pack, product/listing media record, or workflow rule is added, add it to the appropriate table above and keep the top-level pointer in `10_PROMPTS_INDEX.md` current. Do not add archived or deprecated sources unless historical traceability is explicitly requested.

## 2026-06-23 Standard-Sequence Audit

The active sequence owners updated for the photo-first standard are the [v2.0 image-pack generator](prompt_fbm_listing_image_pack_generator_v2.0.md), [FBM catalog rollout workflow](../facebook_marketplace_catalog_rollout_2026-06-03.md), this index, and the [FBM SKU image plan](fbm_sku_image_plan_2026-06-04.md). The top-level [prompt index](../../10_PROMPTS_INDEX.md) points here. Product records, listing records, brand references, the standalone checklist, and the Claude copy generator do not own the standard eight-image or ten-image position order. Existing prompt packs retain their original cards and media order as historical evidence; they are not rewritten by this standard-only update.
