-- DAO Digest - Story Database Schema
-- SQLite database for tracking DAO stories, topics, sources, and coverage over time

-- Core stories table
CREATE TABLE IF NOT EXISTS stories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    source TEXT NOT NULL,
    category TEXT NOT NULL,  -- governance, tooling, funding, regulation, ecosystem, security
    published_date TEXT,     -- ISO 8601 format
    fetched_date TEXT NOT NULL,
    summary TEXT,
    content TEXT,            -- Full scraped content if available
    relevance_score REAL DEFAULT 0.0,
    coverage_status TEXT DEFAULT 'discovered',  -- discovered, covered, monitoring, archived
    edition_date TEXT,       -- Which edition covered this (if any)
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Topics/themes extracted from stories
CREATE TABLE IF NOT EXISTS topics (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    category TEXT,           -- governance, tooling, funding, policy, infra, incident, research
    description TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Many-to-many relationship: stories <-> topics
CREATE TABLE IF NOT EXISTS story_topics (
    story_id INTEGER NOT NULL,
    topic_id INTEGER NOT NULL,
    relevance REAL DEFAULT 1.0,  -- How central is this topic to the story?
    PRIMARY KEY (story_id, topic_id),
    FOREIGN KEY (story_id) REFERENCES stories(id) ON DELETE CASCADE,
    FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE
);

-- Keywords extracted from stories
CREATE TABLE IF NOT EXISTS keywords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    keyword TEXT UNIQUE NOT NULL,
    frequency INTEGER DEFAULT 1,
    first_seen TEXT DEFAULT CURRENT_TIMESTAMP,
    last_seen TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Many-to-many: stories <-> keywords
CREATE TABLE IF NOT EXISTS story_keywords (
    story_id INTEGER NOT NULL,
    keyword_id INTEGER NOT NULL,
    PRIMARY KEY (story_id, keyword_id),
    FOREIGN KEY (story_id) REFERENCES stories(id) ON DELETE CASCADE,
    FOREIGN KEY (keyword_id) REFERENCES keywords(id) ON DELETE CASCADE
);

-- Digest editions
CREATE TABLE IF NOT EXISTS editions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    edition_date TEXT UNIQUE NOT NULL,
    edition_type TEXT DEFAULT 'digest',  -- digest, weekly, special
    title TEXT,
    published BOOLEAN DEFAULT 0,
    substack_url TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    published_at TEXT
);

-- Stories featured in editions
CREATE TABLE IF NOT EXISTS edition_stories (
    edition_id INTEGER NOT NULL,
    story_id INTEGER NOT NULL,
    position INTEGER,         -- Order in the edition
    section TEXT,             -- tl;dr, top-governance, tooling, funding, etc.
    PRIMARY KEY (edition_id, story_id),
    FOREIGN KEY (edition_id) REFERENCES editions(id) ON DELETE CASCADE,
    FOREIGN KEY (story_id) REFERENCES stories(id) ON DELETE CASCADE
);

-- Deep dive topic tracking
CREATE TABLE IF NOT EXISTS deep_dive_candidates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    topic_id INTEGER NOT NULL,
    priority INTEGER DEFAULT 0,
    rationale TEXT,
    story_count INTEGER DEFAULT 0,
    last_coverage_date TEXT,
    status TEXT DEFAULT 'proposed',  -- proposed, researching, drafted, published
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (topic_id) REFERENCES topics(id) ON DELETE CASCADE
);

-- Follow-up tracking
CREATE TABLE IF NOT EXISTS follow_ups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    story_id INTEGER NOT NULL,
    follow_up_type TEXT,      -- governance-vote, funding-round, incident-update, policy
    expected_date TEXT,
    notes TEXT,
    resolved BOOLEAN DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (story_id) REFERENCES stories(id) ON DELETE CASCADE
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_stories_category ON stories(category);
CREATE INDEX IF NOT EXISTS idx_stories_published_date ON stories(published_date);
CREATE INDEX IF NOT EXISTS idx_stories_coverage_status ON stories(coverage_status);
CREATE INDEX IF NOT EXISTS idx_stories_edition_date ON stories(edition_date);
CREATE INDEX IF NOT EXISTS idx_topics_category ON topics(category);
CREATE INDEX IF NOT EXISTS idx_keywords_keyword ON keywords(keyword);

-- Views
CREATE VIEW IF NOT EXISTS v_topic_frequency AS
SELECT 
    t.id,
    t.name,
    t.category,
    COUNT(st.story_id) as story_count
FROM topics t
LEFT JOIN story_topics st ON t.id = st.topic_id
GROUP BY t.id
ORDER BY story_count DESC;

CREATE VIEW IF NOT EXISTS v_recent_stories AS
SELECT * FROM stories
ORDER BY fetched_date DESC;
