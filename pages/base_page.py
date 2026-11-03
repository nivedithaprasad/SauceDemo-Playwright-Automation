from playwright.sync_api import Page


class BasePage:
    # Parent class: holds the Playwright page and helpers shared by all page objects

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        # Navigate to the given URL
        self.page.goto(url)

    def get_url(self) -> str:
        # Return the current browser URL
        return self.page.url

    def get_title(self) -> str:
        # Return the page title shown in the browser tab
        return self.page.title()
