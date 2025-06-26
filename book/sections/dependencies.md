# Dependency Overview

The documentation hub relies on several core JGT packages listed in `requirements.txt`.
These packages provide market data processing, core utilities, machine learning,
and other functionality across the platform.

- **jgtutils** – Common utilities and configuration helpers used by all packages.
- **jgtcore** – Shared core libraries ensuring consistent functionality.
- **jgtpy** – Market data services and indicator calculations.
- **jgtml** – Machine learning models and signal detection routines.

Each package exposes a `llms.txt` file with additional details. Refer to those
files or run the package's CLI tools with `--help` for more information.
