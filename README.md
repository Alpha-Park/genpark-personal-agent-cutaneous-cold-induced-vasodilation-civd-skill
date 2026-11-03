# Cutaneous Cold-Induced Vasodilation (CIVD) Skill

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/zero--dependencies-standard--lib-brightgreen.svg)](requirements.txt)
[![MCP Protocol Ready](https://img.shields.io/badge/mcp-protocol--ready-orange.svg)](mcp_server.py)
[![OpenClaw Certified](https://img.shields.io/badge/openclaw-certified-purple.svg)](SKILL.md)

Zero-dependency sovereign personal agent skill for non-invasive evaluation of Cutaneous Cold-Induced Vasodilation (CIVD), Lewis hunting reaction, rewarming amplitude, and peripheral cold injury resilience.

```mermaid
flowchart TD
    ColdChallenge["Local Cold Immersion Challenge (5 deg C)"] --> Vasoconstriction["Initial Sympathetic Vasoconstriction Nadir (Tmin)"]
    Vasoconstriction --> AxonReflex["Sensory Neuropeptide Release (CGRP / Substance P)"]
    AxonReflex --> AVADilation["Arteriovenous Anastomosis (AVA) Hunting Wave Onset (tonset)"]
    AVADilation --> Rewarming["Peak Periodic Rewarming Amplitude (Tpeak - Tmin)"]
    Rewarming --> CIVDScore["Peripheral Cold Tolerance & Vasomotor Resilience Engine"]
    CIVDScore --> Agent["OpenClaw / Hermes Personal Agent Thermal Prescriptions"]
```

## Features
- **Deterministic Math**: Pure Python standard library implementation with zero external dependencies.
- **Environmental Physiology Standards**: Implements validated equations for Lewis hunting reaction, rewarming amplitude, and hunting index.
- **Microvascular Cold Defense**: Early screening for digital vasospasm, Raynaud's vulnerability, and cold injury predisposition.
- **Model Context Protocol (MCP)**: Native JSON-RPC tool integration for LLMs and autonomous agents.

## Quickstart

```python
from client import CutaneousCIVDClient

client = CutaneousCIVDClient()
result = client.evaluate_civd(
    baseline_temp_c=33.2,
    minimum_temp_c=9.2,
    peak_rewarming_temp_c=15.0,
    onset_time_min=6.2
)
print("Rebound Amplitude:", result["rebound_amplitude_deg_c"], "deg C")
print("Cold Resilience Score:", result["cold_resilience_score"])
print("Classification:", result["classification"])
```

## License
Apache-2.0
