# Woodcraft Local Research Database

This folder contains the free local search setup for the Woodcraft research files.

## What It Does

- Builds a local SQLite database from saved markdown and transcript files.
- Keeps markdown as the source of truth.
- Indexes videos, transcripts, current product records, catalog IDs, product cross-references, unmatched current products, and video ideas that are not yet product records.
- Runs a local browser UI with Python's standard library. No paid service, cloud database, or hosting is required.

## Source Files

- `20_research/YouTubeTranscripts/analysis/whosthevoss_video_concept_product_index_2026-04-30.md`
- `20_research/YouTubeTranscripts/analysis/whosthevoss_video_to_current_products_cross_reference_2026-04-30.md`
- `20_research/YouTubeTranscripts/WhosTheVoss_transcripts/*.txt`
- `30_products/prod_*.md`

## Generated File

- `20_research/YouTubeTranscripts/analysis/woodcraft_research.sqlite`

The SQLite file is rebuildable. If the markdown changes, run the build command again.
If the local web UI is already running, stop it before rebuilding so the SQLite file is not locked.

## Build

From the repo root:

```powershell
python 60_automation\research_database\build_research_db.py
```

## Run Local Web UI

From the repo root:

```powershell
python 60_automation\research_database\server.py
```

Then open:

```text
http://127.0.0.1:8765
```

If port `8765` is already in use, launch another port from the repo root:

```powershell
python 60_automation\research_database\server.py --port 8766
```

Then open:

```text
http://127.0.0.1:8766
```

## Local Playwright Note

Playwright is installed on this computer even if the current Node workspace does not expose it:

- CLI: `D:\Python312\Scripts\playwright.exe`
- Version checked: `1.51.0`
- Python package path: `D:\Python312\Lib\site-packages\playwright\`
- Chromium browser binary installed at: `C:\Users\outdo\AppData\Local\ms-playwright\chromium-1161`
- Chromium headless shell installed at: `C:\Users\outdo\AppData\Local\ms-playwright\chromium_headless_shell-1161`

If a browser check later fails with a missing executable under `C:\Users\outdo\AppData\Local\ms-playwright\`, reinstall the browser binary:

```powershell
playwright install chromium
```

Latest verified UI check:

```powershell
playwright screenshot --viewport-size "900,500" --wait-for-selector ".floating-scrollbar.visible" --timeout 10000 http://127.0.0.1:8766/ $env:TEMP\woodcraft_research_ui_scrollbar_check.png
```

## Rebuild and Relaunch Pattern

Use this whenever transcripts, product records, or cross-reference markdown changes:

```powershell
python 60_automation\research_database\build_research_db.py
python 60_automation\research_database\server.py
```

## Design Rule

Do not manually edit the SQLite database. Edit the markdown/product/transcript source files, then rebuild.
