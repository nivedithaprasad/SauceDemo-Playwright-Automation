from pages.base_page import BasePage


class InventoryPage(BasePage):
    # Page object for the Products (inventory) page, including header and side menu

    # ---------- Locators ----------
    TITLE = ".title"
    ITEMS = ".inventory_item"
    ITEM_NAMES = ".inventory_item_name"
    CART_ICON = ".shopping_cart_link"
    CART_BADGE = ".shopping_cart_badge"
    MENU_BTN = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    # ---------- Helpers to build product-specific locators ----------
    @staticmethod
    def _add_btn(product_id: str) -> str:
        return f"#add-to-cart-{product_id}"

    @staticmethod
    def _remove_btn(product_id: str) -> str:
        return f"#remove-{product_id}"

    # ---------- Actions ----------
    def get_title_text(self) -> str:
        # Heading of the page (expected: "Products")
        return self.page.inner_text(self.TITLE)

    def get_product_count(self) -> int:
        # Number of products listed on the page
        return self.page.locator(self.ITEMS).count()

    def is_cart_icon_visible(self) -> bool:
        # Check that the cart icon in the header is displayed
        return self.page.is_visible(self.CART_ICON)

    def add_product_to_cart(self, product_id: str):
        # Click "Add to cart" for the given product
        self.page.click(self._add_btn(product_id))

    def is_remove_button_visible(self, product_id: str) -> bool:
        # After adding, the button changes to "Remove"
        return self.page.is_visible(self._remove_btn(product_id))

    def get_cart_count(self) -> str:
        # Number shown on the cart badge ("" if the cart is empty)
        if self.page.is_visible(self.CART_BADGE):
            return self.page.inner_text(self.CART_BADGE)
        return ""

    def open_product_details(self, product_name: str):
        # Click a product name to open its details page
        self.page.click(f"{self.ITEM_NAMES}:text-is('{product_name}')")

    def open_cart(self):
        # Click the cart icon to go to the cart page
        self.page.click(self.CART_ICON)

    def logout(self):
        # Open the side menu and click Logout
        self.page.click(self.MENU_BTN)
        self.page.click(self.LOGOUT_LINK)
