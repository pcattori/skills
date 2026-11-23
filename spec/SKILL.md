---
name: spec
description: Use when refining domain terminology or writing or reviewing a behavioral specification.
---

# Spec

Refine the domain's language and behavior together. Record terms in
`spec/glossary.md` and capabilities, rules, and examples in `spec/behavior.md`.

- **Term:** a domain concept with a canonical name and precise meaning.
- **Capability:** a coherent thing a caller can accomplish.
- **Rule:** a guarantee or constraint within a capability.
- **Example:** concrete preconditions, an action, and its expected outcome.

## Refine the model

Treat terminology and behavior as a feedback loop, not separate phases. A concrete
scenario may expose a missing concept; a sharper definition may change a rule.

- **Challenge against defined terms**

  When the user uses a term that conflicts with the glossary, call it out
  immediately: "Your glossary defines 'cancellation' as X, but you seem to mean
  Y. Which is it?"

- **Sharpen fuzzy language**

  When the user uses vague or overloaded terms, propose a precise canonical term:
  "You're saying 'account': do you mean the Customer or the User? Those are
  different things."

- **Discuss concrete scenarios**

  When domain relationships are being discussed, stress-test them with specific
  scenarios. Invent edge cases that force the user to be precise about the
  boundaries between concepts. For example: "Can part of an order line's quantity
  be cancelled? If so, is cancellation a state of the line, or do we need a
  distinct Cancellation concept?"

- **Cross-reference with code**

  When the user states how something works, check whether the code agrees. Surface
  contradictions: "Your code cancels entire Orders, but you just said partial
  cancellation is possible. Which is right?" Resolve the intended contract with
  the user; current behavior is evidence, not automatically the authority.

- **Propose, then record**

  Don't infer approval from usage. Agree on the name and meaning before adding
  or revising a glossary entry. Don't prefill the glossary from a repo scan.

  In a conversation, show the exact proposed changes before writing them.
  The user can approve a batch. Write only what they approve, without adding
  defaults, edge cases, or guarantees. Keep proposals and open questions in chat.

## Review proposed changes

Prefer inline HTML. If the renderer isn't already loaded, search the harness's
tools for it (`html_render` in T3 Code) before falling back. If available, fill in
[the HTML template](references/review.html) and call the renderer. Otherwise,
follow the [terminal example](references/review-terminal.md). Omit empty sections.

Label each change. Use the actual glossary term or capability heading when
changing one; use a short review-only label for individual behavior rules.
Don't write those review labels into the spec.

Add **Why** only to an existing behavior edit that needs a sentence of context.
It stays in the review; put requirements in the proposed rule or example.

## Write the spec

Use `spec/` at the package root in a multi-package monorepo, or the repository
root otherwise. Read any existing spec before proposing changes. Create each
file only when there's an approved change to record.

### Glossary

In `spec/glossary.md`, define context-specific concepts in one or two sentences.
Choose one canonical name and list competing names under `_Avoid_`.

Entries should capture the agreed **domain schema**: the attributes and
relationships that define a concept, including which are required or optional
when that's been decided. Use domain terms, not database or language types.
Put rules about what users can do and how the app responds in Behavior.

```markdown
# Glossary

**Event**: A gift-giving occasion with a required name and date, an optional
description, and a guest list that distinguishes invited guests from those
who've accepted.
_Avoid_: Gathering
```

### Behavior

In `spec/behavior.md`, give each capability a heading named for a caller goal,
not an implementation component. Order capabilities from the simplest useful
behavior to richer cases and interactions as prerequisites allow.

Give each independent rule its own bold bullet, with supporting examples
indented beneath it. Start with a simple example, then boundaries. Keep
rejections beside the rules they enforce.

```markdown
# Behavior

## Place an order

- **Placing an order requires at least one order line.**

  Placing an order with no lines fails with an empty-order error.
```

## Contract tests during implementation

When implementing a capability, give it one corresponding contract test named
for that capability in `spec/behavior.md`. The test can have multiple cases to
cover the capability's rules and examples. Test the behavior callers can
observe, not how the implementation delivers it.
