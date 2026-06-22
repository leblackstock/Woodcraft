# Product To Configurable Family Conversion Manifest Template

Purpose: make an existing standalone-product conversion auditable before changing records, files, media, prompts, or live listing references.

Status: Planning / In Progress / Blocked / Complete

## Conversion Identity

- conversion_id:
- conversion_date:
- owner:
- conversion_status:
- legacy_product_id:
- legacy_catalog_id:
- legacy_catalog_sku:
- legacy_product_name:
- family_product_id:
- family_catalog_id: Preserve the legacy catalog ID unless an explicit catalog migration is approved.
- family_code:
- family_product_name:
- conversion_reason:
- decision_log_ref:

## Legacy Offer To Variant Mapping

| Legacy offer or code | New child Variant code | Child record | Mapping decision | Notes |
| --- | --- | --- | --- | --- |
|  |  |  | Inherited / Retired |  |

## Family And Variant Definition

- shared_family_truth:
- shared_spec_ref:
- shared_cost_ref:
- current_unavailable_options:
- quote_only_boundary:

| Variant code | Customer name | Customer-facing dimensions | Price/finish rule | Spec ref | Cost ref | Clean-reference status | Listing eligibility |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  | Pending / Approved | Draft only / Eligible |

## Legacy Record And File Mapping

| Legacy path or record | New family or child path | Action | Current status | Notes |
| --- | --- | --- | --- | --- |
|  |  | Move / Copy / Retire / Keep historical | Pending / Complete |  |

## External Media And Prompt Mapping

| Legacy filename or prompt | New filename or prompt | Linked child Variant or scope | Hash or provenance | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  | Reuse valid / Regenerate / Retire |

> Mark any image or prompt with superseded price, options, dimensions, title text, or scope as `Regenerate` or `Retire`. Do not present it as current customer-facing media.

## Listing Migration

| Existing listing record | Current status | Posted scope | Conversion action | Resulting listing record / handle |
| --- | --- | --- | --- | --- |
|  | Draft / Published / Archived |  | Update exact legacy scope / Preserve live scope / Create new scope listing / Retire |  |

## Brand Post And Social Migration

| Existing content record | Current status | Product or scope shown | Conversion action | Activation result |
| --- | --- | --- | --- | --- |
|  | Draft / Published / Archived |  | Preserve history / Relink child / Create future scope post | Active / Blocked / Historical |

## Validation Checklist

- [ ] Parent family retains the legacy catalog ID.
- [ ] Every permanent child option has a unique `variant_code` and no independent catalog ID.
- [ ] Legacy offer maps to exactly one child Variant or an explicit retirement decision.
- [ ] Family and child product records link this manifest in `conversion_manifest_ref`.
- [ ] Specs, costs, prompts, and clean references point to the correct child Variant or family parent.
- [ ] Stale external media/prompt outputs are marked for regeneration or retirement.
- [ ] Every active child SKU has its own approved clean reference.
- [ ] Scope references match their exact listing/content `variant_scope` and do not activate variants.
- [ ] Published listings preserve their actual historical offer in `published_variant_scope`.
- [ ] New collections use new listing records and handles.
- [ ] New Facebook Page scope posts require every shown Variant to be Active.
- [ ] `10_PROMPTS_INDEX.md`, active generators, and `12_DECISION_LOG.md` are current.

## Completion

- validation_completed_by:
- validation_date:
- conversion_status: Complete / Blocked
- unresolved_items:
- notes:
