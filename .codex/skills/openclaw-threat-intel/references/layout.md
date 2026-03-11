# Layout Reference

## Canonical Types

### Findings

Use for:

- product vulnerabilities
- exposed services or weak deployment patterns
- incidents or abuse cases
- malicious-skill ecosystem activity

Paths:

- `docs/findings/vulnerabilities/`
- `docs/findings/exposures/`
- `docs/findings/incidents/`
- `docs/findings/malicious-skills/`

### Controls

Use for:

- hardening baselines
- detection approaches
- sandboxing patterns
- scanners or defensive tools

Paths:

- `docs/controls/hardening/`
- `docs/controls/detection/`
- `docs/controls/sandboxing/`
- `docs/controls/scanners/`

### Sources

Use for:

- articles and reports
- advisories and feeds
- official docs
- social posts
- repos and release pages

Paths:

- `docs/sources/articles/`
- `docs/sources/advisories/`
- `docs/sources/docs/`
- `docs/sources/posts/`
- `docs/sources/repos/`

## Recommended IDs

- Findings: `finding-openclaw-...`
- Controls: `control-...`
- Sources: `source-...`

## Minimum Frontmatter

### Finding

- `id`
- `title`
- `type`
- `category`
- `product`
- `severity`
- `status`
- `confidence`
- `first_seen`
- `last_reviewed`
- `tags`
- `related`

### Control

- `id`
- `title`
- `type`
- `category`
- `product`
- `status`
- `confidence`
- `first_seen`
- `last_reviewed`
- `tags`
- `related`

### Source

- `id`
- `title`
- `type`
- `source_type`
- `publisher`
- `author`
- `published`
- `retrieved`
- `url`
- `language`
- `trust_level`
- `relevance`
- `status`
- `related`
- `tags`
