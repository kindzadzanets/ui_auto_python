from playwright.sync_api import sync_playwright, expect, Request, Response

def log_request(request: Request): # объявление функции- обработчика события (callback). 
    # Эта функция передаётся в качестве аргумента (без вызова) и библиотека сама вызовет её в нужный момент.
    # request: Request - означает, что параметр request ожидает объект класса Request в качестве аргумента. 
    # Это называется: анотация, используется для читаемости кода и постановки ide в известность о том-что какой тип будет передан в аргументе, 
    # в данном случае: объект класса Request. Благодаря анотации ide предложила атрибуты типа .url , .method ниже
    # Анотация абсолютно не влияет на поведение функции.
    print(f'Request: {request.url}, {request.method}')

def log_response(response: Response):
    print(f'Response: {response.url} {response.status}')




with sync_playwright() as p:
    browser_c = p.chromium.launch(headless=False)
    auth_page = browser_c.new_page()
    auth_page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    auth_page.on('request', log_request) # метод .on("имя_события", обработчик) - подписывает на события страницы.
    # "имя_события" – строка, название события, которое необходимо слушать ("response", "console", "dialog", "load", "domcontentloaded")
    # обработчик – объявленная выше функция, которую Playwright будет вызывать, когда событие произойдёт.
    # целиком это будет так: playwright будет слушать событие "request" и в случае его появления, вызовет мой обработчик, 
    # который выведет в консоль урл запроса и метод.
    
    
    auth_page.remove_listener('request', log_request) # .remove_listener("имя_события", обработчик) отключает обработчик. 
    # А .once() , например, позволяет обработать событие только один раз.
    auth_page.on('response', log_response) # playwright будет слушать событие "response" и в случае его появления, вызовет мой обработчик, 
    # который выведет в консоль урл ответа и его статус.


    auth_page.wait_for_timeout(5000)

