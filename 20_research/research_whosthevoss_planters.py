import json
import re
from html import unescape
from pathlib import Path

import requests


HEADERS = {"User-Agent": "Mozilla/5.0"}
TIMEOUT = 20
OUTPUT_PATH = Path(r"c:\Users\outdo\Documents\Woodcraft\20_research\whosthevoss_planter_research.json")

PLANTER_URLS = [
    "https://www.whosthevoss.com/product-page/post-planter-box",
    "https://www.whosthevoss.com/product-page/pyramid-planter",
    "https://www.whosthevoss.com/product-page/one-picket-planter",
    "https://www.whosthevoss.com/product-page/46-long-planter-box",
    "https://www.whosthevoss.com/product-page/planter-box-p",
    "https://www.whosthevoss.com/product-page/mailbox-post-planter",
    "https://www.whosthevoss.com/product-page/3-picket-planter-plan",
    "https://www.whosthevoss.com/product-page/three-tiered-planter",
    "https://www.whosthevoss.com/product-page/tall-planter-box",
    "https://www.whosthevoss.com/product-page/better-3-picket-planter",
    "https://www.whosthevoss.com/product-page/raised-garden-bed",
    "https://www.whosthevoss.com/product-page/tapered-planter-box",
    "https://www.whosthevoss.com/product-page/trio-planter-boxes",
    "https://www.whosthevoss.com/product-page/bench-planter",
]

DIMENSION_PATTERNS = [
    re.compile(r"\b\d+(?:\.\d+)?\s*(?:x|×)\s*\d+(?:\.\d+)?(?:\s*(?:x|×)\s*\d+(?:\.\d+)?)?\b", re.I),
    re.compile(r"\b\d+(?:\.\d+)?\s*(?:inches|inch|in\.|\"|ft|feet|')\b", re.I),
    re.compile(r"\b(?:width|height|depth|long|length|wide|tall)\s*[:\-]?\s*\d+(?:\.\d+)?\s*(?:inches|inch|in\.|\"|ft|feet|')\b", re.I),
]

LINK_PATTERNS = ("youtube.com", "youtu.be", "drive.google.com", ".pdf", "docs.google.com")


def extract_meta(html: str, name: str) -> str:
    pattern = re.compile(rf'<meta[^>]+property="{re.escape(name)}"[^>]+content="([^"]*)"', re.I)
    match = pattern.search(html)
    return unescape(match.group(1).strip()) if match else ""


def extract_json_ld_product(html: str) -> dict:
    for match in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.I | re.S):
        raw = match.group(1).strip()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and data.get("@type") == "Product":
            return data
    return {}


def strip_html(html: str) -> str:
    text = re.sub(r"<script.*?</script>", " ", html, flags=re.I | re.S)
    text = re.sub(r"<style.*?</style>", " ", text, flags=re.I | re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = unescape(text)
    text = re.sub(r"\s+", " ", text)
    return text


def find_dimension_candidates(text: str) -> list[str]:
    found = []
    for pattern in DIMENSION_PATTERNS:
        for match in pattern.findall(text):
            if isinstance(match, tuple):
                match = " ".join(match)
            candidate = match.strip()
            if candidate and candidate not in found:
                found.append(candidate)
    return found[:12]


def find_relevant_links(html: str) -> list[str]:
    urls = sorted(set(re.findall(r"https?://[^\s\"'<>]+", html)))
    return [url for url in urls if any(p in url.lower() for p in LINK_PATTERNS)][:12]


def main() -> None:
    results = []
    for url in PLANTER_URLS:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        html = response.text
        product = extract_json_ld_product(html)
        text = strip_html(html)
        results.append(
            {
                "url": url,
                "name": product.get("name") or extract_meta(html, "og:title") or url.rsplit("/", 1)[-1],
                "description": product.get("description") or extract_meta(html, "og:description"),
                "website_price_usd": product.get("Offers", {}).get("price") if isinstance(product.get("Offers"), dict) else "",
                "dimension_candidates": find_dimension_candidates(text),
                "relevant_links": find_relevant_links(html),
            }
        )

    OUTPUT_PATH.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(f"Saved {len(results)} planter records to {OUTPUT_PATH}")
    for item in results:
        dims = "; ".join(item["dimension_candidates"][:4]) or "none found"
        print(f"- {item['name']}: dimensions -> {dims}")


if __name__ == "__main__":
    main()