---
name: pr-create
description: Create pull requests or update their titles and descriptions. Use when publishing a PR or revising its title or description.
---

# Create a pull request

Publish the intended change for review, following repository and host policy.

Try the host's CLI throughout the workflow:

- **GitHub:** `gh`.
- **GitLab:** `glab`, including self-managed hosts.

## Establish scope

- **Identify the source and target.** Determine the repository host, source
  repository and branch, and intended target repository and branch.
- **Reuse an existing PR.** Before filing, check whether a PR for this source and
  target already exists; reuse it rather than creating a duplicate.
- **Review the complete diff.** Compare locally against the target branch to make
  sure its contents match the user's goal and exclude unrelated changes. Account
  for uncommitted or unpushed changes so the published PR contains the intended
  work. Surface scope mismatches before publishing.

## Write the title and description

### Title

- **Follow repository title conventions.** PR titles often become commit messages.
  Look at recently merged PRs and Git history for examples.
- **Explain why the change matters.** Prefer a concise, human-readable title. Use
  quantified outcomes, as in the example below, only when measurements support them.

> ❌️ perf(server): negotiate permessage-deflate on the websocket

> ✅ perf(server): cut websocket frame size by 70%+ with gzipping

### Description

Write a description reviewers can scan, following
[write-for-humans](../write-for-humans/SKILL.md).

- **Lead with the problem, then the solution.** Open with a simple explanation of
  the problem based on the user's original prompt, then briefly explain the
  solution. Do not lead with an implementation inventory.

> ❌️ Removed implicit workspace carry-over from every "new thread" entry point (cmd+n / cmd+shift+o, sidebar v1/v2 buttons, command palette). New threads inherit only the project from context; branch, worktree, and env mode always come from the configured defaults. Deleted buildContextualThreadOptions, startNewThreadInProjectFromContext, and the v1 sidebar's seed-context machinery.

> ✅ My "new worktree" default was ignored when starting new threads on existing worktrees. Super unintuitive. Now your preferences always apply.

- **Include validation details only when they add information beyond CI,**
  following [pr-proof's reporting rules](../pr-proof/SKILL.md#reporting-proof).
  Omit a validation section by default.

## Publish and verify

- **Check for secrets and private details.** Before submission, check the title,
  description, quotes, and attachments for material inappropriate for the destination.
- **Open a ready PR.** Prefer ready over draft so review bots can run.
- **Add reviewers when requested.** Creating a ready PR is not itself a request to
  tag reviewers.
- **Verify the published PR.** Check source, target, title, description, and draft
  status. Return its URL and any unresolved blockers.
- **Keep follow-up comments purposeful.** Post only when they serve the user's
  request.
