"""
MCP Server for Cutaneous Cold-Induced Vasodilation (CIVD) Skill.
Exposes JSON-RPC Model Context Protocol tools for evaluating Lewis hunting reaction, rewarming amplitude, and cold tolerance scores.
"""

import sys
import json
from typing import Dict, Any
from client import CutaneousCIVDClient


def get_tools_manifest() -> Dict[str, Any]:
    return {
        "tools": [
            {
                "name": "evaluate_civd",
                "description": "Calculates Lewis Cold-Induced Vasodilation (CIVD) hunting reaction, rewarming amplitude (deg C), onset time, and cold resilience score.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "baseline_temp_c": {
                            "type": "number",
                            "description": "Baseline skin surface temperature in degrees Celsius (e.g. 33.5 deg C)."
                        },
                        "minimum_temp_c": {
                            "type": "number",
                            "description": "Nadir temperature reached during cold immersion in degrees Celsius (e.g. 9.5 deg C)."
                        },
                        "peak_rewarming_temp_c": {
                            "type": "number",
                            "description": "Peak skin temperature reached during the first rewarming cycle in degrees Celsius (e.g. 14.8 deg C)."
                        },
                        "onset_time_min": {
                            "type": "number",
                            "description": "Time elapsed from start of cold immersion to the onset of rewarming in minutes (e.g. 6.5 min, normative 5-10 min)."
                        },
                        "duration_min": {
                            "type": "number",
                            "description": "Total duration of cold challenge test in minutes (default: 30.0 min).",
                            "default": 30.0
                        },
                        "immersion_water_temp_c": {
                            "type": "number",
                            "description": "Temperature of cold immersion bath in degrees Celsius (default: 5.0 deg C).",
                            "default": 5.0
                        }
                    },
                    "required": ["baseline_temp_c", "minimum_temp_c", "peak_rewarming_temp_c", "onset_time_min"]
                }
            }
        ]
    }


def handle_request(client: CutaneousCIVDClient, req: Dict[str, Any]) -> Dict[str, Any]:
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": get_tools_manifest()
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})

        if name == "evaluate_civd":
            res = client.evaluate_civd(
                baseline_temp_c=float(args.get("baseline_temp_c", 33.0)),
                minimum_temp_c=float(args.get("minimum_temp_c", 10.0)),
                peak_rewarming_temp_c=float(args.get("peak_rewarming_temp_c", 14.5)),
                onset_time_min=float(args.get("onset_time_min", 7.0)),
                duration_min=float(args.get("duration_min", 30.0)),
                immersion_water_temp_c=float(args.get("immersion_water_temp_c", 5.0))
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2)
                        }
                    ]
                }
            }
        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method not found: {name}"
                }
            }
    else:
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "error": {
                "code": -32600,
                "message": f"Invalid Request: Unsupported method {method}"
            }
        }


def main():
    client = CutaneousCIVDClient()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(client, req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_resp = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {
                    "code": -32700,
                    "message": f"Parse error or exception: {str(e)}"
                }
            }
            sys.stdout.write(json.dumps(err_resp) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
