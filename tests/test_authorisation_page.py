from playwright.sync_api import sync_playwright, expect

def test_unsuccessfull_authorization():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)
        page = browser.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

        email_input = page.get_by_test_id('login-form-email-input').locator('input')
        password_input = page.get_by_test_id('login-form-password-input').locator('input')
        button = page.locator('//*[@type="button"]')

        email_input.fill('emai@mail.ru')
        password_input.fill('password')
        button.click()

        page.wait_for_timeout(5000)

test_unsuccessfull_authorization()