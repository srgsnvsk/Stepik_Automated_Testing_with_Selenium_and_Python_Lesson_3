# теория
# перезапуск упавших тестов с помощью плагина pytest-rerunfailures
# плагин перезапускает упавшие тесты нужное количество раз
# `--reruns n`, где n количество перезапусков
# `--tb=line` - сократить результат лога теста
# запуск тестов в консоли:
# chrome: `cd lesson3\lesson3_8 && pytest -s --tb=line --reruns 1 --browser_name_lesson3_8=chrome test_parser_lesson3_8.py`
# firefox: `cd lesson3\lesson3_8 && pytest -s --tb=line --reruns 1 --browser_name_lesson3_8=firefox test_parser_lesson3_8.py`
# для запуска тестов с помощью Testing:
# в файле settings.json (лежит в папке .vscode\settings.json) раскоментировать нужную строку
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

# тест который падает
def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#magic_link")