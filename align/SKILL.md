---
name: align
description: Use when the user wants to align on a plan, design, or idea through pointed questions.
---

# Align

Interview the user until you reach a shared understanding. Read
[spec](../spec/SKILL.md) and the project's existing spec first. Use the glossary
and behavior to challenge assumptions and record approved changes as you go.

## Work the design tree in rounds

Map decisions as a **design tree**: each decision unlocks the decisions that
depend on it. The **frontier** is all open decisions whose prerequisites are
settled. Ask the whole frontier in one round, then wait. Don't ask a follow-up
whose answer depends on a decision still open in this round.

Number the questions and give a recommended answer for each. Phrase the question
so "yes" accepts your recommendation.

```markdown
❓ **Q1** — **<title>**: <question>

➡️ <recommended answer>

---

❓ **Q2** — **<title>**: <question>

➡️ <recommended answer>
```

**Find facts; ask for decisions.** Use a background subagent with fresh context
to look up facts from the environment. If delegation isn't available, look them
up yourself. Don't ask the user for facts you can find. A pending lookup blocks
only the questions that depend on it; ask the rest of the frontier now.

## Review spec changes first

At the start and after each round, look for concrete spec changes, including
distinctions worth naming.

- **Spec changes ready:** Use a spec-only round in the
  [spec review format](../spec/SKILL.md#review-proposed-changes). Wait for the
  user's response and record approved changes before asking design questions.
- **Nothing ready to review:** Ask the design frontier.

**When the frontier is empty and no spec changes are pending**, recap how the
agreed decisions fit together and ask whether anything is off. Don't ask the
user to reapprove recorded changes. Record approved changes as part of the discussion. Implementing the design or
changing tests requires a separate request.
