# Variant-Scope Facebook Marketplace Listing Workflow

Purpose: create, publish, and maintain a Facebook Marketplace listing that offers a specific collection of standard variants from one product family. This workflow is for a buyer choosing one approved option from the stated scope. It is not for bundles, mix-and-match set pricing, or one-off custom quotes.

Use this workflow when a request sounds like: "Create the USA1-SML listing" or "Update image prompts for Wavy Flag Small, Medium, and Large."

## The Three Names To Keep Separate

| Field | Example | Who sees it | Purpose |
| --- | --- | --- | --- |
| `listing_ref` | `Wavy Flag Small, Medium & Large` | Internal only | Plain operator reference for the exact offer. |
| `listing_handle` | `usa1-sml` | Internal only | Short, stable name for chat requests, prompt files, and scope-reference files. |
| `listing_title` | `[[CLAUDE_FINAL_COPY_REQUIRED]]` until complete | Customers | Carefully considered Marketplace title written by Claude from approved facts. |

Never treat the internal reference or handle as customer title copy.

## 1. Define The Offer Boundary

1. Confirm that every intended option belongs to the same product family and has a permanent variant code.
2. Choose the exact variants included in this listing, in the order buyers should see them.
3. Create a new listing record from `80_templates/listing_template.md` only when the collection itself is new. For an existing collection, update its existing record instead.
4. Set these identity fields:

```md
- listing_id: list_marketplace_usa1_sml_001
- listing_ref: Wavy Flag Small, Medium & Large
- listing_handle: usa1-sml
- product_id: prod_usa_wavy_wooden_american_flag_usa1
- product_family_id: prod_usa_wavy_wooden_american_flag_usa1
- variant_scope: USA1-S-NAT, USA1-M-NAT, USA1-L-NAT
```

`variant_scope` is the complete offer boundary. Do not add an option to images, copy, price charts, or buyer messages unless its code is in this field. Do not create a new product number or catalog ID for the collection.

## 2. Confirm Scope Readiness

For every code in `variant_scope`, confirm the variant record has:

- approved customer-facing name, dimensions, price, and included/excluded options
- a price review suitable for the current listing
- an individual approved clean reference for any image that shows that variant alone, or an explicitly documented exception that names the fallback visual-reference attachments and the limited authorized use
- accurate media truth, pickup/delivery, and lead-time facts

Drafting the record and preparing clean-reference prompts may happen before every variant is ready. Publication cannot proceed until every variant actually shown has cleared its applicable gates.

## 3. Create And Record Clean References

Each individual variant normally keeps its own clean reference. If a documented operator decision authorizes a fallback visual-reference exception, use only the named attachments and record that limited exception in the affected product and listing records. If the listing needs images that show the entire selected collection together, create one additional listing-level scope reference unless the same decision specifically names an existing grouped fallback reference.

Example filename:

```text
usa1-sml_scope_ref_clean-01.png
```

Use `40_listings/prompts/prompt_fbm_variant_scope_clean_reference_generator_v1.0.md` to prepare the standalone external image prompt. Attach every included individual clean reference, unless a documented exception names the fallback attachments to use instead. The resulting scope reference must:

- show exactly one of each scoped variant
- preserve accurate relative scale and the approved visual details of each variant
- use a clean, text-free layout with no unscoped variants, props, prices, logos, frames, or unsupported additions

After approval, record the file in the external `Product Ref Images` folder and in `00_brand/references/PRODUCT_REF_IMAGES_MANIFEST.md`. Then add it to the listing record:

```md
- scope_reference_asset: usa1-sml_scope_ref_clean-01.png
- scope_reference_variant_codes: USA1-S-NAT, USA1-M-NAT, USA1-L-NAT
- scope_reference_status: Approved
```

The scope reference is listing-level media only. It does not replace individual references, create a new SKU, or activate a variant in `30_products/sku_activation_index.md`, except within the exact, limited purpose stated by a documented fallback-reference decision.

## 4. Prepare Listing Image Prompts

Use `40_listings/prompts/prompt_fbm_listing_image_pack_generator_v2.0.md` in Variant-Scope Listing Mode.

Provide the exact scope, every included variant's approved facts and prices, the individual clean references or explicitly authorized fallback attachment set, and the scope reference when group images are needed.

- Group images attach the scope reference as the primary control and show only the scoped variants.
- Single-option images attach that option's individual clean reference, or the exact fallback attachment set named in the documented exception.
- When prices differ, include a readable option-and-price chart for every scoped choice. This is not a bundle price card and must not use savings or set wording.
- Do not create any customer-facing image prompt for an included variant whose required clean reference is still pending, unless the relevant product and listing records cite an operator decision authorizing named fallback visual references for that exact use.

Save the output pack using the handle, for example:

```text
fbm_image_prompt_pack_usa1_sml_2026-06-21.md
```

## 5. Prepare The Claude Handoff

After the scope facts and media are approved, use `40_listings/prompts/prompt_fbm_claude_listing_copy_generator_v2.0.md` in Variant-Scope Listing Mode.

The handoff must inline all buyer-visible facts for every scoped option: name, dimensions, price, finish choices, purchase terms, and exclusions. It must ask Claude to write the actual Marketplace title and description. It must not expose `listing_ref`, `listing_handle`, unavailable variants, bundle claims, or unapproved custom options.

Save the handoff using the handle, for example:

```text
claude_fbm_listing_copy_prompt_usa1_sml_2026-06-21.md
```

Paste the returned Claude copy into the same listing record, set `customer_copy_status: Final Integrated`, and complete the normal publish-readiness checks.

## 6. Publish And Update The Same Record

After the manual Marketplace post is live, update that listing record only:

```md
- publish_status: Published
- publish_ready: Yes
- publish_date: YYYY-MM-DD
- published_variant_scope: [copy the exact `variant_scope` as posted]
- live_listing_url: [URL if available]
- customer_copy_status: Final Integrated
```

Then log views, saves, messages, sales, questions, and any scope-specific buyer feedback in its Performance Log. If the collection changes, such as Small + Medium becoming Small + Medium + Large, create a new listing record and handle so the live offer and performance history remain truthful.

## Prompt Routing Summary

| Need | Use | Output |
| --- | --- | --- |
| Individual option reference | Existing per-variant clean-reference prompt | One approved clean reference per variant. |
| All scoped options in one image | `prompt_fbm_variant_scope_clean_reference_generator_v1.0.md` | One listing-level scope reference. |
| Marketplace listing images | `prompt_fbm_listing_image_pack_generator_v2.0.md` in Variant-Scope Listing Mode | Standalone image prompts scoped to the listing. |
| Customer-facing title and description | `prompt_fbm_claude_listing_copy_generator_v2.0.md` in Variant-Scope Listing Mode | Paste-ready Claude handoff. |
| After posting | The listing record's Performance Log | Durable publication and results record. |
