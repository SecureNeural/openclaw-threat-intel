# OpenClaw Threat Intel Agent Guide

This repository is maintained through a shared workflow that should work for Codex, OpenClaw, Claude Code, and similar coding agents.

## Goal

Keep the OpenClaw Threat Intel knowledge base accurate, structured, and easy to browse.

## Core Model

- `docs/findings/`: canonical security subjects
- `docs/controls/`: defensive guidance and operator actions
- `docs/sources/`: evidence records
- `docs/newsfeed/`: curated latest-items view
- `docs/rss.xml`: RSS feed generated from `data/newsfeed.json`

Do not create duplicate findings because multiple posts mention the same issue.

## Retrieval Workflow

When answering a question from the KB:

1. Search `findings/` and `controls/` first.
2. Search `sources/` second.
3. Prefer the canonical conclusion over repeating raw source text.
4. Include confidence or trust context when it matters.

Use fast search first:

```bash
rg -n "term" docs/findings docs/controls docs/sources
```

## Ingestion Workflow

When adding a new item:

1. Resolve and read the primary source when possible.
2. Normalize non-English content into English.
3. Classify the item as:
   - `finding`
   - `control`
   - `source`
4. Check for an existing canonical entry.
5. If it already exists:
   - add or update the source record
   - link it through `related`
6. If it does not exist:
   - create the canonical entry
   - create at least one source record
   - link them through `related`
7. If the item belongs in the subscriber-facing feed, add it to `data/newsfeed.json`.
8. Regenerate feed artifacts.
9. Update the timeline only when the chronology changes materially.

## Feed Workflow

If `data/newsfeed.json` changes, run:

```bash
python3 .codex/skills/openclaw-threat-intel/scripts/generate_newsfeed.py
```

This regenerates:

- `docs/_includes/latest-feed.md`
- `docs/_includes/newsfeed-grid.md`
- `docs/rss.xml`

## Scaffolding

Use the helper script for new file skeletons:

```bash
python3 .codex/skills/openclaw-threat-intel/scripts/scaffold_entry.py \
  --kind source \
  --category articles \
  --slug example-slug \
  --title "Example Title"
```

## Final Verification

Before finishing:

1. Verify links and file placement.
2. If the feed changed, regenerate it.
3. If docs changed materially, run:

```bash
uvx --with mkdocs-material --with pymdown-extensions --from mkdocs mkdocs build --strict
```

4. Report what canonical entries, source records, and feed items were added or updated.
