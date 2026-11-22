# GitHub watcher recovery

If watching stops with "Stopped watching, could not read it", check for rate
limiting before retrying:

```sh
gh api rate_limit --jq .resources.graphql
```

If the limit is exhausted, use a harness-supported delayed wake for the reset if
available; otherwise report the blocker. Never watch again in a tight loop.

When GraphQL is used up, the REST limit is separate and usually still has room.
Use `gh api repos/<owner>/<repo>/pulls/<n>` to read a PR, and
`gh api repos/<owner>/<repo>/commits/<sha>/check-runs` for checks. Reading through
REST does not itself restore monitoring; confirm the watcher is active before
leaving the PR unattended.
