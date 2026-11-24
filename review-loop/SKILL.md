---
name: review-loop
description: Use when the user says 'review loop', asks for a specific model or review gate to review a change, or another workflow delegates a review pass.
---

# Review loop

One reviewer reviews the change. You fix the obvious mistakes it finds and ask
for another round, until a round finds nothing obvious to fix. Larger issues
are collected for the user to decide.

**Authorization:** fix [fix-now](#sort-findings) findings in the current
worktree, commit them, and run checks. Nothing else, including pushing. Never
ask the user mid-loop; end with the [report](#report).

## Reviewer

- **Default:** the latest GPT Sol at high reasoning effort, or the latest
  Claude Opus if you run on Sol yourself. The reviewer shouldn't be the
  author's model.
- **Named model:** the model the user names.
- **Named review gate:** a local reviewer a skill or instruction defines for
  the repo. Run it as directed and treat its output as findings.

Start a model reviewer with the harness's subagent tool (`delegate_task` in T3
Code). If the reviewer is unavailable, report it; don't substitute another.

## Before the first round

- **Scope:** from the base to the working tree, including untracked files. The
  base is the one the user gives, or else the merge base with the target or
  default branch. Leave unrelated changes alone.
- **Known issues first:** run the relevant checks and fix what they catch.

## Brief

Give the reviewer the repo path, base, intent, and check results. Ask for each
finding's `file:line`, failing scenario, and suggested fix. Tell it:

- **Read-only:** don't change any checkout or start subagents.
- **No approvals:** never request approval or permissions. Work around a
  refused command, or skip it and mark the claim unverified.
- **Scratch in `/tmp`:** and don't clean it up. Some harnesses ask for approval
  on any `rm -rf`.

## Sort findings

Check each finding against the code yourself; the reviewer's severity doesn't
decide.

- **Fix now:** clearly wrong for the change's intent, with a small, local
  fix that leaves the public surface alone: exported APIs and types, specs,
  generated output, schemas, dependencies, the security model, and the user's
  decisions.
- **Propose:** any other real issue. Split a mixed finding. When unsure,
  propose.
- **Decline:** a false positive, a nit, or against the intent.

Examples, most severe first:

- **Propose:** response options can override the declared status. Changes what
  an option does.
- **Fix now:** OpenAPI converts a body under the wrong codec.
- **Propose:** an exported config type gives handlers the wrong context.
  Exported type.
- **Fix now:** code allows `params` on a static path, which the spec
  forbids. The code catches up to the spec.
- **Propose:** a helper the change added has no tests. Grows scope.
- **Decline:** HEAD's `body.cancel()` can throw on a locked body. Contrived.

## Rounds

1. **Review.** Brief the reviewer and wait without editing. A reviewer that
   fails, times out, or stops on an approval or question ends the loop.
2. **Fix.** Apply each fix-now and rerun the relevant checks. Commit each fix
   as a new commit, `review: <summary>`. Never rewrite commits from before the
   loop; revise only the loop's own. If the change itself is uncommitted, leave
   the fixes uncommitted too.
3. **Repeat or stop.** Stop when a round has no fix-now findings, or after 3
   rounds unless the user sets another limit. Otherwise brief again with a
   ledger of earlier findings and outcomes. Ask for a review of the fixes and
   changed code only, without re-raising proposed or declined findings.

## Report

Number findings with one counter across both sections, ordering each section
by severity, most severe first. If the round limit stopped the loop, say so and
mark the last round's fixes as unreviewed.

- **Resolved:** a table of fixed (✅) and declined (✖️) findings, with the fix's
  commit SHA in the details.
- **Open:** a list of proposed findings, each with its bold
  title on its own line and the details in a paragraph below.

```markdown
## Review loop: GPT Sol

**2 rounds**, stopped clean. Checks pass.

### Resolved

| #   |     | Finding                                                              | Details                                                                                                            |
| --- | --- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1   | ✅  | **OpenAPI converted shared-media-type bodies under the wrong codec** | A text codec labeled `application/json` failed construction. Each body now converts under its own codec. `9fc40ee` |
| 2   | ✖️  | **HEAD's `body.cancel()` can throw on a locked body**                | Needs a hook that returns an already-locked body.                                                                  |

### Open

3. **Response options can replace the declared status.**

   `c.response(body, { status: 500 })` overrides the status. Take only
   `headers` from options. Not fixed: changes what the option does.
```
