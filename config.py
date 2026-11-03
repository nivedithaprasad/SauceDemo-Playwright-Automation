# Central place for URLs and test data so tests don't hard-code them

BASE_URL = "https://www.saucedemo.com/"
INVENTORY_URL = BASE_URL + "inventory.html"

# Where the saved login session (cookies + localStorage) is stored
AUTH_FILE = "auth/auth_state.json"

# Valid and special users provided by Sauce Demo
STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"

# Product used in the cart / checkout tests
PRODUCT_NAME = "Sauce Labs Backpack"
PRODUCT_BUTTON_ID = "sauce-labs-backpack"  # used to build add-to-cart / remove ids
