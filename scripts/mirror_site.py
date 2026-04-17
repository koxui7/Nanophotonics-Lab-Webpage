from __future__ import annotations

import argparse
import json
import posixpath
import re
from collections import deque
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse, urlunparse

import requests


ASSET_ATTRS = {
    "a": "href",
    "link": "href",
    "script": "src",
    "img": "src",
    "source": "src",
}

CSS_URL_RE = re.compile(r"url\((['\"]?)(.*?)\1\)")


def normalize_url(base_url: str, candidate: str) -> str | None:
    if not candidate or candidate.startswith(("mailto:", "tel:", "javascript:")):
        return None
    absolute = urljoin(base_url, candidate.strip())
    parsed = urlparse(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    normalized = parsed._replace(fragment="", params="", query=parsed.query or "")
    return urlunparse(normalized)


class LinkExtractor(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__()
        self.base_url = base_url
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_name = ASSET_ATTRS.get(tag)
        attrs_dict = dict(attrs)
        if attr_name and attrs_dict.get(attr_name):
            normalized = normalize_url(self.base_url, attrs_dict[attr_name] or "")
            if normalized:
                self.links.add(normalized)

    def handle_data(self, data: str) -> None:
        for _, value in CSS_URL_RE.findall(data):
            normalized = normalize_url(self.base_url, value)
            if normalized:
                self.links.add(normalized)


def extract_links(base_url: str, html: str) -> set[str]:
    parser = LinkExtractor(base_url)
    parser.feed(html)
    return parser.links


def local_path_for_url(output_root: str | Path, url: str) -> str:
    parsed = urlparse(url)
    path = parsed.path or "/"
    if path.endswith("/") or not posixpath.basename(path):
        path = posixpath.join(path, "index.html")
    destination = Path(output_root) / parsed.netloc / path.lstrip("/")
    return str(destination)


def is_same_site(url: str, host: str) -> bool:
    parsed = urlparse(url)
    return parsed.netloc == host


def should_parse_as_html(url: str, content_type: str) -> bool:
    parsed = urlparse(url)
    return "text/html" in content_type or parsed.path.endswith((".html", ".htm")) or parsed.path in {"", "/"}


def write_bytes(path: str | Path, payload: bytes) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_bytes(payload)


def crawl_site(start_url: str, output_root: str | Path, max_pages: int = 500) -> dict[str, list[str]]:
    session = requests.Session()
    session.headers["User-Agent"] = "PhotonLabMirror/1.0 (+local archive for redesign)"

    host = urlparse(start_url).netloc
    queue: deque[str] = deque([start_url])
    visited: set[str] = set()
    html_pages: list[str] = []
    assets: list[str] = []
    failed: list[str] = []

    while queue and len(visited) < max_pages:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        try:
            response = session.get(url, timeout=20)
        except requests.exceptions.RequestException:
            failed.append(url)
            continue
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            failed.append(url)
            continue

        destination = local_path_for_url(output_root, url)
        write_bytes(destination, response.content)

        content_type = response.headers.get("Content-Type", "")
        if should_parse_as_html(url, content_type):
            html_pages.append(url)
            body = response.text
            for discovered in sorted(extract_links(url, body)):
                if is_same_site(discovered, host) and discovered not in visited:
                    queue.append(discovered)
        else:
            assets.append(url)

    return {
        "start_url": [start_url],
        "html_pages": sorted(html_pages),
        "assets": sorted(assets),
        "failed": sorted(failed),
        "visited": sorted(visited),
    }


def write_reports(output_root: str | Path, manifest: dict[str, list[str]]) -> None:
    report_root = Path(output_root)
    visited = manifest["visited"]
    (report_root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    (report_root / "sitemap.txt").write_text("\n".join(visited) + "\n", encoding="utf-8")


def parse_args(argv: Iterable[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Mirror a static site for local comparison.")
    parser.add_argument("start_url", help="Root URL to mirror")
    parser.add_argument("output_root", help="Directory where the mirrored site should be stored")
    parser.add_argument("--max-pages", type=int, default=500, help="Maximum number of same-site URLs to fetch")
    return parser.parse_args(argv)


def main(argv: Iterable[str] | None = None) -> int:
    args = parse_args(argv)
    manifest = crawl_site(args.start_url, args.output_root, max_pages=args.max_pages)
    write_reports(args.output_root, manifest)
    print(f"Mirrored {len(manifest['visited'])} URLs into {args.output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
