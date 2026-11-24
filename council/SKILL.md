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
   Keep their work read-only. For a code review, ask for a score out of 10, but
   leave scores out of reports.
2. **Assess results as they arrive.** Check findings against the code at once
   and [sort each one](#sort-findings) while the other delegates run. Wait to
   edit files until no delegate is reviewing the same checkout. If the user
   marks a delegate as non-blocking, do not wait for it; treat a late result as
   feedback.
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

Show the [report](#report), then use the harness's question tool to ask about
each **Needs decision** finding by number, recommendation first. Without a
question tool, end your turn with the report and the questions. Do not
implement these findings until the user decides. The user may also respond to
**Fixed** or **Declined** findings; address that feedback too. Move each
finding the user weighs in on to **Fixed** or **Declined**, marked as the
user's call.

## Report

Number findings with one counter across the lists: **Fixed** in commit order,
then **Needs decision**, then **Declined**. Refer to findings by their number in
the latest report, or restate them. Never cite a delegate's own numbering; the
user never saw it.

Follow this format. Explain each finding concretely: the failing scenario and
what changed, the trade-off and your recommendation, or the reason for
declining.

```markdown
**Fixed**

1. **Response options could replace the status and body.** - Opus, Sol

   `council: stop response options from replacing the status` (`a138ade`)

   Passing `{ status: 200 }` on an error path returned 200 with an error body.
   Those options are now ignored.

**Needs decision**

2. **Accept `policy_restrictions` as an alias for `policy`?** - Sol

   The upstream docs accept either spelling, but the upstream schema lists only
   `policy`. Accepting it changes the public request schema. Recommended:
   accept it, and return a 400 when the two values conflict.

**Declined**

3. **Pagination accepts fractional values.** - Opus

   Upstream types these fields as `number`, and the stub mirrors upstream.
```

Omit empty lists. Note any member that was unavailable or failed.

**Final report:** first resolve every **Needs decision** finding and all user
feedback on the report, then put the report in the final reply.
