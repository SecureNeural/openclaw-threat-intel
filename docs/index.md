<div class="hero-shell">
  <span class="hero-kicker">Armorer-style Intel Surface</span>
  <h1 class="hero-title">OpenClaw Threat Intel</h1>
  <p class="hero-lead">
    A shared, evidence-backed security knowledge base for OpenClaw attacks, exposures,
    incidents, hardening guidance, and control coverage.
  </p>
  <div class="hero-grid">
    <div class="metric-card">
      <div class="metric-label">Model</div>
      <div class="metric-value">Canonical findings + linked evidence</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Primary Use</div>
      <div class="metric-value">Shared triage and operator reference</div>
    </div>
    <div class="metric-card">
      <div class="metric-label">Ingestion Rule</div>
      <div class="metric-value">Normalize to English, preserve source links</div>
    </div>
  </div>
  <div class="button-cluster">
    <a class="md-button md-button--primary" href="findings/">Browse Findings</a>
    <a class="md-button" href="sources/">Inspect Sources</a>
    <a class="md-button" href="timelines/openclaw-security-timeline/">View Timeline</a>
  </div>
</div>

## Operating Model

<div class="panel-grid">
  <div class="intel-card">
    <div class="intel-eyebrow">Canonical</div>
    <h3>One subject, one main record</h3>
    <p>Findings and controls are the normalized layer. They should not be duplicated because multiple posts mention the same issue.</p>
  </div>
  <div class="intel-card">
    <div class="intel-eyebrow">Evidence</div>
    <h3>Source material lives separately</h3>
    <p>Articles, posts, docs, advisories, and repos stay in <code>sources/</code> and attach to the canonical layer through <code>related</code> links.</p>
  </div>
  <div class="intel-card">
    <div class="intel-eyebrow">Normalization</div>
    <h3>English-first ingestion</h3>
    <p>Non-English material is ingested in English for consistency, while the linked original source remains preserved as evidence.</p>
  </div>
</div>

## Current Coverage

<div class="taxonomy-grid">
  <div class="taxon-card">
    <span class="status-pill">Findings</span>
    <h3>Exposures</h3>
    <p>Local API abuse, control-plane reachability, and deployment mistakes that turn agent capability into host risk.</p>
  </div>
  <div class="taxon-card">
    <span class="status-pill">Findings</span>
    <h3>Incidents</h3>
    <p>Operational misuse, cross-system data leakage, and real-world agent overreach patterns.</p>
  </div>
  <div class="taxon-card">
    <span class="status-pill">Controls</span>
    <h3>Hardening</h3>
    <p>Gateway baselines, DM scoping, auth controls, and least-privilege execution patterns.</p>
  </div>
  <div class="taxon-card">
    <span class="status-pill">Controls</span>
    <h3>Scanners</h3>
    <p>ClawSec scanner and advisory-monitoring controls that map directly to remediation and ongoing coverage.</p>
  </div>
</div>

## Quick Navigation

<div class="inline-link-grid">
  <a class="link-panel" href="findings/">
    <strong>Findings</strong>
    <span>Canonical vulnerabilities, exposures, incidents, and malicious-skill activity.</span>
  </a>
  <a class="link-panel" href="controls/">
    <strong>Controls</strong>
    <span>Hardening baselines, scanners, sandboxing, and detection patterns.</span>
  </a>
  <a class="link-panel" href="sources/">
    <strong>Sources</strong>
    <span>Primary evidence records for articles, docs, advisories, posts, and repos.</span>
  </a>
  <a class="link-panel" href="taxonomies/tags/">
    <strong>Taxonomies</strong>
    <span>Shared tags, source types, and confidence rules for consistent triage.</span>
  </a>
</div>
