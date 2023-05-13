import requests
from bs4 import BeautifulSoup


url = "https://testing-www.codefellows.org/course-calendar/?filters=400:%20Advanced,code-python-401"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# course_results = soup.find_all(itemtype="http://schema.org/CourseInstance")
course_results = soup.find_all(class_="calendar-event")

schedule = "Course Info:\n\n"

for course in course_results:
    if "Python" in course.h1.text:
        schedule += course.h2.text + "\n"
        schedule += course.h1.text + "\n"
        schedule += "\n"

with open("courses.txt", "w") as file:
    file.write(schedule)
