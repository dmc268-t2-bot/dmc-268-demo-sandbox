# Case mapping

Scenario labels (S1–S3) are stable. **GitHub pull numbers** are creation order
and do **not** match S1/S2/S3. Prefer the Eng 5 evidence table in
`dmc-268-ui-t2` → `docs/eng5-demo-sandbox.md`.

| Scenario | Branch | GitHub PR | Theme |
|---|---|---|---|
| S1 | `demo/01-clean` | [pull/1](https://github.com/dmc268-t2-bot/dmc-268-demo-sandbox/pull/1) | Clean parameterized lookup |
| S2 | `demo/02-sql-injection` | [pull/3](https://github.com/dmc268-t2-bot/dmc-268-demo-sandbox/pull/3) | Critical SQL injection |
| S3 | `demo/03-rules-docstring` | [pull/2](https://github.com/dmc268-t2-bot/dmc-268-demo-sandbox/pull/2) | Missing docstring vs `STY-1` |

## S1 — clean (`demo/01-clean` → GitHub pull/1)

- Source: `test-prs-dataset/fixtures/clean-001-well-factored-handler`
- File: `app/users/lookup.py`
- Gold `expected_findings.json`: `[]`

## S2 — critical security (`demo/02-sql-injection` → GitHub pull/3)

- Source: `test-prs-dataset/fixtures/sec-001-sql-injection`
- File: `app/search.py`
- Gold label: critical security on the concatenated query

## S3 — rules violation (`demo/03-rules-docstring` → GitHub pull/2)

- Custom (board DoD: link to `.review/rules.md`)
- File: `app/reports/export.py`
- Violates `[STY-1]` in `.review/rules.md` (public function, no docstring)

## Optional later (not opened by default)

- `sec-002-hardcoded-secret` — fake `sk_live_…` key; useful for log-secret / finding demos
