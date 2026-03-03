#!/bin/bash
set -euo pipefail

ROOT="/home/boilerrat/clawd/projects/dao-digest"
cd "$ROOT"

# Run DAO RSS aggregator
python3 src/aggregator.py

# Import to DB
python3 src/import_aggregator_to_db.py

