# TradingLab Public Presentation Kit

This package is **public-safe demo material**, not a copy of TradingLab-Core or Carlson-Control-Plane.

## Contents
- `index.html`: static standalone dashboard. No JavaScript, runtime, broker, database, telemetry, or private service integration.
- `CONTRIBUTING.md`: collaboration instructions for prospective contributors.
- `SECURITY.md`: disclosure and evidence handling boundaries.
- `architecture.svg`: public, conceptual component diagram.

## Data claims
All visible chart values are explicitly SYNTHETIC and illustrative. No actual backtest, bot health, account exposure, live/paper P&L or regression count is represented. Before incorporating real measurements, independently verify each dated source, anonymize it, and get publication approval.

## Deployment
Open `index.html` locally or visit https://carlsonsbuild.github.io/TradingLab-Public/ . The public site is isolated from TradingLab runtime. Do not publish unscreened sensitive materials.

## Reproducible public demonstration
Run `python -m unittest test_public_demo -v` in this directory. Python 3.11+; standard library only. `evidence.json` contains measured local outputs for synthetic inputs and a source hash. These are educational validator results, not private runtime tests, financial performance, or bot qualification.

## Support policy
Donation links are withheld until ownership is verified in the signed-in Ko-fi owner dashboard. Any future donations fund development; they provide no equity, investment interest or entitlement to trading returns.

## Public demonstration videos
The `media/` videos use synthetic fixtures and measured public-validator results. Their source hashes and review status are in `video-evidence.json`. They contain captions and no audio. No private TradingLab implementation or operational data is included.
