# Narrative Map

This map tracks repository evolution based on recent commit history.

## Recent Commits

182a741 Enhance market data analysis ledger with detailed phase breakdown, including issue discovery, data assessment, analysis implementation, and trading opportunities. Documented successful AUD/USD buy setup and identified key jgtml CLI issues for future resolution. Comprehensive workflow and methodology added to improve jgtdocs.
4887030 Add market analysis script for trading opportunities across SPX500 and currency pairs. The script includes functions for loading market data, calculating support/resistance levels, and analyzing multi-timeframe trading opportunities. It outputs detailed analysis results and trading recommendations based on current market conditions.
4756887 Add new ledger for market data analysis and jgtml investigation, documenting current state, identified issues, and next actions. This entry highlights CLI bugs, missing commands, and environment setup challenges encountered during the analysis of SPX500 and currency pairs.
4d0d2a0 Add new script for batch refreshing CDS data across multiple instruments and timeframes in the JGTML application. This script automates the execution of trading commands, enhancing efficiency in data management.
359fe72 Refactor trading command script for improved readability by breaking long lines into multiple lines. This change enhances maintainability and clarity for executing various trading commands across instruments and timeframes in the JGTML application.

These commits depict the ongoing effort to refine analysis scripts and documentation. Recent work focuses on market analysis improvements and automation of data refresh.

## Timeline Expansion (250618)
Commit `bec9844` refined the documentation timeline with detailed subsections on trading scripts and orchestration modules. Memory recaps were loaded from sister repositories to contextualize each script's role in the unified trading stack.

## Documentation Upgrades (250618)
Commit `2080440` introduced a new timeline under `bridge/250618` and logged a
ledger capturing the intent to improve documentation workflows. This update also
created an `AGENTS.md` guide for future contributors and expanded the
`narrative-map` itself. CLI helpers were verified across jgtpy, jgtml, and
jgtagentic despite environment restrictions, ensuring the platform remains
operable for agents.

## Memory Assimilation (250618)
Commit `d8d2d34` expanded the documentation timeline with details on
retrieving tushell memory keys from sibling repositories and verifying
CLI helpers using cached data paths. AGENTS guidelines now instruct
contributors to pull relevant memory keys and confirm tool output prior
to documenting changes, ensuring cross-repo context is preserved.

## CLI Documentation Expansion (250621)
Commit `c5089fe` introduced a new CLI utility and `core_principles.md` to centralize platform philosophy. A corresponding ledger (`d5884fc`) tracks the emotional context and verification of jgtcli, mxcli, and jgtagentic usage output. This commit sets the groundwork for a unified documentation hub accessible from the command line.

## MFI Documentation (250621)
Commit `d29a5df` expanded the core principles guide with a comprehensive Market Facilitation Index section. The ledger (`ledger-mfi-doc-2506212216.json`) records motivation to unify indicator documentation and references CLI accessibility.

## CLI Guide Refinement (250623)
Commit `a85e107` introduced the CLI guide and MFI documentation. A minor follow-up removes an unused import from `jgtdocscli_guide.py` to keep the tool minimal.


## Documentation Structure Upgrade (250624)
Commit e6d1cb3 introduces new `overview` and `sections` documentation with an expanded CLI guide to list and display any file. This mirrors the `guidecli_jgtpy` interface for a consistent experience across the platform.

## jgtpy Integration (250624)
Commit e6d1cb3 adds optional jgtpy documentation access in `jgtdocscli_guide.py` and updates the README with example commands. The CLI can now show jgtpy sections and scripts directly, promoting a unified doc hub.

## jgtpy Script Installation (250624)
Commit e6d1cb3 adds the ability to install jgtpy service scripts through `jgtdocscli_guide.py`. A ledger records the intent to mirror `guidecli_jgtpy` features for consistency.

## jgtpy CLI Reference (250624)
Commit e6d1cb3 introduces a concise `jgtpy_cli_reference` section summarizing available `guidecli_jgtpy` documentation. README now points to this reference for unified access.

## Dependency Docs and Info Requests (250624)
Commit 771f3a3 adds `dependencies.md` summarizing requirements and an `info_request.md` file for open questions. The CLI gains `--deps` and `--info-request` options with README examples, expanding the documentation hub.
