
from pages.base_page import BasePage
from playwright.sync_api import expect


class CheckoutPage(BasePage):

    # ---------- Locators ----------
    TITLE = ".header_secondary_container .title"
    FIRST_NAME = "#first-name"
    LAST_NAME = "#last-name"
    POSTAL_CODE = "#postal-code"
    CONTINUE_BTN = "#continue"

    # ---------- Actions ----------
    def get_title_text(self) -> str:
        title = self.page.locator(self.TITLE)
        expect(title).to_have_text("Checkout: Your Information")
        return title.inner_text()

    def are_form_fields_visible(self) -> bool:
        return all(
            self.page.is_visible(locator)
            for locator in (
                self.FIRST_NAME,
                self.LAST_NAME,
                self.POSTAL_CODE,
                self.CONTINUE_BTN
            )
        )
