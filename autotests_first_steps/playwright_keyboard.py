from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    safari = p.webkit.launch(headless=False)
    auth_page = safari.new_page()
    auth_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input = auth_page.locator('//div[@data-testid="login-form-email-input"]/div/input')
    email_input.focus() # фокус на поле, необходимое для действия. В данном случае, будет печать в инпут.
    
    for char in 'karL U Klary ukal 1234!@$ q  1234': # цикл, чтобы ввести какой-то текст по одному символу.
        auth_page.keyboard.type(char, delay=300) # есть для объекта страницы очень функциональный атрибут keyboard, 
        # который может осуществлять различные действия по эмуляции клавиатуры. 
        # Метод type(...) позволяет печатать в поле, а его параметр delay - задавать паузу после ввода содержимого первого аргумента

    auth_page.keyboard.press('ControlOrMeta+A') # press(...) эмулирует именно нажатие клавиши, 
    # в данном случае "cmd+a" - для выделения содержимого поля

    auth_page.wait_for_timeout(4000)

