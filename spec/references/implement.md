# Implement the spec

Use the glossary to shape the domain model and the behavior spec to test what
callers can observe.

## Glossary informs types and schemas

- **One canonical model per structured term:** Give each glossary term that
  defines fields or relationships a corresponding domain type or schema named
  for the term. Match the agreed fields, relationships, and required or optional
  status.

- **Keep the mapping at the domain level:** Storage records, API payloads, and
  UI drafts may have different shapes. Map them to or from the canonical model
  at their boundaries.

### Example: Event

Given this entry in `spec/glossary.md`:

```markdown
**Event**: A scheduled gathering with a required title and an optional description.
```

The corresponding TypeScript domain type:

```ts
type Event = {
  title: string;
  description?: string;
};
```

## Behavior informs tests

Spec tests verify caller-visible behavior and mirror the capabilities, rules,
and examples in `spec/behavior.md`.

- **Capability → suite:** use one suite named after the capability heading.

- **Rule → test:** give each rule its own test inside that suite, named for the rule.

- **Examples → cases:** when a rule has multiple examples, use a parameterized
  test with one case per example.

### Example

Given this excerpt from `spec/behavior.md`:

```markdown
## Place an order

- **An order must have at least one line.**

  Placing an order with no lines fails with an empty-order error.

- **Each order line must have a positive quantity.**

  Placing an order with a line quantity of 0 fails with an invalid-quantity error.
  Placing an order with a line quantity of -1 fails with an invalid-quantity error.
```

The same structure in TypeScript with Vitest:

```ts
import { describe, expect, test } from "vitest";
import { placeOrder } from "./orders";

describe("Place an order", () => {
  test("An order must have at least one line", () => {
    expect(() => placeOrder({ lines: [] })).toThrow("empty-order");
  });

  test.each([{ quantity: 0 }, { quantity: -1 }])(
    "Each order line must have a positive quantity (got $quantity)",
    ({ quantity }) => {
      expect(() => placeOrder({ lines: [{ quantity }] })).toThrow("invalid-quantity");
    },
  );
});
```
