# domain/rules.py

RULES = [
    {
        "conditions": ["pc_not_turning_on", "no_fan"],
        "conclusion": "power_supply_failure",
        "confidence": 0.9
    },
    {
        "conditions": ["pc_turns_on", "no_display"],
        "conclusion": "display_issue",
        "confidence": 0.85
    },
    {
        "conditions": ["overheating", "sudden_shutdown"],
        "conclusion": "cooling_problem",
        "confidence": 0.95
    },
]
