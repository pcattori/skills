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

- **Update the spec inline**

  Propose unfamiliar terms in chat. If the user hasn't used a term, add it to the
  glossary only after they explicitly approve both the name and its meaning.
  Finding a term in code or docs isn't approval. Don't prefill the glossary from
  a repo scan.

  Record settled terms, capabilities, rules, and examples as they settle. In a
  conversation, write the settled changes after each round rather than waiting
  until the end. Keep proposals and open questions in chat, not in the spec.

## Write the spec

Use `spec/` at the package root in a multi-package monorepo, or the repository
root otherwise. Read any existing spec before proposing changes. Create each file only when it has something settled to
record.

### Glossary

In `spec/glossary.md`, define context-specific concepts in one or two sentences
each, stating what they are. Choose one canonical name and list competing names
under `_Avoid_`. Keep definitions free of implementation details; general
programming concepts belong only if they have a distinct meaning in this domain.

```markdown
# Glossary

**Order**: A customer's request to purchase one or more order lines.
_Avoid_: Purchase, transaction

**Order line**: A product and quantity requested within an order.
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
