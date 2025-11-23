---
layout: page
title: "Portfolio"
permalink: /portfolio/
---

<style>
  .portfolio-container {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
  }
  
  .section-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-top: 3rem;
    margin-bottom: 1.5rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #f0f0f0;
    color: #111;
    letter-spacing: -0.02em;
  }

  .portfolio-item {
    margin-bottom: 2.5rem;
    padding-left: 1rem;
    border-left: 3px solid transparent;
    transition: border-color 0.3s ease;
  }

  .portfolio-item:hover {
    border-left-color: #667eea;
  }

  .item-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 0.5rem;
    flex-wrap: wrap;
  }

  .item-title {
    font-size: 1.2rem;
    font-weight: 600;
    color: #2c3e50;
    margin: 0;
  }

  .item-role {
    font-size: 0.9rem;
    color: #7f8c8d;
    font-weight: 500;
  }

  .item-desc {
    margin-bottom: 0.8rem;
    line-height: 1.6;
    color: #555;
  }

  .tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .tag {
    background-color: #f8f9fa;
    color: #666;
    padding: 0.2rem 0.6rem;
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: 500;
    border: 1px solid #e9ecef;
  }
  
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 1rem;
  }
  
  .skill-card {
    background: #fff;
    border: 1px solid #eee;
    padding: 1rem;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.02);
  }
  
  .skill-title {
    font-weight: 600;
    margin-bottom: 0.5rem;
    display: block;
    color: #333;
  }
</style>

<div class="portfolio-container">

  <div class="section-title">1. AI & Data Systems for Central Banking</div>

  <div class="portfolio-item">
    <div class="item-header">
      <h3 class="item-title">News Analysis System</h3>
      <span class="item-role">Lead Engineer</span>
    </div>
    <p class="item-desc">Multi-agent LLM pipeline for news clustering, sentiment analysis, and macro signal extraction. Designed and deployed the end-to-end modeling pipeline.</p>
    <div class="tags">
      <span class="tag">Python</span>
      <span class="tag">Spark</span>
      <span class="tag">LangGraph</span>
      <span class="tag">GPT-4o</span>
    </div>
  </div>

  <div class="portfolio-item">
    <div class="item-header">
      <h3 class="item-title">Economic Statistics System (ECOS) Project</h3>
      <span class="item-role">Engineer</span>
    </div>
    <p class="item-desc">GPT + vector search based statistics query system with a Chrome Extension prototype for seamless data access.</p>
    <div class="tags">
      <span class="tag">FastAPI</span>
      <span class="tag">FAISS</span>
      <span class="tag">Google Cloud Run</span>
      <span class="tag">Chrome Extension</span>
    </div>
  </div>

  <div class="section-title">2. Research & Publications</div>

  <div class="portfolio-item">
    <div class="item-header">
      <h3 class="item-title">Measuring Korea’s Data Production Value and Data-Intensity in Occupations</h3>
      <span class="item-role">Working Paper</span>
    </div>
    <p class="item-desc">Research analyzing job postings to measure data-intensiveness using OECD framework.</p>
    <div class="tags">
      <span class="tag">NLP</span>
      <span class="tag">Job Postings Analysis</span>
      <span class="tag">Econometrics</span>
    </div>
  </div>

  <div class="section-title">3. Talks & Workshops</div>

  <div class="portfolio-item">
    <div class="item-header">
      <h3 class="item-title">VIS 2025 / GenAI-VIS</h3>
    </div>
    <p class="item-desc">Activities related to GenAI-VIS and participation in industrial session discussions.</p>
  </div>

  <div class="section-title">4. Skills</div>

  <div class="skills-grid">
    <div class="skill-card">
      <span class="skill-title">Machine Learning / LLMs</span>
      <span style="font-size: 0.9rem; color: #666;">RAG, Agentic Workflows, NLP</span>
    </div>
    <div class="skill-card">
      <span class="skill-title">Data Engineering</span>
      <span style="font-size: 0.9rem; color: #666;">Spark, Pipelines, Cloud Infrastructure</span>
    </div>
    <div class="skill-card">
      <span class="skill-title">Econometrics</span>
      <span style="font-size: 0.9rem; color: #666;">Causal Inference, Time Series</span>
    </div>
  </div>

</div>
