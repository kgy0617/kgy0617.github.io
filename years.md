---
layout: page
title: Year
permalink: /years/
---

<h1>Year</h1>

{%- comment -%}
연도별 글 개수 요약 (상단 테이블)
{%- endcomment -%}

<table>
  <tr>
    {% assign year_list = "" | split: "" %}
    {% for post in site.posts %}
  {% assign y = post.date | date: '%Y' %}
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
        {% assign post_year = post.date | date: '%Y' %}
        {% if post_year == y %}
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
        {% assign post_year = post.date | date: '%Y' %}
        {% if post_year == y %}
        <li>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          <span> — {{ post.date | date: '%Y-%m-%d' }}</span>
        </li>
        {% endif %}
    {% endfor %}
  </ul>
{% endfor %}
