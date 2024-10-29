# теория
# тест с маркировкой
# запуск теста с маркировками smoke и regression pytest -s -v -m "smoke or regression" test_fixture8_l3_5_s3.py
# выполнятся тесты test_guest_should_see_login_link, test_guest_should_see_basket_link_on_the_main_page, test_guest_should_see_basket_link_on_the_main_page_regression
# запуск теста с маркировками smoke и win10 pytest -s -v -m "smoke and win10" test_fixture8_l3_5_s3.py
#  выполнится тест test_guest_should_see_basket_link_on_the_main_page


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

    # маркировка smoke
    # маркировка win10
    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    # маркировка regression
    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page_regression(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
