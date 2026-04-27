# Who's the Voss Combined Profitability - Findings Summary

Date: 2026-04-24

Source workbook analyzed: `c:/Users/outdo/Downloads/whosthevoss_combined_profitability_master.xlsx`

## Snapshot

- Rows analyzed: 96
- Safe rows: 54
- Maybe rows: 41
- Quarantine rows: 1
- Shippable rows: 64
- Local-sale rows: 26
- Assumption-sensitive rows: 41
- Manual verification queue: 87 rows

## Key Findings

- The strongest operating path is the safe + shippable segment from `Top_Safe_Candidates`.
- A large assumption-sensitive segment remains and should be verified before committing build capacity.
- A specific product remains explicitly excluded from strict build-plan ranking.
- Several products remain low confidence due to unsurfaced or incomplete product-page details.

## Immediate Safe Picks

- Table Top / Mantel Clock (score 120, gross profit $-33 to $71, P/L hr max 60.86)
- Woven Cross (score 114, gross profit $-27 to $44, P/L hr max 105.6)
- Table Top Plant Holder (score 111, gross profit $-78.75 to $42.4, P/L hr max 21.2)
- Step / Stool (score 108, gross profit $-52 to $66, P/L hr max 34.43)
- Wine Bottle Holder (score 105, gross profit $-25 to $49, P/L hr max 117.6)
- Modular Wine Holder (score 102, gross profit $-33 to $46, P/L hr max 69)
- Plant Stand (score 96, gross profit $-105 to $137, P/L hr max 45.67)
- Phone Speaker Amplifier (score 87.5, gross profit $-27.6 to $39.4, P/L hr max 94.56)

## Low-Confidence Items Needing Research Follow-up

- Lack O Lantern Style Two: URL text incomplete; no surfaced dimensions/materials/sale-mode detail
- Jack-O-Lanterns Style One: URL text incomplete; no surfaced dimensions/materials/sale-mode detail
- Forever Workbench: No surfaced page copy; URL text incomplete; duplicate relationship unresolved
- Table Saw Frame Jig: URL text incomplete; no surfaced dimensions/page copy
- Miter Saw Frame Jig: URL text incomplete; no surfaced dimensions/page copy
- Push Stick 3: Exact shape/thickness/page copy unsurfaced
- Push Stick 2: Exact shape/thickness/page copy unsurfaced
- Flip Cart Drawer: URL text incomplete; no surfaced page copy; fit dependency unresolved
- Lego Shelving: URL text incomplete; no surfaced dimensions/page copy

## Recommended Removal / Quarantine

- French Cleat Dry Erase Board: Live page says no plan is included in the French Cleat download.

## Recommended Next Actions

1. Start build/listing execution from the top safe + shippable entries.
2. Complete BOM and dimension verification for assumption-sensitive and manual-verify rows.
3. Resolve unresolved URL/detail gaps before promoting low-confidence products.
4. Keep using `Decision_View` for decisions and `Final_Master_Combined` for evidence-level audit.
