---
layout: page
title: 연도
permalink: /years/
---

<h1>연도</h1>

{%- comment -%}
연도별 글 개수 요약 (상단 테이블)
{%- endcomment -%}

<table>
  <tr>
    {% assign years = site.posts | map: "date" | uniq | sort: "date" %}
    {% assign year_list = "" | split: "" %}
    {% for post in site.posts %}
      {% assign y = post.date | date: "%Y" %}
      {% unless year_list contains y %}
        {% assign year_list = year_list | push: y %}
      {% endunless %}
    {% endfor %}
    {% assign year_list = year_list | sort | reverse %}
    {% for y in year_list %}
      <th>{{ y }}</th>
    {% endfor %}
  </tr>
  <tr>
    {% for y in year_list %}
      {% assign count = 0 %}
      {% for post in site.posts %}
        {% if post.date | date: "%Y" == y %}
          {% assign count = count | plus: 1 %}
        {% endif %}
      {% endfor %}
      <td>{{ count }}</td>
    {% endfor %}
  </tr>
</table>

<hr />

{%- comment -%}
연도별 포스트 리스트
{%- endcomment -%}

{% for y in year_list %}
  <h2 id="year-{{ y }}">{{ y }}</h2>
  <ul>
    {% for post in site.posts %}
      {% if post.date | date: "%Y" == y %}
        <li>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          <span> — {{ post.date | date: "%Y-%m-%d" }}</span>
        </li>
      {% endif %}
    {% endfor %}
  </ul>
{% endfor %}
