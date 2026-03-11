---
id: source-openclaw-gateway-security-docs
title: OpenClaw gateway security documentation
type: source
source_type: docs
publisher: OpenClaw
author: OpenClaw
published: 2026-03-11
retrieved: 2026-03-11
url: https://docs.openclaw.ai/gateway/security
language: en
trust_level: primary
relevance: high
status: reviewed
related:
  - control-openclaw-gateway-security-baseline
tags:
  - openclaw
  - gateway
  - hardening
  - auth
---

# Source Summary

## What It Contains

This documentation page provides the vendor-recommended gateway security baseline, including loopback binding, token-based auth, restrictive tool profiles, DM scoping, and disabled elevated execution.

## Extracted Claims

- Local-only gateway operation should use loopback binding.
- Control-plane access should require tokens.
- Shared or messaging workflows need tighter session scoping and restricted tool groups.
- Broad tool access and shared DMs should not be combined.

## Evidence Quality

Primary documentation from the product vendor. Strong for hardening guidance.

## Follow-Up

- Add environment-specific config examples as separate control records if needed.
