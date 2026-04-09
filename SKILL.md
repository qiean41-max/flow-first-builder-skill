---
name: flow-first-builder
description: "Use when a user is building a complex feature or module and the logic is still fuzzy. This skill runs a flow-first workflow: clarify the target, choose main-flow or sub-flow mode, ask one question at a time with A/B/C/D/E options, produce one diagram per round, confirm the logic, then hand off to implementation planning."
license: MIT
user-invocable: true
allowed-tools:
  - Read
  - Glob
  - Grep
  - Write
  - Edit
metadata:
  version: 2.0.0
  audience: beginner-builders
  domains:
    - planning
    - feature-design
    - flowchart
    - module-architecture
    - handoff
---

# Flow First Builder

This skill exists to stop beginners from jumping from a vague idea straight into code.

For any complex feature, module, or multi-module system, the workflow is:

1. clarify the goal
2. choose whether to work on the main flow or a sub flow
3. refine the logic through guided questions
4. generate and revise diagrams
5. confirm the diagram
6. produce a coding handoff

## When To Use

Use this skill when:

- the user is building a feature with multiple modules, steps, or decision branches
- the user is a beginner and may not yet see the module boundaries clearly
- the user asks for a flowchart, tree, logic structure, module split, or implementation sequence
- implementation would likely drift without a diagram-first pass

Do not use this skill when:

- the task is a small isolated tweak
- the logic is already stable and fully specified
- the user explicitly wants direct implementation and the task is trivial

## Triggers

Use this skill when the user says things like:

- `help me draw the flow first`
- `I need a flowchart before coding`
- `split this feature into modules`
- `help me figure out the logic before implementation`
- `draw the main flow`

## Quick Reference

| Item | Rule |
|------|------|
| Entry question | Ask whether to start with the `main flowchart` or `sub flowchart` |
| Question cadence | One key question per round |
| Choice format | Always provide `A/B/C/D/E`, where `E` is custom |
| Diagram count | Exactly one diagram per response |
| Diagram mode | That one diagram must be either `main` or `sub` |
| Diagram source of truth | `Mermaid`, plus zoomable HTML preview when readability is weak |
| Coding rule | Do not move to implementation before diagram confirmation |
| Handoff after confirmation | Implementation order, module split, interfaces, stack guidance |

## Core Rules

### Rule 1: First explain, then branch

The first message should briefly explain what this skill does, then ask:

- start with the **main flowchart**
- or start with the **sub flowchart**

Do not skip this opening branch.

### Rule 2: One question per round

Ask only one key question per round.

Do not dump a checklist.
Do not ask multiple unrelated questions in one response.

### Rule 3: Always provide structured choices

When asking a question, provide:

1. `A`
2. `B`
3. `C`
4. `D`
5. `E` = other / custom

`E` must always exist.

The choices should be:

- mutually exclusive
- easy for a beginner to understand
- framed to reduce ambiguity

### Rule 4: One diagram per response

Every diagram round must output exactly one diagram.

That diagram can only be one of:

- `main flowchart`
- `sub flowchart`

Never output both in the same response.

### Rule 5: Always state current mode

Whenever a diagram is shown, explicitly state:

- whether this is the **main flowchart** or **sub flowchart**
- which module is currently being discussed

This is mandatory.

### Rule 6: Mermaid is the source of truth

Default diagram format is:

- `Mermaid flowchart`
- `Mermaid graph`

If the user needs better readability, generate a zoomable HTML preview from the Mermaid source. Use the bundled `scripts/mermaid_html_preview.py` helper when possible. A static image export can also be generated if the environment supports it, but HTML preview is the default because it is easier to zoom and inspect.

Create a preview when any of these are true:

- the user explicitly asks for an image, preview link, HTML file, or zoomable view
- the diagram has more than 8 nodes
- the diagram has more than 10 edges
- the diagram is visually dense or likely to be unreadable in chat

Recommended output location:

- current project: `docs/flowcharts/<module-or-scope>-<version>.html`
- no project context: `%TEMP%/codex-flowcharts/<module-or-scope>-<version>.html`

When a preview file is created, include a clickable absolute path to it in the response. Do not replace the Mermaid source with HTML only; keep Mermaid as the canonical source for future reasoning.

Mermaid remains the canonical version because AI can continue reasoning from it.

### Rule 7: Do not code before the diagram is confirmed

If the diagram is not yet confirmed, the skill should explicitly say:

`The logic is not fully confirmed yet. Refine the diagram first, then move to implementation.`

Do not encourage coding too early.

### Rule 8: Give technical guidance at key moments

This skill must not assume an AI editor can do everything alone.

At key moments, it should explain:

- what technologies may be needed
- what the AI editor can help with
- what still requires frameworks, services, or other tooling

Examples:

- LangChain
- RAG
- workflow orchestration
- queues
- databases
- schema validation
- API frameworks

Do not give technical stack advice every round.
Give it when it materially helps the user make better architecture decisions.

### Rule 9: Support partial adoption

Users may not have used this skill for every module.

If the user asks for a main flowchart later in the project, the skill may:

- read the current project structure
- infer a candidate flow or architecture map
- present it as a **draft**

Do not present inferred diagrams as certain truth.

Use wording like:

`Based on the current code and file structure, this is a candidate main flowchart draft. Please confirm or correct it.`

## Memory Model

The skill should track:

- the current module being discussed
- whether the current diagram is main or sub
- confirmed diagram versions
- the current module's position in the whole project
- upstream and downstream module relationships

## Versioning Rules

Keep confirmed versions.

Each confirmed diagram should have:

- a version number
- a diagram type (`main` or `sub`)
- a module name or scope label

Only the latest version is the active working version, but older confirmed versions should still be referable.

## Output Structure

Each response should be organized into three layers when applicable:

1. `Diagram`
2. `Explanation`
3. `Handoff`

### Diagram

Contains:

- current mode (`main` or `sub`)
- current module
- Mermaid diagram

### Explanation

Contains:

- what the diagram means
- what changed from the previous version
- what is still unclear

### Handoff

Only output this after confirmation.

Contains:

- implementation order
- module decomposition
- interface relationships
- key technical suggestions
- AI editor boundary reminders when relevant

## Standard Workflow

### Phase 1: Opening

Start with:

- one-sentence explanation of the skill
- main vs sub flow starting choice

Example:

`This skill helps you refine complex feature logic with diagrams before coding. Do you want to start with the main flowchart or a sub flowchart?`

### Phase 2: Guided Refinement

For each round:

- ask one important question
- offer A/B/C/D/E choices
- accept custom input
- update the diagram

### Phase 3: Diagram Confirmation

Ask the user to confirm whether the current diagram matches the intended logic.

If not confirmed:

- revise the diagram
- continue the guided loop

### Phase 4: Handoff

Once the diagram is confirmed:

- output implementation order
- output module split
- output interface relationships
- output key stack suggestions

For diagram patterns, version naming, and export guidance, see [references/diagram-guidelines.md](references/diagram-guidelines.md).

## Completion Condition

A round is complete only when:

- the current diagram is confirmed
- the explanation is clear enough for the user
- the handoff is usable for actual implementation

This means completion requires:

- confirmed diagram
- explanation
- implementation order
- interface relationships
- technical guidance where relevant

## Quality Bar

The skill is successful only if:

- the user can understand the logic visually
- module boundaries are clearer than before
- the diagram reduces coding ambiguity
- the output can be used for implementation planning, project discussion, or interview explanation

If the output still feels fuzzy, continue refining the diagram instead of pretending the planning is complete.

## Verification / Success Criteria

Use this checklist before treating the current round as complete:

- [ ] The response clearly states whether the diagram is `main` or `sub`
- [ ] The response clearly names the current module or scope
- [ ] The response contains exactly one Mermaid diagram
- [ ] The user-facing explanation says what changed and what is still unclear
- [ ] If the diagram is not confirmed, the response explicitly advises refining the logic before coding
- [ ] If the diagram is confirmed, the handoff includes implementation order
- [ ] If the diagram is confirmed, the handoff includes module boundaries and interface relationships
- [ ] If relevant, the response includes key technology suggestions and editor/tooling boundary reminders

## Anti-Patterns

| Do not do this | Do this instead |
|----------------|------------------|
| Output both main and sub diagrams in one response | Output exactly one diagram and state the current mode |
| Ask a checklist of unrelated questions | Ask one key question per round |
| Force coding before the user confirms the logic | Keep refining the diagram until confirmed |
| Present inferred architecture as certain truth | Label inferred output as a draft and ask for correction |
| Give generic stack advice every round | Give stack advice only when it changes design quality or implementation realism |

## Extension Points

- Add automatic project-structure reading to draft a candidate main flow
- Add image export helpers for Mermaid previews
- Add version persistence helpers for confirmed diagrams
- Add framework-specific handoff presets for frontend, backend, and AI workflows
