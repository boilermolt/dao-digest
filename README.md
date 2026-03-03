# DAO Digest

DAO governance + ecosystem intelligence with a Core Brief–style research database.

## What this repo includes
- **Digest archive** in `/digests/` (markdown + docx)
- **SQLite research database** in `/data/dao_digest.db`
- **Aggregator + importer** in `/src/`
- **Import script** for past digests in `/scripts/`

## Quickstart
```bash
# (optional) fetch RSS sources
python src/aggregator.py

# import aggregator cache into DB
python src/import_aggregator_to_db.py

# import historical digests into DB
python scripts/import_digests.py
```

## Database
See `DATABASE.md` for schema + tables.

## Roadmap
See `PLAN.md`.
