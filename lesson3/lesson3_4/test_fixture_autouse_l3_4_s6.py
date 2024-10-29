# теория
# автоиспользование фикстур
# запуск файла pytest -s -v test_fixture_autouse_l3_4_s6_1.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\n\033[34mstart browser for test..\033[0m")
    browser = webdriver.Chrome()
    yield browser
    print("\n\033[34mquit browser..\033[0m")
    browser.quit()


# автоиспользование фикстур применяется ко всем тестовым функциям в области видимости scope
# так как сейчас не задан scope, фикустура применяется ко всем функциям
@pytest.fixture(autouse=True)
def prepare_data():
    print("\033[33mpreparing some critical data for every test\033[0m")


class TestMainPage1:
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
