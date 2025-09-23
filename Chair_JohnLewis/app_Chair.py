# import requests library to call a webpage
import requests
# import beautifulsoup library to parse a webpage
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/john-lewis-dante-garden-lounging-armchair/p1653912")
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
