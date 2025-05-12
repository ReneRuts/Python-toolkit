import json
import socket
import paramiko
from time import sleep
from pathlib import Path
from util import print_feature_header
from Config import config


def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2)
            return s.connect_ex((host, port)) == 0
    except Exception:
        return False


def fetch_services_via_ssh(host, username, password):
    services = []
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password, timeout=5)
        stdin, stdout, stderr = ssh.exec_command("systemctl list-units --type=service")
        for line in stdout.readlines():
            if ".service" in line:
                services.append(line.split()[0])
        ssh.close()
    except Exception as e:
        print(f"[Error] SSH connection failed on {host}: {e}")
    return services


def collect_host_data(num_hosts):
    host_data = []
    for i in range(num_hosts):
        print(f"\nHost {i+1}:")
        host = input("Enter the host IP or domain: ").strip()
        try:
            socket.getaddrinfo(host, 22)
        except socket.gaierror as e:
            print(f"[Error] Invalid host '{host}': {e}")
            continue
        username = input("Enter the SSH username: ").strip()
        password = input("Enter the SSH password: ").strip()
        print("[Info] Setting up the ssh connection....")
        sleep(0.5)
        print("[Info] Fetching services and collecting open ports. Please wait..")
        services = fetch_services_via_ssh(host, username, password)
        open_ports = {port: check_port(host, port) for port in config.DEFAULT_PORTS}
        host_data.append({
            "host": host,
            "services": sorted(set(services)),
            "open_ports": open_ports
        })
        print("[Info] Done fetching services and collecting ports.")
    return host_data


def save_comparison_data(host_data):
    output_dir = Path("output/service_comparator")
    output_dir.mkdir(parents=True, exist_ok=True)
    json_file_path = output_dir / "services_comparison.json"
    with open(json_file_path, "w") as json_file:
        json.dump(host_data, json_file, indent=4)
    print(f"\n[Info] Data saved successfully to {json_file_path}.")


def display_service_differences(host_data):
    print("\n[Comparison Result]")
    all_service_sets = [set(host["services"]) for host in host_data]
    common_services = set.intersection(*all_service_sets)

    if len(host_data) < 2:
        print("[Error] Not enough host data to compare.")
        return

    if all(service_set == all_service_sets[0] for service_set in all_service_sets[1:]):
        print("There are no differences for the services for all the hosts.")
    else:
        print(f"Common services across all hosts ({len(common_services)}):")
        for svc in sorted(common_services):
            print(f"  - {svc}")
        sleep(2)
        print("\nUnique services per host:")
        for host in host_data:
            unique = set(host["services"]) - common_services
            if unique:
                print(f"\nHost: {host['host']}")
                for svc in sorted(unique):
                    print(f"  - {svc}")
            else:
                print(f"\nHost: {host['host']} has no unique services.")


def compare_services():
    print_feature_header("Service Comparator")
    try:
        num_hosts = input(f"Enter the number of hosts to compare (2 - {config.MAX_HOSTS}): ").strip()
        if num_hosts.isdigit():
            num_hosts = int(num_hosts)
        else:
            print(f"[Error] Invalid input! Please enter a number.")
            return
        if num_hosts < 2 or num_hosts > config.MAX_HOSTS:
            print(f"[Error] Invalid number! Only 2 - {config.MAX_HOSTS} hosts supported.")
            return
    except ValueError:
        print("[Error] Please enter a valid number.")
        return

    host_data = collect_host_data(num_hosts)
    if len(host_data) < 2:
        print("[Error] Not enough valid hosts to compare.")
        return

    save_comparison_data(host_data)
    sleep(2)
    display_service_differences(host_data)
    print("\n[Info] Comparison complete!")


def config_menu():
    print("0. Modify MAX_HOSTS")
    print("1. Modify DEFAULT_PORTS")
    print("2. Return to Service Comparator Menu")
    print("3. Exit")
    print("----------------------------------")
    choice = input("Select an option (0-3): ").strip()
    if choice == "0":
        new_max_hosts = input(f"Enter new MAX_HOSTS value (Current: {config.MAX_HOSTS} max=100, \"quit\" to keep): ").strip()
        if new_max_hosts == "quit":
            print("[Info] Keeping current MAX_HOSTS value.")
            return
        elif not new_max_hosts.isdigit():
            print("[Error] Invalid value! Must be a positive integer.")
            return
        new_max_hosts = int(new_max_hosts)
        if new_max_hosts < 1 or new_max_hosts > 100:
            print("[Error] Invalid value! Must be between 1 and 100.")
        else:
            config.update_config(max_hosts=new_max_hosts)
            print(f"[Info] MAX_HOSTS updated to {config.MAX_HOSTS}.")
    elif choice == "1":
        new_ports = input(f"Enter new DEFAULT_PORTS separated by a comma (Current: {config.DEFAULT_PORTS}, \"quit\" to keep): ").strip()
        if new_ports == "quit":
            print("[Info] Keeping current DEFAULT_PORTS value.")
        elif new_ports == "all":
            config.update_config(default_ports=[i for i in range(1, 65536)])
            print(f"[Info] DEFAULT_PORTS updated to all ports (1-65535).")
        elif not all(p.strip().isdigit() for p in new_ports.split(",")):
            print("[Error] Invalid input! Ports must be integers separated by commas.")
        else:
            new_ports_list = [int(p.strip()) for p in new_ports.split(",")]
            config.update_config(default_ports=new_ports_list)
            print(f"[Info] DEFAULT_PORTS updated to {config.DEFAULT_PORTS}.")
    elif choice == "2":
        print("\nReturning to Service Comparator Menu...\n")
    elif choice == "3":
        print("Exiting program. Goodbye!")
        exit(0)
    else:
        print("[Error] Invalid option. Please try again!")
        sleep(2)


def modify_config():
    print_feature_header("Modify Service Comparator Configuration")
    try:
        config.show_config(mode="service_comparator")
        config_menu()
    except KeyboardInterrupt:
        print("\n[Warning] Please use option 3 to exit!\n")
        sleep(2)
    except Exception as e:
        print(f"[Error] Something went wrong: {e}")
        sleep(2)


def display_info():
    print_feature_header("Service Comparator Info")
    print("\n- Compares active services across multiple hosts.")
    print("- Uses SSH to retrieve running services.")
    print("- Scans ports for accessibility (e.g. SSH, HTTP, HTTPS, MySQL).")
    print(f"- Supports up to {config.MAX_HOSTS} hosts.")
    print("~~ Results are saved in JSON format. ~~")
    print("-" * 40)
    input("Press Enter to continue...")


def main():
    while True:
        try:
            print_feature_header("Service Comparator")
            print("0. Get info about this feature")
            print("1. Start Service Comparison")
            print("2. Modify Configuration")
            print("3. Return to Main Menu")
            print("4. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-4): ").strip()

            if choice == "0":
                display_info()
            elif choice == "1":
                compare_services()
            elif choice == "2":
                modify_config()
            elif choice == "3":
                print("\nReturning to Main Menu...\n")
                return
            elif choice == "4":
                print("Exiting program. Goodbye!")
                exit(0)
            else:
                print("[Error] Invalid option. Please try again!")
        except KeyboardInterrupt:
            print("\n[Warning] Please use option 3 to exit!\n")
            sleep(2)


if __name__ == "__main__":
    main()
