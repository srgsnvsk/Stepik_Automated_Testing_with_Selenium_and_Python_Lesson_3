# решение задачи
# с комментариями
# запуск теста pytest -s -v test_l3_6_s5.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# from conftest import final


class TestParameterization:

    @pytest.mark.parametrize("lesson_id", [236898, 236899])
    # "lesson_id", [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905]
    def test_send_answer(self, browser, load_config, lesson_id):
        link = f"https://stepik.org/lesson/{lesson_id}/step/1"

        email_text = load_config["login_stepik"]
        password_text = load_config["password_stepik"]

        browser.get(link)
        login_button = WebDriverWait(browser, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.navbar__auth_login"))
        )
        login_button.click()

        email = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#id_login_email"))
        )
        email.send_keys(email_text)
        password = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        password.send_keys(password_text)
        login = browser.find_element(
            By.CSS_SELECTOR, 'button[class="sign-form__btn button_with-loader "]'
        )
        login.click()

        success_element = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img"))
        )
        assert success_element is not None

        textarea = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "[class='ember-text-area ember-view textarea string-quiz__textarea']",
                )
            )
        )
        answer = math.log(int(time.time()))
        textarea.send_keys(answer)
        submit_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        submit_button.click()
        correct_element = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        )

        message_text = correct_element.text
        assert (
            "Correct!" in message_text
        ), f'Ответ неверный: "{message_text}", а должен быть "Correct!" '

        # if message_text != "Correct!":
        #     final.append(f"Lesson {lesson_id} - Message: {message_text}")
