# Forecasts

A public, append-only record of probabilistic forecasts, scored by [wagwan-score](https://github.com/SMC17/method-wagwan) (Brier, log score, calibration). Every update records its outside view, decomposition, inside view and what would change the forecaster's mind, and chains the hash of the record before it, so history cannot be quietly edited (`python3 ops/forecasts.py check`).

`SMC17` is the owner's own record. `agent:*` records are AI forecasting pipelines, kept and scored separately.

## agent:claude-opus-5.5

3 forecasts, 0 resolved.

| Question | Forecast | Resolves by | Outcome |
|---|---:|---|---|
| [Will the 10-year Treasury yield close at or above 5.00% on 30 November 2026?](forecasts/ledger/ust10y-2026-11-30-at-least-5pct.json) | 0.78 | 2026-12-04 | open |
| [Will US CPI inflation for November 2026 be 4.0% or higher year on year?](forecasts/ledger/us-cpi-2026-11-yoy-at-least-4pct.json) | 0.71 | 2026-12-31 | open |
| [Will the 10-year Treasury yield close at or above 5.25% on 31 December 2026?](forecasts/ledger/ust10y-2026-12-31-at-least-5-25pct.json) | 0.38 | 2027-01-08 | open |
