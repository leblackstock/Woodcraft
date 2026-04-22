import json
import re
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import requests


HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 20
INPUT_PATH = Path(r"c:\Users\outdo\Documents\Woodcraft\20_research\whosthevoss_planter_research.json")
OUTPUT_PATH = Path(r"c:\Users\outdo\Documents\Woodcraft\20_research\whosthevoss_dimension_search.json")
DIMENSION_RE = re.compile(
    r"\b(?:\d+(?:\.\d+)?\s*(?:x|×)\s*\d+(?:\.\d+)?(?:\s*(?:x|×)\s*\d+(?:\.\d+)?)?|\d+(?:\.\d+)?\s*(?:inches|inch|in\.|\"|ft|feet|'))\b",
    re.I,
)


def search_bing(query: str) -> list[dict]:
    url = "https://www.bing.com/search?format=rss&q=" + urllib.parse.quote(query)
    response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
    response.raise_for_status()
    root = ET.fromstring(response.text)
    items = []
    for item in root.findall(".//item")[:5]:
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").strip()
        description = (item.findtext("description") or "").strip()
        items.append({"title": title, "link": link, "description": description})
    return items


def main() -> None:
    products = json.loads(INPUT_PATH.read_text(encoding="utf-8"))
    results = []
    for product in products:
        query = f'WhosTheVoss "{product["name"]}" dimensions size'
        items = search_bing(query)
        dimension_hits = []
        for item in items:
            blob = f'{item["title"]} {item["description"]}'
            hits = DIMENSION_RE.findall(blob)
            if hits:
                dimension_hits.extend(hits)
        deduped_hits = []
        for hit in dimension_hits:
            clean = hit.strip()
            if clean not in deduped_hits:
                deduped_hits.append(clean)
        results.append(
            {
                "name": product["name"],
                "query": query,
                "dimension_hits": deduped_hits,
                "results": items,
            }
        )

    OUTPUT_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")
    print(f"Saved dimension search results to {OUTPUT_PATH}")
    for item in results:
        summary = "; ".join(item["dimension_hits"]) if item["dimension_hits"] else "none"
        print(f'- {item["name"]}: {summary}')


if __name__ == "__main__":
    main()