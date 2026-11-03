from config import LOCKED_USER, PASSWORD
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# TC03: Verify that the Login page opens successfully
def test_login_page_opens(guest_page):
    login = LoginPage(guest_page)

    assert login.get_title() == "Swag Labs"
    assert login.is_logo_visible()
    assert login.is_login_form_visible()


# TC04: Verify that a locked-out user cannot log in
def test_locked_out_user_cannot_login(guest_page):
    login = LoginPage(guest_page)

    login.login(LOCKED_USER, PASSWORD)

    assert "inventory.html" not in login.get_url()
    assert "locked out" in login.get_error_message().lower()


# TC05: Verify that login fails with invalid credentials
def test_login_fails_with_invalid_credentials(guest_page):
    login = LoginPage(guest_page)

    login.login("wrong_user", "wrong_password")

    assert "inventory.html" not in login.get_url()
    assert "do not match" in login.get_error_message().lower()


# TC06: Verify that the user can log out successfully
def test_user_can_logout(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    login = LoginPage(logged_in_page)

    inventory.logout()

    assert login.is_login_form_visible()
    assert "inventory.html" not in login.get_url()
