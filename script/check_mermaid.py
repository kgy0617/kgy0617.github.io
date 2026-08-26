#!/usr/bin/env python3
"""Parse every mermaid diagram on the site and fail if any of them is broken.

A malformed diagram does not break the Jekyll build: the page ships and mermaid
draws an error box in the reader's browser instead, so nobody finds out until
someone opens the post. This runs the same mermaid build the site loads against
every diagram and exits non-zero if one fails to parse.

Usage:  python3 script/check_mermaid.py [repo_root]
Needs:  a Chrome/Chromium binary (set CHROME_BIN to override discovery).
"""

import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import threading
import sys
import tempfile

CHROME_CANDIDATES = [
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
]

# Files that may contain diagrams. _social/ and vendor/ are build inputs, not content.
CONTENT_GLOBS = ["_posts/*.markdown", "_posts/*.md", "*.md", "*.markdown"]


def find_chrome():
    if os.environ.get("CHROME_BIN"):
        return os.environ["CHROME_BIN"]
    for c in CHROME_CANDIDATES:
        if os.path.sep in c:
            if os.path.exists(c):
                return c
        elif shutil.which(c):
            return shutil.which(c)
    return None


def mermaid_src_url(root):
    """Read the mermaid <script src> the site actually loads, so the check can
    never drift from production."""
    head = (root / "_includes" / "head.html").read_text(encoding="utf-8")
    m = re.search(r'src="(https://[^"]*mermaid[^"]*\.js)"', head)
    if not m:
        sys.exit("could not find the mermaid script tag in _includes/head.html")
    return m.group(1)


def collect_blocks(root):
    blocks, seen = [], set()
    for pattern in CONTENT_GLOBS:
        for path in sorted(root.glob(pattern)):
            if path in seen:
                continue
            seen.add(path)
            lines = path.read_text(encoding="utf-8").split("\n")
            i = 0
            while i < len(lines):
                if lines[i].strip() == "```mermaid":
                    j = i + 1
                    while j < len(lines) and lines[j].strip() != "```":
                        j += 1
                    blocks.append({
                        "file": str(path.relative_to(root)),
                        "line": i + 1,
                        "src": "\n".join(lines[i + 1:j]),
                    })
                    i = j
                i += 1
    return blocks


PAGE = """<!doctype html><html><head><meta charset="utf-8">
<script src="__MERMAID__"></script></head>
<body><pre id="out">pending</pre><script>
var BLOCKS = __JSON__;
window.addEventListener('load', function () {
  var lines = [];
  try { mermaid.initialize({ startOnLoad: false, theme: 'neutral' }); }
  catch (e) { document.getElementById('out').textContent = 'LOAD_ERROR ' + e; return; }
  var chain = Promise.resolve();
  BLOCKS.forEach(function (b) {
    chain = chain.then(function () {
      return Promise.resolve(mermaid.parse(b.src))
        .then(function () { lines.push('PASS\\t' + b.file + ':' + b.line); })
        .catch(function (e) {
          lines.push('FAIL\\t' + b.file + ':' + b.line + '\\t' +
            String((e && e.message) || e).replace(/\\s+/g, ' ').slice(0, 300));
        });
    });
  });
  chain.then(function () { document.getElementById('out').textContent = lines.join('\\n'); });
});
</script></body></html>"""


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    blocks = collect_blocks(root)
    if not blocks:
        print("no mermaid diagrams found")
        return 0

    chrome = find_chrome()
    if not chrome:
        sys.exit("no Chrome/Chromium found; set CHROME_BIN to its path")

    page = (PAGE
            .replace("__MERMAID__", mermaid_src_url(root))
            .replace("__JSON__", json.dumps(blocks, ensure_ascii=False)))

    tmp = tempfile.mkdtemp(prefix="mermaid-check-")
    try:
        page_path = pathlib.Path(tmp) / "check.html"
        page_path.write_text(page, encoding="utf-8")
        cmd = [
            chrome, "--headless", "--disable-gpu", "--no-sandbox",
            "--no-first-run", "--no-default-browser-check",
            "--disable-background-networking", "--disable-extensions",
            "--user-data-dir=" + str(pathlib.Path(tmp) / "profile"),
            "--virtual-time-budget=30000", "--dump-dom", page_path.as_uri(),
        ]
        # Chrome writes the DOM and then declines to exit, so read until the
        # document is complete and kill it instead of waiting on the process.
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.DEVNULL, text=True)
        chunks = []

        def drain():
            for line in proc.stdout:
                chunks.append(line)
                if "</html>" in line:
                    break

        reader = threading.Thread(target=drain, daemon=True)
        reader.start()
        reader.join(timeout=90)
        proc.kill()
        # Wait for it to actually die. A killed-but-still-exiting Chrome keeps
        # writing into its profile, which makes removing the temp dir fail.
        try:
            proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            pass
        dom = "".join(chunks)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    m = re.search(r'<pre id="out">(.*?)</pre>', dom, re.S)
    result = html.unescape(m.group(1)).strip() if m else ""

    if not result or result == "pending":
        sys.exit("mermaid never reported a result — could not load " + mermaid_src_url(root))
    if result.startswith("LOAD_ERROR"):
        sys.exit(result)

    failures = 0
    for line in result.split("\n"):
        parts = line.split("\t")
        if parts[0] == "PASS":
            print(f"  ok    {parts[1]}")
        else:
            failures += 1
            print(f"  FAIL  {parts[1]}\n        {parts[2] if len(parts) > 2 else ''}")

    total = len(blocks)
    if failures:
        print(f"\n{failures} of {total} mermaid diagrams failed to parse.")
        print("Edge labels containing punctuation must be quoted: A -->|\"a (b)\"| B")
        return 1
    print(f"\nall {total} mermaid diagrams parse")
    return 0


if __name__ == "__main__":
    sys.exit(main())
