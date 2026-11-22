---
name: spec
description: Define domain language and behavioral contracts. Use when refining terminology, writing a spec, or authoring, reviewing, or organizing tests that express it.
---

# Spec

Refine the domain's language and behavior together, recording terms, capabilities,
rules, and examples in `SPEC.md` and expressing the contract in tests.

- **Term:** a domain concept with a canonical name and precise meaning.
- **Capability:** a coherent thing a caller can accomplish.
- **Rule:** a guarantee or constraint within a capability.
- **Example:** concrete preconditions, an action, and its expected outcome.

## Refine the model

Treat terminology and behavior as a feedback loop, not separate phases. A concrete
scenario may expose a missing concept; a sharper definition may change a rule.

- **Challenge against defined terms**

  When the user uses a term that conflicts with the existing Terms section, call
  it out immediately: "Your spec defines 'cancellation' as X, but you seem to mean
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

  When a term is resolved, update the Terms section right there. Don't batch these
  up: capture them as they happen. Update rules and examples as they settle too.
  Keep unanswered questions explicit rather than inventing guarantees.

## Write the spec

Use `SPEC.md` at the package root in a multi-package monorepo, or the repository
root otherwise. Create the file when there is something resolved to record.

- **Terms:** define context-specific concepts in one or two sentences each,
  stating what they are. Choose one canonical name and list competing names under
  `_Avoid_`. Keep definitions free of implementation details; general programming
  concepts belong only if they have a distinct meaning in this domain.
- **Capabilities:** name caller goals and observable outcomes, not implementation
  components. Order them so understanding accumulates: simplest useful behavior
  first, then richer cases and interactions as prerequisites allow.
- **Rules and examples:** give each independent guarantee its own bold bullet,
  with supporting examples indented beneath it. Start with a simple example, then
  boundaries. Keep rejections beside the rules they enforce.

```markdown
# Ordering

## Terms

**Order**: A customer's request to purchase one or more order lines.
_Avoid_: Purchase, transaction

**Order line**: A product and quantity requested within an order.

## Capabilities

### Place an order

- **An order must contain at least one line.**

  Placing an order with no lines fails with an empty-order error.
```

## Express the contract in tests

- **Mirror the structure:** map test groups to capabilities, test names to rules,
  and concrete cases to examples. Check that the relevant spec rules and examples
  are represented; surface gaps or contradictions.
- **Keep examples independent:** each sets up its own state. Keep decisive inputs
  visible; helpers hide incidental mechanics. One behavior can need several
  assertions; split tests that join unrelated guarantees.
- **Assert the caller's contract:** include failure information callers rely on,
  such as an error tag and reason. Test dependency mechanics only where they are
  part of the promised behavior.
