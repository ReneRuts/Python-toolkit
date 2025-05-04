from time import sleep
import sys
from mac_spoofing import main as mac_spoofing
from web_scraping import main as web_scraping
# from service_comparator import main as service_comparator
# from mini_ddos import main as mini_ddos
# from remote_command_executor import main as remote_command_executor
# from password_tools import main as password_tools
# from data_hider import main as data_hider
# from file_encryption import main as file_encryption

def print_menu():
    print("----------------------------------")
    print("--- Python Toolkit - Main Menu ---")
    print("----------------------------------")
    print("1. MAC spoofing") # Scapy, OS
    print("2. WEB scraping") # Requests, BeautifulSoup, Selenium
    print("3. Service Comparator") # Socket, Paramiko
    print("4. Mini DDOS Attack") # Threading, Time, Socket
    print("5. Remote Command Executor") # Paramiko, Subprocess
    print("6. Password generator & Strength Analyzer") # Passlib, re, random
    print("7. Data -> Image Hider") # Stegano, OS
    print("8. Secure File Encryption & Decryption") # Cryptography, Pathlib, Shutil, send2trash
    print("9. Exit")
    print("----------------------------------")

# The main program is run here using an interactive menu.
def main():
    while True:
        try:
            print_menu()
            selected_option = input("Select an option (1-9): ").strip()
            try:
                choice = int(selected_option)
            except ValueError:
                print("\n[Error] Invalid input. Please enter a number between 1 and 9.")
                sleep(2) # Add a delay before showing the menu again
                continue
            if choice == 1:
                mac_spoofing()
            elif choice == 2:
                web_scraping()
            elif choice == 3:
                #service_comparator()
                print("\n[Info] Service Comparator feature is not yet implemented.")
            elif choice == 4:
                #mini_ddos()
                print("\n[Info] Mini DDOS Attack feature is not yet implemented.")
            elif choice == 5:
                #remote_command_executor()
                print("\n[Info] Remote Command Executor feature is not yet implemented.")
            elif choice == 6:
                #password_tools()
                print("\n[Info] Password Tools feature is not yet implemented.")
            elif choice == 7:
                #data_hider()
                print("\n[Info] Data Hider feature is not yet implemented.")
            elif choice == 8:
                #file_encryption()
                print("\n[Info] File Encryption & Decryption feature is not yet implemented.")
            elif choice == 9:
                print("Exiting program. Goodbye!")
                sys.exit(0)
            else:
                print("\n[Error] Invalid option. Please try again!")
                sleep(2) # Add a delay before showing the menu again

        except KeyboardInterrupt:
            print("\n[Warning] Please use option 9 to exit!\n")
            sleep(2)
        
        except Exception as e:
            print("\n[Unexpected Error] Something went wrong:")
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Message: {e}\n")
            print("Restarting menu...\n")

if __name__ == "__main__":
    main()