import webbrowser
import sys
import argparse
from time import sleep
from Config import config
from mac_spoofing import main as mac_spoofing
from web_scraping import main as web_scraping
from service_comparator import main as service_comparator
from mini_ddos import main as mini_ddos
from remote_command_executor import main as remote_command_executor
from password_tools import main as password_tools
from data_hider import main as data_hider
from file_encryption import main as file_encryption
from file_scanner import main as file_scanner

def print_menu():
    print("----------------------------------")
    print("--- Python Toolkit - Main Menu ---")
    print("----------------------------------")
    print("0. Show Configuration")
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

def parse_args():
    parser = argparse.ArgumentParser(
        description="Python Toolkit - SACA: A multifunctional toolkit for networking, security, and automation.",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument(
        "--tool", "-t",
        type=int,
        choices=range(0, 10),
        metavar="[0-9]",
        help=(
            "Directly run a specific tool without the interactive menu:\n"
            " 0 = Show Configuration\n"
            " 1 = MAC Spoofing\n"
            " 2 = Web Scraping\n"
            " 3 = Service Comparator\n"
            " 4 = Mini DDOS Attack\n"
            " 5 = Remote Command Executor\n"
            " 6 = Password Generator & Strength Analyzer\n"
            " 7 = Data -> Image Hider\n"
            " 8 = Secure File Encryption & Decryption\n"
            " 9 = Smart File Scanner & Email Reporter"
        )
    )

    return parser.parse_args()

# The main program is run here using an interactive menu.
def main():
    while True:
        try:
            print_menu()
            selected_option = input("Select an option (0-10): ").strip()
            try:
                choice = int(selected_option)
            except ValueError:
                print("\n[Error] Invalid input. Please enter a number between 0 and 10.")
                sleep(2) # Add a delay before showing the menu again
                continue
            if choice == 0:
                config.show_config(mode="all")
                input("Press Enter to continue...")
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
                file_encryption()
            elif choice == 9:
                file_scanner()
            elif choice == 10:
                print("Exiting program. Goodbye!")
                sys.exit(0)
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
    #Check if args are parsed with the startup or not.
    args = parse_args()
    if args.tool is not None:
        tools = [
            lambda: config.show_config(mode="all"),
            mac_spoofing,
            web_scraping,
            service_comparator,
            mini_ddos,
            remote_command_executor,
            password_tools,
            data_hider,
            file_encryption,
            file_scanner
        ]
        tools[args.tool]()
    else:
        main()
