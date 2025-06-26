# JGT Platform Documentation Hub

## Overview

## Core Principles
See `book/core_principles.md` for a detailed explanation of the guiding principles and the Market Facilitation Index (MFI). You can also view them via the CLI:

```bash
python -m jgtdocs.jgtdocscli_guide --principles
python -m jgtdocs.jgtdocscli_guide --list       # list all docs
python -m jgtdocs.jgtdocscli_guide --doc overview.md
python -m jgtdocs.jgtdocscli_guide --jgtpy-list  # list jgtpy sections
python -m jgtdocs.jgtdocscli_guide --jgtpy-section idscli  # show a jgtpy section
python -m jgtdocs.jgtdocscli_guide --jgtpy-install-scripts path/to/bin --jgtpy-overwrite
python -m jgtdocs.jgtdocscli_guide --doc sections/jgtpy_cli_reference.md  # summary of guidecli_jgtpy
python -m jgtdocs.jgtdocscli_guide --deps  # show dependency overview
python -m jgtdocs.jgtdocscli_guide --info-request  # view pending documentation questions
```


This repository serves as the central documentation hub for Jean Guillaume's Trading (JGT) platform - a comprehensive algorithmic trading system designed for autonomous signal detection, multi-timeframe analysis, and intelligent trade execution.

## Platform Architecture

The JGT platform consists of interconnected packages forming a complete trading ecosystem:

### 📊 Data & Analytics Layer
- **[jgtpy](https://github.com/jgwill/jgtpy)** - Market data services and core indicator calculations
- **[jgtcore](https://github.com/jgwill/jgtcore)** - Shared libraries and core functionality

### 🤖 Machine Learning & Signal Detection
- **[jgtml](https://github.com/jgwill/jgtml)** - ML models, signal detection, and pattern intelligence
- **[jgtapy](https://github.com/jgwill/jgtapy)** - Technical analysis indicators

### 🔗 Trading Execution & Connectivity
- **[jgtfxcon](https://github.com/jgwill/jgtfxcon)** - FX connectivity and order management
- **[jgtutils](https://github.com/jgwill/jgtutils)** - Platform utilities and configuration

### 🧠 Autonomous Trading Intelligence
- **[jgtagentic](https://github.com/jgwill/jgtagentic)** - Agentic trading orchestration and campaign management

## Key Capabilities

### Signal Detection System
- **FDB (Fractal Divergent Bar)** analysis for precise entry signals
- **Multi-degree Alligator** analysis (Regular/Big/Tide timeframes)
- **Five Dimensions Confluence** validation across multiple indicators
- **Pattern intelligence** learning and adaptation

### Multi-Timeframe Analysis
- **Hierarchical timeframe** analysis from monthly to minute charts
- **Higher timeframe bias** integration for trend alignment
- **Confluence validation** across timeframe dimensions
- **Automated signal scanning** across multiple instruments

### Autonomous Execution
- **Risk-managed order sizing** based on signal quality
- **Stop loss management** using technical levels
- **Campaign orchestration** for multi-instrument strategies
- **Performance tracking** and pattern learning

## Data Processing Pipeline

```
Market Data (PDS) → Technical Indicators (IDS) → Chart Analysis (CDS/ADS) → 
Feature Engineering (TTF) → Matrix Analysis (MX) → Signal Detection → Order Execution
```

## For Developers & LLMs

### Documentation Access
- **Central Hub**: [llms.txt](./llms.txt) - Complete platform overview for LLMs
- **Package-Specific**: Each package has dedicated llms.txt for focused documentation
- **Pattern**: `https://<package>.jgwill.com/llms.txt` for published documentation

### Development Philosophy
- **Intent-Driven Development** - Trading strategies specified in natural language
- **Pattern Intelligence** - Continuous learning from signal performance
- **Multi-Timeframe Confluence** - Systematic validation across timeframes
- **Autonomous Execution** - Minimal human intervention once configured

### Current Development State
- **Production**: Core data services and signal detection
- **Active Development**: Pattern intelligence and signal quality prediction
- **Refactoring**: jgtutils → jgtcore migration for better separation of concerns
- **Innovation**: Intent-driven trading specification language (SpecLang)

## Getting Started

### For Traders
1. Install core packages: `pip install jgtpy jgtml jgtfxcon`
2. Configure market data connection
3. Run signal scanner: `jgtapp fdbscan`
4. Review generated trading signals

### For Developers
1. Review platform architecture in [llms.txt](./llms.txt)
2. Explore package-specific documentation
3. Understand data pipeline and signal detection logic
4. Contribute to pattern intelligence development

### For LLMs
- Start with [llms.txt](./llms.txt) for complete platform context
- Reference package-specific llms.txt files for detailed component information
- Use provided examples and CLI patterns for implementation guidance
- See `book/sections/info_request.md` for open questions and future documentation goals

## Technical Specifications

### Supported Markets
- **Forex**: Major and minor currency pairs
- **Indices**: SPX500, AUS200, and other major indices  
- **Commodities**: XAU/USD and other precious metals

### Timeframes
- **Long-term**: M1 (Monthly), W1 (Weekly)
- **Medium-term**: D1 (Daily), H4, H8 (Multi-hour)
- **Short-term**: H1, H2, H3 (Hourly)
- **Intraday**: m15, m5, m1 (Minutes)

### Signal Types
- **Entry Signals**: FDB breakouts, Alligator confluences
- **Exit Signals**: Technical stop levels, pattern completions
- **Risk Management**: Dynamic position sizing, stop loss management

## Platform Benefits

### For Individual Traders
- **Automated Signal Detection** - No manual chart watching required
- **Multi-Market Coverage** - Simultaneous analysis across instruments
- **Risk Management** - Built-in position sizing and stop loss logic
- **Performance Tracking** - Continuous improvement through pattern learning

### For Trading Teams
- **Systematic Approach** - Consistent signal detection methodology
- **Scalable Analysis** - Handle multiple strategies simultaneously
- **Knowledge Retention** - Pattern intelligence preserves team learning
- **Campaign Management** - Coordinate complex multi-instrument strategies

### For Algorithm Developers
- **Modular Architecture** - Clear separation of concerns across packages
- **Extensible Framework** - Add new indicators and signal types
- **Pattern Learning** - Built-in machine learning for signal improvement
- **Complete Testing** - Backtesting and forward testing capabilities

---

## Support & Resources

- **Documentation**: Package-specific llms.txt files
- **Examples**: Working implementations in each package
- **Community**: GitHub discussions and issue tracking
- **Development**: Continuous integration and testing

*The JGT platform represents a comprehensive approach to algorithmic trading, combining traditional technical analysis with modern machine learning and autonomous execution capabilities.*
