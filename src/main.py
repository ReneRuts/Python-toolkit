import webbrowser
import sys
from time import sleep
from mac_spoofing import main as mac_spoofing
from web_scraping import main as web_scraping
from service_comparator import main as service_comparator
from mini_ddos import main as mini_ddos
from remote_command_executor import main as remote_command_executor
from password_tools import main as password_tools
from data_hider import main as data_hider
# from file_scanner import main as file_scanner
# from file_encryption import main as file_encryption

def print_menu():
    print("----------------------------------")
    print("--- Python Toolkit - Main Menu ---")
    print("----------------------------------")
    print("1. MAC spoofing")  # Scapy, OS
    print("2. WEB scraping")  # Requests, BeautifulSoup, Selenium
    print("3. Service Comparator")  # Socket, Paramiko, JSON
    print("4. Mini DDOS Attack")  # Threading, Time, Socket, Sys
    print("5. Remote Command Executor")  # Paramiko, Subprocess, Argparse
    print("6. Password generator & Strength Analyzer")  # Passlib, re, random, itertools
    print("7. Data -> Image Hider")  # Stegano, OS, Base64, image_viewer
    print("8. Secure File Encryption & Decryption")  # Cryptography, Pathlib, Shutil, Send2trash, Datetime
    print("9. Smart File Scanner & Email Reporter") # email, fnmatch, glob, http
    print("10. Exit")
    print("----------------------------------")

# The main program is run here using an interactive menu.
def main():
    while True:
        try:
            print_menu()
            selected_option = input("Select an option (1-10): ").strip()
            try:
                choice = int(selected_option)
            except ValueError:
                print("\n[Error] Invalid input. Please enter a number between 1 and 10.")
                sleep(2) # Add a delay before showing the menu again
                continue
            if choice == 1:
                mac_spoofing()
            elif choice == 2:
                web_scraping()
            elif choice == 3:
                service_comparator()
            elif choice == 4:
                mini_ddos()
            elif choice == 5:
                remote_command_executor()
            elif choice == 6:
                password_tools()
            elif choice == 7:
                data_hider()
            elif choice == 8:
                #file_encryption()
                print("\n[Info] File Encryption & Decryption feature is not yet implemented.")
            elif choice == 9:
                #file_scanner()
                print("\n[Info] File Scanner & Email Reporter feature is not yet implemented.")
            elif choice == 10:
                print("Exiting program. Goodbye!")
                sys.exit(0)
            elif choice == 11:
                webbrowser.open("https://www.youtube.com/watch?v=hvL1339luv0")
            else:
                print("\n[Error] Invalid option. Please try again!\n")
                sleep(2)

        except KeyboardInterrupt:
            print("\n[Warning] Please use option 10 to exit!\n")
            sleep(2)
        
        except Exception as e:
            print("\n[Unexpected Error] Something went wrong:")
            print(f"Error Message: {e}\n")
            print("Restarting menu...\n")

if __name__ == "__main__":
    main()