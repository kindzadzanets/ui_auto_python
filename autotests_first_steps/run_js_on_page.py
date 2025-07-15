from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    mozila = p.firefox.launch(headless=False)
    page = mozila.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until="networkidle", # очень важный параметр wait_until, 
        # позволяющий дождаться полной или частичной загрузки страницы перед выполнением дальнейших действий.
        # возможные аргументы можно посмотреть внутри метода goto(...) (cmd+click)
    )

    text = "random text" # сохранил какой-то текст в переменную
    page.evaluate(
        f"""
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = '{text}';
"""
    ) # метод плейрайта evaluate(), позволяющий выполнить js код. 
      # По питонски передана переменная в js - через ф-строку.
      # 1е действие: сохранил в переменную title заголовок, найденный по id на странице
      # 2е действие: передал в заголовок текст из переменной методом textContent(...)

    page.wait_for_timeout(4000)



with sync_playwright() as p:
    mozila = p.firefox.launch(headless=False)
    page = mozila.new_page()
    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until="networkidle",
    )

    new_text = "random text"
    page.evaluate(
        """(text) => {
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = text}""",
        new_text,
    ) # можно сделать тоже самое, но только средствами js:
      # безымянная функция, которая принимает аргументом переменную new_text.

    page.wait_for_timeout(4000)
