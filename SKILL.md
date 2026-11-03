---
name: genpark-personal-agent-cutaneous-cold-induced-vasodilation-civd-skill
version: 1.0.0
description: Zero-dependency sovereign personal agent skill for calculating Cutaneous Cold-Induced Vasodilation (CIVD), Lewis hunting reaction, rewarming amplitude, and peripheral cold injury resilience.
author: AlphaPark Inc.
license: Apache-2.0
tags:
  - personal-agent
  - ai-agent
  - openclaw
  - genpark
  - mcp
  - mcp-server
  - model-context-protocol
  - python
  - zero-dependency
  - wellness
  - productivity
  - production-ready
metadata:
  openclaw_compatible: true
  hermes_compatible: true
  zero_dependency: true
---

# Cutaneous Cold-Induced Vasodilation (CIVD) Skill

A sovereign personal agent capability for assessing peripheral microvascular regulation, arteriovenous anastomosis (AVA) vasomotor cycling, the Lewis "hunting reaction", and cold tolerance.

## Core Capabilities
- **Lewis Hunting Reaction Profiling**: Quantifies minimum immersion temperature ($T_{min}$), onset latency ($t_{onset}$ in min), and peak rewarming amplitude ($T_{amp} = T_{peak} - T_{min}$).
- **Hunting Index Formulation**: Computes dynamic thermal recovery rate ($HI = \Delta T / t_{onset}$ in $\text{deg C / min}$).
- **Non-Freezing Cold Injury & Raynaud's Screening**: Detects prolonged alpha-2 adrenergic vasospasm and absence of protective axon reflex rewarming.
- **Thermal Ergonomic Guidance**: Prescribes ambient workstation temperatures, insulated footwear/glove requirements, and cold exposure limits.

## Fast Invocation
```python
from client import CutaneousCIVDClient

client = CutaneousCIVDClient()
res = client.evaluate_civd(
    baseline_temp_c=33.2,
    minimum_temp_c=9.2,
    peak_rewarming_temp_c=15.0,
    onset_time_min=6.2
)
print("Rebound Amplitude:", res["rebound_amplitude_deg_c"], "deg C")
print("Cold Resilience Score:", res["cold_resilience_score"], "/ 100")
```
