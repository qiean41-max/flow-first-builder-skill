# Diagram Guidelines

Use these rules when the main `SKILL.md` needs a deeper reference for diagram handling.

## Diagram Type Rules

Only one diagram may appear in a single response.

Valid modes:

- `main`
- `sub`

Always label:

- current mode
- current module or scope
- version label when the diagram is confirmed

## Version Naming

Use simple labels:

- `main-v1`
- `main-v2`
- `sub-auth-v1`
- `sub-parser-v3`

## Mermaid Guidance

Prefer:

- `flowchart TD`
- `flowchart LR`

Keep labels short enough to remain readable.
If a node becomes too dense, split the logic in the next round instead of cramming more text into one node.

## Export Guidance

Mermaid is the canonical representation.
Create a zoomable HTML preview when:

- the user wants a cleaner preview
- the node count is high enough that raw Mermaid is hard to inspect
- the diagram is needed for slides, documents, or review
- the user asks for an image, preview link, HTML view, or a way to zoom in

Prefer the bundled helper:

```powershell
python "C:\Users\17818\.codex\skills\flow-first-builder\scripts\mermaid_html_preview.py" `
  --input diagram.mmd `
  --output docs\flowcharts\module-main-v1.html `
  --title "Module main flow"
```

The HTML preview should be treated as a readable artifact, not the source of truth. Keep the Mermaid source in the chat or in a sibling `.mmd` file.

Export static images only when:

- the user specifically asks for a PNG/SVG image
- the environment has a reliable Mermaid renderer available
- the output is going into a document or slide deck

## Main vs Sub Usage

Use a `main` flowchart when the user is deciding:

- how modules connect
- where the current module sits in the whole project
- end-to-end system flow

Use a `sub` flowchart when the user is deciding:

- internal logic of one module
- branch handling inside one feature
- detailed handoff before implementation
