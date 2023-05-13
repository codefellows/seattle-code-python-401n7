import requests


url = "https://adamowada.github.io/scrape-demo/"
response = requests.get(url)

print(response.content)
