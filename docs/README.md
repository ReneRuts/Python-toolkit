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

3. Create a Virtual Environment & Install the required libraries:

    ```cmd
    python -m venv .venv
    .\.venv\Scripts\activate
    pip install -r requirements.txt
    ```

    > **Note:** Some features may require additional system dependencies, such as `chromedriver` for Selenium. Ensure you have the necessary permissions.

4. Run the main script:

    1. Through python

          ```cmd
          python src\main.py
          ```

    2. Through arguments

          Get help.

          ```cmd
          python src\main.py --help
          ```

          Run a tool.

          ```cmd
          python src\main.py --tool [1-10]
          ```

    The main script serves as a menu for accessing each toolkit feature.

---

## Preconfigured Tests

The program includes some preconfigured tests to check if everything works as it should.

> **Note:** Please keep in mind that there has to be an active http or https server running on your localhost using port 80 to make all tests succeed.
>
> This can be done by doing the following command on your host:
  
  ```cmd
    python -m http.server 80
  ```

---

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

**Libraries Used:** `scapy`, `os`, `re` & `time`

Change the MAC address of your network interface card (NIC) to spoof or mask your device’s identity.

- **Use Case:** Evade MAC-based tracking, simulate device identities in test networks.
- **How it Works:** Executes system-level MAC address changes, confirmed using Scapy’s packet inspection tools.
- **Testability:** Functionality can be manually tested by observing changes in the system's MAC address post-execution.

---

### 2. WEB Scraping

**Libraries Used:** `requests`,`re`, `time`, `BeautifulSoup` & `selenium`

Scrape static and dynamic websites to extract data quickly and efficiently.

- **Use Case:** Automate data collection from websites, such as articles, product prices, or search results.
- **How it Works:**
  - **Requests** retrieves HTML content for static websites.
  - **BeautifulSoup** parses the HTML to extract key elements such as the page title and headers.
  - **Selenium** automates browsers to handle JavaScript-rendered pages that may require dynamic content loading.
  
  **Tested Features:**
  - URL validation (`is_valid_url`).
  - HTML content fetching (`fetch_html`).
  - Parsing and extracting data (`parse_html`).
  - Full scraping using Requests and Selenium.

- **Test Example:**
  - We validate the URL format using regex to ensure it's in the correct format.
  - The `fetch_html` function is tested by confirming that HTML content is returned and contains an `<html>` tag.
  - The `parse_html` function is tested by confirming that the extracted title and headers match expected content.

  Full tests are available in `test_web_scraping.py` to verify correct operation.

---

### 3. Service Comparator

**Libraries Used:** `socket`, `paramiko`, `json`, `pathlib` & `time`

Compare services and open ports on multiple remote hosts over SSH.

- **Use Case:** System administrators can compare active services across servers for consistency or troubleshooting.
- **How it Works:**
  - Establishes an SSH connection using `paramiko`.
  - Fetches running services with `systemctl list-units` (or equivalent).
  - Scans open ports using `socket`.
  - Outputs the results in a JSON format for easy comparison.

---

### 4. Mini DDOS Attack

**Libraries Used:** `threading`, `time`, `socket` & `sys`

A basic multithreaded tool to simulate a Distributed Denial of Service (DDoS) attack for educational or testing purposes.

- **Use Case:** Simulate simple denial-of-service behavior in controlled environments.
- **How it Works:**
  - Spawns multiple threads that continuously send socket requests to a target.
  - Thread count and delay between requests are customizable via user input.
  - It's important to use this tool responsibly and only in test environments.

---

### 5. Remote Command Executor

**Libraries Used:** `paramiko`, `subprocess` & `time`

Execute shell commands remotely on Linux hosts over SSH.

- **Use Case:** Run diagnostics, gather logs, or automate tasks across multiple remote servers.
- **How it Works:**
  - Uses `paramiko` to manage SSH connections.
  - Executes commands via the remote shell, capturing and displaying results.
  - Command execution is done in real-time with options to execute locally after remote execution.

- **Testability:** Manual tests can be run by providing valid credentials and confirming the output of commands executed on remote systems.

---

### 6. Password Generator & Strength Analyzer

**Libraries Used:** `passlib`, `re`, `random`, `itertools` & `time`

Generate secure passwords and analyze the strength of existing ones.

- **Use Case:** Improve security hygiene by ensuring strong, unique passwords.
- **How it Works:**
  - Uses `random` and `itertools` to construct complex passwords that include uppercase letters, numbers, and symbols.
  - Password strength is determined using regex checks and entropy-based analysis, including checks for length and complexity.
  - `passlib` can be used for secure password hashing.

---

### 7. Data → Image Hider

**Libraries Used:** `stegano`, `pathlib`, `base64`, `time` & `cv2`

Hide sensitive information inside image files using steganography.

- **Use Case:** Securely embed data within images for discreet data transfer or storage.
- **How it Works:**
  - `stegano` embeds base64-encoded data inside PNG image files.
  - Files can be extracted and verified using the same module, making it possible to securely hide and retrieve sensitive information.

---

### 8. Secure File Encryption & Decryption

**Libraries Used:** `cryptography`, `pathlib`, `shutil`, `send2trash` & `datetime`

Encrypt and decrypt sensitive files with optional safe deletion.

- **Use Case:** Protect confidential files with AES encryption.
- **How it Works:**
  - Uses `Fernet` from the `cryptography` library to encrypt files.
  - Encrypted files are saved in a secure directory for easy management.
  - Optional functionality to move old files to trash using `send2trash`.

---

### 9. Smart File Scanner & Email Reporter

**Libraries Used:** `email`, `fnmatch`, `glob`, `http`, `re` & `pathlib`

Scan directories for files matching a specific pattern and simulate sending an email report.

- **Use Case:** Identify specific file types (e.g., `.log`, `.txt`) and generate searchable reports.
- **How it Works:**
  - Scans directories using `glob` and `fnmatch` to locate files matching a pattern.
  - Constructs email reports with `email.mime`.
  - Uses `http.client` to simulate HTTP status reporting during email operations.

---
