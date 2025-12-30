# FACTS = [
#     "pc_not_turning_on",
#     "no_fan",
#     "pc_turns_on",
#     "slow_performance",
#     "high_cpu_usage",
#     "overheating",
#     "sudden_shutdown",
#     "wifi_not_working",
#     "other_devices_work"
# ]

FACTS = [
    # Power & Boot
    "pc_no_power", "fan_spinning_high", "beep_codes_heard", "stuck_on_bios", 
    "blue_screen_of_death", "boot_device_not_found",
    
    # Performance & Thermal
    "slow_performance", "high_cpu_usage", "high_ram_usage", "overheating", 
    "sudden_shutdown", "disk_active_100", "loud_clicking_noise",
    
    # Connectivity
    "wifi_not_working", "other_devices_work", "ethernet_works", 
    "limited_connectivity", "dns_probe_finished",
    
    # Software & Security
    "unknown_popup_ads", "files_encrypted", "browser_redirects", 
    "windows_update_failing", "driver_error_icon"
]