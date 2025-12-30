# RULES = [
#     {
#         "conditions": ["pc_not_turning_on", "no_fan"],
#         "conclusion": "power_supply_failure",
#         "confidence": 0.9
#     },
#     {
#         "conditions": ["pc_turns_on", "no_display"],
#         "conclusion": "display_issue",
#         "confidence": 0.85
#     },
#     {
#         "conditions": ["overheating", "sudden_shutdown"],
#         "conclusion": "cooling_problem",
#         "confidence": 0.95
#     },
# ]

RULES = [
    # Power Logic
    {
        "conditions": ["pc_no_power", "no_fan"],
        "conclusion": "total_psu_failure",
        "confidence": 0.98
    },
    {
        "conditions": ["pc_no_power", "fan_spinning_high"],
        "conclusion": "motherboard_short_circuit",
        "confidence": 0.75
    },
    # Storage & Performance
    {
        "conditions": ["slow_performance", "loud_clicking_noise"],
        "conclusion": "hdd_mechanical_failure",
        "confidence": 0.95
    },
    {
        "conditions": ["slow_performance", "disk_active_100", "windows_update_failing"],
        "conclusion": "os_disk_corruption",
        "confidence": 0.80
    },
    # Networking
    {
        "conditions": ["wifi_not_working", "other_devices_work", "ethernet_works"],
        "conclusion": "network_card_driver_issue",
        "confidence": 0.85
    },
    # Security
    {
        "conditions": ["unknown_popup_ads", "browser_redirects", "high_cpu_usage"],
        "conclusion": "adware_malware_infection",
        "confidence": 0.90
    }
]