# Case mapping

## PR 1 — clean (`demo/01-clean`)

- Source: `test-prs-dataset/fixtures/clean-001-well-factored-handler`
- File: `app/users/lookup.py`
- Gold `expected_findings.json`: `[]`

## PR 2 — critical security (`demo/02-sql-injection`)

- Source: `test-prs-dataset/fixtures/sec-001-sql-injection`
- File: `app/search.py`
- Gold label: critical security on the concatenated query

## PR 3 — rules violation (`demo/03-rules-docstring`)

- Custom (board DoD: link to `.review/rules.md`)
- File: `app/reports/export.py`
- Violates `[STY-1]` in `.review/rules.md` (public function, no docstring)

## Optional later (not opened by default)

- `sec-002-hardcoded-secret` — fake `sk_live_…` key; useful for log-secret / finding demos
