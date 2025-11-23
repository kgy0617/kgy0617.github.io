---
layout: post
title:  "News Analysis System"
date:   2025-11-23 22:00:00 +0900
categories: ai data
---

<style>
  .news-dashboard {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 12px;
    color: #333;
  }
  .news-dashboard .header {
    text-align: center;
    color: white;
    margin-bottom: 30px;
  }
  .news-dashboard h1 {
    font-size: 32px;
    margin-bottom: 10px;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    color: white;
  }
  .news-dashboard .subtitle {
    font-size: 16px;
    opacity: 0.9;
    color: rgba(255, 255, 255, 0.9);
  }
  .news-dashboard .selector-container {
    background: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 15px;
  }
  .news-dashboard label {
    font-weight: 600;
    color: #333;
  }
  .news-dashboard select {
    flex: 1;
    max-width: 300px;
    padding: 10px 15px;
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    font-size: 15px;
    cursor: pointer;
    transition: all 0.3s;
  }
  .news-dashboard select:hover {
    border-color: #667eea;
  }
  .news-dashboard select:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
  }
  .news-dashboard .frame-container {
    background: white;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    overflow: hidden;
  }
  .news-dashboard iframe {
    width: 100%;
    height: 80vh;
    border: none;
    display: block;
  }
</style>

<div class="news-dashboard">
  <div class="header">
    <h1>📰 뉴스 분석 시스템</h1>
    <div class="subtitle">Actor · Tone · Economic State 추출 및 시각화</div>
  </div>
  
  <div class="selector-container">
    <label for="articleSelect">📄 기사 선택:</label>
    <select id="articleSelect" onchange="changeArticle()">
      <option value="news_article_1.html">기사 1</option>
      <option value="news_article_2.html">기사 2</option>
    </select>
    <span style="color: #666;">총 2개 기사</span>
  </div>

  <div class="frame-container">
    <iframe id="articleFrame" src="/news-analysis/news_article_1.html"></iframe>
  </div>
</div>

<script>
  function changeArticle() {
    const sel = document.getElementById('articleSelect');
    const frame = document.getElementById('articleFrame');
    frame.style.opacity = '0.5';
    frame.src = '/news-analysis/' + sel.value;
    frame.onload = () => { frame.style.opacity = '1'; };
  }
</script>
