"""
Scrapes AP News article for title, date, author, and checks if given words appear in the body.
"""
import re
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import requests
from bs4 import BeautifulSoup

URL = "https://apnews.com/article/blizzard-weather-east-coast-a9955d3581a169426ecb0d5fc2941c23"
WORDS = ["Blizzard", "Onomatopoeia", "The"]


def scrape_article(url: str) -> dict:
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    title_el = soup.select_one("h1.Page-headline")
    title = title_el.get_text(strip=True) if title_el else None

    author_el = soup.select_one(".Page-authors a")
    author = author_el.get_text(strip=True) if author_el else None

    # Prefer timestamp (ms) from the page, convert to Eastern and format as MM-DD-YYYY
    date_text = None
    ts_el = soup.select_one("bsp-timestamp[data-timestamp]")
    if ts_el and ts_el.get("data-timestamp"):
        try:
            ts = int(ts_el["data-timestamp"]) / 1000
            dt = datetime.fromtimestamp(ts, tz=ZoneInfo("America/New_York"))
            date_text = dt.strftime("%m-%d-%Y")
        except (ValueError, OSError):
            pass

    # Fallback: parse from byline if no timestamp
    if not date_text:
        byline = soup.select_one(".Page-byline-info")
        if byline:
            for node in byline.find_all(string=True):
                s = node.strip()
                if s.startswith("Updated ") and "[hour]" not in s:
                    match = re.search(r"([A-Za-z]+\s+\d{1,2},\s*\d{4})", s)
                    if match:
                        try:
                            dt = datetime.strptime(match.group(1), "%B %d, %Y")
                            date_text = dt.strftime("%m-%d-%Y")
                        except ValueError:
                            try:
                                dt = datetime.strptime(match.group(1), "%b %d, %Y")
                                date_text = dt.strftime("%m-%d-%Y")
                            except ValueError:
                                date_text = s
                    else:
                        date_text = s
                    break

    # Grab article body (or full page) and see which of WORDS appear in it
    article_el = soup.select_one("article, .ArticleBody, .StoryBody, main")
    article_text = article_el.get_text() if article_el else soup.get_text()
    word_checks = {word: word in article_text for word in WORDS}

    return {"title": title, "date": date_text, "author": author, "word_checks": word_checks}


def main() -> None:
    url = sys.argv[1] if len(sys.argv) > 1 else URL
    data = scrape_article(url)
    print("Title:", data["title"])
    print("Date:", data["date"])
    print("Author:", data["author"])
    for word, found in data["word_checks"].items():
        print(f"  {word}: {found}")


if __name__ == "__main__":
    main()
