import json
import re


def extract_action(response: str) -> str | None:
    match = re.search(r"^Action:\s*(.+)$", response, re.MULTILINE | re.IGNORECASE)
    return match.group(1).strip() if match else None


def extract_action_input(response: str) -> dict:
    match = re.search(r"^Action Input:\s*(.+)$", response, re.MULTILINE | re.IGNORECASE)
    if not match:
        return {}
    try:
        data = json.loads(match.group(1).strip())
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def extract_final_answer(response: str) -> str | None:
    match = re.search(r"^Final Answer:\s*(.+)$", response, re.MULTILINE | re.IGNORECASE | re.DOTALL)
    return match.group(1).strip() if match else None
