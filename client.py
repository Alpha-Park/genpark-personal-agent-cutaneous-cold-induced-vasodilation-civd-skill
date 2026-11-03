"""
Cutaneous Cold-Induced Vasodilation (CIVD) & Lewis Hunting Reaction Engine.
Provides deterministic, zero-dependency modeling of peripheral microvascular cold response,
onset time of rewarming (min), temperature rebound amplitude (deg C), and cold injury resilience.
"""

from typing import Dict, Any, List, Optional


class CutaneousCIVDClient:
    """
    Deterministic client for calculating Cold-Induced Vasodilation (CIVD) parameters.
    Assesses peripheral arteriovenous anastomoses (AVAs), sensory axon reflex neuropeptide release,
    sympathetic vasoconstrictor tone modulation, and non-freezing cold injury (NFCI) vulnerability.
    """

    def __init__(self):
        pass

    def evaluate_civd(
        self,
        baseline_temp_c: float,
        minimum_temp_c: float,
        peak_rewarming_temp_c: float,
        onset_time_min: float,
        duration_min: float = 30.0,
        immersion_water_temp_c: float = 5.0
    ) -> Dict[str, Any]:
        """
        Calculates Lewis hunting reaction parameters and cold resilience score.
        Normative values (during 5 deg C local immersion):
        - Minimum Temperature (Tmin): 7.0 - 12.0 deg C
        - Onset Time of Rewarming (tonset): 5.0 - 10.0 min (< 8 min is robust)
        - Rebound Amplitude (Tpeak - Tmin): 2.5 - 6.5 deg C
        - Hunting Index = (Tpeak - Tmin) / tonset
        """
        if baseline_temp_c <= 0 or minimum_temp_c <= 0 or peak_rewarming_temp_c <= 0:
            return {"error": "Temperatures must be strictly positive"}
        if minimum_temp_c > baseline_temp_c:
            return {"error": "Minimum temperature cannot exceed baseline skin temperature"}
        if peak_rewarming_temp_c < minimum_temp_c:
            return {"error": "Peak rewarming temperature cannot be lower than minimum temperature"}
        if onset_time_min <= 0:
            return {"error": "Onset time must be strictly positive"}

        # 1. Temperature Rebound Amplitude (deg C)
        rebound_amp_deg_c = round(peak_rewarming_temp_c - minimum_temp_c, 2)

        # 2. Total Cold Drop (deg C)
        cold_drop_deg_c = round(baseline_temp_c - minimum_temp_c, 2)

        # 3. Lewis Hunting Index (deg C / min)
        hunting_index = round(rebound_amp_deg_c / onset_time_min, 3)

        # 4. Cold Resilience Score (0 - 100)
        score = 80.0
        if onset_time_min <= 7.5:
            score += 10.0
        elif onset_time_min <= 10.5:
            score += 5.0
        elif onset_time_min > 16.0:
            score -= 25.0
        elif onset_time_min > 12.5:
            score -= 12.0

        if rebound_amp_deg_c >= 3.5:
            score += 10.0
        elif rebound_amp_deg_c >= 2.2:
            score += 5.0
        elif rebound_amp_deg_c < 1.0:
            score -= 25.0  # Absent hunting reaction
        elif rebound_amp_deg_c < 1.8:
            score -= 12.0

        civd_score = round(min(100.0, max(5.0, score)), 1)

        if civd_score >= 85.0 and onset_time_min <= 9.0 and rebound_amp_deg_c >= 2.5:
            tier = "OPTIMAL_CIVD_COLD_HUNTING_RESPONSE"
            interp = f"Rapid cold-induced vasodilation onset ({onset_time_min} min) and vigorous rewarming amplitude ({rebound_amp_deg_c} deg C, Hunting Index {hunting_index}); robust AVA axon reflex."
            guidance = "Superior peripheral thermal tolerance. Arteriovenous anastomoses periodically open to defend digital tissue from hypothermic injury."
        elif rebound_amp_deg_c < 1.2 or onset_time_min > 16.0:
            tier = "BLUNTED_CIVD_COLD_INTOLERANCE"
            interp = f"Severely delayed or absent hunting wave ({onset_time_min} min, Rebound {rebound_amp_deg_c} deg C); sustained vasoconstrictor spasm predisposing to chilblains or Raynaud's phenomenon."
            guidance = "Pronounced cold vulnerability. Use thermal gloves in temperatures below 10 deg C; avoid rapid hand cooling and nicotine exposure."
        else:
            tier = "MODERATE_PERIPHERAL_VASOMOTOR_RESPONSE"
            interp = f"Moderate CIVD hunting reaction (Onset {onset_time_min} min, Rebound {rebound_amp_deg_c} deg C, Drop {cold_drop_deg_c} deg C)."
            guidance = "Adequate cold tolerance. Maintain core body heat during outdoor cold immersion to support peripheral perfusion."

        return {
            "baseline_temp_c": baseline_temp_c,
            "minimum_temp_c": minimum_temp_c,
            "peak_rewarming_temp_c": peak_rewarming_temp_c,
            "onset_time_min": onset_time_min,
            "duration_min": duration_min,
            "rebound_amplitude_deg_c": rebound_amp_deg_c,
            "cold_drop_deg_c": cold_drop_deg_c,
            "hunting_index": hunting_index,
            "cold_resilience_score": civd_score,
            "classification": tier,
            "physiological_interpretation": interp,
            "actionable_guidance": guidance
        }
