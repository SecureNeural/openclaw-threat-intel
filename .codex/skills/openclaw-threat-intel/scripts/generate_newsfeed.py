#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[4]
SITE_URL = "https://secureneural.github.io/openclaw-threat-intel/"
DATA_PATH = ROOT / "data/newsfeed.json"
INCLUDES_DIR = ROOT / "docs/_includes"
RSS_PATH = ROOT / "docs/rss.xml"


def load_items():
    items = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    items.sort(key=lambda item: item["date"], reverse=True)
    return items


def render_item_card(item):
    return f"""  <a class="feed-item" href="../{item['url']}">
    <div class="feed-meta"><span class="feed-badge">{escape(item['type'])}</span> {escape(item['date'])}</div>
    <h3>{escape(item['title'])}</h3>
    <p>{escape(item['summary'])}</p>
  </a>"""


def render_home_item_card(item):
    return f"""  <a class="feed-item" href="{item['url']}">
    <div class="feed-meta"><span class="feed-badge">{escape(item['type'])}</span> {escape(item['date'])}</div>
    <h3>{escape(item['title'])}</h3>
    <p>{escape(item['summary'])}</p>
  </a>"""


def write_include_files(items):
    INCLUDES_DIR.mkdir(parents=True, exist_ok=True)
    newsfeed_grid = "<div class=\"feed-grid\">\n" + "\n".join(render_item_card(item) for item in items) + "\n</div>\n"
    latest_grid = "<div class=\"feed-grid\">\n" + "\n".join(render_home_item_card(item) for item in items[:6]) + "\n</div>\n"
    INCLUDES_DIR.joinpath("newsfeed-grid.md").write_text(newsfeed_grid, encoding="utf-8")
    INCLUDES_DIR.joinpath("latest-feed.md").write_text(latest_grid, encoding="utf-8")


def item_pub_date(item):
    dt = datetime.fromisoformat(item["date"]).replace(tzinfo=timezone.utc)
    return format_datetime(dt)


def write_rss(items):
    rss_items = []
    for item in items:
        link = SITE_URL + item["url"]
        rss_items.append(
            "    <item>\n"
            f"      <title>{escape(item['title'])}</title>\n"
            f"      <link>{escape(link)}</link>\n"
            f"      <guid>{escape(link)}</guid>\n"
            f"      <pubDate>{escape(item_pub_date(item))}</pubDate>\n"
            f"      <description>{escape('[' + item['type'] + '] ' + item['summary'])}</description>\n"
            "    </item>"
        )
    rss = (
        "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
        "<rss version=\"2.0\">\n"
        "  <channel>\n"
        "    <title>OpenClaw Threat Intel</title>\n"
        f"    <link>{SITE_URL}</link>\n"
        "    <description>Curated OpenClaw threat intel newsfeed.</description>\n"
        "    <language>en-us</language>\n"
        f"    <lastBuildDate>{escape(item_pub_date(items[0]))}</lastBuildDate>\n"
        + "\n".join(rss_items)
        + "\n  </channel>\n"
        "</rss>\n"
    )
    RSS_PATH.write_text(rss, encoding="utf-8")


def main():
    items = load_items()
    write_include_files(items)
    write_rss(items)


if __name__ == "__main__":
    main()
