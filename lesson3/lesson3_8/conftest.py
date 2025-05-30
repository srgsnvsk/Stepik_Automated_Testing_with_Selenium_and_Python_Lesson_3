# теория
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name_lesson3_8', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name_lesson3_8 = request.config.getoption("browser_name_lesson3_8") # извлекает значение --browser_name_lesson3_8 переданное в командной строке
    browser = None
    if browser_name_lesson3_8 == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name_lesson3_8 == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name_lesson3_8 should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()