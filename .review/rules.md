# Security
## SEC-1: No SQL string concat
- severity: critical
Do not build SQL with string concatenation or an f-string that embeds user input. Use bound parameters.

# Style
## STY-1: Public functions need docstrings
- severity: medium
Every public function must have a docstring that states purpose and parameters in one or two sentences.
