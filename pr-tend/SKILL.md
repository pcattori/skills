---
name: pr-tend
description: Address PR review feedback and monitor review and CI. Use when triaging or fixing review findings, tending a PR, or another workflow delegates PR follow-through.
---

# Tend a PR

## No merging

**Leave merging to the user:** Never merge, enable auto-merge, enter a merge queue,
push to the default or target branch, bypass branch protection, or delegate those
actions.

**Prevent automatic merging:** Disable existing auto-merge and remove the PR from
any merge queue before work begins; check again before each push. Report these
changes. If you cannot prevent automatic merging, stop as blocked.

## Establish context

Identify the repository host, PR, source branch, and target branch. Read applicable
repository and organization instructions for review bots, checks, and conventions.
Use the host's CLI to inspect the PR: `gh` for GitHub, `glab` for GitLab.

This workflow currently requires T3 Code's `watch_pull_request` and
`unwatch_pull_request` tools. Discover them and confirm support for the PR's host.
If monitoring is unavailable, report the limitation rather than promise unattended
follow-through or substitute a polling script.

Reuse the task's worktree and branch, normally already created by T3 Code.
Preserve unrelated changes and other contributors' work. A PR-tending request
authorizes scoped fixes, relevant verification, commits, pushes, rebasing this
task's branch with `--force-with-lease`, and purposeful review replies. For
anything beyond that, follow [Asking the user](#asking-the-user).

## Waiting

Never write your own watcher, polling loop, or `sleep` loop. Use one watcher per
PR.

Handle the existing checks and comments first. Check readiness before waiting.
If work is still pending, call `watch_pull_request` and end your turn. T3 Code
wakes you with a message when a check fails, the required checks pass, someone
comments or reviews, or the branch conflicts.

- **Only the thread that owns the PR watches it.** If you are a delegated child
  task, never call `watch_pull_request`. The parent owns the PR. Report findings
  to the parent instead.
- **A wake is news, not a readiness decision.** Inspect the latest revision and
  apply the [readiness gate](#readiness-gate) yourself. The watch stays active after each
  wake; do not register it again unless it stopped.
- **Stay quiet while waiting.** When an event needs no action and the PR is not
  ready, end your turn without a message. Never post or say "still waiting".
- **Unwatch when you hand off.** A watched thread stays in Working and out of the
  user's inbox. When you stop (any [outcome](#outcomes), or asking the user a
  question), call `unwatch_pull_request` first. A merge or close ends the watch
  on its own.

If watching a GitHub PR stops because it cannot be read, consult
[GitHub watcher recovery](references/github-rate-limits.md) before retrying.

## Reviews and fixes

**Comments and resolution:** Use
[pr-comments](../pr-comments/SKILL.md) for every comment posted on
the user's behalf. This request authorizes replies with written reasons, and
resolution of threads whose concerns are actually addressed and verified. A
declined finding is not automatically an addressed concern.

**Assess findings:** Verify every bot finding against the source before changing
code. Fix real findings and CI failures, distinguish repository failures from
infrastructure flakes, and reply with a written reason when dismissing false
positives. Check whether older feedback still applies to the current revision
rather than ignoring it solely because it predates the latest push.

**Trace before disputing:** When a bot finding cites a rule, standard, or policy
you believe is wrong or misapplied, trace it to the source the bot read (its
prompt, its config, and the documents it quotes) using applicable instructions.
Dispute with evidence the bot can read on its next run, in the forms its rules
accept. When the source itself is wrong, the fix lies outside this PR: stop as
blocked and report the source location and your recommended upstream fix.

**Review completion:** Identify expected review bots and their completion signals
from applicable instructions, pipeline configuration, and existing reviews.
Completion must cover the latest revision; a failed or skipped review job is not
proof of a completed review. If the expected bot or completion signal is unclear,
surface that gap.

**Scope control:** Review loops tend to grow a PR one cheap-looking fix at a time.
Prefer small fixes within the user's goal. Explain declined suggestions; ask
before expanding scope or noticeably increasing complexity.

**Proof:** Get proof for each fix before you push it, following
[pr-proof](../pr-proof/SKILL.md). After pushing, reassess checks and reviews on
the new revision.

## Base branch

Before handoff, fetch and inspect target-branch changes; the watcher reports
conflicts but not BEHIND status. Rebase if the branch is behind, conflicts, or new
target commits overlap this PR's files. Use rebase, not merge commits. Push a
rewritten published branch with `--force-with-lease`, then wait for checks and
reviews on the updated revision. Pause if the push would overwrite another
contributor's work.

If an overlapping PR makes this one obsolete, stop monitoring, report it to the
user, and ask before closing the PR.

## Readiness and handoff

### Readiness gate

The PR is ready when all of these are true on the latest revision:

- **Proof:** Proof following [pr-proof](../pr-proof/SKILL.md) covers every change
  in the diff, including follow-up fixes.
- **Checks:** Required checks are green. If no required checks are configured,
  inspect the repository's CI checks rather than treating an empty requirement
  list as proof.
- **Bot review:** Expected review bots have finished; each actionable finding is
  fixed or has a written disposition. No unresolved actionable concern remains.
- **Human review:** No human review still requests changes, and any approval
  required by repository policy or the user is present. Do not wait for other
  human reviews.
- **Branch:** The branch is up to date with its target, conflict-free, and
  reported mergeable by the host. Do not bypass branch protection to reach this
  state.
- **PR state:** The live PR is open, not a draft, and not set to merge without
  the user.

Before handing off, fetch the target branch and check the live PR's head, base,
checks, reviews, and mergeability against the gate.

### Outcomes

Stop with one of these outcomes:

- **Ready to merge:** The readiness gate passes.
- **Waiting for required approval:** Only an approval required by repository
  policy or the user remains. Confirm that this is the actual blocker.
- **Blocked:** Readiness cannot be reached safely within the authorized scope.
  Explain what prevents readiness, what you tried, and what is needed. A watcher
  or review-service failure is not approval. Ask the user, following
  [Asking the user](#asking-the-user).

In every outcome, leave the PR open and unmerged.

### Report

After stopping the watch, report:

- The PR link, final head, outcome, and whether the PR is still open and
  unmerged. If someone else merged or closed it, report the actual state.
- Each actionable concern by thread reference and disposition, grouping
  duplicates.
- Consequential decisions you made for the user, and remaining risks.
- Proof, following [pr-proof's reporting rules](../pr-proof/SKILL.md#reporting-proof).

Put user decisions first.

## Asking the user

**Ask only when you cannot continue alone:**

- **Proof is missing:** You cannot prove the change.
- **Readiness is blocked:** The gate cannot pass, and you cannot fix that yourself.
- **Authority is missing:** The next step is outside what the request
  authorized: deleting data, touching production, changing things outside the
  repo, closing a PR, force-pushing any other branch, or overwriting another
  contributor's work.
- **The goal is ambiguous:** The ambiguity changes the result or requires
  materially expanding scope.
- **The work is obsolete:** Another PR makes this one obsolete.

**Use the question tool:** A question in a normal message goes unseen, and the
thread looks done. Use the harness's question tool so the thread shows that it is
waiting. Put all the context in the question: the PR link if available, what
blocks you, and the options with your recommendation first.

**Take the safe path:** If no question tool is available, or the tool returns no
answer, leave the PR open and unmerged, and start your final message with the
question.
