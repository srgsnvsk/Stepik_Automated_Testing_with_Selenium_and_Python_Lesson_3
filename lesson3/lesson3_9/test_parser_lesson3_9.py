# теория

# запуск тестов в консоли:
# chrome: `cd lesson3\lesson3_9 && pytest -s --browser_name_lesson3_9=chrome --language=en test_parser_lesson3_9.py`
# firefox: `cd lesson3\lesson3_9 && pytest -s --browser_name_lesson3_9=firefox --language=en test_parser_lesson3_9.py`
# запуск теста без параметра `--language=en` запустит тест по умолчанию на русском
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
