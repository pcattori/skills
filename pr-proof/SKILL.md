---
name: pr-proof
description: Prove a change works and report the evidence. Use when verifying a change or fix before pushing, deciding whether a fix needs fresh review, or reporting validation in a PR or handoff.
---

# Prove a change

**Proof** is evidence you observed yourself in this session: command output, a
reproduction, a screenshot. Get proof for every change before you push it, using
the most direct method the change allows. Follow repository rules that name the
correct command, fixture, or check.

## Methods

- **Reproduce the failure.** Reproduce the original failure, apply the fix, then
  watch the same reproduction pass.
- **Add regression coverage.** When the behavior has no test and the repo has a
  test setup, add one focused test. Observe that same test fail without the fix
  for the intended reason, then pass with it. A manual reproduction alone does
  not prove the test catches the bug.
- **Exercise real behavior.** For UI and runtime behavior, run the app and
  exercise the real affected path; green mocked tests do not prove the user
  experience works. Use screenshots for visual states and short recordings for
  interactions when they add useful evidence. Show the trigger and the settled
  result; inspect side effects or persistence when pixels alone cannot prove the
  fix.
- **Run relevant checks.** Before pushing, run the local checks the repo's CI
  runs for the affected code, such as typecheck, lint, and tests; avoid
  duplicating the full CI suite without a reason. After pushing, count checks on
  the latest revision as evidence.

## Coverage

Proof must cover the final diff, including follow-up fixes and meaningful
conflict resolutions. After each fix, recheck the behavior it affects. Renew
independent review, such as [council](../council/SKILL.md), only when a change
invalidates the earlier review, not automatically for every small finding.

When you cannot find a way to prove a change, you do not have full confidence.
Ask the user.

## Reporting proof

Report evidence beyond CI: the method you used, manual verification, checks CI
doesn't cover, and consequential validation gaps. Omit routine check inventories
and results already visible in CI. Attach screenshots or recordings to the PR
when they help and you have a way to upload them.
