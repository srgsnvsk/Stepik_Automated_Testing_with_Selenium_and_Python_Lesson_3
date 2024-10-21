# решение задачи
# вариант №3

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class SunInJuly(unittest.TestCase):

    def setUp(self):
        # устанавливаем драйвер
        # Метод автоматически вызывается перед каждым тестовым методом в классе (т.е. перед каждым методом, название которого начинается с test_)
        self.browser = webdriver.Chrome()

    def tearDown(self):
        # закрываем браузер после каждого теста
        # Метод автоматически вызывается после каждого тестового метода
        self.browser.quit()

    def fill_form(self, browser):
        # заполняем поля формы
        browser.find_element(
            By.CSS_SELECTOR, "input.first[placeholder='Input your first name']"
        ).send_keys("Ivan")
        browser.find_element(
            By.CSS_SELECTOR, "input.second[placeholder='Input your last name']"
        ).send_keys("Petrov")
        browser.find_element(
            By.CSS_SELECTOR, "input.third[placeholder='Input your email']"
        ).send_keys("example@example.com")
        browser.find_element(
            By.CSS_SELECTOR, "input.first[placeholder='Input your phone:']"
        ).send_keys("8-800-555-55-55")
        browser.find_element(
            By.CSS_SELECTOR, "input.second[placeholder='Input your address:']"
        ).send_keys("Kursk")

    def reg_page(self, link):
        browser = self.browser
        browser.get(link)

        # заполняем форму
        self.fill_form(browser)

        # нажимаем кнопку
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # возвращаем текст успешной регистрации
        return browser.find_element(By.TAG_NAME, "h1").text

    def test_reg1(self):
        self.assertEqual(
            self.reg_page("http://suninjuly.github.io/registration1.html"),
            "Congratulations! You have successfully registered!",
            "Registration 1 failed",
        )

    def test_reg2(self):
        self.assertEqual(
            self.reg_page("http://suninjuly.github.io/registration2.html"),
            "Congratulations! You have successfully registered!",
            "Registration 2 failed",
        )


if __name__ == "__main__":
    unittest.main()
