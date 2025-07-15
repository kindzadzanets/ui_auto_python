from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    safari = p.webkit.launch(headless=False)
    auth_page = safari.new_page()
    auth_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = auth_page.locator('//div[@data-testid="login-form-email-input"]/div/input')
    email_input.focus()
    
    for char in 'karL U Klary ukal 1234!@$ q  1234':
        auth_page.keyboard.type(char, delay=300)

    auth_page.keyboard.press('ControlOrMeta+A')

    auth_page.wait_for_timeout(4000)

