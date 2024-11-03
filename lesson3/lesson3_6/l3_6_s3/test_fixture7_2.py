# теория
# параметризация
# параметризация можно применять к классу
# запуск файла pytest -s -v test_fixture7_2.py

import pytest
from selenium.webdriver.common.by import By


# тест запустится для друх версий сайта - на русском и английском для каждого теста в классе
@pytest.mark.parametrize("language", ["ru", "en-gb"])
class TestLogin:
    # этот тест запустится 2 раза
    def test_guest_should_see_login_link(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    # этот тест тоже запустится дважды
    def test_guest_should_see_basket_link_on_the_main_page(self, browser, language):
        link = f"http://selenium1py.pythonanywhere.com/{language}/"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
