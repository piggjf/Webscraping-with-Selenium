"""
# Filename: run_selenium.py
"""

## Run selenium and chrome driver to scrape data from cloudbytes.dev
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## Setup chrome options
chrome_options = Options()
chrome_options.add_argument("--headless") # Ensure GUI is off
chrome_options.add_argument("--no-sandbox")
print("Options set!")
# Set path to chromedriver as per your configuration
webdriver_service = Service("/home/jpigg/Projects/ThuVuWalkthru/chromedriver/stable/chromedriver")
print("Service ready...")
# Choose Chrome Browser
browser = webdriver.Chrome(service=webdriver_service, options=chrome_options)
print("Browser chosen...")
# Get page
browser.get("https://cloudbytes.dev")
print("Page retrieved")
# Extract description from page and print
description = browser.find_element(By.NAME, "description").get_attribute("content")
print("Extraction complete:")
print(f"{description}")

#Wait for 10 seconds
time.sleep(10)
browser.quit()