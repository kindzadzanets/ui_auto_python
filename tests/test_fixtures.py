import pytest


# Фикстура в PyTest — это любая функция, помеченная декоратором @pytest.fixture, 
# которая выполняет предусловия и постусловия(если необходимы), 
# обеспечивая его нужными ресурсами (например, браузером, подключением к БД, тестовыми данными и т.д.).

@pytest.fixture(autouse=True) # параметр autouse позволяет автоматически вызывать функцию в пределах её scope.
# Если результат функции являет данные для теста, то фикстуру надо также передать в аргумент.
# ЕСЛИ ПАРАМЕТР scope не задан в фикстуре, то по-умолчанию это: scope="function".
def send_analiytics_data():
    print(
        "AUTOUSE - выполняется автоматически - без передачи в функцию, перед каждым тестом, так как по-умолчанию scope= 'function'"
    )


@pytest.fixture(scope="session") # параметр scope - задаёт частоту выполнения фикстуры.
# scope="session" - функция отработает 1 раз - в начале тестового прогона. (с yield - и по завершении прогона)
def settings():
    print("SESSION - Фикстура выполняется 1 раз за весь прогон(сессию)") 


@pytest.fixture(scope="class") # scope="class" - функция будет заново выполнена перед каждым тестовым классом (с yield - и по завершении всех тестов одного класса)
def user():
    print("CLASS - Выполняется для каждого тестового класса")


@pytest.fixture(scope="function") # scope="function" - выполнение фикстуры перед каждой тестовой функцией (с yield - и по завершении теста)
def browser():
    print(
        "FUNCTION - выполняется для каждой тестовой функции (дефолтное значение для параметра scope)"
    )

# ВАЖНО ПОНИМАТЬ, ЧТО scope - задаёт частоту выполнения функции - фикстуры, 
# но её результат передаётся в аргументах тестам(по необходимости). 
# например, settings() имеет scope="session" и будет вызвана всего 1 раз, 
# но её значение можно передавать в аргументе хоть каждого теста как: (settings,)
class TestUserFlow:
    def test_user_class_login(self, settings, user, browser):
        pass

    def test_user_can_create_course(self, settings, user, browser):
        pass


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        pass
