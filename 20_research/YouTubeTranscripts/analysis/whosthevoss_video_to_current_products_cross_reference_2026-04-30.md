# Who's the Voss Video-to-Product Cross-Reference

date_created: 2026-04-30
source_video_index: `20_research/YouTubeTranscripts/analysis/whosthevoss_video_concept_product_index_2026-04-30.md`
source_transcript_folder: `20_research/YouTubeTranscripts/WhosTheVoss_transcripts/`
source_product_folder: `30_products/`
research_status: Internal cross-reference

## Method Used

This list was made with the following workflow:

1. Read the saved video research index and the current `30_products/` product records.
2. Extract each current product's `product_id`, `product_name`, `reference_code`, `plans_source_ref`, `source_links`, and use-case fields.
3. Match videos to products in this priority order:
   - Exact video title or product/page name already present in a product record.
   - Exact Who's the Voss product-page URL or source slug already present in a product record.
   - Official pricing-guide `reference_code` match, such as `Planter Box A`.
   - Transcript confirmation when the product record was vague but the video transcript described the same object.
4. Use confidence labels:
   - `Confirmed` means the product record or source reference directly supports the match.
   - `Probable` means the names/product family align, but the saved record does not contain the exact video title.
   - `Related only` means the video is useful context but should not be treated as the same product without more checking.
5. Leave `Product letter / code` blank when the current product record has no saved `reference_code`.

Repeat instruction:

> Compare `20_research/YouTubeTranscripts/analysis/whosthevoss_video_concept_product_index_YYYY-MM-DD.md` against `30_products/`. Extract `product_id`, `product_name`, and `reference_code`, then match by exact source title/URL first, product-page slug second, pricing-guide code third, and transcript confirmation for ambiguous cases. Save the result as a cross-reference under `20_research/YouTubeTranscripts/analysis/`.

## Confirmed or High-Confidence Matches

| Current product number / catalog id | Item description | Product letter / code | Matched video(s) | Match confidence | How identified |
|---|---|---|---|---|---|
| `prod_cedar_three_tier_planter_001` | Cedar Three-Tier Planter | Planter Box N | `005` - Simple $25 Planter Box is my 2026 BEST SELLER | Confirmed | Product `plans_source_ref` explicitly maps Three Tiered Planter to this saved video title; pricing guide gives `Planter Box N`. |
| `prod_cedar_tapered_planter_box_001` | Cedar Tapered Planter Box | Planter Box M | `039` - Tapered Planter Box - Free Plans! - Make Money Woodworking | Confirmed | Product `plans_source_ref` explicitly maps Tapered Planter Box to this saved video title; pricing guide gives `Planter Box M`. |
| `prod_cedar_three_picket_planter_001` | Cedar 3-Picket Planter | Planter Box A | `046` - Three Years to Perfection. Do THIS to all your Planter Boxes. | Confirmed | Product links to the Better 3-Picket Planter source; planter summary names this video as the Better 3 Picket Planter reference, and the transcript discusses the improved three-picket planter. |
| `prod_cedar_plant_stand_001` | Cedar Plant Stand | Planter Stand | `043` - $1.50 EASY DIY Plant Stand | Confirmed | Pricing guide says `Plant Stand`, 15 inches tall; video `043` builds a 2x4 plant stand and describes the stand as almost 16 inches tall. |
| `prod_cedar_tabletop_plant_holder_001` | Cedar Tabletop Plant Holder | Table Top Planter | `004` - EASY $100 using Beginner Tools and Cheap Lumber | Confirmed | Owner review confirmed video `004` is the tabletop plant-holder product already represented by the current `Table Top Planter` / Cedar Tabletop Plant Holder record. |
| `prod_cedar_table_saw_cart_001` | Cedar Table Saw Cart |  | `007` - Beginner Table Saw into PROFESSIONAL Work Station | Confirmed | Product source URL is `table-saw-cart`; video transcript is a table saw cart/workstation with outfeed, leveling hardware, and dust collection. |
| `prod_cedar_forever_workbench_001` | Cedar Forever Workbench |  | `030` - How to Build a Professional Workbench, as a Beginner. | Probable | Product source is the Who's the Voss `forever-workbench` page; video `030` is the saved workbench build in the transcript set. The title is not an exact record-title match, so keep this as probable unless the product page confirms the exact video. |
| `prod_cedar_arch_trellis_arbor_001` | Cedar Arch Trellis Arbor |  | `041` - DIY Wooden Garden Arbor | Probable | Product is sourced from the Top 20 `Arch / Trellis / Arbor` item and the product URL slug is `arch-trellis-arbor`; video `041` is a garden arbor build. |

## Related but Not Exact Enough for Direct Product Mapping

| Current product number / catalog id | Item description | Product letter / code | Related video(s) | Confidence | Why not treated as a confirmed direct match |
|---|---|---|---|---|---|
| `prod_cedar_arch_trellis_arbor_001` | Cedar Arch Trellis Arbor |  | `001` - This Simple Garden Trellis Outsells My Complex Projects! | Related only | Video `001` is a simple garden trellis, while the current product is an arch/trellis/arbor product. Useful related research, but not necessarily the same SKU. |
| `prod_cedar_planter_box_001` | Cedar Planter Box 24x24x18 | Pending | `002`, `003`, `044`, `045`, `046` | Related only | The current record links to a Post Planter Box source and Ana White plan, while these videos are broader planter-box builds, sales, finish, or improvement notes. Useful context, not a direct one-to-one match. |
| `prod_cedar_post_planter_box_001` | Cedar Post Planter Box | Planter Box D | `045` | Related only | Video `045` mentions the 4x4/post planter while discussing planter-box updates, but the exact Post Planter Box video was not saved in the 53-transcript set. |
| `prod_cedar_trio_planter_box_set_001` | Cedar Trio Planter Box Set | Planter Box ABC | `005`, `046` | Related only | Current product is the official-guide trio set. The saved videos discuss planter-box family improvements and three-tier/three-picket items, not the exact Trio Planter Boxes source video. |
| `prod_cedar_tall_square_planter_161625_001` | Cedar Tall Square Planter 16x16x25 | Planter Box C | `005`, `046` | Related only | Current record uses the guide and trio-planter source family. No saved transcript in this set clearly isolates Planter Box C. |
| `prod_cedar_petite_planter_box_111113_001` | Cedar Petite Planter Box 11x11x13 | Planter Box ABC - small size reference | `005`, `046` | Related only | Current record is the small-size reference inside the trio set; no saved transcript clearly isolates this exact small planter. |

## Current Product Records With No Direct Saved-Video Match Found

These products exist in `30_products/`, but I did not find a direct match in the 53 saved transcript files. Some are still Who's the Voss items, but their exact source videos were skipped, not saved, or are outside this transcript set.

| Current product number / catalog id | Item description | Product letter / code | Status in current products | Notes |
|---|---|---|---|---|
| `prod_cedar_adirondack_chair_001` | Cedar Adirondack Chair |  | Rejected | No matching video/product idea found in saved index. |
| `prod_cedar_bar_table_desk_build_001` | Cedar Bar Table Desk Build |  | Candidate | Top 20 item, but no matching saved transcript row. |
| `prod_cedar_bench_planter_001` | Cedar Bench Planter | Planter Box E | Candidate | Exact source video appears in older planter summary but not in the 53 saved transcripts. |
| `prod_cedar_entry_bench_001` | Cedar Garden Entry Bench 48in |  | Hold | No matching video/product idea found in saved index. |
| `prod_cedar_flip_cart_001` | Cedar Flip Cart |  | Candidate | Top 20 item, but no matching saved transcript row. |
| `prod_cedar_full_size_coffin_001` | Cedar Full Size Coffin |  | Candidate | Top 20 item, but no matching saved transcript row. |
| `prod_cedar_lego_shelving_001` | Cedar Lego Shelving |  | Candidate | Top 20 item, but no matching saved transcript row. |
| `prod_cedar_long_planter_box_46in_001` | Cedar Long Planter Box 46in | Planter Box G | Candidate | Exact source title appears in planter summary, but not in the 53 saved transcripts. |
| `prod_cedar_mailbox_post_planter_001` | Cedar Mailbox Post Planter | Planter Box J | Candidate | Exact source title appears in planter summary, but not in the 53 saved transcripts. |
| `prod_cedar_one_picket_planter_001` | Cedar One-Picket Planter | Planter Box Q | Candidate | No direct saved transcript match found. |
| `prod_cedar_potting_bench_001` | Cedar Potting Bench with Lower Shelf | Pending | Hold | No matching video/product idea found in saved index. |
| `prod_cedar_privacy_planter_001` | Cedar Planter Privacy Screen Combo | Pending | Rejected | No matching video/product idea found in saved index. |
| `prod_cedar_pyramid_planter_001` | Cedar Pyramid Planter | Planter Box F | Candidate | Exact source title appears in planter summary, but not in the 53 saved transcripts. |
| `prod_cedar_raised_bed_001` | Cedar Raised Garden Bed | Planter Box K | Approved | Who's the Voss source exists in product record, but no direct saved transcript match found. |
| `prod_cedar_secret_bookcase_door_001` | Cedar Secret Bookcase Door |  | Candidate | Top 20 item, but no matching saved transcript row. |
| `prod_cedar_tall_rectangular_planter_461632_001` | Cedar Tall Rectangular Planter 46x16x32 with Shelf | Planter Box H | Candidate | Exact source title appears in planter summary, but not in the 53 saved transcripts. |
| `prod_cedar_wide_planter_box_262812_001` | Cedar Wide Planter Box 26x28x12 | Planter Box P | Candidate | Exact source title appears in planter summary, but not in the 53 saved transcripts. |
| `prod_cedar_window_box_001` | Cedar Window Box Planter 36in | Pending | Hold | No matching video/product idea found in saved index. |

## Video Ideas That Are Not Current Product Records Yet

The video index contains many potential product ideas that do not currently have matching `30_products/prod_*.md` records. The strongest obvious gaps include:

| Video idea | Source video(s) | Current product record? | Notes |
|---|---|---|---|
| Woven cross | `008` | No | Strong craft-show small; not currently in product catalog. |
| Valentine's tealight holders / heart products | `011`, `050` | No | Seasonal smalls, not current product records. |
| Wooden calendar puzzle | `012` | No | Not current product record. |
| Christmas trees and snowflakes | `013`, `014`, `015`, `016` | No | Seasonal decor; no current product records. |
| Savings box / money challenge box | `017` | No | Not current product record. |
| Desktop plant stand | `019` | No direct | Existing `Cedar Plant Stand` appears closer to video `043`; desktop stand remains separate. |
| Seven Nails game | `020` | No | Not current product record. |
| Wooden phone amplifier | `021` | No | Not current product record. |
| Hanging plant holder / clay pot hanger | `023` | No direct | Add-on plant-holder item associated with the tabletop plant-holder family, but not the same current `Table Top Planter` product record. |
| Small stool / step / weeding seat | `025` | No | Not current product record. |
| Modular wine rack | `028` | No | Not current product record. |
| Puzzle box lid holder | `029` | No | Not current product record. |
| Bottle carrier | `031` | No | Not current product record. |
| Viking / camp chair | `032` | No | Not current product record. |
| Wavy American flag | `033` | No | Not current product record. |
| Shoe rack / mudroom storage | `035` | No | Not current product record. |
| Router tray | `037` | No | Not current product record. |
| Easter cutouts and egg holders | `038` | No | Not current product record. |
| Small wooden lantern | `040` | No | Not current product record. |
| Post-it note holder / pencil note stand | `048` | No | Not current product record. |
| Retro TV phone holder | `051` | No | Not current product record. |
| Growth chart ruler | `052` | No | Not current product record. |

## Summary

- Confirmed or high-confidence current-product matches: 8.
- Related/context-only current-product overlaps: 6.
- Current product records with no direct saved-video match found: 18.
- The transcript research index has many sellable smalls and seasonal items that are not yet represented in `30_products/`.
