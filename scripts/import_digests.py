#!/usr/bin/env python3
"""Import past DAO digest markdown files into the DAO Digest database.

- Creates one edition per digest date
- Extracts markdown links as stories
- Uses filename date as edition_date
"""
from __future__ import annotations

import re
from pathlib import Path
from datetime import datetime

import sys
sys.path.append(str(Path(__file__).parent.parent / "src"))
from story_db import StoryDB, Story

DIGEST_DIR = Path(__file__).parent.parent / "digests"

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")


def infer_source(url: str) -> str:
    try:
        host = re.sub(r"^www\.", "", url.split("//", 1)[-1].split("/", 1)[0])
        return host
    except Exception:
        return "unknown"


def guess_category(title: str, url: str) -> str:
    t = (title + " " + url).lower()
    if "governance" in t or "proposal" in t or "vote" in t or "arfc" in t:
        return "governance"
    if "grant" in t or "fund" in t or "treasury" in t:
        return "funding"
    if "tool" in t or "stack" in t or "platform" in t:
        return "tooling"
    if "hack" in t or "exploit" in t or "security" in t:
        return "security"
    if "regulation" in t or "policy" in t:
        return "regulation"
    return "ecosystem"


def import_digest(md_path: Path, db: StoryDB):
    date = md_path.stem[:10]
    edition_id = db.add_edition(date, title=f"DAO Digest — {date}")

    text = md_path.read_text(encoding="utf-8")
    links = LINK_RE.findall(text)

    for i, (label, url) in enumerate(links, start=1):
        story = Story(
            url=url,
            title=label.strip()[:300],
            source=infer_source(url),
            category=guess_category(label, url),
            fetched_date=date,
            coverage_status="covered",
            edition_date=date,
        )
        story_id = db.add_story(story)
        db.link_story_to_edition(edition_id, story_id, position=i)


def main():
    db = StoryDB()
    files = sorted([p for p in DIGEST_DIR.glob("*.md") if p.stem[:4].isdigit()])
    print(f"Importing {len(files)} digests...")
    for f in files:
        import_digest(f, db)
    print("✅ Import complete")


if __name__ == "__main__":
    main()
