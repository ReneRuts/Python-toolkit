from cryptography.fernet import Fernet
from pathlib import Path
import shutil
from send2trash import send2trash
from datetime import datetime
from util import print_feature_header
from config import config



def get_key_file_path():
    OUTPUT_DIR = Path("output/secure_file_encryption_and_decryption")
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    custom_path = input(f"Enter path to key file (press Enter to use default: {config.KEY_FILE}): ").strip()
    return Path(custom_path) if custom_path else OUTPUT_DIR / config.KEY_FILE.name

def generate_key():
    key_path = get_key_file_path()
    key = Fernet.generate_key()
    try:
        key_path.write_bytes(key)
        print(f"[Info] Key successfully generated at: {key_path}")
    except Exception as e:
        print(f"[Error] Unable to write key file: {e}")

def load_key():
    key_path = get_key_file_path()
    if not key_path.exists():
        print(f"[Error] Key file not found at: {key_path}")
        return None
    try:
        return key_path.read_bytes()
    except Exception as e:
        print(f"[Error] Could not read key: {e}")
        return None

def encrypt_file():
    OUTPUT_DIR = Path("output/secure_file_encryption_and_decryption")
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    key = load_key()
    if not key:
        return

    fernet = Fernet(key)
    file_input = input("Enter path to the file to encrypt: ").strip()
    file_path = Path(file_input)

    if not file_path.is_file():
        print("[Error] File not found.")
        return

    try:
        backup_path = OUTPUT_DIR / (file_path.stem + f"_backup_{datetime.now().strftime('%Y%m%d%H%M%S')}{file_path.suffix}")
        shutil.copy2(file_path, backup_path)
        print(f"[Info] Backup created at {backup_path}")

        data = file_path.read_bytes()
        encrypted_data = fernet.encrypt(data)
        encrypted_path = OUTPUT_DIR / (file_path.name + ".enc")
        encrypted_path.write_bytes(encrypted_data)

        print(f"[Info] Encrypted file saved at {encrypted_path} - {datetime.now()}")

        delete_choice = input("Send original file to trash? (y/n): ").strip().lower()
        if delete_choice == "y":
            send2trash(str(file_path))
            print("[Info] Original file sent to trash.")
    except Exception as e:
        print(f"[Error] Encryption failed: {e}")

def decrypt_file():
    OUTPUT_DIR = Path("output/secure_file_encryption_and_decryption")
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    key = load_key()
    if not key:
        return

    fernet = Fernet(key)
    file_input = input("Enter path to the .enc file: ").strip()
    encrypted_path = Path(file_input)

    if not encrypted_path.is_file() or encrypted_path.suffix != ".enc":
        print("[Error] Invalid encrypted file.")
        return

    try:
        encrypted_data = encrypted_path.read_bytes()
        decrypted_data = fernet.decrypt(encrypted_data)
        original_name = encrypted_path.stem
        original_path = OUTPUT_DIR / original_name
        original_path.write_bytes(decrypted_data)

        print(f"[Info] Decrypted file saved as {original_path} - {datetime.now()}")

        delete_choice = input("Send encrypted file to trash? (y/n): ").strip().lower()
        if delete_choice == "y":
            send2trash(str(encrypted_path))
            print("[Info] Encrypted file sent to trash.")
    except Exception as e:
        print(f"[Error] Decryption failed: {e}")

def display_info():
    print_feature_header("Secure File Encryption & Decryption")
    print("This tool securely encrypts and decrypts files using Fernet (symmetric encryption).")
    print("You can manage key files, back up originals, and safely delete with send2trash.")
    print("All paths and files are handled using pathlib.")
    print("-" * 40)
    input("Press Enter to continue...")

def main():
    while True:
        print_feature_header("Secure File Encryption & Decryption")
        print("0. Get info about this feature")
        print("1. Generate Key File")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Return to Main Menu")
        print("5. Exit")

        choice = input("Select an option (0-5): ").strip()

        if choice == "0":
            display_info()
        elif choice == "1":
            generate_key()
        elif choice == "2":
            encrypt_file()
        elif choice == "3":
            decrypt_file()
        elif choice == "4":
            print("\nReturning to Main Menu...\n")
            return
        elif choice == "5":
            print("Exiting program. Goodbye!")
            exit(0)
        else:
            print("[Error] Invalid option. Please try again!")

if __name__ == "__main__":
    main()
