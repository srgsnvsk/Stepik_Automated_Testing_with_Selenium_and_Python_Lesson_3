# решение задачи
# с комментариями
# запуск теста pytest -s -v test_l3_6_s4_1.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://stepik.org/catalog?auth=login"


class TestAuthLogin:

    def test_user_autorization(self, browser, load_config):
        # Загружаем логин и пароль из config.json
        email_text = load_config["login_stepik"]
        password_text = load_config["password_stepik"]

        browser.get(link)
        # явное ожидание
        # как только элемент загрузится, он сохранится в переменной email
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
                (By.CSS_SELECTOR, 'button[class="sign-form__btn button_with-loader "]')
            )
        )
        login.click()

        # Дополнительное ожидание для проверки успешного логина
        # Ожидаем элемент, который появляется после успешного логина
        success_element = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img"))
        )

        # Проверка, что логин был успешным (элемент присутствует на странице)
        assert success_element is not None

        # Можно добавить дополнительное ожидание на несколько секунд
        time.sleep(5)
