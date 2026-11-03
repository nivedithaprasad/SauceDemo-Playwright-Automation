from pages.base_page import BasePage


class ProductDetailsPage(BasePage):
    # Page object for a single product's details page

    # ---------- Locators ----------
    NAME = ".inventory_details_name"
    PRICE = ".inventory_details_price"
    DESCRIPTION = ".inventory_details_desc"
    BACK_BTN = "#back-to-products"

    # ---------- Actions ----------
    def get_name(self) -> str:
        # Product name shown on the details page
        return self.page.inner_text(self.NAME)

    def get_price(self) -> str:
        # Product price shown on the details page
        return self.page.inner_text(self.PRICE)

    def is_description_visible(self) -> bool:
        # Check that the product description is displayed
        return self.page.is_visible(self.DESCRIPTION)

    def is_back_button_visible(self) -> bool:
        # Check that the "Back to products" button is displayed
        return self.page.is_visible(self.BACK_BTN)
