from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    fox = p.firefox.launch(headless=False) # создать экземпляр браузера
    page = fox.new_page() # создать экземпляр страницы
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login') # отправить страницу по урлу

    login_button = page.get_by_test_id('login-page-login-button') # создать экземпляр элемента "кнопка" по data_testid
    # expect(login_button).to_be_disabled() # ожидание, что кнопка залочена.
    expect(login_button).not_to_be_disabled() # ожидание, что кнопка не будет залочена(disabled). Но она залочена и будет ошибка.

    page.wait_for_timeout(4000) # таймаут выхода, чтобы мне можно было посмотреть. Для реальных тестов этого делать не надо.
    


