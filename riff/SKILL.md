---
name: riff
description: Use when the user asks for alternatives to a name, idea, or phrasing, or says 'riff'.
---

# Riff

Propose alternatives to the thing the user gives you: your best 3, then 5 more
ranging from most pedantic to most creative. A number in the request, like
`riff 8`, sets the size of the range list; the top list stays at 3.

## Before riffing

Take the target from the request or the conversation. Ask only when you can't
tell what to riff on.

Find the constraints first: what the thing is for, conventions around it (such
as sibling names in the codebase), and anything the user already rejected. Look
these up rather than asking. Every option must fit them, the creative ones too.

## Format

```markdown
**Top 3**

- 🥇 **<option>**: <why it works, in one line>
- 🥈 **<option>**: <why>
- 🥉 **<option>**: <why>

**From most pedantic to most creative**

1. <option>
2. <option>
3. <option>
4. <option>
5. <option>
```

- **Top 3:** your strongest picks, best first. The 🥇 is your recommendation, so
  add nothing after the lists.
- **Range:** distinct from the top 3. The first option is the most literal and
  conventional; the last is the most metaphorical or unexpected that still
  works.

## Follow-ups

When the user points at an option or a direction ("more like 5"), riff again
around it in the same format. Leave out options they've already seen.
