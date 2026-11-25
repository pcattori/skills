---
name: consult
description: Independent review by other models. Use when the user says 'consult' or asks a specific model to review a change, plan, or idea.
---

# Consult

Ask other models to review the user's request: a change, a plan, or an idea.
Reviewers only read and report. Consult changes nothing and ends with their
reports; what to apply is the user's call afterward.

## Reviewers

- **Default:** one reviewer, the latest GPT Sol at high reasoning effort, or the
  latest Claude Opus if you run on Sol yourself.
- **Named:** exactly the models the user names, like `consult neon opus`, at
  high reasoning effort unless the user says otherwise.

Start them in parallel with the harness's subagent tool. In T3 Code, resolve
current model IDs and reasoning settings through `orchestrator_capabilities`,
then start them with `delegate_task`. If a reviewer is unavailable or fails,
say so; don't retry or substitute another.

## Before you start

- **Known issues first:** fix what you already know about and run the relevant
  checks. If the user wants to discard the implementation and explore new
  ideas, skip fixes to code being replaced.
- **Scope:** for a change, from the base to the working tree, including
  untracked files. The base is the one the user gives, or else the merge base
  with the target or default branch.

## Brief

Give each reviewer the request, the relevant context, the repo path, the base,
and the check results. Tell it:

- **Read-only:** don't change any checkout or start subagents.
- **No approvals:** never request approval or permissions. Work around a
  refused command, or skip it and mark the claim unverified.
- **Scratch in `/tmp`:** and don't clean it up. Some harnesses ask for approval
  on any `rm -rf`.
- **Report:** end with a [report](#report) as its final result.

Don't edit what the reviewers are reading until they finish. A reviewer that
stops on an approval or a question counts as failed: cancel it.

## Report

Reviewers write in this format:

```markdown
## GPT Sol: 7/10

The routing core is solid, but error paths misbehave.

1. **Response options can replace the declared status.** (`src/response.ts:42`)

   `c.response(body, { status: 500 })` on a 200 route returns 500. Suggested
   fix: take only `headers` from options.
```

- **Header:** the reviewer and, for a change, a score out of 10.
- **Summary:** one sentence.
- **Findings:** most severe first, each with its `file:line` when there is one,
  the failing scenario, and a suggested fix.

End your turn with each report as is, in the order they finish. Don't reword,
merge, renumber, or drop findings. After a report, add **Host notes** only for
findings you checked against the code and believe are wrong, citing the
finding's number and your reason.
