from config import PRODUCT_BUTTON_ID, PRODUCT_NAME
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


# TC07: Verify that the Cart icon is displayed
def test_cart_icon_is_displayed(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    assert inventory.is_cart_icon_visible()
    assert inventory.get_cart_count() == ""


# TC08: Verify that a product can be added to the cart
def test_add_product_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    inventory.add_product_to_cart(PRODUCT_BUTTON_ID)

    assert inventory.is_remove_button_visible(PRODUCT_BUTTON_ID)
    assert inventory.get_cart_count() == "1"


# TC09: Verify that clicking the Cart icon opens the Cart page
def test_cart_icon_navigates_to_cart_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)

    inventory.add_product_to_cart(PRODUCT_BUTTON_ID)
    inventory.open_cart()

    assert "cart.html" in cart.get_url()
    assert cart.get_title_text() == "Your Cart"
    assert cart.get_item_count() == 1
    assert PRODUCT_NAME in cart.get_item_names()


# TC10: Verify that the Checkout button navigates to Checkout
def test_checkout_button_navigates_to_checkout_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    cart = CartPage(logged_in_page)
    checkout = CheckoutPage(logged_in_page)

    inventory.add_product_to_cart(PRODUCT_BUTTON_ID)
    inventory.open_cart()
    cart.click_checkout()

    assert "checkout-step-one.html" in checkout.get_url()
    assert checkout.get_title_text() == "Checkout: Your Information"
    assert checkout.are_form_fields_visible()
