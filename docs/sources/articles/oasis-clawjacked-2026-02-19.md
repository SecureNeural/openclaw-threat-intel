---
id: source-oasis-clawjacked-2026-02-19
title: ClawJacked: The new OpenClaw vulnerability exposing remote code execution risks
type: source
source_type: article
publisher: Oasis Security
author: Oasis Security
published: 2026-02-19
retrieved: 2026-03-11
url: https://www.oasis.security/resources/blog/clawjacked-the-new-openclaw-vulnerability-exposing-remote-code-execution-risks
language: en
trust_level: primary
relevance: high
status: reviewed
related:
  - finding-openclaw-clawjacked-local-api-exposure
tags:
  - openclaw
  - exposure
  - remote-code-execution
---

# Source Summary

## What It Contains

This is a primary vendor research article describing the ClawJacked risk pattern around OpenClaw local API exposure and the resulting code-execution implications.

## Extracted Claims

- Local OpenClaw control surfaces can become remotely abusable when deployment assumptions fail.
- The security consequence is not limited to data exposure and can include command or code execution through the agent runtime.
- Mitigation depends on binding, auth, and restrictive access patterns rather than prompt changes alone.

## Evidence Quality

Primary research from a security vendor. High-value for threat modeling and hardening guidance.

## Follow-Up

- Add version scope and any vendor patch details if they are published later.
