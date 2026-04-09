#!/usr/bin/env python3
"""Generate a standalone zoomable HTML preview for Mermaid diagrams."""

from __future__ import annotations

import argparse
import html
from pathlib import Path


DEFAULT_TITLE = "Mermaid Diagram Preview"


def build_html(diagram: str, title: str) -> str:
    safe_title = html.escape(title or DEFAULT_TITLE)
    safe_diagram = html.escape(diagram.strip())
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{safe_title}</title>
  <style>
    :root {{
      color-scheme: light;
      --bg: #f8fafc;
      --panel: #ffffff;
      --ink: #182030;
      --muted: #64748b;
      --line: #c7d2e3;
      --accent: #2563eb;
      --accent-soft: #dbeafe;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      min-height: 100vh;
      font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(37,99,235,.08), transparent 28rem),
        linear-gradient(180deg, #f8fafc, #eef3fb);
    }}
    header {{
      position: sticky;
      top: 0;
      z-index: 2;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding: 14px 18px;
      border-bottom: 1px solid var(--line);
      background: rgba(255,255,255,.92);
      backdrop-filter: blur(14px);
    }}
    h1 {{
      margin: 0;
      font-size: 16px;
      letter-spacing: .02em;
    }}
    .hint {{
      margin: 0;
      color: var(--muted);
      font-size: 13px;
    }}
    .stage {{
      width: 100vw;
      height: calc(100vh - 58px);
      overflow: auto;
      padding: 20px;
    }}
    .canvas-wrap {{
      min-height: 100%;
      display: grid;
      place-items: start center;
    }}
    .canvas {{
      width: fit-content;
      min-width: 0;
      min-height: 0;
      display: inline-grid;
      place-items: center;
      padding: 28px 32px;
      border: 1px solid var(--line);
      border-radius: 22px;
      background: rgba(255,255,255,.9);
      box-shadow: 0 24px 70px rgba(15,23,42,.08);
      transform-origin: top center;
      margin: 0 auto;
    }}
    .mermaid {{
      width: fit-content;
      max-width: none;
      margin: 0;
    }}
    .toolbar {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    button {{
      border: 1px solid var(--line);
      border-radius: 999px;
      background: #ffffff;
      color: var(--ink);
      padding: 7px 12px;
      font: inherit;
      cursor: pointer;
    }}
    button:hover {{
      border-color: var(--accent);
      color: var(--accent);
      background: var(--accent-soft);
    }}
  </style>
</head>
<body>
  <header>
    <div>
      <h1>{safe_title}</h1>
      <p class="hint">Scroll to pan. Use browser zoom or the buttons to inspect details.</p>
    </div>
    <div class="toolbar">
      <button type="button" onclick="zoom(0.85)">Zoom out</button>
      <button type="button" onclick="zoom(1.15)">Zoom in</button>
      <button type="button" onclick="resetZoom()">Reset</button>
    </div>
  </header>
  <main class="stage">
    <section class="canvas-wrap">
      <div id="canvas" class="canvas">
        <pre class="mermaid">
{safe_diagram}
        </pre>
      </div>
    </section>
  </main>
  <script type="module">
    import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
    mermaid.initialize({{
      startOnLoad: true,
      securityLevel: "loose",
      theme: "base",
      themeVariables: {{
        fontFamily: "Segoe UI, sans-serif",
        primaryColor: "#ffffff",
        primaryTextColor: "#182030",
        primaryBorderColor: "#b9c7dc",
        lineColor: "#2563eb",
        secondaryColor: "#ffffff",
        tertiaryColor: "#f8fafc",
        clusterBkg: "#ffffff",
        clusterBorder: "#c7d2e3"
      }}
    }});
    let scale = 1;
    const canvas = document.getElementById("canvas");
    window.zoom = (factor) => {{
      scale = Math.max(0.35, Math.min(3.0, scale * factor));
      canvas.style.transform = `scale(${{scale}})`;
    }};
    window.resetZoom = () => {{
      scale = 1;
      canvas.style.transform = "scale(1)";
    }};
  </script>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to a .mmd/.mermaid file")
    parser.add_argument("--output", required=True, help="Path to write the HTML preview")
    parser.add_argument("--title", default=DEFAULT_TITLE, help="HTML title")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    diagram = input_path.read_text(encoding="utf-8")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_html(diagram, args.title), encoding="utf-8", newline="\n")
    print(str(output_path.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
