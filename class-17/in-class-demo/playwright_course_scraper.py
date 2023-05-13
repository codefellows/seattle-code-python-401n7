from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup


def main():
    with sync_playwright() as playwright:
        # Open Chrome and navigate to my target page
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto("")  # this is where I put my URL


if __name__ == "__main__":
    main()
