# SKU Activation Index

Status: Active workflow gate
Last checked: 2026-06-21
Clean reference source: `00_brand/references/PRODUCT_REF_IMAGES_MANIFEST.md`
External clean reference folder: `C:\Users\outdo\Documents\Woodcraft Catalog Setup\Product Ref Images`

Purpose: define which SKUs are active for Facebook Page, Instagram, and other social post creation.

## Rule

- A SKU is `Active` only when at least one clean reference image exists for that SKU in the external Product Ref Images folder.
- Do not create new Facebook Page, Instagram, ad, or other social posts for products that do not resolve to an `Active` SKU here.
- Prompt preparation and clean-reference generation prompts may be created for inactive SKUs; external listing/social image generation and publication remain blocked until the resulting clean reference is operator-approved and this index is updated.
- A listing-level scope reference does not activate a variant. A scope-based social post may proceed only when every code in its `variant_scope` is individually `Active`; when the post image shows the full scope together, it must also use an approved scope reference.
- Products without a catalog SKU, or with no matching clean reference file, are `Not Active` for post creation even if the product remains a business candidate or listing-prep item.
- Existing draft posts for inactive/no-SKU products should be archived or marked blocked before reuse.
- Final listing/business approval is separate from SKU activation. This file controls content/post eligibility only.

## Active SKUs

| SKU | Linked product record | Product name | Clean ref files |
|---|---|---|---|
| A | `30_products/prod_cedar_three_picket_planter_001.md` | Classic Square Cedar Planter | `A_classic_square_cedar_planter_clean_ref-01.png`; `A_classic_square_cedar_planter_clean_ref-02.png` |
| ABC | `30_products/prod_cedar_trio_planter_box_set_001.md` | Cedar Planter Trio Set | `ABC_cedar_planter_trio_set_ref_clean-01.png`; `ABC_cedar_planter_trio_set_ref_clean-02.png`; `ABC_cedar_planter_trio_set_ref_clean-03.png` |
| B | `30_products/prod_cedar_petite_planter_box_111113_001.md` | Small Square Cedar Planter | `B_small_square_cedar_planter_ref_clean-01.png`; `B_small_square_cedar_planter_ref_clean-02.png` |
| C | `30_products/prod_cedar_tall_square_planter_161625_001.md` | Tall Square Cedar Planter | `C_tall_square_cedar_planter_ref_clean-01.png`; `C_tall_square_cedar_planter_ref_clean-02.png` |
| D | `30_products/prod_cedar_post_planter_box_001.md` | Cedar Post Planter Box | `D_cedar_post_planter_box_ref_clean-01.png`; `D_cedar_post_planter_box_ref_clean-02.png` |
| E | `30_products/prod_cedar_bench_planter_001.md` | Mini Adirondack Cedar Planter | `E_mini_adirondack_cedar_planter_ref_clean-01.png`; `E_mini_adirondack_cedar_planter_ref_clean-02.png` |
| F | `30_products/prod_cedar_pyramid_planter_001.md` | Cedar Pyramid Planter | `F_tiered_cedar_pyramid_planter_ref_clean-01.png`; `F_tiered_cedar_pyramid_planter_ref_clean-02.png` |
| T1 | `30_products/prod_cedar_five_finger_trellis_001.md` | Cedar Five-Finger Trellis | `T1_cedar_five_finger_trellis_ref_clean-01.png` |
| T2 | `30_products/prod_cedar_decorative_obelisk_trellis_001.md` | Cedar Decorative Obelisk Trellis | `T2_cedar_decorative_obelisk_trellis_ref_clean-01.png` |
| G | `30_products/prod_cedar_long_planter_box_46in_001.md` | Long Rectangle Cedar Planter | `G_long_rectangle_cedar_planter_ref_clean-01.png`; `G_long_rectangle_cedar_planter_ref_clean-02.png` |
| H | `30_products/prod_cedar_tall_rectangular_planter_461632_001.md` | Tall Cedar Planter w/ Shelf | `H_tall_cedar_planter_with_shelf_ref_clean-01.png`; `H_tall_cedar_planter_with_shelf_ref_clean-02.png` |
| J | `30_products/prod_cedar_mailbox_post_planter_001.md` | Cedar Mailbox Post Planter | `J_mailbox_post_cedar_planter_ref_clean-01.png`; `J_mailbox_post_cedar_planter_ref_clean-02.png` |
| K | `30_products/prod_cedar_raised_bed_001.md` | Cedar Raised Garden Bed | `K_cedar_raised_garden_bed_ref_clean-01.png`; `K_cedar_raised_garden_bed_ref_clean-02.png` |
| M | `30_products/prod_cedar_tapered_planter_box_001.md` | Cedar Tapered Planter Box | `M_small_tapered_cedar_planter_ref_clean-01.png`; `M_small_tapered_cedar_planter_ref_clean-02.png` |
| N | `30_products/prod_cedar_three_tier_planter_001.md` | Cedar Three-Tier Planter | `N_three_tier_cedar_planter_ref_clean-01.png`; `N_three_tier_cedar_planter_ref_clean-02.png` |
| P | `30_products/prod_cedar_wide_planter_box_262812_001.md` | Tall Patio Planter Box | `P_cedar_patio_planter_box_ref_clean-01.png`; `P_cedar_patio_planter_box_ref_clean-02.png` |
| PS | `30_products/prod_cedar_plant_stand_001.md` | Cedar Plant Stand | `PS_cedar_pot_stand_ref_clean-01.png`; `PS_cedar_pot_stand_ref_clean-02.png` |
| Q | `30_products/prod_cedar_one_picket_planter_001.md` | Mini Cedar Cube Planter | `Q_mini_cedar_cube_planter_ref_clean-01.png`; `Q_mini_cedar_cube_planter_ref_clean-02.png` |
| TT | `30_products/prod_cedar_tabletop_plant_holder_001.md` | Cedar Tabletop Plant Holder | `TT_3_pot_tabletop_herb_planter_ref_clean-01.png`; `TT_3_pot_tabletop_herb_planter_ref_clean-02.png` |
| USA1-L-NAT | `30_products/variant_usa1_l_nat.md` | Wavy Wooden American Flag — Large — Natural Wood with Red & Blue Stain | `USA1-L-NAT_wavy_wooden_american_flag_ref_clean-01.png` |

## Not Active For Post Creation

| Product / SKU | Reason | Handling |
|---|---|---|
| `30_products/variant_usa1_m_nat.md` / `USA1-M-NAT` | Medium clean-reference generation and listing-prompt files are prepared; no approved clean reference exists yet. | Run the prepared clean-reference prompt with the USA1-L-NAT attachment, then approve the result before external listing/social image generation or publication. |
| `30_products/variant_usa1_s_nat.md` / `USA1-S-NAT` | Small clean-reference generation and listing-prompt files are prepared; no approved clean reference exists yet. | Run the prepared clean-reference prompt with the USA1-L-NAT attachment, then approve the result before external listing/social image generation or publication. |
| `30_products/prod_cedar_planter_box_001.md` / `f00015` | No catalog SKU is assigned and no matching clean ref file was found in the external Product Ref Images folder. | Do not create new Facebook Page or Instagram posts. Existing draft social records are archived or marked blocked. |
| Any future product or SKU not listed as `Active` above | No clean ref file is recorded in this index. | Treat as `Not Active` until a clean ref file exists and this index is updated. |
