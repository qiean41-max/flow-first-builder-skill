# Flow First Builder Spec

Status: accepted-v1

## Purpose

Create a planning skill for beginner builders who are working on complex AI application features and need a diagram-first collaboration workflow before implementation.

The skill should not behave like a one-shot diagram generator.
It should behave like a guided planning partner.

## Final Positioning

Flow First Builder is:

- a multi-round planning skill
- a diagram-first logic clarification skill
- a main-flow / sub-flow aware skill
- a versioned handoff skill
- a technical-boundary reminder skill

It is not:

- a pure drawing utility
- a direct coding skill
- a one-message answer generator

## Confirmed Decisions

### 1. Opening style

The skill starts by:

- briefly explaining what it does
- asking whether to start with the main flowchart or a sub flowchart

### 2. Interaction style

The skill asks one key question per round.

Every round should provide:

1. `A`
2. `B`
3. `C`
4. `D`
5. `E` = other / custom

`E` is mandatory.

### 3. Diagram output

The skill outputs exactly one diagram per response.

That diagram is either:

- a main flowchart
- or a sub flowchart

Never both in the same response.

### 4. State signaling

Every diagram response must explicitly say:

- whether it is the main flowchart or sub flowchart
- which module is currently being discussed

### 5. Diagram format

Default format:

- Mermaid as the source of truth
- image export only when needed for readability

### 6. Memory

The skill should track:

- current module
- current diagram type
- confirmed versions
- the module's place in the whole project

### 7. Handoff after confirmation

After the user confirms a diagram, the skill should output:

- implementation order
- module decomposition
- interface relationships
- key technical suggestions when relevant

### 8. Technical guidance

At important moments, the skill should remind the user:

- what technologies may really be needed
- what an AI editor can do
- what an AI editor cannot fully replace

### 9. Trigger policy

Default behavior:

- do not auto-force this skill
- when a request is complex, suggest switching into this workflow

### 10. Readability policy

The skill should not try to solve readability by mixing multiple diagrams in a single reply.

Instead:

- keep one response = one diagram
- clearly label mode and scope

### 11. Code discipline

If the diagram is not confirmed yet, the skill should clearly advise against jumping into coding.

### 12. Version policy

Keep all confirmed versions with version numbers.

The newest confirmed version is the active working reference.

### 13. Output layers

The output should clearly separate:

1. diagram
2. explanation
3. handoff

## Future Extension

V2 may support:

- reading an existing codebase
- inferring a draft main flowchart or sub flowchart
- presenting the inferred diagram as a candidate draft for user confirmation

## Acceptance Standard

The skill is acceptable if:

- a beginner can understand the feature through the diagrams
- the planning process stays structured instead of chaotic
- the handoff is useful for real implementation
- the skill consistently keeps track of main vs sub flow
