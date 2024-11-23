# очистка данных
# выполнять перед запуском теста test_l3_6_s5.py
# код улучшен добавлением visibility_of_element_located

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestClearData:

    @pytest.mark.parametrize("lesson_id", [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
    def test_clear_form(self, browser, load_config, lesson_id):
        
        def wait(by_locator, condition=EC.element_to_be_clickable):
            element = WebDriverWait(browser, 60).until(condition(by_locator))
            return element
        
        link = f"https://stepik.org/lesson/{lesson_id}/step/1"
        email_text = load_config["login_stepik"]
        password_text = load_config["password_stepik"]
        browser.get(link)

        wait((By.CSS_SELECTOR, "a.navbar__auth_login")).click()
        wait((By.CSS_SELECTOR, "#id_login_email")).send_keys(email_text)
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys(password_text)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()
        success_element = wait((By.CSS_SELECTOR, ".navbar__profile-img"))
        assert success_element, "Не удалось войти: изображение профиля не найдено, возможно, не произошла авторизация."
        print("Пользователь авторизован")
        
        textarea = wait((By.CSS_SELECTOR, ".ember-text-area.textarea.string-quiz__textarea"), EC.visibility_of_element_located)
        if not textarea.is_enabled():
            browser.find_element(By.CSS_SELECTOR, ".again-btn").click()
            wait((By.CSS_SELECTOR, "[class='ember-text-area ember-view textarea string-quiz__textarea']"))
            print("Форма ввода ответа очищена")
        else:
            print("Форму ввода ответа очищать не нужно")
        print("Урок готов к решению)")
