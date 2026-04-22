import json
from pathlib import Path

import requests


HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 20
INPUT_PATH = Path(r"c:\Users\outdo\Documents\Woodcraft\20_research\whosthevoss_planter_research.json")


def main() -> None:
    products = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    for product in products:
        print(product["name"])
        links = [u for u in product.get("relevant_links", []) if "youtu" in u.lower()][:2]
        if not links:
            print("  - no youtube links")
            continue
        for link in links:
            try:
                response = requests.get(
                    "https://www.youtube.com/oembed",
                    params={"url": link, "format": "json"},
                    headers=HEADERS,
                    timeout=TIMEOUT,
                )
                response.raise_for_status()
                title = response.json().get("title", "")
                print(f"  - {title}")
            except Exception as exc:
                print(f"  - error: {exc}")


if __name__ == "__main__":
    main()