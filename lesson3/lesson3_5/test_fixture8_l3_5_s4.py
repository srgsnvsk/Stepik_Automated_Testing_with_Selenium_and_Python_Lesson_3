# теория
# пропуск тестов
# запуск теста pytest -s -v test_fixture8_l3_5_s4.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\n\033[34mstart browser for test..\033[0m")
    browser = webdriver.Chrome()
    yield browser
    print("\n\033[34mquit browser..\033[0m")
    browser.quit()


class TestMainPage1:

    # тест test_guest_should_see_login_link будет пропущен, потому что для него стоит маркировка skip
    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
