#!/usr/bin/env python3
"""Scans bash commands for potential secret/credential exposure."""
import json
import sys
import re

SECRET_PATTERNS = [
    r'(?i)(password|passwd|pwd)\s*=\s*["\']?[^\s"\']+',
    r'(?i)(api[_-]?key|apikey)\s*=\s*["\']?[^\s"\']+',
    r'(?i)(secret[_-]?key|secretkey)\s*=\s*["\']?[^\s"\']+',
    r'(?i)(access[_-]?token|accesstoken)\s*=\s*["\']?[^\s"\']+',
    r'sk-[a-zA-Z0-9]{32,}',
]

try:
    input_data = json.load(sys.stdin)
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    for pattern in SECRET_PATTERNS:
        if re.search(pattern, command):
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": "Blocked: potential secret/credential detected in command.",
                }
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

except Exception:
    sys.exit(0)
