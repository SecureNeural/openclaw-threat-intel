# Tags

<div class="section-band">
  <p>
    Tags support cross-cutting navigation, but they do not replace the canonical structure.
    Keep the vocabulary tight and reusable.
  </p>
</div>

<div class="taxonomy-grid">
  <div class="taxon-card"><h3><code>openclaw</code></h3><p>Root product tag for nearly all entries.</p></div>
  <div class="taxon-card"><h3><code>remote-code-execution</code></h3><p>Execution on the host through agent runtime or control surfaces.</p></div>
  <div class="taxon-card"><h3><code>data-leakage</code></h3><p>Unauthorized disclosure of internal, secret, or regulated information.</p></div>
  <div class="taxon-card"><h3><code>exposure</code></h3><p>Reachable or weakly protected attack surface created by deployment.</p></div>
  <div class="taxon-card"><h3><code>malicious-skills</code></h3><p>Ecosystem abuse through poisoned skills, packages, or extensions.</p></div>
  <div class="taxon-card"><h3><code>supply-chain</code></h3><p>Compromise through dependencies, distribution, or publishing paths.</p></div>
  <div class="taxon-card"><h3><code>auth</code></h3><p>Identity, token, session, or control-plane authorization issues.</p></div>
  <div class="taxon-card"><h3><code>gateway</code></h3><p>Gateway configuration, binding, and channel-facing control logic.</p></div>
  <div class="taxon-card"><h3><code>sandboxing</code></h3><p>Containment and runtime isolation mechanisms.</p></div>
  <div class="taxon-card"><h3><code>scanner</code></h3><p>Continuous or on-demand security analysis tooling.</p></div>
  <div class="taxon-card"><h3><code>advisory-monitoring</code></h3><p>Feeds, signatures, and affected-installation monitoring.</p></div>
  <div class="taxon-card"><h3><code>hardening</code></h3><p>Configuration and operational controls that reduce risk.</p></div>
</div>

## Tag Rules

- Prefer a small controlled vocabulary over ad hoc synonyms.
- Reuse existing tags before creating new ones.
- Use technical mechanism tags and operational impact tags together when both matter.
