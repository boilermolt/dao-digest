# DAO Digest Database

SQLite database for DAO stories, topics, keywords, and edition coverage.

**DB file:** `data/dao_digest.db`

## Core tables
- `stories` — individual articles/stories (url, title, source, category)
- `topics` — extracted themes (governance, funding, tooling, regulation, security)
- `story_topics` — many-to-many relationship
- `keywords` + `story_keywords` — keyword tracking
- `editions` — each digest edition (date, title, published)
- `edition_stories` — which stories were covered in each edition
- `deep_dive_candidates` — topics to research deeper
- `follow_ups` — items to monitor

## Views
- `v_topic_frequency` — topic counts
- `v_recent_stories` — recently fetched stories

## Importers
- `scripts/import_digests.py` — parses past digest markdown and writes editions + story links
- `src/import_aggregator_to_db.py` — imports RSS cache JSON into the DB
