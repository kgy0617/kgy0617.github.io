---
layout: page
title: Archive
permalink: /archive/
---

{%- assign years = site.posts | group_by_exp: "post", "post.date | date: '%Y'" -%}
{%- assign cats = site.categories | sort -%}

<p class="archive-intro">
  {{ site.posts | size }} posts, newest first. Use the filters to narrow by topic.
</p>

<div class="archive-filters" role="group" aria-label="Filter posts by category">
  <button type="button" class="archive-filter is-active" data-filter="all">
    All <span class="archive-filter-count">{{ site.posts | size }}</span>
  </button>
  {%- for category in cats -%}
  <button type="button" class="archive-filter" data-filter="{{ category[0] | downcase }}" data-cat="{{ category[0] | downcase }}">
    {{ category[0] }} <span class="archive-filter-count">{{ category[1] | size }}</span>
  </button>
  {%- endfor -%}
</div>

<div class="archive-list">
  {%- for year in years -%}
  <section class="archive-year" data-year="{{ year.name }}">
    <h2 class="archive-year-heading" id="year-{{ year.name }}">
      {{ year.name }}<span class="archive-year-count">{{ year.items | size }}</span>
    </h2>
    <ul class="archive-items">
      {%- for post in year.items -%}
      <li class="archive-item" data-cats="{{ post.categories | join: ' ' | downcase }}">
        <time class="archive-date" datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%b %-d" }}</time>
        <a class="archive-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
        {% include category-badges.html categories=post.categories %}
      </li>
      {%- endfor -%}
    </ul>
  </section>
  {%- endfor -%}
</div>

<p class="archive-empty" hidden>No posts in this category yet.</p>

<script>
  (function () {
    var filters = Array.prototype.slice.call(document.querySelectorAll('.archive-filter'));
    var items   = Array.prototype.slice.call(document.querySelectorAll('.archive-item'));
    var years   = Array.prototype.slice.call(document.querySelectorAll('.archive-year'));
    var empty   = document.querySelector('.archive-empty');
    if (!filters.length) return;

    var known = filters.map(function (b) { return b.dataset.filter; });

    function apply(cat) {
      if (known.indexOf(cat) === -1) cat = 'all';
      var shown = 0;

      items.forEach(function (li) {
        var cats = (li.dataset.cats || '').split(' ');
        var match = cat === 'all' || cats.indexOf(cat) !== -1;
        li.hidden = !match;
        if (match) shown++;
      });

      // Collapse year headings that no longer hold anything, and keep their counts honest.
      years.forEach(function (section) {
        var visible = section.querySelectorAll('.archive-item:not([hidden])').length;
        section.hidden = visible === 0;
        var count = section.querySelector('.archive-year-count');
        if (count) count.textContent = visible;
      });

      filters.forEach(function (b) {
        var on = b.dataset.filter === cat;
        b.classList.toggle('is-active', on);
        b.setAttribute('aria-pressed', on ? 'true' : 'false');
      });

      if (empty) empty.hidden = shown !== 0;
    }

    filters.forEach(function (b) {
      b.addEventListener('click', function () {
        var cat = b.dataset.filter;
        history.replaceState(null, '', cat === 'all' ? location.pathname : '#' + cat);
        apply(cat);
      });
    });

    // Category chips elsewhere on the site link here as /archive/#ai etc.
    window.addEventListener('hashchange', function () {
      apply(location.hash.replace('#', '').toLowerCase());
    });
    apply(location.hash.replace('#', '').toLowerCase());
  })();
</script>
