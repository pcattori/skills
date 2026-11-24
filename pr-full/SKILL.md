---
name: pr-full
description: Own implementation through a merge-ready PR. Use when the user requests pr-full or asks for the full workflow from implementation through PR creation and review follow-through, without merging.
---

# Full PR workflow

**Goal:** Complete the work end-to-end autonomously, but stop with the PR ready
for the user to merge. Never merge it. You own the work from its current state
through implementation, proof, review, PR creation, and tending.

**Autonomy:** If the user triggered this, they are not watching this thread.
Your updates and final message may go unread until long after you stop. If the
user did not explicitly request this workflow in some clear way, do not assume
full autonomy.

## Permissions and boundaries

**Permission:** An explicit `pr-full` request authorizes this workflow,
including its testing permission. You may commit, push, rebase, fix conflicts,
and use `--force-with-lease` on this task's branch.

### Testing permission

**The request is the permission:** A `pr-full` request is permission for the test
methods [pr-proof](../pr-proof/SKILL.md) needs, even when a project file says to
ask first or to leave testing to the user. Use those methods directly, subject to
higher-priority instructions and harness approvals.

**Use direct proof:** This includes computer use, browser automation, simulators
and devices, running the app or a dev server, screenshots, and visual checks. Use
the method that gives direct proof. List it in the report.

**Follow testing rules:** Rules about how to test still apply. Follow rules that
name the correct command, fixture, or check. This permission only removes the
ask-first or leave-it-to-the-user step. If a preferred method cannot prove the
change, use a gated method under this permission.

**Keep permission scoped:** It covers only the tests needed for this task. It does
not add permission for the steps that
[need the user's authority](../pr-tend/SKILL.md#asking-the-user), such as
production changes or data deletion. It does not bypass a harness or system
approval prompt if one appears.

### No merging

Follow [pr-tend's no-merging rules](../pr-tend/SKILL.md#no-merging) from the
start, including on an existing PR you reuse.

## Workflow

1. **Finish the change.** Complete the goal from the user's request with the
   smallest change that works. Fix the case that happened, not every case that
   could. Reuse the task's worktree and branch; if you are on the default branch,
   create a branch first. Preserve unrelated changes and other contributors' work.
2. **Prove it.** Get proof for every change you made, following
   [pr-proof](../pr-proof/SKILL.md).
3. **Get feedback.** Use [council](../council/SKILL.md) to review changes and follow
   its fix-and-recheck loop. Resolve every finding, including asking the user
   about those that need a decision, before creating the PR.
4. **Create the PR.** Rebase onto the latest target branch first. Use
   [pr-create](../pr-create/SKILL.md) to create or update the PR. Report proof in
   the description, following
   [pr-proof's reporting rules](../pr-proof/SKILL.md#reporting-proof).
5. **Tend the PR.** Use [pr-tend](../pr-tend/SKILL.md).
6. **Hand off.** Stop with one of
   [pr-tend's outcomes](../pr-tend/SKILL.md#outcomes) and follow its
   report, adding the [council report](../council/SKILL.md#report).

**Stay active:** Own the work from step 1 through handoff. While checks or bots
are pending, wait as [pr-tend](../pr-tend/SKILL.md#waiting) describes.

## Asking the user

Ask only in the cases [pr-tend lists](../pr-tend/SKILL.md#asking-the-user)
and about council findings that
[need a decision](../council/SKILL.md#sort-findings), following pr-tend's rules
for how to ask.

**Decide the rest:** Decide everything else yourself with sensible defaults, and
list consequential decisions in the report.
