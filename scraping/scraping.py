import os
from playwright.sync_api import sync_playwright


CHAPTER_URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1."

TEXT_OUTPUT_FILE = "scraping/chapter_1.txt"
IMAGE_OUTPUT_FILE = "scraping/chapter_1_image.png"


def scrape_chapter():
    with sync_playwright() as spw:
        browser = spw.chromium.launch(headless=True)
        new_page = browser.new_page()
        print(f"Loading: {CHAPTER_URL}...")
        new_page.goto(CHAPTER_URL)        
        new_page.wait_for_selector("div#bodyContent")        
        new_page.screenshot(path=IMAGE_OUTPUT_FILE, full_page=True)

        # Extracting the text content from the page.
        content = new_page.inner_text("div#bodyContent")
        
        os.makedirs(os.path.dirname(TEXT_OUTPUT_FILE), exist_ok=True)
        with open(TEXT_OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Chapter contents saved to:, {TEXT_OUTPUT_FILE}")

        browser.close()

if __name__ == "__main__":
    scrape_chapter()










