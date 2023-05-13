from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def main():
    with sync_playwright() as playwright:
        # Open Chrome and navigate to my target page
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto("https://testing-www.codefellows.org/")  # this is where I put my URL

        # Do stuff

        # Close my browser
        browser.close()


if __name__ == "__main__":
    main()
