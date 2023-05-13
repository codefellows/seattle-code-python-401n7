import requests
from bs4 import BeautifulSoup


url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# course_results = soup.find_all(itemtype="http://schema.org/CourseInstance")
course_results = soup.find_all(class_="calendar-event")

for course in course_results:
    if "Python" in course.h1.text
