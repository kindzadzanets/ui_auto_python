# маркировка - один из готовых функций-декораторов в пайтест
# для структуризации тестов используются "кастомные маркировки" - эндпоинты после .mark., которые неизвестны библиотеке пайтест.
# любой неизвестный эндпоинт, стоящий после @pytest.mark. (например, @pytest.mark.[name]) будет определён как маркер для группы тестов.
import pytest

@pytest.mark.smoke # макркер - smoke, присвоен отдельной тестовой функции
def test_smoke_case():
    pass

@pytest.mark.regression
def test_regression_case():
    pass



@pytest.mark.smoke # маркер smoke присвоен всему тестовому классу, 
# это значит, что при вызове этого маркера, будут вызваны и все тестовые методы этого класса.
class TestSuite:
    def test_case_1(self): # тоже самое, что если бы на каждом методе класса стоял декоратор @pytest.mark.smoke
        pass
    
    def test_case_2(self):
        pass


@pytest.mark.ui # декоратор класса - маркер: ui
class TestUserAuthentification:

    @pytest.mark.smoke # декоратор метода - маркер smoke. 
    # Это значит, что данный метод имеет три маркера: ui, smoke, critical.
    # и этот тест будет запущен при вызове любого из его маркеров.
    @pytest.mark.critical
    def test_login(self):
        pass
    
    @pytest.mark.smoke
    def test_logout(self):
        pass

    @pytest.mark.slow # а этот метод имеет два маркера: ui(от класса) и slow(собственный маркер метода)
    def test_pass_reset(self):
        pass



# отдельные тестовые функции тоже могут иметь несколько маркеров
# и также будут запущены при вызове любого или нескольких из них.
@pytest.mark.smoke 
@pytest.mark.regression
@pytest.mark.critical
def test_regression_smoke_critical_case():
    pass


# pytest -svm "smoke and not regression" - пример инмтрукции для выполнения тестов, имеющих маркировку smoke, но НЕ имеющих также маркировки regressoin.
# pytest -svm "critical and regression" - только тесты, отмеченные как critical и regression одновременно.
# pytest -svm "login or critical" - все тесты, имеющие хотя бы один маркер: login или critical

#  -s - Разрешает прямой вывод в консоль — отладка, логирование, интерактивный ввод(например, input()) 
# Без -s: Pytest захватывает вывод, и ты не увидишь результат print() в терминале, пока тест не упадёт или не завершится.
#  -v - Вывод подробный — имя файла, имя функции. Используется всегда в автотестах для точного отслеживания, какие именно тесты запускаются
#  -m - Фильтрует тесты по маркеру. Запускает только те, что помечены @pytest.mark.<name>
# используется для частичный прогон (например, только smoke или critical), в CI/CD пайплайнах, при локальной проверке одного блока тестов


# для НЕЗАРЕГЕСТРИРОВАННЫХ маркировок при запуске тестов всегда появляется ворнинг: 
# PytestUnknownMarkWarning: Unknown pytest.mark.regression - is this a typo? You can register custom marks to avoid this warning
# его необходимо исключить с помощью регистрации каждого используемого маркера в файле pytest.ini