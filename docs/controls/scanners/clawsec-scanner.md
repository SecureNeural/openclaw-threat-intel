---
id: control-clawsec-scanner
title: ClawSec Scanner
type: control
category: scanner
product: openclaw
severity: preventive
status: active
confidence: high
first_seen: 2026-03-10
last_reviewed: 2026-03-11
tags:
  - openclaw
  - scanner
  - sast
  - dast
  - dependency-scanning
related:
  - source-clawsec-releases-and-skill-index
---

# ClawSec Scanner

## Summary

ClawSec Scanner is a defensive control that combines dependency scanning, CVE enrichment, static analysis, and OpenClaw-specific dynamic testing into a single workflow.

## What It Covers

- `npm audit` and `pip-audit` style dependency findings
- OSV, NVD, and GitHub advisory enrichment
- Semgrep and Bandit static analysis
- OpenClaw hook-focused dynamic testing

## Why It Belongs In The KB

This is not a threat entry. It is a response control that operators can deploy to continuously reduce risk and discover issues earlier.

## Source

- Repository source record: [ClawSec releases and skill index](../../sources/repos/clawsec-releases-and-skill-index.md)

## Notes

- Track this entry as a control so future findings can reference it as a mitigation.
