# теория
# запуск тестов в консоли:
# chrome: pytest -s -v --browser_name_lesson3_8=chrome test_parser.py
# firefox: pytest -s -v --browser_name_lesson3_8=firefox test_parser.py
# для запуска тестов с помощью Testing:
# в файле settings.json (лежит в папке .vscode\settings.json) раскоментировать нужную строку
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")