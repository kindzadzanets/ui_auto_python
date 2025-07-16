# Импортируем синхронный API Playwright — основной инструмент для работы с браузером
from playwright.sync_api import sync_playwright


# -------------------- ПЕРВЫЙ ЗАПУСК: регистрация и сохранение состояния --------------------
with sync_playwright() as p:  # Контекстный менеджер: гарантирует, что браузер закроется даже при ошибках
    browser = p.firefox.launch(headless=False)  
    # Запускаем браузер Firefox в видимом режиме (headless=False значит НЕ безголовый режим)

    context = browser.new_context()  
    # Создаем новый контекст браузера — как отдельный чистый профиль без куков и данных

    page = context.new_page()  
    # Открываем новую вкладку (Page) в этом контексте

    # Переходим на страницу регистрации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"
    )

    # Ищем элементы формы по data-testid и другим локаторам:
    email = page.get_by_test_id("registration-form-email-input").locator("input")  
    # Находим контейнер с data-testid и уточняем, что нужен именно <input> внутри него
    username = page.get_by_test_id("registration-form-username-input").locator("input")
    password = page.locator('//input[@type="password"]')  
    # XPath локатор для поиска поля пароля
    button = page.get_by_test_id("registration-page-registration-button")  
    # Находим кнопку отправки формы регистрации

    # Вводим тестовые данные в поля формы
    email.fill("vaflia@gmai.com")
    username.fill("vaflia")
    password.fill("kal")

    # Кликаем по кнопке регистрации, отправляем форму
    button.click()

    # Сохраняем состояние контекста (cookies, localStorage, sessionStorage) в JSON-файл
    # Теперь в этом файле хранится авторизованная сессия
    context.storage_state(path="browser_state.json")

    # Ждём 5 секунд, чтобы визуально увидеть результат (не обязательно для автотеста)
    page.wait_for_timeout(5000)


# -------------------- ВТОРОЙ ЗАПУСК: открытие с сохранённой сессией --------------------
with sync_playwright() as p:  # Новый запуск Playwright
    browser = p.firefox.launch(headless=False)  
    # Снова запускаем браузер Firefox в видимом режиме

    context = browser.new_context(storage_state='browser_state.json')  
    # Создаем новый контекст, но теперь загружаем состояние из файла browser_state.json
    # Это значит, что мы сразу входим как авторизованный пользователь, без повторного логина

    page = context.new_page()  
    # Открываем новую вкладку с уже загруженным состоянием

    # Переходим на страницу дашборда, доступную только после авторизации
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"
    )

    # Ждём 5 секунд, чтобы убедиться, что страница открыта (например, увидеть её глазами)
    page.wait_for_timeout(5000)
