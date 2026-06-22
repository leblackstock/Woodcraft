# USA1 Variant Migration Manifest — 2026-06-21

## Purpose

Audit the migration of the existing USA1 pilot to `USA1-L-NAT` before repurposing bare `USA1` as the Wavy Wooden American Flag configurable family.

## Identifier Mapping

| Legacy meaning | Current meaning |
|---|---|
| `USA1` product pilot | `USA1-L-NAT` — Large — Natural Wood with Red & Blue Stain |
| `prod_usa_wavy_wooden_american_flag_usa1` | USA1 family parent, catalog ID `f00034` |
| Legacy USA1 product/spec/cost/prompt paths | USA1-L-NAT child variant paths |

## External Asset Rename Map And Hashes

All listed files were renamed without changing their bytes. Stale text-bearing files are explicitly marked below and must be regenerated externally before customer use.

| New external filename | SHA-256 | Status |
|---|---|---|
| `Product Ref Images/USA1-L-NAT_wavy_wooden_american_flag_ref_clean-01.png` | `BA068194476AADD93430EE33D83646A097550E9B3DC8857B4EE3A0796368AA61` | Approved clean reference; renamed unchanged |
| `Facebook Marketing/USA1-L-NAT - 01.png` | `7EF162CF3CFF4FD9735CFAA36A6E0BEB1357491EC623AFADF17B854D7B03A6AB` | Visual-only; renamed unchanged; operator review required before use |
| `Facebook Marketing/USA1-L-NAT - 02.png` | `EC3D9B742E8AB075C392AA35E6557A2368B80C069347A7298DB738CB01F1416E` | Stale price/options text; do not use; regenerate externally |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_01_best_thumbnail_v01.png` | `7F4538C07295E45ABBE0AAA72E96105F9E697170479B4BEEBFC798831C0ABDE2` | Visual-only; renamed unchanged; operator review required before use |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_02_clean_product_v01.png` | `BDCA8B20104330F663B8EC08B920FC773174B1C89C4A24CCDF8ED3AA69366661` | Visual-only; renamed unchanged; operator review required before use |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_03_price_value_v01.png` | `DD41DBD5217D5B7482194B102F22CC0DB5EA7F132C440112B2B9C36AE2F7AD5A` | Stale $150/old option ladder; do not use; regenerate externally |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_04_size_context_v01.png` | `B9C2D3B8D7D45C5AF8ACE86D2232DA24175F26044D2694EA3B9432B96B58FF1C` | Visual-only; renamed unchanged; operator review required before use |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_05_use_case_v01.png` | `196098B2D782C270C102FA71A2CC1D0578B9565556678C0636A9577F78ED6AA6` | Visual-only; renamed unchanged; operator review required before use |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_06_detail_trust_v01.png` | `D5F6A95C1C4516F59D4E8CA01FF28AAEC3521CD166F1A6A8B3AAB9CB845A2965` | Visual-only; renamed unchanged; operator review required before use |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_07_dimensions_details_v01.png` | `11FF507AC5E27820A92CA9105511B0F4CB112F06539CA21A57495F5A1E4F7B72` | Stale decimal customer dimensions; do not use; regenerate externally |
| `Facebook Marketing/usa1_l_nat_wavy_wooden_american_flag_fbm_08_final_ordering_v01.png` | `E6E91C911C64AD384B0E806C8BCBE0454836DBA7C0206762285EEBD5F37397EA` | Visual-only; renamed unchanged; operator review required before use |

## Approved Current Truth

- Variant code: `USA1-L-NAT`
- Customer-facing dimensions: 24 3/4 in L × 13 in H × 1 1/2 in thick
- Physical target: 24.7 in L × 13 in H × 1.5 in thick
- Base price: $120
- Requested Glossy, Matte, or Oil finish: $145
- Current colorway: Natural Wood with Red & Blue Stain
- Not currently offered: frame, draped, Wood Burned, Blacked Out, Black & Blue, thin-line, flag-cross, and custom dimensions.

## Validation Scope

- All active prompts now use the renamed clean-reference attachment and `usa1_l_nat_` output filenames.
- The three stale text-bearing images are intentionally retained only as renamed obsolete files so they can be replaced outside this repository.
- Third-party competitor images and source transcript assets were not renamed or repurposed.
