def test_user_login():
    print("Hello!")


class TestUserLogin: # ! конструкция необходимая для распознавания класса в pytest: Test* !
    # !!! тестовый класс не может иметь и использовать __init__(self) конструктор класса - pytest их не запустит !!!
    
    def test_1(self): # ! конструкция необходимая для распознавания метода в pytest: test_* !
        pass

    def test_2(self):
        pass

def test_assert_positive():
    assert (2 + 2) == 4

def test_assert_negative():
    assert (2 - 2) == 4, "2 - 2 = 0 !"

# в терминале: python -m pytest - запуск тестов, 
# можно добавить флаг: -s - для перехвата вывода функции в терминал.
#                    : -v - verbous - более развёрнутая информация.
#                    : -k "test_name or test_2" - выполнить конкретный тест и/или тесты по имени/части имени теста или тестового класса


# assert - конструкция для проверки условия, он молчит, если условие True, 
# если False - покажет ошибку AssertionError
# в assert можно добавить сообщение. пример: assert 2 > 4, "два не может быть больше четырёх!"
# при выполнении, сообщение будет добалено после ошибки: AssertionError: два не может быть больше четырёх!
# в условия assert можно добавить для сравнения любые данные: assert 'mama' == 'mama' и т.п.

