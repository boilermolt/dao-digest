#!/usr/bin/env python3
"""Import aggregator JSON cache files into the DAO Digest story database.
Also performs topic extraction and classification.
"""

import json
from pathlib import Path
from datetime import datetime
import re

from story_db import StoryDB, Story, Topic

# Topic classification rules for DAO ecosystem
TOPIC_RULES = {
    'Governance Votes': {
        'keywords': ['vote', 'snapshot', 'proposal', 'temp check', 'arfc', 'aip', 'onchain'],
        'category': 'governance'
    },
    'Treasury & Funding': {
        'keywords': ['treasury', 'grant', 'funding', 'budget', 'allocation', 'incentives'],
        'category': 'funding'
    },
    'DAO Tooling': {
        'keywords': ['tally', 'snapshot', 'boardroom', 'syndicate', 'forum', 'tooling'],
        'category': 'tooling'
    },
    'Security & Incidents': {
        'keywords': ['hack', 'exploit', 'vulnerability', 'incident', 'bug bounty'],
        'category': 'security'
    },
    'Regulation & Policy': {
        'keywords': ['sec', 'cftc', 'regulation', 'policy', 'compliance'],
        'category': 'regulation'
    },
    'Ecosystem Launches': {
        'keywords': ['launch', 'upgrade', 'roadmap', 'partnership', 'integration'],
        'category': 'ecosystem'
    }
}

CACHE_DIR = Path("data/cache")


def extract_topics(title: str, summary: str) -> list[Topic]:
    """Extract topics from story text."""
    text = (title + " " + summary).lower()
    topics = []
    
    for topic_name, rule in TOPIC_RULES.items():
        if any(k in text for k in rule['keywords']):
            topics.append(Topic(name=topic_name, category=rule['category']))
    
    return topics


def extract_keywords(title: str, summary: str) -> list[str]:
    """Extract basic keywords from text."""
    text = (title + " " + summary).lower()
    # Simple keyword extraction: words > 4 chars
    words = re.findall(r'\b[a-z]{5,}\b', text)
    # Deduplicate and return top 20
    return list(dict.fromkeys(words))[:20]


def import_cache_file(path: Path, db: StoryDB):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    for item in data.get('items', []):
        story = Story(
            url=item['url'],
            title=item['title'],
            source=item['source'],
            category=item['category'],
            published_date=item.get('published'),
            summary=item.get('summary') or "",
            relevance_score=item.get('score', 0.0),
            fetched_date=item.get('fetched_date') or datetime.now().date().isoformat(),
            coverage_status='discovered'
        )
        story_id = db.add_story(story)
        
        # Topics
        topics = extract_topics(story.title, story.summary or "")
        for t in topics:
            topic_id = db.add_topic(t)
            db.link_story_topic(story_id, topic_id)
        
        # Keywords
        for kw in extract_keywords(story.title, story.summary or ""):
            kw_id = db.add_keyword(kw)
            db.link_story_keyword(story_id, kw_id)


def main():
    db = StoryDB()
    files = sorted(CACHE_DIR.glob("*.json"))
    if not files:
        print("No cache files found in data/cache")
        return
    
    for path in files:
        import_cache_file(path, db)
        print(f"Imported {path.name}")


if __name__ == "__main__":
    main()
