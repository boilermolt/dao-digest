#!/bin/bash
set -euo pipefail

DATE=${DAO_DATE:-$(date +%F)}

# Convert digest to docx
/home/boilerrat/.venvs/moltbot-docs/bin/python /home/boilerrat/clawd/scripts/dao_digest_to_docx.py --date "$DATE"

# Write to Obsidian vault
python3 /home/boilerrat/clawd/scripts/obsidian_write_dao_digest.py

# Linkify + refresh index
python3 /home/boilerrat/clawd/scripts/obsidian_dao_linkify.py
python3 /home/boilerrat/clawd/scripts/obsidian_dao_index.py

