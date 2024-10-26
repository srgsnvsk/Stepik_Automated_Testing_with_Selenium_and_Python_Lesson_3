# теория с объяснениями
# запуск файла pytest -s -v test_fixture3_l3_4_s4_2.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


# декоратор указывает, что функция browser является фикстурой
@pytest.fixture
# функция которая используется как фикстура
# запускает браузер перед тестом
def browser():
    print("\n\033[34mstart browser for test..\033[0m")
    browser = webdriver.Chrome()
    # ключевое слово yield - финализатор
    # финализаор выполнится даже если код упал с ошибкой
    yield browser
    # этот код выполнится после завершения теста
    print("\n\033[34mquit browser..\033[0m")
    browser.quit()


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
