#!/usr/bin/env python3
"""
Create public-safe copies of n8n workflow JSON exports.

Usage:
    python sanitize_n8n_export.py input.json output.json

This script never modifies the source file.
"""
import copy
import json
import sys

def sanitize(obj):
    if isinstance(obj, dict):
        out = {}
        for key, value in obj.items():
            if key in {"credentials", "webhookId", "versionId", "meta", "pinData"}:
                continue
            if key == "cachedResultUrl":
                continue

            if key == "dataTableId" and isinstance(value, dict):
                value = copy.deepcopy(value)
                value["value"] = "YOUR_DATA_TABLE_ID"
                value.pop("cachedResultUrl", None)

            if key == "workflowId" and isinstance(value, dict):
                value = copy.deepcopy(value)
                value["value"] = "YOUR_REQUEST_ASSESSMENT_CORE_WORKFLOW_ID"
                value.pop("cachedResultUrl", None)

            out[key] = sanitize(value)
        return out

    if isinstance(obj, list):
        return [sanitize(x) for x in obj]

    return obj

if len(sys.argv) != 3:
    raise SystemExit("Usage: python sanitize_n8n_export.py input.json output.json")

src, dst = sys.argv[1], sys.argv[2]

with open(src, "r", encoding="utf-8") as f:
    data = json.load(f)

clean = sanitize(data)
clean.pop("id", None)

with open(dst, "w", encoding="utf-8") as f:
    json.dump(clean, f, indent=2, ensure_ascii=False)

print(f"Wrote sanitized copy: {dst}")
