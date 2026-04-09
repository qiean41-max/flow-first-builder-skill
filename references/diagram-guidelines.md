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

## Layout Guidance

Default to a clean interview-grade layout.

Required layout priorities:

- one dominant reading direction
- centered main flow
- branch outcomes aligned on a shared row or column
- no unnecessary back edges
- avoid line crossings whenever possible

Recommended pattern for a route-based graph:

1. place the intake node at the top or far left
2. place the router directly after the intake node
3. fan out branches from a single rail
4. stack any follow-up step directly under its parent branch

Recommended pattern for a pipeline graph:

1. place each stage on the main spine
2. place optional exits below the decision point
3. place review or gate nodes after execution, not beside unrelated branches

Bad outputs:

- tangled graphs with crossing lines
- giant canvases with tiny content
- nodes stuffed with paragraphs
- ornamental shapes that make the flow harder to explain

Good outputs:

- crisp boxes
- obvious spine
- obvious split point
- obvious outcome nodes
- enough whitespace to read at a glance

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

When a preview is created, the preview should visually reinforce the same clean structure:

- light or dark theme is fine
- typography must stay legible
- the canvas should center the main flow
- avoid decorative clutter that competes with the logic

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
