---
name: write-for-humans
description: Write Markdown that people can scan. Use when writing or revising docs, READMEs, PR descriptions, or skills.
---

# Write for humans

Readers scan for the part they need. Make it easy to find, and make every line
worth reading.

## Structure

- **Overview first:** open with the document's job in one sentence and the
  overall picture, then explain the parts.
- **One H1, then `##`:** use `###` sparingly, only when a `##` section has
  distinct parts a reader needs to jump between.
- **Bold starters:** open paragraphs and long list items with a bold phrase,
  `- **Label:** explanation`, so a reader can tell what each is about at a glance.
- **Headings and labels navigate:** name what's under them, so a reader can find
  the part they need. A heading that only decorates a paragraph can go.
- **Tables and trees:** use tables for entries a reader compares. Use fenced
  `text` trees for directory layouts, annotating only the roles that aren't
  obvious and using placeholders like `packages/<name>/` for collections.
- **Alerts sparingly:** keep primary guidance in the main text. Use
  [alerts](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#alerts)
  (`NOTE`, `WARNING`, ...) only for supporting context or serious risks, and only
  where the renderer supports them.

## Content

- **High signal-to-noise:** cut exposition and anything that doesn't change what
  the reader knows or does.
- **Contrast with examples:** when a rule is about quality, a ❌️/✅ pair teaches
  more than another sentence of rules.
- **Link, don't copy:** link to the source for facts owned elsewhere, such as
  docs, repos, or other documents. Copies go stale.
