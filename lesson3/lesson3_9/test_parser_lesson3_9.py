# теория

# запуск тестов в консоли:
# chrome: `cd lesson3\lesson3_8 && pytest -s --browser_name_lesson3_8=chrome test_parser_lesson3_9.py`
# firefox: `cd lesson3\lesson3_8 && pytest -s --browser_name_lesson3_8=firefox test_parser_lesson3_9.py`
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    time.sleep(3)
    browser.find_element(By.CSS_SELECTOR, "#login_link")
