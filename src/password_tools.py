import re
import random
import itertools
from time import sleep
from passlib.hash import sha256_crypt
from config import config
from util import print_feature_header

def generate_password(length=None):
    length = length or config.PASS_LENGTH
    if length < 4:
        print("[Error] Password length should be at least 4.")
        return None

    char_groups = []
    if config.PASS_INCLUDE_LOWER:
        char_groups.append("abcdefghijklmnopqrstuvwxyz")
    if config.PASS_INCLUDE_UPPER:
        char_groups.append("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if config.PASS_INCLUDE_DIGITS:
        char_groups.append("0123456789")
    if config.PASS_INCLUDE_SYMBOLS:
        char_groups.append("!@#$%^&*()-_=+[]{}|;:',.<>?/")

    if not char_groups:
        print("[Error] No character types enabled.")
        sleep(2)
        return None

    required_chars = [random.choice(group) for group in char_groups]
    remaining_length = length - len(required_chars)
    flat_charset = ''.join(itertools.chain.from_iterable(char_groups))
    remaining_chars = [random.choice(flat_charset) for _ in range(remaining_length)]

    password_chars = required_chars + remaining_chars
    random.shuffle(password_chars)
    return ''.join(password_chars)



def analyze_strength(password):
    print("\n[Analysis Result]")
    score = 0
    messages = []

    if len(password) >= 12:
        score += 1
    else:
        messages.append("- Too short (minimum 12 characters recommended)")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("- Missing lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        messages.append("- Missing uppercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        messages.append("- Missing digits")

    if re.search(r"[^a-zA-Z0-9]", password):
        score += 1
    else:
        messages.append("- Missing special characters")

    if score == 5:
        print("Password strength: STRONG")
    elif score >= 3:
        print("Password strength: MEDIUM")
    else:
        print("Password strength: WEAK")

    if messages:
        print("\nSuggestions:")
        for msg in messages:
            print(msg)

def ask_bool(prompt, current):
        answer = input(f"{prompt} (y/n, current: {current}): ").strip().lower()
        if answer == '':
            return current
        return answer == 'y'

def modify_config():
    print_feature_header("Modify Password Configuration")
    config.show_config(mode="password")

    lower = ask_bool("Include lowercase letters", config.PASS_INCLUDE_LOWER)
    upper = ask_bool("Include uppercase letters", config.PASS_INCLUDE_UPPER)
    digits = ask_bool("Include digits", config.PASS_INCLUDE_DIGITS)
    symbols = ask_bool("Include symbols", config.PASS_INCLUDE_SYMBOLS)

    length_input = input(f"Enter password length (current: {config.PASS_LENGTH}): ").strip()
    if length_input.isdigit():
        length = int(length_input)
    else: 
        length = config.PASS_LENGTH
    if length <= 3:
        print("[Error] Password length should be at least 4.")
        length = 4

    config.update_config(
        pass_lower=lower,
        pass_upper=upper,
        pass_digits=digits,
        pass_symbols=symbols,
        pass_length=length
    )

    print("\n[Info] Password configuration updated.")
    sleep(1)


def display_info():
    print_feature_header("Password Generator & Strength Analyzer")
    print("- Generates secure passwords with configurable settings.")
    print("- Evaluates strength based on structure, length, and character types.")
    print("- Optionally hashes passwords using SHA-256.")
    print("-" * 40)
    input("Press Enter to continue...")


def main():
    while True:
        try:
            print_feature_header("Password Generator & Strength Analyzer")
            print("0. Get info about this feature")
            print("1. Generate a Password")
            print("2. Analyze Existing Password")
            print("3. Hash Password (SHA-256)")
            print("4. Modify Configuration")
            print("5. Return to Main Menu")
            print("6. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-6): ").strip()

            if choice == "0":
                display_info()
            elif choice == "1":
                length_input = input(f"Enter password length (default: {config.PASS_LENGTH}): ").strip()
                length = int(length_input) if length_input.isdigit() else None
                password = generate_password(length)
                if password:
                    print(f"\nGenerated Password: {password}")
            elif choice == "2":
                password = input("Enter the password to analyze: ").strip()
                analyze_strength(password)
            elif choice == "3":
                password = input("Enter password to hash: ").strip()
                hashed = sha256_crypt.hash(password)
                print(f"\nHashed Password: {hashed}")
                salt_only = hashed.split('$')[3]
                print(f"Salt: {salt_only}")
                hash_only = hashed.split('$')[-1]
                print(f"Raw Hash: {hash_only}")

            elif choice == "4":
                modify_config()
            elif choice == "5":
                print("\nReturning to Main Menu...\n")
                return
            elif choice == "6":
                print("Exiting program. Goodbye!")
                exit(0)
            else:
                print("[Error] Invalid option. Please try again.")

        except KeyboardInterrupt:
            print("\n[Warning] Please use option 6 to exit!\n")
            sleep(2)


if __name__ == "__main__":
    main()
