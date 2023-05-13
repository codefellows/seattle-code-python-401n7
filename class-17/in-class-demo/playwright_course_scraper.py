from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def main():
    with sync_playwright() as playwright:
        # Open Chrome and navigate to my target page
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org/")  # this is where I put my URL

        # Do stuff
        page.get_by_text("Course Calendar").click()
        page.click("//label[text() = '400: Advanced']")

        courses = {
            "java": "Code 401: Java",
            "javascript": "Code 401: JavaScript",
            ".net": "Code 401: ASP.NET",
            "python": "Code 401: Python",
            "cybersecurity": "Ops 401: Cybersecurity",
        }

        course_key = "python"  # which course do I WANT to see

        for course in courses:
            if course != course_key:  # then I want to click it
                page.click(f"//label[text() = '{courses[course]}']")

        soup = BeautifulSoup(page.content(), "html.parser")

        course_results = soup.find_all(class_="calendar-event")

        schedule = "Course Info:\n\n"

        for course in course_results:
            schedule += course.h2.text + "\n"
            schedule += course.h1.text + "\n"
            schedule += "\n"

        with open("courses.txt", "w") as file:
            file.write(schedule)

        # Close my browser
        browser.close()


if __name__ == "__main__":
    main()
