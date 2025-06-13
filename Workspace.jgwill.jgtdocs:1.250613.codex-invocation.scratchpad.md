# Workspace.jgwill.jgtdocs:1.250613.codex-invocation.scratchpad

```
🧪 Codex Invocation Scratchpad – Updated Notes

Desires forming:
- Implement FDB Scanner to use real signal detection (no simulation)
- Connect `intent_spec.py` to enhanced parsing logic
- Validate signal output using intent alignment and quality scoring
- Enable CLI invocation via `jgtagenticcli.py`
- Represent MFI signals visually (color-coded, glyph-based)
- Support recommendation generation from scanner phase
- Align signal output with external strategy structure (YAML)

📄 Verbatim Test Strategy Content:
```
instruments:
- EUR/USD
risk_management:
  max_risk_percent: 2.0
  position_size: 1
  target_rr: 2.0
signals:
- description: Alligator-based signal from observation
  jgtml_components:
    alligator_state: TideAlligatorAnalysis.mouth_opening
  name: alligator_signal
- description: Multi-indicator confluence
  jgtml_components:
    alligator_state: TideAlligatorAnalysis.mouth_opening
    fractal_analysis: jgtpy.fractal_detection
    momentum: jgtpy.ao_acceleration
  name: confluence_signal
source_observation: Multi-timeframe alligator confluence with momentum confirmation
strategy_intent: 'Analysis based on observation: Multi-timeframe alligator confluence with momentum confirmation...'
timeframes:
- H4
- H1
- m15
```

📍 Signal Pattern Module: Alligator Illusion Detection

Name: Alligator Illusion Detection  
Intent: Detect false-positive trade entries when lower timeframes appear to trend but contradict broader market structure.

Scope of Awareness:
- Visual trigger begins on m15 (movement appears promising).
- Confirm alignment not only with H1 and H4, but escalate validation to D1, W1, and MN1 (supercycle structure).
- These higher timeframes determine campaign potential—short vs. long term engagement.

Components to Detect:
- Alligator mouth status on each timeframe.
- How long the mouth has been closed (“hunger” of the Alligator).
- Angulation: price diverging sharply from Alligator’s balance lines.
- Elliott Wave Position: current wave vs. alternate count.
  - Determine whether current wave is nearing end.
  - Recognize final wave formations hidden in smaller trends.

Signal Type:
- Visual overlay + verbal alert if mismatch is detected.
- Guidance on campaign duration based on supercycle alignment.
```
