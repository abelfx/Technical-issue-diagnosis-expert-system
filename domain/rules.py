RULES = [
    # --- LEVEL 1: CRITICAL HARDWARE (Priority 1) ---
    {
        "conditions": ["pc_no_power", "no_fan"],
        "conclusion": "total_psu_failure",
        "confidence": 0.98,
        "priority": 1
    },
    {
        "conditions": ["overheating", "sudden_shutdown"],
        "conclusion": "thermal_throttling_shutdown",
        "confidence": 0.95,
        "priority": 1
    },
    {
        "conditions": ["loud_clicking_noise", "slow_performance"],
        "conclusion": "hdd_mechanical_failure",
        "confidence": 0.95,
        "priority": 1
    },
    {
        "conditions": ["blue_screen_of_death", "new_ram_installed"],
        "conclusion": "ram_compatibility_issue",
        "confidence": 0.85,
        "priority": 1
    },
    {
        "conditions": ["artifacting_on_screen", "gpu_overheating"],
        "conclusion": "gpu_hardware_failure",
        "confidence": 0.90,
        "priority": 1
    },

    # --- LEVEL 2: OS & BOOT ISSUES (Priority 2) ---
    {
        "conditions": ["stuck_on_bios", "boot_device_not_found"],
        "conclusion": "boot_loader_corruption",
        "confidence": 0.85,
        "priority": 2
    },
    {
        "conditions": ["slow_performance", "disk_active_100"],
        "conclusion": "windows_indexing_overload",
        "confidence": 0.70,
        "priority": 2
    },
    {
        "conditions": ["pc_turns_on", "no_display", "beep_codes_heard"],
        "conclusion": "post_error_ram_vga",
        "confidence": 0.80,
        "priority": 2
    },
    {
        "conditions": ["files_encrypted", "unknown_extension_added"],
        "conclusion": "ransomware_attack",
        "confidence": 0.99,
        "priority": 1  # Security is always high priority
    },
    {
        "conditions": ["windows_update_failing", "system_files_missing"],
        "conclusion": "os_integrity_corruption",
        "confidence": 0.85,
        "priority": 2
    },

    # --- LEVEL 3: NETWORKING & PERIPHERALS (Priority 3) ---
    {
        "conditions": ["wifi_not_working", "other_devices_work", "ethernet_works"],
        "conclusion": "wlan_card_failure",
        "confidence": 0.80,
        "priority": 3
    },
    {
        "conditions": ["limited_connectivity", "dns_probe_finished"],
        "conclusion": "dns_config_error",
        "confidence": 0.90,
        "priority": 3
    },
    {
        "conditions": ["usb_not_recognized", "works_in_other_port"],
        "conclusion": "usb_port_physical_damage",
        "confidence": 0.75,
        "priority": 3
    },
    {
        "conditions": ["high_ping_in_games", "wifi_connection"],
        "conclusion": "signal_interference",
        "confidence": 0.70,
        "priority": 3
    }
]