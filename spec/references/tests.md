# Spec tests

Spec tests verify caller-visible behavior and mirror the capabilities, rules,
and examples in `spec/behavior.md`.

- **Capability → suite:** use one suite named after the capability heading.
- **Rule → test:** give each rule its own test inside that suite, named for the rule.
- **Examples → cases:** when a rule has multiple examples, use a parameterized
  test with one case per example.

## Example

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
