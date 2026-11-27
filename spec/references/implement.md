# Implement the spec

Use the glossary to shape the domain model, the behavior spec to test what
callers can observe, and the scope to know what not to build yet.

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

## Scope informs tests and stopping points

- **Don't build past a limit:** a limit marks behavior that's deliberately
  absent. Implement it only once the limit is lifted and the behavior is
  specified.

- **Caller-visible limits → one `Scope` suite:** give each limit with an example
  its own test, named for the limit. Stubs get no test, so their stand-in
  behavior never becomes part of the contract.

- **Lift a limit and its test together:** when a limit's entry leaves
  `spec/scope.md`, delete its test and add tests for the behavior rules that
  replace it.
