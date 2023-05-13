from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def main():
    with sync_playwright() as playwright:
        # Open Chrome and navigate to my target page
        browser = playwright.chromium.launch(headless=False, slow_mo=2000)
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org/")  # this is where I put my URL

        # Do stuff
        page.get_by_text("Course Calendar").click()
        page.click(f"text=400: Advanced")

        # Close my browser
        browser.close()


if __name__ == "__main__":
    main()
