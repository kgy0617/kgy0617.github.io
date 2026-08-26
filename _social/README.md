# Social image sources

Jekyll ignores `_`-prefixed directories, so nothing here is published — only the
rendered PNGs in `assets/` are.

| Source | Output | Used for |
|---|---|---|
| `og-card.html` | `assets/images/og-card.png` (1200×630) | `og:image` / `twitter:image` |
| `../assets/favicon.svg` | `assets/favicon-32.png`, `assets/favicon-16.png` | browser tab icon |
| `apple-icon.svg` | `assets/apple-touch-icon.png` (180×180) | iOS home screen |

`apple-icon.svg` is `favicon.svg` with the rounded corners removed and the accent
bar widened: iOS applies its own mask and renders any transparency as black, so
that icon must be an opaque full-bleed square.

## Regenerating

Rendered with headless Chrome, which resolves the same system font stack the site
uses. Chrome may not exit on its own — wrap it in `timeout`.

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# OG card
timeout 45 "$CHROME" --headless --disable-gpu --hide-scrollbars \
  --window-size=1200,630 \
  --screenshot=assets/images/og-card.png \
  _social/og-card.html
```

Icons are rendered by inlining the SVG into a page sized to the target pixel
dimensions; referencing the SVG by relative path silently produces a broken-image
placeholder instead.

Colours track the hero tokens in `assets/main.scss` (`--hero-from`, `--hero-to`,
`--accent-soft`). If those change, regenerate these.
