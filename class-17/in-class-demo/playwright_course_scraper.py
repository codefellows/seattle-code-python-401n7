from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def main():
    with sync_playwright() as playwright:
        # Open Chrome and navigate to my target page
        browser = playwright.chromium.launch(headless=False, slow_mo=3000)
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
        


        # Close my browser
        browser.close()


if __name__ == "__main__":
    main()
