---
id: control-clawsec-suite
title: ClawSec Suite
type: control
category: scanner
product: openclaw
severity: preventive
status: active
confidence: high
first_seen: 2026-03-02
last_reviewed: 2026-03-11
tags:
  - openclaw
  - advisory-monitoring
  - integrity
  - malicious-skills
  - control
related:
  - source-clawsec-releases-and-skill-index
---

# ClawSec Suite

## Summary

ClawSec Suite is a defensive monitoring and integrity package for OpenClaw. It focuses on advisory feed monitoring, affected-skill checking, signature verification, and approval-gated handling of malicious-skill scenarios.

## What It Covers

- advisory polling and change tracking
- matching advisories against locally installed skills
- signature verification for release material
- hook-based alerting at agent bootstrap or session creation

## Why It Belongs In The KB

This is a control entry that maps to ecosystem and supply-chain risks. It should be linked whenever the KB tracks malicious-skill or advisory-feed developments.

## Source

- Repository source record: [ClawSec releases and skill index](../../sources/repos/clawsec-releases-and-skill-index.md)
