---
name: council
description: Independent review by models from several providers. Use when the user says 'council'.
---

# Council

Bring in independent reviewers to review or give feedback on the user's request.
An editor runs the review in its own worktree and commits its best call on each
finding there. The host's worktree stays untouched until the user approves
changes at the end.

## Roles

- **Host:** the agent the user asked for council. It starts the editor, relays
  the editor's final report, and applies the changes the user approves.
- **Editor:** runs the review rounds, commits changes in the editor's worktree,
  and writes all of council's reports. It never touches the host's worktree.
- **Reviewers:** read the editor's worktree, give feedback, and change nothing.

The editor's instructions are in [references/editor.md](references/editor.md).
If the review covers no files in a repo, such as an idea in the conversation,
skip the editor: the host follows those instructions itself, without a worktree
or commits.

## Preparation

Before an audit, fix known issues and run relevant checks. Give council the
updated implementation; do not defer known fixes until reviews return. If the
user wants to discard the implementation and explore new ideas, skip fixes to
code being replaced.

## Start the editor

Start one editor on the host's own model, unless the user names another:

- **In T3 Code:** use `delegate_task` with `isolation: "worktree"`.
- **Elsewhere:** use the harness's subagent tool with its own worktree. If the
  harness's subagents can't start subagents of their own, act as the editor
  yourself from a worktree you create with `git worktree add`, and never edit
  the host's worktree.

Brief the editor with the request, the relevant context, the path of the host's
worktree, any round limit or reviewer choice from the user, and the path of
[references/editor.md](references/editor.md). Tell it to follow that file,
including starting the reviewers. Then wait for its
[final report](references/editor.md#final-report).

## Apply approved changes

The host posts the editor's [final report](references/editor.md#final-report)
as is, adds no questions, and ends its turn. The user replies with what to apply, change, or
drop, possibly including declined findings.

Apply each approved change in the host's worktree as its own commit,
`council: <summary>`. Cherry-pick the editor's commit, or reimplement it when it
doesn't apply cleanly. Do not amend, fixup, squash, or reorder existing commits
unless the user asks. Remove the editor's worktree and its branch once the
approved changes are applied, unless the user wants to keep them.
