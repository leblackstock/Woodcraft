# Standard Product Spec Template

Purpose: define the default launch spec for a repeatable product so GPT-5.5 can infer safe defaults, flag deviations, and reduce repeated operator input.

## Spec Identity

- spec_id:
- linked_product_id:
- product_name:
- status: Draft / Active / Retired
- owner:
- effective_date:

## Standard Launch Definition

- target_dimensions: Stated standard launch dimensions used as the truthful pre-sale size source for made-to-order listings when this spec is locked. Capture actual measured finished dimensions later as post-build validation.
- standard_material_stack:
- hardware_assumption:
- drainage_assumption:
- liner_included: Yes / No / Optional
- finish_assumption:

For made-to-order products, small handmade variance does not automatically invalidate the stated standard size as long as the listing remains truthful. If actual builds show material drift, update the standard spec and listing wording before further sales.

## Fulfillment Baseline

- standard_lead_time_range:
- standard_delivery_policy:
- standard_pickup_policy:

## Included / Excluded

- included_in_base_version:
- excluded_from_base_version:

## Deviation Triggers Requiring Operator Confirmation

- deviation_1:
- deviation_2:
- deviation_3:
- deviation_4:

## Notes

- notes: Use this file as the standard launch source of truth for pre-sale listing facts when the spec is locked. It does not remove the need for live cost inputs, human approval, or post-build actuals capture.