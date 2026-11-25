---
name: consult
description: Independent review by other models. Use when the user says 'consult' or asks a specific model to review a change, plan, or idea.
---

# Consult

Ask other models to review the user's request: a change, a plan, or an idea.
Reviewers only read and report. Consult changes nothing and ends with one
[report](#report) that combines them; what to apply is the user's call afterward.

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
- **Report:** end with a [reviewer report](#reviewer-reports) as its final
  result.

Don't edit what the reviewers are reading until they finish. A reviewer that
stops on an approval or a question counts as failed: cancel it.

## Reviewer reports

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

Save each one as is to a shared directory for this consult, like
`/tmp/consult-a1b2/gpt-sol.md`.

## Report

Wait until every reviewer finishes or fails, then end your turn with one report
that combines them:

```markdown
## Consult report

*[GPT Sol (7/10)](/tmp/consult-a1b2/gpt-sol.md) · [Claude Opus (8/10)](/tmp/consult-a1b2/claude-opus.md) · ~~Claude Neon~~ (timed out)*

Both reviewers think the routing core is solid. Error paths are the weak spot.

1. **Response options can replace the declared status.** (`src/response.ts:42`) *Sol, Opus*

   `c.response(body, { status: 500 })` on a 200 route returns 500. Suggested
   fix: take only `headers` from options.

### Disagreements

- **Error format:** Sol wants RFC 9457 problem details. Opus says keep the
  current shape, because clients already parse it.
```

- **Reviewers:** an italic line under the heading, separated by `·`, with each
  score or status in parentheses. A reviewer that finished links to its saved
  report and shows its score, if it gave one. A failed reviewer has its name
  struck through and a status of a few words, like "timed out" or
  "unavailable". Explain a failure that needs more after the summary.
- **Summary:** one sentence for the whole consult.
- **Findings:** one list, most severe first. Merge findings with the same root
  cause into one, written fresh with the most useful details from each
  reviewer, including each reviewer's fix when they differ. End the title line
  with the reviewers who raised it.
- **Disagreements:** where reviewers contradict each other. Leave the section
  out if there are none.

Report what the reviewers said without adding your own verdicts.
