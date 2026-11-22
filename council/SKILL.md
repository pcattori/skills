---
name: council
description: Independent review by delegates from several model providers. Use when the user says 'council'.
---

# Council

Bring in independent delegates to review or give feedback on the user's request.

## Preparation

Before an audit, address outstanding PR comments, fix known issues, and run
relevant checks. Give council the updated implementation; do not defer known
fixes until reviews return. If the user wants to discard the implementation
and explore new ideas, skip fixes to code being replaced.

## Members

By default, use these flagship models at high reasoning effort:

- **Anthropic:** Claude Opus.
- **OpenAI:** GPT Sol.

Use different members only when the user explicitly requests them.

- **In T3 Code:** resolve current model IDs and supported reasoning settings
  through `orchestrator_capabilities`, then start the delegates in parallel
  with `delegate_task`. Follow the harness's delegation rules.
- **Elsewhere:** use the harness's subagent tools to resolve and start the
  members in parallel.

If a member is unavailable or its run fails, report it once and continue
with the remaining members. Retry or substitute only at the user's request.

## Review

1. **Brief the delegates.** Give each delegate the request and relevant context.
   Keep their work read-only. For a code review, ask for a score out of 10.
2. **Assess results as they arrive.** Check findings against the code at once
   and decide what to fix while the other delegates run. Wait to edit files
   until no delegate is reviewing the same checkout. If the user marks a
   delegate as non-blocking, do not wait for it; treat a late result as feedback
   and do not record its score.
3. **Summarize the review.** Collect the responses and summarize useful findings,
   disagreements, and recommended next steps. Count each full review pass as
   one round.
4. **Fix and repeat.** If you agree with the recommendations, make the changes
   and request a fresh review. Each fresh review after fixes starts a new round.
   Continue until all delegates are satisfied with the outcome, for at most 5
   rounds unless the user sets a different limit. If the limit is reached, stop
   and report the remaining disagreements. Keep changes within the requested
   scope throughout repeated reviews.

## Reporting

If the work ends in a pull request, put the results in the PR description.

```markdown
## Council review

Rounds: 2

| Delegate | Round 1 | Round 2 |
| --- | --- | --- |
| Claude Opus | 7/10 | 9/10 |
| GPT Sol | 8/10 | 10/10 |
```

If a delegate gives no score, write `no score`. Do not invent one.
If the PR is open, edit the description. Do not post a comment for this.
If there is no PR, put the same results in the final reply only.
