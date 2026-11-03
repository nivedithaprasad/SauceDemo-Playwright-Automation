from config import PRODUCT_NAME
from pages.inventory_page import InventoryPage
from pages.product_details_page import ProductDetailsPage


# TC01: Verify that the Home/Products page loads successfully
def test_home_page_loads(logged_in_page):
    inventory = InventoryPage(logged_in_page)

    assert "inventory.html" in inventory.get_url()
    assert inventory.get_title_text() == "Products"
    assert inventory.get_product_count() == 6


# TC02: Verify that product details open when a product is selected
def test_product_details_page_opens(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    details = ProductDetailsPage(logged_in_page)

    inventory.open_product_details(PRODUCT_NAME)

    assert "inventory-item.html" in details.get_url()
    assert details.get_name() == PRODUCT_NAME
    assert details.get_price().startswith("$")
    assert details.is_description_visible()
    assert details.is_back_button_visible()
