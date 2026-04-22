import re
from pathlib import Path


HTML_PATH = Path(r"c:\Users\outdo\Documents\Woodcraft\20_research\whosthevoss_homepage.html")
DOMAINS = (
    "youtube.com",
    "youtu.be",
    "instagram.com",
    "facebook.com",
    "tiktok.com",
)
KEYWORDS = (
    "youtube",
    "instagram",
    "facebook",
    "tiktok",
    "follow",
    "social",
)


def main() -> None:
    html = HTML_PATH.read_text(encoding="utf-8", errors="ignore")
    urls = sorted(set(re.findall(r"https?://[^\s\"'<>]+", html)))
    hits = [url for url in urls if any(domain in url.lower() for domain in DOMAINS)]

    print(f"Social links found: {len(hits)}")
    for url in hits:
        print(url)

    if hits:
        return

    lowered = html.lower()
    snippets = []
    for keyword in KEYWORDS:
        start = 0
        count = 0
        while True:
            idx = lowered.find(keyword, start)
            if idx == -1:
                break
            count += 1
            if len(snippets) < 8:
                snippet = html[max(0, idx - 50): idx + 90]
                snippet = " ".join(snippet.split())
                snippets.append(f"[{keyword}] {snippet}")
            start = idx + len(keyword)
        print(f"Keyword '{keyword}': {count}")

    for snippet in snippets:
        print(snippet)


if __name__ == "__main__":
    main()