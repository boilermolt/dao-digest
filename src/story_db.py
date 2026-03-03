#!/usr/bin/env python3
"""DAO Digest - Story Database Manager"""

import sqlite3
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime

DB_PATH = Path(__file__).parent.parent / "data" / "dao_digest.db"
SCHEMA_PATH = Path(__file__).parent / "schema.sql"


@dataclass
class Story:
    url: str
    title: str
    source: str
    category: str
    published_date: Optional[str] = None
    fetched_date: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None
    relevance_score: float = 0.0
    coverage_status: str = "discovered"
    edition_date: Optional[str] = None
    id: Optional[int] = None


@dataclass
class Topic:
    name: str
    category: str
    description: Optional[str] = None
    id: Optional[int] = None


class StoryDB:
    def __init__(self, db_path: Path = DB_PATH):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            schema = SCHEMA_PATH.read_text()
            conn.executescript(schema)

    def add_story(self, story: Story) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO stories (url, title, source, category, published_date, fetched_date,
                                     summary, content, relevance_score, coverage_status, edition_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(url) DO UPDATE SET
                    title=excluded.title,
                    source=excluded.source,
                    category=excluded.category,
                    published_date=excluded.published_date,
                    fetched_date=excluded.fetched_date,
                    summary=excluded.summary,
                    content=excluded.content,
                    relevance_score=excluded.relevance_score,
                    coverage_status=excluded.coverage_status,
                    edition_date=excluded.edition_date,
                    updated_at=CURRENT_TIMESTAMP
                """,
                (
                    story.url, story.title, story.source, story.category,
                    story.published_date, story.fetched_date, story.summary, story.content,
                    story.relevance_score, story.coverage_status, story.edition_date
                )
            )
            cursor.execute("SELECT id FROM stories WHERE url = ?", (story.url,))
            return cursor.fetchone()[0]

    def add_topic(self, topic: Topic) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO topics (name, category, description)
                VALUES (?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                    category=excluded.category,
                    description=excluded.description
                """,
                (topic.name, topic.category, topic.description)
            )
            cursor.execute("SELECT id FROM topics WHERE name = ?", (topic.name,))
            return cursor.fetchone()[0]

    def link_story_topic(self, story_id: int, topic_id: int, relevance: float = 1.0):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO story_topics (story_id, topic_id, relevance)
                VALUES (?, ?, ?)
                """,
                (story_id, topic_id, relevance)
            )

    def add_keyword(self, keyword: str) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO keywords (keyword, frequency)
                VALUES (?, 1)
                ON CONFLICT(keyword) DO UPDATE SET
                    frequency = frequency + 1,
                    last_seen = CURRENT_TIMESTAMP
                """,
                (keyword,)
            )
            cursor.execute("SELECT id FROM keywords WHERE keyword = ?", (keyword,))
            return cursor.fetchone()[0]

    def link_story_keyword(self, story_id: int, keyword_id: int):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO story_keywords (story_id, keyword_id)
                VALUES (?, ?)
                """,
                (story_id, keyword_id)
            )

    def add_edition(self, edition_date: str, title: Optional[str] = None) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO editions (edition_date, title)
                VALUES (?, ?)
                ON CONFLICT(edition_date) DO UPDATE SET title=excluded.title
                """,
                (edition_date, title)
            )
            cursor.execute("SELECT id FROM editions WHERE edition_date = ?", (edition_date,))
            return cursor.fetchone()[0]

    def link_story_to_edition(self, edition_id: int, story_id: int, position: Optional[int] = None,
                              section: Optional[str] = None):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO edition_stories (edition_id, story_id, position, section)
                VALUES (?, ?, ?, ?)
                """,
                (edition_id, story_id, position, section)
            )

    def get_recent_stories(self, days: int = 7) -> List[Dict]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT * FROM stories
                WHERE fetched_date >= date('now', ?)
                ORDER BY fetched_date DESC
                """,
                (f'-{days} days',)
            )
            return [dict(r) for r in cursor.fetchall()]


if __name__ == "__main__":
    db = StoryDB()
    print(f"DAO Digest DB ready: {db.db_path}")
