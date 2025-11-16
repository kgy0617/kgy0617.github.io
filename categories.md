---
layout: page
title: Categories
permalink: /categories/
---

<h1>Categories</h1>

<ul>
  {% assign cats = site.categories | sort %}
  {% for category in cats %}
    {% assign cat_name = category[0] %}
    {% assign posts = category[1] %}
    <li>
      <a href="#{{ cat_name | slugify }}">{{ cat_name }}</a> ({{ posts | size }})
    </li>
  {% endfor %}
</ul>

<hr />

{% for category in cats %}
  {% assign cat_name = category[0] %}
  {% assign posts = category[1] %}

  <h2 id="{{ cat_name | slugify }}">{{ cat_name }}</h2>
  <ul>
    {% for post in posts %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <span> — {{ post.date | date: "%Y-%m-%d" }}</span>
      </li>
    {% endfor %}
  </ul>
{% endfor %}
