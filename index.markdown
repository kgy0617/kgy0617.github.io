---
layout: home
---

<div class="home-hero">
  <p class="home-eyebrow">Data &amp; AI Engineer · Empirical Researcher</p>
  <h1 class="home-title">Giyong Kim</h1>
  <p class="home-lede">
    I build <strong>multi-agent LLM systems for central banking</strong> — simulating monetary policy
    deliberation, consumer sentiment surveys, and economic policy uncertainty — and modernize the
    statistical software that national institutions run on.
  </p>

  <div class="home-cta">
    <a class="home-btn home-btn-primary" href="{{ '/portfolio/' | relative_url }}">Portfolio</a>
    <a class="home-btn" href="{{ '/ai-dev/' | relative_url }}">AI Architecture</a>
    <a class="home-btn" href="{{ '/about/' | relative_url }}">About</a>
    {%- if site.linkedin_username -%}
    <a class="home-btn" href="https://www.linkedin.com/in/{{ site.linkedin_username }}" target="_blank" rel="noopener">LinkedIn</a>
    {%- endif -%}
  </div>
</div>

<div class="home-highlights">
  <a class="home-highlight" href="{{ '/ai/data/2026/08/15/epu-multi-agent-classification-pipeline.html' | relative_url }}">
    <span class="home-highlight-kicker">Multi-Agent Classification</span>
    <span class="home-highlight-title">EPU Pipeline</span>
    <span class="home-highlight-desc">2-stage Gate + 5 Expert agents over Korean economic news. Recall 0.893–0.933 at the gate, expert F1 0.767–0.808.</span>
  </a>
  <a class="home-highlight" href="{{ '/ai/economics/2026/08/08/agent-csi-llm-consumer-sentiment-simulation.html' | relative_url }}">
    <span class="home-highlight-kicker">LLM Social Simulation</span>
    <span class="home-highlight-title">Agent CSI</span>
    <span class="home-highlight-desc">2,500 stratified household agents reproducing the Bank of Korea Consumer Sentiment Index across 24 survey items.</span>
  </a>
  <a class="home-highlight" href="{{ '/economics/software/2026/04/05/bok-x13-seasonal-adjustment-web-app.html' | relative_url }}">
    <span class="home-highlight-kicker">Legacy Modernization</span>
    <span class="home-highlight-title">BOK-X-13 Web</span>
    <span class="home-highlight-desc">Java/JavaFX desktop seasonal adjustment software re-architected into a containerized Python Flask platform.</span>
  </a>
</div>
