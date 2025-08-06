import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.regression
@pytest.mark.signin
def test_successful_registration():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(
            "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
            wait_until="networkidle",
        )

        email_input = page.get_by_test_id("registration-form-email-input").locator(
            "input"
        )
        username_input = page.get_by_test_id(
            "registration-form-username-input"
        ).locator("input")
        password_input = page.locator('//input[@type="password"]')
        submit_button = page.get_by_test_id("registration-page-registration-button")

        email_input.fill("mail.gmail.com")
        username_input.fill("kisa")
        password_input.fill("password")
        submit_button.click()

        context.storage_state(path="user_authorization.json")
        page.wait_for_timeout(5000)
        # expect(page).to_have_url('')

