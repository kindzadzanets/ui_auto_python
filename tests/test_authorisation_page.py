import pytest
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.login
def test_unsuccessfull_authorization(chromium_page: Page):
    chromium_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    button = chromium_page.locator('//*[@type="button"]')

    email_input.fill('emai@mail.ru')
    password_input.fill('password')
    button.click()

    chromium_page.wait_for_timeout(10000)