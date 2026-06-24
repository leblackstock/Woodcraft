# FBM Variant-Scope Clean Reference Generator Prompt v1.0

Purpose: prepare one standalone external image-generation prompt for a clean, grouped reference image that shows exactly the variants in one Marketplace listing scope.

Use this only after the individual clean references for every scoped variant exist and are approved, unless an operator decision explicitly authorizes a named fallback visual-reference set. This creates listing-level reference media; it does not create a new product, bundle, SKU, or customer-facing listing image.

## Internal Intake

Fill these fields from the listing record and each included variant record before preparing the external prompt:

```md
- listing_ref: [[INTERNAL_PLAIN_LANGUAGE_SCOPE_NAME]]
- listing_handle: [[INTERNAL_HANDLE]]
- variant_scope: [[VARIANT_CODES_IN_DISPLAY_ORDER]]
- output_filename: [[LISTING_HANDLE]]_scope_ref_clean-01.png
- required_attachments: [[EVERY_INCLUDED_VARIANT_CLEAN_REFERENCE_FILENAME_OR_EXACT_DOCUMENTED_FALLBACK_SET]]
- shared_visual_truth: [[MATERIAL_COLORWAY_SHARED_DETAILS]]
- exact_variant_layout: [[LEFT_TO_RIGHT_OR_OTHER_APPROVED_ORDER]]
- relative_scale_truth: [[HOW_EACH_VARIANT_MUST_SCALE_RELATIVE_TO_THE_OTHERS]]
- per_variant_identity: [[NAME_SIZE_AND_VISUAL_DETAILS_FOR_EACH_VARIANT]]
- excluded_options: [[EVERY_FAMILY_OPTION_NOT_ALLOWED_IN_THIS_SCOPE]]
```

## Standalone External Prompt To Fill And Deliver

```text
Please see attached "[[plain-language description of every approved individual clean reference or documented fallback visual-reference attachment being attached]]".

Create one clean, photorealistic listing-scope product-reference image for [[listing_ref]]. It represents exactly these selectable options and no others: [[variant_scope with customer-facing names]]. Use each attached individual reference to preserve its exact product shape, proportions, material/colorway details, and approved visual features.

Show exactly one of each scoped option in this fixed layout: [[exact_variant_layout]]. Preserve this real relative scale: [[relative_scale_truth]]. Include these exact per-option identities: [[per_variant_identity]].

Use a simple clean studio composition with a neutral background, soft realistic shadow, consistent lighting, and enough empty space to inspect each option clearly. Do not render text, prices, option labels, logos, watermarks, people, props, packaging, frames, hardware, bundle indicators, or products outside the stated scope. Do not merge the options into one product or make their sizes look equal when they are not.

This output is a clean grouped reference for later listing-image prompts, not a customer-facing advertisement. Output one square image.
```

## Approval And Record Rules

- Confirm that every visible option appears in `variant_scope` and every `variant_scope` option appears exactly once.
- Confirm the scale relationship, colorway, shape, and excluded-option boundaries before approving the output.
- When a fallback visual-reference set is used, confirm that the product and listing records cite the exact authorizing decision and that the output stays within the decision's limited purpose.
- Save the approved output in the external Product Ref Images folder, add it to `00_brand/references/PRODUCT_REF_IMAGES_MANIFEST.md`, and record it as `scope_reference_asset` in the listing record.
- Do not add this grouped file to the SKU activation index. Individual variant clean references control variant activation.
