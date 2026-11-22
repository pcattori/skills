---
name: pr-comments
description: Attribution and content for PR comments posted on the user's behalf. Use when posting PR comments, inline reviews, or replies.
---

# Leaving PR comments

Prefix every agent-authored comment with this portable Markdown blockquote:

```md
> 🤖 **<model> responding on behalf of <user>**

Actual comment starts here.
```

Use the verified public name of the model that wrote the comment, and the user's
name or repository-host login. If the harness does not expose a model name, use
the harness name. Do not guess.

Keep the attribution inside the blockquote and the actual reply outside it. The
attribution line must start with the robot emoji. Do not add a horizontal rule,
Setext underline, heading, signature footer, or a second attribution.

Apply this format to top-level PR comments, inline review comments, replies to
bots or reviewers, and written explanations used before resolving or dismissing
feedback. Do not add it to PR descriptions, commit messages, or text the user
explicitly asked to post verbatim without attribution.

## Comment content

- Lead with the conclusion.
- Cite the relevant code, behavior, check, or reproduction.
- Keep it concise and avoid filler, canned thanks, or status narration.
- Distinguish verified facts from judgment.

## Publish and verify

Before posting, check the entire comment, including quoted text and attachments,
for secrets and private details. Attribution does not itself authorize posting;
follow the user's request and applicable repository policy.

Check the final Markdown before posting so quoting and blank lines render as
shown. Use the host's CLI or API, such as `gh` for GitHub or `glab` for GitLab.
After posting, verify that the host returned the comment or review URL. If it
returns only an ID, retrieve the posted comment to verify its content and obtain
a link. Resolve a review thread only after its response was posted successfully.
