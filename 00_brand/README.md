# Drakkar Designs Brand Source of Truth

Status: Active source of truth
Created: 2026-06-04
Original asset source package: `20_research/catalog_exports/2026-06-03/source/Drakkar Designs Catalog 6-3-2026/brand/`

Use this folder as the current source of truth for reusable Drakkar Designs identity guidance and approved brand assets.

## Identity References

- [COLOR_PALETTE.md](COLOR_PALETTE.md) — approved color tokens and usage rules
- [TEXT_STYLE_RULES.md](TEXT_STYLE_RULES.md) — typography identity, hierarchy, readability, and reusable prompt wording
- [VISUAL_STYLE.md](VISUAL_STYLE.md) — reusable visual direction for graphics, generated visuals, ads, and image prompts
- [VOICE.md](VOICE.md) — one shared writing voice, four use-case modes, vocabulary, sentence shape, and copy guardrails

## Approved Assets

- `drakkar-logo.png` — primary full logo
- `drakkar-dd.png` — DD mark
- `drakkar-dd-tight.png` — tighter DD mark
- `photos/` — approved catalog product and support images
- `references/` — approved visual references; reference-only unless a workflow explicitly approves listing use
- `references/PRODUCT_REF_IMAGES_MANIFEST.md` — record of the external created product reference image folder at `C:\Users\outdo\Documents\Woodcraft Catalog Setup\Product Ref Images`

## Placement Rules

- Reusable brand identity files belong in `00_brand/`. This includes color palettes, voice guides, visual-style guides, logo guidance, typography guidance, reusable brand marks, and approved brand-reference media.
- Operational records stay with the workflow they serve. Product records remain in `30_products/`, listing records and prompt packs remain in `40_listings/`, content records remain in `50_content/`, and templates remain in `80_templates/`.
- Operational files must point to the relevant `00_brand/` identity references instead of duplicating or owning separate brand rules.
- Historical catalog exports and source packages remain in `20_research/` as provenance. They are not the active brand source of truth.

## Usage Rules

- Read the relevant identity reference before creating brand-specific copy, graphics, ads, images, HTML, templates, prompt packs, or generated visuals.
- Use product photos in `00_brand/photos/` for FBM image prompts and listing-media references.
- Do not overwrite or regenerate approved assets without operator approval.
- If a new brand asset or identity rule is approved, add it here and record its source or provenance in this README or a dated note.

## Provenance

- Logos and approved catalog photos were copied from the saved Drakkar catalog source package.
- `VOICE.md` was promoted from the saved catalog source package; the active copy is UTF-8-clean.
- `TEXT_STYLE_RULES.md` was created from operator-approved typography direction and the saved retail catalog's type system.
- `VISUAL_STYLE.md` was moved from the FBM prompt folder because reusable visual identity belongs with the brand source of truth.
- `references/handmade-cedar-garden-goods-display.png` was copied from the external catalog-setup workspace as the active visual-style reference; the original remains source provenance.
- `references/PRODUCT_REF_IMAGES_MANIFEST.md` records the external folder of created product reference images and logo/title examples; those files remain external until copied into `00_brand/` or selected by an operational record.
