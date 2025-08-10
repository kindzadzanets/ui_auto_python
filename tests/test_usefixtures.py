import pytest

# для использования сервисных фикстур - не возвращающих данные, в определённых кейсах(когда автовыполнение не подходит(autouse=False)),
# используется маркер @pytest.mark.usefixtures("[fixture]")

@pytest.fixture(scope="function") # пример сервисной фикстуры для отчистки БД
def clear_books_from_db():
    print("[Fixture]: удалить все книги из базы")


@pytest.fixture # пример фикстуры, заполняющей БД всеми исходными данными
def fill_db_with_books():
    print("[Fixture]: Добавить все книги в БД")


@pytest.mark.usefixtures("clear_books_from_db") # пример использования сервисной фикстуры в тесте при помощи маркера .usefixtures
def test_read_all_books_from_library(): # то есть, перед выполнением теста будет применена фикстура отчищающая БД
    print("Чтение всех книг.")


@pytest.mark.usefixtures("clear_books_from_db", "fill_db_with_books") # перед выполнением КАЖДОГО(default scope="function") теста этого класса будет отчищена, а затем заполнена БД
class TestLibrary:
    def test_read_book_from_lib():
        pass

    def test_delete_book_from_lib():
        pass
