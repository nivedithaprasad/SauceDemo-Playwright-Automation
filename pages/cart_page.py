
from pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):

    # ---------- Locators ----------
    TITLE = ".header_secondary_container .title"
    CART_ITEMS = ".cart_item"
    ITEM_NAMES = ".inventory_item_name"
    CHECKOUT_BTN = "#checkout"

    # ---------- Actions ----------
    def get_title_text(self) -> str:
        title = self.page.locator(self.TITLE)
        expect(title).to_have_text("Your Cart")
        return title.inner_text()

    def get_item_names(self) -> list:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def get_item_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def click_checkout(self):
        self.page.click(self.CHECKOUT_BTN)

