---
id: control-openclaw-gateway-security-baseline
title: OpenClaw gateway security baseline
type: control
category: hardening
product: openclaw
severity: preventive
status: active
confidence: high
first_seen: 2026-03-11
last_reviewed: 2026-03-11
tags:
  - openclaw
  - hardening
  - gateway
  - auth
  - least-privilege
related:
  - source-openclaw-gateway-security-docs
  - finding-openclaw-clawjacked-local-api-exposure
  - finding-openclaw-agent-overreach-sensitive-systems
---

# OpenClaw Gateway Security Baseline

## Summary

Use the OpenClaw gateway security documentation as the baseline control set for local-only deployment, token-based auth, narrow DM scope, and reduced tool access.

## Core Baseline

- Bind the gateway to loopback for local-only operation.
- Require token auth for the control plane.
- Set `session.dmScope` to isolate conversations per peer.
- Use restrictive messaging profiles and deny runtime, fs, and automation groups by default where possible.
- Keep elevated execution disabled unless there is a strong operational reason.

## Why It Matters

These controls directly reduce the blast radius for the most credible abuse paths: exposed local APIs, over-broad tool use, and data leakage through shared inboxes or channels.

## Source

- Documentation source record: [OpenClaw gateway security docs](../../sources/docs/openclaw-gateway-security-docs.md)

## Implementation Notes

- This baseline should be referenced from every exposure or messaging-related finding.
- A later phase can add concrete configuration snippets per deployment mode.
