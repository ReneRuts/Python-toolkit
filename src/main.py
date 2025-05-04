from time import sleep
import sys

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
                print("\n[MAC Spoofing]")
                # mac_spoofing()
            elif choice == 2:
                print("\n[WEB Scraping]")
                # web_scraping()
            elif choice == 3:
                print("\n[Service Comparator]")
                # service_comparator()
            elif choice == 4:
                print("\n[Mini DDOS Attack]")
                # mini_ddos()
            elif choice == 5:
                print("\n[Remote Command Executor]")
                # remote_command_executor()
            elif choice == 6:
                print("\n[Password Generator & Strength Analyser]")
                # password_generator_and_strength_analyzer()
            elif choice == 7:
                print("\n[Data -> Image Hider]")
                # data_hider()
            elif choice == 8:
                print("\n[Secure File Encryption & Decryption]")
                # secure_file_encryption_and_decryption()
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