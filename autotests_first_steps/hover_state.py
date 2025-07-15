from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
              wait_until='networkidle')
    
    reg_link = page.get_by_test_id('login-page-registration-link')
    reg_link.hover()

    page.wait_for_timeout(5000)
 
