import paramiko
import subprocess
from util import print_feature_header
from time import sleep
import argparse
import sys

def remote_execute_command(host, username, password, command):
    try:
        print(f"[Info] Connecting to {host}...")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password, timeout=5)

        print(f"[Info] Executing command: {command}")
        stdin, stdout, stderr = ssh.exec_command(command)
        
        output = stdout.read().decode()
        errors = stderr.read().decode()
        ssh.close()

        if output:
            print("\n[Output]:")
            print(output)
        if errors:
            print("\n[Errors]:")
            print(errors)
        if not output and not errors:
            print("\n[Info] Command executed with no output.")
    except Exception as e:
        print(f"[Error] Failed to execute command: {e}")

def display_info():
    print_feature_header("Remote Command Executor")
    print("\n- Connects to remote servers via SSH.")
    print("- Lets you run any shell command securely.")
    print("- Great for remote administration or automation.")
    print("~~ Requires server credentials and open SSH port (22). ~~")
    print("-" * 40)
    input("Press Enter to continue...")

def interactive_menu():
    while True:
        try:
            print_feature_header("Remote Command Executor")
            print("0. Get info about this feature")
            print("1. Execute Remote Command")
            print("2. Return to Main Menu")
            print("3. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-3): ").strip()

            if choice == "0":
                display_info()
            elif choice == "1":
                host = input("Enter remote host (IP or domain): ").strip()
                username = input("Enter SSH username: ").strip()
                password = input("Enter SSH password: ").strip()
                command = input("Enter the command to execute: ").strip()

                remote_execute_command(host, username, password, command)
                input("\nPress Enter to continue...")
            elif choice == "2":
                print("\nReturning to Main Menu...\n")
                return
            elif choice == "3":
                print("Exiting program. Goodbye!")
                exit(0)
            else:
                print("[Error] Invalid option. Please try again!")

        except KeyboardInterrupt:
            print("\n[Warning] Please use option 3 to exit!\n")
            sleep(2)

def cli_mode():
    parser = argparse.ArgumentParser(description="Remote Command Executor via SSH")
    parser.add_argument("--host", required=True, help="Remote host IP or domain")
    parser.add_argument("--username", required=True, help="SSH username")
    parser.add_argument("--password", required=True, help="SSH password")
    parser.add_argument("--command", required=True, help="Shell command to execute remotely")

    args = parser.parse_args()

    remote_execute_command(args.host, args.username, args.password, args.command)

def main():
    # If script is run with arguments, use CLI mode
    if len(sys.argv) > 1:
        cli_mode()
    else:
        interactive_menu()

if __name__ == "__main__":
    main()
