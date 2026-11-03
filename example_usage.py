"""
Example Usage: Cutaneous Cold-Induced Vasodilation (CIVD) & Lewis Hunting Reaction.
Demonstrates zero-dependency calculation of CIVD rewarming amplitude, hunting index, and peripheral cold tolerance scoring.
"""

from client import CutaneousCIVDClient


def main():
    client = CutaneousCIVDClient()
    print("=== Cutaneous Cold-Induced Vasodilation (CIVD) Demo ===")

    # Test Case 1: Healthy vigorous hunting reaction (high cold tolerance)
    res1 = client.evaluate_civd(
        baseline_temp_c=33.2,
        minimum_temp_c=9.2,
        peak_rewarming_temp_c=15.0,
        onset_time_min=6.2,
        duration_min=30.0,
        immersion_water_temp_c=5.0
    )
    print("\nTest Case 1: Robust Hunting Reaction (High Cold Tolerance)")
    print(f"  Baseline: {res1['baseline_temp_c']} deg C | Nadir Tmin: {res1['minimum_temp_c']} deg C")
    print(f"  Peak Rewarming: {res1['peak_rewarming_temp_c']} deg C | Rebound: {res1['rebound_amplitude_deg_c']} deg C")
    print(f"  Onset Time: {res1['onset_time_min']} min | Hunting Index: {res1['hunting_index']} deg C/min")
    print(f"  Cold Resilience Score: {res1['cold_resilience_score']} / 100")
    print(f"  Classification: {res1['classification']}")
    print(f"  Physiological Interpretation: {res1['physiological_interpretation']}")
    print(f"  Actionable Guidance: {res1['actionable_guidance']}")

    # Test Case 2: Blunted hunting reaction (cold intolerance / Raynaud's risk)
    res2 = client.evaluate_civd(
        baseline_temp_c=31.5,
        minimum_temp_c=6.8,
        peak_rewarming_temp_c=7.6,
        onset_time_min=18.5,
        duration_min=30.0,
        immersion_water_temp_c=5.0
    )
    print("\nTest Case 2: Blunted CIVD Response (Cold Intolerance Pattern)")
    print(f"  Rebound: {res2['rebound_amplitude_deg_c']} deg C | Onset Time: {res2['onset_time_min']} min")
    print(f"  Cold Resilience Score: {res2['cold_resilience_score']} / 100")
    print(f"  Classification: {res2['classification']}")
    print(f"  Actionable Guidance: {res2['actionable_guidance']}")


if __name__ == "__main__":
    main()
