# теория
# conftest.py используется для хранения часто употребимых фикстур и хранения глобальных настроек
# в файл вынесена фикстура открытия и закрытия браузера

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
