---
name: orient
description: Step-by-step walkthroughs that gloss jargon by its role in context. Use when the user asks to be walked through or oriented in a change, PR, design, or system they lack context for.
---

# Orient

Walk the reader through something they lack context for, such as a PR, a design
doc, or an incident, one step at a time. Explain each piece of jargon by what it
does in this context, not by its general definition.

## Before the first step

- **Read everything first:** the change, its ticket, its review threads, and the
  docs it cites. Steps built on partial reading get rewritten.
- **Separate stated from inferred:** when the sources say what changed but not
  why, say where the why comes from.

## Steps

1. **Problem:** the previous state and what was wrong with it.
2. **Solution:** the approach, at a high level.
3. **Mechanics:** how the solution works, one part per step, such as one CI job
   or one module.

Cover one step per turn, then end with one line naming the next step, so the
reader can say "next" or ask about this one. Answer questions before moving on.

Keep each step short: a sentence or two of setup, then the key points as a short
list.

## Glosses

A gloss explains a term's role here: what it does in this context, which of its
features this context uses, and what changes about it. Leave the general
definition to the linked docs.

- ❌ **Redis:** an open-source, in-memory key-value data store.
- ✅ **Redis:** where sessions now live instead of the database. This PR uses
  only its key expiry, so stale sessions delete themselves instead of needing a
  cleanup job.

Rules for glosses:

- **Which terms:** jargon a newcomer to this context wouldn't know, glossed at
  its first use in each step. Skip words the reader already uses.
- **Length:** one to three sentences of plain text.
- **No new jargon:** write glosses in words the reader already knows. If a gloss
  needs another term, gloss that term in the step text instead.
- **Docs link:** end with a link to the most specific docs for the feature the
  gloss describes, such as a section anchor rather than a product home page.

## Presentation

- **Inline HTML (such as T3 Code):** render each step as an HTML page where
  glossed terms open a popover on hover, focus, or tap. Start from
  [template.html](references/template.html), write the page to
  `/tmp/orient/<topic>-step-<n>.html`, and show it with the host's HTML
  rendering tools. Don't repeat the step in Markdown; reply with the line naming
  the next step.
- **Markdown only:** put the gloss in parentheses after the term at its first
  use, and link the term to its docs. Don't use link titles as tooltips: few
  renderers show them, and they can't hold a link.
