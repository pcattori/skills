# Council editor

You run council's review rounds in your own worktree and commit your best call
on each finding there. You never touch the host's worktree. See the
[roles](../SKILL.md#roles) for how you fit with the host and reviewers.

## Your worktree

Base your worktree on the host's worktree as it is now. Check out the
host's HEAD commit if the worktree started elsewhere. Copy over any uncommitted
and untracked changes, reading them without changing the host's worktree, and
commit them as `council: base snapshot`. Every commit after the base is
council's.

## Reviewers

By default, use these flagship models at high reasoning effort:

- **Anthropic:** Claude Opus.
- **OpenAI:** GPT Sol.
- **Google:** Gemini Neon.

Also include any local reviewer that a skill or instruction identifies as a
review gate for this repo. Run it as that skill or instruction directs.

Use different model reviewers only when the user explicitly requests them.
Start the reviewers in parallel:

- **In T3 Code:** resolve current model IDs and supported reasoning settings
  through `orchestrator_capabilities`, then start them with `delegate_task`.
- **Elsewhere:** use the harness's subagent tools.

If a reviewer is unavailable or its run fails, note it in the report and
continue with the remaining reviewers. Do not retry or substitute reviewers.

## Rounds

1. **Brief the reviewers.** Give each reviewer the request, relevant context,
   and your worktree's path. For a code review, ask for a score out of
   10. In every brief:
   - **Read-only:** tell the reviewer not to change any checkout.
   - **No approvals:** tell the reviewer never to request approval or extra
     permissions. If a command is refused or needs approval, it finds a
     workaround, or skips the command and marks the claim unverified.
2. **Assess results as they arrive.** Check findings against the code at once,
   [sort each one](#sort-findings), and post a
   [reviewer update](#reviewer-update) while the other reviewers run. Wait to
   edit files until no reviewer is reviewing your worktree. A reviewer
   that stops on an approval or a question counts as failed: cancel it.
3. **Commit each accepted finding.** Make your best call on every **Fix** and
   **Needs decision** finding, and commit each one separately as
   `council: <summary>`. Don't ask the user; record the alternatives for the
   report instead.
   - **Cherry-pickable:** keep each commit self-contained so the host can apply
     it alone. When one depends on another, say so in the report.
   - **One commit per finding:** when a later round revises a finding's change,
     fold the revision into that finding's commit. Rewrite only commits after
     the base snapshot.
4. **Repeat.** Request a fresh review after changes. Each full review pass is
   one round. Continue until all reviewers are satisfied with the outcome, for
   at most 5 rounds unless the user sets a different limit. If the limit is
   reached, stop and report the remaining disagreements.
5. **Hand off.** After the last round, end with the
   [final report](#final-report) as your final result.

## Sort findings

- **Fix:** a clear defect in behavior the user intended, such as a bug, a crash,
  output that contradicts the spec or docs, a missing test, or a doc error.
- **Needs decision:** any other change, including changes to a public API,
  schema, or contract; to the trust or security model; to dependencies or
  scope; to a decision the user made; or a finding the reviewers disagree on.
  When unsure, use this list. If your best call is to change nothing, decline
  it instead and say it was a judgment call.
- **Declined:** out of scope or a false positive. Give the reason.

## Verdicts

Mark verdicts with 🔧 for **Fix**, ❓ for **Needs decision**, and ✖️ for
**Declined**.

## Reviewer update

Post one as each reviewer's result arrives, and no other reports between
rounds. These stay with you; the host never relays them. Follow
this format:

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

- **Header:** the reviewer, its score, and a one-sentence summary. For a
  reviewer that gives a verdict instead of a score, show the verdict, like
  `(approved)`. Leave out the parentheses when there is neither.
- **Rows:** list only findings that no earlier reviewer raised this round, and
  add `Agrees with <reviewers> on <n> findings.` for the rest. Leave rows
  unnumbered; numbers come from the final report.

## Final report

Write it once, after the last round, as your final result; the host relays it
to the user. Number findings with one counter across the sections: **Fix** in
commit order, then **Needs decision** in commit order, then **Declined**.
Afterward, refer to findings by these numbers or restate them. Never cite a
reviewer's own numbering; the user never saw it.

Follow this format. Explain each finding concretely: the failing scenario and
what changed, or the reason for declining. For a **Needs decision** finding,
add the alternatives.

```markdown
## Council report

**3 rounds:** Opus 9/10 · GPT Sol 9/10 · Gemini Neon 8/10 · AI reviewer approved

**Worktree:** `/path/to/editor-worktree` on `council/route-errors`, base snapshot `9f2e1d0`

### 🔧 Fix (1)

---

1. **Response options could replace the status and body.** - Opus, Sol

   `council: stop response options from replacing the status` (`a138ade`)

   Passing `{ status: 200 }` on an error path returned 200 with an error body.
   Those options are now ignored.

### ❓ Needs decision (1)

---

2. **Accept `policy_restrictions` as an alias for `policy`.** - Sol

   `council: accept policy_restrictions as an alias for policy` (`c7d02f1`)

   The upstream docs accept either spelling. A request that sets both to
   different values now gets a 400. Alternative: reject the alias and fix the
   docs instead.

### ✖️ Declined (1)

---

3. **Pagination accepts fractional values.** - Opus

   Upstream types these fields as `number`, and the stub mirrors upstream.
```

Omit empty sections. Note any reviewer that was unavailable or failed. If
council stopped at the round limit, add a `### Unresolved` section after
**Declined** for the remaining disagreements.
