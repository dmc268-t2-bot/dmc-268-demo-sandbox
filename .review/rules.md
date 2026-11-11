# Demo repository rules

These rules exist so Eng 5 can show a **rules violation** PR.

## Documentation

- [DOC-1] Every public function must have a docstring that states purpose and parameters in one or two sentences.

## Security

- [SEC-1] Do not build SQL with string concatenation or an f-string that embeds user input. Use bound parameters.
