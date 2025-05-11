import glob
import fnmatch
import http.client
import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from pathlib import Path
from util import print_feature_header
from config import config

def scan_files(directory, pattern):
    try:
        directory = Path(directory).resolve()
        if not directory.is_dir():
            print("[Error] The provided directory does not exist.")
            return []

        matching_files = []
        
        for file in glob.iglob(f"{directory}/**/*", recursive=True):
            if fnmatch.fnmatch(file, pattern):
                matching_files.append(file)
                
        return matching_files

    except Exception as e:
        print(f"[Error] An error occurred while scanning files: {e}")
        return []

def send_email(subject, body, to_email, attachments=None):
    from_email = config.EMAIL_SENDER
    email_password = config.EMAIL_PASSWORD

    try:
        msg = MIMEMultipart()
        msg["From"] = from_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        if attachments:
            for filename in attachments:
                with open(filename, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), Name=Path(filename).name)
                    part["Content-Disposition"] = f"attachment; filename={Path(filename).name}"
                    msg.attach(part)

        print("[Info] Email simulation: Sending email...")

        print(f"[HTTP Status] {http.client.OK} - Email sent successfully")

    except Exception as e:
        print(f"[Error] Failed to send email: {e}")
        print(f"[HTTP Status] {http.client.INTERNAL_SERVER_ERROR} - Failed to send email")

def generate_report(directory, pattern, matching_files):
    report = f"Smart File Scanner Report\n\nScanned directory: {directory}\nPattern: {pattern}\n\nFound files:\n"
    if matching_files:
        for file in matching_files:
            report += f"- {file}\n"
    else:
        report += "No files found matching the pattern.\n"
    return report

def show_email_summary(subject, body, attachments):
    print("\n[Info] Quick Email Summary:")
    print(f"Subject: {subject}")
    print(f"Body:\n{body}")
    print("Attachments:")
    if attachments:
        for attachment in attachments:
            print(f"- {attachment}")
    else:
        print("No attachments.")
    print("-" * 40)

def smart_file_scanner_and_email_reporter():
    print_feature_header("Smart File Scanner & Email Reporter")
    
    directory = input("Enter the directory to scan: ").strip()
    pattern = input("Enter the file pattern to search (e.g., *.txt): ").strip()

    print("[Info] Scanning files...")
    matching_files = scan_files(directory, pattern)

    print("[Info] Generating report...")
    report = generate_report(directory, pattern, matching_files)

    while True:
        to_email = input("Enter the email address to send the report to: ").strip()
        if is_email(to_email):
            break


    attach_files = input("Do you want to attach the found files in the email? (y/n): ").strip().lower()
    attachments = matching_files if attach_files == "y" else None

    show_summary = input("Would you like to view a quick summary of the email to be sent? (y/n): ").strip().lower()
    if show_summary == "y":
        show_email_summary("Smart File Scanner Report", report, attachments)

    send_email("Smart File Scanner Report", report, to_email, attachments)

def is_email(mail):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+$"
    return True if re.match(pattern, mail) is not None else False

def display_info():
    print_feature_header("Smart File Scanner & Email Reporter Info")
    print("\n- Scans a specified directory for files matching a given pattern (e.g., *.txt).")
    print("- Sends an email report with the files found.")
    print("- Supports attaching the found files to the email if needed.")
    print("~~ Email sending is simulated, thus emails aren't actually being sent. ~~")
    print("-" * 40)
    input("Press Enter to continue...")

def main():
    while True:
        try:
            print_feature_header("Smart File Scanner & Email Reporter")
            print("0. Get info about this feature")
            print("1. Start file scan and send report via email")
            print("2. Return to Main Menu")
            print("3. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-3): ").strip()

            if choice == "0":
                display_info()
            elif choice == "1":
                smart_file_scanner_and_email_reporter()
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

if __name__ == "__main__":
    main()
