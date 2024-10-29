# теория
# тест с маркировкой
# маркировки не зарегистрированы в pytest.ini, отобразится warning
# запуск теста с маркировкой smoke pytest -s -v -m test_fixture8_l3_5_s2_2.py

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
    # маркировка smoke
    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # маркировка regression
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
