---
id: finding-openclaw-clawjacked-local-api-exposure
title: ClawJacked local API exposure can enable remote abuse and code execution
type: finding
category: exposure
product: openclaw
severity: critical
status: confirmed
confidence: high
first_seen: 2026-02-19
last_reviewed: 2026-03-11
tags:
  - openclaw
  - exposure
  - remote-code-execution
  - local-api
  - auth
related:
  - source-oasis-clawjacked-2026-02-19
  - control-openclaw-gateway-security-baseline
---

# ClawJacked Local API Exposure

## Summary

Oasis Security documented a class of OpenClaw abuse in which the local agent API can be reached or influenced in ways that break the assumption of single-user local trust. The reported outcome is serious because a reachable or weakly protected local control surface can be driven into dangerous actions, including code execution through the agent runtime.

## Why It Matters

OpenClaw is powerful specifically because it can read files, run commands, and orchestrate tools. If the local control plane becomes reachable to an attacker, the impact is not limited to data disclosure. It can become a host-compromise path.

## Attack Path

- Victim runs OpenClaw with an exposed or insufficiently protected local API surface.
- An attacker reaches that surface directly or indirectly.
- The attacker issues agent actions that the local operator did not intend.
- The agent runtime performs commands or file operations with the victim's local privileges.

## Affected Surface

- Local agent API and gateway exposure model
- Weak binding or auth assumptions
- Deployments that treat local-only access as an adequate trust boundary

## Evidence

- Primary source record: [Oasis ClawJacked source](../../sources/articles/oasis-clawjacked-2026-02-19.md)

## Mitigations

- Bind gateway interfaces to loopback only unless remote access is explicitly required.
- Require token-based auth for any control plane that can trigger tools or runtime actions.
- Deny dangerous tool groups by default in messaging or shared-inbox profiles.
- Use pairing or strict allowlists for DM-style channels.

## Open Questions

- Exact version scope should be added if the source or a follow-up advisory specifies it.
- Reproduction notes can be added later if you want a lab-validation appendix.
