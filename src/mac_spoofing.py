import os
import re
from util import print_feature_header
from scapy.all import RandMAC
from time import sleep

# Get the current MAC address.
def get_current_mac(interface):
    try:
        output = os.popen(f"ifconfig {interface}").read()
        pattern = r"([0-9a-f-A-F]{2}:){5}[0-9a-f-A-F]{2}"
        mac_address = re.search(pattern, output)
        return mac_address.group(0) if mac_address else None
    except Exception as e:
        print(f"[Error] Failed to retrieve MAC address: {e}")
        return None

# Generate a random MAC address using scapy.
def generate_random_mac():
    return str(RandMAC())

# Check if it's a valid MAC address format.
def is_valid_mac(mac):
    pattern = r"([0-9a-f-A-F]{2}:){5}[0-9a-f-A-F]{2}"
    return True if re.match(pattern, mac) else False

# Change the MAC address of the interface the user selected.
def change_mac_address(interface, new_mac):
    try:
        if not is_valid_mac(new_mac):
            print("[Error] Invalid MAC address format.")
            return
        
        print(f"[Info] Changing MAC address for {interface} to {new_mac}...")
        os.system(f"sudo ifconfig {interface} down")
        os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
        os.system(f"sudo ifconfig {interface} up")
        updated_mac = get_current_mac(interface)
        if updated_mac == new_mac:
            print(f"[Success] MAC address changed to {updated_mac}")
        else:
            print("[Error] Failed to change MAC address.")
    except Exception as e:
        print(f"[Error] Could not change MAC address: {e}")

# Start the MAC Spoofing process.
def mac_spoofing():
    interface = input("Enter the network interface (e.g., eth0, wlan0): ").strip()
    choice = input("Generate a random MAC address? (y/n): ").strip().lower()
    new_mac = generate_random_mac() if choice == "y" else input("Enter the new MAC address: ").strip()
    if is_valid_mac(new_mac):
        change_mac_address(interface, new_mac)
    else:
        print("[Error] Invalid MAC address format.")

# Display information about the MAC Spoofing feature.
def display_info():
    print_feature_header("MAC Spoofing")
    print("\n- MAC Spoofing allows you to change your device's MAC address.")
    print("- This can help maintain privacy and bypass certain network restrictions.")
    print("- The change is temporary and will be reset after a reboot.")
    print("~~ Requires administrator privileges to apply changes. ~~")
    print("-" * 40)
    input("Press Enter to continue...")

# Display the menu and start the feature.
def main():
    while True:
        try:
            print_feature_header("MAC Spoofing")
            print("0. Get info about this feature")
            print("1. Start MAC Spoofing")
            print("2. Return to Main Menu")
            print("3. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-3): ").strip()

            if choice == "0":
                display_info()
            elif choice == "1":
                mac_spoofing()
            elif choice == "2":
                print("\nReturning to Main Menu...\n")
                return
            elif choice == "3":
                print("Exiting program. Goodbye!")
                exit(0)
            else:
                print("\n[Error] Invalid option. Please try again!")
        except KeyboardInterrupt:
            print("\n[Warning] Please use option 3 to exit!\n")
            sleep(2)

if __name__ == "__main__":
    main()