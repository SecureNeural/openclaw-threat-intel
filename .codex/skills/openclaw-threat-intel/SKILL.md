---
name: openclaw-threat-intel
description: Work inside the OpenClaw Threat Intel repository to retrieve knowledge, ingest new OpenClaw security sources, normalize non-English material into English, and update the MkDocs knowledge base using the canonical finding/control/source model.
---

# OpenClaw Threat Intel

This workflow is designed to be agent-agnostic. The `.codex/skills/` packaging is for Codex, but the operating model, scripts, and file conventions are intended to work equally well for OpenClaw, Claude Code, or any comparable coding agent.

Use this skill when the task is to search, summarize, add, normalize, or structure information in this repository.

## Modes

### Retrieve

When the user wants information from the KB:

1. Search canonical entries first.
2. Search source records second.
3. Prefer `findings/` and `controls/` over repeating raw source text.
4. Answer with:
   - the canonical conclusion
   - confidence level if it matters
   - supporting file links
   - source links when relevant

Use `rg` first:

```bash
rg -n "term" docs/findings docs/controls docs/sources
```

### Add Or Update

When the user wants to add new material:

1. Resolve and read the primary source when possible.
2. If the source is not in English, ingest it in English.
3. Classify it as one of:
   - `finding`
   - `control`
   - `source`
4. Check whether a canonical entry already exists.
5. If the subject already exists:
   - add or update the `source` record
   - link it from the existing canonical entry if needed
6. If the subject does not exist:
   - create the canonical entry
   - create at least one source record
   - link them through `related`
7. If the item is newsworthy for subscribers, add it to `data/newsfeed.json`.
8. Regenerate feed artifacts after newsfeed changes.
9. Update timeline entries only when the new item materially changes the chronology.

Do not create duplicate findings just because multiple posts mention the same issue.

## Content Model

Follow the repository structure:

- `docs/findings/`: canonical vulnerabilities, exposures, incidents, malicious-skill activity
- `docs/controls/`: hardening, detection, sandboxing, scanners
- `docs/sources/`: articles, advisories, docs, posts, repos
- `docs/timelines/`: chronology pages
- `docs/taxonomies/`: shared vocabulary

Read [references/layout.md](references/layout.md) when choosing where an item belongs.

## Writing Rules

- Normalize to concise English.
- Keep titles stable and descriptive.
- Prefer evidence over speculation.
- Mark commentary or anecdotal items as lower trust than primary research or official docs.
- Use frontmatter consistently.
- Keep `related` links updated in both directions when practical.

## Scaffolding

Use the helper script when creating a new file skeleton:

```bash
python3 .codex/skills/openclaw-threat-intel/scripts/scaffold_entry.py \
  --kind source \
  --category articles \
  --slug example-slug \
  --title "Example Title"
```

Supported kinds:

- `finding`
- `control`
- `source`

Supported categories:

- For `finding`: `vulnerabilities`, `exposures`, `incidents`, `malicious-skills`
- For `control`: `hardening`, `detection`, `sandboxing`, `scanners`
- For `source`: `articles`, `advisories`, `docs`, `posts`, `repos`

## Final Check

Before finishing:

1. Verify links and file placement.
2. If the newsfeed changed, run:

```bash
python3 .codex/skills/openclaw-threat-intel/scripts/generate_newsfeed.py
```

3. If docs changed materially, run:

```bash
uvx --from mkdocs mkdocs build
```

4. Report what canonical entries, source records, and feed items were added or updated.
