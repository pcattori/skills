---
name: hone
description: Use when the user wants to hone a plan, design, or idea together through pointed questions.
---

# Hone

Interview the user until you reach a shared understanding. Read
[spec](../spec/SKILL.md) and the project's existing spec first. Use the glossary
and behavior to challenge assumptions and record settled decisions as you go.

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

## Record decisions and confirm

**After each round**, update the spec with only the glossary entries and behavior
that have settled, following [spec](../spec/SKILL.md#refine-the-model). Keep open
questions in the conversation. Don't create spec files for decisions that don't
belong in them. Recompute the frontier and ask the next round.

**When the frontier is empty**, ask the user to confirm the shared understanding.
Recording settled decisions is part of honing; implementing the design or
changing tests requires a separate request.
