# Product To Configurable Family Conversion Workflow

Purpose: safely convert one existing standalone product into a configurable product family with permanent child variants, without breaking identifiers, live listings, clean-reference activation, media truth, or historical records.

Use this only when the product now has repeatable, separately priced standard choices such as size, colorway, finish, or shape. Do not use it for a one-off custom quote or for a separately priced bundle.

Example: [USA1 Variant Migration Manifest](usa1_variant_migration_2026-06-21.md).

## Core Rules

- Start with a migration manifest created from `80_templates/product_to_family_conversion_manifest_template.md`.
- The existing standalone product becomes the family parent and keeps its stable `product_id`, `catalog_id`, and family code unless an explicit migration says otherwise.
- Each permanent, separately priced standard option becomes a child Variant with a unique `variant_code`. Child variants do not receive independent catalog IDs.
- The legacy offer must map to exactly one child Variant, or be explicitly retired with a reason. Do not leave a former product ambiguously represented by both the parent and multiple variants.
- One-off size, color, finish, or construction requests remain quote-only until they are approved as a repeatable standard Variant.
- Do not change a live listing's offer scope in place. Preserve the posted scope; create a new listing record and handle for a materially different collection.

## 1. Decide Whether Conversion Is Appropriate

Convert only when all of the following are true:

1. The choices are repeatable and intended to remain available.
2. Each choice has, or can receive, its own customer-facing name, dimensions/spec, price, and build truth.
3. The family has a shared identity that remains truthful across all child variants.
4. The choices are not a bundle, a temporary promotion, or arbitrary custom quoting.

If any condition is false, keep one standalone product record and use a featured configuration or quote-only handling instead.

## 2. Freeze The Legacy Snapshot

Before editing the existing record, create a manifest and capture:

- current `product_id`, `catalog_id`, `catalog_sku`, product name, build model, and status
- current standard spec, cost sheet, research, decision-log, and source references
- all listing records, publish states, live URLs, and exact scopes currently posted
- all clean references, generated media, prompt packs, Claude handoffs, and external filenames
- all Facebook Page/Instagram content records and their activation status
- third-party/reference-only assets that must remain non-publishable

For external files that are renamed or carried forward, record the old and new filenames plus hashes when practical. Mark stale text-bearing images and prompts as retired or regeneration-required instead of silently reusing them.

## 3. Define The New Family And Variant Map

1. Convert the existing product record to `record_type: Configurable Product Family`.
2. Preserve its `product_id` and `catalog_id` as the family parent.
3. Define a stable `family_code`.
4. Define each permanent child `variant_code` and write a legacy mapping for the old offer.
5. Record the shared material, visual, build, and fulfillment facts that are true for the whole family.
6. Record each child Variant's customer name, size/spec, price, finish choices, exclusions, build model, cost/spec links, and clean-reference status.

The manifest must state which child Variant inherits the former standalone offer. Example:

```text
Legacy USA1 offer -> USA1-L-NAT
USA1 parent -> configurable Wavy Wooden American Flag family
```

## 4. Create The Child Variant Records

For every permanent standard option, create a child record from `80_templates/product_candidate_template.md` with:

```md
- record_type: Variant
- variant_id: [unique child record ID]
- product_id: [leave blank; reserved for the parent or standalone record]
- family_product_id: [parent product_id]
- family_catalog_id: [parent catalog ID, reference only]
- family_code: [family code]
- variant_code: [permanent variant code]
- catalog_id: [leave blank; no independent child catalog ID]
- catalog_sku: [variant code or approved SKU]
- conversion_manifest_ref: [manifest path]
```

Create or link one standard spec and one cost truth per variant. A family-level spec/cost file may hold shared rules, but it must not replace the variant's own customer-facing dimensions, price, or clean-reference truth.

## 5. Migrate Files, Media, And Prompts

Use the manifest as a one-to-one mapping surface.

- Move or copy legacy specs, costs, prompt packs, and handoffs to the child Variant that inherits the old offer.
- Update internal references to point to the new child file paths.
- Preserve external media filenames only when the asset remains visually/factually valid for that child Variant.
- If a media asset contains old price, options, dimensions, title text, or a changed scope, mark it stale and regenerate it. Do not edit the image in place and call it current.
- Each child Variant needs its own approved clean reference before it becomes Active in `30_products/sku_activation_index.md`.
- A listing-level scope reference may show multiple active variants together, but it never activates a child Variant or replaces its individual clean reference.

## 6. Migrate Listings Without Rewriting History

For each existing Marketplace listing, choose one path in the manifest:

| Existing listing state | Required action |
| --- | --- |
| Draft, same exact former offer | Update the listing to the parent family and its one inherited child `variant_scope`; retain the listing record. |
| Published, same exact former offer | Preserve the live listing and record its inherited child code in `published_variant_scope`. Do not add new options to that live offer. |
| New selected collection of variants | Create a new variant-scope listing record, internal `listing_ref`, and `listing_handle` using `40_listings/variant_scope_marketplace_listing_workflow.md`. |
| A true bundle offer | Create or retain a separate bundle product record. Do not model it as `variant_scope`. |

Update every migrated record's `product_id`, `product_family_id`, `variant_scope`, source refs, prompt refs, and publication history as applicable. Customer-facing title and description changes still go through the Claude gate.

## 7. Migrate Brand Posts And Social Activation

- Keep historical published content as historical evidence; do not rewrite it to pretend it advertised later variants.
- For a future single-variant post, link the child Variant and require its `Active` status.
- For a future product-family showcase, record `linked_product_family_id`, exact `variant_scope`, and `scope_activation_status: All Variants Active`.
- If the image shows the collection together, attach an approved listing-level `scope_reference_asset` that exactly matches the scope.
- Use the Facebook Page rules and generator; scope references never bypass individual activation or the Claude post-copy gate.

## 8. Validate Before Marking The Conversion Complete

Confirm all of the following:

- parent keeps the original catalog ID and every child has a unique variant code
- every legacy offer maps to one child Variant or an explicit retirement decision
- family and child records contain current source/spec/cost/media references
- no child Variant has its own catalog ID
- every active SKU has its own approved clean reference
- scope references match their declared listing/content scope exactly
- current listings use the right family/variant references and preserve posted scopes
- current social records use either one active child or an all-active declared scope
- stale media and old prompt outputs are marked for regeneration rather than reused
- `10_PROMPTS_INDEX.md`, active prompt generators, and the decision log point to the current workflow

Set the manifest `conversion_status: Complete` only after the validation checklist passes. Record the conversion in `12_DECISION_LOG.md` when it changes operating policy or a live product's durable structure.

## After Conversion

Use the parent family for shared facts and the child Variant records for all option-specific facts. Create new listings by scope, not by inventing a new product number. Future permanent options follow the family/variant workflow; temporary custom requests remain quote-only.
