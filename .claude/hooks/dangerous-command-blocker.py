#!/usr/bin/env python3
"""Blocks dangerous shell commands before execution."""
import json
import sys

DANGEROUS_PATTERNS = [
    "rm -rf /",
    "rm -rf ~",
    "dd if=/dev/zero",
    "mkfs",
    "> /dev/sda",
    ":(){ :|:& };:",
    "chmod -R 777 /",
    "chown -R",
    "shutdown",
    "halt",
    "reboot",
    "curl | bash",
    "curl | sh",
    "wget | bash",
    "wget | sh",
]

try:
    input_data = json.load(sys.stdin)
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    for pattern in DANGEROUS_PATTERNS:
        if pattern in command:
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"Blocked: dangerous pattern detected: '{pattern}'",
                }
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

except Exception:
    sys.exit(0)
