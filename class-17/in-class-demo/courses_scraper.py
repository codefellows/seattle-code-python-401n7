import requests
from bs4 import BeautifulSoup


url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

print(soup)
