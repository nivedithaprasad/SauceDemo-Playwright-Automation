<<<<<<< HEAD
# Sauce Demo – Playwright + Pytest (POM) Framework

## Setup
```
pip install -r requirements.txt
playwright install
```

## Run
```
pytest                      # headless, all 10 tests
pytest --headed             # watch the browser
pytest tests/test_05_invalid_login_fails.py   # single test
```

## Outputs
- `reports/report.html` – one consolidated report, screenshots embedded
- `screenshots/` – one PNG per test (`<test>_PASS.png` / `_FAIL.png`)
- `auth/auth_state.json` – saved login session (created automatically)

## Structure
- `pages/` – Page Objects (locators + actions only)
- `tests/` – 10 tests (scenario + assertions only)
- `conftest.py` – session login (auth storage), page fixtures, screenshot + report hook
- `config.py` – URLs, users, product data

## Fixtures
- `auth_state` (session) – logs in once, saves cookies/localStorage
- `logged_in_page` – new context loaded with saved session, already on Products page
- `guest_page` – clean, logged-out page on the login screen
=======
# SauceDemo-Playwright-Automation
Python Playwright Pytest Automation Framework
>>>>>>> 95bdb08a26c032db2a732a94981d0f9061caf2ee
