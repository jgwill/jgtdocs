# Documentation Upgrade Timeline

This timeline captures key events leading toward an optimized documentation state.

## 2025-06-18
- Initial review of repository documentation and package commands.
- Verified jgtpy, jgtml, and jgtagentic CLI helpers display usage output.
- Identified missing `bridge` directory; created `bridge/250618` for ongoing notes.
- Gathered memory recaps from spiral agents for context.
- Scanned `Workspace.jgwill.jgtpy*`, `Workspace.jgwill.jgtml*`, and `Workspace.jgwill.jgtagentic*` keys for relevant ledgers.
  Loaded Codex recap entries (`CodexRecap.*`) to track decisions from sister repositories.
- Verified CLI helpers again to ensure environment variables `JGTPY_DATA` and `JGTPY_DATA_FULL` resolve cached data correctly.
- Reviewed codex recap files pointing to Alligator Illusion Detection, market analysis, and trading platform activation ledgers.

### Memory Integration
- Retrieved key files from `Workspace.jgwill.jgtml.commit.files*` and `Workspace.jgwill.jgtagentic*` to capture recent script and ledger changes across sibling repositories.
- Studied trading scripts to map background processes:
  - `jgt_background_trader.sh` – coordinates multi-timeframe trading.
  - `jgt_batch_trader.sh` – dispatches batch loops across instruments.
  - `jgt_fdb_unified_scan.sh` – performs unified FDB scans before orders.
  - `trader_m5.sh`, `trader_m15.sh`, `trader_H1.sh` – auto-generated loops for each timeframe.
  - `unified_trading_loop.sh` – ties together the entire trading stack.
  - Orchestrator modules (`jgtagentic orchestrate`) – record and trigger workflows.
- Logged additional codex ledgers summarizing unified trading system integration efforts.

### CLI Verification
- Set `JGTPY_DATA` and `JGTPY_DATA_FULL` to cached paths under `/workspace/jgtdocs/data` and validated `jgtcli`, `mxcli`, and `jgtagentic` output to confirm toolchain stability.

## Next Steps
- Evaluate existing ledgers under `book/_/ledgers` to extract relevant phases.
- Draft narrative-map summarizing current repository commits.
- Document CLI issues encountered during `jgtcli` execution for future resolution.

## 2025-06-19
- Reviewed new llms.txt updates from main branch, noting additional package links for LLM documentation.
- Explored data directories under `data/current` and `data/full` using `jgtcli` and `cdscli` commands with cached paths.
- Confirmed dataset files such as `ttf/AUD-USD_H4_mz.csv` and `reports` exist, validating environment for offline analysis.
- Loaded Codex recap memory keys for cross-repo context: jgtpy, jgtml, and jgtagentic sessions.
- Documented these observations in ledger files for historical tracking.

## 2025-06-20
- Merged main branch changes bringing new agent coordination ledger.
- Resolved merge conflicts in AGENTS guidelines, timeline, and narrative map.
- Verified dataset references remained intact and removed obsolete market analysis script.
