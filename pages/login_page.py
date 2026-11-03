from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):
    # Page object for the Sauce Demo login screen

    # ---------- Locators ----------
    USERNAME = "#user-name"
    PASSWORD = "#password"
    LOGIN_BTN = "#login-button"
    ERROR_MSG = "[data-test='error']"
    LOGO = ".login_logo"

    # ---------- Actions ----------
    def open_login_page(self):
        # Open the login (landing) page
        self.open(BASE_URL)

    def login(self, username: str, password: str):
        # Fill the credentials and click Login
        self.page.fill(self.USERNAME, username)
        self.page.fill(self.PASSWORD, password)
        self.page.click(self.LOGIN_BTN)

    def get_error_message(self) -> str:
        # Read the red error banner text shown after a failed login
        return self.page.inner_text(self.ERROR_MSG)

    def is_login_form_visible(self) -> bool:
        # True only if username, password and login button are all displayed
        return (
            self.page.is_visible(self.USERNAME)
            and self.page.is_visible(self.PASSWORD)
            and self.page.is_visible(self.LOGIN_BTN)
        )

    def is_logo_visible(self) -> bool:
        # Check that the "Swag Labs" logo is displayed
        return self.page.is_visible(self.LOGO)
