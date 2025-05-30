# теория
# передача параметров в командной строке
# передача браузеров в командной строке
import pytest
from selenium import webdriver

# добавляет пользовательскую опцию командной строки
def pytest_addoption(parser):
    parser.addoption('--browser_name_lesson3_7', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name_lesson3_7 = request.config.getoption("browser_name_lesson3_7") # извлекает значение --browser_name_lesson3_7 переданное в командной строке
    browser = None
    if browser_name_lesson3_7 == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name_lesson3_7 == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name_lesson3_7 should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()