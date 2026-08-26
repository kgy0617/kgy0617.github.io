# kgy0617.github.io

Personal site and engineering portfolio of **Giyong Kim** — AI engineering, multi-agent
simulation systems for central banking, and empirical econometric research.

**Live:** https://kgy0617.github.io

Built with [Jekyll](https://jekyllrb.com/) 4.3 and the [minima](https://github.com/jekyll/minima)
theme, deployed to GitHub Pages by GitHub Actions.

## Local development

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000, live reload
bundle exec jekyll build   # one-off build into _site/
```

CI builds with the same `Gemfile.lock`, so what you see locally is what ships.

## Layout

| Path | Purpose |
|---|---|
| `_posts/` | Deep-dive project write-ups (`YYYY-MM-DD-slug.markdown`) |
| `_layouts/` | `post`, `category` layout overrides on top of minima |
| `_includes/` | `head.html` (KaTeX + Mermaid), `footer.html`, `comments.html` |
| `assets/main.scss` | Design tokens, dark mode, home hero, shared card styles |
| `portfolio.md` | Project showcase |
| `ai-dev.md` | Architecture and methodology notes |
| `categories.md`, `years.md` | Generated archives |
| `news-analysis/` | Static demo pages embedded by the news-analysis post |

## Authoring notes

**Front matter.** A post needs `layout: post`, `title`, `date` (with `+0900` offset) and
`categories`. Categories become the URL: `categories: ai data` publishes to
`/ai/data/YYYY/MM/DD/slug.html`. Links from `portfolio.md` are hard-coded, so changing a
post's date or categories means updating them there too.

**Diagrams.** Fence a block as ` ```mermaid ` and `_includes/head.html` converts it at load
time. Mermaid runs before KaTeX and diagram bodies are excluded from math rendering.

Quote any edge label containing punctuation — parentheses, colons, commas, quotes:

```
A -->|"정합성 검증 (28개월 시계열)"| B     ✅
A -->|정합성 검증 (28개월 시계열)| B       ❌ Parse error
```

Node labels (`A["..."]`) are already quoted, so only the `|...|` edge labels bite. This
matters because a broken diagram **does not fail the build** — Jekyll ships the page and
mermaid renders an error box in the browser instead, so nobody finds out until someone
opens the post. After editing a diagram, load the page and look at it.

**Math.** Inline math is `$...$`, display math is `$$...$$`. Because `$` is the inline
delimiter, write a literal dollar sign as `\$` — otherwise two currency amounts in one
paragraph get parsed as a formula.

**Liquid.** Raw `{{` or `{%` inside a post must be wrapped in `{% raw %}…{% endraw %}`,
or Jekyll will try to evaluate it and the build fails.

## Deployment

Pushing to `master` triggers `.github/workflows/deploy.yml`: `ruby/setup-ruby` installs the
locked gems, `bundle exec jekyll build` runs with `JEKYLL_ENV=production`, and the result is
published to GitHub Pages. Bumping a gem means committing the updated `Gemfile.lock`.
