import requests
from bs4 import BeautifulSoup


url = "https://adamowada.github.io/scrape-demo/"
response = requests.get(url)

# print(response.content)

# 1. Go to target website
# 2. Find content you WANT to scrape
# 3. Trial and error to target the content

# Target the h1 element's text

soup = BeautifulSoup(response.content, "html.parser")

print(type(soup))
print(soup)
