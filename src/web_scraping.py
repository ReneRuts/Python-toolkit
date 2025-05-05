import requests
import re
from util import print_feature_header
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

def display_info():
    print_feature_header("WEB Scraping")
    print("\n- WEB Scraping allows you to extract data from websites.")
    print("- Static pages can be scraped using Requests and BeautifulSoup.")
    print("- Dynamic pages can be scraped using Selenium.")
    print("\n- Note:\n   This feature gathers the title and headers from the page.\n")
    print("~~ Requires permission from the website owner!! ~~")
    print("-" * 40)
    input("Press Enter to continue...")

def is_valid_url(url):
    pattern = r"^https://(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}(/.*)?$"
    return True if re.match(pattern, url) else False

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"[Error] Failed to retrieve page: {e}")
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string if soup.title else "No title found"
    headers = [h.text for h in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
    return {"title": title, "headers": headers}

def scrape_with_selenium(url):
    try:
        driver = webdriver.Chrome()
        driver.get(url)

        page_source = driver.page_source
        driver.quit()
        return parse_html(page_source)
    except Exception as e:
        print(f"[Error] Selenium failed: {e}")
        return None

def web_scraping():
    print_feature_header("WEB Scraping")
    url = input("Enter the URL to scrape Format: https://example.com: ").strip()

    if not is_valid_url(url):
        print("[Error] Invalid URL format! Please enter a valid URL. Format: https://example.com")
        return

    choice = input("Use Requests or Selenium (r/s): ").strip().lower()

    if choice == "r":
        print("[Info] Using Requests and BeautifulSoup...")
        print("[Info] Fetching HTML content...")
        html = fetch_html(url)
        data = parse_html(html) if html else None
    elif choice == "s":
        print("[Info] Using Selenium...")
        print("[Info] Fetching HTML content...")
        data = scrape_with_selenium(url)
    else:
        print("[Error] Invalid choice. Please select 'r' or 's'.")
        return
    
    if data:
        print("\n[Info] Scraped Data:")
        print(f"Title: {data['title']}")
        print("Headers:")
        for header in data['headers']:
            print(f"- {header}")
    else:
        print("[Error] No data found or failed to scrape the page.")

def main():
    while True:
        try:
            print_feature_header("WEB Scraping")
            print("0. Get info about this feature")
            print("1. Start WEB Scraping")
            print("2. Return to Main Menu")
            print("3. Exit")
            print("----------------------------------")

            choice = input("Select an option (0-3): ").strip()
            
            if choice == "0":
                display_info()
            elif choice == "1":
                web_scraping()
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

if __name__ == "__main__":
    main()