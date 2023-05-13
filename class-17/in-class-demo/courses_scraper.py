import requests
from bs4 import BeautifulSoup


url = "https://adamowada.github.io/scrape-demo/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
h1_result = soup.find("h1")

print(h1_result.text)
