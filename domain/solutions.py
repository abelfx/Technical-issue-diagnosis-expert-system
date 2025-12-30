SOLUTIONS = {
# --- LEVEL 1: CRITICAL HARDWARE ---
"total_psu_failure": (
"1. Check if the power cable is firmly seated and the wall outlet works.\n"
"2. Perform a 'Paperclip Test' on the PSU to check for fan operation.\n"
"3. Test with a known working power supply; replace the PSU if it fails."
),
"thermal_throttling_shutdown": (
"1. Immediately power down and let the system cool.\n"
"2. Clean dust from CPU/GPU heatsinks and all case fans.\n"
"3. Re-apply thermal paste on the CPU and ensure all fans are spinning."
),
"hdd_mechanical_failure": (
"1. IMMEDIATE: Backup critical files if the drive is still readable.\n"
"2. Do not run intensive tasks or attempt repairs on the failing drive.\n"
"3. Replace the clicking drive with an SSD or new HDD."
),
"ram_compatibility_issue": (
"1. Power down and reseat the new RAM modules firmly.\n"
"2. Test each RAM stick individually in the primary DIMM slot.\n"
"3. Check motherboard QVL list and update BIOS for better compatibility."
),
"gpu_hardware_failure": (
"1. Update GPU drivers to the latest stable version.\n"
"2. Clean the GPU heatsink and ensure fans are working.\n"
"3. Test the GPU in another system; if artifacting persists, replace GPU."
),
"ransomware_attack": (
"1. Disconnect from network immediately to prevent spread.\n"
"2. Do NOT pay the ransom. Use ransomware decryption tools (if available).\n"
"3. Restore from a clean backup or perform a complete OS reinstall."
),
# --- LEVEL 2: OS & BOOT ISSUES ---**
"boot_loader_corruption": (
    "1. Enter BIOS/UEFI and verify the boot order.\n"
    "2. Use Windows Recovery to run 'bootrec /fixmbr' and 'bootrec /rebuildbcd'.\n"
    "3. If unsuccessful, perform a Windows repair installation."
),
"windows_indexing_overload": (
    "1. Open Task Manager and check which process is using disk.\n"
    "2. Temporarily disable Windows Search service.\n"
    "3. Add exclusions in Windows Defender for large directories if scanning."
),
"post_error_ram_vga": (
    "1. Note the beep code pattern and check motherboard manual.\n"
    "2. Reseat RAM and graphics card, clearing CMOS if needed.\n"
    "3. Test with minimal hardware: one RAM stick, onboard graphics if available."
),
"os_integrity_corruption": (
    "1. Run Command Prompt as Admin: 'sfc /scannow' to repair system files.\n"
    "2. Run 'DISM /Online /Cleanup-Image /RestoreHealth'.\n"
    "3. If issues persist, perform a Windows reset keeping personal files."
),

# --- LEVEL 3: NETWORKING & PERIPHERALS ---**
"wlan_card_failure": (
    "1. Toggle Airplane mode on/off and restart the router.\n"
    "2. Reinstall WLAN drivers from Device Manager.\n"
    "3. Test with a USB WiFi adapter; if it works, replace internal WLAN card."
),
"dns_config_error": (
    "1. Flush DNS cache: Open Command Prompt as Admin and run 'ipconfig /flushdns'.\n"
    "2. Change DNS to Google (8.8.8.8) or Cloudflare (1.1.1.1).\n"
    "3. Reset TCP/IP stack with 'netsh int ip reset' and restart."
),
"usb_port_physical_damage": (
    "1. Inspect the USB port for bent pins or debris; clean with compressed air.\n"
    "2. Update USB controller drivers from Device Manager.\n"
    "3. If physical damage is visible, the port may need motherboard repair."
),
"signal_interference": (
    "1. Move the router away from appliances like microwaves and cordless phones.\n"
    "2. Change WiFi channel to 1, 6, or 11 to avoid congestion.\n"
    "3. Use 5GHz band if available, or consider Powerline adapters for gaming."
),

# --- ADDITIONAL COMMON ISSUES (for completeness) ---**
"motherboard_short_circuit": (
    "1. Power down and disconnect all components.\n"
    "2. Inspect motherboard for 'blown' or bulging capacitors.\n"
    "3. Test the system outside of the case to rule out a grounding short."
),
"os_disk_corruption": (
    "1. Open Command Prompt as Admin and run 'sfc /scannow'.\n"
    "2. Run 'chkdsk /f' to repair file system errors.\n"
    "3. If issues persist, perform a Windows 'Cloud Reset' or clean install."
),
"cooling_problem": (
    "1. Power off and use compressed air to clean dust from fans/heatsinks.\n"
    "2. Remove the CPU cooler and re-apply high-quality thermal paste.\n"
    "3. Ensure the PC has at least 4 inches of clearance for airflow."
),
"network_card_driver_issue": (
    "1. Go to Device Manager, right-click the Network Adapter, and select 'Uninstall'.\n"
    "2. Restart the PC; Windows will auto-reinstall the driver.\n"
    "3. Download the latest drivers from the manufacturer's website."
),
"adware_malware_infection": (
    "1. Disconnect from internet and boot into 'Safe Mode with Networking'.\n"
    "2. Run a full scan with Malwarebytes or Windows Defender Offline.\n"
    "3. Check 'Add/Remove Programs' for recently installed suspicious software."
) 
}