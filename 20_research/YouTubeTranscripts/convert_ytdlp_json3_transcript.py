import csv
import json
import re
import sys
from datetime import datetime
from pathlib import Path


def clean_text(text: str) -> str:
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def transcript_from_json3(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    lines = []

    for event in data.get("events", []):
        segs = event.get("segs") or []
        text = "".join(seg.get("utf8", "") for seg in segs)
        text = clean_text(text)
        if text:
            lines.append(text)

    return clean_text(" ".join(lines))


def write_index(index_path: Path, row: dict) -> None:
    fieldnames = [
        "number",
        "title",
        "video_id",
        "channel",
        "url",
        "duration",
        "upload_date",
        "request_time",
        "status",
        "file",
        "source_caption_file",
        "error",
    ]

    rows = []
    if index_path.exists():
        with index_path.open("r", encoding="utf-8", newline="") as f:
            rows = list(csv.DictReader(f))

    rows = [existing for existing in rows if existing.get("video_id") != row["video_id"]]
    rows.append(row)

    with index_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    if len(sys.argv) != 9:
        print(
            "Usage: python convert_ytdlp_json3_transcript.py "
            "<json3> <output_txt> <index_csv> <number> <title> <video_id> <channel> <url>"
        )
        return 2

    json3_path = Path(sys.argv[1])
    output_txt = Path(sys.argv[2])
    index_csv = Path(sys.argv[3])
    number = sys.argv[4]
    title = sys.argv[5]
    video_id = sys.argv[6]
    channel = sys.argv[7]
    url = sys.argv[8]

    transcript = transcript_from_json3(json3_path)
    request_time = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")

    output_txt.parent.mkdir(parents=True, exist_ok=True)
    output_txt.write_text(
        "\n".join(
            [
                f"Title: {title}",
                f"URL: {url}",
                f"Video ID: {video_id}",
                f"Channel: {channel}",
                "Duration: 9:32",
                "Upload Date: 2024-08-12",
                f"Request Time: {request_time}",
                "Transcript Source: YouTube auto captions via yt-dlp json3",
                "",
                "--- TRANSCRIPT ---",
                "",
                transcript,
            ]
        ),
        encoding="utf-8",
    )

    write_index(
        index_csv,
        {
            "number": number,
            "title": title,
            "video_id": video_id,
            "channel": channel,
            "url": url,
            "duration": "9:32",
            "upload_date": "2024-08-12",
            "request_time": request_time,
            "status": "saved",
            "file": output_txt.name,
            "source_caption_file": json3_path.name,
            "error": "",
        },
    )

    print(output_txt)
    print(index_csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
