# DMC-268 Team 2 — demo sandbox

Public demo repository for Sprint 5 Eng 5. Three pull requests map to the board DoD and (where noted) to gold-corpus cases in `dmc-268-api-t2/test-prs-dataset`.

| PR theme | Expected bot behaviour | Gold fixture (if any) |
|---|---|---|
| Clean parameterized lookup | Approve / LGTM, no critical findings | `clean-001-well-factored-handler` |
| SQL injection via string concat | Critical security comment | `sec-001-sql-injection` |
| Missing docstring vs `.review/rules.md` | Comment that cites the rules file | *(custom — not in gold set)* |

## Branches

- `demo/01-clean`
- `demo/02-sql-injection`
- `demo/03-rules-docstring`

Open each as a PR into `main`, connect this repo to the AI Code Reviewer bot, run review, leave comments visible for the defense.

## Not this repo

Gold **scores** still come from `scripts.eval_harness` on fixtures. These PRs are the live demo path.
