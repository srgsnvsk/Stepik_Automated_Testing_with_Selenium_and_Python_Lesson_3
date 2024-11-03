# решение задачи
# запуск теста pytest -s -v test_l3_6_s4_2.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://stepik.org/catalog?auth=login"


class TestAuthLogin:

    def test_user_autorization(self, browser, load_config):

        email_text = load_config["login_stepik"]
        password_text = load_config["password_stepik"]

        browser.get(link)

        email = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
        )
        email.send_keys(email_text)

        password = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_password"))
        )
        password.send_keys(password_text)

        login = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    'button[class="sign-form__btn button_with-loader "]',
                )
            )
        )
        login.click()

        success_element = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img"))
        )

        assert success_element is not None

        time.sleep(2)
