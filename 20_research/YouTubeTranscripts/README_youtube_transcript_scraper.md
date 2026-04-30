# YouTube Channel Transcript Scraper — No API Key Needed

This project pulls available YouTube transcripts from a specific channel and saves them as searchable `.txt` files.

Current target channel:

```text
https://www.youtube.com/@WhosTheVoss/videos
```

It uses:

- `yt-dlp` to get the channel's video list.
- `youtube-transcript-api` to fetch public/manual/auto-generated transcripts.
- Python to save transcripts and create an `index.csv`.

No YouTube API key is required.

---

## What This Is For

Use this when you want to gather searchable information from a YouTube channel, such as:

- Build instructions
- Product ideas
- Tool mentions
- Pricing comments
- Material choices
- Sales/business advice
- Repeated tips across multiple videos

For example, with a woodworking channel, you can search all saved transcripts for terms like:

```text
planter
cedar
picket
Facebook
Marketplace
price
sell
jig
```

---

## Folder Setup

Recommended location:

```powershell
D:\YouTubeTranscripts
```

The script will create this output folder automatically:

```text
D:\YouTubeTranscripts\WhosTheVoss_transcripts
```

Inside that folder, you will get:

```text
001 - Video Title.txt
002 - Video Title.txt
index.csv
```

Each transcript file includes:

- Video title
- Video URL
- Video ID
- Transcript text

The `index.csv` tracks:

- Video number
- Title
- Video ID
- URL
- Status
- Saved filename
- Error message, if any

---

## Requirements

You need Python installed.

Check Python:

```powershell
python --version
```

Example working version:

```text
Python 3.12.6
```

Install the required packages:

```powershell
python -m pip install yt-dlp youtube-transcript-api
```

If anything acts weird, update them:

```powershell
python -m pip install --upgrade yt-dlp youtube-transcript-api
```

---

## Create the Project Folder

In PowerShell:

```powershell
D:
mkdir D:\YouTubeTranscripts
cd D:\YouTubeTranscripts
```

If the folder already exists, just go into it:

```powershell
cd D:\YouTubeTranscripts
```

---

## Create the Script

Open Notepad from PowerShell:

```powershell
notepad pull_transcripts.py
```

Paste the script into Notepad, save it, then close Notepad.

---

## Script: `pull_transcripts.py`

```python
import csv
import json
import random
import re
import subprocess
import time
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

CHANNEL_URL = "https://www.youtube.com/@WhosTheVoss/videos"
OUTPUT_DIR = Path("WhosTheVoss_transcripts")
OUTPUT_DIR.mkdir(exist_ok=True)

INDEX_CSV = OUTPUT_DIR / "index.csv"


def safe_filename(text: str, max_len: int = 120) -> str:
    text = re.sub(r'[<>:"/\\|?*]', "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_len] or "untitled"


def get_video_entries(channel_url: str):
    cmd = ["yt-dlp", "--flat-playlist", "--dump-single-json", channel_url]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    data = json.loads(result.stdout)
    return data.get("entries", [])


def get_existing_saved_ids():
    if not INDEX_CSV.exists():
        return set()

    saved_ids = set()
    with open(INDEX_CSV, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("status") == "saved":
                saved_ids.add(row.get("video_id"))
    return saved_ids


def get_transcript_text(video_id: str):
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages=["en", "en-US", "en-GB"])

    lines = []
    for item in transcript:
        text = item.text.replace("\n", " ").strip()
        if text:
            lines.append(text)

    return " ".join(lines)


def main():
    print(f"Getting video list from: {CHANNEL_URL}")
    entries = get_video_entries(CHANNEL_URL)

    already_saved = get_existing_saved_ids()
    rows = []

    print(f"Found {len(entries)} videos.")
    print(f"Already saved: {len(already_saved)}")
    print("Trying remaining transcripts slowly...")

    for i, entry in enumerate(entries, start=1):
        video_id = entry.get("id")
        title = entry.get("title") or video_id
        url = f"https://www.youtube.com/watch?v={video_id}"

        if not video_id:
            continue

        if video_id in already_saved:
            print(f"[{i}/{len(entries)}] Already saved: {title}")
            rows.append({
                "number": i,
                "title": title,
                "video_id": video_id,
                "url": url,
                "status": "saved",
                "file": "already_saved",
                "error": "",
            })
            continue

        print(f"[{i}/{len(entries)}] Trying: {title}")

        try:
            transcript_text = get_transcript_text(video_id)

            filename = f"{i:03d} - {safe_filename(title)}.txt"
            filepath = OUTPUT_DIR / filename

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"Title: {title}\n")
                f.write(f"URL: {url}\n")
                f.write(f"Video ID: {video_id}\n")
                f.write("\n--- TRANSCRIPT ---\n\n")
                f.write(transcript_text)

            status = "saved"
            error = ""

        except Exception as e:
            status = "error/skipped"
            error = type(e).__name__ + ": " + str(e)
            filename = ""

            if "IpBlocked" in error or "RequestBlocked" in error:
                print("YouTube blocked requests again. Stop here and try later.")
                break

        rows.append({
            "number": i,
            "title": title,
            "video_id": video_id,
            "url": url,
            "status": status,
            "file": filename,
            "error": error,
        })

        time.sleep(random.uniform(8, 18))

    with open(INDEX_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["number", "title", "video_id", "url", "status", "file", "error"],
        )
        writer.writeheader()
        writer.writerows(rows)

    saved = sum(1 for r in rows if r["status"] == "saved")
    failed = sum(1 for r in rows if r["status"] != "saved")

    print("\nDone.")
    print(f"Saved/previously saved: {saved}")
    print(f"Skipped/errors this run: {failed}")
    print(f"Folder: {OUTPUT_DIR.resolve()}")
    print(f"Index: {INDEX_CSV.resolve()}")


if __name__ == "__main__":
    main()
```

---

## Run the Script

From PowerShell:

```powershell
cd D:\YouTubeTranscripts
python pull_transcripts.py
```

The script will:

1. Get the list of videos from the channel.
2. Skip transcripts that were already saved.
3. Try to fetch transcripts for the remaining videos.
4. Save successful transcripts as `.txt` files.
5. Update `index.csv`.
6. Wait 8–18 seconds between transcript requests.
7. Stop if YouTube blocks requests.

---

## Why the Script Waits Between Requests

YouTube may temporarily block transcript requests if too many are made too quickly.

A previous run found:

```text
Found 122 videos
Saved transcripts: 40
Skipped/errors: 82
```

The errors in `index.csv` were `IpBlocked`, which means the transcript tool was blocked temporarily by YouTube. It does **not** necessarily mean those videos have no transcript.

That is why the slower script:

- Resumes from already saved videos.
- Waits 8–18 seconds between requests.
- Stops if blocked instead of hammering YouTube.
- Reduces the chance of making the temporary block worse.

Tiny subtitle goblin must act casual.

---

## How Long to Wait After Being Blocked

Recommended waiting times:

| Situation | Wait Time |
|---|---:|
| First block | 1–2 hours minimum |
| Safer first retry | 3–6 hours |
| Best low-stress retry | Next day |
| Blocks again quickly | 12–24 hours |

Do not keep rerunning immediately after an `IpBlocked` or `RequestBlocked` error. That usually makes YouTube grumpier.

---

## Check Saved Files

List the output folder:

```powershell
dir D:\YouTubeTranscripts\WhosTheVoss_transcripts
```

Open the index:

```powershell
notepad D:\YouTubeTranscripts\WhosTheVoss_transcripts\index.csv
```

Or open it with Excel/LibreOffice if you want easier sorting and filtering.

---

## Search the Transcripts

Search for a word or phrase:

```powershell
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "planter"
```

Useful searches:

```powershell
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "price"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "sell"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "Facebook"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "Marketplace"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "cedar"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "picket"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "jig"
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "table saw"
```

Search for an exact phrase:

```powershell
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "Facebook Marketplace"
```

---

## What Each Major Part Does

### `CHANNEL_URL`

```python
CHANNEL_URL = "https://www.youtube.com/@WhosTheVoss/videos"
```

This is the channel videos page the script reads from.

To use a different channel, replace this URL.

---

### `OUTPUT_DIR`

```python
OUTPUT_DIR = Path("WhosTheVoss_transcripts")
```

This is where transcript files and `index.csv` are saved.

Because it is a relative path, it saves inside the folder where the script is run:

```text
D:\YouTubeTranscripts\WhosTheVoss_transcripts
```

---

### `safe_filename()`

Cleans video titles so Windows can use them as filenames.

It removes characters Windows does not allow in filenames, such as:

```text
< > : " / \ | ? *
```

---

### `get_video_entries()`

Uses `yt-dlp` to get the video list from the channel without downloading the videos.

This command is run internally:

```powershell
yt-dlp --flat-playlist --dump-single-json https://www.youtube.com/@WhosTheVoss/videos
```

Why this matters:

- No YouTube API key needed.
- No video downloading.
- Fast video ID collection.

---

### `get_existing_saved_ids()`

Reads the existing `index.csv` and remembers which video IDs already saved successfully.

This prevents wasting requests on videos already downloaded.

---

### `get_transcript_text()`

Uses `youtube-transcript-api` to request the English transcript for one video.

It tries:

```text
en
en-US
en-GB
```

It can work with public transcripts and many auto-generated captions, but only when YouTube exposes them.

---

### `main()`

Controls the whole workflow:

1. Gets the channel video list.
2. Checks what was already saved.
3. Loops through the videos.
4. Downloads available transcripts.
5. Saves each transcript as `.txt`.
6. Logs results to `index.csv`.
7. Waits between requests.
8. Stops if YouTube blocks the run.

---

## Common Errors

### `IpBlocked`

YouTube temporarily blocked transcript requests.

Fix:

```text
Wait 3–6 hours, then try again.
```

If it happens again fast, wait 12–24 hours.

---

### `RequestBlocked`

Similar to `IpBlocked`.

Fix:

```text
Stop running the script and wait.
```

---

### `NoTranscriptFound`

The video may not have an available transcript in the requested language.

This one may be a real skip.

---

### `TranscriptsDisabled`

The video owner disabled transcripts/captions, or YouTube does not expose them.

---

### `VideoUnavailable`

The video may be private, deleted, region-blocked, age-restricted, or otherwise unavailable.

---

### `yt-dlp` Not Found

Update/reinstall:

```powershell
python -m pip install --upgrade yt-dlp
```

Then try again.

---

### `youtube_transcript_api` Not Found

Install/update:

```powershell
python -m pip install --upgrade youtube-transcript-api
```

---

## Safer Usage Tips

- Do not repeatedly rerun immediately after a block.
- Use the slower resume script.
- Run in small chunks over time if needed.
- Keep `index.csv`; it is what lets the script avoid redoing saved work.
- Update packages if YouTube changes things.

---

## Optional Next Step: Turn Transcripts Into Notes

Once transcripts are saved, you can use them to create:

- A searchable woodworking idea database
- Product idea notes
- Build-method summaries
- Pricing/sales strategy notes
- Material lists
- A spreadsheet of project ideas
- AI summaries grouped by topic

Example workflow:

```text
Saved transcript files
    ↓
Search by keyword
    ↓
Copy relevant transcripts into ChatGPT
    ↓
Ask for summaries, product ideas, pricing notes, or build takeaways
```

---

## Quick Command Cheat Sheet

```powershell
D:
cd D:\YouTubeTranscripts
python -m pip install --upgrade yt-dlp youtube-transcript-api
notepad pull_transcripts.py
python pull_transcripts.py
dir D:\YouTubeTranscripts\WhosTheVoss_transcripts
Select-String -Path "D:\YouTubeTranscripts\WhosTheVoss_transcripts\*.txt" -Pattern "planter"
```
