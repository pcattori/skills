---
name: council
description: Independent review by delegates from several model providers. Use when the user says 'council'.
---

# Council

Bring in independent delegates to review or give feedback on the user's request.

## Preparation

Before an audit, fix known issues and run relevant checks. Give council the
updated implementation; do not defer known fixes until reviews return. If the
user wants to discard the implementation and explore new ideas, skip fixes to
code being replaced.

## Members

By default, use these flagship models at high reasoning effort:

- **Anthropic:** Claude Opus.
- **OpenAI:** GPT Sol.
- **Google:** Gemini Neon.

Also include any local reviewer that a skill or instruction identifies as a
review gate for this repo. Run it as that skill or instruction directs.

Use different model members only when the user explicitly requests them. Start
the members in parallel:

- **In T3 Code:** resolve current model IDs and supported reasoning settings
  through `orchestrator_capabilities`, then start them with `delegate_task`.
- **Elsewhere:** use the harness's subagent tools.

If a member is unavailable or its run fails, report it once and continue
with the remaining members. Retry or substitute only at the user's request.

## Review

1. **Brief the delegates.** Give each delegate the request and relevant context.
   For a code review, ask for a score out of 10. In every brief:
   - **Read-only:** tell the delegate not to change the checkout.
   - **No approvals:** tell the delegate never to request approval or extra
     permissions. If a command is refused or needs approval, it finds a
     workaround, or skips the command and marks the claim unverified.
2. **Assess results as they arrive.** Check findings against the code at once,
   [sort each one](#sort-findings), and post a
   [member update](#member-update) while the other delegates run. Wait to
   edit files until no delegate is reviewing the same checkout. If the user
   marks a delegate as non-blocking, do not wait for it; treat a late result as
   feedback.
   - **Stalled delegate:** if a delegate stops on an approval or a question,
     tell the user at once and offer to answer it, cancel the delegate, or mark
     it non-blocking. Do not approve on the user's behalf.
3. **Fix, then ask.** Commit each fix separately as `council: <summary>`. Do
   not amend, fixup, squash, or reorder existing commits unless the user asks.
   If any finding needs the user's decision, [ask](#ask-the-user) before the
   next round, so that round reviews the decided changes.
4. **Repeat.** Request a fresh review after changes. Each full review pass is
   one round. Continue until all delegates are satisfied with the outcome, for
   at most 5 rounds unless the user sets a different limit. If the limit is
   reached, stop and report the remaining disagreements.

### Sort findings

- **Fix:** a clear defect in behavior the user intended, such as a bug, a crash,
  output that contradicts the spec or docs, a missing test, or a doc error. Fix
  it without asking.
- **Needs decision:** any other change, including changes to a public API,
  schema, or contract; to the trust or security model; to dependencies or
  scope; to a decision the user made; or a finding the delegates disagree on.
  When unsure, use this list.
- **Declined:** out of scope or a false positive. Give the reason.

### Ask the user

Use the harness's question tool to ask about each **Needs decision** finding,
restating it with its trade-off, recommendation first. Without a question tool,
end your turn with the questions. Do not implement these findings until the
user decides. The user may also respond to **Fix** or **Declined** findings in
a member update; address that feedback too. Move each finding the user weighs
in on to **Fixed** or **Declined**, marked as the user's call.

## Report

Post a [member update](#member-update) as each member's result arrives, and the
[final report](#final-report) when council ends. Between rounds, post no other
reports except a [stalled delegate](#review) notice. Mark verdicts with 🔧 for
**Fix**, ❓ for **Needs decision**, and ✖️ for **Declined**.

### Member update

Follow this format:

```markdown
**GPT Sol (6/10):** The routing core is solid, but error paths and HEAD requests misbehave.

| Verdict | Finding | Note |
|---|---|---|
| 🔧 | Response options replace status and body | `{ status: 200 }` on an error path returns 200 |
| 🔧 | HEAD hangs on cancel | Cancelling the client never ends the request |
| ❓ | `policy_restrictions` alias | Docs accept it, schema doesn't |
| ✖️ | Staging contract test | Needs a deployed env |

Still running: Opus, Gemini Neon, AI reviewer.
```

- **Header:** the member, its score, and a one-sentence summary. For a member
  that gives a verdict instead of a score, show the verdict, like
  `(approved)`. Leave out the parentheses when there is neither.
- **Rows:** list only findings that no earlier member raised this round, and
  add `Agrees with <members> on <n> findings.` for the rest. Leave rows
  unnumbered; numbers come from the final report.

### Final report

First resolve every **Needs decision** finding and all user feedback, then put
the final report in the final reply. Number findings with one counter across
the sections: **Fixed** in commit order, then **Declined**. Afterward, refer to
findings by these numbers or restate them. Never cite a delegate's own
numbering; the user never saw it.

Follow this format. Explain each finding concretely: the failing scenario and
what changed, or the reason for declining. Mark findings the user decided with
`· you` after the member names.

```markdown
## Council report

**3 rounds:** Opus 9/10 · GPT Sol 9/10 · Gemini Neon 8/10 · AI reviewer approved

### 🔧 Fixed (2)

---

1. **Response options could replace the status and body.** - Opus, Sol

   `council: stop response options from replacing the status` (`a138ade`)

   Passing `{ status: 200 }` on an error path returned 200 with an error body.
   Those options are now ignored.

2. **Accept `policy_restrictions` as an alias for `policy`.** - Sol · you

   `council: accept policy_restrictions as an alias for policy` (`c7d02f1`)

   The upstream docs accept either spelling. A request that sets both to
   different values now gets a 400.

### ✖️ Declined (1)

---

3. **Pagination accepts fractional values.** - Opus

   Upstream types these fields as `number`, and the stub mirrors upstream.
```

Omit empty sections. Note any member that was unavailable or failed. If council
stopped at the round limit, add a `### ❓ Unresolved` section after **Declined**
for the remaining disagreements.
