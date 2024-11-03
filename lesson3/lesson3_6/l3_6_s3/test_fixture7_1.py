# теория
# параметризация
# параметризация позволяет запустить один тест с разыми параметрами
# запуск файла pytest -s -v test_fixture7_1.py

import pytest
from selenium.webdriver.common.by import By


# тест запустится для друх версий сайта - на русском и английском
@pytest.mark.parametrize("language", ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
