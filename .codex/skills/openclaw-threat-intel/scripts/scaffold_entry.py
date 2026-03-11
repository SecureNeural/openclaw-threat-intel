#!/usr/bin/env python3
import argparse
from datetime import date
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[4]
TODAY = date.today().isoformat()

PATHS = {
    "finding": {
        "vulnerabilities": ROOT / "docs/findings/vulnerabilities",
        "exposures": ROOT / "docs/findings/exposures",
        "incidents": ROOT / "docs/findings/incidents",
        "malicious-skills": ROOT / "docs/findings/malicious-skills",
    },
    "control": {
        "hardening": ROOT / "docs/controls/hardening",
        "detection": ROOT / "docs/controls/detection",
        "sandboxing": ROOT / "docs/controls/sandboxing",
        "scanners": ROOT / "docs/controls/scanners",
    },
    "source": {
        "articles": ROOT / "docs/sources/articles",
        "advisories": ROOT / "docs/sources/advisories",
        "docs": ROOT / "docs/sources/docs",
        "posts": ROOT / "docs/sources/posts",
        "repos": ROOT / "docs/sources/repos",
    },
}


def build_frontmatter(kind: str, category: str, slug: str, title: str) -> str:
    if kind == "finding":
        return f"""---
id: finding-{slug}
title: {title}
type: finding
category: {category.rstrip('s')}
product: openclaw
severity: medium
status: needs-triage
confidence: medium
first_seen: {TODAY}
last_reviewed: {TODAY}
tags:
  - openclaw
related: []
---

# {title}

## Summary

## Why It Matters

## Attack Path

## Affected Surface

## Evidence

## Mitigations

## Open Questions
"""
    if kind == "control":
        return f"""---
id: control-{slug}
title: {title}
type: control
category: {category.rstrip('s')}
product: openclaw
status: active
confidence: medium
first_seen: {TODAY}
last_reviewed: {TODAY}
tags:
  - openclaw
related: []
---

# {title}

## Summary

## What It Covers

## Why It Matters

## Source

## Notes
"""
    return f"""---
id: source-{slug}
title: {title}
type: source
source_type: {category[:-1] if category.endswith('s') else category}
publisher: Unknown
author: Unknown
published: {TODAY}
retrieved: {TODAY}
url: https://example.com
language: en
trust_level: secondary
relevance: medium
status: reviewed
related: []
tags:
  - openclaw
---

# Source Summary

## What It Contains

## Extracted Claims

- 

## Evidence Quality

## Follow-Up
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold a KB entry for openclaw-threat-intel.")
    parser.add_argument("--kind", required=True, choices=PATHS.keys())
    parser.add_argument("--category", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    if args.category not in PATHS[args.kind]:
        valid = ", ".join(sorted(PATHS[args.kind].keys()))
        print(f"invalid category '{args.category}' for kind '{args.kind}'. valid: {valid}", file=sys.stderr)
        return 1

    target_dir = PATHS[args.kind][args.category]
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{args.slug}.md"

    if target.exists():
        print(f"refusing to overwrite existing file: {target}", file=sys.stderr)
        return 1

    target.write_text(build_frontmatter(args.kind, args.category, args.slug, args.title), encoding="utf-8")
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
