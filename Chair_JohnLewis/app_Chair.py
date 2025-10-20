'''# import requests library to call a webpage
import requests
# import beautifulsoup library to parse a webpage
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-rowley-office-chair/p111535524")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("p", {"class": "price"})

# remove trailing spaces
string_price = element.text.strip()

# remove trailing symbol
price_without_symbol = string_price[1:]
price = float(price_without_symbol)

if price < 250:
    print("You can buy the chair.")
    print("Price of the chair is {}.".format(string_price))
else:
    print("Do not buy the chair.")


import requests
from bs4 import BeautifulSoup
import json

url = "https://www.johnlewis.com/john-lewis-rowley-office-chair/p111535524"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Fetch the page
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Find the JSON-LD script that contains product info
script_tag = soup.find("script", type="application/ld+json")

if script_tag:
    data = json.loads(script_tag.string)
    price = float(data["offers"]["price"])
    currency = data["offers"]["priceCurrency"]

    print(f"Price of the chair: {currency} {price}")

    if price < 250:
        print("✅ You can buy the chair.")
    else:
        print("❌ Do not buy the chair.")
else:
    print("Price information not found on the page.")

import requests
from bs4 import BeautifulSoup
import json

url = "https://www.johnlewis.com/john-lewis-rowley-office-chair/p111535524"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

try:
    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"❌ Connection failed: {e}")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = soup.find("script", type="application/ld+json")

    if script_tag:
        data = json.loads(script_tag.string)
        price = float(data["offers"]["price"])
        currency = data["offers"]["priceCurrency"]

        print(f"✅ Price of the chair: {currency} {price}")
        if price < 250:
            print("You can buy the chair.")
        else:
            print("Do not buy the chair.")
    else:
        print("Price information not found on the page.")'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Product page
url = "https://www.johnlewis.com/john-lewis-rowley-office-chair/p111535524"

# Set up Chrome in headless mode (no window)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    driver.get(url)

    # Wait for the price element to appear
    wait = WebDriverWait(driver, 15)
    price_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='product-price']"))
    )

    # Extract text (e.g., "£179.00")
    string_price = price_element.text.strip()
    print("Raw price text:", string_price)

    # Clean price (remove £ sign)
    price_value = float(string_price.replace("£", "").replace(",", ""))

    # Compare price
    if price_value < 250:
        print(f"✅ You can buy the chair. Price: £{price_value}")
    else:
        print(f"❌ Do not buy the chair. Price: £{price_value}")

except Exception as e:
    print(f"⚠️ Error: {e}")
finally:
    driver.quit()


