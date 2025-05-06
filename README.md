# Python Toolkit - SACA

Welcome to the **Python Toolkit - SACA** — a powerful suite of tools for network operations, security testing, file management, and data manipulation. Below is an overview of each feature, in the same order as the toolkit's main menu.

---

## Getting Started

To run the toolkit:

1. Clone the repository:

    ```cmd
    git clone git@gitlab.ti.howest.be:ti/2024-2025/s2/scripting-and-code-analysis/projects/rene-ruts/my-project.git
    ```

2. Navigate to the project directory:

    ```cmd
    cd my-project
    ```

3. Install the required libraries:

    ```cmd
    pip install -r requirements.txt
    ```

    > **Note:** Some features may require additional system dependencies. Ensure you have the necessary permissions and libraries installed.
4. Run the main script:

    ```cmd
    python src\main.py
    ```

## Main Menu

1. MAC Spoofing  
2. WEB Scraping  
3. Service Comparator  
4. Mini DDOS Attack  
5. Remote Command Executor  
6. Password Generator & Strength Analyzer  
7. Data → Image Hider  
8. Secure File Encryption & Decryption  
9. Smart File Scanner & Email Reporter  

---

## Features

### 1. MAC Spoofing

**Libraries Used:** `scapy`, `os`

Change the MAC address of your network interface card (NIC) to spoof or mask your device’s identity.

- **Use Case:** Evade MAC-based tracking, simulate device identities in test networks.
- **How it Works:** Executes system-level MAC address changes, confirmed using Scapy’s packet inspection tools.

---

### 2. WEB Scraping

**Libraries Used:** `requests`, `BeautifulSoup`, `selenium`

Scrape static and dynamic websites to extract data quickly and efficiently.

- **Use Case:** Automate data collection from websites, such as articles, product prices, or search results.
- **How it Works:**
  - `requests` retrieves HTML content.
  - `BeautifulSoup` parses and extracts elements.
  - `selenium` automates browsers to handle JavaScript-rendered pages.

---

### 3. Service Comparator

**Libraries Used:** `socket`, `paramiko`, `json`

Compare services and open ports on multiple remote hosts over SSH.

- **Use Case:** System administrators can compare active services across servers for consistency or troubleshooting.
- **How it Works:**
  - SSH connection established using `paramiko`.
  - Services fetched with `systemctl list-units`.
  - Ports scanned using `socket` and results saved in JSON.

---

### 4. Mini DDOS Attack

**Libraries Used:** `threading`, `time`, `socket`, `sys`

A basic multithreaded tool to simulate a Distributed Denial of Service (DDoS) attack for educational or testing purposes.

- **Use Case:** Simulate simple denial-of-service behavior in controlled environments.
- **How it Works:**
  - Spawns threads to send continuous socket requests to a target.
  - Delay and thread count customizable.

---

### 5. Remote Command Executor

**Libraries Used:** `paramiko`, `subprocess`, `argparse`

Execute shell commands remotely on Linux hosts over SSH.

- **Use Case:** Run diagnostics, gather logs, or automate tasks across multiple remote servers.
- **How it Works:**
  - `paramiko` manages SSH connection.
  - Commands executed via remote shell, results displayed to the user.
  - CLI options handled with `argparse`.

---

### 6. Password Generator & Strength Analyzer

**Libraries Used:** `passlib`, `re`, `random`, `itertools`

Generate secure passwords and analyze the strength of existing ones.

- **Use Case:** Improve security hygiene by ensuring strong, unique passwords.
- **How it Works:**
  - Uses `random` and `itertools` to construct complex passwords.
  - Regex and entropy-based strength checks.
  - `passlib` used for secure hashing or further analysis.

---

### 7. Data → Image Hider

**Libraries Used:** `stegano`, `os`, `base64`, `image_viewer`

Hide sensitive information inside image files using steganography.

- **Use Case:** Securely embed data within images for discreet data transfer or storage.
- **How it Works:**
  - `stegano` hides base64-encoded data within PNG files.
  - Files can be extracted and verified using the same module.

---

### 8. Secure File Encryption & Decryption

**Libraries Used:** `cryptography`, `pathlib`, `shutil`, `send2trash`, `datetime`

Encrypt and decrypt sensitive files with optional safe deletion.

- **Use Case:** Protect confidential files with AES encryption.
- **How it Works:**
  - Encrypts files using `Fernet` from the `cryptography` library.
  - Encrypted files saved to a dedicated output directory.
  - Old files optionally moved to trash using `send2trash`.

---

### 9. Smart File Scanner & Email Reporter

**Libraries Used:** `email`, `fnmatch`, `glob`, `http`

Scan directories for files matching a specific pattern and simulate sending an email report.

- **Use Case:** Identify specific file types (e.g., `.log`, `.txt`) and generate searchable reports.
- **How it Works:**
  - `glob` and `fnmatch` scan recursively for matching files.
  - `email.mime` constructs the report.
  - `http.client` is used to simulate HTTP status reporting for email operations.

---

_There is an easter egg hidden in the code! Have Fun!_
