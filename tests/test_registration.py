import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
    chromium_page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration",
        wait_until="networkidle",
    )

    email_input = chromium_page.get_by_test_id("registration-form-email-input").locator(
        "input"
    )
    username_input = chromium_page.get_by_test_id(
        "registration-form-username-input"
    ).locator("input")
    password_input = chromium_page.locator('//input[@type="password"]')
    submit_button = chromium_page.get_by_test_id(
        "registration-page-registration-button"
    )
    dushboard_title = chromium_page.get_by_test_id("dashboard-toolbar-title-text")

    email_input.fill("mail.gmail.com")
    username_input.fill("kisa")
    password_input.fill("password")
    submit_button.click()

    expect(chromium_page).to_have_url('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
    expect(dushboard_title).to_have_text("Dashboard")
    chromium_page.wait_for_timeout(5000)
    # expect(page).to_have_url('')
