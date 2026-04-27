# Cedar Planter Box Standard Spec

Purpose: define the default launch spec for the cedar planter box so verification can reuse one truthful baseline before any Claude handoff is prepared.

## Spec Identity

- spec_id: spec_cedar_planter_box_standard
- linked_product_id: prod_cedar_planter_box_001
- product_name: Cedar Planter Box Standard Launch Spec
- status: Active
- owner: Lauren
- effective_date: 2026-04-21

## Standard Launch Definition

- target_dimensions: 24in x 24in x 18in high target finished size. For made-to-order pre-sale use, this locked standard size is the listing source of truth unless the launch spec itself changes or proves inaccurate enough to require revision. Capture actual measured finished dimensions after the first real build as post-build validation.
- standard_material_stack: Cedar-board planter build for the launch version, using cedar as the visible primary material for the sides and base components. Do not imply alternate species, trim packages, liners, or hidden upgrades unless they are actually present.
- hardware_assumption: Exterior-rated screws are the standard hardware assumption for the base build.
- drainage_assumption: Basic drain-through / drainage-gap construction only. Do not claim sealed reservoirs, drainage hardware, or other special water-management features unless confirmed.
- liner_included: No. The base launch version excludes a liner unless explicitly added and approved as a deviation.
- finish_assumption: No finish, stain, or coating is assumed unless a specific finished sample confirms otherwise.

For made-to-order items, `target_dimensions` are the stated standard launch dimensions used for truthful pre-sale listings. Small handmade variance does not by itself invalidate the stated standard size, but if real builds show material drift, update the standard spec and listing wording before further sales.

## Fulfillment Baseline

- standard_lead_time_range: 3 to 5 days for made-to-order units, subject to current queue and material availability.
- standard_delivery_policy: Local pickup preferred. Delivery may be available within 25 miles. Ask for an estimate or quote; free delivery may be available in the local area, and a fee may apply outside this area.
- standard_pickup_policy: Local pickup by appointment after completion confirmation.

## Included / Excluded

- included_in_base_version: Assembled cedar planter box in the standard launch size with basic drainage.
- excluded_from_base_version: Plants, soil, liner, custom sizing, finish/stain, installation, shipping, and beyond-radius delivery pricing unless separately approved.

## Deviation Triggers Requiring Operator Confirmation

- Any finished size change from the 24x24x18 target.
- Any liner inclusion/removal change relative to the base version.
- Any change in visible material, hardware type, or finish/coating.
- Any lead-time promise outside the 3 to 5 day baseline.
- Any delivery scope beyond local pickup or paid delivery within 25 miles.
- Any price adjustment needed to preserve guardrail compliance after live cost inputs are added.
- Any customer-facing claim that depends on measured proof, delivery promise, or market comparison not yet confirmed.

## Notes

- notes: This file is a default launch baseline used to reduce repeated decisions, support one-shot verification packets, and provide the pre-sale size truth for the made-to-order standard version. It does not remove the need for live cost inputs, required human approval for final pricing and publishing, or post-build actuals capture.