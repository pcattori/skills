---
name: spec
description: Use before any edit to spec/*.md, when refining domain terminology, writing or reviewing a behavioral specification, changing terminology or behavior while prototyping, or implementing against an existing spec.
---

# Spec

Actively refine the domain's language and behavior as you design, prototype, and
implement. Record terms in `spec/glossary.md` and capabilities, rules, and
examples in `spec/behavior.md`.

- **Term:** a domain concept with a canonical name and precise meaning.
- **Capability:** a coherent thing a caller can accomplish.
- **Rule:** a guarantee or constraint within a capability.
- **Example:** concrete preconditions, an action, and its expected outcome.

## Every spec edit needs approval

Before writing to a spec file, show the change in the
[review format](#review-proposed-changes) and wait for the user to approve it.
That holds however small the edit or whatever prompted it: syncing the spec with
code, fixing review findings, or carrying out an agreed design. Approving a code
change doesn't approve the spec edits that go with it.

If you can't ask the user, as a subagent or delegate, don't edit the spec.
Return the proposed changes in the [terminal format](references/review-terminal.md)
so they can be presented for approval.

## Keep the spec current

Keep using this skill after `align` ends. Before acting on prototype or
implementation feedback, check the relevant glossary entries and behavior rules.
Surface proposed spec changes in the same turn: is “Surprises” a canonical
rename or just a screen label? Call out behavior changes separately. Leave
styling, copy, and prototype shortcuts out unless they change the contract.

You can try an unsettled change in a prototype, but flag the mismatch and
resolve it before implementing the affected behavior for real.

## Refine the model

- **Clarify terminology**

  Flag conflicts with the glossary immediately and propose precise terms when
  language is vague or overloaded. For example: “The glossary distinguishes
  Customer from User. Which do you mean by ‘account’?”

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

  Show the exact proposed changes for approval, individually or as a batch.
  Record only what the user approves, and do so promptly. Don't add defaults,
  edge cases, or guarantees. Keep proposals and open questions in chat.

- **Apply approved renames throughout the spec**

  An approved canonical rename applies throughout the spec. Search for the old
  term and update every reference to that concept except intentional `_Avoid_`
  entries; ask separately only if meaning or behavior changes.

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

## Implementation

When implementing against a spec, read [Implement the spec](references/implement.md)
for how the glossary maps to domain types and schemas and behavior maps to tests.
