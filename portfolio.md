---
layout: page
title: "Portfolio"
permalink: /portfolio/
---

<style>
  .portfolio-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: var(--text);
    line-height: 1.6;
  }
  
  .portfolio-hero {
    background: linear-gradient(135deg, var(--hero-from) 0%, var(--hero-to) 100%);
    color: white;
    padding: 2.2rem 1.8rem;
    border-radius: 12px;
    margin-bottom: 2.5rem;
    box-shadow: var(--shadow-md);
  }
  
  .portfolio-hero h1 {
    font-size: 1.85rem;
    font-weight: 800;
    margin: 0 0 0.6rem 0;
    color: var(--hero-text);
    letter-spacing: -0.02em;
  }
  
  .portfolio-hero p {
    font-size: 1.05rem;
    color: var(--hero-muted);
    margin: 0;
    line-height: 1.5;
  }
  
  .stats-row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 1rem;
    margin-top: 1.5rem;
    padding-top: 1.2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
  }
  
  .stat-box {
    text-align: center;
  }
  
  .stat-number {
    font-size: 1.4rem;
    font-weight: 700;
    color: var(--accent-soft);
    display: block;
  }
  
  .stat-label {
    font-size: 0.8rem;
    color: var(--hero-muted);
    text-transform: uppercase;
    letter-spacing: 0.05em;
  }

  .section-heading {
    font-size: 1.4rem;
    font-weight: 700;
    margin: 2.8rem 0 1.2rem 0;
    padding-bottom: 0.6rem;
    border-bottom: 2px solid var(--border);
    color: var(--text-strong);
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .project-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.25s ease;
    box-shadow: var(--shadow-sm);
    position: relative;
    overflow: hidden;
  }

  .project-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
    border-color: var(--border-strong);
  }

  .project-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 4px;
    height: 100%;
    background: var(--accent);
  }

  .project-card.purple::before { background: #8b5cf6; }
  .project-card.emerald::before { background: #10b981; }
  .project-card.amber::before { background: #f59e0b; }
  .project-card.rose::before { background: #f43f5e; }

  .project-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.6rem;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .project-title {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-strong);
    margin: 0;
  }

  .project-badge {
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.2rem 0.6rem;
    border-radius: 9999px;
    background: var(--surface-sunken);
    color: var(--text-muted);
    border: 1px solid var(--border);
  }

  .project-desc {
    color: var(--text);
    font-size: 0.95rem;
    margin-bottom: 1rem;
    line-height: 1.6;
  }

  .feature-list {
    margin: 0 0 1rem 0;
    padding-left: 1.2rem;
    font-size: 0.9rem;
    color: var(--text);
  }

  .feature-list li {
    margin-bottom: 0.35rem;
  }

  .tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.4rem;
    margin-top: 0.8rem;
  }

  .tech-tag {
    font-size: 0.75rem;
    font-weight: 500;
    padding: 0.2rem 0.55rem;
    background: var(--surface-subtle);
    border: 1px solid var(--border);
    border-radius: 6px;
    color: var(--text);
  }

  .project-links {
    margin-top: 1rem;
    display: flex;
    gap: 0.8rem;
    font-size: 0.85rem;
  }

  .project-link {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-weight: 600;
    color: var(--link);
    text-decoration: none;
  }

  .project-link:hover {
    text-decoration: underline;
  }

  .skills-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1.2rem;
    margin-top: 1.2rem;
  }

  .skill-block {
    background: var(--surface-subtle);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1.2rem;
  }

  .skill-block-title {
    font-weight: 700;
    font-size: 1rem;
    color: var(--text-strong);
    margin-bottom: 0.5rem;
    display: block;
  }

  .skill-block-desc {
    font-size: 0.85rem;
    color: var(--text-muted);
    line-height: 1.5;
  }
</style>

<div class="portfolio-wrapper">

  <!-- Hero Header -->
  <div class="portfolio-hero">
    <h1>Giyong Kim — AI & Data Engineering Portfolio</h1>
    <p>Designing intelligent multi-agent systems, central bank statistical platforms, and empirical econometric models.</p>
    
    <div class="stats-row">
      <div class="stat-box">
        <span class="stat-number">5+</span>
        <span class="stat-label">Core Systems</span>
      </div>
      <div class="stat-box">
        <span class="stat-number">2,500+</span>
        <span class="stat-label">Agent Personas</span>
      </div>
      <div class="stat-box">
        <span class="stat-number">0.808</span>
        <span class="stat-label">Peak F1 Score</span>
      </div>
      <div class="stat-box">
        <span class="stat-number">ACL 2026</span>
        <span class="stat-label">Peer-Reviewed</span>
      </div>
    </div>
  </div>

  <!-- SECTION 1: LLM & Multi-Agent Systems -->
  <div class="section-heading">
    <span>🤖</span> 1. LLM & Multi-Agent Intelligence Systems
  </div>

  <div class="project-grid">

    <!-- Project 1: EPU -->
    <div class="project-card">
      <div class="project-header">
        <h3 class="project-title">EPU — Hierarchical 2-Stage Multi-Agent Classification Pipeline</h3>
        <span class="project-badge">Lead Architect / Research</span>
      </div>
      <p class="project-desc">
        A production-grade multi-agent pipeline designed to classify Korean financial and economic news articles into 5 dimensions of Economic Policy Uncertainty (Macro, Market, Policy, Corporate, Geo) with UP/NA decision criteria.
      </p>
      <ul class="feature-list">
        <li><strong>Stage 1 Gate Routing</strong>: High-recall filtering (Recall 0.893~0.933) using Gemma-4-26b with k=8 and False Negative Shield v2.</li>
        <li><strong>Stage 2 Expert Agents</strong>: 5 specialized agents leveraging Qwen-3.6-27b with dynamic few-shot retrieval (kNN + BM25 Reciprocal Rank Fusion).</li>
        <li><strong>Heuristic Optimization</strong>: Tailored decision pipelines per dimension (Market consecutive pattern gate, Corporate NA-first inversion, Geo paragraph-level code re-voting).</li>
      </ul>
      <div class="tech-tags">
        <span class="tech-tag">Multi-Agent</span>
        <span class="tech-tag">Gemma-4</span>
        <span class="tech-tag">Qwen-3.6</span>
        <span class="tech-tag">kNN + BM25 RRF</span>
        <span class="tech-tag">Few-Shot Mining</span>
      </div>
      <div class="project-links">
        <a class="project-link" href="/ai/data/2026/08/15/epu-multi-agent-classification-pipeline.html">Read Deep-Dive Article →</a>
      </div>
    </div>

    <!-- Project 2: Agent CSI -->
    <div class="project-card purple">
      <div class="project-header">
        <h3 class="project-title">Agent CSI — LLM-Powered Consumer Sentiment Simulation</h3>
        <span class="project-badge">Core Researcher & Engineer</span>
      </div>
      <p class="project-desc">
        Simulating the Bank of Korea's official Consumer Survey Index (CSI) across 24 survey items using an agentic population of 2,500 stratified households, benchmarked against 28 months of empirical central bank releases.
      </p>
      <ul class="feature-list">
        <li><strong>Stratified Agent Population</strong>: Sampled 2,500 Korean household personas from NVIDIA's Nemotron-Personas-Korea dataset (1M+ profiles) mirroring national demographic distributions.</li>
        <li><strong>4-Stage Information Injection</strong>: Demographics → 11-attribute Personas → Self-referential past month memory → LLM daily economic news & quantitative indicator summaries (CPI, interest rates, NSI).</li>
        <li><strong>Causal Graph Architecture</strong>: Implemented causal pathways (Shock → Mediator → Survey Question) with Shock z-scores to model macroeconomic stress transmission.</li>
      </ul>
      <div class="tech-tags">
        <span class="tech-tag">LLM Simulation</span>
        <span class="tech-tag">Nemotron-Personas</span>
        <span class="tech-tag">Causal Inference</span>
        <span class="tech-tag">Time-Series Alignment</span>
        <span class="tech-tag">Central Banking</span>
      </div>
      <div class="project-links">
        <a class="project-link" href="/ai/economics/2026/08/08/agent-csi-llm-consumer-sentiment-simulation.html">Read Deep-Dive Article →</a>
      </div>
    </div>

    <!-- Project 3: FOMC Agent Council -->
    <div class="project-card amber">
      <div class="project-header">
        <h3 class="project-title">FOMC Agent Council — Multi-Agent Monetary Policy Deliberation</h3>
        <span class="project-badge">Lead Developer</span>
      </div>
      <p class="project-desc">
        A deliberative multi-agent framework modeling the US Federal Open Market Committee (FOMC) interest rate decisions through simulated interactions between Hawkish, Dovish, and Centrist Chair personas — and a peer-reviewed diagnosis of where that framework fails.
      </p>
      <ul class="feature-list">
        <li><strong>Council Protocol</strong>: Simulates structured debate rounds between economic perspectives, grounded in qualitative Beige Book summaries and quantitative macroeconomic indicators.</li>
        <li><strong>RAG Integration</strong>: Precedent retrieval engine indexing historical FOMC minutes, transcripts, and policy statements.</li>
        <li><strong>Systematic Experimentation (E1~E6 × M1~M5)</strong>: Evaluated decision accuracy across snapshot vs. 3M/6M trend horizons on strictly time-consistent vintage data, against empirical FOMC rate actions and Taylor Rule benchmarks.</li>
        <li><strong>Published Finding — "Hold Bias"</strong>: LLM committees systematically over-predict Hold and resist Cut even during easing cycles. Debate and consensus aggregation <em>amplify</em> this caution rather than correcting it, which is costly precisely at policy turning points.</li>
      </ul>
      <div class="tech-tags">
        <span class="tech-tag">Multi-Agent Debate</span>
        <span class="tech-tag">FOMC</span>
        <span class="tech-tag">RAG</span>
        <span class="tech-tag">Monetary Policy</span>
        <span class="tech-tag">Taylor Rule</span>
      </div>
      <div class="project-links">
        <a class="project-link" href="/ai/economics/2026/02/20/fomc-agent-council-monetary-policy-simulation.html">Read Deep-Dive Article →</a>
        <a class="project-link" href="https://aclanthology.org/2026.trustnlp-main.52/" target="_blank" rel="noopener">Paper (TrustNLP 2026) →</a>
      </div>
    </div>

    <!-- Project 4: News Analysis System -->
    <div class="project-card rose">
      <div class="project-header">
        <h3 class="project-title">Central Bank News Analysis System</h3>
        <span class="project-badge">Lead Engineer</span>
      </div>
      <p class="project-desc">
        End-to-end distributed NLP and multi-agent pipeline for clustering, sentiment scoring, and macro signal extraction from thousands of financial news articles per day.
      </p>
      <div class="tech-tags">
        <span class="tech-tag">PySpark</span>
        <span class="tech-tag">LangGraph</span>
        <span class="tech-tag">GPT-4o</span>
        <span class="tech-tag">Macro Signals</span>
      </div>
      <div class="project-links">
        <a class="project-link" href="/ai/data/2025/11/23/news-analysis-system.html">View Interactive Demo & Post →</a>
      </div>
    </div>

  </div>

  <!-- SECTION 2: Central Banking & Economic Systems -->
  <div class="section-heading">
    <span>🏛️</span> 2. Central Banking & Statistical Software Modernization
  </div>

  <div class="project-grid">

    <!-- Project 5: BOK-X-13 Web -->
    <div class="project-card emerald">
      <div class="project-header">
        <h3 class="project-title">BOK-X-13 Web — Seasonal Adjustment Web Platform</h3>
        <span class="project-badge">Full-Stack Modernization</span>
      </div>
      <p class="project-desc">
        Modernized the Bank of Korea's legacy desktop seasonal adjustment software (`BOK-X-13ARIMA-SEATS` in Java/JavaFX) into a responsive, containerized Python Flask web application.
      </p>
      <ul class="feature-list">
        <li><strong>Engine Decoupling</strong>: Ported core modules into Python (`spec_generator`, `ghl_generator` for Korean holiday regressors, `x13_executor` with US Census Bureau binary invocation).</li>
        <li><strong>Interactive Visualization</strong>: Integrated Chart.js for real-time visualization of original series, seasonally adjusted series, trend-cycle, and irregular components.</li>
        <li><strong>Automated Diagnostic Parser</strong>: Real-time parsing of X-13 diagnostic outputs (M-statistics, Q-statistics, sliding spans).</li>
      </ul>
      <div class="tech-tags">
        <span class="tech-tag">Python Flask</span>
        <span class="tech-tag">X-13ARIMA-SEATS</span>
        <span class="tech-tag">Time Series</span>
        <span class="tech-tag">Chart.js</span>
        <span class="tech-tag">System Migration</span>
      </div>
      <div class="project-links">
        <a class="project-link" href="/economics/software/2026/04/05/bok-x13-seasonal-adjustment-web-app.html">Read Deep-Dive Article →</a>
      </div>
    </div>

    <!-- Project 6: ECOS Modernization -->
    <div class="project-card">
      <div class="project-header">
        <h3 class="project-title">Economic Statistics System (ECOS) Modernization</h3>
        <span class="project-badge">Systems Engineer</span>
      </div>
      <p class="project-desc">
        Modernized statistical pipeline architectures, migrating legacy STATA/SAS batch programs to Python, Oracle, and Kubernetes environments with natural-language querying capabilities.
      </p>
      <div class="tech-tags">
        <span class="tech-tag">Python</span>
        <span class="tech-tag">Java</span>
        <span class="tech-tag">Oracle SQL</span>
        <span class="tech-tag">Kubernetes</span>
        <span class="tech-tag">FastAPI</span>
      </div>
    </div>

  </div>

  <!-- SECTION 3: Research & Applied Econometrics -->
  <div class="section-heading">
    <span>📈</span> 3. Research & Applied Econometrics
  </div>

  <div class="project-grid">

    <!-- Project 7: Data Production Value & Occupational Intensity -->
    <div class="project-card purple">
      <div class="project-header">
        <h3 class="project-title">Measuring Korea’s Data Production Value and Occupational Data Intensity</h3>
        <span class="project-badge">Working Paper / Empirical Research</span>
      </div>
      <p class="project-desc">
        A large-scale empirical study quantifying data asset production and the transition of the Korean labor force towards data-intensive roles using NLP text-mining over job vacancy postings under the OECD framework.
      </p>
      <ul class="feature-list">
        <li><strong>Tri-Pillar Classification</strong>: Structured occupational data activities into Data Entry, Database Architecture, and Data Analytics.</li>
        <li><strong>NLP Dispersion Metrics</strong>: Evaluated semantic similarity and density using Korean morphological analyzers (Kiwi, Konlpy) and dense vector embeddings (spaCy).</li>
        <li><strong>Macroeconomic Estimation</strong>: Derived national-level data asset values and structural labor shift indices.</li>
      </ul>
      <div class="tech-tags">
        <span class="tech-tag">Empirical Econometrics</span>
        <span class="tech-tag">NLP / Text Mining</span>
        <span class="tech-tag">OECD Framework</span>
        <span class="tech-tag">Kiwi / spaCy</span>
        <span class="tech-tag">Labor Economics</span>
      </div>
      <div class="project-links">
        <a class="project-link" href="/economics/data/2026/01/20/measuring-korea-data-production-value-occupational-intensity.html">Read Deep-Dive Article →</a>
        <a class="project-link" href="https://cifer2026.mhirano.jp/accepted_papers" target="_blank" rel="noopener">Paper (IEEE CIFEr 2026) →</a>
      </div>
    </div>

  </div>

  <!-- SECTION 4: Publications -->
  <div class="section-heading">
    <span>📚</span> 4. Publications
  </div>

  <div class="pub-list">
    <div class="pub-entry">
      <h3 class="pub-title">The Conservative AI: Diagnosing Hold Bias and Reliability Limits in Persona-Based Monetary Policy Simulation</h3>
      <p class="pub-authors"><strong>Giyong Kim</strong>, Sojung Kim</p>
      <p class="pub-venue">
        Proceedings of the 6th Workshop on Trustworthy NLP (TrustNLP 2026),
        Association for Computational Linguistics · San Diego, California · July 2026 · pp. 663–677
      </p>
      <p class="pub-abstract">
        Evaluates whether LLMs can reliably simulate historical FOMC decisions under strictly
        time-consistent vintage information. Identifies <em>Hold bias</em> — a systematic reluctance to
        predict Cut even during easing cycles — and shows that debate and consensus-style agentic
        workflows amplify rather than mitigate it, concluding that plausible deliberation alone is not
        sufficient for trustworthy decision support.
      </p>
      <div class="project-links">
        <a class="project-link" href="https://aclanthology.org/2026.trustnlp-main.52/" target="_blank" rel="noopener">ACL Anthology →</a>
        <a class="project-link" href="https://aclanthology.org/2026.trustnlp-main.52.pdf" target="_blank" rel="noopener">PDF →</a>
        <a class="project-link" href="https://doi.org/10.18653/v1/2026.trustnlp-main.52" target="_blank" rel="noopener">DOI →</a>
      </div>
    </div>

    <div class="pub-entry">
      <h3 class="pub-title">Anchor-and-Verify LLM Cascades for Economic Measurement of Data-Intensive Work from Online Job Postings</h3>
      <p class="pub-authors"><strong>Giyong Kim</strong>, Sojung Kim</p>
      <p class="pub-venue">
        IEEE Computational Intelligence in Financial Engineering and Economics (CIFEr 2026)
        · Tokyo, Japan · September 2026
        <span class="pub-status">Accepted — to be presented</span>
      </p>
      <p class="pub-abstract">
        Applies an anchor-and-verify LLM cascade to measuring data-intensive work from
        large-scale online job postings, extending the occupational data-intensity
        estimation described in the article below.
      </p>
      <div class="project-links">
        <a class="project-link" href="https://cifer2026.mhirano.jp/accepted_papers" target="_blank" rel="noopener">Accepted papers →</a>
        <a class="project-link" href="/economics/data/2026/01/20/measuring-korea-data-production-value-occupational-intensity.html">Related article →</a>
      </div>
    </div>
  </div>

  <!-- SECTION 5: Skills Matrix -->
  <div class="section-heading">
    <span>⚡</span> 5. Technical Competencies
  </div>

  <div class="skills-container">
    <div class="skill-block">
      <span class="skill-block-title">AI &amp; Multi-Agent</span>
      <span class="skill-block-desc">Gemma-4 (26B), Qwen-3.6 (27B/35B), GPT-4o, Claude, Nemotron-Personas · LangGraph, custom hierarchical routers, multi-agent council protocols, prompt engineering</span>
    </div>
    <div class="skill-block">
      <span class="skill-block-title">Retrieval &amp; RAG</span>
      <span class="skill-block-desc">kNN dense vector embeddings, BM25 lexical search, Reciprocal Rank Fusion (RRF), FAISS, dynamic few-shot mining</span>
    </div>
    <div class="skill-block">
      <span class="skill-block-title">Languages &amp; Backends</span>
      <span class="skill-block-desc">Python (Flask, FastAPI, PyTorch), Java, SQL</span>
    </div>
    <div class="skill-block">
      <span class="skill-block-title">Data &amp; Infrastructure</span>
      <span class="skill-block-desc">PySpark, Celery, Oracle, PostgreSQL, Docker, Kubernetes, Git / GitHub Actions, legacy system modernization</span>
    </div>
    <div class="skill-block">
      <span class="skill-block-title">Econometrics &amp; Evaluation</span>
      <span class="skill-block-desc">X-13ARIMA-SEATS, seasonal adjustment, causal inference, survey simulation, Stata, R, Kiwi, spaCy · Macro/Micro F1, Pearson correlation, MAE, bias decomposition</span>
    </div>
  </div>

</div>


