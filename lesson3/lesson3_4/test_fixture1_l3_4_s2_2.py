# теория c объяснениями
# запуск теста pytest -s test__fixture1_l3_4_s2.py

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1:

    # декоратор указывает, что метод относится к классу
    @classmethod
    # метод запускается один раз до всех тестов в классе
    def setup_class(self):
        print("\n\033[34mstart browser for test suite 1 ..\033[0m")
        # запуск браузера
        self.browser = webdriver.Chrome()

    @classmethod
    # метод запускается после выполнения всех тестов в классе
    def teardown_class(self):
        print("\n\033[34mquit browser for test suite 1 ..\033[0m")
        # закрытие браузера
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2:

    # метод запускается перед каждым тестом
    def setup_method(self):
        print("\n\033[34mstart browser for test 2 ..\033[0m")
        self.browser = webdriver.Chrome()

    # метод запускается после каждого теста
    def teardown_method(self):
        print("\n\033[34mquit browser for test 2 ..\033[0m")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
