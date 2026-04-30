import csv
import json
import random
import re
import subprocess
import time
from datetime import datetime
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
        request_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

        if not video_id:
            continue

        if video_id in already_saved:
            print(f"[{i}/{len(entries)}] Already saved: {title}")
            rows.append({
                "number": i,
                "title": title,
                "video_id": video_id,
                "url": url,
                "request_time": request_time,
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
                f.write(f"Request Time: {request_time}\n")
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
                rows.append({
                    "number": i,
                    "title": title,
                    "video_id": video_id,
                    "url": url,
                    "request_time": request_time,
                    "status": status,
                    "file": filename,
                    "error": error,
                })
                break

        rows.append({
            "number": i,
            "title": title,
            "video_id": video_id,
            "url": url,
            "request_time": request_time,
            "status": status,
            "file": filename,
            "error": error,
        })

        time.sleep(random.uniform(8, 18))

    with open(INDEX_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "number",
                "title",
                "video_id",
                "url",
                "request_time",
                "status",
                "file",
                "error",
            ],
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