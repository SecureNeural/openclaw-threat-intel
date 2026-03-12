# OpenClaw Threat Intel

Shared Markdown knowledge base for OpenClaw security research, threat tracking, hardening guidance, and source evidence.

## Structure

- `docs/findings/`: canonical entries for vulnerabilities, exposures, incidents, and malicious-skill activity
- `docs/controls/`: hardening guidance, detection approaches, sandboxing, and scanners
- `docs/sources/`: source records for articles, docs, repos, release notes, and posts
- `docs/timelines/`: curated chronology views
- `docs/taxonomies/`: tags, source types, and confidence rules
- `templates/`: reusable templates for new entries

## Entry Model

Use this rule consistently:

- one canonical entry per security subject
- one or more source records attached to that subject

Do not create duplicate findings because multiple people posted about the same issue.

## Agent Workflow

This repo includes an agent-agnostic maintenance workflow packaged as a local Codex skill at `.codex/skills/openclaw-threat-intel/`.

The same workflow is suitable for Codex, OpenClaw, Claude Code, and similar coding agents because it relies on repository structure and scripts rather than Codex-only features.

Use it when you want an agent to:

- retrieve existing KB information from canonical entries and source records
- ingest new sources into the right `finding`, `control`, or `source` path
- normalize non-English material into English
- scaffold new entries with the helper script
- update the curated newsfeed and regenerate `rss.xml`

## Local Preview

If `mkdocs` is installed:

```bash
mkdocs serve
```

Or with `uv`:

```bash
uvx --with mkdocs-material --with pymdown-extensions --from mkdocs mkdocs serve
```
