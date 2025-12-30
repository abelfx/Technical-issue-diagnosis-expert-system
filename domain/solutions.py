# SOLUTIONS = {
#     "power_supply_failure": "Check or replace the power supply.",
#     "display_issue": "Check display cables or graphics card.",
#     "cooling_problem": "Clean fans and replace thermal paste."
# }

SOLUTIONS = {
    # Power & Boot Issues
    "total_psu_failure": (
        "1. Check if the power cable is firmly seated.\n"
        "2. Perform a 'Paperclip Test' on the PSU to check for life.\n"
        "3. Replace PSU if it fails to power the fan."
    ),
    "motherboard_short_circuit": (
        "1. Reseat RAM modules and CMOS battery.\n"
        "2. Inspect the motherboard for 'blown' or bulging capacitors.\n"
        "3. Test the system outside of the case to rule out a grounding short."
    ),
    
    # Storage & OS
    "hdd_mechanical_failure": (
        "1. IMMEDIATE: Backup critical files if the drive is still readable.\n"
        "2. Do not run intensive tasks.\n"
        "3. Replace the clicking drive with an SSD."
    ),
    "os_disk_corruption": (
        "1. Open Command Prompt as Admin and run 'sfc /scannow'.\n"
        "2. Run 'chkdsk /f' to repair file system errors.\n"
        "3. If issues persist, perform a Windows 'Cloud Reset'."
    ),
    
    # Cooling & Thermal
    "cooling_problem": (
        "1. Power off and use compressed air to clean dust from fans/heatsinks.\n"
        "2. Remove the CPU cooler and re-apply high-quality thermal paste.\n"
        "3. Ensure the PC has at least 4 inches of clearance for airflow."
    ),

    # Networking
    "network_card_driver_issue": (
        "1. Go to Device Manager, right-click the Network Adapter, and select 'Uninstall'.\n"
        "2. Restart the PC; Windows will auto-reinstall the driver.\n"
        "3. Download the latest drivers from the manufacturer's website using another PC."
    ),

    # Security & Malware
    "adware_malware_infection": (
        "1. Disconnect from the internet and boot into 'Safe Mode with Networking'.\n"
        "2. Run a full scan with Malwarebytes or Windows Defender Offline.\n"
        "3. Check 'Add/Remove Programs' for recently installed suspicious software."
    )
}