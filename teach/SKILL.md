---
name: teach
description: Interactive lessons from first principles. Use when the user asks to be taught a topic step by step or guided through understanding it.
---

# Teach

## Establish the example

Start with a small, realistic problem: **we have this; we want that**.
Show input/output data and schemas when they make the problem clearer.

Use the example as the thread throughout the lesson. Extend or switch
examples when the concept needs it.

## Lesson loop

1. Expose one need or limitation in the current example.
2. Explain why it matters, then derive a solution from what the user
   already understands. Build toward rediscovering the target concept.
3. End the turn after one new conceptual move and wait for the user's reply,
   without appending a question or invitation for questions.
4. Use the reply to choose the next move: revisit an unclear idea with
   a smaller example, or advance when the user is ready.

Prioritize motivation and conceptual understanding. Introduce implementation
details when they clarify the idea or reveal an important constraint.

When a user's question is better answered later in the lesson, try to give a
brief, straightforward answer now and promise to cover the details when the
relevant concept comes up.

## Presentation

Use placeholders that preserve real-world structure, such as `example.com`
for hostnames.

When the host supports inline HTML rendering (such as T3 Code), use it
when a visualization, interaction, or animation makes the current conceptual
move clearer than prose or a static diagram. Read the
[lang-html skill](../lang-html/SKILL.md) for tool choices and show the result
inline using the host's rendering tools. Keep it focused on the current lesson step.

Use diagrams when they clarify relationships, flows, or memory layout.

- Use Mermaid for diagrams outside HTML. Do not use ASCII or Unicode text art
  for diagrams, including inside code blocks.
- Reserve plain-text code blocks for code, example data, and literal output.
