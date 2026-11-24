# Testing

For modeling a behavioral spec in test code, see the [Behavior informs tests](../../spec/references/implement.md#behavior-informs-tests).

## Source-code fixtures

- **Dedented templates:** use `dedent` for embedded text or code.
  Use import aliases for syntax highlighted tagged templates. For example, `ts` alias for embedded TypeScript code.

- **Comparable layout:** put fixture contents on lines between separate opening
  and closing backtick lines, even when the source itself is a single line.

- **Relative indentation:** indent fixtures with the surrounding test code;
  preserve the source's internal indentation relative to that common margin.

- **Exact bytes:** use explicit escapes when bytes such as tabs or CRLF line
  endings are the behavior under test, rather than letting dedentation alter them.

```ts
import ts from "dedent";

const fixture = {
  input: ts`
    type IsString<T> = T extends string ? true : false;
  `,
  output: ts`
    type IsString<T> =
      T extends string ? true :
      false;
  `,
};
```
