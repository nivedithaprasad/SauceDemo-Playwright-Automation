import base64
import os
import re

import pytest
import pytest_html
from playwright.sync_api import Page

from config import AUTH_FILE, BASE_URL, INVENTORY_URL, PASSWORD, STANDARD_USER

SCREENSHOT_DIR = "screenshots"


# ======================================================================
# Setup: make sure output folders exist before the run starts
# ======================================================================
def pytest_configure(config):
    for folder in (SCREENSHOT_DIR, "reports", os.path.dirname(AUTH_FILE)):
        os.makedirs(folder, exist_ok=True)


# ======================================================================
# Session / authentication fixtures
# ======================================================================
@pytest.fixture(scope="session")
def auth_state(browser):
    # Runs ONCE per test run: logs in with a fresh context and saves the session
    # (cookies + localStorage) to a JSON file so other tests can reuse it.
    context = browser.new_context()
    page = context.new_page()

    page.goto(BASE_URL)
    page.fill("#user-name", STANDARD_USER)
    page.fill("#password", PASSWORD)
    page.click("#login-button")
    page.wait_for_url(INVENTORY_URL)  # make sure login really finished

    # Save the logged-in session to disk (auth storage) and also return it
    state = context.storage_state(path=AUTH_FILE)
    context.close()
    return state


@pytest.fixture
def logged_in_page(browser, auth_state):
    # Gives each test a NEW context pre-loaded with the saved session,
    # so the test starts already logged in on the inventory page (no login steps).
    context = browser.new_context(storage_state=auth_state)
    page = context.new_page()
    page.goto(INVENTORY_URL)
    yield page
    context.close()  # cleanup after the test (and after the report hook ran)


@pytest.fixture
def guest_page(browser):
    # Gives each test a clean, NOT logged-in page opened on the login screen.
    # Used for login / negative login tests.
    context = browser.new_context()
    page = context.new_page()
    page.goto(BASE_URL)
    yield page
    context.close()


# ======================================================================
# Screenshot + consolidated HTML report
# ======================================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Runs after every test phase. We let pytest build the report first,
    # then add a screenshot of the browser to it.
    outcome = yield
    report = outcome.get_result()

    # Only the "call" phase is the actual test body (not setup/teardown)
    if report.when != "call":
        return

    # Find whichever Playwright page the test used (logged_in_page or guest_page)
    page = next((v for v in item.funcargs.values() if isinstance(v, Page)), None)
    if page is None:
        return

    # Clean test name so parametrized names like test[a-b] make a valid filename
    safe_name = re.sub(r"[^\w\-]", "_", item.name)
    status = "PASS" if report.passed else "FAIL"
    path = os.path.join(SCREENSHOT_DIR, f"{safe_name}_{status}.png")

    try:
        page.screenshot(path=path)  # saved for every test (pass or fail)

        # Embed the image into the HTML report as base64 so the report is a single file
        with open(path, "rb") as img:
            encoded = base64.b64encode(img.read()).decode("utf-8")
        extras = getattr(report, "extras", [])
        extras.append(pytest_html.extras.image(encoded, mime_type="image/png"))
        report.extras = extras
    except Exception as err:
        print(f"Could not capture screenshot for {item.name}: {err}")
