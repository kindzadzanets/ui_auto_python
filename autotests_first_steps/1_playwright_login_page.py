from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p: # команда python (with), предназначенная для работы с контекстным менеджером*
    # эта команда открывает что-то: браузер, файл и т.д. и гарантирует, 
    # что это будет закрыто корректно даже при возникновении ошибки. 
    # Далее - функция, запускающая плейрайт, т.е. возвращающая объект - контекстный менеджер*, который сохраняется в переменную "р"
    chromium = p.chromium.launch(headless=False) # запуск функции launch с аргументом headless=False для объекта chromium, 
    # который является атрибутом для объекта р.
    # headless - означает "запустить в памяти машины" - без UI. короче говоря был создан объект chromi - браузер, который вернулся в методе лаунч
    page = chromium.new_page() # создание объекта новой страницы в браузере, которая вернулась в методе new_page
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login") # вызов метода goto и передача в него ссылки

    email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input') # создание обекта поля имеил, 
    # который возвращает метод .locator(...) по указанному локатору(пути), на созданном ранее по ссылке объекте страницы
    email_input.fill("agapramon@gmail.com") # вызов метода .fill(...), который принимает текст и вставляет его в окно

    password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill("123321")

    button = page.locator('//*[@id="login-page-login-button"]')
    button.click()

    alert = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]//div[@class="MuiAlert-message css-1xsto0d"]')
    
    expect(alert).to_be_visible() # expect принимает alert в качестве аргумента, созданный по локатору объект и проверяет его состояние указанным методом .to_be_visible()
    # "ожидаю, что объект страницы - видимый"
    expect(alert).to_have_text("Wrong email or password") # ещё один метод объекта возвращаемого expect(...), который проверяет содержащийся в нём текст.

    page.wait_for_timeout(5000) # задан таймаут для страницы, чтобы просто она не закрылась сразу после вставки. ДЛЯ ТРЕНЕРОВКИ


# data-testid - специальный атрибут, присваиваемый к элементам в html для их локации в playwright.
# это создаёт идеальные условия для создания объектов на основе уникальных локаторов, на которые не повлияет изменение других атрибутув.
# НАПРИМЕР:

with sync_playwright() as p:
    chromium = p.chromium.launch(headless=False)
    page = chromium.new_page()
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login") 

    email_input = page.get_by_test_id('login-form-email-input').locator('input') # в метод get_by_test_id было передано занчение параметра data-testid со страницы. 
    # В данном случае, этот атрибут есть только у контейнера, поэтому добавлен метод locator, в который передаётся необходимый в контейнере элемент ("input")
    email_input.fill("agapramon@gmail.com")
    password_input = page.get_by_test_id('login-form-password-input').locator('input') # тот же случай, что и с логином. Стоит добавить, что вместо "input", 
    # в аргумент можно указать остаток пути xpath к нужному элементу.
    password_input.fill("123321")
    button = page.get_by_test_id('login-page-login-button') # здесь - data-testid был присвоен непосредственно кнопке, так-что дополнительных манипуляций не надо
    button.click()

    alert = page.get_by_test_id('login-page-wrong-email-or-password-alert') # так же как и с кнопкой
        
    expect(alert).to_be_visible()
    expect(alert).to_have_text("Wrong email or password!") # сделано намеренно для демонстрации ошибки
    page.wait_for_timeout(5000)

    # УМОЛЯЙ РАЗРАБОВ ДОБАВИТЬ ТЕБЕ АТРИБУТ data-testid КО ВСЕМ ЭЛЕМЕНТАМ ИЛИ ВЫПРОСИ ПРАВО ДЕЛАТЬ ЭТО САМОСТОЯТЕЛЬНО И БУДЕТ СЧАСТЬЕ!