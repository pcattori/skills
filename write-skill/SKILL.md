---
name: write-skill
description: Author and organize agent skills. Use when creating, editing, splitting, merging, or renaming a skill or its reference files.
---

# Write a skill

A skill is read by two audiences: the agent deciding whether to load it, and a
human maintaining it. Write for both: an accurate trigger for the agent, and a
body a person can scan without their eyes glazing over, following
[write-for-humans](../write-for-humans/SKILL.md).

## Skill or reference file

- **Reference file:** material within the skill's subject that only some uses
  need, like `lang-typescript/references/testing.md`.
- **Own skill:** material the parent must spell out in detail for the agent to
  find it. A `toolchains` skill whose description listed both TypeScript and HTML
  cases became `lang-typescript` and `lang-html`.

## Naming and layout

- **Group by prefix:** give related skills a shared prefix when there are several
  in one domain (`pr-`, `lang-`, `write-`). Name each after the word you'd
  actually type to ask for it.
- **Generic first, specific on top:** keep conventions specific to one host or
  company, like GitLab quick actions for assigning reviewers, in their own skill
  layered on a generic one like `pr-create`.
- **Files:** `<name>/SKILL.md`, with supporting files in `<name>/references/`.

## Description

List the distinct cases that should load the skill:
`Use when <case>, <case>, or <case>.` Give each case once; synonyms for the same
case add load without adding reach. Include the words you actually speak or type, but
don't summarize the body.

Open with a subject (`<Subject>. Use when …`) only when the cases don't make it
obvious, such as a skill named after a project, or one that adds a convention
like attribution to an everyday task.

## Body

- **Only what changes behavior:** cut instructions the agent would follow anyway.
- **Tools by role:** name tools generically ("the harness's question tool"). When
  a skill needs a specific harness tool, say what to do when it's unavailable.
- **Autonomy needs limits:** a skill that lets the agent act on its own states
  what the request authorizes, when to ask, and how it ends.

## Warm cache

Keep a short local copy of linked material only when the agent will need it
often and looking it up is expensive; then the skill acts as a warm cache for
what matters most to its task.

Spend the skill's words on what no lookup would turn up: unwritten conventions,
the reasons behind choices, and gotchas the docs don't mention.

## Links between skills

- **Relative paths:** link other skills as `[pr-proof](../pr-proof/SKILL.md)`,
  and sections as `../pr-tend/SKILL.md#no-merging`.
- **Headings are API:** before renaming a heading or moving or renaming a file,
  find links to it from other skills and update them.

## Verify

Check that every relative link and `#anchor` pointing into a skill you changed
still resolves by running [check-links.py](scripts/check-links.py).
