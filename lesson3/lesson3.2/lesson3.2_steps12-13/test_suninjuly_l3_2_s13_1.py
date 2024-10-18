# решение задачи
# вариант №1

import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class SunInJuly(unittest.TestCase):
    def test_reg1(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element(
            By.CSS_SELECTOR,
            "input.form-control.first[placeholder='Input your first name']",
        ).send_keys("Ivan")
        browser.find_element(
            By.CSS_SELECTOR,
            "input.form-control.second[placeholder='Input your last name']",
        ).send_keys("Petrov")
        browser.find_element(
            By.CSS_SELECTOR, "input.form-control.third[placeholder='Input your email']"
        ).send_keys("example@example.com")
        browser.find_element(
            By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your phone:']"
        ).send_keys("8-800-555-55-55")
        browser.find_element(
            By.CSS_SELECTOR,
            "input.form-control.second[placeholder='Input your address:']",
        ).send_keys("Kursk")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            welcome_text,
            welcome_text_elt.text,
            "Congratulations! You have successfully registered!",
        )

    def test_reg2(self):
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element(
            By.CSS_SELECTOR,
            "input.form-control.first[placeholder='Input your first name']",
        ).send_keys("Ivan")
        browser.find_element(
            By.CSS_SELECTOR,
            "input.form-control.second[placeholder='Input your last name']",
        ).send_keys("Petrov")
        browser.find_element(
            By.CSS_SELECTOR, "input.form-control.third[placeholder='Input your email']"
        ).send_keys("example@example.com")
        browser.find_element(
            By.CSS_SELECTOR, "input.form-control.first[placeholder='Input your phone:']"
        ).send_keys("8-800-555-55-55")
        browser.find_element(
            By.CSS_SELECTOR,
            "input.form-control.second[placeholder='Input your address:']",
        ).send_keys("Kursk")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            welcome_text,
            welcome_text_elt.text,
            "Congratulations! You have successfully registered!",
        )


if __name__ == "__main__":
    unittest.main()
